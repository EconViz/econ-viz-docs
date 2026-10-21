---
seo_title: "样式与颜色"
---

# 样式与颜色

<span id="sec-styles"></span>

## 稀疏样式

每个样式都是冻结的 dataclass，且所有字段都可以是 `None`。`None` 表示继承：字段值取自优先级较低的样式（详见[主题与配置](themes.md#sec-themes)）。假值不等于 `None`，因此 `opacity=0`、`width=0` 与 `LegendStyle(visible=False)` 都是明确的覆盖。

<span id="def-merge"></span>

!!! abstract "定义 · 稀疏合并"

    设 $a$、$b$ 为同类型、字段集合为 $F$ 的样式。样式 $a \triangleright b$（`a.merged_over(b)`）对每个 $\phi \in F$ 满足

    $$
    (a \triangleright b)_\phi = \begin{cases}\begin{aligned}a_\phi & \text{if} a_\phi \ne \text{None}\end{aligned} \\\ \begin{aligned}b_\phi & \text{otherwise}.\end{aligned}\end{cases}
    $$

    空样式 $\epsilon$ 的每个字段都是 `None`。样式组逐槽合并，`None` 槽视同 $\epsilon$。

<span id="prop-monoid"></span>

!!! abstract "命题 · 合并构成幺半群"

    对同类型的样式 $a, b, c$，
    (i) 结合律为

    $$
    (a \triangleright b) \triangleright c = a \triangleright (b \triangleright c);
    $$

    (ii) 空样式是单位元，

    $$
    \epsilon \triangleright a = a \triangleright \epsilon = a;
    $$

    (iii) 合并具有幂等性，

    $$
    a \triangleright a = a.
    $$

    逐栏来看，$a_1 \triangleright \cdots \triangleright a_n$ 取第一个不是 `None` 的值。

因此，多个样式无论如何分组合并，结果都相同。可以将它们视为一份优先级列表：某字段的值取自第一个设置该字段的来源。

<!-- api: agora.mosaickit.guides_styles_1 -->

[稀疏合并](styles.md#def-merge)的合并。不同类型的样式引发 `TypeError`。

## 样式类型

<!-- api: agora.mosaickit.guides_styles_2 -->

线条样式。`width` 以点为单位；`dash` 为 `DashStyle`（`SOLID`、`DASHED`、`DOTTED`、`DASHDOT`）；`arrow` 为 `ArrowStyle`（`OPEN`、`TRIANGLE`、`FANCY`、`WEDGE`），画在图层的 `ArrowPlacement`（`START`、`END`、`BOTH`）处。

<!-- api: agora.mosaickit.guides_styles_3 -->

`Stroke` 的线条类型；也接受简写 `-`、`--`、`:` 与 `-.`。

<!-- api: agora.mosaickit.guides_styles_4 -->

`Stroke` 的箭头样式。`SIMPLE` 是 `OPEN` 的另一个名称，也接受 Matplotlib 写法 `->` 与 `-|>`。

<!-- api: agora.mosaickit.guides_styles_5 -->

图层的箭头画在哪里。

<!-- api: agora.mosaickit.guides_styles_6 -->

区域内部的填色样式；`hatch` 为 Matplotlib 的填充图案，例如 `"//"`，`""` 表示无填充图案。

<!-- api: agora.mosaickit.guides_styles_7 -->

点标记样式。`size` 是以平方点计的面积，与 Matplotlib 的 `scatter` 相同（36 对应 6 pt 圆点）；`shape` 为 Matplotlib 标记，例如 `"o"`、`"s"` 或 `"X"`。

<!-- api: agora.mosaickit.guides_styles_8 -->

文字样式。`size` 以點为单位，`font` 是通用字体（`"sans"`、`"serif"` 或 `"mono"`，见[字体](styles.md#sec-fonts)），`weight` 是 1 到 1000 的整数、`"normal"` 或 `"bold"`，`rotation` 为逆时针旋转的角度（度）。`family`（字体家族名称）仍可用但已弃用：它走 Matplotlib 绘制，不经过 `glyphkit`，1.0 会移除。

## 字体

<span id="sec-fonts"></span>

文字由 `glyphkit` 依字体文件排版。三种通用字体指向字体文件：`"sans"`（默认）、`"serif"` 与 `"mono"`。MosaicKit 默认用 DejaVu Sans、DejaVu Serif 与 DejaVu Sans Mono，也就是 Matplotlib 附的文件。它*不会搜索系统字体*，其他字体一律要自己给文件。

<!-- api: agora.mosaickit.guides_styles_9 -->

取代通用字体的字体文件。每个字段可给一个文件或一个列表；需要的字面都要列出，例如常规与粗体两个文件。样式的 `weight` 会选最接近的字面，文件顺序则是第一个文件缺字时依次尝试的顺序。没给的字段沿用 DejaVu 默认。

<!-- api: agora.mosaickit.guides_styles_10 -->

OpenType 数学字体，如 STIX Two Math、Libertinus Math 或 Fira Math，文件要有 `MATH` 表。`italic` 让单个拉丁字母与小写希腊字母用斜体字母表，和 TeX 一樣。没有数学字体时，`$...$` 内的数学式由 Matplotlib 排版。

```python
from mosaickit import (
    Canvas,
    CanvasSpec,
    Config,
    MathFont,
    TextFonts,
    TextLayer,
    TextStyle,
    use_config,
)

fonts = TextFonts(
    serif=[
        "fonts/Pagella-Regular.otf",
        "fonts/Pagella-Bold.otf",
    ]
)
config = Config(
    fonts=fonts, math_font=MathFont("fonts/Pagella-Math.otf")
)

with use_config(config):
    canvas = Canvas(CanvasSpec(x_range=(0, 1), y_range=(0, 1)))
    canvas.add(
        TextLayer(
            (0.5, 0.5),
            "$u = x^{0.5}$",
            style=TextStyle(font="serif"),
        )
    )
```

TikZ 渲染器把 `sans`、`serif`、`mono` 对应到 `\sffamily`、`\rmfamily` 与 `\ttfamily`。

<!-- api: agora.mosaickit.guides_styles_11 -->

图例：Matplotlib 的位置名称，例如 `"best"` 或 `"upper right"`、外框，以及字号。

大小、宽度与不透明度在创建样式时检查：大小必须为有限非负数，不透明度在 $[0, 1]$ 内，旋转角度必须有限。

<span id="tab-primitive"></span>

| 样式 | 值 |
| --- | --- |
| `Stroke` | `grey-800`、宽 1.5、实线、不透明度 1 |
| `Fill` | `grey-200`、不透明度 0.3、无填充图案 |
| `Marker` | `grey-800`、大小 36、`"o"`、不透明度 1、边框 `grey-800` 宽 0 |
| `TextStyle` | `grey-900`、12 pt、DejaVu Sans、一般字重、不透明度 1、不旋转 |
| `LegendStyle` | 显示、位置 `"best"`、无外框、10 pt |

## 颜色

<!-- api: agora.mosaickit.guides_styles_12 -->

不可变的 RGBA 颜色，各通道在 $[0, 1]$ 内。`channels` 返回四个值，`from_channels()` 创建颜色，`to_hex(include_alpha=None)` 写出 `#RRGGBB`，当 `include_alpha` 为真、或默认情况下 alpha 不为 1 时加上 `AA`。`TRANSPARENT` 为 `Color(0, 0, 0, 0)`。

<span id="prop-hex"></span>

!!! abstract "命题 · 十六进制往返"

    对每个由十六进制数字组成、形如 `#RRGGBB` 或 `#RRGGBBAA` 的字符串 $h$，`Color.from_hex(h).to_hex(include_alpha=len(h) == 9)` 等于 $h$ 的大写形式。三位数的 `#RGB` 读作 `#RRGGBB`。

样式的 `color` 或 `edge_color` 接受 `Color`、`"#hex"` 字符串（立即解析），或其他任何字符串，后者保留为*调色板名称*。

## 调色板

<!-- api: agora.mosaickit.guides_styles_13 -->

命名的颜色表。值可以是 `Color` 或十六进制字符串；`palette[name]` 查询颜色，名称不存在时引发指出该调色板的 `ConfigurationError`，`name in palette` 检查名称是否存在。

<span id="tab-palette"></span>

| 名称 | 值 | 默认主题中的用途 |
| --- | --- | --- |
| `grey-900` | `#222222` | 文字 |
| `grey-800` | `#333333` | 线条、标记、坐标轴 |
| `grey-600` | `#666666` | 坐标轴注释 |
| `grey-400` | `#999999` | 辅助线 |
| `grey-200` | `#CCCCCC` | 填色 |
| `grey-100` | `#E6E6E6` |  |
| `white` | `#FFFFFF` | 画布背景 |
| `blue` | `#01A2D9` | `primary` |
| `red` | `#E3120B` | `secondary` |
| `teal` | `#00887D` | `accent` |

主题与样式以名称引用颜色，画布创建渲染计划时才在生效的调色板（`Config.palette`）中查询，因此渲染器只会收到具体颜色。在调色板中改一次颜色，所有引用它的角色都随之改变。调色板缺少的名称在绘制时引发 `ConfigurationError`，信息指明角色、样式字段与调色板。Python 的 `Palette` 会取代默认调色板，因此应从 `DEFAULT_PALETTE.colors` 创建，以保留内置主题所用的名称：

```python
from mosaickit import (
    DEFAULT_PALETTE,
    Canvas,
    Config,
    Palette,
    use_config,
)

brand = Palette(
    "brand", {**DEFAULT_PALETTE.colors, "blue": "#0072B2"}
)
with use_config(Config(palette=brand)):
    # primary now draws in #0072B2
    canvas = Canvas()
```
