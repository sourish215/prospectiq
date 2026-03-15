from fastapi import APIRouter
from app.services.embeddings import create_embedding
from app.services.search import search_chunks

router = APIRouter()

@router.post("/chat")
def chat(question: str):

    embedding = create_embedding(question)

    chunks = search_chunks(embedding)

    return {"results": chunks}
