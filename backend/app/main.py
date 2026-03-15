from fastapi import FastAPI
from app.api import upload, chat, status
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="ProspectIQ")

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router)
app.include_router(chat.router)
app.include_router(status.router)

@app.get("/")
def health():
    return {"status": "running"}
