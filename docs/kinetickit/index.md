---
seo_title: "Deterministic 2D and 3D Animation for Python"
description: "KineticKit builds deterministic 2D and 3D animation from immutable scenes and motions, then writes animated SVG, streamed GIF or self-contained interactive HTML."
---

<h1 class="ev-visually-hidden">kinetickit: deterministic 2D and 3D animation for Python</h1>

<p align="center"><em>A domain-neutral engine for precise, deterministic 2D and 3D animation.</em></p>

<p align="center">
  <a href="https://github.com/EconViz/kinetickit"><img alt="GitHub" src="https://img.shields.io/badge/github-EconViz%2Fkinetickit-181818?style=flat-square&labelColor=f3f3f3"></a>
  <a href="https://pypi.org/project/kinetickit/"><img alt="PyPI" src="https://img.shields.io/pypi/v/kinetickit?include_prereleases&style=flat-square&label=pypi+package&color=181818&labelColor=f3f3f3&cacheSeconds=300"></a>
  <a href="https://pypi.org/project/kinetickit/"><img alt="Python" src="https://img.shields.io/pypi/pyversions/kinetickit?style=flat-square&color=181818&labelColor=f3f3f3"></a>
</p>

!!! warning "kinetickit 1.0 is in beta"

    kinetickit 1.0.0b2 is a pre-release. The contracts listed in [Compatibility](compatibility.md) are meant to be stable, but they may still change between pre-releases, always with a changelog entry.

```python
from kinetickit import Animation, Bounds2D, Point2D, Scene2D, Vec2, ease

dot = Point2D(id="dot", position=Vec2(1, 1), size=8, color="#e4572e")
scene = Scene2D(dot)
scene = scene.bind({scene.camera.ref("view"): Bounds2D(Vec2(0, 0), Vec2(10, 10))})

motion = dot.animate.position.to(Vec2(9, 9), duration=1.5, easing=ease.out_cubic)
animation = Animation(scene, motion)

animation.save("dot.svg", width=400, height=400)
```

## Features

<div class="grid cards" markdown>

-   :material-animation-play: **Scenes and motion**

    Immutable 2D and 3D nodes, and motions that you compose with `then`, `with_`, `delay`, `repeat`, `yoyo`, `reverse` and `trim`.

    [:octicons-arrow-right-24: Scenes and motion](guides/scenes-motion.md)

-   :material-timer-outline: **Time and easing**

    Frames at exact times, easing families and cubic Bézier timing, keyframes and markers.

    [:octicons-arrow-right-24: Time and easing](guides/time-easing.md)

-   :material-shape-polygon-plus: **Morphing and transitions**

    Path, mesh and surface morphs with explicit correspondence, and scene transitions that match nodes by stable id.

    [:octicons-arrow-right-24: Morphing](guides/morphing.md)

-   :material-cube-outline: **3D scenes and cameras**

    Meshes, height-field surfaces, lights, and perspective or orthographic cameras with one shared projection.

    [:octicons-arrow-right-24: Camera geometry and projection](guides/projection.md)

-   :material-export: **Three outputs from one scene**

    Animated SVG, streamed GIF up to 1200 DPI, and self-contained interactive HTML, each checked against its capabilities before a file is written.

    [:octicons-arrow-right-24: Output formats](guides/outputs.md)

-   :material-format-font: **Typography**

    Text that arrives as a neutral asset, laid out by GlyphKit from caller-provided fonts, with permission-checked font subsets embedded.

    [:octicons-arrow-right-24: Typography](guides/typography.md)

-   :material-human-greeting-variant: **Accessibility and interaction**

    Roles, labels and reading order, a reduced-motion policy, and data-only interactions bound to node ids.

    [:octicons-arrow-right-24: Accessibility and interaction](guides/accessibility.md)

-   :material-puzzle-outline: **Examples and adapters**

    A chart from plain shapes, a plain Python object model animated through an adapter, and a lit 3D surface.

    [:octicons-arrow-right-24: Examples](guides/examples.md)

</div>

## Install

```bash
uv add --prerelease allow "kinetickit[studio]"
```

Requires Python 3.10 to 3.13. See [Installation](installation.md) for the optional extras.

## Examples

Every figure in this documentation comes with the script that writes it. Download them all in one file.

[Download all examples](../assets/kinetickit/kinetickit-examples.zip){ .md-button download="" }
