---
seo_title: "标签与位置"
---

# 标签与位置

<span id="sec-labels"></span>

## 语系表

`macro-viz` 放进图中的每个字都在 `src/macro_viz/locale/labels.json`，先依语言（`en`、`zh-TW`、`zh-CN`）、再依稳定的编号（`islm.curve.is`）索引。语言来自设置的 `[macro] language`。

含字段的文本使用大括号，例如 `$AS({capital})$`。数学式写在 `$...$` 中，不使用 Unicode 下标。

符号在各图之间固定：只有价格 $p$ 用小写，其他变量（$Y$、$R$、$W$、$N$、$K$）一律用大写斜体。缩写（`IS`、`LM`、`AD`、`AS`）与点名保留原有的大小写。

<!-- api: macro_viz.guides_labels_1 -->

| 前缀 | 编号数 | 图形 |
| --- | --- | --- |
| `keynesian` | 16 | 消费函数、凯因斯十字、乘数 |
| `money` | 17 | 货币市场与央行货币 |
| `adas` | 18 | 总合供给与需求及其调整 |
| `islm` | 17 | IS-LM 与含预期通膨的 IS-LM |
| `solow` | 40 | 生产函数与梭罗成长 |
| `labor` | 14 | 工资设置与价格设置 |
| `parity` | 7 | 利率平价与开放经济 IS-LM |
| `panels` | 20 | 连动面板 |
| `axis, open` | 2 | 原点与开放经济商品市场 |

```python
from macro_viz.i18n import label_ids

label_ids()
```

## 取代文本

<span id="sec-replace"></span>

你传入的文本照原样使用，不会翻译。`labels` 把编号对应到文本；未知的编号会引发 `ValidationError`。

```python
from macro_viz.visuals import islm_canvas

islm_canvas(
    tax,
    title="A tax increase",
    labels={"islm.curve.is": "$IS_0$", "islm.curve.is_shifted": "$IS_1$"},
).save("islm_tax_increase.svg")
```

`title=None`（缺省）不画标题。

## 名称放在哪里

曲线的名称放在线的末端，依序试右下、左上、左下、右上，再试其他空位。文本没有碰到任何曲线、辅助线、箭头、圆点、座标轴或其他标签，这个位置才算空。点的名称放在圆点旁边。

## 缺省移动标签

<span id="sec-nudges"></span>

`[macro.label.<group>]` 缺省移动一组中的每个标签。分组依标签所指的对象而定。

| 分组 | 对象 |
| --- | --- |
| `point` | 圆点：均衡点与路径点（`A`、`A'`、`B`） |
| `curve` | 在末端命名的曲线（`IS`、`LM`、`AD`、`AS`、`ZZ`） |
| `mark` | 图上的数值与记号 |
| `region` | 填色区域中的名称 |
| `annotation` | 其他所有文本：大括号、移动量、注记 |

```toml
[macro.label.point]
top = "2pt"      # 还有 bottom、left、right；单位 pt、mm、cm 或 in
```

座标轴标题与轴上记号不属于任何分组，不能移动。
