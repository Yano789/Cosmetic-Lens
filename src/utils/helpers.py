"""Shared helper functions."""

from __future__ import annotations

from pathlib import Path


def ensure_parent_dir(path: str) -> Path:
	"""Ensure parent folder for a file path exists."""
	file_path = Path(path)
	file_path.parent.mkdir(parents=True, exist_ok=True)
	return file_path
