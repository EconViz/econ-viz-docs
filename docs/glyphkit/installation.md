---
seo_title: "Installation"
---

# Installation

<span id="sec-install"></span>

`glyphkit` supports Python 3.10 to 3.13. It is on PyPI as a pre-release, so uv needs `--prerelease allow`.

```bash
uv add --prerelease allow glyphkit
uv add --prerelease allow "glyphkit[portable]"  # WOFF2 subset payloads
uv add "glyphkit==1.0.0b4"                       # pin one release
```

The base installation includes FontTools, HarfBuzz bindings (`uharfbuzz`), Unicode segmentation (`uniseg`) and bidirectional-text support (`python-bidi`). The `portable` extra adds Brotli, which WOFF2 output needs; SFNT subsets work without it. No renderer is installed.

Fonts are not installed either. GlyphKit reads only the fonts that you pass in, so the examples assume a `fonts/` folder next to the script. They use Source Sans 3 and Noto Sans TC, both open-source families, and STIX Two Math for mathematics.

For development:

```bash
git clone https://github.com/EconViz/glyphkit.git
cd glyphkit
uv sync --all-extras
uv run pytest
uv run ruff check .
uv run mypy
uv run lint-imports
```
