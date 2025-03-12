import asyncio
from pathlib import Path

import pytesseract
from PIL import Image


async def read_image(input_image_path: Path, lang="eng"):
    try:
        text = pytesseract.image_to_string(input_image_path, lang=lang)
        await asyncio.sleep(2)
        return text
    except Exception as e:
        return f"ERROR occured while converting image to string : {e}"
