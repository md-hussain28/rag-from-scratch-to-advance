import re
from typing import List
from app.ingestion.models import ParsedDocument, ParserMetrics

class LayoutParser:
    """
    Node 2: Structural Extraction Layer.
    Processes the document body to separate layout streams, identify 
    headings, and isolate data tables into structured Python matrix arrays.
    """
    def parse(self, raw_bytes: bytes) -> ParsedDocument:
        # Decode the byte buffer safely using error mitigation replacements
        raw_stream = raw_bytes.decode("utf-8", errors="replace")
        
        # Isolate metadata fields embedded at the file level
        extracted_title = "Document Fragment"
        title_match = re.search(r"Title:\s*(.*)\n", raw_stream, re.IGNORECASE)
        if title_match:
            extracted_title = title_match.group(1).strip()

        # Isolate layout data blocks from embedded narrative content
        # For our framework-free extraction strategy, we locate data rows using matching rules
        table_rows: List[List[str]] = []
        narrative_accumulator: List[str] = []
        
        lines = raw_stream.splitlines()
        for line in lines:
            trimmed = line.strip()
            if not trimmed:
                continue
                
            # Table Row Rule: Detect tabular boundaries using delimiter patterns (e.g., pipe characters)
            if trimmed.startswith("|") and trimmed.endswith("|"):
                cells = [cell.strip() for cell in trimmed.split("|")[1:-1]]
                table_rows.append(cells)
            else:
                narrative_accumulator.append(trimmed)

        return ParsedDocument(
            title=extracted_title,
            raw_text_flow="\n".join(narrative_accumulator),
            isolated_tables=table_rows,
            parser_metrics=ParserMetrics(
                extracted_lines=len(lines),
                has_tables=len(table_rows) > 0,
            ),
        )