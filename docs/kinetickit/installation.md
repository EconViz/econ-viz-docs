---
seo_title: "Installation"
---

# Installation

<span id="sec-install"></span>

`kinetickit` supports Python 3.10 to 3.13. Every installation includes NumPy and GlyphKit. It is on PyPI as a pre-release, so uv needs `--prerelease allow`.

```bash
uv add --prerelease allow kinetickit               # animated SVG
uv add --prerelease allow "kinetickit[raster]"     # SVG and GIF
uv add --prerelease allow "kinetickit[interactive]"# SVG and HTML
uv add --prerelease allow "kinetickit[studio]"     # every built-in output
uv add "kinetickit[studio]==1.0.0b2"               # pin one release
```

| Extra | Adds | Output |
| --- | --- | --- |
| none | NumPy, GlyphKit | animated SVG (`vector`) |
| `raster` | Matplotlib, Pillow | GIF (`raster`) |
| `interactive` | Plotly | interactive HTML (`interactive`) |
| `studio` | all of the above | all three |

The third-party libraries stay behind private adapters. They never appear in the public scene or renderer interfaces, and they may be replaced without a breaking change.

Saving a format whose extra is missing raises `CapabilityError` and names the extra to install. No file is written. `available_formats()` lists the registered formats, so it shows all three even when an extra is missing.

For development:

```bash
git clone https://github.com/EconViz/kinetickit.git
cd kinetickit
uv sync --all-extras
uv run pytest
uv run ruff check .
uv run mypy
uv run lint-imports
uv run python -m kinetickit.conformance
```
