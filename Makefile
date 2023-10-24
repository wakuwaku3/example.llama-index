.PHONY: install
install:
	poetry install

.PHONY: run-save
.SILENT:
run-save:
	poetry run python ./sgpt_review_with_preconditionrc/save.py

.PHONY: run-review
.SILENT:
run-review:
	poetry run python ./gpt_review_with_precondition/review.py

.PHONY: build
build:
	poetry build

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
	poetry run pylint ./gpt_review_with_precondition/**

.PHONY: test
test:
	poetry run pytest

.PHONY: publish
publish:
	poetry publish
