# Stable Diffusion Endpoint with FastAPI and AWS EC2

This project uses FastAPI to create an endpoint that returns an image generated from a text prompt using [Stability-AI's Stable Diffusion model](https://github.com/Stability-AI/stablediffusion). If you run it on your local machine it will use your Nvidia GPU and CUDA if you have one or your CPU otherwise (this will take a lot longer). Alternatively, you can can run it on an AWS EC2 GPU Instance using the instructions below. If you would like to upload images to an S3 bucket and return the image url instead of returning the raw image bytes then check out the [s3 branch](https://github.com/martin-bartolo/stablediffusion-fastapi/tree/s3).

This code is tested using Python 3.10 and diffusers 0.21.4

These instructions assume that you have already set-up everything using the instructions on the main branch

## Instructions To Use an S3 Bucket

1. Create an s3 bucket

   Create your s3 bucket, ensuring to make it public and create an AMI key to access it. Add the following policy to the bucket so that you can access the images that you create using their url

   ```json
   {
   	"Version": "2012-10-17",
   	"Statement": [
   		{
   			"Sid": "PublicReadGetObject",
   			"Effect": "Allow",
   			"Principal": "*",
   			"Action": "s3:GetObject",
   			"Resource": "arn:aws:s3:::stable-diffusion-martin/*"
   		}
   	]
   }
   ```

2. ssh into your EC2 instance

3. switch to the s3 branch

   ```bash
   git checkout s3
   ```

4. Install requirements.txt

   ```bash
   pip install -r requirements.txt
   ```

5. Create a .env file and enter your AWS credentials

   Create the .env file

   ```bash
   sudo nano .env
   ```

   Input the following ensuring to use your correct credentials
   AWS_ACCESS_KEY_ID=...
   AWS_SECRET_ACCESS_KEY=...
   AWS_REGION_NAME=...

   Save the file and exit

6. Start up uvicorn server using

   ```bash
   uvicorn main:app
   ```

7. Run the request example using

   ```bash
   python request-example.py
   ```
