---
seo_title: "命令行工具"
---

# 命令行工具

<span id="sec-cli"></span>

命令行工具可绘图、批量处理及输出需求公式。以 `uv tool install utility-viz` 安装为独立工具，或在 `uv` 项目中于命令前加上 `uv run`（详见[安装命令行工具](installation.md#sec-install-cli)）。由 `econ-viz` 兼容包安装的 1.x 命令 `econ-viz` 在 2.x 仍可使用：它会发出弃用警告，再以相同参数运行 `utility-viz`（详见[从 `econ-viz` 迁移](installation.md#sec-migrate)）。

| 命令 | 说明 |
| --- | --- |
| `utility-viz help [``command``]` | 显示命令行工具或特定命令的说明 |
| `utility-viz models` | 列出所有支持的效用模型 |
| `utility-viz plot ...` | 生成并导出图形 |
| `utility-viz solve-tex ...` | 以 TeX 格式输出 Marshall 需求的闭式解 |
| `utility-viz init [path]` | 创建 `utility-viz.toml` 配置模板 |

## 说明与模型

<!-- api: agora.utility_viz.getting_started_cli_1 -->

未指定参数时列出所有命令；指定命令名称时显示该命令的选项。

```bash
utility-viz help          # 所有命令
utility-viz help plot     # plot 选项
utility-viz help models   # models 选项
```

<!-- api: agora.utility_viz.getting_started_cli_2 -->

列出命令行接口支持的模型名称与参数。`--model` 使用 kebab-case 名称，与 Python 类名称不同（参见[命令行模型](cli.md#tab-models)）。参数选项详见[绘图](cli.md#sec-cli-plot)。

<span id="tab-models"></span>

| 模型 | `--model` 值 | 必要参数 | 可选参数 |
| --- | --- | --- | --- |
| Cobb-Douglas | `cobb-douglas` | `alpha`、`beta` | -- |
| CES | `ces` | `rho` | `alpha`、`beta` |
| 完全互补 | `leontief` | `a`、`b` | -- |
| 完全替代 | `perfect-substitutes` | `a`、`b` | -- |
| 饱和偏好 | `satiation` | `bliss-x`、`bliss-y` | `a`、`b` |
| 准线性 | `quasi-linear` | -- | `v-func`、`linear-in` |
| Stone-Geary | `stone-geary` | -- | `alpha`、`beta`、`bar-x`、`bar-y` |
| Translog | `translog` | -- | `alpha-0`、`alpha-x`、`alpha-y`、`beta-xx`、`beta-yy`、`beta-xy` |

## 绘图

<span id="sec-cli-plot"></span>

<!-- api: agora.utility_viz.getting_started_cli_3 -->

使用 `--model` 指定模型，或使用 `--latex` 输入效用函数，两者择一。指定 `--output` 时导出文件，省略时打开交互窗口。

预算线与均衡点需要完整的价格与收入。`--no-budget`、`--no-equilibrium`、`--no-curves` 可分别省略对应图层，且可并用（参见[图层控制选项](cli.md#tab-plot-flags)）。

<span id="tab-plot-flags"></span>

| 情况 | 结果 |
| --- | --- |
| 提供完整 `--px`、`--py`、`--income` | 绘制预算线并求解均衡 |
| 省略任一价格或收入 | 仅绘制无差异曲线，不画预算线与均衡点 |
| 加上 `--no-equilibrium` | 跳过求解与均衡标注，即使提供了价格与收入 |
| 加上 `--no-budget` | 隐藏预算线，即使提供了价格与收入 |
| `--no-curves` 搭配完整价格与收入 | 只呈现预算线与均衡点，不画无差异曲线 |

```bash
# 指定模型名称
utility-viz plot --model cobb-douglas --alpha 0.5 --beta 0.5 ...

# LaTeX 表达式
utility-viz plot --latex "x^{0.4} y^{0.6}" ...
```

```bash
# Cobb-Douglas 并为可行集合加阴影
utility-viz plot --model cobb-douglas --alpha 0.5 --beta 0.5 \
              --px 2 --py 3 --income 30 \
              --fill --output cobb_douglas.png

# 用 LaTeX 与 Nord 主题画扩张路径
utility-viz plot --latex "x^{0.4} y^{0.6}" \
              --px 2 --py 3 --income 30 \
              --theme nord --show-ray \
              --output cd_latex.png

# 完全互补并放大画布
utility-viz plot --model leontief --a 1 --b 2 \
              --px 2 --py 3 --income 30 \
              --x-max 20 --y-max 15 \
              --output leontief.png

# CES 只画无差异曲线
utility-viz plot --model ces --rho -0.5 \
              --x-max 20 --y-max 15 --n-curves 6 \
              --no-budget --no-equilibrium \
              --output ces.png

# 饱和效用与饱和点
utility-viz plot --model satiation --bliss-x 6 --bliss-y 4 \
              --x-max 12 --y-max 10 \
              --no-budget --no-equilibrium \
              --output satiation.png

# 不加 --output 就打开窗口
utility-viz plot --model cobb-douglas --px 2 --py 3 --income 30
```

### 选择模型

### 价格与收入

### 模型参数

准线性、Stone-Geary 与 Translog 另有下列选项，可按模型使用：

```bash
utility-viz plot --model stone-geary --bar-x 2 --bar-y 2 \
              --px 2 --py 3 --income 30 \
              --x-max 20 --y-max 15 --output stone_geary.png
```

此例的最低消费支出为 $2 \times 2 + 3 \times 2 = 10$，收入 $30$ 高于此限制。若将收入改为 $10$ 或更低，求解会因不符合模型定义域而失败。

### 画布与图层

批量生成图形时，为每组参数指定不同文件名，并先创建输出目录。`--x-max` 与 `--y-max` 不会随价格自动调整；轴截距或最优点超出范围时，应同步增大画布上限。

## 创建配置文件

<span id="sec-cli-init"></span>

<!-- api: agora.utility_viz.getting_started_cli_4 -->

创建带注释的 `utility-viz.toml` 模板。省略路径时写入当前目录；文件已存在时，必须使用 `--force` 才会覆盖。`--migrate` 则改为从同一目录中旧的 `econ-viz.toml` 创建 `utility-viz.toml`，并保留旧文件。

```bash
utility-viz init
utility-viz init config/figures.toml
utility-viz init --migrate
utility-viz plot --config utility-viz.toml --model cobb-douglas \
              --px 2 --py 3 --income 30 --output figure.png
```

## 需求公式

<!-- api: agora.utility_viz.getting_started_cli_5 -->

以 TeX 格式输出 Marshall 需求的闭式解，可用于支持 TeX 数学式的文件。

```bash
# 数值参数
utility-viz solve-tex --model cobb-douglas --alpha 0.4 --beta 0.6

# 符号参数
utility-viz solve-tex --model cobb-douglas --symbolic-params

# 自定义价格与收入符号
utility-viz solve-tex --model leontief --a 2 --b 3 \
                   --px-symbol p_1 --py-symbol p_2 --income-symbol M
```

支持 `cobb-douglas`、`leontief`、`perfect-substitutes` 及其 LaTeX 表达式。此命令只输出公式文字，不生成图像文件。
