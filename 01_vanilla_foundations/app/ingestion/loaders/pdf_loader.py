import os
import time
from app.constants import MAX_FILE_SIZE
from app.ingestion.models import FileMetadata, LoadedPDF

class PDFLoader:
    """
    Node 1: I/O Isolation Boundary.
    Safely reads file binaries into volatile heap space and collects
    immutable OS-level metadata tracking markers.
    """
    def __init__(self, max_bytes: int = MAX_FILE_SIZE):
        self.max_bytes = max_bytes

    def load(self, file_path: str) -> LoadedPDF:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Target ingestion binary path missing: {file_path}")
            
        file_stats = os.stat(file_path)
        if file_stats.st_size > self.max_bytes:
            raise ValueError(f"File size exceeds safety limit allocation boundary: {file_stats.st_size} bytes")

        # Open kernel-level binary read descriptor 
        with open(file_path, "rb") as f:
            binary_buffer = f.read()

        return LoadedPDF(
            content=binary_buffer,
            metadata=FileMetadata(
                source_file=os.path.basename(file_path),
                absolute_path=os.path.abspath(file_path),
                file_size_bytes=file_stats.st_size,
                disk_created_at=file_stats.st_ctime,
                read_completed_at=time.time(),
            ),
        )