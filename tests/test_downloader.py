import os
import tempfile

import requests_mock

from page_loader import loader
from page_loader.reader import read

url = 'https://ru.hexlet.io/courses'


def test_download():
    with requests_mock.Mocker() as mock:
        mock.get(url, text=read('tests/fixtures/page.html'))

        with tempfile.TemporaryDirectory() as temp:
            expected = read('tests/fixtures/page.html')
            result_path = loader(url, temp)
            assert read(result_path) == expected
            assert os.path.exists(result_path)
