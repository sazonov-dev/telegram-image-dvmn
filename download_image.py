import requests

def download_image(file_url, path):
    response = requests.get(file_url)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)

download_image("https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg", 'images/hubble.jpeg')