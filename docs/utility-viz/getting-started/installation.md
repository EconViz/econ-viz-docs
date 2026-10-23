---
seo_title: "Installation"
---

# Installation

<span id="sec-install"></span>

## Requirements

`utility-viz` requires Python 3.10 or
later (The Python website provides installers for every operating system: [https://www.python.org/downloads/](https://www.python.org/downloads/).).
This chapter manages packages and projects with
`uv` (`uv` is a fast Python package and project manager by Astral that can also manage Python versions; see its documentation for installation and usage: [https://docs.astral.sh/uv/](https://docs.astral.sh/uv/).)
and gives the matching `pip` command where useful.

Installing the package also installs `NumPy`, `SciPy`,
`matplotlib` and `SymPy`, for array computation, numerical
solving, plotting and symbolic
algebra, together with `mosaickit` and `bezierkit`, for
backend-neutral scenes and Bézier curves (Ordinary Python plotting needs no LaTeX installation; a LaTeX distribution is only required to compile exported TikZ code.).

## Installing `uv`

The commands in this manual use `uv`. Existing projects can keep using
`pip`, `pipx` or `Poetry`; the package API does not depend
on the tool that installed it.

Run the installer for your operating system.

### macOS, Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Windows

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Installing `utility-viz`

Create a project and add `utility-viz` as a dependency:

```bash
uv init my-diagrams
cd my-diagrams
uv add utility-viz
```

Run scripts inside the project environment with `uv run`:

```bash
uv run python main.py
```

Save the basic example of [Quick start](quickstart.md#sec-quickstart) as `main.py` in the project
directory, then run the command above. `uv add` records the dependency and
`uv run` uses the project's Python environment; install and run in the same
environment.

To pin the version this manual describes, give it when adding the
dependency:

```bash
uv add "utility-viz==2.0.0b1"
```

2.0.0b1 is a pre-release. While no stable 2.x release exists,
`uv add utility-viz` and `pip install utility-viz` pick it up; once a stable
release is published alongside it, opt in to pre-releases with
`uv add --prerelease allow utility-viz` or `pip install --pre utility-viz`.

In an existing Python virtual environment, install it with `pip`:

```bash
python -m pip install -U utility-viz
```

The package is named `utility-viz`; its Python import name is `utility_viz`:

```python
from utility_viz import Canvas, solve
```

An `import` statement cannot contain a hyphen. On `ModuleNotFoundError`,
check that the interpreter running the script is the one the package was
installed into.

## Optional dependencies

<span id="sec-extras"></span>

Animation and Jupyter widgets need optional dependencies. Install the group
you need:

<!-- api: agora.utility_viz.getting_started_installation_1 -->

```bash
uv add "utility-viz[animation]"    # GIF export (Pillow)
uv add "utility-viz[interactive]"  # notebook widgets
uv add "utility-viz[all]"          # all extras
```

Installing an extra does not run an animation or open a notebook by itself;
call the API as shown in the relevant chapter.

## Installing the command-line tool

<span id="sec-install-cli"></span>

To use only the command-line interface, install `utility-viz` as a
standalone tool ([Command-line interface](cli.md#sec-cli)):

```bash
uv tool install utility-viz
```

This installs the tool in an environment of its own. To import the package
in your own Python code, still run `uv add utility-viz` in that project; calling
`uv run utility-viz` inside the project keeps the CLI and your code on the same
version.

## Development setup

```bash
git clone https://github.com/EconViz/utility-viz.git
cd utility-viz
uv sync --all-packages --all-extras
```

The repository is a `uv` workspace with two distributions
released in lockstep: `utility-viz` at the root and `econ-viz`
in `packages/econ-viz/`, the compatibility package of [Migrating from `econ-viz`](installation.md#sec-migrate).
`uv sync --all-packages --all-extras` installs both in editable mode,
together with the development dependencies and every optional dependency.
Then run the full quality gate:

```bash
uv run pytest
uv run ruff check .
uv run ruff format --check .
uv run mypy .
```

## Verifying the installation

```bash
uv run utility-viz --version   # utility-viz 2.0.0b1
uv run utility-viz help
```

The version in the comment is only an example; the output reflects the
installed version. To check that Python can import the drawing and solving
API:

```bash
uv run python -c "from utility_viz import Canvas, solve; print('OK')"
```

On a server or any environment without a display, write files with `save()`
or the CLI's `--output`. `show()` needs an interactive plotting backend, so a
window that fails to open does not mean the installation failed.

## Migrating from

<span id="sec-migrate"></span>

`econ-viz`

`econ-viz` was renamed `utility-viz` in 2.0.0 ([Names in 1.x and 2.x](installation.md#tab-migrate)).

<span id="tab-migrate"></span>

|  | 1.x | 2.x |
| --- | --- | --- |
| Distribution | `pip install econ-viz` | `pip install utility-viz` |
| Import | `import econ_viz` | `import utility_viz` |
| Command | `econ-viz` | `utility-viz` |
| Configuration file | `econ-viz.toml` | `econ-viz.toml`, shared by every EconViz package |
| Configuration layout | `[color]`, `[stroke.*]`, `[legend]`, ... at the top level | utility-viz's tables under `[utility]`; `base`, `[font]`, `[fonts]` and the shared colours at the top level |

### Which package to install

`utility-viz` ships only the `utility_viz` package and the
`utility-viz` command. `econ-viz` 2.x, released with the same version
number, is a thin compatibility distribution: it depends on `utility-viz`
of that version and adds the `econ_viz` package and the `econ-viz` command.
Upgrading a 1.x installation with `pip install --upgrade econ-viz` (add
`--pre` for a pre-release) therefore moves it onto 2.x and keeps old code
running. Switch to `pip install utility-viz` once the code no longer imports
`econ_viz`.

### Compatibility layer

Throughout 2.x, documented 1.x code keeps working:

- `import econ_viz` emits one deprecation warning per process.
- `from econ_viz import ...` and the documented submodules
  (`econ_viz.models`, `econ_viz.optimizer`, `econ_viz.themes`, ...) resolve
  to their `utility_viz` equivalents; names that did not change are the very
  same objects.
- Constructing `econ_viz.Canvas`, `econ_viz.Figure` or
  `econ_viz.animation.Animator`, or accessing `econ_viz.Layout`, emits a
  `UtilityVizDeprecationWarning` naming the replacement.
- The `econ-viz` command prints a deprecation warning and forwards its
  arguments to `utility-viz`.
- A `utility-viz.toml`, the file name of the 2.0 betas up to 2.0.0b6, is
  still read with a warning ([File lookup](../guides/themes.md#sec-config-lookup)), and so are utility-viz's
  tables at the top level of `econ-viz.toml`, the 1.x layout;
  `utility-viz init --migrate` moves them under `[utility]` in
  `econ-viz.toml` ([Creating a configuration file](cli.md#sec-cli-init)).

<!-- api: agora.utility_viz.getting_started_installation_2 -->

A `FutureWarning` subclass, so it is shown by default. Its message states
the version that deprecated the feature, the version that removes it and
the replacement, for example:

```text
econ_viz.Canvas is deprecated since 2.0.0 and will be removed in 3.0.0;
use utility_viz.Canvas instead.
```

### Updating code

Most code only needs the import name changed. Modules that were importable
on their own in 1.x now live elsewhere ([Moved modules](installation.md#tab-migrate-modules)); their names
are also available from the package root.

<span id="tab-migrate-modules"></span>

| 1.x | 2.x |
| --- | --- |
| `econ_viz.optimizer` | `utility_viz` (root) or `utility_viz.models` |
| `econ_viz.analysis` | `utility_viz.models` |
| `econ_viz.exceptions` | `utility_viz` (root) |
| `econ_viz.animation` | `utility_viz.core.animation` |
| `econ_viz.interactive` | `utility_viz.core.interactive` |

The public API is the package root (`from utility_viz import Canvas, ...`)
and `utility_viz.models`. Other `utility_viz.core.*` modules are advanced
APIs that may move between minor releases.

### Removal in 3.0.0

The `econ_viz` package, the `econ-viz` command, `utility-viz.toml` lookup
and utility-viz's tables at the top level of `econ-viz.toml` are removed in
3.0.0, not 2.0.0. Only the documented 1.x API is covered;
undocumented deep paths such as `econ_viz.canvas.renderers` resolve on a
best-effort basis and may disappear at any time.
