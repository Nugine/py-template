# https://github.com/casey/just
# https://docs.astral.sh/uv/

dev:
    uv sync
    just fmt
    just lint
    just test

fmt:
    uvx ruff format

lint:
    uvx ruff check
    uvx pyright

test *ARGS:
    uv run pytest {{ARGS}}

ci:
    uv sync --locked
    uvx ruff format --check
    just lint
    just test
