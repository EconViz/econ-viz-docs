---
seo_title: "Advanced models"
---

# Advanced models

<span id="sec-advanced"></span>

Advanced models extend the built-in families with user-defined functions
or more than two goods.

### Custom utility

<!-- api: agora.utility_viz.models_advanced_1 -->

Wrap any vectorised Python callable as an `utility-viz` model. The
callable must accept two `NumPy` arrays and return an array of the
same shape. The example below uses

$$
u(x, y) = ln x + ln y.
$$

```python
import numpy as np

from utility_viz import Canvas, Config, levels, solve
from utility_viz.models import CustomUtility

Config.load("manual.toml").use()  # figure settings

# any array function works
model = CustomUtility(func=lambda x, y: np.log(x) + np.log(y), name="log+log")
eq = solve(model, px=2.0, py=3.0, income=30.0)

cvs = Canvas(x_max=20, y_max=15, x_label="$x$", y_label="$y$")
cvs.add_utility(model, levels=levels.around(eq.utility, n=5))
cvs.add_budget(2.0, 3.0, 30.0)
cvs.add_equilibrium(eq)
cvs.save("custom.png")
```

<figure class="ev-fig" markdown>

![A custom model $ln x + ln y$](../../assets/utility-viz/agora/models/custom.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../assets/utility-viz/agora/models/custom.py" download aria-label="Download the source"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Download the source</span></a></div>

<figcaption markdown>A custom model $ln x + ln y$</figcaption>

</figure>

### Many-good Cobb-Douglas

<!-- api: agora.utility_viz.models_advanced_2 -->

Cobb-Douglas preferences over $N$ goods:

$$
u(x_1, ..., x_N) = product_{i=1}^N x_i^{\alpha_i}.
$$

`freeze()` fixes every good except $x$ and $y$ and returns a
`CustomUtility` that can be drawn on a two-dimensional canvas.

```python
from utility_viz import Canvas, Config, levels, solve
from utility_viz.models import MultiGoodCD

Config.load("manual.toml").use()  # figure settings

# three goods with z held at 10
model = MultiGoodCD({"x": 0.3, "y": 0.3, "z": 0.4})
two_good_model = model.freeze(z=10.0)
eq = solve(two_good_model, px=2.0, py=3.0, income=30.0)

cvs = Canvas(x_max=20, y_max=15, x_label="$x$", y_label="$y$")
cvs.add_utility(two_good_model, levels=levels.around(eq.utility, n=5))
cvs.add_budget(2.0, 3.0, 30.0, fill=True)
cvs.add_equilibrium(eq)
cvs.save("multigood.png")
```

<figure class="ev-fig" markdown>

![Three-good Cobb-Douglas](../../assets/utility-viz/agora/models/multigood.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../assets/utility-viz/agora/models/multigood.py" download aria-label="Download the source"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Download the source</span></a></div>

<figcaption markdown>Three-good Cobb-Douglas</figcaption>

</figure>

### Backend-neutral scenes

<span id="sec-scenes"></span>

`utility_viz.core.scenes` builds the same economic components as `Canvas`,
but as immutable `mosaickit` layers instead of drawing on
`matplotlib` axes. Every layer has a stable id (`budget`,
`budget.fill`, `equilibrium.drop`, `ic.2`, ...) and a dotted theme role
(`utility.budget`, `utility.indifference.secondary`, ...), so the scene can
be inspected, edited and rendered by any `mosaickit` backend. It is an
advanced, additive API: `Canvas` and the other diagrams are unchanged.

<!-- api: agora.utility_viz.models_advanced_3 -->

Return a tuple of layers for the budget line $p_x x + p_y y = I$, the
equilibrium bundle, and the indifference curves of a model over
$[0, x_{\max}] \times [0, y_{\max}]$. Styling comes from the theme roles; sparse
`Stroke`, `Marker` and `Fill` overrides are accepted.
`indifference_layers` returns `(layers, levels)` and traces the curves as
Bézier paths with `bezierkit`, so it also handles non-monotone and
kinked utilities.

<!-- api: agora.utility_viz.models_advanced_4 -->

`UTILITY_THEME` is a `mosaickit` theme with the `utility.*` roles,
matching the default theme's colours. `canvas_to_tikz(canvas)` exports a
scene as TikZ with native `.. controls ..` curves.

```python
from mosaickit import Canvas, CanvasSpec, quadrant_axes

from utility_viz.core.scenes import (
    UTILITY_THEME,
    budget_layers,
    canvas_to_tikz,
    equilibrium_layers,
    indifference_layers,
)
from utility_viz.models import CobbDouglas, solve

model = CobbDouglas(alpha=0.5, beta=0.5)
eq = solve(model, px=2.0, py=3.0, income=30.0)
u = eq.utility
ic, _ = indifference_layers(model, [0.6 * u, u, 1.4 * u], 18, 12)

spec = CanvasSpec(x_range=(0, 18), y_range=(0, 12))
canvas = (
    Canvas(spec, theme=UTILITY_THEME)
    .extend(quadrant_axes(18, 12))
    .extend(ic)
    .extend(budget_layers(2.0, 3.0, 30.0, fill=True))
    .extend(equilibrium_layers(eq))
)
canvas.save("scene.png")
tex = canvas_to_tikz(canvas)
```

The TikZ exporter handles path, fill, marker and text layers. The traced
utility must be finite on the plotted region.
