from fastapi import APIRouter, UploadFile
import uuid

from app.services.storage import upload_file
from app.db.supabase_client import supabase
from app.workers.document_processor import process_document

router = APIRouter()


@router.post("/upload")
async def upload_document(file: UploadFile):

    doc_id = str(uuid.uuid4())

    file.file.seek(0)

    file_url = upload_file(file.file, f"{doc_id}.pdf")

    supabase.table("documents").insert({
        "id": doc_id,
        "file_url": file_url,
        "status": "processing"
    }).execute()

    process_document(doc_id, file_url)

    return {"document_id": doc_id}

