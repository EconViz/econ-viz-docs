---
seo_title: "Reproducibility and renderer contracts"
---

# Reproducibility and renderer contracts

<span id="sec-glyph-repro"></span>

## Font identity

GlyphKit snapshots font bytes when a `FontLibrary` is built. A face id includes a content fingerprint and collection index, so matching does not depend on later machine state.

## Deterministic inputs

For repeatable output, provide explicit `FontSource` values, keep their order stable, declare fallback families, and serialize the resulting layout or manifest. System-font discovery is an opt-in enumeration step, not hidden fallback.

<!-- api: agora.glyphkit.guides_reproducibility_1 -->

A serialisable inventory of available font faces, stable identities, sources, and variation metadata.

<!-- api: agora.glyphkit.guides_reproducibility_2 -->

Records which face and variation coordinates served one or more source ranges in a layout.

## Consumer obligations

A renderer consumes positioned glyphs in order, applies $s/U$ to exact outlines, honours offsets and baselines, and draws `MathRule` segments with supplied thickness. It must not reshape text or repeat font matching.

## Serialization and embedding

`to_data()` emits versioned plain data; `from_data()` validates schema and limits. Font subsetting enforces embedding permission and requires an explicit use.

## Backend invariance

!!! abstract "Proposition · Backend invariance"

    If two renderers consume the same layout, exact outlines, affine unit conversion, and clipping rectangle, their glyph geometry is identical up to output numeric precision.

Raster antialiasing may differ, but shaping, advances, line breaks, and Bézier geometry do not.
