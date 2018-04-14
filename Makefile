
test:
	@pytest

dev: deps
	@ptw -- --testmon

deps:
	@pip3 install -r requirements.txt

lint:
	@mypy --ignore-missing-imports --allow-untyped-decorators --strict **/*.py
	@pylint **/*.py
	@pycodestyle **/*.py
	@pydocstyle
clean:
	@rm -r */__pycache__
	@rm -r .tmontmp
	@rm -r .mypy_cache

fmt:
	autopep8 -ai **/*.py
