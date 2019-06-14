.PHONY: test dev deps clean lint fmt

test: lint
	@pytest

dev: deps
	@ptw -- --testmon

deps:
	@pip3 install -r requirements.txt

lint:
	@mypy --ignore-missing-imports --allow-untyped-decorators --strict **/*.py
	@python3 -m pylint **/*.py
	@python3 -m pycodestyle **/*.py
	@python3 -m pydocstyle **/*.py
clean:
	@rm -r */__pycache__
	@rm -r .tmontmp
	@rm -r .mypy_cache

fmt:
#	@python3 -m black --line-length 79 **/*.py
	@find . -name *.py | xargs python3 -m black --line-length 79
