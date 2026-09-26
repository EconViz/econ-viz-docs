---
seo_title: "Installation"
description: "Install the econ-viz Python package with uv, including optional extras for GIF animation and Jupyter notebook widgets."
---

# Installation

## Requirements

Install these tools before creating a project:

- [Python](https://www.python.org/downloads/) 3.10 or later
- [uv](https://docs.astral.sh/uv/)

## Install uv

=== ":fontawesome-brands-apple: macOS"

    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

=== ":fontawesome-brands-linux: Linux"

    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

=== ":fontawesome-brands-windows: Windows"

    ```powershell
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

Alternatively, use a package manager:

=== ":simple-homebrew: Homebrew"

    ```bash
    brew install uv
    ```

=== ":simple-macports: MacPorts"

    ```bash
    sudo port install uv
    ```

=== ":fontawesome-brands-windows: WinGet"

    ```powershell
    winget install --id=astral-sh.uv -e
    ```

=== ":material-bucket-outline: Scoop"

    ```powershell
    scoop install main/uv
    ```

=== ":simple-pipx: pipx"

    ```bash
    pipx install uv
    ```

=== ":simple-rust: Cargo"

    ```bash
    cargo install --locked uv
    ```

## Install econ-viz

Create a project and add `econ-viz` as a dependency:

```bash
uv init my-diagrams
cd my-diagrams
uv add econ-viz
```

Run scripts inside the project environment with `uv run`:

```bash
uv run python main.py
```

## Optional dependencies

Extras enable features that require additional packages:

```bash
uv add "econ-viz[animation]"    # GIF export (Pillow)
uv add "econ-viz[interactive]"  # notebook widgets
uv add "econ-viz[all]"          # all extras
```

## Global CLI installation

To use only the command-line interface, install it as a standalone tool so `econ-viz` is available on your `PATH`:

```bash
uv tool install econ-viz
```

## Development setup

```bash
git clone https://github.com/EconViz/econ-viz.git
cd econ-viz
uv sync --all-extras
```

`uv sync` installs the `dev` dependency group by default; `--all-extras` also installs every optional dependency. Run the test suite with:

```bash
uv run pytest
```

## Verifying the installation

```bash
uv run econ-viz --version   # econ-viz 1.10.0
uv run econ-viz help
```
