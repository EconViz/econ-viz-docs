.PHONY: install serve watch build clean

install:
	uv sync --frozen

serve:
	uv run --frozen mkdocs serve --livereload

# Dev server that also watches the Python hooks, so editing them rebuilds the site.
watch:
	uv run --frozen mkdocs serve --livereload --watch hooks --dev-addr 127.0.0.1:8000

build:
	uv run --frozen mkdocs build

clean:
	rm -rf site/
