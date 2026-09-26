"""Generate the built-in theme example images for the theme guide.

Run from the repository root:

    uv run --with econ-viz python scripts/theme_figures.py
"""

from pathlib import Path

from econ_viz import Canvas, levels, solve, themes
from econ_viz.models import CobbDouglas

OUT = Path(__file__).resolve().parent.parent / "docs" / "assets" / "themes"
OUT.mkdir(parents=True, exist_ok=True)

model = CobbDouglas(alpha=0.5, beta=0.5)
px, py, income = 2.0, 3.0, 30.0
eq = solve(model, px, py, income)
lvls = levels.around(eq.utility, n=3)

for theme in [themes.paper, themes.monochrome, themes.presentation, themes.dark]:
    (
        Canvas(x_max=20, y_max=15, x_label="Pizza", y_label="Cola", dpi=140, theme=theme)
        .add_utility(model, levels=lvls)
        .add_budget(px, py, income, fill=True)
        .add_equilibrium(eq)
        .save(str(OUT / f"theme_{theme.name}.png"))
    )
