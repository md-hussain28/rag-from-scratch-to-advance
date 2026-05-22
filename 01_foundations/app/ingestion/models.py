from pydantic import BaseModel, Field


class FileMetadata(BaseModel):
    source_file: str
    absolute_path: str
    file_size_bytes: int = Field(ge=0)
    disk_created_at: float
    read_completed_at: float


class LoadedPDF(BaseModel):
    content: bytes
    metadata: FileMetadata


class ParserMetrics(BaseModel):
    extracted_lines: int = Field(ge=0)
    has_tables: bool


class ParsedDocument(BaseModel):
    title: str
    raw_text_flow: str
    isolated_tables: list[list[str]]
    parser_metrics: ParserMetrics


class IngestionResult(BaseModel):
    document_hash: str
    markdown_content: str
    system_metadata: FileMetadata
    parser_metrics: ParserMetrics
