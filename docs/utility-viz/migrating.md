---
seo_title: "Migration Guide"
description: "econ-viz was renamed to utility-viz in 2.0. What changed, which package to install, and how the compatibility layer works until 3.0."
---

# Migration Guide

`econ-viz` was renamed to **utility-viz** in 2.0.0.

!!! warning "utility-viz 2.0 is in beta"

    2.0.0b1 is a pre-release. `econ-viz` 1.x remains the stable line until 2.0 final is released.
    Pre-releases need `--prerelease allow`, for example `uv add --prerelease allow utility-viz`.

## What changed

| | 1.x | 2.x |
|---|---|---|
| Distribution | `uv add econ-viz` | `uv add utility-viz` |
| Import | `import econ_viz` | `import utility_viz` |
| CLI | `econ-viz` | `utility-viz` |
| Config file | `econ-viz.toml` | `utility-viz.toml` (section names unchanged) |

## Which package to install

| Package | Installs |
|---|---|
| `utility-viz` | `utility_viz` and the `utility-viz` command |
| `econ-viz` 2.x | `utility-viz` of the same version, plus the deprecated `econ_viz` package and `econ-viz` command |

`econ-viz` 2.x is a thin compatibility distribution that shares its version number with `utility-viz`.
Upgrading an existing 1.x installation therefore keeps working and moves you onto 2.x:

```bash
uv add --upgrade-package econ-viz econ-viz
```

!!! tip "Ready to drop the compatibility layer?"

    Switch to `uv add utility-viz`. For pre-releases, add `--prerelease allow` to either command.

## Compatibility layer

Throughout 2.x, documented 1.x code keeps working through the `econ-viz` distribution.

| Area | Behavior |
|---|---|
| `import econ_viz` | One deprecation warning per process |
| `from econ_viz import ...` and documented sub-modules | Resolve to their `utility_viz` equivalents |
| `Canvas`, `Figure`, `Animator`, `Layout` | `UtilityVizDeprecationWarning` |
| `econ-viz` command | Warns, then forwards to `utility-viz` |

- Names that did not change are the very same objects as in `utility_viz`.
- The warning is a `FutureWarning` that reads "deprecated since 2.0.0, removed in 3.0.0" and names the replacement.
- `Figure`, `Layout` and `Animator` map to their current 2.x equivalents.

!!! note "Declarative replacements are planned"

    `CanvasGrid` and `Animation` are planned replacements for `Figure` and `Animator`.
    The warning message labels them as planned.

### Config lookup

Config files are looked up in this order:

1. The explicit path.
2. `utility-viz.toml`.
3. Legacy `econ-viz.toml`, with a warning.
4. Defaults.

!!! warning "Both files exist"

    The new file wins and the legacy one is ignored with a warning.

| Call | Behavior |
|---|---|
| `Config.load()` | Follows the order above; raises if neither file exists, as in 1.x |
| `Config.discover()` | Follows the order above; falls back to defaults |
| `Config.load("file.toml")` | Reads exactly that file |

`utility-viz plot` applies the same lookup in the current directory when `--config` is not given.

### Migrate your config

```bash
utility-viz init --migrate
```

This writes `utility-viz.toml` from `econ-viz.toml` and keeps the old file.

## Removal timeline

The compatibility layer is removed in 3.0.0, not 2.0.0.

| Removed in 3.0.0 |
|---|
| `econ_viz` package |
| `econ-viz` command |
| `econ-viz.toml` lookup |

!!! info "What the compatibility contract covers"

    - **Covered:** the documented 1.x public API.
    - **Best effort:** undocumented deep module paths such as `econ_viz.canvas.renderers.*`. They may disappear at any time.
    - **Not covered:** internal `utility_viz.core.*` modules. They are advanced APIs.
