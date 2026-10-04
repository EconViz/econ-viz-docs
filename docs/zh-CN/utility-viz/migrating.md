---
seo_title: "从 econ-viz 迁移"
description: "econ-viz 在 2.0 更名为 utility-viz：有哪些变化、该安装哪个包，以及兼容层在 3.0 之前如何工作。"
---

# 从 econ-viz 迁移

`econ-viz` 在 2.0.0 更名为 **utility-viz**。

!!! warning "utility-viz 2.0 目前处于 Beta 阶段"

    2.0.0b1 是预发布版本（pre-release）。在 2.0 正式版发布之前，稳定版仍是 `econ-viz` 1.x。
    安装预发布版本需要加上 `--pre`，例如 `pip install --pre utility-viz`。

## 变化一览

| | 1.x | 2.x |
|---|---|---|
| 发行包 | `pip install econ-viz` | `pip install utility-viz` |
| 导入 | `import econ_viz` | `import utility_viz` |
| 命令行 | `econ-viz` | `utility-viz` |
| 配置文件 | `econ-viz.toml` | `utility-viz.toml`（段名不变） |

## 该安装哪个包

`utility-viz` 只包含 `utility_viz` 与 `utility-viz` 命令，不含 `econ_viz` 包，也没有 `econ-viz` 命令。

`econ-viz` 2.x（版本号相同）是一个轻量的兼容发行包。执行 `pip install econ-viz` 会安装同版本的 `utility-viz`，
再加上 `econ_viz` 包和 `econ-viz` 命令，二者都会提示已被弃用。因此，用
`pip install --upgrade econ-viz` 升级现有的 1.x 环境仍可正常工作，并会把你带到 2.x。
预发布版本需要加上 `--pre`，例如 `pip install --pre --upgrade econ-viz`。

准备好不再依赖兼容层时，再改装 `pip install utility-viz` 即可。

## 兼容层

在整个 2.x 期间，`econ-viz` 发行包都会提供 `econ_viz` 包与 `econ-viz` 命令，让文档中记载的 1.x 代码继续可用：

- `import econ_viz` 每个进程只会发出一次弃用警告。
- `from econ_viz import ...` 以及文档中记载的子模块（`econ_viz.models`、`econ_viz.optimizer`、
  `econ_viz.themes` 等）会对应到 `utility_viz` 中的同名项；名称没有变化的，就是同一个对象。
- 创建 `econ_viz.Canvas`、`econ_viz.Figure` 或 `econ_viz.animation.Animator`，或访问 `econ_viz.Layout` 时，
  会发出 `utility_viz.UtilityVizDeprecationWarning`（属于 `FutureWarning`），消息会注明
  “deprecated since 2.0.0, removed in 3.0.0” 以及替代写法。`Figure`、`Layout` 和 `Animator` 会对应到 2.x 现有的
  等价对象；它们的声明式替代方案（`CanvasGrid`、`Animation`）尚在规划中，消息中也会如此标明。
- 配置文件的查找顺序：显式指定的路径、`utility-viz.toml`、旧版 `econ-viz.toml`（会发出警告），最后是默认值。
  两个文件同时存在时，以新文件为准，并以警告提示旧文件已被忽略。
  不带参数的 `Config.load()` 按上述文件顺序查找，两个文件都不存在时会抛出错误（与 1.x 相同）；
  `Config.discover()` 则会回退到默认值；`Config.load("file.toml")` 只读取该文件。
  未指定 `--config` 时，`utility-viz plot` 会在当前目录应用相同的查找顺序。
- `econ-viz` 命令会打印弃用警告，然后转交给 `utility-viz` 执行。
- `utility-viz init --migrate` 会根据 `econ-viz.toml` 生成 `utility-viz.toml`，并保留旧文件。

## 移除时间表（3.0.0）

`econ_viz` 包、`econ-viz` 命令和 `econ-viz.toml` 的查找功能会在 3.0.0 移除，而不是 2.0.0。

兼容范围仅限文档中记载的 1.x 公开 API。未记载的深层模块路径（例如 `econ_viz.canvas.renderers.*`）
只会尽力对应，随时可能消失。`utility_viz.core.*` 内部模块属于高级 API，不在兼容保证之内。
