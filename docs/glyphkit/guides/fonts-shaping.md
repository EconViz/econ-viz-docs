---
seo_title: "Fonts and shaping"
---

# Fonts and shaping

<span id="sec-fonts-shaping"></span>

## Matching and fallback

<!-- api: glyphkit.guides_fonts_shaping_1 -->

Describes preferred families, weight, width, slant, and variation coordinates for font matching.

<!-- api: glyphkit.guides_fonts_shaping_2 -->

The recorded result of a query, including the selected face and resolved variation coordinates.

<!-- api: glyphkit.guides_fonts_shaping_3 -->

A snapshot of one usable face, with stable identity, names, metrics, character coverage, and font-table access.

```python
from glyphkit import FontLibrary, FontSource, Paragraph, TextSpan, TextStyle

library = FontLibrary.from_sources(
    (
        FontSource.path("fonts/SourceSans3-Regular.ttf"),
        FontSource.path("fonts/NotoSansTC-Regular.otf"),
    ),
    generic_families={"sans-serif": ("Source Sans 3", "Noto Sans TC")},
)
layout = library.layout(
    Paragraph((TextSpan("效用 U(x)", TextStyle(("sans-serif",), 18)),))
)
```

The examples use Source Sans 3 and Noto Sans TC, both open-source families available from Google Fonts. The mathematics chapter uses the openly licensed STIX Two Math family.

Face identity comes from the font content's SHA-256 digest and collection index, not its filename. `FontManifest` records the sources and faces needed to reproduce a layout. Glyph selection, positioning, and variation data use the structures defined by the OpenType specification [{Microsoft} (2025)](../project/references.md#opentype2025).

## Unicode shaping

<!-- api: glyphkit.guides_fonts_shaping_4 -->

The script, direction, language, OpenType features, and spacing options applied during shaping.

<!-- api: glyphkit.guides_fonts_shaping_5 -->

A visually ordered run sharing one face and shaping context, with source range and positioned glyphs.

<!-- api: glyphkit.guides_fonts_shaping_6 -->

One glyph id plus its cluster, advance, offsets, and resolved font-face identity.

<!-- api: glyphkit.guides_fonts_shaping_7 -->

Shapes Unicode text with explicit fallback and returns backend-neutral glyph ids and positions.

Mixed left-to-right and right-to-left text keeps logical source ranges even when visual runs are reordered, following the logical-versus-visual distinction in the Unicode Bidirectional Algorithm [{Unicode Consortium} (2026)](../project/references.md#unicode-bidi2026). A missing glyph raises `MissingGlyphError`; GlyphKit never swaps in an unconfigured system font silently.

## System fonts

<!-- api: glyphkit.guides_fonts_shaping_8 -->

Opt-in discovery of installed fonts. For reproducible builds, prefer explicit files or bytes and save the resulting manifest.
