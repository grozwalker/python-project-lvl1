install:
	poetry install

brain-games:
	poetry run brain-games

run:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python -m pip install dist/*.whl
