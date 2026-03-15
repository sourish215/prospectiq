from fastapi import APIRouter, UploadFile, BackgroundTasks
import uuid

from app.services.storage import upload_file
from app.db.supabase_client import supabase
from app.workers.document_processor import process_document
from app.utils.logger import get_logger

router = APIRouter()
logger = get_logger(__name__)


@router.post("/upload")
async def upload_document(file: UploadFile, background_tasks: BackgroundTasks):

    logger.info("Upload request received")

    doc_id = str(uuid.uuid4())

    file.file.seek(0)

    file_url = upload_file(file.file, f"{doc_id}.pdf")

    logger.info("File uploaded: %s", file_url)

    supabase.table("documents").insert({
        "id": doc_id,
        "file_url": file_url,
        "status": "processing"
    }).execute()

    process_document.delay(doc_id, file_url)

    return {
        "document_id": doc_id,
        "status": "processing"
    }