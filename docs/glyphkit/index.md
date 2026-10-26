---
seo_title: "Renderer-Independent Typography for Python"
description: "GlyphKit selects explicit fonts, shapes Unicode, lays out paragraphs and math, extracts exact glyph outlines and builds permission-aware font subsets, without owning a renderer."
---

<h1 class="ev-visually-hidden">glyphkit: renderer-independent typography for Python</h1>

<p align="center"><em>A Python typography engine that returns immutable layout data and draws nothing.</em></p>

<p align="center">
  <a href="https://github.com/EconViz/glyphkit"><img alt="GitHub" src="https://img.shields.io/badge/github-EconViz%2Fglyphkit-181818?style=flat-square&labelColor=f3f3f3"></a>
  <a href="https://pypi.org/project/glyphkit/"><img alt="PyPI" src="https://img.shields.io/pypi/v/glyphkit?include_prereleases&style=flat-square&label=pypi+package&color=181818&labelColor=f3f3f3&cacheSeconds=300"></a>
  <a href="https://pypi.org/project/glyphkit/"><img alt="Python" src="https://img.shields.io/pypi/pyversions/glyphkit?style=flat-square&color=181818&labelColor=f3f3f3"></a>
</p>

!!! warning "glyphkit 1.0 is in beta"

    glyphkit 1.0.0b4 is a pre-release. Each change between pre-releases is recorded in the [change history](project/changelog.md).

```python
from glyphkit import FontLibrary, FontSource, Paragraph, TextSpan, TextStyle

library = FontLibrary.from_sources(
    (
        FontSource.path("fonts/SourceSans3-Regular.ttf"),
        FontSource.path("fonts/NotoSansTC-Regular.otf"),
    ),
    generic_families={"sans-serif": ("Source Sans 3", "Noto Sans TC")},
)

paragraph = Paragraph(
    (TextSpan("效用 U(x₁, x₂)", TextStyle(("sans-serif",), 18)),),
    max_width=360,
)
layout = library.layout(paragraph)
print(layout.logical_bounds)
```

## Features

<div class="grid cards" markdown>

-   :material-format-font: **Fonts and shaping**

    Explicit font sources, deterministic matching, configured fallback, Unicode scripts, bidirectional text and OpenType shaping.

    [:octicons-arrow-right-24: Fonts and shaping](guides/fonts-shaping.md)

-   :material-format-text: **Paragraph layout**

    Wrapped paragraphs with logical and ink bounds, baselines, alignment and indentation, in layout units rather than pixels.

    [:octicons-arrow-right-24: Text layout and mathematics](guides/layout-math.md)

-   :material-sigma: **Structured mathematics**

    A defined LaTeX-like grammar laid out by TeX's rules with the constants of the font's OpenType MATH table.

    [:octicons-arrow-right-24: Math grammar](guides/math-grammar.md)

-   :material-vector-curve: **Exact glyph outlines**

    Move, line, quadratic, cubic and close commands in font units, with adaptive flattening to a tolerance you choose.

    [:octicons-arrow-right-24: Outlines and embedding](guides/outlines-embedding.md)

-   :material-shield-lock-outline: **Permission-aware font subsets**

    Subset bytes in SFNT or WOFF2 that respect the font's embedding permissions, and plain-data serialization with versions.

    [:octicons-arrow-right-24: Font safety](guides/reproducibility.md)

-   :material-axis-arrow: **Coordinates and metrics**

    Font units, scale, advances against ink, and which box to use when you align, crop or test for collisions.

    [:octicons-arrow-right-24: Coordinates and metrics](guides/coordinate-metrics.md)

</div>

## Install

```bash
uv add --prerelease allow glyphkit
```

Requires Python 3.10 to 3.13. See [Installation](installation.md) for the WOFF2 extra.

## Examples

Every figure in this documentation comes with the script that draws it. Download them all in one file.

[Download all examples](../assets/glyphkit/glyphkit-examples.zip){ .md-button download="" }
