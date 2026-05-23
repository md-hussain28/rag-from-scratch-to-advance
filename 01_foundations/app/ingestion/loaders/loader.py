import os
import time
from typing import Dict, Type
from app.ingestion.models import LoadedFile
from app.ingestion.loaders.pdf_loader import PDFLoader
from app.ingestion.loaders.docx_loader import DocxLoader
from app.constants import MAX_FILE_SIZE, SUPPORTED_FILE_EXTENSIONS

# ==========================================
# 1. CENTRAL ROUTER LOADER (The Factory)
# ==========================================

class CentralLoader:
    """
    The Orchestrator Node. Inspects file properties, enforces universal 
    guardrails, and routes files to the correct specialized parser.
    """
    def __init__(self, max_bytes: int = MAX_FILE_SIZE):
        self.max_bytes = max_bytes
        # Map extensions to their corresponding class constructors
        self._registry: Dict[str, Type] = {
            ".pdf": PDFLoader,
            ".docx": DocxLoader
        }

    def load_document(self, file_path: str) -> LoadedFile:
        # Guardrail 1: Universal Existence Check
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File missing at path: {file_path}")

        # Guardrail 2: Universal Size Check
        file_stats = os.stat(file_path)
        if file_stats.st_size > self.max_bytes:
            raise ValueError(f"File exceeds maximum safety allocation: {file_stats.st_size} bytes")

        # Routing Step: Extract extension (e.g., '.pdf')
        _, ext = os.path.splitext(file_path.lower())

        if ext not in self._registry:
            raise ValueError(f"Unsupported file extension '{ext}'. Allowed: {list(self._registry.keys())}")

        # Instantiate the correct loader dynamically and execute it
        worker_class = self._registry[ext]
        worker_instance = worker_class()
        
        print(f"⚙️ Routing '{ext}' file to specialized {worker_class.__name__}...")
        return worker_instance.load(file_path, file_stats)

# ==========================================
#  TESTING LOCAL VERIFICATION
# ==========================================
if __name__ == "__main__":
    # Let's create a quick dummy tester file
    test_file = "sample_document.docx"
    with open(test_file, "w") as f:
        f.write("Mock Word Data")

    try:
        # Initialize the central manager
        central_manager = CentralLoader()
        
        # Process the file through the system
        result: LoadedFile = central_manager.load_document(test_file)
        
        print("\n🎉 SUCCESSFUL PRODUCTION-GRADE EXTRACTION")
        print(f"Data Type Verified: {type(result)}")
        print(f"Extracted Text:     {result.content}")
        print(f"Validated Size:     {result.metadata.file_size_bytes} bytes")
        
    finally:
        if os.path.exists(test_file):
            os.remove(test_file)