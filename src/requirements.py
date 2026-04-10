import re

REQUIREMENT_PATTERNS = [
    r"\bshall\b",
    r"\bmust\b",
    r"\brequired\b",
    r"\bshould\b",
    r"\bmay not\b",
    r"\bmust not\b",
    r"\bprohibited\b",
    r"\bis required to\b",
    r"\bare required to\b",
    r"\bin accordance with\b",
    r"\bin compliance with\b",
]


def is_requirement_text(text: str) -> bool:
    text_lower = text.lower()
    return any(re.search(pattern, text_lower) for pattern in REQUIREMENT_PATTERNS)


def requirement_matches(text: str) -> list[str]:
    text_lower = text.lower()
    matches = []

    for pattern in REQUIREMENT_PATTERNS:
        if re.search(pattern, text_lower):
            matches.append(pattern.replace(r"\b", ""))

    return matches