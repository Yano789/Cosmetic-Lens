"""Similarity search utilities."""

from __future__ import annotations

import numpy as np


def cosine_similarity_search(
	query: np.ndarray,
	corpus: np.ndarray,
	top_k: int = 5,
) -> list[int]:
	"""Return top-k corpus indices by cosine similarity."""
	if corpus.size == 0:
		return []

	query_norm = query / (np.linalg.norm(query) + 1e-12)
	corpus_norm = corpus / (np.linalg.norm(corpus, axis=1, keepdims=True) + 1e-12)
	scores = corpus_norm @ query_norm
	return np.argsort(scores)[::-1][:top_k].tolist()
