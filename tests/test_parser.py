from pathlib import Path

from src.pdf_parser import parse_pdf


def test_parse_pdf_file_not_found():
    missing = Path("data/raw/does_not_exist.pdf")
    try:
        parse_pdf(missing)
        assert False, "Expected FileNotFoundError"
    except FileNotFoundError:
        assert True
