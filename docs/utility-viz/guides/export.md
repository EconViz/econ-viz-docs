---
seo_title: "Export"
---

# Export

<span id="sec-export"></span>

## Output formats

<!-- api: agora.utility_viz.guides_export_1 -->

Write the figure to `path`; the format follows the extension. `Figure`,
`DemandDiagram` and `EdgeworthBox` have the same method.

- PNG: raster, at the canvas `dpi` (default 300).
- PDF, SVG: vector output that stays sharp when printed or scaled.
- TeX: TikZ code (`.tex`) for inclusion in LaTeX documents; adjust it with
  the keyword arguments `tikz_scale` and `tikz_standalone`.

```python
# PNG at the canvas DPI and 300 by default
cvs.save("figure.png")
# PDF vector
cvs.save("figure.pdf")
# SVG vector
cvs.save("figure.svg")
# TikZ
cvs.save("figure.tex")
```

The `dpi` parameter of `Canvas` only affects raster output; lower it for
faster previews:

```python
# lower DPI for a faster preview
cvs = Canvas(x_max=20, y_max=15, dpi=150)
```

## Animated GIFs

Export a GIF with `Animator.save()`; [Animation](animation.md#sec-animation) has complete examples.

```python
from utility_viz.core.animation import Animator

Animator(draw_frame, frames=frames).save(
    "animation.gif", fps=12, dpi=120
)
```

## Interactive window

`cvs.show()` opens a live `matplotlib` window instead of saving. In
the CLI, omitting `--output` has the same effect ([Plotting](../getting-started/cli.md#sec-cli-plot)):

```bash
utility-viz plot --model cobb-douglas --px 2 --py 3 --income 30
```
