from fastapi import FastAPI
from app.api import upload, chat, status

app = FastAPI(title="ProspectIQ")

app.include_router(upload.router)
app.include_router(chat.router)
app.include_router(status.router)

@app.get("/")
def health():
    return {"status": "running"}
