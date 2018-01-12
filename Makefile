
test:
	@pytest

dev: deps
	@ptw -- --testmon

deps:
	@pip3 install -r requirements.txt

lint:
	@mypy --strict **/*.py
	@prospector -s veryhigh 

clean:
	@rm -r */__pycache__
	@rm -r .tmontmp
	@rm -r .mypy_cache
