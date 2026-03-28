# Leontief (Perfect Complements)

$$U(x, y) = \min(ax, by)$$

Goods are consumed in fixed proportions. Indifference curves are L-shaped with a kink along the expansion path $y = \tfrac{a}{b}\,x$.

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `a` | float | 1.0 | Coefficient on good $x$ |
| `b` | float | 1.0 | Coefficient on good $y$ |

## Optimisation

The consumer solves

$$\max_{x,\,y}\; \min(ax, by) \quad \text{subject to}\quad p_x x + p_y y = I$$

The $\mathrm{MRS}$ is undefined at the kink, so the standard tangency condition never holds in the interior. The optimum always lies at the kink vertex where $ax = by$. Substituting $y = \tfrac{a}{b}\,x$ into the budget constraint:

$$\begin{aligned}
p_x x + p_y \cdot \frac{a}{b}\,x &= I \\[6pt]
x\!\left(p_x + \frac{a\,p_y}{b}\right) &= I
\end{aligned}$$

The Marshallian demands are therefore

$$x^* = \frac{I}{p_x + \dfrac{a}{b}\,p_y}, \qquad y^* = \frac{a}{b}\,x^*$$

## Usage

=== "Python"

    ```python
    from econ_viz import Canvas, levels, solve
    from econ_viz.models import Leontief

    model = Leontief(a=1.0, b=1.0)
    eq    = solve(model, px=2.0, py=3.0, income=30.0)
    lvls  = levels.around(eq.utility, n=5)

    Canvas(x_max=20, y_max=15, title=r"Leontief $\min(x, y)$") \
        .add_utility(model, levels=lvls, show_rays=True, show_kinks=True) \
        .add_budget(2.0, 3.0, 30.0) \
        .add_equilibrium(eq) \
        .save("leontief.png")
    ```

=== "CLI"

    ```bash
    econ-viz plot --model leontief --a 1 --b 1 \
                  --px 2 --py 3 --income 30 --output leontief.png
    ```
