---
seo_title: "Outlines, subsets, and portable data"
---

# Outlines, subsets, and portable data

<span id="sec-outlines-embedding"></span>

## Glyph geometry

```python
glyph = layout.lines[0].runs[0].glyphs[0]
outline = library.outline(glyph)
print(outline.units_per_em, outline.bounds, outline.commands[:3])
```

<!-- api: glyphkit.outlines_outline -->

Returns the exact outline of a positioned glyph. It is in font units, so scale it by the run's `size / outline.units_per_em` and add the glyph's position.

<!-- api: glyphkit.guides_outlines_embedding_1 -->

An exact glyph outline: ordered path commands, bounds and the units per em.

<!-- api: glyphkit.guides_outlines_embedding_2 -->

Starts a new contour at the given point in font space.

<!-- api: glyphkit.guides_outlines_embedding_3 -->

Adds a straight segment from the current point to its end point.

<!-- api: glyphkit.guides_outlines_embedding_4 -->

Adds a quadratic Bézier segment with one control point and one end point.

<!-- api: glyphkit.guides_outlines_embedding_5 -->

Adds a cubic Bézier segment with two control points and one end point.

<!-- api: glyphkit.guides_outlines_embedding_6 -->

Closes the current contour by connecting it to its start.

<!-- api: glyphkit.guides_outlines_embedding_7 -->

Approximates curved commands with line segments at a tolerance that you choose, in font units.

<!-- api: glyphkit.guides_outlines_embedding_8 -->

One open or closed sequence of points returned by flattening.

<span id="fig-glyph-outline"></span>

<figure class="ev-fig" markdown>

![The exact outline of a glyph. Squares are on-curve points, circles are control points, and dashed lines are control polygons.](../../assets/glyphkit/outlines/glyph.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../assets/glyphkit/outlines/glyph.py" download aria-label="Download the source"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Download the source</span></a></div>

<figcaption markdown>The exact outline of a glyph. Squares are on-curve points, circles are control points, and dashed lines are control polygons.</figcaption>

</figure>

## Permission-aware subsets

<!-- api: glyphkit.outlines_subset -->

Builds a font subset that covers a layout, and returns bytes and metadata. It never writes markup or a file.

<!-- api: glyphkit.guides_outlines_embedding_9 -->

Declares why the subset will be embedded, so the font's permissions are enforced for that use.

<!-- api: glyphkit.guides_outlines_embedding_10 -->

Chooses the container of the returned font: SFNT (OpenType) or WOFF2.

<!-- api: glyphkit.guides_outlines_embedding_11 -->

The complete subsetting result: the portable fonts, diagnostics and metadata.

<!-- api: glyphkit.guides_outlines_embedding_12 -->

One permission-checked font payload with family, subset tag, glyph ids, permission and the bytes.

```python
from glyphkit.embedding import EmbeddingUse, FontContainer

bundle = library.subset(layout, embedding_use=EmbeddingUse.WEB, container=FontContainer.WOFF2)
```

WOFF2 needs the `portable` extra. The permission rules are on the [Reproducibility and font safety](reproducibility.md#sec-font-safety) page.

## Serialization

<!-- api: glyphkit.guides_outlines_embedding_13 -->

Converts a supported immutable public value into versioned plain data that is ready for JSON-like storage.

<!-- api: glyphkit.guides_outlines_embedding_14 -->

Validates versioned data and rebuilds the public value within the configured limits.
