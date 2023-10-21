from fastapi import FastAPI
from fastapi.responses import Response
from utils import generate_image
from io import BytesIO

app = FastAPI()


@app.get("/generate")
async def get_image(prompt: str):
    image = await generate_image(prompt)

    # Convert PIL image to bytes
    image_bytes = BytesIO()
    image.save(image_bytes, format='PNG')

    return Response(content=image_bytes.getvalue(), media_type="image/png")
