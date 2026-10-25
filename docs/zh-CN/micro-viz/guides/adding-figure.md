---
seo_title: "添加图形"
---

# 添加图形

<span id="sec-adding"></span>

要做哪些图由保存库的 issue 与里程碑决定。统计数据图与方块加箭头的流程图不画。添加一张图有五个步骤。

1. **模型。** 把方程序放进 `micro_viz/<主题>.py` 的冻结 dataclass，检查输入并丢出套件错误的子类别，不引入任何绘图套件。
2. **绘图函数。** 写 `micro_viz/visuals/<主题>.py`。`Plane` 收集曲线、辅助线、点、标记、区域与箭头，并给它们稳定的图层编号（`micro.<前缀>.<种类>.<序号>`）。
3. **文本。** 把文本加进 `locale/labels.json` 的三种语言，绘图函数里**不写**显示文本。
4. **导出与范例。** 把名称加进 `micro_viz/__init__.py`、`visuals/__init__.py` 与 `tests/test_package.py`；用 `common.py` 共用的 `parser` 与 `Session` 写 `examples/scripts/<主题>.py`，让范围与选项都是参数。
5. **测试与更新纪录。** 测模型、参数改变时图会跟着变、`title=None` 不画标题、标签找得到空位，以及范例能运行。

```python
from micro_viz.visuals.plane import Plane, linear, sample


def demand_canvas(intercept: float, slope: float, x_max: float, *, title: str | None = None):
    plane = Plane(
        prefix="demo",
        x_label="Q",
        y_label="p",
        x_max=x_max,
        y_max=intercept,
        title=title,
    )
    plane.line(linear(intercept, -slope, x_max), plane.t("monopoly.demand"))
    return plane.finish()
```

## 惯例

- 变动后的曲线是细实线，**不用虚线**。平行移动用直的箭头从旧的点指向新曲线；弯箭头只代表旋转。
- 曲线名称放在线的末端，点标签放在点旁，任何东西都不重叠。
- 移动方向的逻辑放在 `visuals/movement.py`。
- 主题一律白底，随附范例使用 `manual`。

## 检查

```bash
uv run ruff check . && uv run ruff format --check .
uv run mypy
uv run pytest
```
