from typing import List, Dict

from vectordb import VectorDB
from convert_to_embed import ImageEmbedder
from metadata_db import get_items


class LostService:
    def __init__(self):
        self.vectordb = VectorDB()
        self.embedder = ImageEmbedder()

    def search_lost_item(self, image_path: str, top_k: int = 5) -> List[Dict]:
        """
        Searches for similar found items using an image.
        image_path: path to lost item image
        top_k: number of results to return
        """

        # 1️⃣ Convert image to embedding
        embedding = self.embedder.image_to_embedding(image_path)

        # 2️⃣ Query vector DB
        item_ids = self.vectordb.query(embedding, top_k=top_k)

        if not item_ids:
            return []

        # 3️⃣ Fetch metadata for matched IDs
        items = get_items(item_ids)

        return items