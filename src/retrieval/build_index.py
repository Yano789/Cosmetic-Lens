"""Build retrieval index from vector embeddings."""

from __future__ import annotations

import numpy as np


def build_index(embeddings: np.ndarray, index_path: str) -> str:
	"""Persist placeholder index bytes to disk.

	Replace with FAISS index serialization in implementation phase.
	"""
	with open(index_path, "wb") as fp:
		fp.write(b"FAISS_PLACEHOLDER")
	return index_path
