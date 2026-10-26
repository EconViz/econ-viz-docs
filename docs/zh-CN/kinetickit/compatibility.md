---
seo_title: "兼容性"
---

# 兼容性

<span id="sec-compatibility"></span>

## 支持的平台

- Python 3.10、3.11、3.12 与 3.13。
- 基本安装包含 NumPy 与 GlyphKit。`raster` 与 `interactive` 是选用的额外安装项，它们的第三方引擎属于私有的实现细节。

## 稳定的接口（1.0）

| 接口 | 导入路径 |
| --- | --- |
| 时间轴、补间、关键帧、调度器 | `kinetickit.timeline`、`.tween`、`.keyframes`、`.scheduler`、`.easing`、`.interpolation` |
| 2D 与 3D 场景契约 | `kinetickit.scene`、`.geometry`、`.styles` |
| 变形与转场 | `kinetickit.morph`、`.transitions` |
| 绘图端与导出器协定 | `kinetickit.renderers`（`Renderer`、`RendererCapabilities`、`register_renderer`）、`kinetickit.exporters`（`Destination`、`ExportManifest`、`register_exporter`） |
| 交互与无障碍 | `kinetickit.interaction`、`.accessibility` |
| 排版端口与文本素材 | `kinetickit.typography` |
| 一致性测试数据 | `kinetickit.conformance` |

公开软件包 `__all__` 导出的一切都是公开的。以底线开头的名称，以及名称以底线开头的模块（`_matplotlib`、`_plotly`、`_gif_stream`）里的一切，都是私有的，随时可能改变。可视化的语义不在范围内。

## 版本

KineticKit 从 1.0 起遵循语义化版本。预发行版本（`1.0.0bN`、`1.0.0rcN`）可能在版本之间改变公开契约，每项变更都会记录在变更记录中。

## 弃用

1. 被弃用的公开名称至少再维持一个次要版本。
2. 它会发出 `DeprecationWarning`，指出替代名称与移除的版本。
3. 移除会记录在变更记录中。
4. 被弃用的名称只会在主要版本移除。

输出格式遵守同样的规则。会改变既有成品的变更（例如 SVG 的结构）会出现在变更记录中，并在同一次提交更新黄金文件。
