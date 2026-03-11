"""CSV export and import for backup/analysis."""

import os
from pathlib import Path

import pandas as pd
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
import openpyxl

from db.connection import engine


async def export_table_to_csv(session: AsyncSession, table: str, output_path: str) -> str:
    """Export a table to CSV. Returns the output path."""
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    result = await session.execute(text(f"SELECT * FROM {table}"))
    rows = result.fetchall()
    columns = result.keys()
    df = pd.DataFrame(rows, columns=columns)
    df.to_csv(output_path, index=False)
    return output_path


def load_csv_for_analysis(path: str) -> pd.DataFrame | None:
    """Load a CSV file for analysis. Returns a DataFrame or None if file missing."""
    if not os.path.exists(path):
        return None
    return pd.read_csv(path)


def export_to_excel(df: pd.DataFrame, path: str) -> None:
    """Export DataFrame to Excel. Uses openpyxl as engine."""
    df.to_excel(path, index=False, engine="openpyxl")
