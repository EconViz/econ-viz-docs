---
seo_title: "Migration Guide"
description: "principle-econ was renamed to principle-viz. What changed, how to switch packages, and which behavior changes to expect when upgrading from principle-econ 0.1.0."
---

# Migration Guide

`principle-econ` was renamed to **principle-viz** and joined the EconViz family alongside `utility-viz`.

!!! warning "No compatibility layer"

    `principle-econ` stops receiving updates after v0.1.0, and there is no `principle_econ` shim in
    `principle-viz`. Update your imports and commands when you switch.

## What changed

| | principle-econ | principle-viz |
|---|---|---|
| Distribution | `uv add principle-econ` | `uv add principle-viz` |
| Import | `import principle_econ` | `import principle_viz` |
| CLI | `principle-econ` | `principle-viz` |

## Switch packages

```bash
uv remove principle-econ
uv add principle-viz
```

Then replace the package name in your code and scripts:

- `principle_econ` becomes `principle_viz` in every import.
- `principle-econ` becomes `principle-viz` in shell scripts and CI.

!!! tip "Module layout is unchanged"

    Sub-packages such as `core`, `policy`, `welfare`, `plot`, `api` and `cli` keep their names, so
    `principle_econ.core.line` is now `principle_viz.core.line`.

## Behavior changes since 0.1.0

Upgrading from principle-econ 0.1.0 also brings the figure changes made up to v0.10.0.

| Area | Change |
|---|---|
| Legend | `MarketFigure.finalize()` no longer adds a legend. Pass `finalize(legend=True)` to keep the old behavior |
| Welfare labels | Regions are named ("Consumer surplus", "DWL", ...) instead of lettered `A/B/C/D` |
| `LabeledRegion` | Carries `key`, `label` and `short_label` instead of `letter` |
| Curve names | Placed beside the curve end instead of only in the legend |
| Dependency | Requires `mosaickit>=0.5.1,<0.6.0`, installed automatically |

!!! note "Calculations are unchanged"

    Welfare and equilibrium results are the same. Only the drawing and labeling changed.

## For contributors

The project switched from Poetry to uv: `pyproject.toml` is PEP 621 with `uv_build`, and `uv.lock` replaces
`poetry.lock`. Use `uv sync` to set up, as described in [Installation](installation.md#development-setup).
