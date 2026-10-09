---
seo_title: "Layers and axes"
---

# Layers and axes

<span id="sec-layers"></span>

## Common fields

<!-- api: agora.mosaickit.guides_layers_1 -->

The immutable base of every layer. All layers take these keyword-only
fields after their own positional ones.

Coordinates are pairs of finite real numbers in data units, or parameter
expressions ([Parameters, grids and animation](parameters.md#sec-parameters)). Invalid geometry raises `ConfigurationError`
when the layer is created, not when it is drawn.

## Primitive layers

<span id="tab-layers"></span>

| Layer | Default role | Draws |
| --- | --- | --- |
| `PathLayer(path, stroke)` | `primary` | The polyline through at least two points |
| `FillLayer(boundary, fill, stroke)` | `region` | The polygon on at least three points, filled and outlined |
| `MarkerLayer(points, marker)` | `point` | A marker at each of at least one point |
| `TextLayer(position, text)` | `text` | Text at a point |
| `ArrowLayer(start, end, stroke)` | `annotation` | A straight arrow, optionally labelled |
| `LegendLayer(entries, style)` | `legend` | A legend of labelled layers |
| `GroupLayer(children)` | `primary` | Nothing of its own; groups layers |

<!-- api: agora.mosaickit.guides_layers_2 -->

Joins its points with straight segments. When the resolved stroke has an
`arrow` style, arrowheads are drawn at the `START`, `END` or `BOTH` ends,
aligned with the end segments. `clip=False` lets the line run past the
plot edge at full width, which is what the axis presets use.

<!-- api: agora.mosaickit.guides_layers_3 -->

A closed polygon filled with `fill` and outlined with `stroke`. Its id is
what a `RegionLabelLayer` names.

<!-- api: agora.mosaickit.guides_layers_4 -->

One marker per point. Markers are drawn whole. A marker centred on the plot
edge, such as a point on an axis, is not cut in half; one centred outside
the plot is omitted.

<!-- api: agora.mosaickit.guides_layers_5 -->

Text at `position`, moved by `offset` points. `anchor` names the point of
the text box placed there: `center`, `left`, `right`, `top`, `bottom`,
`top-left`, `top-right`, `bottom-left` or `bottom-right`. With
`math=True` the text is set as mathematics (`"a_1"` gives $a_1$).

<!-- api: agora.mosaickit.guides_layers_6 -->

A straight arrow from `start` to `end`, with an open head unless the
stroke names another `ArrowStyle`; `label` is written at its midpoint.
A dashed, dotted or dash-dot stroke dashes the shaft and leaves the heads
solid. Arrowheads are not clipped to the plot.

<!-- api: agora.mosaickit.guides_layers_7 -->

A legend listing the layers whose ids are in `entries`, or every layer
that has a `legend` label when `entries` is empty. An id that is missing or
has no label raises `RenderError`. `LegendStyle(visible=False)` hides it.

<!-- api: agora.mosaickit.guides_layers_8 -->

Groups several layers without drawing anything of its own. Children are
drawn as if they were in the scene,
with the group's `z_index` added to theirs; an invisible group hides them
all.

## Axes

<!-- api: agora.mosaickit.guides_layers_9 -->

`build_axes` turns two axis specifications into ordinary layers with the
role `axes`. When neither has an `arrow`, the result is a closed frame
around the extents; otherwise each axis is a line along $y = 0$ or
$x = 0$, with filled triangle heads at the `ArrowPlacement` given. Titles
sit past the arrow tips: the x title to the right, the y title above, 6 pt
away.

<!-- api: agora.mosaickit.guides_layers_10 -->

Three presets, respectively: two axes from the origin with heads at the far
ends; two axes through the origin with heads at both ends; and a frame
without heads.

Every axis is made of `PathLayer` and `TextLayer`, so it can be restyled
through the `axes` role, removed by id (`axes.x`, `axes.y`, `axes.frame`,
`axes.x.label`, `axes.y.label`) or replaced by hand-made layers.
