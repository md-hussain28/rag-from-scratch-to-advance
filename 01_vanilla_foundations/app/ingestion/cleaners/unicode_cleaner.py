import unicodedata
from typing import List

class UnicodeCleaner:
    """
    Node 3: Sanitization & Standardization Layer.
    Fixes character encoding variations, strips control sequences, 
    and converts extracted arrays into unified Markdown text.
    """
    def clean(self, title: str, raw_text: str, tables: List[List[str]]) -> str:
        # Step 1: Enforce uniform NFC normalization to resolve byte discrepancies
        normalized_title = unicodedata.normalize("NFC", title.strip())
        normalized_text = unicodedata.normalize("NFC", raw_text)
        
        # Step 2: Strip non-printable and invalid control characters
        sanitized_text = "".join(
            ch for ch in normalized_text if unicodedata.category(ch)[0] != "C" or ch in "\n\t"
        )
        
        # Standardize whitespace variations across layout runs
        clean_narrative = "\n\n".join(
            " ".join(paragraph.split()) for paragraph in sanitized_text.split("\n\n") if paragraph.strip()
        )

        # Step 3: Format text and structured matrices into clean Markdown syntax
        markdown_output = f"# {normalized_title}\n\n{clean_narrative}\n\n"
        
        if tables and len(tables) > 0:
            headers = tables[0]
            data_rows = tables[1:]
            
            # Construct standard Markdown table headers and lines
            markdown_output += "| " + " | ".join(headers) + " |\n"
            markdown_output += "| " + " | ".join(["---"] * len(headers)) + " |\n"
            
            # Append rows securely
            for row in data_rows:
                # Pad row segments if short to maintain structural alignment
                if len(row) < len(headers):
                    row.extend([""] * (len(headers) - len(row)))
                markdown_output += "| " + " | ".join(row[:len(headers)]) + " |\n"

        return markdown_output.strip()