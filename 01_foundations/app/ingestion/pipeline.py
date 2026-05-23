import hashlib
from typing import Optional
from app.ingestion.loaders.loader import CentralLoader
from app.ingestion.parsers.parser import Parser
from app.ingestion.cleaners.unicode_cleaner import UnicodeCleaner
from app.ingestion.models import ParsedDocument, LoadedFile

class IngestionPipeline:
    """
    The Main Pipeline Coordinator.
    Directs data transformations across the three processing layers
    and runs deduplication checks before passing text down to chunking.
    """
    def __init__(self):
        self.loader = CentralLoader()
        self.parser = Parser()
        self.cleaner = UnicodeCleaner()
        # Thread-safe lookups matching previously seen content hashes
        self._processed_hashes = set()

    def process_file(self, file_path: str) -> Optional[ParsedDocument]:
        # Node 1: Execute Disk I/O stream into system memory
        file_payload = self.loader.load_document(file_path)
        print(f"File Payload: {file_payload} \n\n")
        # Node 2: Extract content layout into primitive data forms
        parsed_components = self.parser.parse(file_payload)
        print(f"Parsed Components: {parsed_components} \n\n")

        # Node 3: Sanitize text and build the unified Markdown structure
        # clean_markdown = self.cleaner.clean(
        #     title=parsed_components.title,
        #     raw_text=parsed_components.raw_text_flow,
        #     tables=parsed_components.isolated_tables,
        # )
        # print(f"Clean Markdown: {clean_markdown}")
        # # Content Deduplication Guard
        # content_hash = hashlib.sha256(clean_markdown.encode("utf-8")).hexdigest()
        # if content_hash in self._processed_hashes:
        #     return None # Skip downstream processing entirely

        # self._processed_hashes.add(content_hash)

        # return IngestionResult(
        #     document_hash=content_hash,
        #     markdown_content=clean_markdown,
        #     system_metadata=file_payload.metadata,
        #     parser_metrics=parsed_components.parser_metrics,
        # )