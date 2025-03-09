from fastapi import APIRouter
from PIL import Image
import pytesseract

router = APIRouter()

router.post("/ocr")
def perform_ocr(request):
    return pytesseract.image_to_string(Image.open(request))
