---
seo_title: "迁移指南"
description: "principle-econ 已更名为 principle-viz：有哪些变化、如何切换包，以及从 principle-econ 0.1.0 升级时会遇到的行为变化。"
---

# 迁移指南

`principle-econ` 已更名为 **principle-viz**，与 `utility-viz` 一同加入 EconViz 家族。

!!! warning "没有兼容层"

    `principle-econ` 在 v0.1.0 之后不再更新，`principle-viz` 也没有提供 `principle_econ` 兼容包。
    切换时请一并更新导入与命令。

## 变化一览

| | principle-econ | principle-viz |
|---|---|---|
| 发行包 | `uv add principle-econ` | `uv add principle-viz` |
| 导入 | `import principle_econ` | `import principle_viz` |
| 命令行 | `principle-econ` | `principle-viz` |

## 切换包

```bash
uv remove principle-econ
uv add principle-viz
```

接着在代码与脚本中替换名称：

- 所有导入中的 `principle_econ` 改为 `principle_viz`。
- Shell 脚本与 CI 中的 `principle-econ` 改为 `principle-viz`。

!!! tip "模块结构不变"

    `core`、`policy`、`welfare`、`plot`、`api`、`cli` 等子包名称都没有变，
    所以 `principle_econ.core.line` 现在是 `principle_viz.core.line`。

## 0.1.0 之后的行为变化

从 principle-econ 0.1.0 升级，也会一并带来直到 v0.10.0 为止的图形变更。

| 项目 | 变更 |
|---|---|
| 图例 | `MarketFigure.finalize()` 默认不再添加图例；要保留旧行为请传入 `finalize(legend=True)` |
| 福利标签 | 区域改用名称（“消费者剩余”“DWL”等），不再用 `A/B/C/D` 字母 |
| `LabeledRegion` | 以 `key`、`label`、`short_label` 取代 `letter` |
| 曲线名称 | 直接标在曲线末端旁，不再只出现在图例 |
| 依赖包 | 需要 `mosaickit>=0.5.1,<0.6.0`，会自动安装 |

!!! note "计算结果不变"

    福利与均衡的计算结果相同，改变的只有绘图与标注。

## 给贡献者

项目已由 Poetry 改为 uv：`pyproject.toml` 采用 PEP 621 与 `uv_build`，`uv.lock` 取代 `poetry.lock`。
请按[安装](installation.md)中的方式用 `uv sync` 创建环境。
