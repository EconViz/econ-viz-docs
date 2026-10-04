---
seo_title: "Install mosaickit"
description: "Install mosaickit with pip or uv, enable GIF and MP4 output, and set up a development environment."
---

# Installation

## Requirements

- [Python](https://www.python.org/downloads/) 3.10 or later (the project supports 3.10 to 3.13)

mosaickit installs `numpy` and `matplotlib` as dependencies, plus `tomli` on Python 3.10.

## Install

=== ":simple-pypi: pip"

    ```bash
    pip install mosaickit
    ```

=== ":simple-uv: uv"

    ```bash
    uv add mosaickit
    ```

This page describes mosaickit 0.5.1.

## Animation output

`Animation` writes GIF files with Pillow, which comes along with Matplotlib, so GIF output works after a plain
install. MP4 output requires `ffmpeg` on your `PATH`.

## Verify the installation

```bash
python -c "import mosaickit; print(mosaickit.__version__)"
```

This prints `0.5.1` for the version described here.

## Development setup

```bash
git clone https://github.com/EconViz/mosaickit.git
cd mosaickit
uv sync --locked
uv run pytest
```
