format:
	ruff format .

lint:
	ruff check . --fix

test:
	uvx --with-requirements pyproject.toml pytest tests

run:
	uv run src/main.py