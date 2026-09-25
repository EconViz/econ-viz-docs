---
seo_title: "Install Econ-Viz"
description: "Install the econ-viz Python package with uv, including optional extras for GIF animation and Jupyter notebook widgets."
---

# Installation

## Requirements

- Python 3.10 or later
- [uv](https://docs.astral.sh/uv/)

## Install uv

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

On Windows or with other package managers, see the [uv installation guide](https://docs.astral.sh/uv/getting-started/installation/).

## Add econ-viz to a project

```bash
uv init my-diagrams
cd my-diagrams
uv add econ-viz
```

Run your scripts inside the project environment with `uv run`:

```bash
uv run python main.py
```

## Optional extras

Install only what you need:

```bash
uv add "econ-viz[animation]"    # Pillow for GIF export
uv add "econ-viz[interactive]"  # ipywidgets + IPython for notebooks
uv add "econ-viz[all]"          # both extras
```

## Install the CLI as a tool

If you only need the command-line interface, install it globally so `econ-viz` is available in any terminal:

```bash
uv tool install econ-viz
```

## Install for development

```bash
git clone https://github.com/EconViz/econ-viz.git
cd econ-viz
uv sync --all-extras
```

`uv sync` installs the development dependencies by default, and `--all-extras` adds the notebook and animation tooling. Run the test suite with:

```bash
uv run pytest
```

## Verify

```bash
uv tree --package econ-viz --depth 0   # econ-viz v1.6.0
uv run econ-viz help
```
