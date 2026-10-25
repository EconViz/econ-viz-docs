---
seo_title: "Change history"
---

<span id="sec-changelog"></span>

# Change history

Release history of `micro-viz`. The package is at version 0.2.0.dev0 and is not on PyPI yet; the repository's [CHANGELOG](https://github.com/EconViz/micro-viz/blob/main/CHANGELOG.md) lists every change. Documentation-only changes are not listed; each entry is tagged where the feature it describes is documented, following l3doc convention, so the page number is the real page.

## 0.2.0.dev0

- First manual edition for the development version: producer theory, market structure, factor markets, uncertainty and information [Introduction](guides/introduction.md)
- Figures are built on `mosaickit` (`mosaickit>=1.0.0rc9,<2.0.0`) [Introduction](guides/introduction.md)
- `Config` — Settings are read from the shared `econ-viz.toml`; `micro-viz` declares its own tables under `[micro]` [Settings](guides/settings.md)
- `Config` — `[micro.region]` shades the marginal-return regions or not, to the top of the plot or only under the curve [Settings](guides/settings.md)
- `save_svg` — Animated SVG and GIF from the same builder that draws the static figure; needs the `animation` extra [Animation](guides/animation.md)

