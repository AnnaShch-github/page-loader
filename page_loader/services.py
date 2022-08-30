import os
import re
import requests


from page_loader.logger import logger
from urllib.parse import urlparse


def get_file_name(link):
    first_step = urlparse(link)
    second_step = ''.join([first_step.netloc, first_step.path])
    file_name, extension = os.path.splitext(second_step)
    re_file_name = re.sub(r'[^0-9a-zA-Z]', r'-', file_name)
    if not extension:
        extension = '.html'
    result = ''.join([re_file_name, extension])
    return result


def get_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.HTTPError as http_error:
        logger.error(http_error)
        raise requests.HTTPError(http_error)
    except requests.ConnectionError as connection_error:
        logger.error(connection_error)
        raise requests.ConnectionError(connection_error)
    except requests.URLRequired as url_error:
        logger.error(url_error)
        raise requests.URLRequired(url_error)
    except requests.TooManyRedirects as redirects_error:
        logger.error(redirects_error)
        raise requests.TooManyRedirects(redirects_error)
    except requests.Timeout as timeout_error:
        logger.error(timeout_error)
        raise requests.Timeout(timeout_error)
    else:
        data = response.content
        return data


def write_to_file(filepath, data):
    format_file = 'w'
    encoding = 'utf-8'
    if isinstance(data, bytes):
        format_file = 'wb'
        encoding = None
    with open(filepath, format_file, encoding=encoding) as page:
        page.write(data)
    logger.debug(f'The file {filepath} is downloaded')


def read(file_path):
    with open(file_path, 'rb') as f:
        result = f.read()
    return result
