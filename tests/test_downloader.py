import os

import pytest
import requests


from page_loader import download
from page_loader.services import read

URL = 'https://ru.hexlet.io'
URL_CSS = 'https://ru.hexlet.io/assets/application.css'
URL_PNG = 'https://ru.hexlet.io/assets/professions/nodejs.png'
URL_HTML = 'https://ru.hexlet.io/courses'
URL_JS = 'https://ru.hexlet.io/script.js'


CREATED_JS = 'tests/fixtures/files/fixture.js'
EXPECTED_JS = 'tests/fixtures/files/fixture.js'
NEW_JS = 'ru-hexlet_files/ru-hexlet-io-script.js'
CREATED_HTML = 'tests/fixtures/files/fixture.html'
EXPECTED_HTML = 'tests/fixtures/files/fixture.html'
NEW_HTML = 'ru-hexlet_files/ru-hexlet-io-courses.html'
CREATED_PNG = 'tests/fixtures/files/fixture.png'
EXPECTED_PNG = 'tests/fixtures/files/fixture.png'
NEW_PNG = 'ru-hexlet_files/ru-hexlet-io-assets-professions-nodejs.png'
CREATED_CSS = 'tests/fixtures/files/fixture.css'
EXPECTED_CSS = 'tests/fixtures/files/fixture.css'
NEW_CSS = 'ru-hexlet_files/ru-hexlet-io-assets-application.css'
CHANGED_PAGE = 'tests/fixtures/changed.html'
CREATED_PAGE = 'tests/fixtures/original.html'
CREATED_DIR = 'ru-hexlet_files'


@pytest.mark.parametrize('new_file, changed', [(NEW_CSS, EXPECTED_CSS),
                                               (NEW_PNG, EXPECTED_PNG),
                                               (NEW_HTML, EXPECTED_HTML),
                                               (NEW_JS, EXPECTED_JS)])
def test_download(new_file, changed, tmpdir, requests_mock):
    requests_mock.get(URL, content=read(CREATED_PAGE))
    requests_mock.get(URL_CSS, content=read(CREATED_CSS))
    requests_mock.get(URL_PNG, content=read(CREATED_PNG))
    requests_mock.get(URL_HTML, content=read(CREATED_HTML))
    requests_mock.get(URL_JS, content=read(CREATED_JS))
    result_path = download(URL, tmpdir)
    new_file = os.path.join(tmpdir, new_file)
    assert read(result_path) == read(CHANGED_PAGE)
    assert os.path.exists(result_path)
    assert len(os.listdir(os.path.join(tmpdir, CREATED_DIR))) == 4
    assert read(new_file) == read(changed)


@pytest.mark.parametrize('connection_error_excepted', [
    requests.HTTPError, requests.ConnectionError,
    requests.URLRequired, requests.TooManyRedirects, requests.Timeout,
    PermissionError, FileNotFoundError,
])
def test_download_exceptions(connection_error_excepted, tmpdir, requests_mock):
    with pytest.raises(connection_error_excepted):
        requests_mock.get(URL, exc=connection_error_excepted)
        download(URL, tmpdir)
