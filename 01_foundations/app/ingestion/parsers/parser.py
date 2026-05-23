from app.ingestion.models import LoadedFile, ParsedDocument, FileMetadata
import fitz
from app.constants import SUPPORTED_FILE_EXTENSIONS


class PDFParser:
    """
    The PDF Parser.
    Parses the PDF document and returns a structured output.
    """
    def parse(self, document: LoadedFile) -> ParsedDocument:
        doc = fitz.open(stream=document.content, filetype="pdf")
        page_texts = []
        for page in doc:
            text = page.get_text("text")
            page_texts.append(text)
        raw_text = "\n\n".join(page_texts).strip()
        title =  document.metadata.source_file
        return ParsedDocument(
            title=title,
            content=raw_text,
            metadata=document.metadata,
        )
        

class DocxParser:
    """
    The Docx Parser.
    Parses the Docx document and returns a structured output.
    """
    def parse(self, document: LoadedFile) -> ParsedDocument:
        if document.metadata.file_extension != ".docx":
            raise ValueError(f"Unsupported file extension: {document.metadata.file_extension}")
        return ParsedDocument(
            title=document.metadata.source_file,
            content="Not implmented YET",
            metadata=document.metadata,
        )

class Parser:
    """
    The Parser Node.
    Parses the document and returns a structured output.
    """
    def __init__(self):
        self.supported_file_extensions = SUPPORTED_FILE_EXTENSIONS

    def parse(self, document: LoadedFile) -> ParsedDocument:
        if document.metadata.file_extension == ".pdf":
            return PDFParser().parse(document)
        elif document.metadata.file_extension == ".docx":
            return DocxParser().parse(document)
        else:
            raise ValueError(f"Unsupported file extension: {document.metadata.file_extension}")