from pydantic import BaseModel


class PageDocument(BaseModel):
    source_file: str
    page_number: int
    text: str


class TextChunk(BaseModel):
    chunk_id: str
    source_file: str
    page_number: int
    text: str