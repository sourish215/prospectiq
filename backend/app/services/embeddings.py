import requests
from app.config import HF_TOKEN
from app.utils.logger import get_logger
from concurrent.futures import ThreadPoolExecutor

logger = get_logger(__name__)

API_URL = "https://router.huggingface.co/hf-inference/models/BAAI/bge-small-en"

BATCH_SIZE = 32

MAX_WORKERS = 5


def batch_embeddings(batch):

    headers = {
        "Authorization": f"Bearer {HF_TOKEN}",
        "Content-Type": "application/json"
    }

    logger.debug("Embedding batch size: %s", len(batch))

    response = requests.post(
        API_URL,
        headers=headers,
        json={"inputs": batch},
        timeout=30
    )

    data = response.json()

    if isinstance(data, dict) and "error" in data:
        raise Exception(data["error"])

    return data

def parallel_embeddings(chunks):
    logger.debug("Total chunks: %s", len(chunks))

    batches = [chunks[i:i+BATCH_SIZE] for i in range(0, len(chunks), BATCH_SIZE)]

    logger.debug("Total batches: %s", len(batches))

    embeddings = []

    with ThreadPoolExecutor(MAX_WORKERS) as executor:

        results = executor.map(batch_embeddings, batches)

    for result in results:
        embeddings.extend(result)

    return embeddings

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
