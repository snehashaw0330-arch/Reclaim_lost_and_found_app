import os
import uuid
from typing import Dict

from metadata_db import insert_item
from vectordb import VectorDB
from convert_to_embed import ImageEmbedder


UPLOAD_DIR = "uploads"


class FoundService:
    def __init__(self):
        os.makedirs(UPLOAD_DIR, exist_ok=True)

        self.vectordb = VectorDB()
        self.embedder = ImageEmbedder()

    def post_found_item(self, image_file, contact_number: str) -> Dict:
        """
        Handles the logic for posting a found item.
        image_file: file-like object (from Flask later)
        contact_number: string
        """

        # 1️⃣ Generate unique ID
        item_id = str(uuid.uuid4())

        # 2️⃣ Save image to disk
        image_path = os.path.join(UPLOAD_DIR, f"{item_id}.jpg")
        image_file.save(image_path)

        # 3️⃣ Convert image to embedding
        embedding = self.embedder.image_to_embedding(image_path)

        # 4️⃣ Store embedding in Vector DB
        self.vectordb.add_embedding(item_id, embedding)

        # 5️⃣ Store metadata
        insert_item(
            item_id=item_id,
            image_path=image_path,
            contact_number=contact_number
        )

        return {
            "id": item_id,
            "message": "Found item stored successfully"
        }