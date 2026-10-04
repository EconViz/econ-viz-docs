---
seo_title: "Install bezierkit"
description: "Install the bezierkit 0.5.0rc1 pre-release with pip or uv, add the optional CLI and Matplotlib extras, and set up a development environment."
---

# Installation

## Requirements

- [Python](https://www.python.org/downloads/) 3.10 or later

bezierkit installs `numpy` as its only required dependency.

## Install

bezierkit 0.5.0rc1 is a pre-release, and pip and uv skip pre-releases by default. Opt in with `--pre`, or pin the
exact version.

=== ":simple-pypi: pip"

    ```bash
    pip install --pre bezierkit
    # or pin the exact version:
    pip install bezierkit==0.5.0rc1
    ```

=== ":simple-uv: uv"

    ```bash
    uv add --prerelease allow bezierkit
    # or pin the exact version:
    uv add bezierkit==0.5.0rc1
    ```

## Optional extras

| Extra | Adds | Install |
|---|---|---|
| `cli` | The `bezierkit` command (typer and rich) | `pip install --pre "bezierkit[cli]"` |
| `matplotlib` | The Matplotlib path adapter | `pip install --pre "bezierkit[matplotlib]"` |

With uv, use `uv add --prerelease allow "bezierkit[cli]"` in the same way.

## Verify the installation

```bash
python -c "import bezierkit; print(bezierkit.__version__)"
```

This prints `0.5.0rc1`. With the `cli` extra installed, `bezierkit --help` lists the commands.

## Development setup

```bash
git clone https://github.com/EconViz/bezierkit.git
cd bezierkit
uv sync --all-extras --dev
uv run pytest
```
