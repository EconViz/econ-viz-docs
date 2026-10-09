---
seo_title: "Change history"
---

<span id="sec-changelog"></span>

# Change history

Release history of `bezierkit`. Documentation-only changes are not
listed; each entry is tagged where the feature it describes is documented,
following l3doc convention, so the page number is the real page.

## 1.0.0

- First stable release; the public API follows semantic versioning [Introduction](../guides/introduction.md)
- `bezierkit` — Continuous integration tests Python 3.10, 3.11, 3.12 and 3.13 [Installation](../installation.md)
- `PiecewiseBezier.segment` — Returns the requested interval when `t0` falls inside a segment; previously the end point was wrong, because the path was split at `t0` and the suffix re-parameterized [Cubic segments and paths](../guides/paths.md)

## 0.5.0rc1

- First release on PyPI: degree-generic Bézier curves, cubic segments and paths, constructions, Hermite interpolation, fitting, level-set tracing, sampling, exporters and a command-line interface [Introduction](../guides/introduction.md)

