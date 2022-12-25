import requests
import os
import random
import datetime

from urllib.parse import urlparse, unquote
from dotenv import load_dotenv
load_dotenv()


splitext = os.path.splitext
nasa_api_token = os.environ["NASA_API_TOKEN"]

def download_image(url, path):
    params = {
        "api_key": nasa_api_token
    }
    response = requests.get(url,params=params)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)

def get_spacex_images():
    response = requests.get('https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a')
    response.raise_for_status()
    images_info = response.json()
    all_images_links = images_info['links']['flickr']['original']
    return all_images_links

def fetch_spacex_last_launch():
    images = get_spacex_images()
    for image_number, images in enumerate(images):
        download_image(images, f'images/spacex{image_number}.jpg')

def get_ext(url):
    url_parse = urlparse(url)
    unquote_parse = unquote(url_parse.scheme + url_parse.netloc + url_parse.path)
    extension = splitext(unquote_parse)[1]
    return extension

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
        download_image(f'https://api.nasa.gov/EPIC/archive/natural/{image_date}/png/{image_name}.png', f'images/epic_{epic_number}.png')

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
        download_image(nasa_info['url'], f'images/nasa_apod_{image_number}{extension}')



# download_image("https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg", 'images/hubble.jpeg')
# get_spacex_images()
# fetch_spacex_last_launch()
# download_nasa_images('https://api.nasa.gov/planetary/apod')
get_epic_image('https://api.nasa.gov/EPIC/api/natural/images')