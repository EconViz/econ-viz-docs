---
seo_title: "Examples"
---

# Examples

<span id="sec-examples"></span>

Each example uses only public KineticKit API and generic content: points, lines, paths, shapes, text assets, meshes and surfaces. None of them needs MosaicKit or a visualization package. The scripts sit next to the figures, and the [download](../index.md#examples) has all of them.

## A chart from plain shapes

<span id="sec-example-chart"></span>

Bars are `Shape2D` rectangles that grow with `morph_to`, and the trend line draws itself with `draw_progress`. `Axis2D` and `Grid2D` from `kinetickit.guides` compile to ordinary nodes against the resolved layout.

```python
from kinetickit import ease
from kinetickit.animation import Animation
from kinetickit.geometry.two_d import Bounds2D, Path2D, Vec2
from kinetickit.guides import Axis2D, Grid2D
from kinetickit.layout import Viewport, resolve_layout
from kinetickit.scene import PathNode2D, Scene2D, Shape2D

VALUES = [3.0, 5.5, 4.0, 7.5, 6.0]
bars = [
    Shape2D(id=f"bar{i}", path=Path2D.rect(i + 0.15, 0, 0.7, 0.0001), fill="#999999")
    for i, _ in enumerate(VALUES)
]
line = PathNode2D.polyline(
    "trend", [(i + 0.5, v) for i, v in enumerate(VALUES)], width=3, color="#000000", draw_progress=0.0
)
base = Scene2D(*bars, line)
base = base.bind({base.camera.ref("view"): Bounds2D(Vec2(-0.9, -1.2), Vec2(5.9, 9))})

layout = resolve_layout(Animation(base), Viewport(280, 420))
guides = [
    Grid2D("grid", (0, 5), (0, 8)).compile(),
    Axis2D("x", "x", (0, 5)).compile(layout),
    Axis2D("y", "y", (0, 8), at=0).compile(layout),
]
scene = Scene2D(*guides, *bars, line, camera=base.camera)

motion = None
for i, (bar, value) in enumerate(zip(bars, VALUES, strict=True)):
    grow = bar.morph_to(Path2D.rect(i + 0.15, 0, 0.7, value), duration=0.8, easing=ease.out_cubic)
    motion = grow if motion is None else motion.with_(grow, offset=0.1 * i)
motion = motion.then(line.animate.draw_progress.to(1.0, duration=1.0))

Animation(scene, motion).save("chart.svg", width=280, height=420, loop=True)
```

<span id="fig-kinetic-chart"></span>

<figure class="ev-fig" markdown>

![Bars grow one after another, then the trend line draws itself.](../../assets/kinetickit/chart/chart.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../assets/kinetickit/chart/chart.py" download aria-label="Download the source"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Download the source</span></a></div>

<figcaption markdown>Bars grow one after another, then the trend line draws itself.</figcaption>

</figure>

<!-- api: kinetickit.examples_axis2d -->

A guide that compiles to the nodes of an axis against a resolved layout.

<!-- api: kinetickit.examples_grid2d -->

A guide that compiles to grid lines.

<!-- api: kinetickit.examples_viewport -->

The size and margins of the frame that a layout is resolved for.

<!-- api: kinetickit.examples_resolve_layout -->

Resolves the camera, the margins and the units of an animation for one viewport.

## Any object model, through an adapter

<span id="sec-example-adapter"></span>

KineticKit knows nothing about your classes. You write a function that translates one object into nodes with stable ids, and `transition(before, after, depict)` matches the nodes of two states by id. Ids that exist only in `after` fade in, ids that exist only in `before` fade out, and compatible properties interpolate.

```python
import math
from dataclasses import dataclass

from kinetickit.adapters import adapt, transition
from kinetickit.animation import Animation
from kinetickit.geometry.two_d import Bounds2D, Vec2
from kinetickit.scene import Line2D, Point2D


@dataclass(frozen=True)
class Satellite:
    name: str
    angle: float
    radius: float
    tint: str


def depict(satellite: Satellite):
    position = Vec2(
        satellite.radius * math.cos(satellite.angle), satellite.radius * math.sin(satellite.angle)
    )
    return [
        Point2D(id=f"{satellite.name}.body", position=position, size=7, color=satellite.tint),
        Line2D(id=f"{satellite.name}.tether", start=Vec2(0, 0), end=position, width=1.5, color="#999999"),
    ]


before = [Satellite("alpha", 0.0, 3.0, "#000000"), Satellite("beta", 2.0, 5.0, "#666666")]
after = [
    Satellite("alpha", 1.5, 4.0, "#000000"),
    Satellite("beta", 4.0, 5.0, "#666666"),
    Satellite("gamma", 5.5, 2.0, "#999999"),
]
step = transition(before, after, depict, duration=1.5)
scene = step.scene
scene = scene.bind({scene.camera.ref("view"): Bounds2D(Vec2(-6, -6), Vec2(6, 6))})
Animation(scene, step.motion).save("satellites.svg", width=360, height=360)
```

<span id="fig-kinetic-adapter"></span>

<figure class="ev-fig" markdown>

![Two satellites move to new orbits and a third fades in.](../../assets/kinetickit/adapters/satellites.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../assets/kinetickit/adapters/satellites.py" download aria-label="Download the source"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Download the source</span></a></div>

<figcaption markdown>Two satellites move to new orbits and a third fades in.</figcaption>

</figure>

`adapt(objects, depict)` builds the plain scene of one state. A parameter sweep from another package works the same way: depict each frame's layers with the layer ids as node ids, and join the transitions with `then` ([Migrating animation code](../migration.md#sec-migration)).

<!-- api: kinetickit.examples_adapt -->

Turns a collection of your objects into one scene, by calling your depiction function on each.

<!-- api: kinetickit.examples_transition -->

Matches the nodes of two states by id and returns the scene and the motion that carries one to the other.

## A lit 3D surface

<span id="sec-example-surface"></span>

The surface example is [on the scenes page](scenes-motion.md#fig-kinetic-surface). The same animation writes SVG, GIF and HTML:

```python
animation.save("surface.svg", width=480, height=360)  # projected 3D, no extras
animation.save("surface.gif", width=320, height=240, fps=10)  # kinetickit[raster]
animation.save("surface.html", width=640, height=420, fps=12, title="Surface")  # kinetickit[interactive]
```

The projected SVG of this surface is about 2.9 MB, because every sampled frame carries all of its faces. The GIF is about 320 KB and the HTML, which embeds a plotting runtime, about 5 MB. Use a coarser grid when file size matters.

## Interactions and accessibility

<span id="sec-example-interactive"></span>

Two points carry roles, labels and reading order. Clicking `a` plays the named range `run`, and clicking `b` toggles its selection and dims it. The HTML runs both bindings. The SVG drops them, because SVG cannot run interactions, and the manifest says so.

```python
from kinetickit.accessibility import AccessibilityInfo, Semantics
from kinetickit.animation import Animation
from kinetickit.geometry.two_d import Bounds2D, Vec2
from kinetickit.interaction import Binding, Event, InteractionSpec, PlayRange, Select, SetProperty
from kinetickit.scene import Point2D, Scene2D

a = Point2D(
    id="a",
    position=Vec2(1, 1),
    size=9,
    semantics=Semantics(
        role="graphics-symbol", label="Start", description="Where the motion begins", reading_order=1
    ),
)
b = Point2D(
    id="b",
    position=Vec2(8, 8),
    size=9,
    semantics=Semantics(role="graphics-symbol", label="Goal", reading_order=2),
)
scene = Scene2D(a, b)
scene = scene.bind({scene.camera.ref("view"): Bounds2D(Vec2(0, 0), Vec2(10, 10))})
motion = a.animate.position.to(Vec2(8, 8), duration=2.0).mark("arrived", 2.0)

interactions = InteractionSpec(
    (
        Binding(Event.CLICK, (PlayRange("run"),), "a"),
        Binding(Event.CLICK, (Select(mode="toggle"), SetProperty(None, "opacity", 0.6)), "b"),
    ),
    {"run": (0.0, 2.0)},
)
info = AccessibilityInfo(
    title="Reaching the goal",
    description="A dot travels to a target",
    long_description="A dot starts at the lower left and moves to the upper right.",
)
animation = Animation(scene, motion, interactions=interactions, accessibility=info)
animation.save("interactive.html", width=480, height=480, autoplay=False)
animation.save("interactive.svg", width=480, height=480)
```

<!-- api: kinetickit.examples_playrange -->

Action that plays a named time range.

<!-- api: kinetickit.examples_select -->

Action that selects, deselects or toggles a node.

<!-- api: kinetickit.examples_setproperty -->

Action that sets a property of a node, such as its opacity.

[Open the interactive page](../../assets/kinetickit/interactive/interactive.html){ target="_blank" }. It is one self-contained file.
