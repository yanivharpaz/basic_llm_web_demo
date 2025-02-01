from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os

class VectorStore:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.dimension = 384  # Output dimension of the model
        self.index = faiss.IndexFlatL2(self.dimension)
        self.texts = []

    def add_texts(self, texts):
        if not texts:
            return
        
        embeddings = self.model.encode(texts)
        self.index.add(np.array(embeddings).astype('float32'))
        self.texts.extend(texts)

    def search(self, query, k=3):
        query_vector = self.model.encode([query])
        distances, indices = self.index.search(np.array(query_vector).astype('float32'), k)
        
        results = []
        for idx in indices[0]:
            if idx != -1 and idx < len(self.texts):
                results.append(self.texts[idx])
        
        return results 