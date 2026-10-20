---
seo_title: "Scenes and motion"
---

# Scenes and motion

<span id="sec-scenes-motion"></span>

## 2D and 3D scenes

<!-- api: agora.kinetickit.guides_scenes_motion_1 -->

A stroked segment between two points. Its endpoints, colour, width, dash pattern, and drawing progress can be animated.

<!-- api: agora.kinetickit.guides_scenes_motion_2 -->

An open or closed stroked `Path2D`. It preserves line and Bézier commands and supports path morphing.

<!-- api: agora.kinetickit.guides_scenes_motion_3 -->

A filled path, optionally with a stroke. Use it for areas, closed outlines, and compound shapes.

<!-- api: agora.kinetickit.guides_scenes_motion_4 -->

A node that applies shared transforms, opacity, and clipping to an ordered collection of child nodes.

<!-- api: agora.kinetickit.guides_scenes_motion_5 -->

A positioned `TextAsset` produced by a typography adapter, with animatable scale, transform, and opacity.

<!-- api: agora.kinetickit.guides_scenes_motion_6 -->

Defines the visible 2D world rectangle and its mapping to the output viewport.

<!-- api: agora.kinetickit.guides_scenes_motion_7 -->

An immutable 3D scene containing geometry, lights, groups, and one camera.

<!-- api: agora.kinetickit.guides_scenes_motion_8 -->

A point marker in three-dimensional space with animatable position, size, colour, and opacity.

<!-- api: agora.kinetickit.guides_scenes_motion_9 -->

A single 3D segment projected by the active camera.

<!-- api: agora.kinetickit.guides_scenes_motion_10 -->

An ordered chain of 3D points rendered as connected segments.

<!-- api: agora.kinetickit.guides_scenes_motion_11 -->

Indexed vertices and faces with validated topology, optional per-face colour, and material settings.

<!-- api: agora.kinetickit.guides_scenes_motion_12 -->

A regular height-field surface built from an $x,y$ grid and height values.

<!-- api: agora.kinetickit.guides_scenes_motion_13 -->

An ordered group of 3D nodes sharing a transform and opacity.

<!-- api: agora.kinetickit.guides_scenes_motion_14 -->

A perspective or orthographic camera with position, target, clipping planes, and projection settings.

## Composing time

<!-- api: agora.kinetickit.guides_scenes_motion_15 -->

An immutable description of change over time. Motions can be sequenced, overlapped, delayed, repeated, reversed, or trimmed.

<!-- api: agora.kinetickit.guides_scenes_motion_16 -->

The compiled, random-access form of a motion tree. It evaluates property values at any valid time.

<!-- api: agora.kinetickit.guides_scenes_motion_17 -->

One value at one time, optionally carrying the easing rule for the following interval.

<!-- api: agora.kinetickit.guides_scenes_motion_18 -->

A validated sequence of keyframes for one property, including endpoint and ordering checks.

```python
motion = (
    a.animate.position.to(Vec2(5, 5), duration=1.0)
    .then(b.animate.opacity.to(1.0, duration=0.5))
    .with_(c.animate.size.to(9, duration=0.5), offset=1.0)
    .mark("settled")
)
```

<!-- api: agora.kinetickit.guides_scenes_motion_19 -->

Builds a motion between two scenes by matching nodes with stable ids and interpolating compatible properties.

<!-- api: agora.kinetickit.guides_scenes_motion_20 -->

Controls how unmatched or structurally incompatible nodes enter, leave, cross-fade, or fail.

Paths, meshes, and surfaces have dedicated morphing tools. Use explicit correspondence overrides when automatic normalization cannot infer the intended topology.

<span id="fig-kinetic-surface"></span>

<figure class="ev-fig" markdown>

![A 3D surface projected and depth-sorted by KineticKit's vector renderer](../../assets/kinetickit/agora/projection/surface.svg){ .ev-figure-lg }

<figcaption markdown>A 3D surface projected and depth-sorted by KineticKit's vector renderer</figcaption>

</figure>
