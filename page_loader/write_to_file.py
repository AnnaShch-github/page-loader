from page_loader.logger import logger


def write_to_file(filepath, data):
    format_file = 'w'
    encoding = 'utf-8'
    if isinstance(data, bytes):
        format_file = 'wb'
        encoding = None
    with open(filepath, format_file, encoding=encoding) as page:
        page.write(data)
    logger.debug(f'The file {filepath} is downloaded')
