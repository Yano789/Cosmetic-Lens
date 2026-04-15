from __future__ import annotations

import numpy as np

from src.retrieval.search import cosine_similarity_search


def test_cosine_similarity_search_returns_expected_index_order() -> None:
	query = np.array([1.0, 0.0, 0.0], dtype=np.float32)
	corpus = np.array(
		[
			[1.0, 0.0, 0.0],
			[0.0, 1.0, 0.0],
			[0.9, 0.1, 0.0],
		],
		dtype=np.float32,
	)

	indices = cosine_similarity_search(query, corpus, top_k=2)
	assert indices == [0, 2]
