.PHONY: all test dev deps clean lint fmt pycodestyle pydocstyle pylint pytype flake8 vulture

all: lint test

test:
	@poetry run python3 -m pytest .

lint: fmt mypy pytype pylint pycodestyle pydocstyle flake8 vulture

dev: deps
	@ptw -- --testmon

deps:
	@poetry install

fmt:
	@poetry run python3 -m black .

mypy:
	@poetry run python3 -m mypy --ignore-missing-imports --allow-untyped-decorators --strict **/*.py

pytype:
	@poetry run python3 -m pytype -j auto algorithms/

pylint:
	@poetry run python3 -m pylint -j 0 **/*.py

pycodestyle:
	@poetry run python3 -m pycodestyle **/*.py
pydocstyle:
	@poetry run python3 -m pydocstyle **/*.py

flake8:
	@poetry run python3 -m flake8 algorithms/

vulture:
	@poetry run python3 -m vulture .

clean:
	@rm -r */__pycache__
	@rm -r .tmontmp
	@rm -r .mypy_cache

