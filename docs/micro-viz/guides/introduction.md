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

| Topic | Description |
| --- | --- |
| [Model and figure](model-figure.md#sec-model-figure) | How models, builders, layer ids and panels fit together |
| [Production and costs](production-costs.md#sec-production-costs) | Short-run production, cost functions, stepped and kinked cost |
| [Competition](competition.md#sec-competition) | Price-taking firms, industry supply, long-run costs, entry |
| [Monopoly and pricing](monopoly.md#sec-monopoly) | Monopoly, monopolistic competition, regulation, discrimination, tariffs, bundling, advertising, exhaustible resources |
| [Oligopoly](oligopoly.md#sec-oligopoly) | Duopoly, kinked demand, dominant firm, vertical chains |
| [Inputs and technology](inputs.md#sec-inputs) | Isoquants, cost minimisation, learning and scope, factor markets, monopsony and unions |
| [Uncertainty and information](uncertainty.md#sec-uncertainty) | Expected utility, risk, auctions, adverse selection, signalling, moral hazard |
| [Settings](settings.md#sec-settings) | The `[micro]` tables of `econ-viz.toml` |
| [Labels and placement](labels.md#sec-labels) | The locale table, replacing text, moving labels |
| [Adding a figure](adding-figure.md#sec-adding) | Model, builder, text, export, tests |
| [Animation](animation.md#sec-animation) | Animating a figure over a parameter |

On first use, read [Quick start](../quickstart.md#sec-quickstart) and [Model and figure](model-figure.md#sec-model-figure). Each topic chapter then shows the model first and the figures second.

The scripts that draw the figures of these pages come as one zip, sorted by topic: [micro-viz-examples.zip](https://econ-viz.org/assets/micro-viz/micro-viz-examples.zip).
