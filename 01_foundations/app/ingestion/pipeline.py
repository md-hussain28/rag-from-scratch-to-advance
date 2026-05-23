import hashlib
from typing import Optional
from app.ingestion.loaders.loader import CentralLoader
from app.ingestion.parsers.parser import Parser
from app.ingestion.cleaners.cleaner import Cleaner
from app.ingestion.models import IngestionResult

class IngestionPipeline:
    def __init__(self):
        self.loader = CentralLoader()
        self.parser = Parser()
        self.cleaner = Cleaner()

    def process_file(self, file_path: str) -> Optional[IngestionResult]:

        file_payload = self.loader.load_document(file_path)
        print(f"File Payload: {file_payload} \n\n")

        parsed_components = self.parser.parse(file_payload)
        print(f"Parsed Components: {parsed_components} \n\n")

        #Node 3: Sanitize text and build the unified Markdown structure
        clean_markdown = self.cleaner.clean(
            title=parsed_components.title,
            raw_text=parsed_components.content,
        )
        print(f"Clean Markdown: {clean_markdown} \n\n")

        # Content Deduplication Guard
        # TODO: Implement content deduplication guard

        return IngestionResult(
            document_hash=hashlib.sha256(clean_markdown.encode("utf-8")).hexdigest(),
            markdown_content=clean_markdown,
            system_metadata=file_payload.metadata,
        )