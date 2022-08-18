import os
import tempfile

import pytest
import requests_mock

from page_loader import loader
from page_loader.reader import read

URL = 'https://ru.hexlet.io/courses'
TEST_FOLDER = os.path.dirname(__file__)
PATH_ORIGINAL = os.path.join(TEST_FOLDER, 'fixtures')
URL_IMAGE = 'https://ru.hexlet.io/courses'
CHANGED = 'tests/fixtures/changed.html'
HTML_FILE_NAME = os.path.join(PATH_ORIGINAL, 'page-loader-hexlet-repl-co.html')
ORIGINAL = 'tests/fixtures/original.html'
JS_FILE = os.path.join(TEST_FOLDER,'fixtures', 'page-loader-hexlet-repl-co_files', 'page-loader-hexlet-repl-co-script.js')
URL_JS = 'https://ru.hexlet.io/coursespage-loader-hexlet-repl-co_files/page-loader-hexlet-repl-co-script.js'
DOWNLOADS_DIR = os.path.join(TEST_FOLDER, 'fixtures')
CHANGED_HTML_FILE_NAME = 'page-loader-hexlet-repl-co.html'
CREATED_HTML_FILE = os.path.join(DOWNLOADS_DIR, CHANGED_HTML_FILE_NAME)
CREATED_DIR_NAME = 'page-loader-hexlet-repl-co_files'
JS_NAME = 'page-loader-hexlet-repl-co-script.js'
CREATED_JS = os.path.join(CREATED_DIR_NAME, JS_NAME)
EXPECTED_JS = os.path.join(DOWNLOADS_DIR, CREATED_JS)


@pytest.mark.parametrize('original_file, changed', [(CHANGED_HTML_FILE_NAME, CREATED_HTML_FILE),  (CREATED_JS, EXPECTED_JS)])
def test_download(original_file, changed, requests_mock):
    requests_mock.get(URL, text=read(HTML_FILE_NAME))
    requests_mock.get(URL_JS, text=read(JS_FILE))
    with tempfile.TemporaryDirectory() as temp:
        result_path = loader(URL, temp)
        assert read(result_path) == read(changed)
        assert os.path.exists(result_path)
