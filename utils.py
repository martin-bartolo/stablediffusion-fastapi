from io import BytesIO
from dotenv import load_dotenv
import torch
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
from PIL import Image
import boto3
import uuid
import os

# Model Setup
model_id = "stabilityai/stable-diffusion-2-1"

if torch.cuda.is_available():
    print('Found a GPU')
    device = 'cuda'
    pipe = StableDiffusionPipeline.from_pretrained(
        model_id, torch_dtype=torch.float16)
else:
    print('No GPU Found. Using CPU')
    device = 'cpu'
    pipe = StableDiffusionPipeline.from_pretrained(model_id)

pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
pipe = pipe.to(device)


async def generate_image(prompt: str) -> Image:
    images = pipe(prompt=prompt)[0]
    return images[0]


# Amazon S3 setup
load_dotenv()
s3 = boto3.client('s3',
                  aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                  aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                  region_name=os.getenv('AWS_REGION_NAME'))
bucket_name = 'stable-diffusion-martin'


async def s3_upload(image_bytes: BytesIO) -> str:
    image_name = str(uuid.uuid4()) + ".png"
    s3.upload_fileobj(image_bytes, bucket_name, image_name)
    return f"https://{bucket_name}.s3.amazonaws.com/{image_name}"
