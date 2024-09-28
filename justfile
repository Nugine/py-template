# https://github.com/casey/just
# https://docs.astral.sh/uv/

dev:
    uv sync --locked
    just fmt
    just lint
    just typecheck
    just test

fmt:
    uv run ruff format

lint:
    uv run ruff check

typecheck:
    uv run mypy .
    uv run pyright

test *ARGS:
    uv run pytest --show-capture=all {{ARGS}}
