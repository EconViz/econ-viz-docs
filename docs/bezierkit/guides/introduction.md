---
seo_title: "Introduction"
---

# Introduction

<span id="sec-intro"></span>

The `bezierkit` package is a small mathematical toolkit for Bézier
curves. It builds curves from control points or from endpoint conditions,
evaluates and differentiates them, splits and restricts them, fits them to
functions, sampled points and level sets, and writes them out as JSON, SVG
path data or TikZ. It draws nothing: plotting is left to renderers such as
Matplotlib, `mosaickit` or a LaTeX document, which receive exact
cubic control points.

## Notation

A point or vector lives in $\mathbb{R}^d$ for some dimension $d \ge 1$; most figures
use $d = 2$. The Euclidean norm of $x \in \mathbb{R}^d$ is

$$
\left\lVert x \right\rVert = \sqrt{x_1^2 + \ldots + x_d^2},
$$

and $\left\lVert x \right\rVert_\infty = \max_k |x_k|$ is the maximum norm. A set $S \subseteq \mathbb{R}^d$
is convex if $\lambda p + (1 - \lambda) q \in S$ whenever $p, q \in S$ and
$\lambda \in [0, 1]$; the convex hull of a finite set of points is the set of
all their convex combinations $\sum_i \lambda_i P_i$ with $\lambda_i \ge 0$ and
$\sum_i \lambda_i = 1$. A map $A: \mathbb{R}^d \to \mathbb{R}^e$ is affine if
$A(x) = M x + v$ for a matrix $M$ and a vector $v$. A function is
$C^k$ if it has continuous derivatives up to order $k$.

A Bézier curve of degree $n$ has $n + 1$ control points $P_0, \ldots, P_n$ and
is the map

$$
B(t) = \sum_{i=0}^n b_{i,n}(t) P_i, \quad t \in [0, 1],
$$

where

$$
b_{i,n}(t) = \binom{n}{i} t^i (1-t)^{n-i}
$$

are the Bernstein polynomials ([Bézier curves](curves.md#sec-curves)). The control points, joined in
order, form the control polygon. Every curve in the package is parameterized
over $[0, 1]$; a parameter outside it raises `ParameterOutOfDomain`. The
letter $d$ always denotes the dimension; tolerances are written $\epsilon$.

## Mathematics and proofs

Each chapter first recalls the standard definitions it uses, with a
reference, and then states the properties the algorithms rely on as numbered
lemmas, propositions, theorems and corollaries: what the Bernstein basis
guarantees, why de Casteljau's algorithm evaluates and subdivides a curve,
how far a Hermite interpolant can stray, what the exporters lose to rounding.
Their proofs are collected in [Proofs](../project/proofs.md#app-proofs), so the chapters can be read for
the API alone. Conventions that belong to this package, and not to the
literature, are called package conventions. The standard references are
[Farin (2002)](../project/references.md#farin2002), [Prautzsch (2002)](../project/references.md#prautzsch2002) and, for the Bernstein basis,
[Farouki (2012)](../project/references.md#farouki2012).

## Reading guide

<span id="tab-guide"></span>

| Topic | Contents | Section |
| --- | --- | --- |
| Points, vectors, parameters, errors | [Geometry values](geometry.md#sec-geometry) | Bernstein basis, curves, evaluation |
| [Bézier curves](curves.md#sec-curves) | Derivatives, reversal, subdivision | [Derivatives, reversal and subdivision](operations.md#sec-operations) |
| Cubic segments and piecewise paths | [Cubic segments and paths](paths.md#sec-paths) | Constructions and Hermite interpolation |
| [Constructions and Hermite interpolation](construction.md#sec-construction) | Fitting functions and polylines | [Fitting](fitting.md#sec-fitting) |
| Tracing level sets | [Level sets](implicit.md#sec-implicit) | Sampling, JSON, SVG, TikZ, Matplotlib |
| [Sampling and export](export.md#sec-export) | Command line | [Command-line interface](../cli.md#sec-cli) |

On first use, read [Quick start](../quickstart.md#sec-quickstart) and [Bézier curves](curves.md#sec-curves). The figures in this
manual are themselves `bezierkit` output: every curve in them was
written by the TikZ exporter of [Sampling and export](export.md#sec-export) and compiled with LaTeX.
