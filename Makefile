.PHONY: install
install:
	poetry install

.PHONY: run
.SILENT:
run:
	poetry run python ./src/main.py

.PHONY: build
build:
	poetry run python -m py_compile ./src/main.py

.PHONY: lint
lint:lint-isort lint-black lint-pflake8 lint-mypy lint-pylint

.PHONY: lint-isort
lint-isort:
	poetry run isort . --check-only

.PHONY: lint-black
lint-black:
	poetry run black . --check

.PHONY: lint-pflake8
lint-pflake8:
	poetry run pflake8

.PHONY: lint-mypy
lint-mypy:
	poetry run mypy

.PHONY: lint-pylint
lint-pylint:
	poetry run pylint ./src/**

.PHONY: test
test:
	poetry run pytest
