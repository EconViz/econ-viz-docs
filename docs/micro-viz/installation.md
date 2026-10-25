---
seo_title: "Installation"
---

# Installation

<span id="sec-install"></span>

## Requirements

`micro-viz` requires Python 3.10 or later. Its only runtime dependency is `mosaickit`
(1.0.0rc9 or later, below 2), which draws the figures through `matplotlib`.

## Installing the package

`micro-viz` is not on PyPI yet. Install the development version from GitHub:

```bash
uv add "micro-viz @ git+https://github.com/EconViz/micro-viz"
```

With `pip`, use `python -m pip install "micro-viz @ git+https://github.com/EconViz/micro-viz"`.
`mosaickit` 1.0.0rc9 is a pre-release, so add `--prerelease allow` to `uv` (or `--pre` to `pip`)
until 1.0 final is published.

<span id="sec-extras"></span>

## Optional dependencies

`micro-viz[animation]` adds `kinetickit`, which animates a figure over a parameter
([Animation](guides/animation.md#sec-animation)). Static figures never import it.

```bash
uv add "micro-viz[animation] @ git+https://github.com/EconViz/micro-viz"
```

## Development setup

```bash
git clone https://github.com/EconViz/micro-viz.git
cd micro-viz
uv sync --locked
uv run pytest
```

## Running the examples

The scripts in `examples/scripts/` write SVG files into `examples/output/`. They use the
black-and-white `manual` look, which needs the TeX Gyre Pagella fonts; pass the directory of the
font files with `--fonts-dir` if they are not found automatically.

```bash
uv run python examples/scripts/production.py
uv run python examples/scripts/production.py --config examples/econ-viz.zh-TW.toml \
    --fonts-dir path/to/NotoSerifTC
```
