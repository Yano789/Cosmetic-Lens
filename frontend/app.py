"""Streamlit frontend for product search demo."""

from __future__ import annotations

import streamlit as st


st.set_page_config(page_title="Cosmetic Lens", page_icon="CL", layout="wide")
st.title("Cosmetic Lens")
st.caption("Discover similar products and compare retailer pricing.")

query = st.text_input("Search product", placeholder="e.g., hydrating serum")

if query:
	st.success(f"Search placeholder received: {query}")
else:
	st.info("Enter a product name to start searching.")
