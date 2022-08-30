import os
from urllib.parse import urljoin

from bs4 import BeautifulSoup
from progress.bar import Bar

from page_loader.links_for_downloading import get_links_for_download
from page_loader.logger import logger
from page_loader.services import write_to_file, get_content, get_file_name


def download(url, output='os.getcwd'):
    """
    Function loading a page and files from the link
    :param url: link to the website
    :param output: the name of the existing directory,
    current working directory by default
    :return: path to new file
    """
    data = get_content(url)
    page_name = get_file_name(url)
    if output == 'os.getcwd':
        if os.path.exists(os.path.abspath(output)):
            directory = 'os.getcwd'
        else:
            directory = os.getcwd()
    else:
        directory = output
    folder_name, extension = os.path.splitext(page_name)
    folder_for_files = f'{directory}/{folder_name}_files'
    if not os.path.isdir(folder_for_files):
        os.mkdir(folder_for_files)
        logger.info(f'The directory for files from {url} is created')
    else:
        logger.info(f'The directory for files from {url} exists')
    page_path = os.path.join(directory, page_name)
    soup = BeautifulSoup(data, 'html.parser')
    links = get_links_for_download(soup, url)
    bar = Bar('Processing', max=len(links), suffix='%(percent)d%%\n\n')
    for file_link, tag, atr in links:
        link_for_file = urljoin(url, file_link)
        files_bytes = get_content(link_for_file)
        if files_bytes is None:
            logger.debug('There is no data to write')
        else:
            file_name = get_file_name(link_for_file)
            file_path = os.path.join(folder_for_files, file_name)
            write_to_file(file_path, files_bytes)
            changed_data = '/'.join(file_path.split('/')[-2:])
            tag[atr] = changed_data
        bar.next()
    soup_data = soup.prettify()
    write_to_file(page_path, soup_data)
    logger.info(f'The page {url} is saved')
    return page_path
