---
seo_title: "Change history"
---

# Change history

<span id="sec-changelog"></span>

Releases of `kinetickit` covered by this documentation.

## 1.0.0b2 (2026-10-19)

- GlyphKit (`>=1.0.0b2,<2`) is installed with KineticKit and owns all font processing. The `kinetickit.integrations.glyphkit` adapter is still the only import boundary, core imports stay lazy and the neutral text contracts are unchanged ([Typography](../guides/typography.md#sec-typography)).
- Added `export_png_frames(...)`, a streaming bridge from encoded PNG frames to GIF with exact centisecond error distribution ([Output formats](../guides/outputs.md#sec-outputs)).

## 1.0.0b1 (2026-10-13)

- First 1.0 beta. The motion, scene, renderer, exporter and artifact contracts in [Compatibility](../compatibility.md) are meant to be stable, and they may still change between pre-releases.
- Deterministic timelines, standard and cubic Bézier easing, keyframes and a fluent motion tree ([Time and easing](../guides/time-easing.md#sec-kinetic-time)).
- 2D and 3D scenes, path, mesh and surface morphing, and scene transitions by stable id ([Scenes and motion](../guides/scenes-motion.md#sec-scenes-motion)).
- Animated SVG, streamed GIF and interactive HTML output, with capability checks before writing ([Output formats](../guides/outputs.md#sec-outputs)).
- Interactions, accessibility metadata and the conformance suite ([Accessibility and interaction](../guides/accessibility.md#sec-accessibility)).

Known limitations of the beta are listed under [Output formats](../guides/outputs.md#sec-outputs).
