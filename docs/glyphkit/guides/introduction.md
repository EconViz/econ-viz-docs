---
seo_title: "Introduction"
---

# Introduction

<span id="sec-intro"></span>

`glyphkit` turns caller-provided fonts and text into immutable layout data. It selects faces, shapes Unicode, lays out paragraphs and mathematical expressions, measures text, extracts glyph outlines and builds font subsets. A drawing package can consume the same result for SVG, HTML, raster output or another backend.

GlyphKit does not draw, animate, create scenes, download fonts, interpret licenses or write output files. Fonts enter through explicit paths, bytes or streams. System font discovery exists, but it runs only when the caller asks for it.

## Where it fits

- Use GlyphKit when a renderer needs exact glyph positions, bounds, paths or portable font bytes.
- Use `kinetickit` when those text assets need to be placed in a scene and animated.
- Keep the final renderer responsible for pixels, vector elements, files and DPI.

The everyday workflow is short: build a `FontLibrary`, describe text with `Paragraph` and `TextStyle`, call `layout()`, then pass the `TextLayout` to a consumer.

## What every result has in common

Every result is an immutable value made of ordinary data: tuples, numbers, strings and frozen dataclasses. `to_data()` turns a supported value into versioned plain data and `from_data()` validates it again. GlyphKit has no hidden global state; a face is identified by the SHA-256 of its bytes and its collection index, not by a path.
