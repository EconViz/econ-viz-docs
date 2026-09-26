"""Generate the Haagsma figure on the Advanced Models page.

Run from the repository root:

    uv run --with econ-viz python scripts/advanced_figures.py
"""

import warnings
from pathlib import Path

from econ_viz import Canvas, Effect
from econ_viz.models import Haagsma
from econ_viz.optimizer import decompose_price_effect

OUT = Path(__file__).resolve().parent.parent / "docs" / "assets" / "advanced"
OUT.mkdir(parents=True, exist_ok=True)

model = Haagsma(alpha_x=1.0, alpha_y=2.0, gamma_x=2.0, gamma_y=27.0)
with warnings.catch_warnings():
    warnings.filterwarnings("ignore", message=".*(inferior|Giffen) good.*")
    result = decompose_price_effect(model, px=(2.0, 1.0), py=1.0, income=28.0, method="hicks")

(
    Canvas(x_max=16, y_max=32, title="Haagsma: Giffen good", dpi=140)
    .add_decomposition(
        result,
        show_x_projections=True,
        substitution=Effect(label="SE"),
        income=Effect(label="IE"),
    )
    .save(str(OUT / "advanced_haagsma.png"))
)
