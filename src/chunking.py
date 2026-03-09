from typing import List

from src.config import DEFAULT_CHUNK_OVERLAP, DEFAULT_CHUNK_SIZE
from src.models import PageDocument, TextChunk


def split_text_into_chunks(text: str, chunk_size: int, overlap: int) -> list[str]:
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")
    if overlap < 0:
        raise ValueError("overlap must be non-negative")
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
        page_chunks = split_text_into_chunks(
            text=page.text,
            chunk_size=chunk_size,
            overlap=overlap,
        )

        for idx, chunk_text in enumerate(page_chunks):
            chunk = TextChunk(
                chunk_id=f"{page.source_file}_p{page.page_number}_c{idx}",
                source_file=page.source_file,
                page_number=page.page_number,
                text=chunk_text,
            )
            all_chunks.append(chunk)

    return all_chunks


def preview_chunks(chunks: List[TextChunk], preview_chars: int = 300) -> None:
    print(f"Total chunks: {len(chunks)}")
    for chunk in chunks[:5]:
        print("=" * 80)
        print(f"Chunk ID: {chunk.chunk_id}")
        print(f"Source: {chunk.source_file}")
        print(f"Page: {chunk.page_number}")
        print(chunk.text[:preview_chars])
        print()


if __name__ == "__main__":
    from src.pdf_parser import parse_pdf

    sample_path = "data/raw/sample.pdf"
    pages = parse_pdf(sample_path)
    chunks = chunk_pages(pages)

    preview_chunks(chunks)