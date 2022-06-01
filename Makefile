all: setup

setup:
	poetry install

run:
	poetry run python src/app.py

test:
	poetry run pytest tests


.PHONY: all setup run test