import os
import torch
import numpy as np
from PIL import Image
from tqdm import tqdm
import clip

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"


class CLIPEmbedder:
    def __init__(self):
        self.model, self.preprocess = clip.load("ViT-B/32", device=DEVICE)

    def embed(self, image):
        image = self.preprocess(image).unsqueeze(0).to(DEVICE)

        with torch.no_grad():
            features = self.model.encode_image(image)
            features /= features.norm(dim=-1, keepdim=True)

        return features.cpu().numpy().flatten()


def generate_embeddings(image_folder, output_path="outputs/embeddings.npy"):
    embedder = CLIPEmbedder()

    embeddings = []
    image_paths = []

    for file in tqdm(os.listdir(image_folder)):
        if file.endswith((".jpg", ".png")):
            path = os.path.join(image_folder, file)
            image = Image.open(path).convert("RGB")

            emb = embedder.embed(image)

            embeddings.append(emb)
            image_paths.append(path)

    np.save(output_path, np.array(embeddings))
    np.save("outputs/image_paths.npy", np.array(image_paths))


if __name__ == "__main__":
    generate_embeddings("data/images")