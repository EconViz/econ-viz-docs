---
seo_title: "Installation"
---

# Installation

<span id="sec-install"></span>

## Requirements

`mosaickit` requires Python 3.10 or later, `NumPy`
1.24 or later, `Matplotlib` 3.6 or later (below 4) and `glyphkit`
1.0.0b3 or later (below 2), which sets the text. On Python 3.10, it also
installs `tomli` to read TOML.

## Installing the package

```bash
uv add mosaickit                 # the library
uv add "mosaickit==1.0.0rc6"     # the version this manual describes
```

Version 1.0.0rc6 is a pre-release. Until 1.0 final is published, plain
`uv add mosaickit` and `pip install mosaickit` install 0.9.2; opt in to
pre-releases with `uv add --prerelease allow mosaickit` or
`pip install --pre mosaickit`.

With `pip`, use `python -m pip install mosaickit`. Importing
`mosaickit` does not import Matplotlib: the built-in renderer is loaded by
name the first time a canvas renders ([Rendering](guides/rendering.md#sec-rendering)).

## Development setup

```bash
git clone https://github.com/EconViz/mosaickit.git
cd mosaickit
uv sync --locked
uv run pre-commit install
uv run pytest
uv run ruff check .
uv run ruff format --check .
uv run mypy
uv run lint-imports
uv build
```

The lockfile pins every development dependency. The continuous-integration
workflow runs the same commands on Python 3.10, 3.11, 3.12 and 3.13. It then
installs the built wheel into a clean environment, checks that `bezierkit`
is absent, and runs the test suite against the wheel. Import contracts enforce
the module boundaries: scenes, styles, themes and parameters never import the
rendering or canvas modules, and the core never imports a domain package.
