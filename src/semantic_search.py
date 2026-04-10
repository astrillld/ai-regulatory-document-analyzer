from typing import List

import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

from src.models import TextChunk
from src.config import EMBEDDING_MODEL_NAME


# === 1. MODEL ===
def load_embedding_model() -> SentenceTransformer:
    return SentenceTransformer(EMBEDDING_MODEL_NAME)


# === 2. EMBEDDINGS ===
def embed_chunks(
    chunks: List[TextChunk],
    model: SentenceTransformer
) -> np.ndarray:
    texts = [chunk.text for chunk in chunks]
    embeddings = model.encode(texts)
    return np.array(embeddings).astype("float32")


# === 3. INDEX ===
def build_faiss_index(embeddings: np.ndarray) -> faiss.IndexFlatL2:
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index


# === 4. SEARCH ===
def search_chunks(
    query: str,
    chunks: List[TextChunk],
    index: faiss.IndexFlatL2,
    model: SentenceTransformer,
    top_k: int = 3
):
    query_embedding = model.encode([query])
    query_embedding = np.array(query_embedding).astype("float32")

    distances, indices = index.search(query_embedding, top_k)

    results = []

    for rank, idx in enumerate(indices[0]):
        chunk = chunks[idx]
        results.append({
            "chunk_id": chunk.chunk_id,
            "page": chunk.page_number,
            "score": float(distances[0][rank]),
            "text": chunk.text[:300]
        })

    return results