import os.path
from urllib.parse import urlparse, unquote

def get_ext(url):
    url = urlparse(url)
    url_unquote = unquote(url.scheme + url.netloc + url.path)
    for element in url_unquote:
        if element == '%s' or element == '+':
            url_unquote.replace(element, '')
    extension = os.path.splitext(url_unquote)[1]
    return extension