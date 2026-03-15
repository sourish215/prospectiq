from app.db.supabase_client import supabase
from app.utils.logger import get_logger

logger = get_logger(__name__)


def store_chunks(document_id, chunks, embeddings):

    rows = []

    for chunk, embedding in zip(chunks, embeddings):

        rows.append({
            "document_id": document_id,
            "chunk_text": chunk,
            "embedding": embedding
        })

    logger.debug("Storing %s chunks", len(rows))

    supabase.table("document_chunks").insert(rows).execute()
