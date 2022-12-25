import requests
import os

from urllib.parse import urlparse, unquote
from dotenv import load_dotenv
load_dotenv()


splitext = os.path.splitext
nasa_api_token = os.environ["NASA_API_TOKEN"]

def download_image(url, path):
    response = requests.get(url)
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
    response = requests.get(url + nasa_api_token)
    response.raise_for_status()
    nasa_info = response.json()
    url_parse = urlparse(nasa_info['url'])
    unquote_parse = unquote(url_parse.scheme + url_parse.netloc + url_parse.path)
    extension = splitext(unquote_parse)[1]
    return extension



# download_image("https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg", 'images/hubble.jpeg')
# get_spacex_images()
# fetch_spacex_last_launch()

get_ext('https://api.nasa.gov/planetary/apod?api_key=')