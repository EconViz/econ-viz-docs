# Installation

## Requirements

- Python 3.12 or later

![Cobb-Douglas equilibrium example](assets/models/cobb_douglas.png)

## Install from PyPI

```bash
pip install econ-viz
```

## Install for development

```bash
git clone https://github.com/EconViz/econ-viz.git
cd econ-viz
poetry install --with dev
```

## Verify

```bash
python -c "import importlib.metadata as m; print(m.version('econ-viz'))"
econ-viz help
```
