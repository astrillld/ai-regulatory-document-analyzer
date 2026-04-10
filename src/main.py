from src.pdf_parser import parse_pdf
from src.chunking import chunk_pages
from src.semantic_search import (
    load_embedding_model,
    embed_chunks,
    build_faiss_index,
    search_chunks
)

print("MAIN STARTED")

def run_pipeline(pdf_path: str, query: str):
    print("Parsing PDF...")
    pages = parse_pdf(pdf_path)

    print("Chunking...")
    chunks = chunk_pages(pages)

    print(f"Total chunks: {len(chunks)}")

    print("Loading model...")
    model = load_embedding_model()

    print("Embedding chunks...")
    embeddings = embed_chunks(chunks, model)

    print("Building FAISS index...")
    index = build_faiss_index(embeddings)

    print(f"\nSearching for: '{query}'\n")

    results = search_chunks(query, chunks, index, model)

    for r in results:
        print("=" * 80)
        print(f"Chunk ID: {r['chunk_id']}")
        print(f"Page: {r['page']}")
        print(f"Score: {r['score']:.4f}")

        req_flag = is_requirement_text(r["text"])
        print(f"Requirement-like: {req_flag}")

        if req_flag:
            print(f"Matched patterns: {requirement_matches(r['text'])}")

        print(r["text"])
        print()


if __name__ == "__main__":
    pdf_path = "data/raw/sample.pdf"
    query = "requirements for safety"

    run_pipeline(pdf_path, query)