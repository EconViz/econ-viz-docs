---
seo_title: "Command-line interface"
---

# Command-line interface

<span id="sec-cli"></span>

The command-line interface plots diagrams, runs batches and prints demand
formulas. Install it as a standalone tool with `uv tool install utility-viz`,
or prefix each command with `uv run` inside a `uv` project
([Installing the command-line tool](installation.md#sec-install-cli)). The 1.x command `econ-viz`, installed by the
`econ-viz` compatibility distribution, still works in 2.x: it warns
that it is deprecated and runs `utility-viz` with the same arguments
([Migrating from `econ-viz`](installation.md#sec-migrate)).

| Command | Description |
| --- | --- |
| `utility-viz help [``command``]` | Show help for the CLI or a specific command |
| `utility-viz models` | List all supported utility models |
| `utility-viz plot ...` | Generate and export a diagram |
| `utility-viz solve-tex ...` | Print a closed-form Marshallian demand as TeX |
| `utility-viz init [path]` | Create an `econ-viz.toml` configuration template |

## Help and models

<!-- api: agora.utility_viz.getting_started_cli_1 -->

Without an argument, list all commands; with one, show its options.

```bash
utility-viz help          # all commands
utility-viz help plot     # plot options
utility-viz help models   # models options
```

<!-- api: agora.utility_viz.getting_started_cli_2 -->

List the model names and parameters the CLI supports. `--model` takes
kebab-case names, which differ from the Python class names
([CLI models](cli.md#tab-models)). The parameter options are described in [Plotting](cli.md#sec-cli-plot).

<span id="tab-models"></span>

| Model | `--model` value | Required | Optional |
| --- | --- | --- | --- |
| Cobb-Douglas | `cobb-douglas` | `alpha`, `beta` | -- |
| CES | `ces` | `rho` | `alpha`, `beta` |
| Perfect complements | `leontief` | `a`, `b` | -- |
| Perfect substitutes | `perfect-substitutes` | `a`, `b` | -- |
| Satiation | `satiation` | `bliss-x`, `bliss-y` | `a`, `b` |
| Quasi-linear | `quasi-linear` | -- | `v-func`, `linear-in` |
| Stone-Geary | `stone-geary` | -- | `alpha`, `beta`, `bar-x`, `bar-y` |
| Translog | `translog` | -- | `alpha-0`, `alpha-x`, `alpha-y`, `beta-xx`, `beta-yy`, `beta-xy` |

## Plotting

<span id="sec-cli-plot"></span>

<!-- api: agora.utility_viz.getting_started_cli_3 -->

Give the model with `--model`, or the utility function with `--latex`,
not both. With `--output` the diagram is written to a file; without it an
interactive window opens.

The budget line and equilibrium need both prices and income.
`--no-budget`, `--no-equilibrium` and `--no-curves` each omit one layer
and can be combined ([Layer options](cli.md#tab-plot-flags)).

<span id="tab-plot-flags"></span>

| Case | Result |
| --- | --- |
| `--px`, `--py` and `--income` all given | Budget line drawn and equilibrium solved |
| Any price or income missing | Indifference curves only, no budget line or equilibrium |
| `--no-equilibrium` added | No solve and no equilibrium, even with prices and income |
| `--no-budget` added | Budget line hidden, even with prices and income |
| `--no-curves` with prices and income | Budget line and equilibrium only, no indifference curves |

```bash
# named model
utility-viz plot --model cobb-douglas --alpha 0.5 --beta 0.5 ...

# LaTeX expression
utility-viz plot --latex "x^{0.4} y^{0.6}" ...
```

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

# perfect complements, larger canvas
utility-viz plot --model leontief --a 1 --b 2 \
              --px 2 --py 3 --income 30 \
              --x-max 20 --y-max 15 \
              --output leontief.png

# CES, curves only
utility-viz plot --model ces --rho -0.5 \
              --x-max 20 --y-max 15 --n-curves 6 \
              --no-budget --no-equilibrium \
              --output ces.png

# satiation (bliss point)
utility-viz plot --model satiation --bliss-x 6 --bliss-y 4 \
              --x-max 12 --y-max 10 \
              --no-budget --no-equilibrium \
              --output satiation.png

# no --output: open a window
utility-viz plot --model cobb-douglas --px 2 --py 3 --income 30
```

### Model selection

### Prices and income

### Model parameters

Quasi-linear, Stone-Geary and Translog take these further options:

```bash
utility-viz plot --model stone-geary --bar-x 2 --bar-y 2 \
              --px 2 --py 3 --income 30 \
              --x-max 20 --y-max 15 --output stone_geary.png
```

Subsistence spending here is $2 \times 2 + 3 \times 2 = 10$, below the income
of $30$. With an income of $10$ or less, the solve fails because the budget
lies outside the model's domain.

### Canvas and layers

For batch runs, give each parameter set its own file name and create the
output directory first. `--x-max` and `--y-max` do not follow the prices;
when an intercept or the optimum falls outside the canvas, raise the limits
as well.

## Creating a configuration file

<span id="sec-cli-init"></span>

<!-- api: agora.utility_viz.getting_started_cli_4 -->

Write a commented `econ-viz.toml` template: the shared settings at the top
level and utility-viz's own under `[utility]`. Without a path it goes in
the current directory; an existing file is overwritten only with `--force`.
`--migrate` instead moves utility-viz's top-level tables under
`[utility]`, keeping the comments: it rewrites a `utility-viz.toml` in the
same directory into `econ-viz.toml` and keeps the old file, or, without
one, rewrites an old-layout `econ-viz.toml` in place.

```bash
utility-viz init
utility-viz init config/figures.toml
utility-viz init --migrate
utility-viz plot --config econ-viz.toml --model cobb-douglas \
              --px 2 --py 3 --income 30 --output figure.png
```

## Demand formulas

<!-- api: agora.utility_viz.getting_started_cli_5 -->

Print the closed-form Marshallian demand as TeX, for any document that
supports TeX math.

```bash
# numeric parameters
utility-viz solve-tex --model cobb-douglas --alpha 0.4 --beta 0.6

# symbolic parameters
utility-viz solve-tex --model cobb-douglas --symbolic-params

# custom price and income symbols
utility-viz solve-tex --model leontief --a 2 --b 3 \
                   --px-symbol p_1 --py-symbol p_2 --income-symbol M
```

Supports `cobb-douglas`, `leontief`, `perfect-substitutes` and their
LaTeX expressions. The command prints the formula only and writes no
figure.
