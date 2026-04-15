"""Logging setup utility."""

from __future__ import annotations

import logging


def get_logger(name: str, level: str = "INFO") -> logging.Logger:
	"""Create and return a module logger."""
	logger = logging.getLogger(name)
	if not logger.handlers:
		logging.basicConfig(
			level=getattr(logging, level.upper(), logging.INFO),
			format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
		)
	return logger
