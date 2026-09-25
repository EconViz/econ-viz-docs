.PHONY: install serve build clean

install:
	poetry install

serve:
	poetry run mkdocs serve --livereload

build:
	poetry run mkdocs build

clean:
	rm -rf site/
