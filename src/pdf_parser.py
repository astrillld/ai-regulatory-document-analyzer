from pathlib import Path
from typing import List

import fitz  # PyMuPDF

from src.models import PageDocument


def parse_pdf(pdf_path: str | Path) -> List[PageDocument]:
    pdf_path = Path(pdf_path)

    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    pages: List[PageDocument] = []

    with fitz.open(pdf_path) as doc:
        for i, page in enumerate(doc):
            text = page.get_text("text").strip()
            pages.append(
                PageDocument(
                    source_file=pdf_path.name,
                    page_number=i + 1,
                    text=text,
                )
            )

    return pages


def preview_pdf(pdf_path: str | Path, preview_chars: int = 500) -> None:
    pages = parse_pdf(pdf_path)

    print(f"Parsed pages: {len(pages)}")
    for page in pages[:3]:
        print("=" * 60)
        print(f"Page {page.page_number}")
        print(page.text[:preview_chars])
        print()


if __name__ == "__main__":
    sample_path = "data/raw/sample.pdf"
    preview_pdf(sample_path)
