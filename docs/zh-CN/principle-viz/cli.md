---
seo_title: "命令行界面"
---

# 命令行界面

<span id="sec-cli"></span>

`principle-viz` 命令在命令行运行本手册中的计算，并以 JSON 打印结果；`--output` 会另外写成文件。此命令不绘图。可将其安装为工具（详见[安装命令行工具](installation.md#sec-install-cli)），或在项目中于命令前加上 `uv run`。

```bash
principle-viz equilibrium \
  --demand-intercept 10 --demand-slope -1 \
  --supply-intercept 2 --supply-slope 1
```

```text
{
  "q_star": 4.0,
  "p_star": 6.0,
  "is_valid_market": true,
  "notes": []
}
```

## 市场参数

多数命令以反函数形式 $p = a + b Q$ 的两条直线描述市场：

<!-- api: agora.principle_viz.cli_1 -->

## 命令

各命令对应的计算与选项如[命令行命令](cli.md#tab-cli)；每个命令的计算说明见对应章节。

<span id="tab-cli"></span>

| 命令 | 计算与其他选项 | 章节 |
| --- | --- | --- |
| `equilibrium` | 线性均衡 | [线性市场](guides/markets.md#sec-markets) |
| `shift` | 比较静态：`--demand-delta-intercept`、`--demand-delta-slope`、`--supply-delta-intercept`、`--supply-delta-slope` | [比较静态](guides/markets.md#sec-shifts) |
| `discrete` | 离散市场：`--demand-values`、`--supply-values`、`--price-rule {midpoint,lower,upper}` | [离散市场](guides/discrete.md#sec-discrete) |
| `elasticity` | 点弹性：`--intercept`、`--slope`、`--quantity`；加上 `--q1`、`--p1` 计算弧弹性 | [弹性与总收益](guides/elasticity.md#sec-elasticity) |
| `revenue` | 弹性与总收益表：`--samples` | [弹性与总收益](guides/elasticity.md#sec-elasticity) |
| `welfare` | 剩余：`--policy {baseline,tax,subsidy,control}` 与该政策的选项 | [福利](guides/welfare.md#sec-welfare) |
| `report-dwl` | 单列无谓损失报表：`--policy {tax,subsidy,control}`、`--csv` | [福利](guides/welfare.md#sec-welfare) |
| `tax` | `--tax-type {fixed,per_unit,ad_valorem}`、`--amount`、`--tax-on {consumer,producer}` | [税收与补贴](guides/taxes.md#sec-taxes) |
| `subsidy` | `--amount`、`--subsidy-to {consumer,producer}` | [税收与补贴](guides/taxes.md#sec-taxes) |
| `controls` | `--control-type {ceiling,floor}`、`--control-price` | [价格管制](guides/controls.md#sec-controls) |
| `trade` | `--world-price`、`--tariff`、`--import-quota`、`--quota-rent-recipient` | [国际贸易](guides/trade.md#sec-trade) |
| `externality` | `--external-cost`、`--external-benefit` | [市场失灵](guides/failures.md#sec-failures) |
| `common-resource` | `--congestion-cost` | [市场失灵](guides/failures.md#sec-failures) |
| `public-good` | `--benefit-intercepts`、`--benefit-slopes`、`--cost-intercept`、`--cost-slope`、`--samples` | [市场失灵](guides/failures.md#sec-failures) |
| `minimum-wage` | `--labor-demand-*`、`--labor-supply-*`、`--minimum-wage` | [劳动与可贷资金](guides/factor-markets.md#sec-factor) |
| `loanable-funds` | `--savings-*`、`--investment-*`、`--savings-shift`、`--investment-shift`、`--government-borrowing` | [劳动与可贷资金](guides/factor-markets.md#sec-factor) |
| `ppf` | `--x-intercept`、`--y-intercept`、`--curvature`、`--x-good`、`--y-good`、`--x-growth`、`--y-growth`、`--samples` | [生产可能性曲线](guides/ppf.md#sec-ppf) |

`principle-viz <command> --help` 列出命令的所有选项。

```bash
principle-viz tax \
  --demand-intercept 10 --demand-slope -1 \
  --supply-intercept 2 --supply-slope 1 \
  --tax-type per_unit --amount 1 --tax-on producer
```

输出包含未征税的均衡（`baseline_equilibrium`）、征税后的均衡（`post_tax`）与各项变动，与 `compare_tax_scenario()` 的返回值相同：本例数量为 3.5，消费者价格 6.5，生产者价格 5.5。
