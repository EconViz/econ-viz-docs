# Cobb-Douglas

$$U(x, y) = x^\alpha \cdot y^\beta$$

The most common textbook utility function. Indifference curves are smooth, strictly convex, and asymptotic to both axes.

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `alpha` | float | 0.5 | Output elasticity of good $x$ |
| `beta` | float | 0.5 | Output elasticity of good $y$ |

## Optimisation

The consumer solves

$$\max_{x,\,y}\; x^\alpha y^\beta \quad \text{subject to}\quad p_x x + p_y y = I$$

The Lagrangian is

$$\mathcal{L}(x, y, \lambda) = x^\alpha y^\beta - \lambda\,(p_x x + p_y y - I)$$

First-order conditions:

$$\begin{aligned}
\frac{\partial \mathcal{L}}{\partial x} &= \alpha x^{\alpha-1} y^\beta - \lambda p_x = 0 \\[6pt]
\frac{\partial \mathcal{L}}{\partial y} &= \beta x^\alpha y^{\beta-1} - \lambda p_y = 0 \\[6pt]
\frac{\partial \mathcal{L}}{\partial \lambda} &= p_x x + p_y y - I = 0
\end{aligned}$$

Dividing the first two conditions gives the tangency condition $\mathrm{MRS} = p_x/p_y$:

$$\frac{\alpha y}{\beta x} = \frac{p_x}{p_y}$$

Substituting into the budget constraint yields the Marshallian demands:

$$x^* = \frac{\alpha}{\alpha + \beta}\cdot\frac{I}{p_x}, \qquad y^* = \frac{\beta}{\alpha + \beta}\cdot\frac{I}{p_y}$$

## Usage

=== "Python"

    ```python
    from econ_viz import Canvas, levels, solve
    from econ_viz.models import CobbDouglas

    model = CobbDouglas(alpha=0.5, beta=0.5)
    eq    = solve(model, px=2.0, py=3.0, income=30.0)
    lvls  = levels.around(eq.utility, n=5)

    Canvas(x_max=20, y_max=15, title=r"Cobb-Douglas $x^{0.5} y^{0.5}$") \
        .add_utility(model, levels=lvls) \
        .add_budget(2.0, 3.0, 30.0, fill=True) \
        .add_equilibrium(eq, show_ray=True) \
        .save("cobb_douglas.png")
    ```

=== "CLI"

    ```bash
    econ-viz plot --model cobb-douglas --alpha 0.5 --beta 0.5 \
                  --px 2 --py 3 --income 30 --output cobb_douglas.png
    ```
