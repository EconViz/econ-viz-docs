---
seo_title: "Animation"
---

# Animation

<span id="sec-animation"></span>

`Animator` calls a drawing function over a sequence of parameter values and
exports the returned `Canvas` or `Figure` objects as a GIF. It needs the
`animation` extra ([Optional dependencies](../getting-started/installation.md#sec-extras)). Import it from
`utility_viz.core.animation`; it was `econ_viz.animation` in 1.x.

<!-- api: agora.utility_viz.guides_animation_1 -->

Call `draw(value)` for every value in `frames` and write the canvases as
the frames of a GIF.

- `save()` uses `Pillow`, so no `ffmpeg` dependency is required.
- Frames are composited onto white before export, which prevents
  frame-stacking artefacts.
- `fps`, `dpi` and `loop` set the frame rate, resolution and loop count.

```python
import numpy as np

from utility_viz import Canvas, levels, solve
from utility_viz.core.animation import Animator
from utility_viz.models import CobbDouglas

def draw(px: float) -> Canvas:
    model = CobbDouglas(alpha=0.5, beta=0.5)
    eq = solve(model, px=px, py=2.0, income=20.0)
    lvls = levels.around(eq.utility, n=5)

    return (
        Canvas(
            x_max=14, y_max=12,
            x_label="X_1", y_label="X_2",
            title="Price sweep"
        )
        .add_utility(model, levels=lvls)
        .add_budget(px=px, py=2.0, income=20.0, fill=True)
        .add_equilibrium(eq, show_ray=True, drop_dashes=True)
    )

Animator(draw, frames=np.linspace(1.0, 6.0, 45)).save(
    "price_sweep.gif",
    fps=12,
    dpi=120,
)
```

`examples/scripts/animation.py` provides four examples (Each example covers Cobb-Douglas, CES, perfect substitutes and perfect complements.):

- Parameter sweep: prices and income fixed, a utility-function parameter
  varies.
- Price sweep: utility function and $p_y$ fixed, $p_x$ varies and the
  budget line rotates, as in the example above.
- Income sweep: utility function and prices fixed, income varies and the
  budget line shifts.
- Budget-only sweep: the budget line alone, without the utility layers.

The four differ only in which values `draw()` holds fixed and which one it
varies. For the parameter sweep, let the `draw()` above take `alpha` and fix
the price at $p_x = 2$:

```python
def draw(alpha: float) -> Canvas:
    model = CobbDouglas(alpha=alpha, beta=1.0 - alpha)
    eq = solve(model, px=2.0, py=2.0, income=20.0)
    ...

Animator(draw, frames=np.linspace(0.1, 0.9, 45)).save("parameter_sweep.gif")
```

For the income sweep, `draw()` takes `income` and passes it to
`add_budget()` and `solve()`. For the budget line alone, leave out
`add_utility()` and `add_equilibrium()`.

[Parameter sweep $\alpha$ varies with $\beta = 1 - \alpha$](animation.md#fig-sweep-param) to [Income sweep](animation.md#fig-sweep-income) each show four frames.

```python
import numpy as np

from utility_viz import Canvas, Config, levels, solve
from utility_viz.core.animation import Animator
from utility_viz.models import CobbDouglas

Config.load("manual.toml").use()  # figure settings

def draw(alpha: float) -> Canvas:
    """One frame: the weight on x is alpha, the weight on y is 1 - alpha."""
    model = CobbDouglas(alpha=alpha, beta=1.0 - alpha)
    eq = solve(model, px=2.0, py=2.0, income=20.0)
    cvs = Canvas(x_max=14, y_max=12, x_label="$x_1$", y_label="$x_2$")
    cvs.add_utility(model, levels=levels.around(eq.utility, n=5))
    cvs.add_budget(2.0, 2.0, 20.0, fill=True)
    cvs.add_equilibrium(eq, show_ray=True)
    return cvs

Animator(draw, frames=np.linspace(0.1, 0.9, 45)).save("parameter_sweep.gif", fps=12, dpi=120)
```

<span id="fig-sweep-param"></span>

<figure class="ev-fig" markdown>

![Parameter sweep $\alpha$ varies with $\beta = 1 - \alpha$](../../assets/utility-viz/agora/animation/parameter_sweep.svg){ .ev-figure-lg }

<div class="ev-downloads"><a class="ev-download" href="../../assets/utility-viz/agora/animation/parameter_sweep.py" download aria-label="Download the source"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Download the source</span></a></div>

<figcaption markdown>Parameter sweep $\alpha$ varies with $\beta = 1 - \alpha$</figcaption>

</figure>

Each figure below shows four frames of its GIF, which has 45.

```python
import numpy as np

from utility_viz import Canvas, Config, levels, solve
from utility_viz.core.animation import Animator
from utility_viz.models import CobbDouglas

Config.load("manual.toml").use()  # figure settings

model = CobbDouglas(alpha=0.5, beta=0.5)
# same curves in every frame
fixed = levels.around(solve(model, px=2.0, py=2.0, income=20.0).utility, n=5)

def draw(px: float) -> Canvas:
    """One frame: the price of x is px."""
    eq = solve(model, px=px, py=2.0, income=20.0)
    cvs = Canvas(x_max=14, y_max=12, x_label="$x_1$", y_label="$x_2$")
    cvs.add_utility(model, levels=fixed)
    cvs.add_budget(px, 2.0, 20.0, fill=True)
    cvs.add_equilibrium(eq, show_ray=True)
    return cvs

Animator(draw, frames=np.linspace(1.0, 6.0, 45)).save("price_sweep.gif", fps=12, dpi=120)
```

<span id="fig-sweep-price"></span>

<figure class="ev-fig" markdown>

![Price sweep](../../assets/utility-viz/agora/animation/price_sweep.svg){ .ev-figure-lg }

<div class="ev-downloads"><a class="ev-download" href="../../assets/utility-viz/agora/animation/price_sweep.py" download aria-label="Download the source"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Download the source</span></a></div>

<figcaption markdown>Price sweep</figcaption>

</figure>

```python
import numpy as np

from utility_viz import Canvas, Config, levels, solve
from utility_viz.core.animation import Animator
from utility_viz.models import CobbDouglas

Config.load("manual.toml").use()  # figure settings

model = CobbDouglas(alpha=0.5, beta=0.5)
# same curves in every frame
fixed = levels.around(solve(model, px=2.0, py=2.0, income=20.0).utility, n=5)

def draw(income: float) -> Canvas:
    """One frame: income is `income`."""
    eq = solve(model, px=2.0, py=2.0, income=income)
    cvs = Canvas(x_max=14, y_max=12, x_label="$x_1$", y_label="$x_2$")
    cvs.add_utility(model, levels=fixed)
    cvs.add_budget(2.0, 2.0, income, fill=True)
    cvs.add_equilibrium(eq, show_ray=True)
    return cvs

Animator(draw, frames=np.linspace(8.0, 36.0, 45)).save("income_sweep.gif", fps=12, dpi=120)
```

<span id="fig-sweep-income"></span>

<figure class="ev-fig" markdown>

![Income sweep](../../assets/utility-viz/agora/animation/income_sweep.svg){ .ev-figure-lg }

<div class="ev-downloads"><a class="ev-download" href="../../assets/utility-viz/agora/animation/income_sweep.py" download aria-label="Download the source"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Download the source</span></a></div>

<figcaption markdown>Income sweep</figcaption>

</figure>

## Sweep gallery

The GIFs below are drawn by `scripts/animation_figures.py` in the docs repository, with the settings of `manual.toml`. They cover the same four sweeps: parameter, price, income and budget-only.

### Parameter sweeps

Vary utility-function parameters to see how the shape of the preference map changes.

<table class="gif-table">
  <tbody>
    <tr>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">Cobb-Douglas</span>
    <img src="../../../assets/animation/parameter_sweeps/cobb_douglas_parameter_sweep.gif" alt="Cobb-Douglas parameter sweep GIF">
    <figcaption>Vary \(\alpha\) while \(\beta = 1 - \alpha\)</figcaption>
  </figure>
      </td>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">CES</span>
    <img src="../../../assets/animation/parameter_sweeps/ces_parameter_sweep.gif" alt="CES parameter sweep GIF">
    <figcaption>Vary \(\rho\) to change curvature and substitutability</figcaption>
  </figure>
      </td>
    </tr>
    <tr>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">Perfect substitutes</span>
    <img src="../../../assets/animation/parameter_sweeps/perfect_substitutes_parameter_sweep.gif" alt="Perfect substitutes parameter sweep GIF">
    <figcaption>Vary \(a\) with \(b\) fixed</figcaption>
  </figure>
      </td>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">Leontief</span>
    <img src="../../../assets/animation/parameter_sweeps/leontief_parameter_sweep.gif" alt="Leontief parameter sweep GIF">
    <figcaption>Vary \(a\) with \(b\) fixed to move the kink path</figcaption>
  </figure>
      </td>
    </tr>
  </tbody>
</table>

### Price sweeps

Hold the utility function and background indifference-curve levels fixed, then vary one good's price to trace equilibrium as the budget line rotates.

<table class="gif-table">
  <tbody>
    <tr>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">Cobb-Douglas</span>
    <img src="../../../assets/animation/price_sweeps/cobb_douglas_price_sweep.gif" alt="Cobb-Douglas price sweep GIF">
    <figcaption>Price sweep with \(p_y\) fixed</figcaption>
  </figure>
      </td>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">CES</span>
    <img src="../../../assets/animation/price_sweeps/ces_price_sweep.gif" alt="CES price sweep GIF">
    <figcaption>Price sweep with a fixed utility surface</figcaption>
  </figure>
      </td>
    </tr>
    <tr>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">Perfect substitutes</span>
    <img src="../../../assets/animation/price_sweeps/perfect_substitutes_price_sweep.gif" alt="Perfect substitutes price sweep GIF">
    <figcaption>Under a rotating budget line</figcaption>
  </figure>
      </td>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">Leontief</span>
    <img src="../../../assets/animation/price_sweeps/leontief_price_sweep.gif" alt="Leontief price sweep GIF">
    <figcaption>Price sweep with fixed right-angle indifference curves</figcaption>
  </figure>
      </td>
    </tr>
    <tr>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">Budget only</span>
    <img src="../../../assets/animation/price_sweeps/budget_only_price_sweep.gif" alt="Budget-only price sweep GIF">
    <figcaption>Price sweep for isolating pure rotation of the constraint</figcaption>
  </figure>
      </td>
      <td class="gif-table__empty" aria-hidden="true"></td>
    </tr>
  </tbody>
</table>

### Income sweeps

Hold the utility function and prices fixed, then vary income to trace equilibrium as the budget line shifts in parallel.

<table class="gif-table">
  <tbody>
    <tr>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">Cobb-Douglas</span>
    <img src="../../../assets/animation/income_sweeps/cobb_douglas_income_sweep.gif" alt="Cobb-Douglas income sweep GIF">
    <figcaption>Income sweep with fixed prices</figcaption>
  </figure>
      </td>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">CES</span>
    <img src="../../../assets/animation/income_sweeps/ces_income_sweep.gif" alt="CES income sweep GIF">
    <figcaption>Income sweep with fixed prices and fixed utility function</figcaption>
  </figure>
      </td>
    </tr>
    <tr>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">Perfect substitutes</span>
    <img src="../../../assets/animation/income_sweeps/perfect_substitutes_income_sweep.gif" alt="Perfect substitutes income sweep GIF">
    <figcaption>Income sweep</figcaption>
  </figure>
      </td>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">Leontief</span>
    <img src="../../../assets/animation/income_sweeps/leontief_income_sweep.gif" alt="Leontief income sweep GIF">
    <figcaption>Income sweep with fixed prices</figcaption>
  </figure>
      </td>
    </tr>
    <tr>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">Budget only</span>
    <img src="../../../assets/animation/income_sweeps/budget_only_income_sweep.gif" alt="Budget-only income sweep GIF">
    <figcaption>Income sweep for isolating parallel shifts in the constraint</figcaption>
  </figure>
      </td>
      <td class="gif-table__empty" aria-hidden="true"></td>
    </tr>
  </tbody>
</table>
