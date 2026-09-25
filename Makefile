.PHONY: install serve build clean

install:
	uv sync --frozen

serve:
	uv run --frozen mkdocs serve --livereload

build:
	uv run --frozen mkdocs build

clean:
	rm -rf site/
