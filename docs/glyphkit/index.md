---
seo_title: "GlyphKit: Renderer-Independent Typography for Python"
description: "GlyphKit selects explicit fonts, shapes Unicode, lays out paragraphs and math, extracts glyph outlines, and creates permission-aware subsets without owning a renderer."
---

<h1 class="ev-visually-hidden">GlyphKit: renderer-independent typography for Python</h1>

<p align="center">
  <img src="../assets/glyphkit/banner.svg" alt="glyphkit" style="max-width: 480px; width: 100%; margin: 2rem 0 1rem;">
</p>

GlyphKit turns caller-provided fonts and text into immutable layout data. It handles font matching, Unicode shaping, paragraphs, mathematical expressions, exact glyph outlines, and permission-aware font subsets. It does not draw or write output files.

```bash
uv add --prerelease allow glyphkit
```

```python
from glyphkit import (
    FontLibrary,
    FontSource,
    Paragraph,
    TextSpan,
    TextStyle,
)

library = FontLibrary.from_sources(
    (FontSource.path("fonts/SourceSans3-Regular.ttf"),)
)
family = library.faces[0].family
layout = library.layout(
    Paragraph(
        (
            TextSpan(
                "Utility U(x₁, x₂)", TextStyle((family,), 18)
            ),
        )
    )
)
```

## What GlyphKit owns

<div class="grid cards" markdown>

-   :material-format-font: **Fonts and shaping**

    Explicit font sources, deterministic matching, configured fallback, Unicode scripts, bidirectional text, and OpenType shaping.

    [:octicons-arrow-right-24: Fonts and shaping](guides/fonts-shaping.md)

-   :material-format-text: **Text and math layout**

    Wrapped paragraphs, logical and ink bounds, and structured OpenType MATH layout from a defined LaTeX-like grammar.

    [:octicons-arrow-right-24: Layout and mathematics](guides/layout-math.md)

-   :material-vector-curve: **Portable geometry and fonts**

    Exact glyph paths, controlled flattening, versioned ordinary data, and font subsets that check embedding permissions.

    [:octicons-arrow-right-24: Outlines and embedding](guides/outlines-embedding.md)

</div>

GlyphKit stays independent of renderers and animation packages. KineticKit uses its public data through one adapter; GlyphKit never imports KineticKit.

<!-- agora-navigation -->

## Documentation

- [Introduction](guides/introduction.md)
- [Installation](installation.md)
- [Quick start](quickstart.md)
- [Fonts and shaping](guides/fonts-shaping.md)
- [Text layout and mathematics](guides/layout-math.md)
- [Outlines, subsets, and portable data](guides/outlines-embedding.md)
- [Coordinates, metrics, and bounds](guides/coordinate-metrics.md)
- [Bézier outline geometry](guides/bezier-geometry.md)
- [OpenType mathematics layout](guides/math-layout-model.md)
- [Line construction and spacing](guides/line-layout-algorithms.md)
- [Reproducibility and renderer contracts](guides/reproducibility.md)
- [Change history](project/changelog.md)

<!-- /agora-navigation -->
