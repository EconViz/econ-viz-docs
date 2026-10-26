---
seo_title: "添加图形"
---

# 添加图形

<span id="sec-adding"></span>

要画哪些图由保存库的议题与里程碑决定。统计图与会计方块不绘制。添加一张图有五个步骤。

+ *模型。*把方程序放进 `macro_viz/<topic>/models.py` 的冻结 dataclass。检查输入并引发 `ValidationError`。不导入绘图器。
+ *比较。*在 `analysis.py` 加一个 `analyze_*` 函数，回传两个模型与各项变动的方向。
+ *绘图函数。*用 `_theory.py` 的工具写 `macro_viz/visuals/<topic>.py`。里面不写任何显示文本。
+ *文本。*把每个词以稳定的编号（`islm.curve.is`）加入 `locale/labels.json` 的三种语言。
+ *导出、范例与测试。*把名称加进 `visuals/__init__.py`，写一个从 `examples/examples.toml` 读数字的 `examples/scripts/<topic>.py`，并测试模型、参数改变会让图形改变、`title=None` 不画标题，以及没有标签盖到线。

```python
from macro_viz.i18n import Labels
from macro_viz.visuals._theory import (
    curve,
    drop_lines,
    marked_point,
    point_name,
    theory_canvas,
    trim,
)


def demand_canvas(intercept, slope, x_max, *, title=None):
    text = Labels()
    y_max = intercept
    canvas = theory_canvas(
        x_max,
        y_max,
        labels=text,
        x_label_id="keynesian.axis.income",
        y_label_id="keynesian.axis.demand",
        title=title,
    )
    line = [(0.0, intercept), (x_max, intercept - slope * x_max)]
    canvas.extend(
        curve(
            trim(line, x_max, y_max),
            layer_id="macro.demo.demand",
            role="macro.curve.primary",
            label=text("keynesian.curve.demand"),
        )
    )
    return canvas
```

## 理论图工具

<span id="sec-kit"></span>

`macro_viz.visuals._theory` 的工具负责各图共用的部分，每个都有稳定的编号与主题角色。

<!-- api: macro_viz.guides_adding_figure_1 -->

由原点出发、带箭头座标轴与符号轴标题的画布，可加标题。`x_max` 与 `y_max` 是轴长。

<!-- api: macro_viz.guides_adding_figure_2 -->

通过 `points` 的曲线，名称放在右端。角色说明它是什么：`macro.curve.primary` 或 `secondary` 是粗曲线，加上 `.shifted` 后缀就是变动后的细实线。画布会把名称放在末端第一个空的斜角位置：右下、左上、左下、右上。

<!-- api: macro_viz.guides_adding_figure_3 -->

表示平行移动的细实线直线箭头。它从旧均衡出发、结束于新曲线，所以横向移动是水平的，上下移动是垂直的。

<!-- api: macro_viz.guides_adding_figure_4 -->

唯一弯曲的箭头，用于斜率改变：曲率平缓，凹面朝下。弯曲的程度是参数 `BULGE`，以箭头长度的比例表示。

## 惯例

- 变动后的曲线是细实线，不用虚线；平行移动用直线箭头；弯曲箭头只代表转动。
- 点状辅助线把点接到座标轴，轴上的记号标示它的值。
- 只有价格 `p` 用小写；其他变量用大写斜体。缩写与点名保持原有的大小写。
- 没有任何写死的数值：文本来自语系表，数字来自参数，颜色、线宽与字体来自主题。
- 主题一律是白底。范例使用 `manual`。

## 检查

```bash
uv run ruff check . && uv run ruff format --check .
uv run mypy
uv run pytest
```
