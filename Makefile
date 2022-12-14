make lint:
	poetry run flake8 brain_games
install:
	poetry install
brain-games:
	poetry run brain-games
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl
brain-even:
	poetry run brain-even
update:
	python3 -m pip install --user --force-reinstall dist/*.whl
all:
	poetry install
	poetry build
	poetry publish --dry-run
	python3 -m pip install --user dist/*.whl