# CLI

`econ-viz` ships with a command-line interface for generating diagrams without writing Python.

## Commands

| Command | Description |
|---------|-------------|
| `econ-viz help [<command>]` | Show help for the CLI or a specific command |
| `econ-viz models` | List all supported utility models |
| `econ-viz plot ...` | Generate and export a diagram |
| `econ-viz solve-tex ...` | Print a closed-form Marshallian demand in plain TeX text |

## `econ-viz help`

```bash
econ-viz help          # top-level help
econ-viz help plot     # full plot options
econ-viz help models   # models command help
```

## `econ-viz models`

```bash
econ-viz models
```

Prints all model names and their parameters.

## `econ-viz plot`

### Model selection

Provide either `--model` or `--latex` — not both.

```bash
# Named model
econ-viz plot --model cobb-douglas --alpha 0.5 --beta 0.5 ...

# LaTeX expression (Cobb-Douglas / Leontief / Perfect Substitutes)
econ-viz plot --latex "x^{0.4} y^{0.6}" ...
```

### Examples

```bash
# Cobb-Douglas with equilibrium, budget line, and shaded feasible set
econ-viz plot --model cobb-douglas --alpha 0.5 --beta 0.5 \
              --px 2 --py 3 --income 30 \
              --fill --output cobb_douglas.png

# Parse a LaTeX expression, apply the Nord theme, draw expansion-path ray
econ-viz plot --latex "x^{0.4} y^{0.6}" \
              --px 2 --py 3 --income 30 \
              --theme nord --show-ray \
              --output cd_latex.png

# Leontief with larger canvas
econ-viz plot --model leontief --a 1 --b 2 \
              --px 2 --py 3 --income 30 \
              --x-max 20 --y-max 15 \
              --output leontief.png

# CES — curves only, no budget or equilibrium
econ-viz plot --model ces --rho -0.5 \
              --x-max 20 --y-max 15 --n-curves 6 \
              --no-budget --no-equilibrium \
              --output ces.png

# Satiation (bliss point)
econ-viz plot --model satiation --bliss-x 6 --bliss-y 4 \
              --x-max 12 --y-max 10 \
              --no-budget --no-equilibrium \
              --output satiation.png

# Open an interactive window instead of saving
econ-viz plot --model cobb-douglas --px 2 --py 3 --income 30
```

### All options

| Flag | Default | Description |
|------|---------|-------------|
| `--model`, `-m` | — | Model name: `cobb-douglas`, `leontief`, `perfect-substitutes`, `ces`, `satiation` |
| `--latex`, `-l` | — | LaTeX expression (Cobb-Douglas / Leontief / Perfect Substitutes) |
| `--px` | — | Price of good x |
| `--py` | — | Price of good y |
| `--income` | — | Consumer income |
| `--alpha` | 0.5 | Alpha parameter (Cobb-Douglas / CES) |
| `--beta` | 0.5 | Beta parameter (Cobb-Douglas / CES) |
| `--a` | 1.0 | a parameter (Leontief / Perfect Substitutes / Satiation) |
| `--b` | 1.0 | b parameter (Leontief / Perfect Substitutes / Satiation) |
| `--rho` | 0.5 | Substitution parameter (CES) |
| `--bliss-x` | 5.0 | Bliss point x-coordinate (Satiation) |
| `--bliss-y` | 5.0 | Bliss point y-coordinate (Satiation) |
| `--x-max` | 10 | Horizontal axis limit |
| `--y-max` | 10 | Vertical axis limit |
| `--x-label` | `x` | Horizontal axis label |
| `--y-label` | `y` | Vertical axis label |
| `--title` | — | Figure title |
| `--theme` | `default` | Colour theme: `default`, `nord` |
| `--n-curves` | 5 | Number of indifference curves |
| `--dpi` | 300 | Raster output resolution |
| `--fill` | off | Shade feasible set below the budget line |
| `--show-ray` | off | Draw expansion-path ray through the optimum |
| `--no-budget` | off | Omit the budget line |
| `--no-equilibrium` | off | Omit the equilibrium point |
| `--no-curves` | off | Omit indifference curves |
| `--output`, `-o` | — | Output file (`.png`, `.pdf`, `.svg`); omit to open an interactive window |

## `econ-viz solve-tex`

Use `solve-tex` when you want the closed-form Marshallian demand formula without generating a figure.

```bash
# Numeric parameters
econ-viz solve-tex --model cobb-douglas --alpha 0.4 --beta 0.6

# Symbolic parameters
econ-viz solve-tex --model cobb-douglas --symbolic-params

# Custom symbols for prices and income
econ-viz solve-tex --model leontief --a 2 --b 3 \
                   --px-symbol p_1 --py-symbol p_2 --income-symbol M
```

Supported closed-form models currently include:

- `cobb-douglas`
- `leontief`
- `perfect-substitutes`
- LaTeX shortcuts for Cobb-Douglas, Leontief, and Perfect Substitutes

The command prints plain TeX text, so you can drop the output directly into Markdown math, LaTeX, or slide tooling.
