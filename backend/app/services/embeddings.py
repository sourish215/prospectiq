import requests
from app.config import HF_TOKEN

API_URL = "https://router.huggingface.co/hf-inference/models/BAAI/bge-small-en"

def create_embedding(text):

    headers = {
        "Authorization": f"Bearer {HF_TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        API_URL,
        headers=headers,
        json={"inputs": text}
    )

    data = response.json()

    print("Embedding response:", data)

    if isinstance(data, dict) and "error" in data:
        raise Exception(data["error"])
    
    embedding = data

    return embedding
