"""CLIP embedder wrapper for text/image product representations."""

from __future__ import annotations

from typing import Iterable

import numpy as np


class ClipEmbedder:
	"""Simple placeholder wrapper around an embedding model."""

	def __init__(self, model_name: str = "openai/clip-vit-base-patch32") -> None:
		self.model_name = model_name

	def encode_text(self, texts: Iterable[str]) -> np.ndarray:
		"""Return deterministic zero vectors as placeholder embeddings."""
		texts_list = list(texts)
		return np.zeros((len(texts_list), 512), dtype=np.float32)
