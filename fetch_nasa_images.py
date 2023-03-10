import requests
import os
import random

from download_image import download_img
from get_file_extension import get_ext

def get_epic_image(url, nasa_api_token):
    params = {
        "api_key": nasa_api_token
    }
    response = requests.get(url,params=params)
    response.raise_for_status()
    nasa_response_content = response.json()
    for epic_number, epic_image in enumerate(nasa_response_content):
        image_name = epic_image['image']
        image_date = epic_image['date'].split(' ')[0].replace('-', '/')
        url = f'https://api.nasa.gov/EPIC/archive/natural/{image_date}/png/{image_name}.png'
        response = requests.get(url,params=params)
        response.raise_for_status()
        with open(f'images/epic_{epic_number}.png', 'wb') as file:
            file.write(response.content)

def download_nasa_images(url, nasa_api_token):
    random_count = random.randint(30, 50)
    params = {
        "count": random_count,
        "api_key": nasa_api_token
    }
    response = requests.get(url, params=params)
    nasa_response_content = response.json()
    for image_number, nasa_image in enumerate(nasa_response_content):
        extension = get_ext(nasa_image['url'])
        if not extension:
            return
        download_img(nasa_image['url'], f'images/nasa_apod_{image_number}{extension}')