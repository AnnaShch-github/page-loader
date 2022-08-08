import requests
import os

from bs4 import BeautifulSoup

from page_loader.links_for_downloading import links_for_dowloads
from page_loader.modify_name import modify_page_name, modify_file_name
from page_loader.write_to_file import write_to_file


DICTIONARY= {
    'img': 'src',
    'link': 'href',
    'script': 'src'
}
link = 'https://ru.hexlet.io/courses'
def loader(url, output='os.getcwd'):
    """
    Function loading a page from the link
    :param url: link to the website
    :param output: the name of the existing directory,
    current working directory by default
    :return: path to new file
    """
    response = requests.get(url)
    data = response.content
    page_name = modify_page_name(url)
    if output == 'os.getcwd':
        directory = os.getcwd()
    else:
        directory = output
    folder_for_files = f'{directory}/{page_name}_files'
    os.mkdir(folder_for_files)
    filepath = os.path.join(directory, page_name + '.html')
    soup = BeautifulSoup(data, 'html.parser')
    links = links_for_dowloads(soup, url)
    for file_link, object, atr in links:
        #print(f'before {object[atr]}')
        image_bytes = requests.get(f'{url}{file_link}').content
        modified_file_name = modify_file_name(file_link)
        file_name = f'{folder_for_files}/{modified_file_name}'
        write_to_file(file_name, image_bytes)
        object[atr] = file_name
        #print(f'after {object[atr]}')
    soup.prettify()
    content = str(soup)
    write_to_file(filepath, content)
    return filepath
