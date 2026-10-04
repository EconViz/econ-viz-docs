---
seo_title: "Command-Line Interface"
description: "Generate indifference curve and budget constraint diagrams from the command line with the utility-viz CLI, without writing any Python."
---

# CLI

`utility-viz` ships with a command-line interface for generating diagrams without writing Python.

Install it as a global command with `uv tool install utility-viz`, or prefix each command with `uv run` inside a uv project. See [Installation](installation.md) for details.

## Commands

| Command | Description |
|---------|-------------|
| `utility-viz help [<command>]` | Show help for the CLI or a specific command |
| `utility-viz models` | List all supported utility models |
| `utility-viz plot ...` | Generate and export a diagram |
| `utility-viz solve-tex ...` | Print a closed-form Marshallian demand in plain TeX text |
| `utility-viz init [path]` | Write a commented [settings file](../guides/config.md) template (`--force` overwrites) |

## Help {#utility-viz-help data-toc-label="Help"}

```bash
utility-viz help          # all commands
utility-viz help plot     # plot options
utility-viz help models   # models options
```

## Models {#utility-viz-models data-toc-label="Models"}

```bash
utility-viz models
```

Prints all model names and their parameters.

## Plot {#utility-viz-plot data-toc-label="Plot"}

### Model selection

Provide either `--model` or `--latex` — not both.

```bash
# named model
utility-viz plot --model cobb-douglas --alpha 0.5 --beta 0.5 ...

# LaTeX expression
utility-viz plot --latex "x^{0.4} y^{0.6}" ...
```

### Examples

```bash
# Cobb-Douglas, shaded budget set
utility-viz plot --model cobb-douglas --alpha 0.5 --beta 0.5 \
              --px 2 --py 3 --income 30 \
              --fill --output cobb_douglas.png

# LaTeX input, Nord theme, expansion path
utility-viz plot --latex "x^{0.4} y^{0.6}" \
              --px 2 --py 3 --income 30 \
              --theme nord --show-ray \
              --output cd_latex.png

# Leontief, larger canvas
utility-viz plot --model leontief --a 1 --b 2 \
              --px 2 --py 3 --income 30 \
              --x-max 20 --y-max 15 \
              --output leontief.png

# CES, curves only
utility-viz plot --model ces --rho -0.5 \
              --x-max 20 --y-max 15 --n-curves 6 \
              --no-budget --no-equilibrium \
              --output ces.png

# Satiation (bliss point)
utility-viz plot --model satiation --bliss-x 6 --bliss-y 4 \
              --x-max 12 --y-max 10 \
              --no-budget --no-equilibrium \
              --output satiation.png

# no --output: open a window
utility-viz plot --model cobb-douglas --px 2 --py 3 --income 30
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
| `--config` | — | [Settings file](../guides/config.md) (`utility-viz.toml`); `--theme` replaces its `base` |
| `--n-curves` | 5 | Number of indifference curves |
| `--dpi` | 300 | Raster output resolution |
| `--fill` | off | Shade feasible set below the budget line |
| `--show-ray` | off | Draw expansion-path ray through the optimum |
| `--no-budget` | off | Omit the budget line |
| `--no-equilibrium` | off | Omit the equilibrium point |
| `--no-curves` | off | Omit indifference curves |
| `--output`, `-o` | — | Output file (`.png`, `.pdf`, `.svg`); omit to open an interactive window |

## Demand formulas {#utility-viz-solve-tex data-toc-label="Demand formulas"}

Use `solve-tex` when you want the closed-form Marshallian demand formula without generating a figure.

```bash
# numeric parameters
utility-viz solve-tex --model cobb-douglas --alpha 0.4 --beta 0.6

# symbolic parameters
utility-viz solve-tex --model cobb-douglas --symbolic-params

# custom price/income symbols
utility-viz solve-tex --model leontief --a 2 --b 3 \
                   --px-symbol p_1 --py-symbol p_2 --income-symbol M
```

Supported closed-form models currently include:

- `cobb-douglas`
- `leontief`
- `perfect-substitutes`
- LaTeX shortcuts for Cobb-Douglas, Leontief, and Perfect Substitutes

The command prints plain TeX text, so you can drop the output directly into Markdown math, LaTeX, or slide tooling.
