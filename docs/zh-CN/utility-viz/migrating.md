---
seo_title: "迁移指南"
description: "econ-viz 在 2.0 更名为 utility-viz：有哪些变化、该安装哪个包，以及兼容层在 3.0 之前如何工作。"
---

# 迁移指南

`econ-viz` 在 2.0.0 更名为 **utility-viz**。

!!! warning "utility-viz 2.0 目前处于 Beta 阶段"

    2.0.0b8 是预发布版本（pre-release）。在 2.0 正式版发布之前，稳定版仍是 `econ-viz` 1.x。
    安装预发布版本需要加上 `--prerelease allow`，例如 `uv add --prerelease allow utility-viz`。

## 变化一览

| | 1.x | 2.x |
|---|---|---|
| 发行包 | `uv add econ-viz` | `uv add utility-viz` |
| 导入 | `import econ_viz` | `import utility_viz` |
| 命令行 | `econ-viz` | `utility-viz` |
| 配置文件 | `econ-viz.toml` | `econ-viz.toml`，由所有 EconViz 软件包共享 |
| 配置文件格式 | `[color]`、`[stroke.*]`、`[legend]` 等位于顶层 | utility-viz 的表位于 `[utility]` 下；`base`、`[font]`、`[fonts]` 与共享颜色位于顶层 |

## 该安装哪个包

| 包 | 安装内容 |
|---|---|
| `utility-viz` | `utility_viz` 与 `utility-viz` 命令 |
| `econ-viz` 2.x | 同版本的 `utility-viz`，加上已弃用的 `econ_viz` 包与 `econ-viz` 命令 |

`econ-viz` 2.x 是轻量的兼容发行包，版本号与 `utility-viz` 相同。
因此升级现有的 1.x 环境仍可正常工作，并会把你带到 2.x：

```bash
uv add --upgrade-package econ-viz econ-viz
```

!!! tip "准备好不再依赖兼容层？"

    改装 `uv add utility-viz` 即可。要安装预发布版本时，两个命令都要加上 `--prerelease allow`。

## 兼容层

在整个 2.x 期间，文档中记载的 1.x 代码都能通过 `econ-viz` 发行包继续使用。

| 项目 | 行为 |
|---|---|
| `import econ_viz` | 每个进程发出一次弃用警告 |
| `from econ_viz import ...` 与文档记载的子模块 | 对应到 `utility_viz` 中的同名项目 |
| `Canvas`、`Figure`、`Animator`、`Layout` | 发出 `UtilityVizDeprecationWarning` |
| `econ-viz` 命令 | 发出警告，再转交给 `utility-viz` |

- 名称没有变化的项目，与 `utility_viz` 中的是同一个对象。
- 警告属于 `FutureWarning`，内容为“deprecated since 2.0.0, removed in 3.0.0”，并注明替代写法。
- `Figure`、`Layout` 与 `Animator` 会对应到 2.x 现有的等价对象。

!!! note "声明式替代方案尚在规划中"

    `CanvasGrid` 与 `Animation` 是 `Figure` 与 `Animator` 的规划替代方案，警告消息中也会标示为规划中。

### 配置文件查找

配置文件按下列顺序查找：

1. 显式指定的路径。
2. `econ-viz.toml`。
3. `utility-viz.toml`（2.0 测试版至 2.0.0b6 使用的名称，会发出警告）。
4. 默认值。

!!! warning "两个文件同时存在"

    以 `econ-viz.toml` 为准，并以警告提示 `utility-viz.toml` 已被忽略。

| 调用 | 行为 |
|---|---|
| `Config.load()` | 按上述顺序查找；两个文件都不存在时会抛出错误（与 1.x 相同） |
| `Config.discover()` | 按上述顺序查找；找不到时回退到默认值 |
| `Config.load("file.toml")` | 只读取该文件 |

未指定 `--config` 时，`utility-viz plot` 会在当前目录应用相同的查找顺序。

### 迁移配置文件

```bash
utility-viz init --migrate
```

1.x 与 2.0.0b7 及更早版本的配置文件，把 utility-viz 的表放在顶层。这类文件仍可读取，每次加载会发出一次 `UtilityVizDeprecationWarning`；同一个键同时出现在 `[utility]` 与顶层时，以 `[utility]` 为准。`utility-viz init --migrate` 会把表移到 `[utility]` 下并保留注释：有 `utility-viz.toml` 时，将其改写为 `econ-viz.toml` 并保留旧文件；没有时，则直接改写旧格式的 `econ-viz.toml`。

```toml
# 旧格式
[color]
ic = "#2E86AB"

# 新格式
[utility.color]
ic = "#2E86AB"
```

完整格式请参阅[配置文件](guides/config.md)。

## 移除时间表

兼容层会在 3.0.0 移除，而不是 2.0.0。

| 3.0.0 移除项目 |
|---|
| `econ_viz` 包 |
| `econ-viz` 命令 |
| `utility-viz.toml` 查找 |
| `econ-viz.toml` 顶层的 utility-viz 表 |

!!! info "兼容保证的范围"

    - **在保证内：** 文档中记载的 1.x 公开 API。
    - **尽力对应：** 未记载的深层模块路径，例如 `econ_viz.canvas.renderers.*`，随时可能消失。
    - **不在保证内：** 内部的 `utility_viz.core.*` 模块，属于高级 API。
