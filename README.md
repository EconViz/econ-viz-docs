<p align="center">
  <img src="https://raw.githubusercontent.com/EconViz/econ-viz-docs/main/docs/assets/banner.svg" alt="Econ-Viz" width="480">
</p>

<p align="center">
  <a href="https://www.mkdocs.org"><img alt="Built with MkDocs" src="https://img.shields.io/badge/built%20with-MkDocs-181818?style=flat-square&color=181818&labelColor=f3f3f3"></a>
  <a href="https://squidfunk.github.io/mkdocs-material"><img alt="Theme" src="https://img.shields.io/badge/theme-Material-181818?style=flat-square&color=181818&labelColor=f3f3f3"></a>
  <a href="https://econ-viz.org"><img alt="Site" src="https://img.shields.io/badge/site-econ--viz.org-181818?style=flat-square&color=181818&labelColor=f3f3f3"></a>
</p>

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
