---
seo_title: "Installation"
---

# Installation

<span id="sec-install"></span>

## Requirements

`bezierkit` requires Python 3.10 or later and
`NumPy`. Two optional extras add the rest:

<!-- api: agora.bezierkit.installation_1 -->

## Installing the package

```bash
uv add bezierkit                 # the library
uv add "bezierkit[cli]"          # with the command-line interface
uv add "bezierkit[matplotlib]"   # with the Matplotlib adapter
uv add "bezierkit==1.0.0"        # the version this manual describes
```

With `pip`, use `python -m pip install bezierkit` and the same extras.
Version 1.0.0 is the first stable release: the names exported from
`bezierkit` and its documented subpackages follow semantic versioning, and
the JSON path schema stays at version 1.

## Development setup

```bash
git clone https://github.com/EconViz/bezierkit.git
cd bezierkit
uv sync --all-extras --dev
uv run pytest
uv run ruff check src tests benchmarks
uv run lint-imports
```

The continuous-integration workflow runs the same commands on Python 3.10,
3.11, 3.12 and 3.13. `lint-imports` checks the package layering: the
mathematical core imports no renderer, and only the adapters import
Matplotlib.
