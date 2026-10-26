---
seo_title: "Coordinates, metrics, and bounds"
---

# Coordinates, metrics, and bounds

<span id="sec-glyph-coordinates"></span>

## Font units and layout scale

Font files store outlines and metrics in font units. If a face has $U$ units per em and the requested size is $s$, GlyphKit uses $\lambda = s / U$. A font-space point $p = (x, y)$ reaches layout space as $\lambda p$. A positioned glyph adds the shaping origin and offset:

$$
p' = (x_g + \delta_x, y_g + \delta_y) + \lambda p.
$$

[Baselines, width, and vertical font metrics](../quickstart.md#fig-glyph-metrics) marks the ascender line, the baseline, the descender line and the advance width. GlyphKit reads those metrics in font units and maps them into layout space with $\lambda$; width and depth are measured in the same coordinate system. A layout is y-up, with the first baseline at $y = 0$.

## Advances are not ink

The pen position after glyph $i$ is $x_{i+1} = x_i + a_i$, where $a_i$ is its shaped advance. The visible outline may begin before $x_i$ or extend beyond $x_{i+1}$. GlyphKit therefore reports both a logical box $L$ and an ink box $I$.

!!! abstract "Definition · Bounds union"

    For non-empty axis-aligned boxes $B_j$, their union has $x_{\min} = \min_j x_{\min,j}$, $y_{\min} = \min_j y_{\min,j}$, $x_{\max} = \max_j x_{\max,j}$, and $y_{\max} = \max_j y_{\max,j}$.

## Choosing the correct box

Use logical bounds to align lines and reserve space. Use ink bounds for cropping, collision tests, and tight export. A renderer should keep the baseline explicit instead of inferring it from either rectangle.

## DPI enters only at the edge

GlyphKit does not choose pixels. A consumer exporting at $d$ dots per inch maps $q$ typographic points to $q d / 72$ pixels. Keeping this conversion outside the layout engine makes one `TextLayout` reusable in SVG, PDF, raster, and animation renderers.

!!! warning "Known issue in 1.0.0b4"

    The `ink_bounds` of a `LineLayout` and of a `TextLayout` are built from glyph extents that are relative to each glyph's origin, so they do not cover a line of several glyphs, and they are wrong for wrapped lines. Until this is fixed, use the logical bounds, or take the union of `glyph.x + glyph.ink_bounds.x_max` and its siblings yourself for text that is not wrapped.
