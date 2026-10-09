---
seo_title: "Command-line interface"
---

# Command-line interface

<span id="sec-cli"></span>

The `principle-viz` command runs the calculations of this manual from the
shell and prints the result as JSON; `--output` also writes it to a file. It
draws no figures. Install it as a tool ([Installing the command-line tool](installation.md#sec-install-cli)), or prefix each
command with `uv run` inside a project.

```bash
principle-viz equilibrium \
  --demand-intercept 10 --demand-slope -1 \
  --supply-intercept 2 --supply-slope 1
```

```text
{
  "q_star": 4.0,
  "p_star": 6.0,
  "is_valid_market": true,
  "notes": []
}
```

## Market arguments

Most commands describe the market by two lines in inverse form,
$p = a + b Q$:

<!-- api: agora.principle_viz.cli_1 -->

## Commands

[CLI commands](cli.md#tab-cli) lists the calculation and options of each command; the calculation
of each is described in its chapter.

<span id="tab-cli"></span>

| Command | Calculation and extra options | Section |
| --- | --- | --- |
| `equilibrium` | Linear equilibrium | [Linear markets](guides/markets.md#sec-markets) |
| `shift` | Comparative statics: `--demand-delta-intercept`, `--demand-delta-slope`, `--supply-delta-intercept`, `--supply-delta-slope` | [Comparative statics](guides/markets.md#sec-shifts) |
| `discrete` | Discrete market: `--demand-values`, `--supply-values`, `--price-rule {midpoint,lower,upper}` | [Discrete markets](guides/discrete.md#sec-discrete) |
| `elasticity` | Point elasticity: `--intercept`, `--slope`, `--quantity`; arc elasticity with `--q1`, `--p1` | [Elasticity and total revenue](guides/elasticity.md#sec-elasticity) |
| `revenue` | Elasticity and revenue schedule: `--samples` | [Elasticity and total revenue](guides/elasticity.md#sec-elasticity) |
| `welfare` | Surplus: `--policy {baseline,tax,subsidy,control}` with the options of that policy | [Welfare](guides/welfare.md#sec-welfare) |
| `report-dwl` | One-row DWL report: `--policy {tax,subsidy,control}`, `--csv` | [Welfare](guides/welfare.md#sec-welfare) |
| `tax` | `--tax-type {fixed,per_unit,ad_valorem}`, `--amount`, `--tax-on {consumer,producer}` | [Taxes and subsidies](guides/taxes.md#sec-taxes) |
| `subsidy` | `--amount`, `--subsidy-to {consumer,producer}` | [Taxes and subsidies](guides/taxes.md#sec-taxes) |
| `controls` | `--control-type {ceiling,floor}`, `--control-price` | [Price controls](guides/controls.md#sec-controls) |
| `trade` | `--world-price`, `--tariff`, `--import-quota`, `--quota-rent-recipient` | [International trade](guides/trade.md#sec-trade) |
| `externality` | `--external-cost`, `--external-benefit` | [Market failures](guides/failures.md#sec-failures) |
| `common-resource` | `--congestion-cost` | [Market failures](guides/failures.md#sec-failures) |
| `public-good` | `--benefit-intercepts`, `--benefit-slopes`, `--cost-intercept`, `--cost-slope`, `--samples` | [Market failures](guides/failures.md#sec-failures) |
| `minimum-wage` | `--labor-demand-*`, `--labor-supply-*`, `--minimum-wage` | [Labor and loanable funds](guides/factor-markets.md#sec-factor) |
| `loanable-funds` | `--savings-*`, `--investment-*`, `--savings-shift`, `--investment-shift`, `--government-borrowing` | [Labor and loanable funds](guides/factor-markets.md#sec-factor) |
| `ppf` | `--x-intercept`, `--y-intercept`, `--curvature`, `--x-good`, `--y-good`, `--x-growth`, `--y-growth`, `--samples` | [Production possibilities](guides/ppf.md#sec-ppf) |

`principle-viz <command> --help` lists every option of a command.

```bash
principle-viz tax \
  --demand-intercept 10 --demand-slope -1 \
  --supply-intercept 2 --supply-slope 1 \
  --tax-type per_unit --amount 1 --tax-on producer
```

The output holds the untaxed equilibrium (`baseline_equilibrium`), the taxed
one (`post_tax`) and the changes, as `compare_tax_scenario()` returns them.
Here the quantity is 3.5, the consumer price 6.5 and the producer price 5.5.
