from app.utils.logger import get_logger
from app.utils.pdf_parser import extract_text
from app.services.chunker import chunk_text
from app.services.embeddings import parallel_embeddings
from app.services.vector_db import store_chunks
from app.services.ipo_analyzer import analyze_document
from app.db.supabase_client import supabase
from app.workers.celery_app import celery_app

logger = get_logger(__name__)

@celery_app.task(
    bind=True,
    autoretry_for=(Exception,),
    retry_backoff=True,
    time_limit=600
)
def process_document(doc_id, file_url):

    logger.info("Starting document processing: %s", doc_id)

    text = extract_text(file_url)

    logger.debug("Extracted text length: %s", len(text))

    chunks = chunk_text(text)

    logger.debug("Chunks created: %s", len(chunks))

    embeddings = parallel_embeddings(chunks)

    logger.debug("Embeddings generated: %s", len(embeddings))

    store_chunks(doc_id, chunks, embeddings)

    logger.info("Vectors stored")

    analysis = analyze_document(text)

    supabase.table("documents").update({
        "status": "ready",
        "ipo_score": analysis["score"]
    }).eq("id", doc_id).execute()

    logger.info("Processing complete")
