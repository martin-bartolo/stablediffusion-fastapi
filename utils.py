import torch
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
from PIL import Image

model_id = "stabilityai/stable-diffusion-2-1"
pipe = StableDiffusionPipeline.from_pretrained(model_id)
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)

device = 'cuda' if torch.cuda.is_available() else 'cpu'
pipe = pipe.to(device)


async def generate_image(prompt: str) -> Image:
    images = pipe(prompt=prompt)[0]
    return images[0]
