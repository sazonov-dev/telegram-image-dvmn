import requests

from download_image import download_img

def fetch_spacex_image(id):
    if not id:
        response = requests.get(f'https://api.spacexdata.com/v5/launches/latest')
    else:
        response = requests.get(f'https://api.spacexdata.com/v5/launches/{id}')
    response.raise_for_status()
    spacex_response_content = response.json()
    download_spacex_image(spacex_response_content)

def download_spacex_image(response):
    images = response['links']['flickr']['original']
    for image_number, images in enumerate(images):
        download_img(images, f'images/spacex_{image_number}.jpg')

