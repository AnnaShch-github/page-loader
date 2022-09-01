import os
import re
from urllib.parse import urlparse


def get_file_name(url):
    first_step = urlparse(url)
    second_step = ''.join([first_step.netloc, first_step.path])
    file_name, extension = os.path.splitext(second_step)
    re_file_name = re.sub(r'[^0-9a-zA-Z]', r'-', file_name)
    if not extension:
        extension = '.html'
    result = ''.join([re_file_name, extension])
    return result


def get_page_name(url):
    first_step = urlparse(url)
    second_step = ''.join([first_step.netloc, first_step.path])
    final_step = re.sub(r'[^0-9a-zA-Z]', r'-', second_step)
    folder_name = ''.join([final_step, '_files'])
    file_name = ''.join([final_step, '.html'])
    return file_name, folder_name
