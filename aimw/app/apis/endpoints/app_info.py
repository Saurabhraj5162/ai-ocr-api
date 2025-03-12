from fastapi import APIRouter

router = APIRouter()

@router.get("/info")
def app_info():
    return {"Hello! Welcome to Image to Text generation."}


