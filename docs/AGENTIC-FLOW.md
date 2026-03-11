# Agentic Flow: Dependency Documentation Gate

This document describes exactly where the flow stops, what the gate emits, and what the agent must do to fix it.

## Flow Overview

1. Deterministic code parses manifests (Gemfile, package.json, pyproject.toml) and extracts dependency names.
2. Deterministic code parses markdown dependency docs and extracts documented entries.
3. Checker compares both sets.
4. If any rule fails, the gate fires and prints an actionable payload.
5. Agent (or human) edits markdown docs and reruns.
6. Gate passes and flow completes.

## Gate Contract

**Condition:** The gate passes only when:

- Every manifest dependency is documented (exactly once).
- Each documented dependency has `**Necessity**: **LOW|MEDIUM|HIGH|CRITICAL**`.
- No dependency appears in multiple doc files.

**On failure:** The checker always emits `❌ VALIDATION ERROR:` and `🔧 AI AGENT HELPER --> FIX REQUIRED`, then a structured payload. Which sections appear depends on what failed—only the relevant ones are printed.

## Example Gate Outputs

### Example A: Missing documentation entries

A dependency is in `package.json` but has no doc entry:

```
❌ VALIDATION ERROR: Dependency documentation is out of sync with manifests.
🔧 AI AGENT HELPER --> FIX REQUIRED
Condition:
- Every dependency declared in configured manifests must appear exactly once in dependency docs.
- Every documented dependency must include a Necessity severity (LOW, MEDIUM, HIGH, or CRITICAL).

Prompt:
- Inspect the payload below, update markdown dependency docs, and make the gate pass without changing manifest files unless intentional.

Context payload:
- Target repo: /path/to/examples/minimal-repo
- Docs directory: /path/to/examples/minimal-repo/dependency-docs
- Missing documentation entries:
  - lodash
  - axios

Mutation:
- Edit files under the docs directory to add missing dependencies, fill Necessity lines, and remove duplicates.
- Keep dependency names aligned with manifest package names.

Rerun command: make check-dependencies
```

### Example B: Incomplete entries (missing Necessity)

Docs exist but lack the Necessity line:

```
Context payload:
- Target repo: /path/to/examples/minimal-repo
- Docs directory: /path/to/examples/minimal-repo/dependency-docs
- Incomplete documentation entries (missing Necessity):
  - express: examples/minimal-repo/dependency-docs/javascript.md
  - zod: examples/minimal-repo/dependency-docs/javascript.md
```

### Example C: Duplicate entries

Same dependency documented in multiple files:

```
Context payload:
- Target repo: /path/to/examples/minimal-repo
- Docs directory: /path/to/examples/minimal-repo/dependency-docs
- Duplicate documentation entries (same dependency in multiple files):
  - react: dependency-docs/core.md, dependency-docs/ui.md
```

### Example D: Mixed failure

Multiple issues at once—all applicable sections appear:

```
Context payload:
- Target repo: /path/to/repo
- Docs directory: /path/to/repo/dependency-docs
- Missing documentation entries:
  - new-package
- Incomplete documentation entries (missing Necessity):
  - old-package: dependency-docs/legacy.md
- Duplicate documentation entries (same dependency in multiple files):
  - shared-lib: dependency-docs/a.md, dependency-docs/b.md
```

### Example E: Missing manifest file

Config references a manifest that doesn't exist:

```
Context payload:
- Target repo: /path/to/repo
- Docs directory: /path/to/repo/dependency-docs
- Missing manifest files:
  - python: /path/to/repo/pyproject.toml
```

## Mutation

- **Missing entries:** Add `- [x] **package-name**` plus `**Necessity**: **HIGH**` (or LOW/MEDIUM/CRITICAL) and a brief rationale.
- **Incomplete:** Add the Necessity line to existing entries.
- **Duplicates:** Keep the entry in one file; remove it from the others.
- **Missing manifests:** Add the file or set that manifest to `null` in config.

## Re-entry

The gate prints the exact rerun command (e.g. `make check-dependencies`). Run it after mutation. If the fix is correct, the gate passes.

## Why This Pattern Matters

“Please keep dependency docs updated” becomes an enforced checkpoint. The deterministic checker runs every time; the gate payload tells the agent exactly what to fix and how to retry.
