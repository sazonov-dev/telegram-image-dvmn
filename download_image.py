import requests

def download_image(file_url, path):
    response = requests.get(file_url)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)

def get_spacex_images():
    response = requests.get('https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a')
    response.raise_for_status()
    images_info = response.json()
    all_images_links = images_info['links']['flickr']['original']
    return all_images_links

def download_all_images():
    images = get_spacex_images()
    for image_number, images in enumerate(images):
        download_image(images, f'images/spacex{image_number}.jpg')

# download_image("https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg", 'images/hubble.jpeg')
# get_spacex_images()
download_all_images()