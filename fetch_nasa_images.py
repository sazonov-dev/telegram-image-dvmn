import requests
import os
import random

from dotenv import load_dotenv
from download_image import download_img
from get_file_extension import get_ext
load_dotenv()
nasa_api_token = os.environ["NASA_API_TOKEN"]

def get_epic_image(url):
    params = {
        "api_key": nasa_api_token
    }
    response = requests.get(url,params=params)
    response.raise_for_status()
    epic_info = response.json()
    for epic_number, epic_info in enumerate(epic_info):
        image_name = epic_info['image']
        image_date = epic_info['date'].split(' ')[0].replace('-', '/')
        download_img(f'https://api.nasa.gov/EPIC/archive/natural/{image_date}/png/{image_name}.png', f'images/epic_{epic_number}.png')

def download_nasa_images(url):
    random_count = random.randint(30, 50)
    params = {
        "count": random_count,
        "api_key": nasa_api_token
    }
    response = requests.get(url, params=params)
    nasa_info = response.json()

    for image_number, nasa_info in enumerate(nasa_info):
        extension = get_ext(nasa_info['url'])
        if not extension:
            return
        download_img(nasa_info['url'], f'images/nasa_apod_{image_number}{extension}')