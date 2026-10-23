---
seo_title: "配置文件"
description: "把 utility-viz 图形的样式存成所有 EconViz 软件包共享的 econ-viz.toml，用 Config 一次加载。"
---

# 配置文件

把颜色、线条、标签与 legend 的设置存成 `econ-viz.toml`，加载一次就好，不用每个方法都传一样的参数。所有 EconViz 软件包都读取同一个文件，并由 mosaickit 统一解析与检查。

## 格式

顶层放置所有 EconViz 软件包共享的配置：`base`、`[font]`、`[fonts]`，以及 `[color]` 中的 `background`、`axis` 与 `label` 颜色。utility-viz 自身的配置放在 `[utility]` 下；其他软件包各有自己的表，例如 `[principle]`，utility-viz 会跳过这些表。表名对应 Theme 的属性，字段名称与样式对象的参数相同。没写到的设置沿用内置默认值。

```toml
# econ-viz.toml
base = "manual"                  # 共享主题

[font]
text = "serif"
math = "fonts/texgyrepagella-math.otf"

[fonts]
serif = ["fonts/NotoSerifSC-Regular.ttf", "fonts/NotoSerifSC-Bold.ttf"]

[color]                          # 各软件包共享
background = "#ffffff"
axis = "#1a1a1a"
label = "#1a1a1a"

[utility.color]
ic = "#2E86AB"
budget = "#6C3483"
equilibrium = "#C0392B"

[utility.stroke.budget]          # theme.budget_stroke
width = 1.5
style = "solid"

[utility.stroke.ic]              # theme.ic_stroke
width = 1.8
opacity = 0.9

[utility.marker.equilibrium]     # theme.eq_marker
size = 5

[utility.label.point]            # theme.point_label
fontsize = 12
position = "top-right"
top = "2pt"

[utility.label.origin]
visible = false

[utility.fill.budget]            # theme.budget_fill
color = "lightgrey"
opacity = 0.3

[utility.legend]                 # theme.legend
position = "auto"
fontsize = 10

[principle]                      # 由 principle-viz 读取
language = "zh-CN"
```

| 表 | 设置的对象 | 字段 |
|------|------------|------|
| `base` | 作为起点的共享主题 | `"manual"`、`"default"`、`"colorblind"`、`"monochrome"`、`"nord"`、`"paper"`、`"presentation"` |
| `[font]` | 正文与数学字体（共享） | `text`（`"sans"`、`"serif"`、`"mono"`）、`math`（数学字体文件） |
| `[fonts]` | 字体文件（共享） | `sans`、`serif`、`mono`：一个文件或文件列表 |
| `[color]` | 共享颜色 | `background`、`axis`、`label` |
| `[utility.color]` | Theme 的颜色，例如 `ic` → `ic_color` | 颜色字符串 |
| `[utility.stroke.<name>]` | `theme.<name>_stroke` | `width`、`style`、`color`、`arrow`、`opacity` |
| `[utility.marker.<name>]` | `theme.<name>_marker` | `color`、`size`、`shape`、`opacity` |
| `[utility.label.<name>]` | `theme.<name>_label` | `text`、`position`、`offset`、`color`、`fontsize`、`visible`、`opacity`、`top`、`bottom`、`left`、`right` |
| `[utility.fill.<name>]` | `theme.<name>_fill` | `color`、`opacity` |
| `[utility.legend]` | `theme.legend` | `position`、`fontsize`、`frame`、`columns`、`visible`、`opacity` |

`eq` 也可以写成 `equilibrium`（`[utility.marker.equilibrium]`、`[utility.color] equilibrium`）。相对路径以配置文件所在文件夹为准。写错时，错误信息会指出文件与表，并提示最接近的名称：

```text
econ-viz.toml: [utility.stroke.budgt] no such setting; did you mean 'budget'? (choose: axis, box, budget, ...)
```

## 主题

`base` 从七个 EconViz 共享主题中选一个。同一名称在 utility-viz、principle-viz 与其他软件包中外观一致：每个主题为各个角色指定颜色，再由各软件包决定元素使用哪个角色。`[utility.*]` 表仍可在其上调整单个元素。

| `base` | 外观 | 用途 |
|--------|------|------|
| `manual` | 白底、黑色坐标轴与点、灰色曲线 | 手册与 playground 的黑白样式，适合打印与讲义 |
| `default` | 色盲友好配色、透明背景 | 日常图形 |
| `colorblind` | 与 `default` 相同的配色 | 需要在名称上明确标示时 |
| `monochrome` | 只用黑色，以线型与标记区分图层 | 黑白打印 |
| `nord` | Nord 冷色系 | 屏幕与幻灯片 |
| `paper` | 柔和颜色、较细线条 | 论文 |
| `presentation` | 颜色更鲜明，线条、标记与标签分别放大为 1.5、1.3 与 1.25 倍 | 投影 |

内置主题不含深色主题：`base = "dark"` 会发出警告并改用 `default`。需要不透明背景时，请设置 `[color] background`。使用 `base = "manual"` 时，无须逐一写出手册的颜色与线宽：

```toml
base = "manual"

[font]
text = "serif"
```

## 微调标签

`top`、`bottom`、`left` 与 `right` 会在标签自动定位之后再移动，位置仍由软件包决定，只做细部调整。在配置文件中，它们为同一类标签设置默认值，单位可用 pt、mm、cm 或 in：

```toml
[utility.label.point]
top = "2pt"
```

在代码中，`Label` 可移动单个标签，距离可为点数，或 `"10pt"`、`"0.5em"`（以标签字号为单位）、`"2mm"` 等字符串，并取代配置文件中该方向的值：

```python
from utility_viz import Label

cvs.add_equilibrium(eq, label=Label(top="10pt"))
cvs.add_point(5, 3, label=Label(text="A", left="6pt"))
```

principle-viz 也支持相同的微调，例如 `MarketFigure(labels={"market.equilibrium": Label(top="4pt")})`。

## 旧版配置文件

为 utility-viz 2.0.0b7 及更早版本编写的配置文件，把 utility-viz 的表放在顶层（`[color] ic`、`[stroke.budget]`、`[legend]` 等）。这类文件在 3.0 之前仍可读取，每次加载会发出一次弃用警告，指出各表的新位置；同一个键同时出现在 `[utility]` 与顶层时，以 `[utility]` 为准。2.0 测试版至 2.0.0b6 使用的 `utility-viz.toml` 也仍可读取，但会发出警告。`utility-viz init --migrate` 会把表移到 `[utility]` 下，并保留注释：

```bash
uv run utility-viz init --migrate
```

有 `utility-viz.toml` 时，会将其改写为 `econ-viz.toml` 并保留旧文件；没有时，则直接改写旧格式的 `econ-viz.toml`。

## 加载

`Config` 把主题与字体选项放在一起。从文件读进来后，可以让它成为之后所有图的默认值，也可以只把它的 `theme` 交给单独一张 `Canvas`。

### 读取配置文件 {#config_load data-toc-label="读取配置文件"}

把一个 TOML 文件读成 `Config`。

<!-- api: config.load -->

??? example "查看示例"

    ```python
    from utility_viz import Config

    config = Config.load("econ-viz.toml")
    theme = config.theme
    ```

### 自动查找 {#config_discover data-toc-label="自动查找"}

依次查找：指定的路径、`econ-viz.toml`、较旧的 `utility-viz.toml`（会发出警告）、内置默认值。和 `Config.load` 不同的是，找不到文件时不会出错。

<!-- api: config.discover -->

??? example "查看示例"

    ```python
    from utility_viz import Config

    # 找不到文件时回到内置默认值
    config = Config.discover()
    ```

### 应用 {#config_use data-toc-label="应用"}

让这份 `Config` 成为之后创建的图的默认值，并返回它自己。只想影响单独一张图时，把它的 `theme` 传给 `Canvas(theme=...)`。

<!-- api: config.use -->

??? example "查看示例"

    ```python
    from utility_viz import Canvas, Config

    # 之后创建的图
    Config.load("econ-viz.toml").use()
    # 应用配置文件
    Canvas(x_max=20, y_max=15)

    theme = Config.load("econ-viz.toml").theme
    # 或只应用于这张图
    Canvas(theme=theme)
    ```

### 还原 {#config_reset data-toc-label="还原"}

回到内置默认值。`Config.active()` 可以查看当前使用的是哪一份 `Config`。

<!-- api: config.reset -->

<!-- api: config.active -->

??? example "查看示例"

    ```python
    from utility_viz import Config

    # 回到内置默认值
    Config.reset()
    ```

方法显式传入的参数仍然优先于配置文件：以上面的设置为例，`add_budget(..., stroke=Stroke(width=1))` 会画出 1 pt 粗、其余沿用配置文件样式的线。

## 命令行

`utility-viz init` 会生成一份带注释的模板，列出所有可以设置的名称；`utility-viz plot` 则通过 `--config` 读取同一份配置文件：

```bash
uv run utility-viz init                       # 生成 econ-viz.toml
uv run utility-viz plot --model cobb-douglas --px 2 --py 3 --income 30 \
    --config econ-viz.toml --output cd.png
```

`mosaickit.econ_toml.use("econ-viz.toml")` 会一次为所有已安装的 EconViz 软件包加载此文件。
