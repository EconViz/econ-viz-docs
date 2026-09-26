"""Generate indifference-curve hierarchy examples for the Canvas guide.

Run from the repository root:

    uv run --with econ-viz python scripts/ic_hierarchy_figures.py
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

from econ_viz import Canvas, levels, solve
from econ_viz.models import CobbDouglas

OUT = Path(__file__).resolve().parent.parent / "docs" / "assets" / "canvas"
OUT.mkdir(parents=True, exist_ok=True)

model = CobbDouglas(alpha=0.5, beta=0.5)
px, py, income = 2.0, 3.0, 30.0
eq = solve(model, px, py, income)
lvls = levels.around(eq.utility, n=5)

for name, options in [
    ("ic_hierarchy_before", {}),
    ("ic_hierarchy_after", {"highlight_level": eq.utility}),
    (
        "ic_hierarchy_ordinal",
        {"highlight_level": eq.utility, "show_ic_labels": True, "label_style": "ordinal"},
    ),
]:
    (
        Canvas(x_max=20, y_max=15, x_label="Pizza", y_label="Cola", dpi=140)
        .add_utility(model, levels=lvls, **options)
        .add_budget(px, py, income, fill=True)
        .add_equilibrium(eq)
        .save(str(OUT / f"{name}.png"))
    )
