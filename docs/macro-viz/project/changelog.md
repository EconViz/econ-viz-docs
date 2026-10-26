---
seo_title: "Change history"
---

# Change history

`macro-viz` is at `0.2.0.dev0`. The repository's [CHANGELOG](https://github.com/EconViz/macro-viz/blob/main/CHANGELOG.md) lists every change.

## Unreleased

### Added

- The model families `keynesian`, `money`, `adas`, `islm`, `growth`, `labor`, `open_economy` and `panels`, each with typed models, comparisons and figure builders.
- A registered `[macro.*]` settings schema and a locale table in English, Traditional Chinese and Simplified Chinese.
- `macro_viz.animation` and the `macro-viz[animation]` extra: GIF and animated SVG from any builder.
- Linked four- and five-panel diagrams with typed curve movements.

### Changed

- Figures follow the manual style: black and white, only the price `p` lowercase, a thin 45-degree line.
- A curve after a change is thin and solid; a parallel shift is a straight arrow from the old equilibrium onto the new curve; a curved arrow means rotation only; curve names stand at the line end.

### Removed

- The data-series, national-accounts and business-cycle family: statistics-style charts are out of scope.
