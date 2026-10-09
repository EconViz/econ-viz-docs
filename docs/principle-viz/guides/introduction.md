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

Curves are named at their ends instead of in a legend, areas are named
inside them, values are marked on the axes, and no text covers a line, a
point or other text. Figures are written as PNG, SVG or PDF; the
command-line tool prints calculation results as JSON.

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

| Part | Topic | Description | Section |
| --- | --- | --- | --- |
| Linear markets | Lines, equilibrium and shifts | [Linear markets](markets.md#sec-markets) | Discrete markets |
| Unit-by-unit demand and supply schedules | [Discrete markets](discrete.md#sec-discrete) | Market curves from individuals | Horizontal sum of individual curves |
| [Market curves from individuals](aggregation.md#sec-aggregation) | Elasticity and total revenue | Point and arc elasticity, total revenue curve | [Elasticity and total revenue](elasticity.md#sec-elasticity) |
| Welfare | Consumer surplus, producer surplus and deadweight loss | [Welfare](welfare.md#sec-welfare) | Taxes and subsidies |
| Tax wedge and subsidy cost | [Taxes and subsidies](taxes.md#sec-taxes) | Price controls | Price ceilings, price floors and shortages |
| [Price controls](controls.md#sec-controls) | International trade | Free trade, tariffs and import quotas | [International trade](trade.md#sec-trade) |
| Market failures | Externalities, common resources and public goods | [Market failures](failures.md#sec-failures) | Labor and loanable funds |
| Minimum wage and government borrowing | [Labor and loanable funds](factor-markets.md#sec-factor) | Production possibilities | Opportunity cost, growth and comparative advantage |
| [Production possibilities](ppf.md#sec-ppf) | Figures | Labels, layers and palettes | [Figures](figures.md#sec-figures) |
| Command line | Calculation results as JSON | [Command-line interface](../cli.md#sec-cli) |

On first use, read [Quick start](../quickstart.md#sec-quickstart), [Linear markets](markets.md#sec-markets) and [Figures](figures.md#sec-figures) in that
order. Each later chapter covers one topic: the calculation first, then the
figure. For the options of a specific command, go to [Command-line interface](../cli.md#sec-cli).
