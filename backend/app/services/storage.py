from app.db.supabase_client import supabase
from app.config import SUPABASE_URL

BUCKET = "prospectiq-docs"

def upload_file(file, filename):
    file_bytes = file.read()

    supabase.storage.from_("prospectiq-docs").upload(
        filename,
        file_bytes,
        {"content-type": "application/pdf"}
    )

    url = f"{SUPABASE_URL}/storage/v1/object/public/{BUCKET}/{filename}"

    print(f"File uploaded to: {url}")

    return url
