import os

from urllib.parse import urlparse, unquote
splitext = os.path.splitext


def get_ext(url):
    url_parse = urlparse(url)
    unquote_parse = unquote(url_parse.scheme + url_parse.netloc + url_parse.path)
    extension = splitext(unquote_parse)[1]
    return extension