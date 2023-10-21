# Stable Diffusion Endpoint Returning an Image with FastAPI

This project uses FastAPI to create an endpoint that returns an image generated from a text prompt using [Stability-AI's Stable Diffusion model](https://github.com/Stability-AI/stablediffusion/blob/main/scripts/txt2img.py).

This code is tested using python 3.10 and diffusers 0.21.4

## Instructions To Run

1. Install requirements.txt

   ```bash
   pip install -r requirements.txt
   ```

2. Start up uvicorn server using

   ```bash
   uvicorn main:app
   ```

3. Run the request example using

   ```bash
   python request-example.py
   ```
