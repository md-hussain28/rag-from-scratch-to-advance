# /// script
# requires-python = ">=3.10"
# ///
"""
Execution Entrypoint: app/main.py
Coordinates the full ingestion sequence for local development testing.
"""

from app.ingestion.pipeline import IngestionPipeline


def main():
    pipeline = IngestionPipeline()
    result = pipeline.process_file("data/dummy.pdf")

   


if __name__ == "__main__":
    main()