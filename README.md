# CAG Example: Dependency Documentation Checker

This repository is a standalone **Composite Agentic Gate (CAG)** example.

**What’s a CAG?** A Composite Agentic Gate is a checkpoint where code stops and hands off to an AI agent (or human): the gate gives context (e.g. missing docs, manifest paths), asks for a fix or decision, and prints the exact rerun command. That turns dependency-doc drift into a repeatable fix-and-rerun loop instead of stale, untrusted docs. **Read more:** [The Compound Agentic Workflow — How AI agents can solve messy real-world problems](https://medium.com/constant-total-amazement/the-compound-agentic-workflow-how-ai-agents-can-solve-messy-real-world-problems-25561e482876).

**About this repo.** This code was extracted from a private monorepo (and rehydrated from a patch), sanitized, and AI-ported to demonstrate a CAG example. It may be usable—you’re welcome to use it under the MIT license—but it is not intended (yet) as a ready-to-use, production tool.

It combines deterministic code (manifest parsing + markdown validation) with an agentic gate that stops the flow when docs drift from dependency manifests. The gate emits a fix payload and an exact rerun command, so an agent can mutate docs and re-enter the same pipeline immediately.

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

## Run with an AI Agent (Primary)

The point of this repo is to run the dependency checker with an AI agent. You do one-time setup, then the agent runs the check and handles gate output (fix docs, rerun) for you.

**Agent runner:** This is configured for **Codex**. Have Codex installed and logged in so it can run in this repo. To use another agent (Cursor, Claude, etc.), the gate output and flow are the same—port the runner; it should work with minimal changes.

**Codex setup (brief):** Install the Codex CLI, log in, and ensure it can execute in this directory. Once that’s done, you’re ready to run the flow with an agent.

**One-time setup (you):**

```bash
make install
```

Default config validates the bundled sample repo in [`examples/minimal-repo`](examples/minimal-repo).

**Run the flow with your agent:** Point your agent at this repo and tell it to run the dependency checker. The agent should:

1. Run: `make check-dependencies`
2. If the gate fails, read the gate output (`❌ VALIDATION ERROR:`, `🔧 AI AGENT HELPER --> FIX REQUIRED`, and the listed issues), update dependency markdown or config as indicated, then rerun `make check-dependencies`.
3. Repeat until the check passes.

That’s it. The agent keeps dependency docs in sync with manifests.

## Repository Layout

- `dependency_checker.py` - deterministic validator and gate emitter
- `dependency-checker.config.json` - target repo + manifest/docs mapping
- `examples/minimal-repo/` - runnable sample target with manifests + docs
- `docs/AGENTIC-FLOW.md` - gate contract and full loop walkthrough
- `legacy/codeorg-snapshot/` - archived source artifacts from original split-out rehydration

## Configure For Your Repo

1. Copy `dependency-checker.config.json` and set:
   - `target_repo`
   - `docs_dir`
   - `manifests` paths (set any manifest to `null` if not used)
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

## License

MIT. See [`LICENSE`](LICENSE).
