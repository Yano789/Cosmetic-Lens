"""Optional reranking stage for retrieval results."""

from __future__ import annotations

from typing import Any


def rerank(results: list[dict[str, Any]]) -> list[dict[str, Any]]:
	"""Return results unchanged as baseline behavior."""
	return results
