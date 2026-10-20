---
seo_title: "Core models"
---

# Core models

<span id="sec-models"></span>

The core models cover smooth, kinked, linear, income-dependent, and
reference-point preferences. They all live in `utility_viz.models`. This chapter
gives each model's function, parameters, distinct behaviour, and figure.

## Smooth preferences

These models produce smooth indifference curves and normally have an
interior optimum when prices and income are positive.

### Cobb-Douglas

<!-- api: agora.utility_viz.models_index_1 -->

The standard model for smooth, strictly convex preferences
[Cobb (1928)](../project/references.md#cobb1928):

$$
u(x, y) = x^\alpha y^\beta.
$$

The exponents control the relative weight placed on each good. The
indifference curves approach both axes without touching them.

### CES

<!-- api: agora.utility_viz.models_index_2 -->

Constant elasticity of substitution [Arrow (1961)](../project/references.md#arrow1961): the ease of substitution varies
while preferences stay smooth,

$$
u(x, y) = (\alpha x^\rho + \beta y^\rho)^{1 / \rho}.
$$

The elasticity of substitution is $\sigma = 1 / (1 - \rho)$. As $\rho$
changes, CES approaches Cobb-Douglas ($\rho \to 0$), Leontief
($\rho \to -\infty$) or perfect substitutes ($\rho \to 1$).

```python
from utility_viz import Canvas, Config, levels, solve
from utility_viz.models import CES

# figure settings
Config.load("manual.toml").use()

model = CES(alpha=0.5, beta=0.5, rho=-0.5)
eq = solve(model, px=2.0, py=3.0, income=30.0)

cvs = Canvas(x_max=20, y_max=15, x_label="$x$", y_label="$y$")
cvs.add_utility(model, levels=levels.around(eq.utility, n=5))
cvs.add_budget(2.0, 3.0, 30.0)
cvs.add_equilibrium(eq)
cvs.save("ces.png")
```

<figure class="ev-fig" markdown>

![CES with $\rho = -0.5$](../../assets/utility-viz/agora/models/ces.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../assets/utility-viz/agora/models/ces.py" download aria-label="Download the source"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Download the source</span></a></div>

<figcaption markdown>CES with $\rho = -0.5$</figcaption>

</figure>

### Translog

<!-- api: agora.utility_viz.models_index_3 -->

A flexible log-quadratic model for smooth preferences
[Christensen (1975)](../project/references.md#christensen1975):

$$
\begin{aligned}\ln u(x, y) = & \alpha_0 + \alpha_x \ln x + \alpha_y \ln y \\ & + 1/2 \beta_{x x} (\ln x)^2 + 1/2 \beta_{y y} (\ln y)^2 + \beta_{x y} \ln x \ln y.\end{aligned}
$$

The quadratic and interaction terms let the curvature vary across the
consumption space. With all $\beta$ coefficients zero it reduces to a
Cobb-Douglas-style log-linear form.

```python
from utility_viz import Canvas, Config, levels, solve
from utility_viz.models import Translog

# figure settings
Config.load("manual.toml").use()

model = Translog(alpha_x=0.6, alpha_y=0.4, beta_xy=0.12)
eq = solve(model, px=2.0, py=3.0, income=30.0)

cvs = Canvas(x_max=18, y_max=12, x_label="$x$", y_label="$y$")
cvs.add_utility(model, levels=levels.around(eq.utility, n=4))
cvs.add_budget(2.0, 3.0, 30.0)
cvs.add_equilibrium(eq)
cvs.save("translog.png")
```

<figure class="ev-fig" markdown>

![Translog with $\beta_{x y} = 0.12$](../../assets/utility-viz/agora/models/translog.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../assets/utility-viz/agora/models/translog.py" download aria-label="Download the source"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Download the source</span></a></div>

<figcaption markdown>Translog with $\beta_{x y} = 0.12$</figcaption>

</figure>

## Kinks and corners

These models show how non-smooth or linear preferences move the optimum
to a kink or a corner.

### Perfect complements

<!-- api: agora.utility_viz.models_index_4 -->

Goods consumed in fixed proportions:

$$
u(x, y) = \min(a x, b y).
$$

The indifference curves are L-shaped, and the optimum lies at the kink
where the two weighted quantities are equal.

The corners are drawn as exact right angles, in image and TikZ
output alike; this also holds for piecewise `min`/`max` functions built
with `CustomUtility`.

```python
from utility_viz import Canvas, Config, levels, solve
from utility_viz.models import Leontief

# figure settings
Config.load("manual.toml").use()

model = Leontief(a=1.0, b=1.0)
eq = solve(model, px=2.0, py=3.0, income=30.0)

cvs = Canvas(x_max=20, y_max=15, x_label="$x$", y_label="$y$")
cvs.add_utility(
    model,
    levels=levels.around(eq.utility, n=5),
    show_rays=True,
    # ray and marker at each kink
    show_kinks=True,
)
cvs.add_budget(2.0, 3.0, 30.0)
cvs.add_equilibrium(eq)
cvs.save("leontief.png")
```

<figure class="ev-fig" markdown>

![Leontief with kink ray](../../assets/utility-viz/agora/models/leontief.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../assets/utility-viz/agora/models/leontief.py" download aria-label="Download the source"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Download the source</span></a></div>

<figcaption markdown>Leontief with kink ray</figcaption>

</figure>

### Perfect substitutes

<!-- api: agora.utility_viz.models_index_5 -->

A constant rate of trade-off between the goods:

$$
u(x, y) = a x + b y.
$$

The indifference curves are straight lines. The consumer normally buys
only the good with the greater marginal utility per dollar, a corner
solution.

```python
from utility_viz import Canvas, Config, levels, solve
from utility_viz.models import PerfectSubstitutes

# figure settings
Config.load("manual.toml").use()

model = PerfectSubstitutes(a=1.0, b=2.0)
eq = solve(model, px=2.0, py=3.0, income=30.0)

cvs = Canvas(x_max=20, y_max=15, x_label="$x$", y_label="$y$")
cvs.add_utility(model, levels=levels.around(eq.utility, n=5))
cvs.add_budget(2.0, 3.0, 30.0)
cvs.add_equilibrium(eq)
cvs.save("perfect_substitutes.png")
```

<figure class="ev-fig" markdown>

![Perfect substitutes corner solution](../../assets/utility-viz/agora/models/perfect_substitutes.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../assets/utility-viz/agora/models/perfect_substitutes.py" download aria-label="Download the source"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Download the source</span></a></div>

<figcaption markdown>Perfect substitutes corner solution</figcaption>

</figure>

### Maximum utility

<!-- api: agora.utility_viz.models_index_6 -->

Maximum utility keeps only the larger weighted quantity in each bundle:

$$
u(x, y) = \max(a x, b y).
$$

Each indifference curve has two arms that extend towards the axes. The
preferences are non-convex, so on a linear budget the optimum normally
lies at the intercept with the greater weighted utility. There is no
dedicated class; the model is built with `CustomUtility`
([Advanced models](advanced.md#sec-advanced)).

```python
import numpy as np

from utility_viz import Canvas, Config, levels, solve
from utility_viz.models import CustomUtility

# figure settings
Config.load("manual.toml").use()

model = CustomUtility(
    func=lambda x, y: np.maximum(x, y), name="maximum"
)
eq = solve(model, px=2.0, py=3.0, income=30.0)

cvs = Canvas(x_max=25, y_max=20, x_label="$x$", y_label="$y$")
cvs.add_utility(model, levels=levels.around(eq.utility, n=5))
cvs.add_budget(2.0, 3.0, 30.0)
cvs.add_equilibrium(eq)
cvs.save("maximum.png")
```

<figure class="ev-fig" markdown>

![Maximum utility](../../assets/utility-viz/agora/models/maximum.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../assets/utility-viz/agora/models/maximum.py" download aria-label="Download the source"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Download the source</span></a></div>

<figcaption markdown>Maximum utility</figcaption>

</figure>

## Income and reference points

These models add special income effects, subsistence requirements or a
preferred consumption point.

### Quasi-linear

<!-- api: agora.utility_viz.models_index_7 -->

One good enters utility linearly:

$$
u(x, y) = f(x) + y.
$$

Once the solution is interior, the non-linear good has no income effect.
`linear_in` reverses the roles of $x$ and $y$.

```python
import numpy as np

from utility_viz import Canvas, Config, levels, solve
from utility_viz.models import QuasiLinear

# figure settings
Config.load("manual.toml").use()

model = QuasiLinear(v_func=np.log, linear_in="y")
eq = solve(model, px=1.0, py=2.0, income=20.0)

cvs = Canvas(x_max=15, y_max=15, x_label="$x$", y_label="$y$")
cvs.add_utility(model, levels=levels.around(eq.utility, n=5))
cvs.add_budget(1.0, 2.0, 20.0)
cvs.add_equilibrium(eq)
cvs.save("quasi_linear.png")
```

<figure class="ev-fig" markdown>

![Quasi-linear preferences vertically parallel indifference curves](../../assets/utility-viz/agora/models/quasi_linear.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../assets/utility-viz/agora/models/quasi_linear.py" download aria-label="Download the source"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Download the source</span></a></div>

<figcaption markdown>Quasi-linear preferences vertically parallel indifference curves</figcaption>

</figure>

### Haagsma

<!-- api: agora.utility_viz.models_index_8 -->

The [Haagsma (2012)](../project/references.md#haagsma2012) utility function,

$$
u(x, y) = \alpha_x \ln(x - \gamma_x) - \alpha_y \ln(\gamma_y - y).
$$

It is defined for $x > \gamma_x$ and $0 \le y < \gamma_y$, and requires
$0 < \alpha_x < \alpha_y$. Marshallian demand for $x$ falls with income, and
$x$ is a Giffen good when $\gamma_y p_y < I < \gamma_y p_y + \gamma_x p_x$.

Once income reaches $\gamma_y p_y + \gamma_x p_x$, utility has no finite
maximum on the budget line and the model raises `InvalidParameterError`.

```python
from utility_viz import Canvas, Config, levels, solve
from utility_viz.models import Haagsma

# figure settings
Config.load("manual.toml").use()

model = Haagsma(gamma_y=10.0)
eq = solve(model, px=1.0, py=1.0, income=11.0)

cvs = Canvas(x_max=9, y_max=12, x_label="$x$", y_label="$y$")
cvs.add_utility(model, levels=levels.around(eq.utility, n=4))
cvs.add_budget(1.0, 1.0, 11.0)
cvs.add_equilibrium(eq)
cvs.save("haagsma.png")
```

<figure class="ev-fig" markdown>

![Haagsma with $\gamma_y = 10$](../../assets/utility-viz/agora/models/haagsma.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../assets/utility-viz/agora/models/haagsma.py" download aria-label="Download the source"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Download the source</span></a></div>

<figcaption markdown>Haagsma with $\gamma_y = 10$</figcaption>

</figure>

### Stone-Geary

<!-- api: agora.utility_viz.models_index_9 -->

Cobb-Douglas with minimum consumption requirements
[Stone (1954)](../project/references.md#stone1954)[Geary (1950)](../project/references.md#geary1950):

$$
u(x, y) = (x - \overline{x})^\alpha (y - \overline{y})^\beta.
$$

The consumer first covers the subsistence quantities $\overline{x}$ and
$\overline{y}$, then allocates the remaining income like a Cobb-Douglas
consumer.

```python
from utility_viz import Canvas, Config, levels, solve
from utility_viz.models import StoneGeary

# figure settings
Config.load("manual.toml").use()

model = StoneGeary(alpha=0.5, beta=0.5, bar_x=2.0, bar_y=2.0)
eq = solve(model, px=2.0, py=3.0, income=30.0)

cvs = Canvas(x_max=20, y_max=15, x_label="$x$", y_label="$y$")
cvs.add_utility(model, levels=levels.around(eq.utility, n=5))
cvs.add_budget(2.0, 3.0, 30.0, fill=True)
cvs.add_equilibrium(eq)
cvs.save("stone_geary.png")
```

<figure class="ev-fig" markdown>

![Stone-Geary with $\overline{x} = \overline{y} = 2$](../../assets/utility-viz/agora/models/stone_geary.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../assets/utility-viz/agora/models/stone_geary.py" download aria-label="Download the source"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Download the source</span></a></div>

<figcaption markdown>Stone-Geary with $\overline{x} = \overline{y} = 2$</figcaption>

</figure>

### Satiation

<!-- api: agora.utility_viz.models_index_10 -->

A bliss point that maximises utility:

$$
u(x, y) = -a (x - x^*)^2 - b (y - y^*)^2.
$$

Utility falls in every direction away from $(x^*, y^*)$, so the
indifference curves are closed ellipses and monotonicity does not hold.

```python
import numpy as np

from utility_viz import Canvas, Config, levels
from utility_viz.models import Satiation

# figure settings
Config.load("manual.toml").use()

model = Satiation(bliss_x=6.0, bliss_y=4.0)

# curves from a utility grid
X, Y = np.meshgrid(
    np.linspace(0.1, 12.0, 300), np.linspace(0.1, 10.0, 300)
)

cvs = Canvas(x_max=12, y_max=10, x_label="$x$", y_label="$y$")
# five percentiles of u
cvs.add_utility(
    model, levels=levels.percentile(model(X, Y), n=5)
)
cvs.save("satiation.png")
```

<figure class="ev-fig" markdown>

![Satiation around the bliss point $(6, 4)$](../../assets/utility-viz/agora/models/satiation.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../assets/utility-viz/agora/models/satiation.py" download aria-label="Download the source"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Download the source</span></a></div>

<figcaption markdown>Satiation around the bliss point $(6, 4)$</figcaption>

</figure>
