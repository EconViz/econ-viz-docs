"""Render the sweep GIFs of the Animation page.

The page shows the same sweeps as the manual's Animation chapter, drawn with the manual's settings
(`econ-viz.toml`, loaded the way the manual's examples load it): grey curves, black axes, a white page,
no title and no text on the frame. Each sweep holds some inputs fixed and varies one.

    parameter   prices and income fixed, one utility parameter varies
    price       utility and income fixed, the price of x varies
    income      utility and prices fixed, income varies
    budget      the budget line alone, without curves or optimum

Run it from this repository's root, in an environment that has `utility-viz[animation]`:

    uv run --with "utility-viz[animation]" python scripts/animation_figures.py

The GIFs go to docs/assets/animation/. Pass names to render only some, e.g. `ces_price_sweep`.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path

import matplotlib
import numpy as np

matplotlib.use("Agg")

from utility_viz import Canvas, Config, levels, solve  # noqa: E402
from utility_viz.core.animation import Animator  # noqa: E402
from utility_viz.models import CES, CobbDouglas, Leontief, PerfectSubstitutes  # noqa: E402
from utility_viz.models.curves.layers import Layer  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
AGORA = ROOT.parent / "agora"
SETTINGS = AGORA / "packages" / "utility-viz" / "config" / "econ-viz.toml"
# Besides agora/fonts, the TeX distribution holds the Latin font files that econ-viz.toml names.
TEXMF_DIRS = ["fonts/opentype/public/tex-gyre", "fonts/opentype/public/tex-gyre-math"]
OUT = ROOT / "docs" / "assets" / "animation"

X_MAX, Y_MAX = 14, 12
INCOME, PX, PY = 20.0, 2.0, 2.0  # the values a sweep holds fixed unless it varies them
FRAME_COUNT = 45


@dataclass(frozen=True)
class Family:
    """One utility function of the gallery."""

    key: str
    vary: Callable[[float], object]  # the model at one value of the swept parameter
    values: np.ndarray  # the parameter values of the parameter sweep
    model: object  # the model the price and income sweeps hold fixed
    extras: dict = field(default_factory=dict)  # extra `add_utility` arguments


FAMILIES = [
    Family(
        "cobb_douglas",
        lambda alpha: CobbDouglas(alpha=alpha, beta=1.0 - alpha),
        np.linspace(0.2, 0.8, FRAME_COUNT),
        CobbDouglas(alpha=0.5, beta=0.5),
    ),
    Family(
        "ces",
        lambda rho: CES(alpha=0.5, beta=0.5, rho=rho),
        np.concatenate([np.linspace(-1.2, -0.1, 23), np.linspace(0.1, 0.8, 22)]),  # skips rho = 0
        CES(alpha=0.5, beta=0.5, rho=0.4),
    ),
    Family(
        "perfect_substitutes",
        lambda a: PerfectSubstitutes(a=a, b=1.0),
        np.linspace(0.6, 2.4, FRAME_COUNT),
        PerfectSubstitutes(a=1.5, b=1.0),
        {"show_rays": True},
    ),
    Family(
        "leontief",
        lambda a: Leontief(a=a, b=1.0),
        np.linspace(0.6, 2.4, FRAME_COUNT),
        Leontief(a=1.5, b=1.0),
        {"show_rays": True, "show_kinks": True},
    ),
]

# Prices that move the x-intercept I/px at a constant speed (equal steps in price look slow, then fast).
PRICES = INCOME / np.linspace(INCOME / 6.0, INCOME / 1.0, FRAME_COUNT)
INCOMES = np.linspace(8.0, 36.0, FRAME_COUNT)


def canvas() -> Canvas:
    return Canvas(x_max=X_MAX, y_max=Y_MAX, x_label="$x_1$", y_label="$x_2$")


def fixed_levels(model) -> list[float]:
    """Five curves, chosen once for the whole sweep, so that only the budget line and the optimum move."""
    _, _, z = Layer.compute_contour(model, (0.1, X_MAX), (0.1, Y_MAX), res=400)
    return levels.percentile(z, n=5, lo=20, hi=80)


def parameter_sweep(family: Family) -> Callable[[float], Canvas]:
    def draw(value: float) -> Canvas:
        model = family.vary(float(value))
        eq = solve(model, px=PX, py=PY, income=INCOME)
        cvs = canvas()
        cvs.add_utility(model, levels=levels.around(eq.utility, n=5), **family.extras)
        cvs.add_budget(PX, PY, INCOME, fill=True)
        cvs.add_equilibrium(eq, show_ray=True)
        return cvs

    return draw


def price_sweep(family: Family) -> Callable[[float], Canvas]:
    fixed = fixed_levels(family.model)

    def draw(px: float) -> Canvas:
        eq = solve(family.model, px=float(px), py=PY, income=INCOME)
        cvs = canvas()
        cvs.add_utility(family.model, levels=fixed, **family.extras)
        cvs.add_budget(float(px), PY, INCOME, fill=True)
        cvs.add_equilibrium(eq, show_ray=True)
        return cvs

    return draw


def income_sweep(family: Family) -> Callable[[float], Canvas]:
    fixed = fixed_levels(family.model)

    def draw(income: float) -> Canvas:
        eq = solve(family.model, px=PX, py=PY, income=float(income))
        cvs = canvas()
        cvs.add_utility(family.model, levels=fixed, **family.extras)
        cvs.add_budget(PX, PY, float(income), fill=True)
        cvs.add_equilibrium(eq, show_ray=True)
        return cvs

    return draw


def budget_price_sweep(px: float) -> Canvas:
    cvs = canvas()
    cvs.add_budget(float(px), PY, INCOME, fill=True)
    return cvs


def budget_income_sweep(income: float) -> Canvas:
    cvs = canvas()
    cvs.add_budget(PX, PY, float(income), fill=True)
    return cvs


def jobs() -> dict[str, tuple[str, Callable[[float], Canvas], np.ndarray]]:
    """name -> (folder, draw, frames)"""
    found = {}
    for family in FAMILIES:
        found[f"{family.key}_parameter_sweep"] = ("parameter_sweeps", parameter_sweep(family), family.values)
        found[f"{family.key}_price_sweep"] = ("price_sweeps", price_sweep(family), PRICES)
        found[f"{family.key}_income_sweep"] = ("income_sweeps", income_sweep(family), INCOMES)
    found["budget_only_price_sweep"] = ("price_sweeps", budget_price_sweep, PRICES)
    found["budget_only_income_sweep"] = ("income_sweeps", budget_income_sweep, INCOMES)
    return found


def font_dirs() -> list[Path]:
    """Where the font files named in econ-viz.toml live: agora/fonts and the TeX distribution."""
    dirs = [AGORA / "fonts"]
    try:
        texmf = subprocess.run(
            ["kpsewhich", "-var-value", "TEXMFDIST"], capture_output=True, text=True, check=True
        ).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return dirs
    return dirs + [Path(texmf) / rel for rel in TEXMF_DIRS]


def stage_settings(tmp: str) -> Path:
    """Copy econ-viz.toml into *tmp* with the font files beside it.

    `Config.load` resolves the font names of [font] and [fonts] against the directory of the file, and
    the files are not in agora's config folder, so link them in first.
    """
    shutil.copy(SETTINGS, Path(tmp) / "econ-viz.toml")
    for directory in font_dirs():
        for font in directory.glob("*.[ot]t[fc]"):
            link = Path(tmp) / font.name
            if not link.exists():
                link.symlink_to(font)
    return Path(tmp) / "econ-viz.toml"


def main(only: list[str]) -> None:
    todo = {k: v for k, v in jobs().items() if not only or k in only}
    if not todo:
        raise SystemExit(f"no sweep named {only}; choose from {sorted(jobs())}")
    with tempfile.TemporaryDirectory() as tmp:
        Config.load(str(stage_settings(tmp))).use()
        for name, (folder, draw, frames) in todo.items():
            path = OUT / folder / f"{name}.gif"
            path.parent.mkdir(parents=True, exist_ok=True)
            Animator(draw, frames=frames).save(str(path), fps=12, dpi=120)
            print(" ", path.relative_to(ROOT))


if __name__ == "__main__":
    main(sys.argv[1:])
