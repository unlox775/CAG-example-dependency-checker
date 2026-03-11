#!/usr/bin/env python3
"""Standalone dependency documentation checker with an explicit CAG gate output."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, List, Set

try:
    import tomllib  # Python 3.11+
except ModuleNotFoundError:  # pragma: no cover
    import tomli as tomllib  # type: ignore

DEPENDENCY_LINE_RE = re.compile(r"^- \[[xX ]\] \*\*([^*]+)\*\*")
NECESSITY_RE = re.compile(
    r"\*\*Necessity\*\*:\s*\*\*(LOW|MEDIUM|HIGH|CRITICAL)\*\*",
    re.IGNORECASE,
)
NAME_RE = re.compile(r"^[A-Za-z0-9_.-]+")
MANIFEST_TYPES = ("ruby", "javascript", "python")


@dataclass(frozen=True)
class DocumentedDependency:
    file_path: Path
    has_necessity: bool
    severity: str


@dataclass
class CheckerConfig:
    target_repo: Path
    docs_dir: Path
    manifests: Dict[str, Path]
    rerun_command: str
    include_dev_dependencies: bool

    @classmethod
    def load(cls, config_path: Path) -> "CheckerConfig":
        with config_path.open("r", encoding="utf-8") as handle:
            raw = json.load(handle)

        target_repo = cls._resolve(config_path.parent, raw.get("target_repo", ".")).resolve()
        docs_dir = cls._resolve(target_repo, raw.get("docs_dir", "dependency-docs")).resolve()

        defaults = {
            "ruby": "Gemfile",
            "javascript": "package.json",
            "python": "pyproject.toml",
        }
        raw_manifests = raw.get("manifests", {})
        manifests: Dict[str, Path] = {}
        for manifest_type in MANIFEST_TYPES:
            configured = raw_manifests.get(manifest_type, defaults[manifest_type])
            if configured:
                manifests[manifest_type] = cls._resolve(target_repo, configured).resolve()

        rerun_command = raw.get("rerun_command", "make check-dependencies")
        include_dev_dependencies = bool(raw.get("include_dev_dependencies", True))

        return cls(
            target_repo=target_repo,
            docs_dir=docs_dir,
            manifests=manifests,
            rerun_command=rerun_command,
            include_dev_dependencies=include_dev_dependencies,
        )

    @staticmethod
    def _resolve(base_dir: Path, raw_path: str) -> Path:
        candidate = Path(raw_path)
        if candidate.is_absolute():
            return candidate
        return base_dir / candidate


@dataclass
class CheckResults:
    source_dependencies: Dict[str, Set[str]]
    missing_dependencies: Set[str]
    incomplete_dependencies: Dict[str, List[DocumentedDependency]]
    duplicated_dependencies: Dict[str, List[DocumentedDependency]]
    documented_dependencies: Dict[str, List[DocumentedDependency]]
    missing_manifests: Dict[str, Path]

    @property
    def all_source_dependencies(self) -> Set[str]:
        combined: Set[str] = set()
        for deps in self.source_dependencies.values():
            combined.update(deps)
        return combined

    @property
    def is_success(self) -> bool:
        return not self.missing_dependencies and not self.incomplete_dependencies and not self.duplicated_dependencies


class DependencyChecker:
    def __init__(self, config: CheckerConfig):
        self.config = config

    def run(self) -> CheckResults:
        source_dependencies: Dict[str, Set[str]] = {"ruby": set(), "javascript": set(), "python": set()}
        missing_manifests: Dict[str, Path] = {}

        for manifest_type, manifest_path in self.config.manifests.items():
            if not manifest_path.exists():
                missing_manifests[manifest_type] = manifest_path
                continue

            if manifest_type == "ruby":
                source_dependencies[manifest_type] = self.extract_gemfile_dependencies(manifest_path)
            elif manifest_type == "javascript":
                source_dependencies[manifest_type] = self.extract_package_json_dependencies(manifest_path)
            elif manifest_type == "python":
                source_dependencies[manifest_type] = self.extract_python_dependencies(manifest_path)

        documented_dependencies = self.scan_markdown_files(self.config.docs_dir)
        all_source_dependencies = set().union(*source_dependencies.values())

        documented_names = set(documented_dependencies.keys())
        missing_dependencies = all_source_dependencies - documented_names

        incomplete_dependencies = {
            name: entries
            for name, entries in documented_dependencies.items()
            if name in all_source_dependencies and any(not entry.has_necessity for entry in entries)
        }

        duplicated_dependencies = {
            name: entries
            for name, entries in documented_dependencies.items()
            if name in all_source_dependencies and len(entries) > 1
        }

        return CheckResults(
            source_dependencies=source_dependencies,
            missing_dependencies=missing_dependencies,
            incomplete_dependencies=incomplete_dependencies,
            duplicated_dependencies=duplicated_dependencies,
            documented_dependencies=documented_dependencies,
            missing_manifests=missing_manifests,
        )

    @staticmethod
    def extract_gemfile_dependencies(gemfile_path: Path) -> Set[str]:
        content = gemfile_path.read_text(encoding="utf-8")
        deps: Set[str] = set()
        for line in content.splitlines():
            match = re.match(r"^\s*gem\s+['\"]([^'\"]+)['\"]", line)
            if match:
                deps.add(match.group(1).strip())
        return deps

    def extract_package_json_dependencies(self, package_json_path: Path) -> Set[str]:
        with package_json_path.open("r", encoding="utf-8") as handle:
            package_data = json.load(handle)

        sections = ["dependencies"]
        if self.config.include_dev_dependencies:
            sections.extend(["devDependencies", "peerDependencies", "optionalDependencies"])

        deps: Set[str] = set()
        for section in sections:
            section_data = package_data.get(section, {})
            if isinstance(section_data, dict):
                deps.update(section_data.keys())
        return deps

    @staticmethod
    def extract_python_dependencies(pyproject_path: Path) -> Set[str]:
        with pyproject_path.open("rb") as handle:
            data = tomllib.load(handle)

        deps: Set[str] = set()

        project_table = data.get("project", {})
        for dep_spec in project_table.get("dependencies", []):
            dep_name = normalize_dependency_name(dep_spec)
            if dep_name:
                deps.add(dep_name)

        optional_table = project_table.get("optional-dependencies", {})
        if isinstance(optional_table, dict):
            for dependency_list in optional_table.values():
                if isinstance(dependency_list, list):
                    for dep_spec in dependency_list:
                        dep_name = normalize_dependency_name(dep_spec)
                        if dep_name:
                            deps.add(dep_name)

        poetry_deps = data.get("tool", {}).get("poetry", {}).get("dependencies", {})
        if isinstance(poetry_deps, dict):
            for dep_name in poetry_deps.keys():
                normalized = normalize_dependency_name(dep_name)
                if normalized and normalized.lower() != "python":
                    deps.add(normalized)

        return deps

    @staticmethod
    def scan_markdown_files(docs_dir: Path) -> Dict[str, List[DocumentedDependency]]:
        documented: Dict[str, List[DocumentedDependency]] = {}
        if not docs_dir.exists():
            return documented

        markdown_files = sorted(docs_dir.rglob("*.md"))
        for md_file in markdown_files:
            content = md_file.read_text(encoding="utf-8")
            for dep_name, block_text in iter_dependency_blocks(content):
                necessity_match = NECESSITY_RE.search(block_text)
                has_necessity = bool(necessity_match)
                severity = necessity_match.group(1).upper() if necessity_match else "UNKNOWN"

                entry = DocumentedDependency(
                    file_path=md_file,
                    has_necessity=has_necessity,
                    severity=severity,
                )
                documented.setdefault(dep_name, []).append(entry)

        return documented


def iter_dependency_blocks(markdown_text: str) -> Iterable[tuple[str, str]]:
    current_name: str | None = None
    current_lines: List[str] = []

    for line in markdown_text.splitlines():
        match = DEPENDENCY_LINE_RE.match(line)
        if match:
            if current_name is not None:
                yield current_name, "\n".join(current_lines)
            current_name = match.group(1).strip()
            current_lines = [line]
            continue

        if current_name is not None:
            if line.startswith("- ["):
                yield current_name, "\n".join(current_lines)
                current_name = None
                current_lines = []
            else:
                current_lines.append(line)

    if current_name is not None:
        yield current_name, "\n".join(current_lines)


def normalize_dependency_name(dep_spec: str) -> str:
    if not isinstance(dep_spec, str):
        return ""

    cleaned = dep_spec.strip()
    if not cleaned:
        return ""

    cleaned = cleaned.split(";", 1)[0].strip()
    if " @ " in cleaned:
        cleaned = cleaned.split(" @ ", 1)[0].strip()

    match = NAME_RE.match(cleaned)
    return match.group(0) if match else ""


def save_report(results: CheckResults, output_dir: Path) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    report_path = output_dir / f"dependency-checker-last-run-{datetime.now().strftime('%Y-%m-%d')}.txt"

    with report_path.open("w", encoding="utf-8") as handle:
        handle.write("DEPENDENCY CHECKER REPORT\n")
        handle.write(f"Generated: {datetime.now().isoformat(timespec='seconds')}\n\n")

        for manifest_type in MANIFEST_TYPES:
            deps = sorted(results.source_dependencies.get(manifest_type, set()))
            handle.write(f"{manifest_type.upper()} ({len(deps)}):\n")
            for dep in deps:
                handle.write(f"  - {dep}\n")
            handle.write("\n")

        handle.write(f"MISSING ({len(results.missing_dependencies)}):\n")
        for dep in sorted(results.missing_dependencies):
            handle.write(f"  - {dep}\n")
        handle.write("\n")

        handle.write(f"INCOMPLETE ({len(results.incomplete_dependencies)}):\n")
        for dep, entries in sorted(results.incomplete_dependencies.items()):
            files = ", ".join(str(entry.file_path) for entry in entries)
            handle.write(f"  - {dep}: {files}\n")
        handle.write("\n")

        handle.write(f"DUPLICATED ({len(results.duplicated_dependencies)}):\n")
        for dep, entries in sorted(results.duplicated_dependencies.items()):
            files = ", ".join(str(entry.file_path) for entry in entries)
            handle.write(f"  - {dep}: {files}\n")
        handle.write("\n")

    return report_path


def print_summary(results: CheckResults, report_path: Path) -> None:
    print("Dependency checker summary")
    print(f"- Ruby dependencies: {len(results.source_dependencies.get('ruby', set()))}")
    print(f"- JavaScript dependencies: {len(results.source_dependencies.get('javascript', set()))}")
    print(f"- Python dependencies: {len(results.source_dependencies.get('python', set()))}")
    print(f"- Missing docs: {len(results.missing_dependencies)}")
    print(f"- Incomplete docs: {len(results.incomplete_dependencies)}")
    print(f"- Duplicate docs: {len(results.duplicated_dependencies)}")
    print(f"- Report: {report_path}")


def print_gate_failure(results: CheckResults, config: CheckerConfig) -> None:
    print("\n❌ VALIDATION ERROR: Dependency documentation is out of sync with manifests.")
    print("🔧 AI AGENT HELPER --> FIX REQUIRED")
    print("Condition:")
    print("- Every dependency declared in configured manifests must appear exactly once in dependency docs.")
    print("- Every documented dependency must include a Necessity severity (LOW, MEDIUM, HIGH, or CRITICAL).")

    print("Prompt:")
    print("- Inspect the payload below, update markdown dependency docs, and make the gate pass without changing manifest files unless intentional.")

    print("Context payload:")
    print(f"- Target repo: {config.target_repo}")
    print(f"- Docs directory: {config.docs_dir}")

    if results.missing_manifests:
        print("- Missing manifest files:")
        for manifest_type, path in sorted(results.missing_manifests.items()):
            print(f"  - {manifest_type}: {path}")

    if results.missing_dependencies:
        print("- Missing documentation entries:")
        for dep in sorted(results.missing_dependencies):
            print(f"  - {dep}")

    if results.incomplete_dependencies:
        print("- Incomplete documentation entries (missing Necessity):")
        for dep, entries in sorted(results.incomplete_dependencies.items()):
            files = ", ".join(str(entry.file_path) for entry in entries)
            print(f"  - {dep}: {files}")

    if results.duplicated_dependencies:
        print("- Duplicate documentation entries (same dependency in multiple files):")
        for dep, entries in sorted(results.duplicated_dependencies.items()):
            files = ", ".join(str(entry.file_path) for entry in entries)
            print(f"  - {dep}: {files}")

    print("Mutation:")
    print("- Edit files under the docs directory to add missing dependencies, fill Necessity lines, and remove duplicates.")
    print("- Keep dependency names aligned with manifest package names.")

    print(f"Rerun command: {config.rerun_command}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate dependency docs against manifest files.")
    parser.add_argument(
        "--config",
        default=os.environ.get("DEPENDENCY_CHECKER_CONFIG", "dependency-checker.config.json"),
        help="Path to the checker config JSON file.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config_path = Path(args.config).resolve()

    if not config_path.exists():
        print(f"Configuration file not found: {config_path}")
        return 2

    config = CheckerConfig.load(config_path)
    checker = DependencyChecker(config)
    results = checker.run()

    report_path = save_report(results, output_dir=Path(__file__).parent / "results")
    print_summary(results, report_path)

    if results.is_success:
        print("\n✅ Gate passed: dependency documentation is complete and consistent.")
        return 0

    print_gate_failure(results, config)
    return 1


if __name__ == "__main__":
    sys.exit(main())
