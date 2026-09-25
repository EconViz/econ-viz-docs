"""Generate the step-by-step figures on the Canvas page.

Run from the repository root:

    uv run --with econ-viz python scripts/canvas_figures.py
"""

from pathlib import Path

import matplotlib.pyplot as plt

from econ_viz import ArrowStyle, Canvas, LineStyle, levels, solve
from econ_viz.models import CobbDouglas

OUT = Path(__file__).resolve().parent.parent / "docs" / "assets" / "canvas"

model = CobbDouglas(alpha=0.5, beta=0.5)
eq = solve(model, px=2.0, py=3.0, income=30.0)
lvls = levels.around(eq.utility, n=3)

# Each figure adds one method on top of the indifference map.
STEPS = {
    "add_utility": lambda c: c,
    "add_budget": lambda c: c.add_budget(2.0, 3.0, 30.0, fill=True),
    "add_equilibrium": lambda c: c.add_budget(2.0, 3.0, 30.0, fill=True).add_equilibrium(eq),
    "add_ray": lambda c: c.add_budget(2.0, 3.0, 30.0).add_equilibrium(eq).add_ray(eq.y / eq.x),
    "add_point": lambda c: c.add_budget(2.0, 3.0, 30.0).add_point(12.0, 2.0, label="A"),
    "show_save": lambda c: c.add_budget(2.0, 3.0, 30.0, fill=True).add_equilibrium(eq, show_ray=True),
}

OUT.mkdir(parents=True, exist_ok=True)
for name, step in STEPS.items():
    canvas = Canvas(x_max=20, y_max=15, x_label="x", y_label="y", dpi=140)
    step(canvas.add_utility(model, levels=lvls)).save(str(OUT / f"{name}.png"))

line_styles = [
    LineStyle.SOLID,
    LineStyle.DASHED,
    LineStyle.DOTTED,
    LineStyle.DASHDOT,
]
fig, axes = plt.subplots(2, 2, figsize=(7, 7))
for ax, style in zip(axes.flat, line_styles):
    Canvas(
        title=style.value,
        x_line_style=style,
        y_line_style=style,
        fig=fig,
        ax=ax,
    )
fig.tight_layout()
fig.savefig(OUT / "line_styles.png", dpi=160, transparent=True)
plt.close(fig)

arrow_styles = [
    ArrowStyle.SIMPLE,
    ArrowStyle.TRIANGLE,
    ArrowStyle.FANCY,
    ArrowStyle.WEDGE,
]
fig, axes = plt.subplots(2, 2, figsize=(7, 7))
for ax, style in zip(axes.flat, arrow_styles):
    Canvas(
        title=style.name.title(),
        x_arrow_style=style,
        y_arrow_style=style,
        fig=fig,
        ax=ax,
    )
fig.tight_layout()
fig.savefig(OUT / "arrow_styles.png", dpi=160, transparent=True)
plt.close(fig)
