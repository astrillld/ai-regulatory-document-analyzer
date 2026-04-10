from src.requirements import is_requirement_text

def test_detects_shall():
    text = "The system shall ensure compliance."
    assert is_requirement_text(text)

def test_detects_non_requirements():
    text = "This section describes the system."
    assert not is_requirement_text(text)