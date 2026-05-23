from docx import Document
import os
import time
from app.ingestion.models import FileMetadata, LoadedFile


class DocxLoader:
    """Worker Node: Extracts text from Microsoft Word files."""
    def load(self, file_path: str, file_stats: os.stat_result) -> LoadedFile:
        doc = Document(file_path)
        extracted_text = "\n".join([p.text for p in doc.paragraphs])
        
        return LoadedFile(
            content=extracted_text.encode("utf-8"),
            metadata=FileMetadata(
                file_extension=".docx",
                source_file=os.path.basename(file_path),
                absolute_path=os.path.abspath(file_path),
                file_size_bytes=file_stats.st_size,
                disk_created_at=file_stats.st_ctime,
                read_completed_at=time.time(),
            )
        )
