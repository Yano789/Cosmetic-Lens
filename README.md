# CosmeticLens 💄🔍
**Image-Based Cosmetic Product Search & Price Comparison**

CosmeticLens is a deep learning-powered application that allows users to upload an image of a cosmetic product (e.g., lipstick or foundation) and instantly find visually similar items across multiple retailers, along with price comparisons and purchase links.

---

## Features

- Upload an image of a cosmetic product
- Deep learning-based visual similarity search (CLIP embeddings)
- Retrieve similar products from a curated dataset
- Compare prices across retailers
- Direct links to purchase products
- Simple web interface for demonstration

---

## 📁 Repository Structure

```
cosmetic-lens/
│
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
│
├── data/
│   ├── raw/                # Raw scraped data (unprocessed)
│   ├── interim/            # Partially cleaned data
│   ├── processed/          # Final dataset (CSV format)
│   └── images/             # Downloaded product images
│
├── notebooks/
│   └── exploration.ipynb   # Data exploration only (not used in pipeline)
│
├── src/
│   ├── data/
│   │   ├── scrape_sephora.py     # Scrape product data from Sephora
│   │   ├── scrape_douglas.py     # Scrape product data from Douglas
│   │   ├── clean_data.py         # Data cleaning and normalization
│   │   └── build_dataset.py      # Build final dataset
│   │
│   ├── models/
│   │   ├── embedder.py           # CLIP model wrapper
│   │   ├── train_embedder.py     # (Optional) fine-tuning script
│   │   └── infer_embedder.py     # Generate embeddings for images
│   │
│   ├── retrieval/
│   │   ├── build_index.py        # Build FAISS index
│   │   ├── search.py             # Perform similarity search
│   │   └── rerank.py             # Optional re-ranking logic
│   │
│   ├── pricing/
│   │   ├── retailer_clients.py   # Retailer-specific logic
│   │   └── normalize_offers.py   # Normalize and compare prices
│   │
│   ├── api/
│   │   └── app.py                # FastAPI backend
│   │
│   └── utils/
│       ├── config.py             # Configuration management
│       ├── logger.py             # Logging utilities
│       └── helpers.py            # General helper functions
│
├── frontend/
│   └── app.py                    # Streamlit web interface
│
├── tests/
│   ├── test_search.py            # Tests for retrieval system
│   └── test_api.py               # Tests for API endpoints
│
├── outputs/
│   ├── embeddings.npy            # Saved image embeddings
│   ├── faiss_index.bin           # FAISS index file
│   └── sample_results.json       # Example outputs
│
└── docs/
    ├── architecture.png          # System architecture diagram
    └── week1_notes.md            # Development notes
```

---

## System Pipeline

```
Image Upload → Embedding Model → Similarity Search → Product Matching → Price Aggregation → Results Display
```

1. User uploads an image
2. Image is converted into an embedding using a deep learning model (CLIP)
3. FAISS retrieves the most similar products
4. Matching products are grouped and enriched with pricing information
5. Results are returned via API and displayed in the frontend

---

## Installation

```bash
git clone <repo-url>
cd cosmetic-lens
pip install -r requirements.txt
```

---

## Running the Project

### 1. Build dataset

```bash
python src/data/build_dataset.py
```

### 2. Generate embeddings

```bash
python src/models/infer_embedder.py
```

### 3. Build similarity index

```bash
python src/retrieval/build_index.py
```

### 4. Run backend API

```bash
uvicorn src.api.app:app --reload
```

### 5. Run frontend

```bash
streamlit run frontend/app.py
```

---

## Dataset

The dataset consists of cosmetic products (e.g., lipsticks, foundations) collected from online retailers. Each entry includes:

- Product name
- Brand
- Category
- Price
- Retailer
- Image
- Product URL

---

## Evaluation (Planned)

- Top-K retrieval accuracy
- Visual similarity relevance (manual evaluation)
- Query latency
- Coverage of price comparisons

---

## Notes

- This is a research/educational prototype
- Data is collected in limited quantities for demonstration purposes
- Performance may vary depending on dataset quality and size

---

## Team

...

---

## Future Improvements

- Shade detection and color matching
- OCR for product label recognition
- Brand classification
- Personalized recommendations
- Mobile app integration