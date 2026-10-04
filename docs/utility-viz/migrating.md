---
seo_title: "Migrating from econ-viz"
description: "econ-viz was renamed to utility-viz in 2.0. What changed, which package to install, and how the compatibility layer works until 3.0."
---

# Migrating from econ-viz

`econ-viz` was renamed to **utility-viz** in 2.0.0.

!!! warning "utility-viz 2.0 is in beta"

    2.0.0b1 is a pre-release. `econ-viz` 1.x remains the stable line until 2.0 final is released.
    Pre-releases need `--pre`, for example `pip install --pre utility-viz`.

## What changed

| | 1.x | 2.x |
|---|---|---|
| Distribution | `pip install econ-viz` | `pip install utility-viz` |
| Import | `import econ_viz` | `import utility_viz` |
| CLI | `econ-viz` | `utility-viz` |
| Config file | `econ-viz.toml` | `utility-viz.toml` (section names unchanged) |

## Which package to install

`utility-viz` ships only `utility_viz` and the `utility-viz` command. It has no `econ_viz` package and no
`econ-viz` command.

`econ-viz` 2.x (same version number) is a thin compatibility distribution. `pip install econ-viz` installs
`utility-viz` of the same version plus the `econ_viz` package and the `econ-viz` command, which warn that
they are deprecated. Upgrading an existing 1.x installation with `pip install --upgrade econ-viz` therefore
keeps working and moves you onto 2.x. Pre-releases need `--pre`, for example
`pip install --pre --upgrade econ-viz`.

Switch to `pip install utility-viz` when you are ready to drop the compatibility layer.

## Compatibility layer

Throughout 2.x the `econ-viz` distribution provides an `econ_viz` package and an `econ-viz` command, so
documented 1.x code keeps working:

- `import econ_viz` emits one deprecation warning per process.
- `from econ_viz import ...` and the documented sub-modules (`econ_viz.models`, `econ_viz.optimizer`,
  `econ_viz.themes`, ...) resolve to their `utility_viz` equivalents. Names that did not change are the very
  same objects.
- Constructing `econ_viz.Canvas`, `econ_viz.Figure` or `econ_viz.animation.Animator`, or accessing
  `econ_viz.Layout`, emits a `utility_viz.UtilityVizDeprecationWarning` (a `FutureWarning`) stating
  "deprecated since 2.0.0, removed in 3.0.0" and the replacement. `Figure`, `Layout` and `Animator` map to
  their current 2.x equivalents; their declarative replacements (`CanvasGrid`, `Animation`) are planned and
  named in the message as such.
- Config lookup: explicit path, then `utility-viz.toml`, then legacy `econ-viz.toml` (with a warning), then
  defaults. If both files exist the new one wins and the legacy one is ignored with a warning.
  `Config.load()` with no argument follows the file order and raises if neither file exists (as in 1.x);
  `Config.discover()` falls back to defaults; `Config.load("file.toml")` reads exactly that file.
  `utility-viz plot` applies the same lookup in the current directory when `--config` is not given.
- The `econ-viz` command prints a deprecation warning and forwards to `utility-viz`.
- `utility-viz init --migrate` writes `utility-viz.toml` from `econ-viz.toml` and keeps the old file.

## Removal boundary (3.0.0)

The `econ_viz` package, the `econ-viz` command and `econ-viz.toml` lookup are removed in 3.0.0, not 2.0.0.

Only the documented 1.x public API is covered. Undocumented deep module paths (for example
`econ_viz.canvas.renderers.*`) resolve on a best-effort basis and may disappear at any time. Internal
`utility_viz.core.*` modules are advanced APIs and not part of the compatibility contract.
