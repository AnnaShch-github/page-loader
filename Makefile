install:
	poetry install

build:
	poetry build

publish:
	poetry run --dry-run

package-install:
	python3 -m pip install dist/*.whl 

lint:
	poetry run flake8 page_loader && poetry run flake8 tests

uninstall:
	pip uninstall hexlet-code

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=page-loader --cov-report xml