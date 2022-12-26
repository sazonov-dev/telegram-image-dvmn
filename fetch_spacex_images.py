import requests
import argparse

from download_image import download_img
parser = argparse.ArgumentParser()
parser.add_argument('id', nargs='*')
args = parser.parse_args()


def get_spacex_image(id):
    response = requests.get(f'https://api.spacexdata.com/v5/launches/{id}')
    response.raise_for_status()
    images_info = response.json()
    all_images_links = get_images_links(images_info)
    return download_spacex_image(all_images_links)

def fetch_spacex_last_launch():
    response = requests.get(f'https://api.spacexdata.com/v5/launches/latest')
    response.raise_for_status()
    last_launch = response.json()
    all_images_links = get_images_links(last_launch)
    if not all_images_links:
        return 'Ссылки на изображение не существует'
    else:
        return download_spacex_image(all_images_links)

def download_spacex_image(images):
    for image_number, images in enumerate(images):
        download_img(images, f'images/spacex_{image_number}.jpg')

def get_images_links(response):
    return response['links']['flickr']['original']

def download_spacex_main():
    if not args.id:
        return fetch_spacex_last_launch()
    else:
        return get_spacex_image(args.id)

download_spacex_main()