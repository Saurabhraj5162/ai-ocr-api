import shutil
import uuid
from pathlib import Path

import pytesseract
from app.database import SessionLocal
from app.models.ocr_results import OcrResults
from app.services.read_image import read_image
from fastapi import APIRouter, BackgroundTasks, Depends, File, UploadFile
from PIL import Image
from sqlalchemy.orm import Session

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()


@router.post("/ocr", response_model=dict)
async def perform_ocr(file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_extension = file.filename.split(".")[-1]
    unique_filename = f"{uuid.uuid4()}.{file_extension}"
    file_location = Path("temp_files") / unique_filename

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = read_image(file_location)

    # creating and saving ocr result in db:
    ocr_record = OcrResults()
    ocr_record.file_name = unique_filename
    ocr_record.text = text
    db.add(ocr_record)
    db.commit()
    db.refresh(ocr_record)

    # removing temp:
    file_location.unlink()
    return {
        "id": ocr_record.id,
        "filename": ocr_record.filename,
        "text": ocr_record.text,
    }
