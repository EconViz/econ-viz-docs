---
seo_title: "KineticKit: Deterministic 2D and 3D Animation for Python"
description: "KineticKit builds deterministic 2D and 3D animation from immutable scenes and motions, then exports animated SVG, streamed GIF, or interactive HTML."
---

<h1 class="ev-visually-hidden">KineticKit: deterministic 2D and 3D animation for Python</h1>

<p align="center">
  <img src="../assets/kinetickit/banner.svg" alt="kinetickit" style="max-width: 480px; width: 100%; margin: 2rem 0 1rem;">
</p>

KineticKit is a domain-neutral 2D and 3D animation engine. One immutable scene and motion can produce animated SVG, streamed GIF, or self-contained interactive HTML.

```bash
uv add --prerelease allow "kinetickit[studio]"
```

```python
from kinetickit import (
    Animation,
    Bounds2D,
    Point2D,
    Scene2D,
    Vec2,
)

dot = Point2D(id="dot", position=Vec2(1, 1), size=8)
scene = Scene2D(dot).bind(
    {"camera.view": Bounds2D(Vec2(0, 0), Vec2(10, 10))}
)
motion = dot.animate.position.to(Vec2(9, 9), duration=1.5)
Animation(scene, motion).save("dot.svg", width=400, height=400)
```

## What KineticKit owns

<div class="grid cards" markdown>

-   :material-animation-play: **Scenes and motion**

    Immutable 2D and 3D nodes, composable motions, keyframes, path and mesh morphing, and stable-id scene transitions.

    [:octicons-arrow-right-24: Scenes and motion](guides/scenes-motion.md)

-   :material-export: **Three output paths**

    Native animated SVG, bounded-memory GIF rendering up to 1200 DPI, and interactive HTML with explicit capability checks.

    [:octicons-arrow-right-24: Output formats](guides/outputs.md)

-   :material-format-font: **Typography and accessibility**

    GlyphKit-backed text assets, embedded font subsets, object semantics, reduced-motion policy, and portable interactions.

    [:octicons-arrow-right-24: Typography and accessibility](guides/typography-accessibility.md)

</div>

KineticKit contains no economics or chart semantics. A consuming package translates its own objects into points, lines, paths, shapes, text assets, meshes, and surfaces.

<!-- agora-navigation -->

## Documentation

- [Introduction](guides/introduction.md)
- [Installation](installation.md)
- [Quick start](quickstart.md)
- [Scenes and motion](guides/scenes-motion.md)
- [Output formats](guides/outputs.md)
- [Typography and accessibility](guides/typography-accessibility.md)
- [Migrating animation code](migration.md)
- [Time, easing, and motion algebra](guides/time-easing.md)
- [Interpolation and transforms](guides/interpolation-transforms.md)
- [Camera geometry and projection](guides/projection.md)
- [Path, mesh, and surface morphing](guides/morphing.md)
- [Frame sampling and encoding](guides/sampling-encoding.md)
- [Change history](project/changelog.md)

<!-- /agora-navigation -->
