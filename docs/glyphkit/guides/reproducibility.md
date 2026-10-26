---
seo_title: "Reproducibility and font safety"
---

# Reproducibility and font safety

<span id="sec-glyph-repro"></span>

## Font identity

GlyphKit never searches the machine while it builds an ordinary `FontLibrary`. Supply font paths, immutable bytes or a binary stream. It reads the input once and identifies a face by the SHA-256 of the bytes and the collection index, so relocating identical bytes does not change the identity.

## Deterministic inputs

For repeatable output, provide explicit `FontSource` values, keep their order stable, declare the fallback families, and serialize the resulting layout or manifest. System-font discovery is an opt-in enumeration step, never a hidden fallback. `discover_system_fonts()` returns a manifest. Freeze it, then restore it only through a resolver that checks the recorded fingerprint. A manifest is an inventory, not a bundle of font bytes.

<!-- api: glyphkit.guides_reproducibility_1 -->

A serialisable inventory of the faces, with their stable identities, sources and variation metadata.

<!-- api: glyphkit.guides_reproducibility_2 -->

Records which face and variation coordinates served one or more source ranges of a layout.

Font input is bounded to 128 MiB. Empty, malformed, inaccessible and oversized data raise structured GlyphKit errors. GlyphKit does not use the network, and it never silently selects an unconfigured system font.

## Font safety
<span id="sec-font-safety"></span>

`library.subset()` returns bytes and metadata. The policy is mechanical and is not legal advice:

| Declared permission | Default result |
| --- | --- |
| Installable or editable | Allowed for the compatible use |
| Preview or print | Only non-editable preview or print output |
| Restricted | Rejected |
| Unknown or absent | Rejected unless `allow_unknown=True` |

The caller stays responsible for the font license and the distribution rights. The optional `portable` profile enables WOFF2, and SFNT subsets are available in the base package.

## Consumer obligations

A renderer consumes the positioned glyphs in order, applies $s/U$ to the exact outlines, honours the offsets and baselines, and draws each `MathRule` with the thickness it supplies. It must not reshape the text or repeat font matching.

## Backend invariance

!!! abstract "Proposition · Backend invariance"
    If two renderers consume the same layout, the same exact outlines, the same affine unit conversion and the same clipping rectangle, their glyph geometry is identical up to the numeric precision of the output.

Raster antialiasing may differ, but the shaping, the advances, the line breaks and the Bézier geometry do not.
