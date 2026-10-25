---
seo_title: "Introduction"
---

# Introduction

<span id="sec-intro"></span>

`micro-viz` is a Python package for the firm side of microeconomics: production, costs, perfect competition, monopoly and pricing, oligopoly, factor markets, uncertainty and information. Each topic has a model, which answers questions with numbers, and a figure drawn in textbook conventions from that model.

Figures are written as PNG, SVG or PDF. Statistics-style data charts and box-and-arrow flowcharts are outside the package.

`micro-viz` belongs to the EconViz family of packages and draws with `mosaickit`, a domain-independent scene and drawing library. Consumer theory and general equilibrium belong to `utility-viz`; introductory supply-and-demand diagrams belong to `principle-viz`; game theory is outside the package.

## Scope

The package covers six groups of topics, each with its own chapter ([Chapter guide](introduction.md#tab-guide)). Models never import a renderer, so a result can be used without drawing, and a builder only places what the model computed.

## Reading guide

<span id="tab-guide"></span>

| Topic | Description | Section |
| --- | --- | --- |
| Model and figure | How models, builders, layer ids and panels fit together | [Model and figure](model-figure.md#sec-model-figure) |
| Production and costs | Short-run production, cost functions, stepped and kinked cost | [Production and costs](production-costs.md#sec-production-costs) |
| Competition | Price-taking firms, industry supply, long-run costs, entry | [Competition and the long run](competition.md#sec-competition) |
| Monopoly and pricing | Monopoly, monopolistic competition, regulation, discrimination, tariffs, bundling, advertising, exhaustible resources | [Monopoly and pricing](monopoly.md#sec-monopoly) |
| Oligopoly | Duopoly, kinked demand, dominant firm, vertical chains | [Oligopoly and vertical chains](oligopoly.md#sec-oligopoly) |
| Inputs and technology | Isoquants, cost minimisation, learning and scope, factor markets, monopsony and unions | [Inputs and technology](inputs.md#sec-inputs) |
| Uncertainty and information | Expected utility, risk, auctions, adverse selection, signalling, moral hazard | [Uncertainty and information](uncertainty.md#sec-uncertainty) |
| Settings | The `[micro]` tables of `econ-viz.toml` | [Settings](settings.md#sec-settings) |
| Labels and placement | The locale table, replacing text, moving labels | [Labels and placement](labels.md#sec-labels) |
| Adding a figure | Model, builder, text, export, tests | [Adding a figure](adding-figure.md#sec-adding) |
| Animation | Animating a figure over a parameter | [Animation](animation.md#sec-animation) |

On first use, read [Quick start](../quickstart.md#sec-quickstart) and [Model and figure](model-figure.md#sec-model-figure). Each topic chapter then shows the model first and the figures second.

The scripts that draw the figures of these pages come as one zip, sorted by topic: [micro-viz-examples.zip](https://econ-viz.org/assets/micro-viz/micro-viz-examples.zip).
