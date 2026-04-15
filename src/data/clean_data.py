"""Data cleaning utilities for cosmetic product records."""

from __future__ import annotations

import pandas as pd


def clean_records(df: pd.DataFrame) -> pd.DataFrame:
	"""Apply baseline cleaning and return a normalized dataframe."""
	if df.empty:
		return df

	cleaned = df.copy()
	cleaned.columns = [c.strip().lower() for c in cleaned.columns]
	return cleaned
