---
seo_title: "Change history"
---

<span id="sec-changelog"></span>

# Change history

Release history of `utility-viz`. Documentation-only changes are not
listed; each entry is tagged where the feature it describes is documented,
following l3doc convention, so the page number is the real page.

## 2.0.0b1

- Renamed from `econ-viz` to `utility-viz`: distribution, import package, command and configuration file [Introduction](../guides/introduction.md)
- Internals reorganised into `core` and `models`; the public API is the package root and `utility_viz.models` [Introduction](../guides/introduction.md)
- New dependencies `mosaickit` and `bezierkit` [Introduction](../guides/introduction.md)
- The whole repository passes `mypy`; Ruff enforces line length, complexity and statement limits [Introduction](../guides/introduction.md)
- `utility-viz` — New dependencies `mosaickit>=0.5.1,<0.6.0` and `bezierkit>=0.5.0rc1,<0.6.0` [Installation](../getting-started/installation.md)
- `utility-viz` — The repository is a `uv` workspace releasing `utility-viz` and `econ-viz` in lockstep [Installation](../getting-started/installation.md)
- `econ-viz` — Renamed to `utility-viz`; the `econ_viz` package, the `econ-viz` command and `econ-viz.toml` lookup remain as a deprecated compatibility layer until 3.0.0 [Installation](../getting-started/installation.md)
- `econ-viz` — The compatibility layer ships as a separate `econ-viz` distribution, so upgrading a 1.x installation no longer deletes files shared with `utility-viz` [Installation](../getting-started/installation.md)
- `UtilityVizError` — `UtilityVizError` is the base exception; `EconVizError` remains as an alias of the same class [Quick start](../getting-started/quickstart.md)
- `Leontief` — Indifference curves of kinked utilities keep exact right-angle corners in Matplotlib and TikZ output [Core models](../models/index.md)
- `core.scenes` — Backend-neutral `mosaickit` layer factories for budget lines, equilibria and indifference curves, with native Bézier TikZ export [Advanced models](../models/advanced.md)
- `Config` — Default file renamed `utility-viz.toml`; legacy `econ-viz.toml` still read with a warning [Themes and configuration](../guides/themes.md)
- `Config.discover` — New `Config.discover()`, falling back to the built-in defaults when no file exists [Themes and configuration](../guides/themes.md)
- `utility-viz` — The command is now `utility-viz`; `econ-viz` prints a deprecation warning and forwards to it [Command-line interface](../getting-started/cli.md)
- `utility-viz plot` — Without `--config`, reads `utility-viz.toml` (or legacy `econ-viz.toml`) from the current directory [Command-line interface](../getting-started/cli.md)
- `utility-viz init` — New `--migrate` option [Command-line interface](../getting-started/cli.md)
- `Animator` — Moved to `utility_viz.core.animation` [Animation](../guides/animation.md)
- `WidgetViewer` — Moved to `utility_viz.core.interactive` [Interactive widgets](../guides/interactive.md)

## 1.12.0

- Focal and secondary indifference-curve levels, with numeric or ordinal labels [Introduction](../guides/introduction.md)
- `Canvas.add_utility` — Focal utility level, secondary curve style and ordinal labels [Canvas](../guides/canvas.md)
- `Theme` — Colour, width and opacity of secondary indifference curves [Themes and configuration](../guides/themes.md)

## 1.11.0

- Complete theme system: one visual language across canvases, multi-panel figures, demand diagrams, decompositions and Edgeworth boxes [Introduction](../guides/introduction.md)
- `Canvas` — Backgrounds, labels, lines and markers all take their defaults from the theme [Canvas](../guides/canvas.md)
- `Figure` — Panel backgrounds, labels, lines and markers fully follow the theme [Figures and demand diagrams](../guides/consumer.md)
- `EdgeworthBox` — Box frame, contract curve, core, endowment, price line and Walrasian equilibrium fully follow the theme [Figures and demand diagrams](../guides/consumer.md)
- `Theme` — Complete theme system: background colour, label scale and defaults for every economic layer [Themes and configuration](../guides/themes.md)
- `themes` — New `paper`, `monochrome`, `presentation` and `dark` themes [Themes and configuration](../guides/themes.md)
- `Config` — Configuration files accept every built-in theme and keep the same visual meaning across diagram types [Themes and configuration](../guides/themes.md)
- `econ-viz plot` — `--theme` accepts every built-in CLI theme [Command-line interface](../getting-started/cli.md)

## 1.10.1

- Ships `py.typed`; CI runs Ruff and Mypy [Introduction](../guides/introduction.md)

## 1.10.0

- `econ-viz` — Python 3.10 reads TOML configuration files with `tomli` [Installation](../getting-started/installation.md)
- `Figure` — Falls back to the active `Config` when no theme or font is given [Figures and demand diagrams](../guides/consumer.md)
- `EdgeworthBox` — Falls back to the active `Config` when no theme or font is given [Figures and demand diagrams](../guides/consumer.md)
- `Config` — `Config`, `econ-viz.toml`, `econ-viz init` and `plot --config` [Themes and configuration](../guides/themes.md)
- `econ-viz init` — Configuration-template command and `plot --config` [Command-line interface](../getting-started/cli.md)

## 1.9.0

- `Canvas` — Axes, origin, titles and other text elements accept a `Label` [Canvas](../guides/canvas.md)
- `Stroke` — New `opacity` field [Canvas](../guides/canvas.md)
- `DemandDiagram` — Supports `Legend`, `Marker`, `Label` and per-layer `Stroke` [Figures and demand diagrams](../guides/consumer.md)
- `Canvas.add_decomposition` — Draws the indifference curves through A, B and C by default, with curve labels and `Legend` [Figures and demand diagrams](../guides/consumer.md)
- `Canvas.add_decomposition` — Effect arrows below the horizontal axis point A→B and B→C; zero effects draw no arrow [Figures and demand diagrams](../guides/consumer.md)
- `Haagsma` — Haagsma utility model with a closed-form solution, for inferior- and Giffen-good analysis [Core models](../models/index.md)

## 1.8.0

- `Canvas` — `Axis`, `Marker`, `Label` and `Fill` style objects [Canvas](../guides/canvas.md)
- `Stroke` — Every line style is a `Stroke`; the individual style arguments remain as shorthands [Canvas](../guides/canvas.md)
- `Canvas.add_decomposition` — `Effect`, `Marker` and `Label` style objects [Figures and demand diagrams](../guides/consumer.md)
- `EdgeworthBox` — Markers, text and axes accept `Marker`, `Label` and `Axis` [Figures and demand diagrams](../guides/consumer.md)

## 1.7.0

- CI tests Python 3.10--3.13, enforces branch coverage, and smoke-tests runnable examples [Introduction](../guides/introduction.md)
- Tagged releases publish only after tests pass [Introduction](../guides/introduction.md)
- `econ-viz` — Package management and builds migrated to `uv` [Installation](../getting-started/installation.md)
- `econ-viz` — All example scripts run from a clean checkout [Installation](../getting-started/installation.md)
- `Canvas` — Per-figure text and math fonts without changing `matplotlib`'s global configuration [Canvas](../guides/canvas.md)
- `Canvas` — Independent axis-label positions, line styles and arrowhead styles for `Canvas` and `Figure` [Canvas](../guides/canvas.md)
- `Stroke` — One `Stroke` controls line width, style, colour and arrowheads across canvases, figures, demand diagrams and Edgeworth boxes [Canvas](../guides/canvas.md)
- `CobbDouglas` — Fixed utility domains, asymmetric CES expansion paths, Cobb-Douglas limit cases, and satiation optima that leave income unspent [Core models](../models/index.md)
- `CobbDouglas` — Fixed contour levels when utility is near zero or negative [Core models](../models/index.md)
- `comparative_statics` — Comparative statics no longer step outside the domain near zero prices or income, or near subsistence constraints [Analysis](../tools/analysis.md)
- `econ-viz` — `econ-viz --version` prints the installed package version [Command-line interface](../getting-started/cli.md)

## 1.6.0

- Generated files under `examples/output/` are no longer tracked [Introduction](../guides/introduction.md)
- `Canvas` — Default indifference-curve line width reduced from `2.0` to `1.8` [Canvas](../guides/canvas.md)
- `themes.default` — Colour-blind-friendly default palette, with `COLORBLIND_CYCLE_RGB` and `COLORBLIND_CYCLE_HEX` [Themes and configuration](../guides/themes.md)
- `Canvas.save` — TikZ axis regression tests no longer depend on colour indices [Export](../guides/export.md)
- `Animator` — Animation examples moved to `examples/scripts/animation.py` [Animation](../guides/animation.md)

## 1.5.0

- New example scripts for decomposition, demand diagrams, PCC/ICC paths, multi-panel layouts and TikZ export [Introduction](../guides/introduction.md)
- Regression tests for TikZ export and price-effect decomposition [Introduction](../guides/introduction.md)
- `econ-viz` — Notebook install flow on Colab is restart-safe [Installation](../getting-started/installation.md)
- `Figure` — Better placement and visibility of axis labels in shared-panel layouts [Figures and demand diagrams](../guides/consumer.md)
- `decompose_price_effect` — Price-effect decomposition: `decompose_price_effect()`, `PriceEffectDecomposition` and `Canvas.add_decomposition()`, drawing bundles A/B/C with substitution and income effects [Figures and demand diagrams](../guides/consumer.md)
- `decompose_price_effect` — Decomposition API importable from the package root [Figures and demand diagrams](../guides/consumer.md)
- `Canvas.save` — Pure TikZ export backend; `Canvas.save()` and `Figure.save()` accept `.tex` [Export](../guides/export.md)

## 1.4.0

- Tests for `Animator` and `WidgetViewer` [Introduction](../guides/introduction.md)
- `econ-viz[extras]` — Optional extras `animation`, `interactive` and `all` [Installation](../getting-started/installation.md)
- `Animator.save` — Frames are composited onto an opaque background before export, for more reliable GIFs [Export](../guides/export.md)
- `Animator` — `Animator` produces GIF parameter sweeps with `Pillow`, without `ffmpeg` [Animation](../guides/animation.md)
- `Animator` — GIF examples for utility-parameter, price, income and budget-only sweeps [Animation](../guides/animation.md)
- `WidgetViewer` — `WidgetViewer` provides slider controls in Jupyter notebooks [Interactive widgets](../guides/interactive.md)
- `WidgetViewer` — Numeric input boxes for notebook widgets [Interactive widgets](../guides/interactive.md)

## 1.3.2

- Publish workflow skips versions already on PyPI [Introduction](../guides/introduction.md)
- `EdgeworthBox` — Contract curve and price line default to black dashed lines [Figures and demand diagrams](../guides/consumer.md)

## 1.3.1

- Package-root exports load lazily, with the public API unchanged [Introduction](../guides/introduction.md)
- `Canvas` — Canvas rendering split into `canvas.renderers` and `canvas.primitives` [Canvas](../guides/canvas.md)
- `EdgeworthBox` — Edgeworth internals split into compute, state and plotter modules [Figures and demand diagrams](../guides/consumer.md)
- `models.registry` — Model registry (`models.registry`) used by the command-line tool to build models [Core models](../models/index.md)
- `CobbDouglas` — Contour-level rules gathered in `contours.level_policies` [Core models](../models/index.md)
- `Canvas.save` — `Canvas`, `Figure` and `EdgeworthBox` share one figure exporter (`io.exporter`) [Export](../guides/export.md)
- `econ-viz` — CLI errors raise `CliConfigError`, with exit handling centralised in `cli.main` [Command-line interface](../getting-started/cli.md)

## 1.3.0

- `examples/edgeworth_box.py` covering common utility-function combinations [Introduction](../guides/introduction.md)
- Dedicated Edgeworth tests [Introduction](../guides/introduction.md)
- `EdgeworthBox` — `EdgeworthBox` and `EquilibriumFocusConfig` for two-consumer exchange diagrams [Figures and demand diagrams](../guides/consumer.md)
- `EdgeworthBox` — Contract-curve, core and Walrasian-equilibrium overlays, with equilibrium-focused indifference curves [Figures and demand diagrams](../guides/consumer.md)

## 1.2.3

- `slutsky_matrix` — `SlutskyMatrix` checks symmetry, negative semidefiniteness and homogeneity, and warns when a condition fails [Analysis](../tools/analysis.md)
- `econ-viz models` — CLI supports `QuasiLinear`, `StoneGeary` and `Translog` [Command-line interface](../getting-started/cli.md)

## 1.2.2

- Dedicated PCC/ICC example generator and tests [Introduction](../guides/introduction.md)
- `PricePath` — PCC/ICC paths are smoothed by default, with slightly extended ends and no markers unless requested [Figures and demand diagrams](../guides/consumer.md)
- `PricePath` — PCC/ICC paths use their own colours; more padding in the goods space of demand diagrams [Figures and demand diagrams](../guides/consumer.md)

## 1.2.0

- `Layout` — Multi-panel `Figure` layouts and the `Layout` enum [Figures and demand diagrams](../guides/consumer.md)
- `PricePath` — `PricePath`, `IncomePath` and `Canvas.add_path()` for PCC/ICC plots [Figures and demand diagrams](../guides/consumer.md)
- `DemandDiagram` — `DemandDiagram`, linking goods space and Marshallian demand [Figures and demand diagrams](../guides/consumer.md)

## 1.1.0

- `Translog` — `Translog` model, with legends and indifference-curve labels [Core models](../models/index.md)
- `comparative_statics` — `comparative_statics` helper [Analysis](../tools/analysis.md)
- `HomogeneityAnalyzer` — `HomogeneityAnalyzer` and `ReturnsToScale` in the analysis module [Analysis](../tools/analysis.md)

## 1.0.2

- `econ-viz` — NumPy upper bound removed to avoid conflicts on Colab [Installation](../getting-started/installation.md)
- `Canvas` — Math axis labels are no longer double-wrapped [Canvas](../guides/canvas.md)

## 1.0.1

- `econ-viz` — Pin `numpy<2` to avoid ABI mismatches on Colab and local installs [Installation](../getting-started/installation.md)
- `econ-viz` — Relaxed Python and NumPy bounds; `pytest` pinned to 8.x [Installation](../getting-started/installation.md)

## 1.0.0

- Initial release [Change history](changelog.md)

