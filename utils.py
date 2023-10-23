import torch
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
from PIL import Image

model_id = "stabilityai/stable-diffusion-2-1"

if torch.cuda.is_available():
    device = 'cuda'
    pipe = StableDiffusionPipeline.from_pretrained(
        model_id, torch_dtype=torch.float16)
else:
    device = 'cpu'
    pipe = StableDiffusionPipeline.from_pretrained(model_id)

pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
pipe = pipe.to(device)


async def generate_image(prompt: str) -> Image:
    images = pipe(prompt=prompt)[0]
    return images[0]
