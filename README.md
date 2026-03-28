<p align="center">
  <img src="https://raw.githubusercontent.com/EconViz/econ-viz-docs/main/docs/assets/banner.svg" alt="Econ-Viz" width="480">
</p>

# econ-viz-docs

[![Built with MkDocs](https://img.shields.io/badge/built%20with-MkDocs-4051b5?style=flat-square)](https://www.mkdocs.org)
[![Material for MkDocs](https://img.shields.io/badge/theme-Material-4051b5?style=flat-square)](https://squidfunk.github.io/mkdocs-material)
[![Site](https://img.shields.io/badge/site-econ--viz.org-4051b5?style=flat-square)](https://econ-viz.org)

Documentation source for [econ-viz](https://github.com/EconViz/econ-viz), a Python toolkit for producing publication-quality microeconomics diagrams.

## Prerequisites

- Python 3.11+
- [Poetry](https://python-poetry.org)

## Setup

```bash
poetry install
```

## Development

```bash
make serve
```

Opens a live-reloading server at `http://127.0.0.1:8000`.

## Build

```bash
make build
```

Outputs the static site to `site/`.
