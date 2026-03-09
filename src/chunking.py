from typing import List

from src.models import PageDocument, TextChunk
from src.config import DEFAULT_CHUNK_SIZE, DEFAULT_CHUNK_OVERLAP


def split_text_into_chunks(text: str, chunk_size: int, overlap: int) -> list[str]:
    if chunk_size <= 0:
        raise ValueError("chunk_size must be > 0")
    if overlap < 0:
        raise ValueError("overlap must be >= 0")
    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    words = text.split()
    if not words:
        return []

    chunks = []
    step = chunk_size - overlap

    for start in range(0, len(words), step):
        chunk_words = words[start:start + chunk_size]
        if not chunk_words:
            continue
        chunks.append(" ".join(chunk_words))

    return chunks


def chunk_pages(
    pages: List[PageDocument],
    chunk_size: int = DEFAULT_CHUNK_SIZE,
    overlap: int = DEFAULT_CHUNK_OVERLAP,
) -> List[TextChunk]:
    all_chunks: List[TextChunk] = []

    for page in pages:
        page_chunks = split_text_into_chunks(page.text, chunk_size, overlap)

        for idx, chunk_text in enumerate(page_chunks):
            chunk = TextChunk(
                chunk_id=f"{page.source_file}_p{page.page_number}_c{idx}",
                source_file=page.source_file,
                page_number=page.page_number,
                text=chunk_text,
            )
            all_chunks.append(chunk)

    return all_chunks
