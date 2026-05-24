from typing import List



class Chunker:
    def __init__(self):
        self.chunk_size = 1000
        self.chunk_overlap = 100

    def chunk(self, text: str) -> List[str]:
        chunks = []
        for i in range(0, len(text), self.chunk_size):
            chunks.append(text[i:i+self.chunk_size])
        return chunks