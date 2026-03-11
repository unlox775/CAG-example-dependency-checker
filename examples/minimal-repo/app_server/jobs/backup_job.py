"""Backup job: export database tables to SQLite backup."""

import asyncio
from tenacity import retry, stop_after_attempt
import structlog

from db.connection import async_session
from db.models import ExportRecord
from exports.csv_export import export_table_to_csv

logger = structlog.get_logger()


@retry(stop=stop_after_attempt(3))
async def run_backup():
    logger.info("Starting backup job")
    async with async_session() as session:
        # Export contacts/records to CSV
        path = await export_table_to_csv(session, "export_records", "backups/records.csv")
        logger.info("Backup complete", path=path)
