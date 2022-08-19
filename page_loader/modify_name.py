import os
import re


def modify_page_name(link):
    """
    Modify the link to get the name of the downloaded page
    :param link: link to the website
    :return: name for the new page
    """
    first_step = '/'.join(link.split('/')[2:])
    second_step = os.path.splitext(first_step)[0]
    page_name = re.sub(r'[^0-9a-zA-Z]', r'-', second_step)
    return page_name


def modify_file_name(link):
    """
    Modify the link to get the name of the downloaded file
    :param link: link to the file
    :return: name for the new file
    """
    first_step = '/'.join(link.split('/')[2:])
    second_step = os.path.splitext(first_step)[0]
    third_step = os.path.splitext(first_step)[1]
    fourth_step = re.sub(r'[^0-9a-zA-Z]', r'-', second_step)
    file_name = f'{fourth_step}{third_step}'
    return file_name


def change_name_for_file(file_name):
    first_step = '/'.join(file_name.split('/')[-2:])
    second_step = os.path.splitext(first_step)[0]
    third_step = os.path.splitext(first_step)[1]
    fourth_step = re.sub(r'[^0-9a-zA-Z]/', r'-', second_step)
    name_for_file = f'{fourth_step}{third_step}'
    return name_for_file
