import requests
import os

from bs4 import BeautifulSoup
from progress.bar import Bar

from page_loader.get_content import get_page, get_files
from page_loader.links_for_downloading import links_for_dowloads
from page_loader.logger import logger
from page_loader.modify_name import modify_page_name, modify_file_name
from page_loader.write_to_file import write_to_file


DICTIONARY = {
    'img': 'src',
    'link': 'href',
    'script': 'src'
}


def loader(url, output='os.getcwd'):
    """
    Function loading a page from the link
    :param url: link to the website
    :param output: the name of the existing directory,
    current working directory by default
    :return: path to new file
    """
    data = get_page(url)
    page_name = modify_page_name(url)
    if output == 'os.getcwd':
        directory = os.getcwd()
    else:
        directory = output
    folder_for_files = f'{directory}/{page_name}_files'
    if not os.path.isdir(folder_for_files):
        os.mkdir(folder_for_files)
        logger.info(f'The directory for files from {url} is created')
    else:
        logger.info(f'The directory for files from {url} exists')
    filepath = os.path.join(directory, page_name + '.html')
    soup = BeautifulSoup(data, 'html.parser')
    links = links_for_dowloads(soup, url)
    bar = Bar('Processing', max=len(links), suffix='%(percent)d%%\n\n')
    for file_link, tag, atr in links:
        image_bytes = get_files(url, file_link)
        if image_bytes is None:
            logger.debug('There is no data to download')
        else:
            modified_file_name = modify_file_name(file_link)
            file_name = f'{folder_for_files}/{modified_file_name}'
            write_to_file(file_name, image_bytes)
            tag[atr] = file_name
        bar.next()
    soup.prettify()
    content = str(soup)
    write_to_file(filepath, content)
    logger.debug(f'The page {url} is saved')
    return filepath
