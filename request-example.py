import requests
from PIL import Image
from io import BytesIO

url = 'http://publicip/generate'
params = {'prompt': 'little boy juggling volcanoes'}

# Get the image url
url_response = requests.get(url, params=params)
url_response_data = url_response.json()
image_url = url_response_data['image_url']

# Get the image from the url
image_response = requests.get(image_url)
image_bytes = image_response.content
image = Image.open(BytesIO(image_bytes))
image.show()
