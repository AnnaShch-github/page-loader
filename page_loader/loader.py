import requests
import os

from page_loader.image_loader import image_loader
from page_loader.modify_name import modify_page_name


def loader(link, output='os.getcwd'):
    """
    Function loading a page from the link
    :param link: link to the website
    :param output: the name of the existing directory,
    current working directory by default
    :return: path to new file
    """
    response = requests.get(link)
    data = response.text
    file_name = modify_page_name(link)
    if output == 'os.getcwd':
        directory = os.getcwd()
    else:
        directory = output
    filepath = os.path.join(directory, file_name + '.html')
    with open(filepath, 'w') as page:
        page.write(data)
    image_loader(filepath, link)
    return filepath
