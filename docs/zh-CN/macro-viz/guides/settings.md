---
seo_title: "设置"
---

# 设置

<span id="sec-settings"></span>

`macro-viz` 读取共用的 `econ-viz.toml`。`mosaickit` 负责解析并检查文件；`macro-viz` 只声明 `[macro]` 之下接受哪些项目。

<!-- api: macro_viz.guides_settings_1 -->

没有写的键保留内置缺省，完全没有文件时，图形使用内置的颜色。

```python
from macro_viz import Config

Config.load("econ-viz.toml").use()
```

```toml
base = "manual"            # 共用外观：白底黑线

[font]
text = "serif"
math = "texgyrepagella-math.otf"

[fonts]
serif = ["texgyrepagella-regular.otf", "texgyrepagella-italic.otf"]

[macro]
language = "en"            # en, zh-TW 或 zh-CN

[macro.stroke]
curve = 3.5                # 点

[macro.text]
scale = 1.5                # 所有文本大小的倍数
```

这些页面的图形由 `config/econ-viz.toml`、`config/econ-viz.zh-TW.toml` 与 `config/econ-viz.zh-CN.toml` 画出（[下载示例](#sec-download)），三者只有字体与语言不同。

## 共用的键

`base`、`[font]`、`[fonts]`、`background`、`axis` 与 `label` 由所有 EconViz 软件包共用，说明见 `mosaickit`。没有深色主题：背景一律是白色。

## `[macro]` 各表

<span id="sec-macro-tables"></span>

<span id="tab-macro"></span>

| 键 | 意义 | 默认值 |
| --- | --- | --- |
| `palette` | 只用于 macro-viz 的色彩模型；优先于 `base` | base 的设置 |
| `language` | 内置图形文本的语言：`en`、`zh-TW` 或 `zh-CN` | `en` |
| `color.<role>` | 角色的颜色：`background`、`axis`、`label`、`primary`、`secondary`、`tertiary` | 主题的设置 |
| `stroke.curve` | 粗理论曲线的线宽（点） | 3.5 |
| `stroke.shifted` | 变动后曲线的线宽（细实线） | 1.0 |
| `stroke.arrow` | 移动箭头的线宽（实线，比曲线细） | 1.0 |
| `stroke.guide` | 点状辅助线的线宽 | 1.0 |
| `stroke.line45` | 单面板图形中 45 度线的线宽 | 0.8 |
| `stroke.diagonal` | 连动面板中 45 度线的线宽 | 0.6 |
| `stroke.link` | 连动面板之间虚线投影的线宽 | 0.7 |
| `marker.point` | 均衡点圆点的直径（点） | 6.5 |
| `text.scale` | 所有文本大小的倍数 | 1.0 |
| `label.<group>.<side>` | 移动一组标签（参见 [缺省移动标签](labels.md#sec-nudges)） | 无 |

颜色指定主题的角色，所以 `manual` 是黑白，彩色主题则有颜色。变动后的曲线一律是细实线，平行移动是直线箭头，弯曲箭头只代表转动；设置可以改线宽，但不会改这些惯例。

## 代码中的主题

<!-- api: macro_viz.guides_settings_2 -->

`get_theme(name)` 依共用主题名称（如 `"manual"`）建出 `mosaickit` 主题，包含 macro 的各个角色（`macro.curve.primary`、`macro.curve.primary.shifted`、`macro.movement`、`macro.point`、`macro.guide` 等）。`list_themes()` 列出名称。`MANUAL_THEME` 是黑白主题。

```python
from macro_viz.themes import MANUAL_THEME, list_themes

list_themes()
MANUAL_THEME.resolve("macro.movement", fallback_category="path").stroke
```

<span id="sec-download"></span>

## 示例

示例压缩包包含 `examples/scripts/<topic>/*.py`、示例数字 `examples.toml` 与三份配置文件。每个脚本都接受 `--output`、`--config`、`--data` 与 `--suffix`；`--help` 会列出。脚本里没有写死任何数字：数字来自 `examples.toml`。

<div class="ev-downloads"><a class="ev-download" href="../../../assets/macro-viz/macro-viz-examples.zip" download aria-label="下载范例"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载示例</span></a></div>

```bash
uv run python examples/scripts/islm/islm.py --output out --config examples/econ-viz.toml
```
