from fastapi import APIRouter
from app.apis.endpoints import app_info, ocr

api_router = APIRouter()

api_router.include_router(app_info.router, prefix="/info", tags=[''])
api_router.include_router(ocr.router, prefix="/ocr", tags=["ocr"])