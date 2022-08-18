import os
import tempfile

import requests_mock

from page_loader import loader
from page_loader.reader import read

url = 'https://ru.hexlet.io/courses'


#@pytest.mark.parametrize(new.html, expected.html, [])
def test_download():
    with requests_mock.Mocker() as mock:
        mock.get(url, text=read('tests/fixtures/expected.html'))

        with tempfile.TemporaryDirectory() as temp:
            expected = read('tests/fixtures/expected.html')
            result_path = loader(url, temp)
            print(result_path)
            assert read(result_path) == expected
            assert os.path.exists(result_path)
