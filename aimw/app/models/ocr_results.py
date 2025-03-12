from app.database import Base
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func


class OcrResults(Base):
    __tablename__ = "ocr_results"
    id = Column(Integer, primary_key=True, index=True)
    file_name = Column(String, index=True)
    text = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
