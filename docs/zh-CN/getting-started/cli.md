---
seo_title: "命令行工具"
description: "用 econ-viz 命令行工具直接在终端产生无差异曲线与预算约束图，不需要写任何 Python。"
---

# 命令行工具

`econ-viz` 内置命令行工具，不写 Python 也能产生图形。

用 `uv tool install econ-viz` 把它安装为全局命令，或在 uv 项目中于每个命令前加上 `uv run`。详见[安装](installation.md)。

## 指令

| 指令 | 说明 |
|---------|-------------|
| `econ-viz help [<command>]` | 显示命令行工具或特定指令的说明 |
| `econ-viz models` | 列出所有支持的效用模型 |
| `econ-viz plot ...` | 产生并导出图形 |
| `econ-viz solve-tex ...` | 以纯 TeX 文本输出马歇尔需求的闭式解 |
| `econ-viz init [path]` | 生成带注释的[配置文件](../guides/config.md)模板（`--force` 覆盖已有文件） |

## 帮助 {#econ-viz-help data-toc-label="帮助"}

```bash
econ-viz help          # 所有命令
econ-viz help plot     # plot 选项
econ-viz help models   # models 选项
```

## 模型 {#econ-viz-models data-toc-label="模型"}

```bash
econ-viz models
```

输出所有模型名称与对应参数。

## 绘图 {#econ-viz-plot data-toc-label="绘图"}

### 选择模型

`--model` 和 `--latex` **择一**提供，不能同时使用。

```bash
# 指定模型名称
econ-viz plot --model cobb-douglas --alpha 0.5 --beta 0.5 ...

# LaTeX 表达式
econ-viz plot --latex "x^{0.4} y^{0.6}" ...
```

### 范例

```bash
# Cobb-Douglas．可行集阴影
econ-viz plot --model cobb-douglas --alpha 0.5 --beta 0.5 \
              --px 2 --py 3 --income 30 \
              --fill --output cobb_douglas.png

# LaTeX 输入．Nord 主题．扩展路径
econ-viz plot --latex "x^{0.4} y^{0.6}" \
              --px 2 --py 3 --income 30 \
              --theme nord --show-ray \
              --output cd_latex.png

# 完全互补．加大画布
econ-viz plot --model leontief --a 1 --b 2 \
              --px 2 --py 3 --income 30 \
              --x-max 20 --y-max 15 \
              --output leontief.png

# CES．只画无差异曲线
econ-viz plot --model ces --rho -0.5 \
              --x-max 20 --y-max 15 --n-curves 6 \
              --no-budget --no-equilibrium \
              --output ces.png

# 饱和（极乐点）
econ-viz plot --model satiation --bliss-x 6 --bliss-y 4 \
              --x-max 12 --y-max 10 \
              --no-budget --no-equilibrium \
              --output satiation.png

# 不加 --output：打开窗口
econ-viz plot --model cobb-douglas --px 2 --py 3 --income 30
```

### 所有选项

| 标志 | 默认值 | 说明 |
|------|---------|-------------|
| `--model`, `-m` | — | 模型名称：`cobb-douglas`、`leontief`、`perfect-substitutes`、`ces`、`satiation` |
| `--latex`, `-l` | — | LaTeX 算式（Cobb-Douglas / 完全互补 / 完全替代） |
| `--px` | — | 商品 x 的价格 |
| `--py` | — | 商品 y 的价格 |
| `--income` | — | 消费者收入 |
| `--alpha` | 0.5 | Alpha 参数（Cobb-Douglas / CES） |
| `--beta` | 0.5 | Beta 参数（Cobb-Douglas / CES） |
| `--a` | 1.0 | a 参数（完全互补 / 完全替代 / 饱和） |
| `--b` | 1.0 | b 参数（完全互补 / 完全替代 / 饱和） |
| `--rho` | 0.5 | 替代参数（CES） |
| `--bliss-x` | 5.0 | 饱和点的 x 坐标（饱和） |
| `--bliss-y` | 5.0 | 饱和点的 y 坐标（饱和） |
| `--x-max` | 10 | 横轴上限 |
| `--y-max` | 10 | 纵轴上限 |
| `--x-label` | `x` | 横轴标签 |
| `--y-label` | `y` | 纵轴标签 |
| `--title` | — | 图形标题 |
| `--theme` | `default` | 配色主题：`default`、`nord` |
| `--config` | — | [配置文件](../guides/config.md)（`econ-viz.toml`）；`--theme` 会替换其中的 `base` |
| `--n-curves` | 5 | 无差异曲线数量 |
| `--dpi` | 300 | 位图输出分辨率 |
| `--fill` | 关闭 | 为预算线下方的可行集加上阴影 |
| `--show-ray` | 关闭 | 画出通过最优点的扩张路径射线 |
| `--no-budget` | 关闭 | 不画预算线 |
| `--no-equilibrium` | 关闭 | 不画均衡点 |
| `--no-curves` | 关闭 | 不画无差异曲线 |
| `--output`, `-o` | — | 输出文件（`.png`、`.pdf`、`.svg`）；省略时会打开交互窗口 |

## 需求公式 {#econ-viz-solve-tex data-toc-label="需求公式"}

只想获得马歇尔需求的闭式解公式、不需要画图时，使用 `solve-tex`。

```bash
# 数值参数
econ-viz solve-tex --model cobb-douglas --alpha 0.4 --beta 0.6

# 符号参数
econ-viz solve-tex --model cobb-douglas --symbolic-params

# 自定义价格与收入符号
econ-viz solve-tex --model leontief --a 2 --b 3 \
                   --px-symbol p_1 --py-symbol p_2 --income-symbol M
```

目前支持闭式解的模型：

- `cobb-douglas`
- `leontief`
- `perfect-substitutes`
- Cobb-Douglas、完全互补与完全替代的 LaTeX 简写

输出是纯 TeX 文本，可以直接贴进 Markdown 数学式、LaTeX 文文件或演示文稿工具。
