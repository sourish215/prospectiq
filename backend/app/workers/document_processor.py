from app.utils.pdf_parser import extract_text
from app.services.chunker import chunk_text
from app.services.embeddings import create_embedding
from app.services.vector_db import store_chunks
from app.services.ipo_analyzer import analyze_document
from app.db.supabase_client import supabase
from app.utils.logger import get_logger

logger = get_logger(__name__)

def process_document(doc_id, file_url):

    text = extract_text(file_url)

    chunks = chunk_text(text)

    embeddings = [create_embedding(chunk) for chunk in chunks]

    store_chunks(doc_id, chunks, embeddings)

    analysis = analyze_document(text)

    supabase.table("documents").update({
        "status": "ready",
        "ipo_score": analysis["score"]
    }).eq("id", doc_id).execute()
