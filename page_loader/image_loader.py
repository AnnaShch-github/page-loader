import os

import requests
from bs4 import BeautifulSoup

from page_loader.modify_name import modify_page_name, modify_file_name


def image_loader(page_path, link):
    """
    Function loading images and modifying the page.
    :param link: link to the website
    :param output: the name of existing directory,
    current working directory by default
    :return: path to new file
    """
    with open(page_path, 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
    all_image = soup.find_all('img')
    directory_name = os.getcwd()
    page_name = modify_page_name(link)
    directory = f'{directory_name}/{page_name}_files'
    os.mkdir(directory)
    for image in all_image:
        image_link = image.get('src')
        if image_link is not None and not image_link.startswith('http') and (
                image_link.endswith('jpg') or image_link.endswith('png')):
            image_bytes = requests.get(f'{link}{image_link}').content
            modified_file_name = modify_file_name(image_link)
            file_name = f'{directory}/{modified_file_name}'
            with open(file_name, 'wb') as file:
                file.write(image_bytes)
            image['src'] = file_name
    soup.prettify()
    content = str(soup)
    with open(page_path, 'w') as f:
        f.write(content)
