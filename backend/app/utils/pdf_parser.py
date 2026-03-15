from pypdf import PdfReader
import requests
import io
from app.utils.logger import get_logger

logger = get_logger(__name__)

def extract_text(file_url):
    logger.debug("Downloading PDF from %s", file_url)

    response = requests.get(file_url)

    if response.status_code != 200:
        raise Exception("Failed to download PDF")

    pdf_bytes = io.BytesIO(response.content)

    reader = PdfReader(pdf_bytes)

    logger.debug("Extracting text")

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text
    
    logger.debug("Text length: %s", len(text))
    
    return text
