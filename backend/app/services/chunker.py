from app.utils import logger
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.utils.logger import get_logger

logger = get_logger(__name__)

def chunk_text(text):
    logger.debug("Chunking document")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=200
    )

    return splitter.split_text(text)
