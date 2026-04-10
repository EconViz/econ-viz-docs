# Installation

## Requirements

- Python 3.12 or later

![Cobb-Douglas equilibrium example](assets/models/cobb_douglas.png)

## Install from PyPI

```bash
pip install econ-viz
```

## Optional extras

Install only what you need:

```bash
pip install "econ-viz[animation]"    # Pillow for GIF export
pip install "econ-viz[interactive]"  # ipywidgets + IPython for notebooks
pip install "econ-viz[all]"          # both extras
```

## Install for development

```bash
git clone https://github.com/EconViz/econ-viz.git
cd econ-viz
poetry install --with dev
```

If you want the optional notebook and animation tooling in a local editable environment:

```bash
poetry run pip install -e ".[all]"
```

## Verify

```bash
python -c "import importlib.metadata as m; print(m.version('econ-viz'))"
econ-viz help
```
