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
	@poetry run python3 -m pytype -j auto algorithms/
	@poetry run python3 -m pylint -j 0 algorithms/ tests/
	@poetry run python3 -m pycodestyle algorithms/ tests/
	@poetry run python3 -m pydocstyle algorithms/ tests/
	@poetry run python3 -m flake8 algorithms/ tests/
	@poetry run python3 -m vulture --exclude docs/*.py .
clean:
	@rm -r */__pycache__
	@rm -r .tmontmp
	@rm -r .mypy_cache

