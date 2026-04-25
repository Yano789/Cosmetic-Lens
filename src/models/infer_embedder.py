import torch
import numpy as np
from PIL import Image
import clip

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"


class CLIPInference:
    def __init__(self):
        self.model, self.preprocess = clip.load("ViT-B/32", device=DEVICE)

    def embed(self, image_path):
        image = Image.open(image_path).convert("RGB")
        image = self.preprocess(image).unsqueeze(0).to(DEVICE)

        with torch.no_grad():
            features = self.model.encode_image(image)
            features /= features.norm(dim=-1, keepdim=True)

        return features.cpu().numpy().flatten()


if __name__ == "__main__":
    model = CLIPInference()
    emb = model.embed("tests/test_image.jpeg") #Test!!
    print(emb.shape)