---
seo_title: "Quick start"
---

# Quick start

<span id="sec-quickstart"></span>

One point moves across the view, and the same animation is written to three formats.

```python
from kinetickit import Animation, Bounds2D, Point2D, Scene2D, Vec2, ease

dot = Point2D(id="dot", position=Vec2(1, 1), size=8, color="#e4572e")
scene = Scene2D(dot)
scene = scene.bind({scene.camera.ref("view"): Bounds2D(Vec2(0, 0), Vec2(10, 10))})

motion = dot.animate.position.to(Vec2(9, 9), duration=1.5, easing=ease.out_cubic)
animation = Animation(scene, motion)

animation.save("dot.svg", width=400, height=400)  # native animated SVG
animation.save("dot.gif", width=400, height=400, fps=30)  # needs kinetickit[raster]
animation.save("dot.html", width=400, height=440)  # needs kinetickit[interactive]
```

<span id="fig-kinetic-dot"></span>

<figure class="ev-fig" markdown>

![The point moves from (1, 1) to (9, 9) with cubic ease-out.](../assets/kinetickit/quickstart/dot.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../assets/kinetickit/quickstart/dot.py" download aria-label="Download the source"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Download the source</span></a></div>

<figcaption markdown>The point moves from (1, 1) to (9, 9) with cubic ease-out.</figcaption>

</figure>

<!-- api: kinetickit.quickstart_1 -->

The facade that joins an immutable scene to a motion. `frames()` yields snapshots lazily, `sample(t)` returns the scene at one time, and `save()` picks an exporter from the destination suffix.

<!-- api: kinetickit.quickstart_save -->

Writes the animation and returns an `ExportManifest`. The write is atomic: a failed export leaves no file behind.

<!-- api: kinetickit.quickstart_2 -->

An immutable collection of 2D nodes plus a camera. `bind()` returns a new scene with the camera view set instead of changing the original.

<!-- api: kinetickit.quickstart_3 -->

A circular 2D mark with a stable id, a position, a size, a colour and an opacity. Each of these can be animated through `node.animate`.

<!-- api: kinetickit.quickstart_4 -->

An axis-aligned rectangle, used for camera views, clipping, layout and bounds.

<!-- api: kinetickit.quickstart_5 -->

An immutable two-component vector for positions, directions and sizes.

<!-- api: kinetickit.quickstart_6 -->

The easing namespace. [Time and easing](guides/time-easing.md#sec-kinetic-time) lists every function.

## Reading the scene at a time

A scene and a time always give the same state, so you can ask for any moment without playing the animation.

```python
print(animation.duration)  # 1.5
print(animation.sample(0.0).get("dot").position)  # Vec2(x=1.0, y=1.0)
print(animation.sample(0.75).get("dot").position)  # Vec2(x=8.0, y=8.0)
print(animation.sample(1.5).get("dot").position)  # Vec2(x=9.0, y=9.0)
```

At 0.75 seconds the progress is 0.5, and cubic ease-out gives $1 - (1 - 0.5)^3 = 0.875$ of the way, so the point is at $1 + 8 \times 0.875 = 8$.

## Composing motions

A motion is a value. Combine motions with `then`, `with_`, `delay`, `repeat`, `yoyo`, `reverse` and `trim`, and give a moment a name with `mark`.

```python
from kinetickit import Animation, Bounds2D, Point2D, Scene2D, Vec2

a = Point2D(id="a", position=Vec2(0, 0), size=8)
b = Point2D(id="b", position=Vec2(0, 5), size=8, opacity=0.0)
c = Point2D(id="c", position=Vec2(5, 5), size=4)
scene = Scene2D(a, b, c)
scene = scene.bind({scene.camera.ref("view"): Bounds2D(Vec2(-1, -1), Vec2(11, 11))})

motion = (
    a.animate.position.to(Vec2(5, 5), duration=1.0)
    .then(b.animate.opacity.to(1.0, duration=0.5).with_(c.animate.size.to(9, duration=0.5)))
    .mark("settled")
)
print(Animation(scene, motion).duration)  # 1.5
```

The GIF and HTML lines need their matching extras. Capability checks run before a destination is opened, so an unsupported combination raises `CapabilityError` and leaves no partial file ([Output formats](guides/outputs.md#sec-outputs)).
