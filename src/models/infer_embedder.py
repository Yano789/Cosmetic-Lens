"""Generate embeddings for product descriptions."""

from __future__ import annotations

import numpy as np

from src.models.embedder import ClipEmbedder


def generate_embeddings(texts: list[str], output_path: str) -> str:
	"""Run text embedding inference and persist array to disk."""
	model = ClipEmbedder()
	embeddings = model.encode_text(texts)
	np.save(output_path, embeddings)
	return output_path
