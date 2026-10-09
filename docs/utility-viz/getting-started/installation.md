---
seo_title: "Installation"
description: "Install the utility-viz Python package with uv, including optional extras for GIF animation and Jupyter notebook widgets."
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

## Install utility-viz

!!! warning "utility-viz 2.0 is in beta"

    utility-viz 2.0.0b1 is a pre-release. The stable line stays `econ-viz` 1.x until 2.0 final is released.
    Pre-releases are skipped by default, so the commands below pass `--prerelease allow`.
    Coming from `econ-viz`? See [Migration guide](../migrating.md).

With uv, create a project and add it as a dependency:

```bash
uv init my-diagrams
cd my-diagrams
uv add --prerelease allow utility-viz
```

Run scripts inside the project environment with `uv run`:

```bash
uv run python main.py
```

## Optional dependencies

Extras enable features that require additional packages:

```bash
uv add --prerelease allow "utility-viz[animation]"    # GIF export (Pillow)
uv add --prerelease allow "utility-viz[interactive]"  # notebook widgets
uv add --prerelease allow "utility-viz[all]"          # all extras
```

## Global CLI installation

To use only the command-line interface, install it as a standalone tool so `utility-viz` is available on your `PATH`:

```bash
uv tool install --prerelease allow utility-viz
```

## Development setup

```bash
git clone https://github.com/EconViz/utility-viz.git
cd utility-viz
uv sync --all-extras
```

`uv sync` installs the `dev` dependency group by default; `--all-extras` also installs every optional dependency. Run the test suite with:

```bash
uv run pytest
```

## Verifying the installation

```bash
uv run utility-viz --version
uv run utility-viz help
```
