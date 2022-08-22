import os
from urllib.parse import urljoin

from bs4 import BeautifulSoup
from progress.bar import Bar

from page_loader.get_content import get_page, get_files
from page_loader.links_for_downloading import links_for_dowloads
from page_loader.logger import logger
from page_loader.modify_name import modify_page_name, modify_file_name, \
    change_name_for_file
from page_loader.write_to_file import write_to_file


def download(url, output='os.getcwd'):
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
        logger.info(f'This is url: {url}')
        #link_for_file = f'{url}{file_link}'
        link_for_file = urljoin(url, file_link)
        logger.info(f'The link should be different: {link_for_file}')
        image_bytes = get_files(link_for_file)
        if image_bytes is None:
            logger.debug('There is no data to main')
        else:
            modified_file_name = modify_file_name(link_for_file)
            file_name = os.path.join(folder_for_files, modified_file_name)
            write_to_file(file_name, image_bytes)
            name_for_file = change_name_for_file(file_name)
            tag[atr] = name_for_file
        bar.next()
    soup.prettify()
    content = str(soup)
    write_to_file(filepath, content)
    logger.debug(f'The page {url} is saved')
    return filepath
