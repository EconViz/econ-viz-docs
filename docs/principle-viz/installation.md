---
seo_title: "Install principle-viz"
description: "Install principle-viz with pip or uv, check the installation, and set up a development environment."
---

# Installation

## Requirements

- [Python](https://www.python.org/downloads/) 3.10 or later

`principle-viz` depends on [mosaickit](../mosaickit/index.md) (`>=0.5.1,<0.6.0`), which pip and uv install
automatically.

## Install

=== ":simple-pypi: pip"

    ```bash
    pip install principle-viz
    ```

=== ":simple-uv: uv"

    ```bash
    uv add principle-viz
    ```

This page describes principle-viz 0.10.0.

## Verify the installation

```bash
python -c "import principle_viz; print('principle_viz imported')"
principle-viz --help
```

The second command lists the sub-commands, such as `equilibrium`, `tax`, `subsidy`, `trade` and `controls`.

## Development setup

```bash
git clone https://github.com/EconViz/principle-viz.git
cd principle-viz
uv sync
```

Run the checks and the test suite with:

```bash
uv run ruff check src tests examples/scripts
uv run pytest -q
```
