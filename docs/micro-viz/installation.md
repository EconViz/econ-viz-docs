---
seo_title: "Installation"
---

# Installation

<span id="sec-install"></span>

## Requirements

`micro-viz` requires Python 3.10 or later (the Python website provides installers for every operating system: [https://www.python.org/downloads/](https://www.python.org/downloads/)). Its only runtime dependency is `mosaickit` (1.0.0rc9 or later, below 2), which draws the figures through `matplotlib`.

## Installing `uv`

The commands on these pages use `uv` (`uv` is a fast Python package and project manager by Astral that also manages Python versions. Installation and full documentation: [https://docs.astral.sh/uv/](https://docs.astral.sh/uv/)). Existing projects can keep using `pip`; the package API does not depend on the tool.

### macOS and Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Windows

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Installing `micro-viz`

`micro-viz` is not on PyPI yet. Install the development version from GitHub:

```bash
uv init my-diagrams
cd my-diagrams
uv add "micro-viz @ git+https://github.com/EconViz/micro-viz"
```

With `pip`, use `python -m pip install "micro-viz @ git+https://github.com/EconViz/micro-viz"`. `mosaickit` 1.0.0rc9 is a pre-release, so add `--prerelease allow` to `uv` (or `--pre` to `pip`) until 1.0 final is published.

## Optional dependencies

<span id="sec-extras"></span>

`micro-viz[animation]` adds `kinetickit`, which animates a figure over a parameter ([Animation](guides/animation.md#sec-animation)). Static figures never import it.

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

<span id="sec-run-examples"></span>

The scripts in `examples/scripts/<topic>/` write SVG files into `examples/output/<topic>/`. They use the black-and-white `manual` look, which needs the TeX Gyre Pagella fonts; pass the directory of the font files with `--fonts-dir` if they are not found automatically.

```bash
uv run python examples/scripts/production/production.py
uv run python examples/scripts/production/production.py \
    --config examples/econ-viz.zh-TW.toml \
    --fonts-dir path/to/NotoSerifTC
```

The figures of these pages are drawn by these scripts; the archive linked in [Introduction](guides/introduction.md#sec-intro) holds them together with the three settings files.
