import requests
from app.config import HF_API_KEY

API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"

def create_embedding(text):

    headers = {"Authorization": f"Bearer {HF_API_KEY}"}

    response = requests.post(
        API_URL,
        headers=headers,
        json={"inputs": text}
    )

    embedding = response.json()

    # flatten embedding
    if isinstance(embedding[0], list):
        embedding = embedding[0]

    return embedding

