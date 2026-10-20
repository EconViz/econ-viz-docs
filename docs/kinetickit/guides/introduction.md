---
seo_title: "Introduction"
---

# Introduction

<span id="sec-intro"></span>

`kinetickit` is a domain-neutral animation engine. It owns scenes, motions, deterministic frame scheduling, renderer capabilities, interactions, accessibility metadata, and file export. Economics packages and other applications translate their own objects into ordinary KineticKit nodes.

One immutable scene and one motion can drive three outputs: animated SVG, streamed GIF, and self-contained interactive HTML. The same scene and time always produce the same snapshot; wall-clock timing and a particular renderer do not affect the model.

KineticKit does not import `mosaickit`, `utility-viz`, or another domain package. Font processing belongs to `glyphkit` and enters through one adapter described in [Typography and accessibility](typography-accessibility.md#sec-typography-accessibility).
