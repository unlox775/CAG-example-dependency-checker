"""Analysis job: aggregate data, produce reports."""

import structlog
import pandas as pd

from exports.csv_export import load_csv_for_analysis

logger = structlog.get_logger()


async def run_analysis():
    logger.info("Starting analysis job")
    df = load_csv_for_analysis("backups/records.csv")
    if df is not None and not df.empty:
        summary = df.describe()
        logger.info("Analysis complete", rows=len(df))
    else:
        logger.info("No data to analyze")
