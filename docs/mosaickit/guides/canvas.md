---
seo_title: "Canvases and scenes"
---

# Canvases and scenes

<span id="sec-canvas"></span>

## Canvas specifications

<!-- api: agora.mosaickit.guides_canvas_1 -->

The physical dimensions and coordinate ranges of a diagram. `x_range` and
`y_range` are the data ranges shown; `width` and `height` are the figure
size in inches; `dpi` is an integer in $[1, 1200]$. The properties
`x_min`, `x_max`, `y_min`, `y_max` read the ranges, and `replace(**changes)`
returns a copy with some fields changed. Ranges must be finite with
`lo < hi`, sizes positive and finite; anything else raises
`ConfigurationError`.

<!-- api: agora.mosaickit.guides_canvas_2 -->

A finite increasing interval, `lo < hi`, shared by specifications and
axes.

## Canvas

<!-- api: agora.mosaickit.guides_canvas_3 -->

A fluent builder around an immutable scene. Arguments left `None` come
from the configuration active when the canvas is created ([Configuration](themes.md#sec-config)):
its `canvas_spec`, `theme` and `renderer`. `role_overrides` maps role names
to `StyleBundle`s applied on top of the theme and the configuration
([Resolution order](themes.md#thm-resolution)).

The builder methods change the canvas, never an existing scene. Each call
replaces the canvas's scene with a new one, so an earlier snapshot, copy or
bound canvas remains unchanged.

```python
from mosaickit import Canvas, PathLayer

canvas = Canvas()
before = canvas.snapshot()
canvas.add(PathLayer([(0, 0), (1, 1)], id="line"))
# the old snapshot is unchanged
assert before.layers == ()
assert canvas.snapshot().layers[0].id == "line"
```

## Scenes

<!-- api: agora.mosaickit.guides_canvas_4 -->

A persistent, immutable, ordered collection of layers. `add()`, `extend()`,
`remove()` and `clear()` return new scenes; `Scene.empty()` is the empty
one. Layer ids must be unique across the whole scene, groups included;
a duplicate raises `ConfigurationError`. `ordered_layers` sorts the
top-level layers by `z_index`, keeping insertion order among equals, which
is the order in which they are drawn.

## Errors and warnings

| Class | Raised or emitted when |
| --- | --- |
| `MosaicKitError` | Base class of the three errors below |
| `ConfigurationError` | A model, style, theme, specification or configuration value is invalid |
| `BindingError` | A parameter is missing, has the wrong type, or an expression cannot be evaluated |
| `RenderError` | A renderer cannot do what was asked: an unknown format or renderer, a missing legend entry |
| `LayoutWarning` | Automatic placement could not avoid every obstacle ([Region and point labels](labels.md#sec-labels)) |
| `CacheBypassWarning` | A layer's model is not hashable, so it is rendered without caching |
