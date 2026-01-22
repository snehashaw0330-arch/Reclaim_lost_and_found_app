from sentence_transformers import SentenceTransformer
from PIL import Image
from typing import List


class ImageEmbedder:
    def __init__(self):
        # CLIP model for image embeddings
        self.model = SentenceTransformer("clip-ViT-B-32")

    def image_to_embedding(self, image_path: str) -> List[float]:
        """
        Converts an image to a vector embedding.
        """
        image = Image.open(image_path).convert("RGB")
        embedding = self.model.encode(image)

        # Convert numpy array to Python list
        return embedding.tolist()