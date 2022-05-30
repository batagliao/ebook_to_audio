all: setup

setup:
	poetry install

run:
	poetry run python src/app.py


.PHONY: all setup run