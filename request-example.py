import requests
from PIL import Image
from io import BytesIO

url = 'http://127.0.0.1:8000/generate'
params = {'prompt': 'Astronaut riding a bicycle in space'}

response = requests.get(url, params=params)

image_bytes = response.content
img = Image.open(BytesIO(image_bytes))
img.show()
