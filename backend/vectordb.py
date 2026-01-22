import chromadb
from chromadb.config import Settings
from typing import List


class VectorDB:
    def __init__(self, persist_dir: str = "chroma_db"):
        self.client = chromadb.Client(
            Settings(
                persist_directory=persist_dir,
                anonymized_telemetry=False
            )
        )

        self.collection = self.client.get_or_create_collection(
            name="lost_and_found"
        )

    def add_embedding(self, item_id: str, embedding: List[float]):
        self.collection.add(
            ids=[item_id],
            embeddings=[embedding]
        )

    def query(self, embedding: List[float], top_k: int = 5) -> List[str]:
        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=top_k
        )

        return results["ids"][0]