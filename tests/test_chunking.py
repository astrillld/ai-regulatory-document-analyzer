from src.chunking import split_text_into_chunks


def test_split_text_into_chunks_basic():
    text = " ".join([f"word{i}" for i in range(100)])
    chunks = split_text_into_chunks(text, chunk_size=20, overlap=5)

    assert len(chunks) > 0
    assert all(isinstance(chunk, str) for chunk in chunks)