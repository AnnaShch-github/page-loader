import os
import tempfile

import pytest
import requests


from page_loader import loader
from page_loader.reader import read

URL = 'https://ru.hexlet.io/courses'
URL_CSS = 'https://ru.hexlet.io/courses/assets/application.css'
URL_PNG = 'https://ru.hexlet.io/courses/assets/professions/nodejs.png'
URL_HTML = 'https://ru.hexlet.io/courses/courses'
URL_JS = 'https://ru.hexlet.io/courses/script.js'


CREATED_JS = 'tests/fixtures/files/fixture.css'
EXPECTED_JS = 'tests/fixtures/files/fixture.js'
CREATED_HTML = 'tests/fixtures/files/fixture.html'
EXPECTED_HTML = 'tests/fixtures/files/fixture.html'
CREATED_PNG = 'tests/fixtures/files/fixture.png'
EXPECTED_PNG = 'tests/fixtures/files/fixture.png'
CREATED_CSS = 'tests/fixtures/files/fixture.css'
EXPECTED_CSS = 'tests/fixtures/files/fixture.css'
CHANGED_PAGE = 'tests/fixtures/changed.html'
CREATED_PAGE = 'tests/fixtures/original.html'
CREATED_DIR = 'ru-hexlet-io-courses_files'


@pytest.mark.parametrize('new_file, changed', [(CHANGED_PAGE, CREATED_PAGE),
                                               (CREATED_CSS, EXPECTED_CSS),
                                               (CREATED_PNG, EXPECTED_PNG),
                                               (CREATED_HTML, EXPECTED_HTML),
                                               (CREATED_JS, EXPECTED_JS)])
def test_download(new_file, changed, requests_mock):
    requests_mock.get(URL, content=read(CREATED_PAGE))
    requests_mock.get(URL_CSS, content=read(CREATED_CSS))
    requests_mock.get(URL_PNG, content=read(CREATED_PNG))
    requests_mock.get(URL_HTML, content=read(CREATED_HTML))
    requests_mock.get(URL_JS, content=read(CREATED_JS))
    with tempfile.TemporaryDirectory() as temp:
        result_path = loader(URL, temp)
        assert read(result_path) == read(CHANGED_PAGE)
        assert os.path.exists(result_path)
        assert len(os.listdir(os.path.join(temp, CREATED_DIR))) == 4


@pytest.mark.parametrize('connection_error_excepted', [
    requests.HTTPError, requests.ConnectionError,
    requests.URLRequired, requests.TooManyRedirects, requests.Timeout
])
def test_download_exceptions(connection_error_excepted, requests_mock):
    with pytest.raises(connection_error_excepted):
        requests_mock.get(URL, exc=connection_error_excepted)
        with tempfile.TemporaryDirectory() as temp:
            loader(URL, temp)
