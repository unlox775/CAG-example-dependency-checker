# Agentic Flow: Dependency Documentation Gate

## Flow Summary

This example demonstrates a deterministic pipeline with a hard agentic checkpoint:

1. Parse dependency manifests.
2. Parse markdown dependency docs.
3. Compare both sets.
4. Stop at gate if any contract rule fails.

## Gate Contract

### Condition

The gate passes only when all of the following are true:

- Every manifest dependency is documented.
- Each documented dependency has `**Necessity**: **LOW|MEDIUM|HIGH|CRITICAL**`.
- No dependency is documented in multiple files.

### Prompt Output (on failure)

The checker emits these exact markers:

- `❌ VALIDATION ERROR:`
- `🔧 AI AGENT HELPER --> FIX REQUIRED`

Then it prints:

- condition that failed
- context payload (missing/incomplete/duplicate dependencies)
- mutation instructions
- exact re-entry command

### Context Payload

The payload includes:

- target repo path
- docs directory path
- missing dependencies
- incomplete entries (missing Necessity)
- duplicate entries
- missing manifests (if configured but absent)

### Mutation

Expected mutation is data-level, not code-level:

- edit markdown dependency docs
- add missing dependency entries
- add missing Necessity severity
- deduplicate conflicting entries

### Re-entry

Exact rerun command:

```bash
make check-dependencies
```

If the mutation is correct, the gate passes and the pipeline completes.

## Why This Pattern Matters

This turns “please keep docs updated” into enforced process flow. The deterministic checker guarantees the checkpoint runs every time, and the gate payload makes correction steps explicit for a human or another agent.
