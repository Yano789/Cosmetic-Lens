"""Retailer price client stubs."""

from __future__ import annotations

from typing import Any


def fetch_retailer_offers(product_id: str) -> list[dict[str, Any]]:
	"""Fetch offers from configured retailers."""
	return [
		{
			"product_id": product_id,
			"retailer": "placeholder",
			"price": None,
			"currency": "USD",
			"url": "",
		}
	]
