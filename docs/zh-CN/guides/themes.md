---
seo_title: "经济学图形的配色主题"
description: "用内置主题控制 econ-viz 图形的颜色与线条粗细，包含色盲友善的缺省配色，也可以自定义主题。"
---

# 主题

主题控制 Canvas 使用的所有颜色与线条粗细。

![缺省主题范例](../../assets/themes/theme_default.png)

## 内置主题

### Default

```python
from econ_viz import Canvas, themes

cvs = Canvas(x_max=20, y_max=15, theme=themes.default)
```

默认主题的颜色取自一组**色盲友好**的配色\citep{thriveth2014}，可从 `themes.COLORBLIND_CYCLE_HEX` 与 `themes.COLORBLIND_CYCLE_RGB` 获取。经济学教学大量依赖图形，因此不应只靠颜色传达含义，以免视觉障碍的学生无法辨识\citep{kugler1996}。

### Nord

```python
cvs = Canvas(x_max=20, y_max=15, theme=themes.nord)
```

Nord 主题使用 [Nord 配色](https://www.nordtheme.com/)，以冷色蓝与低饱和色调为主，适合学术演示文稿。

![Nord 主题范例](../../assets/themes/theme_nord.png)

### Paper

```python
cvs = Canvas(x_max=20, y_max=15, theme=themes.paper)
```

Paper 主题使用较细的线条、较小的标记，以及节制的字号，背景透明，适合印刷或期刊排版对墨量与版面较敏感的场合。

![Paper 主题范例](../../assets/themes/theme_paper.png)

### Monochrome

```python
cvs = Canvas(x_max=20, y_max=15, theme=themes.monochrome)
```

Monochrome 主题完全不使用颜色，所有元素都是灰阶，改以**线条样式**区分曲线、预算线与射线，并以**标记形状**区分不同的点。适合黑白打印，或需要完全不依赖颜色辨识的色盲友好场合。

![Monochrome 主题范例](../../assets/themes/theme_monochrome.png)

### Presentation

```python
cvs = Canvas(x_max=20, y_max=15, theme=themes.presentation)
```

Presentation 主题使用较大的文字、较粗的线条与较大的标记，适合投影屏幕或演讲厅等需要远距离辨识的场合。

![Presentation 主题范例](../../assets/themes/theme_presentation.png)

### Dark

```python
cvs = Canvas(x_max=20, y_max=15, theme=themes.dark)
```

Dark 主题使用深色背景搭配浅色前景，适合深色模式的幻灯片或网站。

![Dark 主题范例](../../assets/themes/theme_dark.png)

## 自定义主题

构造函数可以只传入想改的字段，其余保留内置默认值：

```python
from econ_viz import Theme

my_theme = Theme(
    name="custom",
    axis_color="#333333",
    label_color="#333333",
    ic_color="#2563eb",
    ic_linewidth=1.5,
    budget_color="#dc2626",
    eq_color="#16a34a",
    eq_markersize=6.0,
)

cvs = Canvas(x_max=20, y_max=15, theme=my_theme)
```

图上每一条线、每一种标记、填色、标签与图例，也都有一个由上面字段组成的整体默认值，例如 `theme.ic_stroke`、`theme.eq_marker`、`theme.point_label`。如果想整组修改（例如让 Edgeworth 盒状图的 core 段除了颜色，还要有箭头），可以继承 `Theme` 并重写该属性：

```python
from econ_viz import ArrowStyle, Stroke, Theme

class MyTheme(Theme):
    @property
    def core_stroke(self) -> Stroke:
        return Stroke(width=3.0, color="#C0392B", arrow=ArrowStyle.TRIANGLE)

cvs = EdgeworthBox(..., theme=MyTheme(name="my-theme"))
```

方法显式传入的参数（例如 `add_core(stroke=...)`）仍然优先于主题，主题则优先于内置默认值，与[配置文件](config.md)的优先顺序一致。

## 主题字段

| 字段 | 说明 |
|------|------|
| `name` | 主题名称 |
| `axis_color` | 坐标轴与箭头的颜色 |
| `label_color` | 坐标轴标签与原点标签的颜色 |
| `ic_color`、`ic_linewidth` | 无差异曲线的颜色与线宽 |
| `path_color`、`path_linewidth` | PCC / ICC 路径的颜色与线宽 |
| `budget_color`、`budget_linewidth` | 预算线的颜色与线宽 |
| `budget_fill_alpha` | 可行集阴影的不透明度 |
| `eq_color`、`eq_markersize` | 均衡点的颜色与大小 |
| `ray_color`、`ray_linewidth` | 扩张路径射线的颜色与线宽 |
| `kink_color` | 折点标记的颜色 |
| `sub_effect_color`、`inc_effect_color` | 替代效应、收入效应箭头的颜色 |
| `effect_arrow_linewidth` | 效应箭头的线宽 |
| `compensated_budget_color`、`compensated_budget_linewidth`、`compensated_budget_linestyle` | 分解图中补偿后预算线的样式 |
| `subsistence_color`、`subsistence_linewidth` | Stone-Geary 最低消费参考线 |
| `contract_color`、`contract_linewidth` | Edgeworth 契约曲线 |
| `core_color`、`core_linewidth` | Edgeworth core |
| `price_color`、`price_linewidth` | Edgeworth 价格线 |
| `walrasian_color`、`walrasian_markersize` | Edgeworth Walrasian 均衡点标记 |
| `axis_stroke`、`drop_stroke`、`projection_stroke`、`guide_stroke`、`box_stroke` | 没有各自颜色／线宽字段的线条 |

## 样式属性

以下每个属性都是由上面的字段组成的 [`Stroke`](canvas.md#styles)、[`Marker`](canvas.md#styles)、[`Label`](canvas.md#styles)、[`Fill`](canvas.md#styles) 或 [`Legend`](canvas.md#styles)。在子类中重写某个属性，会影响所有没有另外传入该项参数的图形；[配置文件](config.md)的 `[stroke.<name>]`、`[marker.<name>]`、`[label.<name>]`、`[fill.<name>]` 部分设置的正是同一批属性。

| 种类 | 属性 |
|------|------|
| Stroke | `ic_stroke`、`budget_stroke`、`ray_stroke`、`path_stroke`、`compensated_budget_stroke`、`final_budget_stroke`、`substitution_stroke`、`income_stroke`、`subsistence_stroke`、`contract_stroke`、`core_stroke`、`price_stroke`、`axis_stroke`、`drop_stroke`、`projection_stroke`、`guide_stroke`、`box_stroke` |
| Marker | `eq_marker`、`point_marker`、`kink_marker`、`bliss_marker`、`path_marker`、`core_marker`、`endowment_marker`、`walrasian_marker` |
| Label | `axis_label`、`origin_label`、`title_label`、`box_label`、`effect_label`、`point_label`、`bundle_label`、`bliss_label`、`ic_label`、`edgeworth_label` |
| Fill | `budget_fill` |
| Legend | `legend` |
