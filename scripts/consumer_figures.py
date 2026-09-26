"""Generate the price-decomposition figure on the consumer guide.

Run from the repository root:

    uv run --with econ-viz python scripts/consumer_figures.py
"""

from pathlib import Path

from econ_viz import Canvas, DecompositionMethod
from econ_viz.models import CobbDouglas
from econ_viz.optimizer import decompose_price_effect

OUT = Path(__file__).resolve().parent.parent / "docs" / "assets" / "consumer"
OUT.mkdir(parents=True, exist_ok=True)

model = CobbDouglas(alpha=0.5, beta=0.5)
result = decompose_price_effect(model, px=(2.0, 4.0), py=3.0, income=60.0, method=DecompositionMethod.HICKS)

(
    Canvas(x_max=25, y_max=25, title="Hicks decomposition", dpi=140)
    .add_decomposition(result, show_arrows=True, label_effects=True, show_x_projections=True)
    .save(str(OUT / "cobb_douglas_hicks.png"))
)
