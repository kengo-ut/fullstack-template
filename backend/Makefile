.PHONY: help development setup fmt lint test check dev
.DEFAULT_GOAL := help

help:
	@echo "Usage:"
	@echo "  make setup         Set up pre-commit hooks"
	@echo "  make fmt           Format .py and .ipynb files"
	@echo "  make lint          Run lint checks (ruff, mypy) on .py and .ipynb files"
	@echo "  make test          Run tests with pytest"
	@echo "  make check         Run pre-commit on all files (CI check)"
	@echo "  make dev           Run the development server with uvicorn"

setup:
	uv run pre-commit install

fmt:
	uv run ruff format .

lint:
	uv run ruff check . --fix
	uv run mypy . --ignore-missing-imports

test:
	uv run pytest

check:
	uv run pre-commit run --all-files --show-diff-on-failure

dev:
	uv run uvicorn api.main:app --reload
