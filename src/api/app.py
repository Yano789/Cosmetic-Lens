"""FastAPI application for retrieval and pricing endpoints."""

from __future__ import annotations

from fastapi import FastAPI

app = FastAPI(title="Cosmetic Lens API", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
	"""Health check endpoint."""
	return {"status": "ok"}
