"""Build final dataset from cleaned intermediate files."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


def build_dataset(interim_dir: str, output_csv: str) -> Path:
	"""Combine interim CSV files into a single processed dataset."""
	files = sorted(Path(interim_dir).glob("*.csv"))
	frames = [pd.read_csv(path) for path in files]
	dataset = pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()

	out_path = Path(output_csv)
	out_path.parent.mkdir(parents=True, exist_ok=True)
	dataset.to_csv(out_path, index=False)
	return out_path
