import requests

from page_loader.logger import logger


def get_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.HTTPError:
        logger.error('An HTTP error occurred.')
        raise requests.HTTPError('An HTTP error occurred.')
    except requests.ConnectionError:
        logger.error('A Connection error occurred.')
        raise requests.ConnectionError('A Connection error occurred.')
    except requests.URLRequired:
        logger.error('A valid URL is required to make a request')
        raise requests.URLRequired('A valid URL is required to make a request')
    except requests.TooManyRedirects:
        logger.error('Too many redirects.')
        raise requests.TooManyRedirects('Too many redirects.')
    except requests.Timeout:
        logger.error('The request timed out.')
        raise requests.Timeout('The request timed out.')
    else:
        data = response.text
        return data


def get_files(link_for_file):
    try:
        response = requests.get(link_for_file)
        response.raise_for_status()
    except requests.HTTPError:
        logger.warning('An HTTP error occurred.')
    except requests.ConnectionError:
        logger.warning('A Connection error occurred.')
    except requests.URLRequired:
        logger.warning('A valid URL is required to make a request')
    except requests.TooManyRedirects:
        logger.warning('Too many redirects.')
    except requests.Timeout:
        logger.warning('The request timed out.')
    else:
        data = response.content
        return data
