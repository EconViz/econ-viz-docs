---
seo_title: "Layout geometry"
---

# Layout geometry

<span id="sec-geometry"></span>

Label placement runs after everything else is drawn and uses display
coordinates: pixels, with $y$ increasing upward. The package
`mosaickit.layout` contains this geometry and imports nothing from the
renderers, so it can be tested and reused independently. The functions in
this chapter are in `mosaickit.layout.geometry`; `Rect` and `polylabel` are
also exported from `mosaickit.layout`. A point is a pair `(x, y)`, a segment
is a pair of points, and a polygon is a sequence of points whose last point
joins the first.

## Rectangles

<!-- api: agora.mosaickit.guides_geometry_1 -->

The closed axis-aligned rectangle $[x_0, x_1] \times [y_0, y_1]$.
`Rect.centered(center, width, height)` builds one around a point. It has
`width`, `height`, `center`, `inflate(pad)`, `corners()` (counter-clockwise
from $(x_0, y_0)$), `edges()`, `contains(point)` (edges included),
`within(other)`, `intersects(other)` (touching counts) and
`nearest_point(point)`.

<span id="lem-nearest"></span>

!!! abstract "Lemma · Nearest point of a rectangle"

    For a rectangle $R$ and a point $p$, `nearest_point` returns

    $$
    q = (\min(\max(p_x, x_0), x_1), \min(\max(p_y, y_0), y_1)).
    $$

    This is the unique point of $R$ closest to $p$.

Callout leaders end at this point, so a leader is as short as the label's
position allows.

## Orientation and segments

<span id="def-orient"></span>

!!! abstract "Definition · Orientation"

    For points $a, b, c$ in the plane,

    $$
    \text{orient}(a, b, c) = (b_x - a_x)(c_y - a_y) - (b_y - a_y)(c_x - a_x),
    $$

    the cross product of $b - a$ and $c - a$.

<span id="lem-orient"></span>

!!! abstract "Lemma · Orientation test"

    $\text{orient}(a, b, c)$ is positive when $c$ lies to the left of the directed
    line from $a$ to $b$ (the turn $a \to b \to c$ is counter-clockwise),
    negative when it lies to the right, and zero when $a$, $b$, $c$ are
    collinear. It is invariant under cyclic permutation and changes sign when
    two arguments are swapped.

<!-- api: agora.mosaickit.guides_geometry_2 -->

Whether the closed segments $[a, b]$ and $[c, d]$ share a point. With
$d_1 = \text{orient}(c, d, a)$, $d_2 = \text{orient}(c, d, b)$,
$d_3 = \text{orient}(a, b, c)$, $d_4 = \text{orient}(a, b, d)$, it answers yes when
$d_1 d_2 < 0$ and $d_3 d_4 < 0$, or when some $d_i$ is zero and its point
lies in the bounding box of the other segment [Cormen (2009)](../project/references.md#cormen2009).

<span id="thm-segments"></span>

!!! abstract "Theorem · Segment intersection"

    In exact arithmetic, `segments_intersect(a, b, c, d)` is true if and only
    if $[a, b] \cap [c, d] \ne \emptyset$.

<!-- api: agora.mosaickit.guides_geometry_3 -->

Whether the segment touches the rectangle: an endpoint lies in it, or the
segment meets one of its four edges.

<span id="lem-rect-segment"></span>

!!! abstract "Lemma · Segments and rectangles"

    `rect_hits_segment(R, a, b)` is true if and only if $[a, b] \cap R \ne \emptyset$.

## Polygons

<span id="def-polygon"></span>

!!! abstract "Definition · Simple polygon"

    A polygon $P = (p_0, \ldots, p_{m-1})$, $m \ge 3$, is _simple_ when its
    edges $[p_i, p_{i+1}]$ (indices mod $m$) meet only at shared endpoints of
    consecutive edges and its vertices are not all collinear. Its boundary
    $\partial P$ is the union of the edges; by the Jordan curve theorem the
    complement of $\partial P$ has one bounded component, the _interior_
    $\text{int} P$, and one unbounded one, the _exterior_. We write
    $\overline{P} = \text{int} P \cup \partial P$.

<!-- api: agora.mosaickit.guides_geometry_4 -->

The edges, last vertex to first included, and the Euclidean distance
from a point to the nearest edge. Each edge distance projects the point
onto the edge's line and clamps the parameter to $[0, 1]$.

<span id="lem-segment-distance"></span>

!!! abstract "Lemma · Distance to a segment"

    For $a \ne b$, let

    $$
    t^* = \text{clamp}((p - a) \cdot (b - a) / |b - a|^2, 0, 1).
    $$

    Then $a + t^* (b - a)$ is the point of $[a, b]$ nearest to $p$.

<!-- api: agora.mosaickit.guides_geometry_5 -->

The even–odd rule: follow the horizontal ray from the point to the right
and count the edges it crosses. An edge counts when exactly one of its
endpoints lies strictly above the ray's line and the crossing is right of
the point [Haines (1994)](../project/references.md#haines1994).

<span id="prop-even-odd"></span>

!!! abstract "Proposition · Even-odd rule"

    Let $P$ be simple and $p \notin \partial P$. Then
    `point_in_polygon(p, P)` is true if and only if $p \in \text{int} P$.

<!-- api: agora.mosaickit.guides_geometry_6 -->

Inside: all four corners pass the even-odd test and no edge of the polygon
touches the rectangle. Overlaps: some corner passes, or some edge touches
the rectangle (which also catches a polygon lying wholly inside it).

<span id="thm-rect-inside"></span>

!!! abstract "Theorem · Rectangles in polygons"

    Let $P$ be simple and $R$ a rectangle. Then `rect_inside_polygon(R, P)` is
    true if and only if $R \subset \text{int} P$.

<span id="cor-rect-overlap"></span>

!!! abstract "Corollary · Rectangles overlapping polygons"

    Let $P$ be simple and $R$ a rectangle. Then `rect_overlaps_polygon(R, P)`
    is true if and only if $R \cap \overline{P} \ne \emptyset$.

<!-- api: agora.mosaickit.guides_geometry_7 -->

The largest $t \ge 0$ at which the ray $o + t r$ meets an edge that is not
parallel to it, or $0$ if there is none. Callouts use it to start their
search where the ray leaves the region.

<span id="prop-ray-exit"></span>

!!! abstract "Proposition · Leaving a polygon for good"

    Let $P$ be simple, $r \ne 0$ and $T =$ `ray_exit(o, r, P)`. Then
    $o + t r \notin \overline{P}$ for every $t > T$.

## The visual centre of a region

The centroid of a region can lie outside it ([Pole, largest disc and centroid.](geometry.md#fig-polylabel)). A label belongs
at the deepest interior point, which is farthest from the boundary.

<span id="def-pole"></span>

!!! abstract "Definition · Signed distance and pole"

    For a simple polygon $P$ the _signed distance_ is
    $f(p) = d(p, \partial P)$ for $p \in \overline{P}$ and $f(p) = -d(p, \partial P)$
    otherwise. A _pole of inaccessibility_ of $P$ is a point where $f$ attains
    its maximum $f^*$, the radius of the largest disc inside $P$.

<span id="lem-lipschitz"></span>

!!! abstract "Lemma · Signed distance is 1-Lipschitz"

    For all points $p, q$, $|f(p) - f(q)| \le |p - q|$.

<!-- api: agora.mosaickit.guides_geometry_8 -->

A best-first search over square cells [Agafonkin (2016)](../project/references.md#agafonkin2016). The
bounding box is covered with squares as wide as its shorter side. Each
cell with centre $c$ and half-size $h$ is given the bound
$f(c) + h \sqrt{2}$ and kept in a priority queue, largest bound first. The
best centre seen so far is remembered, starting with the centre of the
bounding box; a popped cell whose bound exceeds the best value by more
than `precision` is split into four, the others are dropped. A polygon
with a zero-width or zero-height bounding box returns its first vertex.

<span id="thm-polylabel"></span>

!!! abstract "Theorem · Pole of inaccessibility"

    Let $P$ be simple, with a bounding box of positive width and height, and
    let $\epsilon > 0$ be the precision. Then `polylabel` terminates and
    returns a point $q$ with $f(q) \ge f^* - \epsilon$. In particular $q$ lies
    in $\text{int} P$ whenever $f^* > \epsilon$.

<span id="fig-polylabel"></span>

![Pole, largest disc and centroid.](../../assets/mosaickit/agora/geometry/polylabel.svg){ .ev-figure-sm }

For a triangle the pole is the incentre. Placement calls `polylabel` with
the default precision of one pixel, finer than any text-placement increment.

## Brace outlines

<!-- api: agora.mosaickit.guides_geometry_9 -->

A curly brace over `start`..`end`, as a `Brace(points, tip)`. Its ends
lie on the line `base` (a constant across coordinate), and the tip sits at
the middle of the span, `depth` past `base` on the side `direction`
($\pm 1$). On axis `"y"` points are (across, along); on `"x"` they
are (along, across). Each quarter arc is sampled with `samples` segments.
An empty span, a non-positive depth or another direction or axis raise
`ValueError`.

The outline is built in a local frame, $u$ across and $v$ along, from four
quarter circles of radius $r = \min(\text{depth}/2, (\text{end} - \text{start})/4)$ joined
by two straight pieces, and then stretched across by $\text{depth} / 2r$,
so a short span gets small arcs but the tip still reaches the full depth
([Brace outlines; the right span is under $2 \delta$.](geometry.md#fig-brace)).

<span id="prop-brace"></span>

!!! abstract "Proposition · Shape of a brace"

    Let $\ell < h$ be the ends of the span, $m = (\ell + h) / 2$ its middle
    and $\delta$ the depth. In the local frame, before sampling, the outline is
    a curve from $(0, \ell)$ to $(0, h)$ through the tip $(\delta, m)$ that
    (i) stays in the strip $0 \le u \le \delta$, (ii) is symmetric under
    $v |\to \ell + h - v$, and (iii) has a continuous tangent everywhere except
    at the tip, where it turns back on itself (a cusp).

<span id="fig-brace"></span>

![Brace outlines; the right span is under $2 \delta$.](../../assets/mosaickit/agora/geometry/brace.svg){ .ev-figure-sm }
