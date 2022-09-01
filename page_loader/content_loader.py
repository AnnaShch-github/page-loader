import requests

from page_loader.logger import logger, logger_error


def get_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.HTTPError as http_error:
        logger_error.error(http_error)
        raise requests.HTTPError(http_error)
    except requests.ConnectionError as connection_error:
        logger_error.error(connection_error)
        raise requests.ConnectionError(connection_error)
    except requests.URLRequired as url_error:
        logger_error.error(url_error)
        raise requests.URLRequired(url_error)
    except requests.TooManyRedirects as redirects_error:
        logger_error.error(redirects_error)
        raise requests.TooManyRedirects(redirects_error)
    except requests.Timeout as timeout_error:
        logger_error.error(timeout_error)
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
