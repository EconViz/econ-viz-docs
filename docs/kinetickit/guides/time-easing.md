---
seo_title: "Time, easing, and motion algebra"
---

# Time, easing, and motion algebra

<span id="sec-kinetic-time"></span>

## Normalised segment time

An animated property changes over a segment $[t_0,t_0+D]$. KineticKit first normalises time,

$$
u = \text{clamp}((t-t_0)/D, 0, 1),
$$

then evaluates an easing function $e(u)$, and finally asks the property's interpolator for the value at progress $e(u)$.

## Easing families

`ease.linear` is $e(u)=u$. For $n = 2, 3, 4, 5$ the names `quad`, `cubic`, `quart` and `quint` stand for the powers:

| Name | Formula |
| --- | --- |
| `in_*` | $u^n$ |
| `out_*` | $1-(1-u)^n$ |
| `in_out_*` | $\tfrac12 (2u)^n$ for $u < \tfrac12$, otherwise $1 - \tfrac12 (2(1-u))^n$ |

The sine family is `in_sine` $= 1-\cos(\pi u/2)$, `out_sine` $= \sin(\pi u/2)$ and `in_out_sine` $= \tfrac12 (1-\cos \pi u)$. The exponential family is `in_expo` $= (2^{10u}-1)/1023$, with `out_expo` and `in_out_expo` built from it the same way. Every function satisfies $e(0)=0$ and $e(1)=1$ exactly. The dictionary `ease.STANDARD` maps each name to its function.

<!-- api: kinetickit.guides_time_easing_1 -->

The easing namespace: the families above, `cubic_bezier(x1, y1, x2, y2)` for CSS-style timing curves, and `STANDARD`. Overshooting curves leave $[0,1]$ inside the segment, and the exact property values are still returned at the segment ends.

```python
from kinetickit import ease

print(ease.out_cubic(0.5))  # 0.875
spring = ease.cubic_bezier(0.34, 1.56, 0.64, 1)
print(round(spring(0.5), 4))  # 1.0874, past the end value
```

<span id="fig-kinetic-motion"></span>

<figure class="ev-fig" markdown>

![Six easing functions, each moving a point from one end of its track to the other in two seconds. The last curve overshoots.](../../assets/kinetickit/motion/easing.svg){ .ev-figure-lg }

<div class="ev-downloads"><a class="ev-download" href="../../assets/kinetickit/motion/easing.py" download aria-label="Download the source"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Download the source</span></a></div>

<figcaption markdown>Six easing functions, each moving a point from one end of its track to the other in two seconds. The last curve overshoots.</figcaption>

</figure>

## Cubic Bézier timing

A cubic Bézier timing curve with controls $(x_1,y_1)$ and $(x_2,y_2)$ is

$$
B(t) = (1-t)^3(0,0) + 3(1-t)^2t(x_1,y_1) + 3(1-t) t^2(x_2,y_2) + t^3(1,1).
$$

For a requested time $u$, the easing value is the $y$ coordinate whose $x$ coordinate equals $u$. The two $x$ controls must lie in $[0,1]$, so $x$ is monotone and the solution is unique; the $y$ controls are free, which is how the last track above overshoots.

## Composition

For `a.then(b, gap=g)`, the duration is $D_a+g+D_b$. For `a.with_(b, offset=o)` it is $\max(D_a,o+D_b)$. Repetition multiplies the duration, reversal samples child time $D-t$, and trimming maps a new interval back into the child interval. These operations build immutable motion trees before compilation.

```python
forward = dot.animate.position.to(Vec2(9, 9), duration=1.0)
motion = forward.then(forward.reverse(), gap=0.4)  # D + 0.4 + D
```

The figure above is built this way: six motions run together with `with_`, then the whole motion is followed by its own `reverse()`.

## Keyframes and markers

A `Keyframes` motion lists values at times for one property. Each `Keyframe` can carry the easing for the interval that follows it, and `hold=True` keeps the value until the next keyframe. `mark("name", at=0.0)` names a moment on any motion, and interactions can seek to it ([Accessibility and interaction](accessibility.md#sec-interaction)).

```python
from kinetickit import Keyframe, Keyframes, Point2D, Vec2, ease

p = Point2D(id="p", position=Vec2(0, 0))
fade = Keyframes(
    p.ref("opacity"),
    (Keyframe(0.0, 0.0), Keyframe(1.0, 1.0, easing=ease.out_quad), Keyframe(2.0, 0.2)),
)
print(fade.duration)  # 2.0
```
