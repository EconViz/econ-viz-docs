---
seo_title: "Installation"
---

# Installation

<span id="sec-install"></span>

## Requirements

`macro-viz` requires Python 3.10 or later. Its runtime dependencies are `mosaickit` (1.0.0rc10 or later, below 2), which draws the figures through `matplotlib`, and `bezierkit` (1.1.1 or later, below 2), which supplies the curve geometry of rotation markers.

## Installing the package

`macro-viz` is not on PyPI yet. Install the development version from GitHub:

```bash
uv add "macro-viz @ git+https://github.com/EconViz/macro-viz"
```

With `pip`, use `python -m pip install "macro-viz @ git+https://github.com/EconViz/macro-viz"`. `mosaickit` 1.0.0rc10 is a pre-release, so add `--prerelease allow` to `uv` (or `--pre` to `pip`) until 1.0 final is published.

<span id="sec-extras"></span>

## Optional dependencies

`macro-viz[animation]` adds `kinetickit` with its raster extra, which animates a figure over a parameter ([Animation](guides/animation.md#sec-animation)). Static figures never import it.

```bash
uv add "macro-viz[animation] @ git+https://github.com/EconViz/macro-viz"
```

## Fonts

The figures of these pages use TeX Gyre Pagella for text and math, and Noto Serif TC or SC for Chinese. Font files are named in the `[font]` and `[fonts]` tables of `econ-viz.toml` ([Settings](guides/settings.md#sec-settings)); without them a figure falls back to the default serif face. The examples find the TeX Gyre files in a TeX distribution or in the folders listed in the environment variable `MACRO_VIZ_FONT_DIR`.

## Development setup

```bash
git clone https://github.com/EconViz/macro-viz.git
cd macro-viz
uv sync --locked
uv run pytest
```
