---
seo_title: "Export Diagrams to PNG, PDF, SVG, and GIF"
description: "Save utility-viz economics diagrams as PNG, PDF, or SVG for papers and slides, export animated GIFs, or open an interactive matplotlib window."
---

# Export

## Raster formats

Call `cvs.save()` with a `.png`, `.pdf`, or `.svg` extension:

```python
# PNG, canvas DPI (default 300)
cvs.save("figure.png")
# PDF (vector)
cvs.save("figure.pdf")
# SVG (vector)
cvs.save("figure.svg")
```

The `dpi` parameter on `Canvas` controls raster resolution:

```python
# lower DPI, faster preview
cvs = Canvas(x_max=20, y_max=15, dpi=150)
```

DPI is clamped to the range 1–1200.

## Animated GIF export

For multi-frame output, use `Animator` instead of `Canvas.save()`:

```python
from utility_viz.animation import Animator

Animator(draw_frame, frames=frames).save(
    "animation.gif", fps=12, dpi=120
)
```

See the [Animation](animation.md) page for parameter, price, income, and budget-only sweep examples.

## Interactive window

Call `cvs.show()` to open a live matplotlib window instead of saving:

```python
cvs.show()
```

In the CLI, omit `--output` to get the same behaviour:

```bash
utility-viz plot --model cobb-douglas --px 2 --py 3 --income 30
```
