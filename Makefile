.PHONY: test dev deps clean lint fmt

test: lint
	@poetry run python3 -m pytest .

dev: deps
	@ptw -- --testmon

deps:
	@poetry install

fmt:
	@poetry run python3 -m black .

lint:
	@poetry run python3 -m mypy --ignore-missing-imports --allow-untyped-decorators --strict **/*.py
	@poetry run python3 -m pylint **/*.py
	@poetry run python3 -m pycodestyle **/*.py
	@poetry run python3 -m pydocstyle **/*.py
	@poetry run python3 -m flake8 algorithms/
	@poetry run python3 -m vulture .
clean:
	@rm -r */__pycache__
	@rm -r .tmontmp
	@rm -r .mypy_cache

