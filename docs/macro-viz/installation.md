---
seo_title: "Installation"
---

# Installation

<span id="sec-install"></span>

## Requirements

`macro-viz` requires Python 3.10 or later. Its only runtime dependency is `mosaickit`
(1.0.0rc9 or later, below 2), which draws the figures through `matplotlib`.

## Installing the package

`macro-viz` is not on PyPI yet. Install the development version from GitHub:

```bash
uv add "macro-viz @ git+https://github.com/EconViz/macro-viz"
```

With `pip`, use `python -m pip install "macro-viz @ git+https://github.com/EconViz/macro-viz"`.
`mosaickit` 1.0.0rc9 is a pre-release, so add `--prerelease allow` to `uv` (or `--pre` to `pip`)
until 1.0 final is published.

<span id="sec-extras"></span>

## Optional dependencies

`macro-viz[animation]` adds `kinetickit`, which animates a figure over a parameter
([Animation](guides/animation.md#sec-animation)). Static figures never import it.

```bash
uv add "macro-viz[animation] @ git+https://github.com/EconViz/macro-viz"
```

## Development setup

```bash
git clone https://github.com/EconViz/macro-viz.git
cd macro-viz
uv sync --locked
uv run pytest
```
