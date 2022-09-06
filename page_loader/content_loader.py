import requests

from page_loader.logger import logger, logger_error


def get_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except (requests.HTTPError,
            requests.ConnectionError,
            requests.URLRequired,
            requests.TooManyRedirects,
            requests.Timeout) as error:
        logger_error.error(error)
        raise error
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
