"""Normalize offers from multiple retailers into one schema."""

from __future__ import annotations

from typing import Any


def normalize_offers(offers: list[dict[str, Any]]) -> list[dict[str, Any]]:
	"""Lower-case retailer names and keep required fields."""
	normalized: list[dict[str, Any]] = []
	for offer in offers:
		normalized.append(
			{
				"product_id": offer.get("product_id"),
				"retailer": str(offer.get("retailer", "")).lower(),
				"price": offer.get("price"),
				"currency": offer.get("currency", "USD"),
				"url": offer.get("url", ""),
			}
		)
	return normalized
