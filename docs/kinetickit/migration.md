---
seo_title: "Migrating animation code"
---

# Migrating animation code

<span id="sec-migration"></span>

KineticKit is a new, independent engine. It does not import MosaicKit or any `*-viz` package, and it ships no compatibility layer for them. To migrate, describe your objects as KineticKit nodes through a small adapter. The removed MosaicKit and utility-viz animation APIs are not re-exported.

## From a parameter sweep

MosaicKit's `Animation.sweep(canvas, values)` yields immutable scene frames. Depict each layer as KineticKit nodes keyed by the layer id, then let KineticKit interpolate between frames.

1. Give every source layer a stable id.
2. Write a depiction function that turns one layer into nodes.
3. Turn adjacent frames into transitions with `kinetickit.adapters.transition` and join their motions with `then()`.
4. Export through `Animation.save()`.

```python
from kinetickit import Animation
from kinetickit.adapters import transition


def depict(layer):  # use public MosaicKit fields only
    ...  # PathLayer -> PathNode2D(id=layer.id, ...), and so on


frames = list(sweep.frames())
steps = [transition(a.layers, b.layers, depict, duration=1.0) for a, b in zip(frames, frames[1:])]
motion = steps[0].motion
for step in steps[1:]:
    motion = motion.then(step.motion)
animation = Animation(steps[0].scene, motion)
```

<!-- api: kinetickit.examples_transition -->

Matches the nodes of two states by id and returns the scene and the motion that carries one to the other.

Layers must keep their ids from frame to frame. Unmatched ids fade in or out, and a structural change cross-fades and reports a diagnostic in `Transition.diagnostics`. The adapter belongs in the consuming package, where the domain objects are understood.

## From a factory-style animator

Replace the factory with a depiction function and build the animation directly.

1. Translate each domain object into nodes with `adapt(objects, depict)`.
2. Express change as `node.animate.<property>.to(...)` or `SceneTransition.between()`.
3. Export with `animation.save(path)`. The exporter owns the file path, the frame rate, the DPI and the fallbacks.

## Fonts

Replace renderer-specific font paths with caller-owned `FontSource` values and a `FontLibrary`, and convert layouts through `GlyphKitTypography` ([Typography](guides/typography.md#sec-typography)). Do not ask the scene model or an optional renderer to discover fonts.

Existing `Text2D`, `TextAsset`, `GlyphShape`, `FontResource` and typography-protocol consumers keep their contracts.
