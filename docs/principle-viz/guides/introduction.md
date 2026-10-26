---
seo_title: "Introduction"
---

# Introduction

<span id="sec-intro"></span>

`principle-viz` is a Python package for the diagrams of a
principles-of-economics course: supply and demand, equilibrium and its
shifts, taxes and subsidies, price controls, welfare, international trade,
market failures, factor markets and the production possibilities frontier.
Each topic has a calculation, which returns numbers, and a figure drawn in
textbook conventions.

Figures are written as PNG, SVG or PDF; the command-line tool prints
calculation results as JSON.

`principle-viz` belongs to the EconViz family of packages and draws
with `mosaickit`, a domain-independent scene and drawing library. Its
sibling `utility-viz` is a microeconomics package covering utility
models, optimal-bundle solving, indifference curves, budget lines, consumer
equilibrium, demand curves and Edgeworth boxes; `principle-viz` does
not include these.

## Scope

`principle-viz` handles linear markets, and its features fall into
four parts: markets, policy, applications and tools. Calculations and
figures can be used separately: a result can be printed, written as JSON or
passed to `MarketFigure` to be drawn.

## Reading guide

The manual is organized in four parts: markets, policy, applications and
tools (see [Chapter guide](introduction.md#tab-guide)).

<span id="tab-guide"></span>

| Part | Topic | Description |
| --- | --- | --- |
| Markets | [Linear markets](markets.md#sec-markets) | Lines, equilibrium and shifts |
|  | [Discrete markets](discrete.md#sec-discrete) | Unit-by-unit demand and supply schedules |
|  | [Market curves from individuals](aggregation.md#sec-aggregation) | Horizontal sum of individual curves |
|  | [Elasticity and total revenue](elasticity.md#sec-elasticity) | Point and arc elasticity, total revenue curve |
| Policy | [Welfare](welfare.md#sec-welfare) | Consumer surplus, producer surplus and deadweight loss |
|  | [Taxes and subsidies](taxes.md#sec-taxes) | Tax wedge and subsidy cost |
|  | [Price controls](controls.md#sec-controls) | Price ceilings, price floors and shortages |
| Applications | [International trade](trade.md#sec-trade) | Free trade, tariffs and import quotas |
|  | [Market failures](failures.md#sec-failures) | Externalities, common resources and public goods |
|  | [Labor and loanable funds](factor-markets.md#sec-factor) | Minimum wage and government borrowing |
|  | [Production possibilities](ppf.md#sec-ppf) | Opportunity cost, growth and comparative advantage |
| Tools | [Figures](figures.md#sec-figures) | Labels, layers and palettes |
|  | [Command line](../cli.md#sec-cli) | Calculation results as JSON |

On first use, read [Quick start](../quickstart.md#sec-quickstart), [Linear markets](markets.md#sec-markets) and [Figures](figures.md#sec-figures) in that
order. Each later chapter covers one topic: the calculation first, then the
figure. For the options of a specific command, go to [Command-line interface](../cli.md#sec-cli).

The scripts that draw the figures of this manual come as one zip, sorted by topic: [principle-viz-examples.zip](https://econ-viz.org/assets/principle-viz/agora/principle-viz-examples.zip).
