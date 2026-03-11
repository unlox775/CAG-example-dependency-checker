# Minimal Monorepo Example

Sample monorepo for the dependency documentation checker. Not intended to run; it exists so an agent can scan the codebase and trace where each dependency is used.

## Structure

- **frontend/** — Vite + React contact form. Proxies `/api` to the backend. 14 JS deps.
- **backend/** — Sinatra API. Contact submission, health check. 14 Ruby gems.
- **app_server/** — FastAPI app server. Backup job, analysis job, CSV export, SQLite. 14 Python deps.

## Dependency docs

See `dependency-docs/` for documented dependencies with usage references. Each file lists 10–15 dependencies with Necessity ratings and where they're used in the code.
