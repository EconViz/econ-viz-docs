---
seo_title: "Typography and accessibility"
---

# Typography and accessibility

<span id="sec-typography-accessibility"></span>

## GlyphKit integration

```python
from glyphkit import FontLibrary, FontSource
from kinetickit import Animation, Bounds2D, Scene2D, Text2D, Vec2
from kinetickit.integrations.glyphkit import GlyphKitTypography

library = FontLibrary.from_sources(
    (FontSource.path("fonts/SourceSans3-Regular.ttf"),)
)
typography = GlyphKitTypography(
    library,
    families=(library.faces[0].family,),
    size=48,
)
title = Text2D(
    id="title",
    asset=typography.asset("HELLO"),
    position=Vec2(1, 1),
    scale=0.05,
)
scene = Scene2D(title).bind(
    {"camera.view": Bounds2D(Vec2(0, 0), Vec2(10, 6))}
)
motion = title.animate.position.to(Vec2(4, 3), duration=1.5)
Animation(scene, motion).save("text.svg")
```

<!-- api: agora.kinetickit.guides_typography_accessibility_1 -->

A configured adapter that turns text or mathematics into renderer-neutral KineticKit `TextAsset` values.

<!-- api: agora.kinetickit.guides_typography_accessibility_2 -->

Converts an existing GlyphKit `TextLayout` into positioned paths, metrics, and optional portable font data.

<!-- api: agora.kinetickit.guides_typography_accessibility_3 -->

Converts a GlyphKit `MathBox` tree, including glyphs and rules, into a KineticKit text asset.

Installing KineticKit installs a compatible GlyphKit. Core KineticKit imports remain lazy: only `kinetickit.integrations.glyphkit` imports the typography package.

<span id="fig-kinetic-type"></span>

<figure class="ev-fig" markdown>

![GlyphKit outlines embedded in a KineticKit animated SVG](../../assets/kinetickit/agora/typography/glyphkit-text.svg){ .ev-figure-lg }

<figcaption markdown>GlyphKit outlines embedded in a KineticKit animated SVG</figcaption>

</figure>

## Semantics and reduced motion

<!-- api: agora.kinetickit.guides_typography_accessibility_4 -->

Per-node accessibility metadata: role, label, description, reading order, and decorative status.

<!-- api: agora.kinetickit.guides_typography_accessibility_5 -->

Animation-level title, description, language, and ordered semantic information.

<!-- api: agora.kinetickit.guides_typography_accessibility_6 -->

Specifies the representative static state and autoplay behaviour when reduced motion is requested.

`ReducedMotion` corresponds to the web platform's `prefers-reduced-motion` user preference [{W3C} (2026)](../project/references.md#mediaqueries5); it is an authored alternative, not an automatic reduction in frame rate.

SVG and HTML preserve titles, descriptions, stable object ids, and per-node semantics. HTML adds keyboard-operable controls and an ordered object list. GIF cannot carry those runtime semantics, so accessibility output requires a text description and may include a representative PNG.

## Interaction

<!-- api: agora.kinetickit.guides_typography_accessibility_7 -->

A portable interaction trigger such as hover, click, focus, or playback progress.

<!-- api: agora.kinetickit.guides_typography_accessibility_8 -->

Connects one event to a data-only action and marks whether that interaction is required.

<!-- api: agora.kinetickit.guides_typography_accessibility_9 -->

The validated collection of bindings attached to an animation.
