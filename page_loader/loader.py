import requests
import os
import re


def loader(link, output='os.getcwd'):
    """
    Function loading a page from the link
    :param link: link to the website
    :param output: the name of existing directory, current working directory by default
    :return: path to new file
    """ 
    response = requests.get(link)
    data = response.content
    file_name = modify_file_name(link)
    if output == 'os.getcwd':
        directory = os.getcwd()
    else:
        directory = output
    filepath = os.path.join(directory, file_name + '.html')
    with open(filepath, 'w') as page:
        page.write(data)
    return filepath


def modify_file_name(link):
    """
    Modify the link to get the name of the downloaded file
    :param link: link to the website
    :return: name for the new file
    """
    first_step = '/'.join(link.split('/')[2:])
    second_step = os.path.splitext(first_step)[0]
    final_step = re.sub(r'[^0-9a-zA-Z]', r'-', second_step)
    return final_step
