# Agent Instructions: Dependency Documentation Checker

This file describes how an agent should operate this repository.

## Core Goal

Run the dependency documentation checker. When the validation gate fails (docs out of sync with manifests), fix the dependency markdown files and rerun until the gate passes.

## Composite Agentic Gate

This project enforces a single hard-stop gate:

### Dependency Documentation Gate

- Trigger: after `dependency_checker.py` runs and finds missing, incomplete, or duplicate dependency entries
- Condition: every manifest dependency is documented; each has `**Necessity**: **LOW|MEDIUM|HIGH|CRITICAL**`; no duplicates
- On failure: process exits non-zero with `❌ VALIDATION ERROR:` and `🔧 AI AGENT HELPER --> FIX REQUIRED`
- Fix: edit markdown files under the docs directory; add missing entries; fill Necessity lines; remove duplicates
- Rerun: `make check-dependencies` (or the exact command printed in the gate output)

## Gate Handling Procedure (Mandatory)

When you see output containing `❌ VALIDATION ERROR:` and `🔧 AI AGENT HELPER --> FIX REQUIRED`, do the following:

1. Read the failing criteria from the gate output (missing deps, incomplete entries, duplicates).
2. Edit the markdown files under the configured docs directory.
3. Add missing dependency entries, add `**Necessity**: **LOW|MEDIUM|HIGH|CRITICAL**` where missing, and deduplicate.
4. Rerun the exact command shown in the gate output (typically `make check-dependencies`).
5. Repeat until the gate passes.

## Commands

```bash
make check-dependencies
```

Or with a custom config:

```bash
make check-dependencies DEPENDENCY_CHECKER_CONFIG=path/to/your-config.json
```

## Expected Success Signals

- Command exits 0.
- Output includes `✅ Gate passed: dependency documentation is complete and consistent.`
- No `❌ VALIDATION ERROR` in stderr.
