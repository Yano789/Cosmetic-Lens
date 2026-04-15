"""Configuration helpers."""

from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass(frozen=True)
class Settings:
	app_env: str = "development"
	log_level: str = "INFO"
	embeddings_path: str = "outputs/embeddings.npy"
	faiss_index_path: str = "outputs/faiss_index.bin"


def get_settings() -> Settings:
	"""Load environment variables and return typed settings."""
	load_dotenv()
	return Settings(
		app_env=os.getenv("APP_ENV", "development"),
		log_level=os.getenv("LOG_LEVEL", "INFO"),
		embeddings_path=os.getenv("EMBEDDINGS_PATH", "outputs/embeddings.npy"),
		faiss_index_path=os.getenv("FAISS_INDEX_PATH", "outputs/faiss_index.bin"),
	)
