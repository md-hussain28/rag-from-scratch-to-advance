# /// script
# requires-python = ">=3.10"
# ///
"""
Execution Entrypoint: app/main.py
Coordinates the full ingestion sequence for local development testing.
"""

from app.ingestion.pipeline import IngestionPipeline
from app.chunking.chunking import Chunker
from statistics import mode

def main():
    pipeline = IngestionPipeline()
    result = pipeline.process_file("data/dummy.pdf")
    chunks = Chunker().chunk(result.markdown_content if result else "")
    for chunk in chunks:
        print(chunk)
        print("\n\n")
    print(f"Total chunks: {len(chunks)}")
    print(f"Total size: {sum(len(chunk) for chunk in chunks)}")
    print(f"Average chunk size: {sum(len(chunk) for chunk in chunks) / len(chunks)}")
    print(f"Max chunk size: {max(len(chunk) for chunk in chunks)}")
    print(f"Min chunk size: {min(len(chunk) for chunk in chunks)}")
    print(f"Median chunk size: {sorted(len(chunk) for chunk in chunks)[len(chunks) // 2]}")
    print(f"Mode chunk size: {mode(len(chunk) for chunk in chunks)}")
   
if __name__ == "__main__":
    main()