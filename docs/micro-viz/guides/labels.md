---
seo_title: "Labels and placement"
---

# Labels and placement

<span id="sec-labels"></span>

## The locale table

Every word `micro-viz` puts in a figure lives in `src/micro_viz/locale/labels.json`, keyed by a stable id (`production.tp`) and then by language (`en`, `zh-TW`, `zh-CN`). The language comes from `[micro] language`, from `PlotTheme.language`, or from `--language` in the example scripts.

A text with fields uses doubled braces in the table, as in `$D_{{{index}}}$`; a text without fields uses single braces. Math is written in `$...$`; Unicode subscripts are not used.

Notation is fixed across figures: only the price $p$ is lowercase; every other variable is an uppercase italic symbol; acronyms (MC, ATC) and point names keep their case.

## Replacing text

Anything passed by the caller is used as given and never translated.

```python
unit_cost_canvas(
    analysis,
    title="Unit costs",
    x_label="Quantity",
    labels={"cost.mc": "Marginal cost"},
)
```

`title=None` (the default) draws no title. To change one label of one saved figure by its layer id, use the shared per-figure table, which `mosaickit` applies when the figure is saved:

```toml
[figure.unit_cost.label."micro.cost.avc.label"]
top = "3pt"
right = "2mm"
```

## Moving labels by default

<span id="sec-nudges"></span>

`[micro.label.<group>]` moves every label of a group by one length per side (`top`, `bottom`, `left`, `right`; units `pt`, `mm`, `cm`, `in`). The groups follow what a label names ([Label groups](labels.md#tab-label-groups)).

<span id="tab-label-groups"></span>

| Group | Labels |
| --- | --- |
| `point` | Labelled dots |
| `curve` | Curve names beside their end |
| `region` | Names inside shaded regions, including callouts |
| `mark` | Price lines, quantity marks and other guides that carry a value |
| `annotation` | Other text |

Axis titles, the origin and the axis marks ($L_1$, $Q^*$) belong to no group and cannot be moved.

## Where labels go

- A curve name sits beside the end of its curve. Where two curves end close together, the builder names one of them part of the way along (`at`), so the names do not touch.
- A point label sits beside its dot, and `mosaickit` chooses the side that touches no line, marker or other text.
- Text that cannot find a free spot makes `mosaickit` emit a `LayoutWarning`. Tests render figures with layout warnings turned into errors, so a figure with an overlapping label fails.

## Guides that lie on a curve

A dashed guide that lies entirely on a solid straight curve piece is not drawn. The price line carrying a dashed price guide is the usual case. The mark that names the level, such as $p$, is a separate layer and stays.

The rule is `drop_covered_guides` in `micro_viz.visuals.common`, applied once when a `Plane` or a competition figure is finished. A dashed curve (AFC, for example) does not hide a guide.

<span id="fig-firm-loss"></span>

<figure class="ev-fig" markdown>

![A loss: the price mark stays, the dashed price line is dropped](../../assets/micro-viz/competition/firm_loss.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../assets/micro-viz/competition/competition.py" download aria-label="Download the source"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Download the source</span></a></div>

<figcaption markdown>A loss: the price mark stays, the dashed price line is dropped</figcaption>

</figure>
