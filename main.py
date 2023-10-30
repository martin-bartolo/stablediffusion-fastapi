from fastapi import FastAPI
from fastapi.responses import JSONResponse
from utils import generate_image, s3_upload
from io import BytesIO

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/generate")
async def get_image(prompt: str):
    image = await generate_image(prompt)

    # Convert PIL image to bytes
    image_bytes = BytesIO()
    image.save(image_bytes, format='PNG')
    image_bytes.seek(0)

    # Upload image to s3 and get url
    s3_url = await s3_upload(image_bytes)
    return JSONResponse(content={"image_url": s3_url})
