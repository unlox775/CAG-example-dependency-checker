# CAG Example: Dependency Documentation Checker

Dependency docs drift from manifests and nobody keeps them updated. This checker validates that manifest dependencies (Gemfile, package.json, pyproject.toml) are documented in markdown—and when they're not, hands off to an agent to fix them. It's a standalone **Composite Agentic Gate (CAG)** example.

**What's a CAG?** A Composite Agentic Gate is a checkpoint where code stops and hands off to an AI agent (or human): the gate gives context (e.g. missing docs, manifest paths), asks for a fix or decision, and prints the exact rerun command. That turns dependency-doc drift into a repeatable fix-and-rerun loop instead of stale, untrusted docs. **Read more:** [The Compound Agentic Workflow — How AI agents can solve messy real-world problems](https://medium.com/constant-total-amazement/the-compound-agentic-workflow-how-ai-agents-can-solve-messy-real-world-problems-25561e482876).

**About this repo.** Extracted from a private monorepo, sanitized, and AI-ported to demonstrate a CAG example. MIT license; not (yet) a production-ready tool.

## Why This Is a CAG Example

Without the gate, dependency docs become stale and untrustworthy. With the gate:

1. Deterministic code extracts dependency names from `Gemfile`, `package.json`, and `pyproject.toml`.
2. Deterministic code checks markdown dependency docs for coverage and completeness.
3. If validation fails, an **agentic gate** prints:
   - `❌ VALIDATION ERROR:`
   - `🔧 AI AGENT HELPER --> FIX REQUIRED`
   - context payload (missing/incomplete/duplicate items)
   - mutation instructions
   - exact rerun command: `make check-dependencies`
4. Agent mutates docs and reruns. Gate passes, pipeline continues.

## Run with Codex (Primary)

The primary way to use this repo is with **Codex**. Codex runs the checker, and when the gate fails, it reads the gate output, fixes the dependency docs, and reruns—looping until the gate passes.

**Prerequisites:** Codex must be installed and connected. Install the Codex CLI, log in, and ensure it can execute in this directory.

**One-time setup:**

```bash
make install
```

**Run the flow:**

```bash
make agent-check-dependencies
```

This wraps the checker inside a Codex `exec` call. Codex reads [`AGENTS.md`](AGENTS.md) for instructions, runs `make check-dependencies`, and when the gate fails (missing/incomplete/duplicate entries), it edits the markdown files and reruns until the gate passes. Output is captured to `codex-final.txt`.

Default config validates the bundled sample repo in [`examples/minimal-repo`](examples/minimal-repo). Override with:

```bash
make agent-check-dependencies DEPENDENCY_CHECKER_CONFIG=path/to/your-config.json
```

## Run Manually (No Agent)

For quick runs when you don't need the fix-and-rerun loop:

```bash
make check-dependencies
```

If the gate fails, the output tells you what broke and suggests rerunning with `make agent-check-dependencies` so Codex can fix it.

## Want to See the Gate in Action?

Right now the sample repo passes—zero missing, incomplete, or duplicate docs. To trigger the gate and watch Codex regenerate documentation:

- **Add a new dependency** to a manifest without documenting it: e.g. add `"chalk": "^5.0.0"` to `examples/minimal-repo/frontend/package.json`, then run `make check-dependencies`. The gate will report a missing doc.
- **Remove a doc entry** that's still in a manifest: delete an entry from `examples/minimal-repo/dependency-docs/javascript.md` for a package that remains in `package.json`. The gate reports it as missing.
- **Add an incomplete entry**: add `- [x] **new-package**` without the `**Necessity**: **HIGH**` line. The gate reports incomplete.

Then run `make agent-check-dependencies` and Codex should fix the docs and rerun until the gate passes.

**Caveat:** This was never a fully complete project. The sample monorepo and checker may still have rough edges or unexpected behavior.

## Repository Layout

- `dependency_checker.py` - deterministic validator and gate emitter
- `dependency-checker.config.json` - target repo + manifest/docs mapping
- `AGENTS.md` - agent instructions for Codex
- `Makefile` - agent and manual make targets
- `examples/minimal-repo/` - sample monorepo (frontend, backend, app_server) with manifests + docs; ~30 files, 14 deps per language
- `docs/AGENTIC-FLOW.md` - gate contract and full loop walkthrough
- `legacy/codeorg-snapshot/` - archived source artifacts from original split-out rehydration

## Configure For Your Repo

1. Copy `dependency-checker.config.json` and set:
   - `target_repo`
   - `docs_dir`
   - `manifests` paths for each language (e.g. `frontend/package.json`, `backend/Gemfile`, `app_server/pyproject.toml`; set to `null` if not used)
2. Keep dependency docs in markdown entries like:

```markdown
- [x] **dependency-name**
  - **Necessity**: **HIGH**
  - Why this dependency exists.
```

3. Run:

```bash
python3 dependency_checker.py --config path/to/your-config.json
```

## Standalone Scope

This repo no longer depends on monorepo-relative paths. The default run uses local sample files only.

Legacy Code.org-specific analysis files are preserved under `legacy/` for reference and are not part of the standalone flow.

## Background: The Real Problem

Most dependencies in a codebase exist because some developer, quite a while ago, decided to add something. They used it in a couple of places. Maybe those places aren't even very used anymore. The *gravity* of why that dependency is still in the tree has more to do with **history** than with how useful it is to the current repository.

That's frustrating when you're patching security vulnerabilities. You stare at a CVE: *Why the heck is this thing even in here?* And you're left untangling what's used, where, and whether it matters.

The ideal would be docs that explain *why* each dependency exists, *where* it's used, *what* benefit it provides. People rarely write that—it's tedious, goes stale, and nobody maintains it. AI agents are good at scanning large codebases, finding where a dependency is used, and synthesizing that into useful docs.

## What This Attempts To Do

This project tries to turn that insight into a practical flow. It categorizes and organizes dependencies (opinions about groupings), tracks necessity and rationale in structured markdown, emits an agentic gate when docs drift from manifests, and provides a repeatable loop so an agent can mutate docs and re-enter until everything is coherent.

**Caveat:** This never completely worked. It was one of my earlier things while refining the idea of composite agentic gates. The idea is solid; the implementation is a proof-of-concept.

## Architecture Reflection / Big TODO

What this *should* have been: an **agentic loop** that iterates on each dependency individually—possibly one at a time. There's a lot of work per dependency (hunting through code, finding references, synthesizing usage). When context balloons, agents get inefficient and make shortcuts. Many separate agents, each with small context for one dependency, would scale better. That's a significant pivot—and a major TODO for anyone who wants to take this further.

## License

MIT. See [`LICENSE`](LICENSE).
