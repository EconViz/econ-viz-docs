---
seo_title: "Frame sampling and encoding"
---

# Frame sampling and encoding

<span id="sec-kinetic-sampling"></span>

## Fixed-rate schedules

Offline export uses random-access sampling. For duration $D$ and integer frame rate $f$, `FixedFPS` chooses

$$
N=\max(2, \left\lfloor D f+1/2 \right\rfloor)
$$

and includes both endpoints at

$$
t_i = D i/(N-1), \quad i=0,...,N-1.
$$

The final timestamp is assigned exactly $D$ to avoid accumulated floating-point drift.

<!-- api: kinetickit.guides_sampling_encoding_1 -->

Produces evenly spaced, endpoint-inclusive sample times for a requested integer frame rate.

<!-- api: kinetickit.guides_sampling_encoding_2 -->

Validates and stores explicit non-decreasing sample times within the animation duration.

<!-- api: kinetickit.guides_sampling_encoding_3 -->

One sampled scene paired with its timestamp, duration, and frame index.

## GIF centiseconds

GIF stores delays in hundredths of a second. At rate $f$, KineticKit distributes integer centiseconds by rounded cumulative boundaries:

$$
d_i = round((i+1) 100/f)-round(i 100/f).
$$

This alternates neighbouring delays when $100/f$ is not integral and keeps total drift bounded, unlike independently rounding every frame.

## Explicit timestamps

For arbitrary timestamps, delay boundaries are midpoints between adjacent samples, clipped to the animation interval and quantised cumulatively. Minimum-delay rules are checked before bytes are written.

## Streaming and determinism

The GIF writer quantises and writes one frame at a time, so memory does not grow with duration. SVG stores analytic motion, while HTML stores the scene, timeline, controls, and accessibility metadata. Every exporter returns a manifest describing the format, dimensions, duration, frame count, fallbacks, and generated assets.

!!! abstract "Proposition · Endpoint agreement"

    All endpoint-inclusive schedulers render the same initial and final scene snapshots as direct calls to `Animation.sample(0)` and `Animation.sample(D)`.
