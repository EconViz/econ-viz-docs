---
seo_title: "Labels and placement"
---

# Labels and placement

<span id="sec-labels"></span>

## The locale table

Every word `macro-viz` puts in a figure is in `src/macro_viz/locale/labels.json`, indexed by language (`en`, `zh-TW`, `zh-CN`) and then by a stable id (`islm.curve.is`). The language comes from `[macro] language` of the settings.

A text with a field uses braces, such as `$AS({capital})$`. Math is written between `$...$`, not with Unicode subscripts.

Symbols are fixed across figures: only the price $p$ is lowercase, and every other variable ($Y$, $R$, $W$, $N$, $K$) is uppercase italic. Acronyms (`IS`, `LM`, `AD`, `AS`) and point names keep their case.

<!-- api: macro_viz.guides_labels_1 -->

| Prefix | Ids | Figures |
| --- | --- | --- |
| `keynesian` | 16 | Consumption function, Keynesian cross, multiplier |
| `money` | 17 | Money market and central-bank money |
| `adas` | 18 | Aggregate supply and demand and adjustment |
| `islm` | 17 | IS-LM and IS-LM with expected inflation |
| `solow` | 40 | Production function and Solow growth |
| `labor` | 14 | Wage setting and price setting |
| `parity` | 7 | Interest parity and open-economy IS-LM |
| `panels` | 20 | Linked panels |
| `axis, open` | 2 | The origin and the open-economy goods market |

```python
from macro_viz.i18n import label_ids

label_ids()
```

## Replacing text

<span id="sec-replace"></span>

Text you pass is used as written and is never translated. `labels` maps ids to text; an unknown id raises `ValidationError`.

```python
from macro_viz.visuals import islm_canvas

islm_canvas(
    tax,
    title="A tax increase",
    labels={"islm.curve.is": "$IS_0$", "islm.curve.is_shifted": "$IS_1$"},
).save("islm_tax_increase.svg")
```

`title=None` (the default) draws no title.

## Where a name goes

The name of a curve stands at the line end, in the first free place of the order lower-right, upper-left, lower-left, upper-right, then anywhere free. A place is free if the text touches no curve, guide, arrow, dot, axis or other label. The name of a point stands beside its dot.

## Moving labels by default

<span id="sec-nudges"></span>

`[macro.label.<group>]` moves every label of a group by default. The groups follow what a label names.

| Group | Names |
| --- | --- |
| `point` | Dots: equilibrium and path points (`A`, `A'`, `B`) |
| `curve` | Curves named at their end (`IS`, `LM`, `AD`, `AS`, `ZZ`) |
| `mark` | Values and marks on the figure |
| `region` | Names inside filled regions |
| `annotation` | Everything else that is text: braces, shift sizes, notes |

```toml
[macro.label.point]
top = "2pt"      # also bottom, left, right; pt, mm, cm or in
```

Axis titles and axis marks belong to no group and cannot be nudged.
