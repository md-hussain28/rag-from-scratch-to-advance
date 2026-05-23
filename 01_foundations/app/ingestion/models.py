from pydantic import BaseModel, Field


class FileMetadata(BaseModel):
    file_extension: str
    source_file: str
    absolute_path: str
    file_size_bytes: int = Field(ge=0)
    disk_created_at: float
    read_completed_at: float


class LoadedFile(BaseModel):
    content: bytes
    metadata: FileMetadata

class ParsedDocument(BaseModel):
    title: str
    content: str
    metadata: FileMetadata

