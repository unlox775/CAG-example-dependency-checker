"""Tests for export module."""

import pytest
import pandas as pd
from exports.csv_export import load_csv_for_analysis, export_to_excel


def test_load_csv_missing_returns_none():
    result = load_csv_for_analysis("nonexistent.csv")
    assert result is None


def test_export_to_excel(tmp_path):
    df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
    path = tmp_path / "out.xlsx"
    export_to_excel(df, str(path))
    assert path.exists()
