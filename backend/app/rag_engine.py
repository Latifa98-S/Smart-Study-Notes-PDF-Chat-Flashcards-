import numpy as np
from sentence_transformers import SentenceTransformer
import faiss

MODEL_NAME = "all-MiniLM-L6-v2"

class RAGEngine:
    def __init__(self):
        self.model = SentenceTransformer(MODEL_NAME)
        self.index = None
        self.chunks = []

    def chunk_text(self, text, chunk_size=500, overlap=100):
        words = text.split()
        chunks = []

        for i in range(0, len(words), chunk_size - overlap):
            chunk = " ".join(words[i:i + chunk_size])
            if chunk.strip():
                chunks.append(chunk)

        return chunks

    def build_index(self, texts):
        self.chunks = texts
        embeddings = self.model.encode(texts, show_progress_bar=True)

        dim = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(embeddings.astype("float32"))

    def search(self, query, k=4):
        if self.index is None:
            return []

        query_vec = self.model.encode([query]).astype("float32")
        distances, indices = self.index.search(query_vec, k)

        return [self.chunks[i] for i in indices[0]]
