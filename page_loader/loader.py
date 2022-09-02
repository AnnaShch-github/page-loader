import os
from urllib.parse import urljoin

from bs4 import BeautifulSoup
from progress.bar import Bar

from page_loader.links_for_downloading import get_sources_for_download
from page_loader.logger import logger, logger_error
from page_loader.names_formatter import get_file_name, get_page_name
from page_loader.content_loader import write_to_file, get_content


def download(url, output):
    """
    Function loading a page and files from the link
    :param url: link to the website
    :param output: the name of the existing directory,
    current working directory by default
    :return: path to new file
    """
    if not os.path.exists(output):
        logger_error.error(f'Sorry, the directory {output} does not exist.')
        raise IOError(f'Sorry, the directory {output} does not exist.')
    data = get_content(url)
    page_name, folder_name = get_page_name(url)
    folder_for_files = os.path.join(output, folder_name)
    if not os.path.isdir(folder_for_files):
        os.mkdir(folder_for_files)
        logger.info(f'The directory for files from {url} is created')
    else:
        logger.info(f'The directory for files from {url} exists')
    page_path = os.path.join(output, page_name)
    soup = BeautifulSoup(data, 'html.parser')
    list_of_sources = get_sources_for_download(soup, url)
    bar = Bar('Processing', max=len(list_of_sources),
              suffix='%(percent)d%%\n\n')
    for file_link, tag, atr in list_of_sources:
        link_for_file = urljoin(url, file_link)
        files_bytes = get_content(link_for_file)
        if files_bytes is None:
            logger.debug('There is no data to write')
        else:
            file_name = get_file_name(link_for_file)
            file_path = os.path.join(folder_for_files, file_name)
            write_to_file(file_path, files_bytes)
            changed_atr = os.path.relpath(file_path, output)
            tag[atr] = changed_atr
        bar.next()
    soup_data = soup.prettify()
    write_to_file(page_path, soup_data)
    logger.info(f'The page {url} is saved')
    return page_path
