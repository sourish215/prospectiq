from fastapi import APIRouter
from app.db.supabase_client import supabase

router = APIRouter()

@router.get("/status/{doc_id}")
def get_status(doc_id: str):

    res = supabase.table("documents").select("*").eq("id", doc_id).execute()

    return res.data
