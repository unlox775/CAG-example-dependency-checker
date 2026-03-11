# Python Dependencies

App server with FastAPI, backup jobs, analysis jobs, and CSV export.

## Web Framework

- [x] **fastapi**
  - **Necessity**: **CRITICAL**
  - Async web framework. Used in `app_server/main.py`, `api/routes.py`.

- [x] **uvicorn**
  - **Necessity**: **CRITICAL**
  - ASGI server. Run via `uvicorn main:app`.

## Database

- [x] **sqlalchemy**
  - **Necessity**: **HIGH**
  - ORM and async engine. Used in `app_server/db/connection.py`, `db/models.py`, `exports/csv_export.py`.

- [x] **aiosqlite**
  - **Necessity**: **HIGH**
  - Async SQLite driver for SQLAlchemy. Used in `app_server/db/connection.py`.

## Data Processing and Jobs

- [x] **pandas**
  - **Necessity**: **HIGH**
  - DataFrames for CSV and analysis. Used in `app_server/exports/csv_export.py`, `jobs/analysis_job.py`.

- [x] **apscheduler**
  - **Necessity**: **HIGH**
  - Scheduled backup and analysis jobs. Used in `app_server/jobs/scheduler.py`, `main.py`.

- [x] **openpyxl**
  - **Necessity**: **MEDIUM**
  - Excel export. Used in `app_server/exports/csv_export.py` via `export_to_excel`.

## HTTP and Config

- [x] **httpx**
  - **Necessity**: **MEDIUM**
  - Async HTTP client. Used in `app_server/api/routes.py` for external API calls.

- [x] **python-dotenv**
  - **Necessity**: **MEDIUM**
  - Load `.env` for config. Used in `app_server/main.py`.

## Utilities

- [x] **pydantic**
  - **Necessity**: **HIGH**
  - Request/response validation. Used in `app_server/api/routes.py` for `ExportRequest`.

- [x] **tenacity**
  - **Necessity**: **MEDIUM**
  - Retry logic for backup job. Used in `app_server/jobs/backup_job.py`.

- [x] **structlog**
  - **Necessity**: **MEDIUM**
  - Structured logging. Used in `app_server/main.py`, `jobs/backup_job.py`, `jobs/analysis_job.py`.

## Dev Dependencies

- [x] **pytest**
  - **Necessity**: **MEDIUM**
  - Test runner. Used for `app_server/tests/`.

- [x] **pytest-asyncio**
  - **Necessity**: **MEDIUM**
  - Async test support. Used in `app_server/tests/test_exports.py`.
