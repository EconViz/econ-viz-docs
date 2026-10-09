---
seo_title: "Installation"
---

# Installation

<span id="sec-install"></span>

## Requirements

`mosaickit` requires Python 3.10 or later, `NumPy`
1.24 or later and `Matplotlib` 3.6 or later (below 4). On Python 3.10,
it also installs `tomli` to read TOML. GIF output uses `Pillow`,
which Matplotlib already depends on. MP4 output needs `ffmpeg` on the
`PATH`.

## Installing the package

```bash
uv add mosaickit                 # the library
uv add "mosaickit==0.5.1"        # the version this manual describes
```

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
