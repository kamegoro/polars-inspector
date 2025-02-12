format:
	uvx --with-requirements pyproject.toml ruff format .

lint:
	uvx --with-requirements pyproject.toml ruff check . --fix

test:
	uvx --with-requirements pyproject.toml pytest tests

run:
	uv run src/main.py