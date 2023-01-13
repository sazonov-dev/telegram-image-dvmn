import requests

from download_image import download_img

def fetch_spacex_image(id):
    if not id:
        response = requests.get(f'https://api.spacexdata.com/v5/launches/latest')
    else:
        response = requests.get(f'https://api.spacexdata.com/v5/launches/{id}')
    response.raise_for_status()
    spacex_response_content = response.json()
    images = spacex_response_content['links']['flickr']['original']
    for image_number, image in enumerate(images):
        download_img(image, f'images/spacex_{image_number}.jpg')
