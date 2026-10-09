---
seo_title: "命令列介面"
---

# 命令列介面

<span id="sec-cli"></span>

`principle-viz` 指令在命令列執行本手冊中的計算，並以 JSON 印出結果；`--output` 會另外寫成檔案。此指令不繪圖。可將其安裝為工具（詳見[安裝命令列工具](installation.md#sec-install-cli)），或在專案中於指令前加上 `uv run`。

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

## 市場參數

多數指令以反函數形式 $p = a + b Q$ 的兩條直線描述市場：

<!-- api: agora.principle_viz.cli_1 -->

## 指令

各指令對應的計算與選項如[命令列指令](cli.md#tab-cli)；每個指令的計算說明見對應章節。

<span id="tab-cli"></span>

| 指令 | 計算與其他選項 | 章節 |
| --- | --- | --- |
| `equilibrium` | 線性均衡 | [線性市場](guides/markets.md#sec-markets) |
| `shift` | 比較靜態：`--demand-delta-intercept`、`--demand-delta-slope`、`--supply-delta-intercept`、`--supply-delta-slope` | [比較靜態](guides/markets.md#sec-shifts) |
| `discrete` | 離散市場：`--demand-values`、`--supply-values`、`--price-rule {midpoint,lower,upper}` | [離散市場](guides/discrete.md#sec-discrete) |
| `elasticity` | 點彈性：`--intercept`、`--slope`、`--quantity`；加上 `--q1`、`--p1` 計算弧彈性 | [彈性與總收益](guides/elasticity.md#sec-elasticity) |
| `revenue` | 彈性與總收益表：`--samples` | [彈性與總收益](guides/elasticity.md#sec-elasticity) |
| `welfare` | 剩餘：`--policy {baseline,tax,subsidy,control}` 與該政策的選項 | [福利](guides/welfare.md#sec-welfare) |
| `report-dwl` | 單列無謂損失報表：`--policy {tax,subsidy,control}`、`--csv` | [福利](guides/welfare.md#sec-welfare) |
| `tax` | `--tax-type {fixed,per_unit,ad_valorem}`、`--amount`、`--tax-on {consumer,producer}` | [租稅與補貼](guides/taxes.md#sec-taxes) |
| `subsidy` | `--amount`、`--subsidy-to {consumer,producer}` | [租稅與補貼](guides/taxes.md#sec-taxes) |
| `controls` | `--control-type {ceiling,floor}`、`--control-price` | [價格管制](guides/controls.md#sec-controls) |
| `trade` | `--world-price`、`--tariff`、`--import-quota`、`--quota-rent-recipient` | [國際貿易](guides/trade.md#sec-trade) |
| `externality` | `--external-cost`、`--external-benefit` | [市場失靈](guides/failures.md#sec-failures) |
| `common-resource` | `--congestion-cost` | [市場失靈](guides/failures.md#sec-failures) |
| `public-good` | `--benefit-intercepts`、`--benefit-slopes`、`--cost-intercept`、`--cost-slope`、`--samples` | [市場失靈](guides/failures.md#sec-failures) |
| `minimum-wage` | `--labor-demand-*`、`--labor-supply-*`、`--minimum-wage` | [勞動與可貸資金](guides/factor-markets.md#sec-factor) |
| `loanable-funds` | `--savings-*`、`--investment-*`、`--savings-shift`、`--investment-shift`、`--government-borrowing` | [勞動與可貸資金](guides/factor-markets.md#sec-factor) |
| `ppf` | `--x-intercept`、`--y-intercept`、`--curvature`、`--x-good`、`--y-good`、`--x-growth`、`--y-growth`、`--samples` | [生產可能曲線](guides/ppf.md#sec-ppf) |

`principle-viz <command> --help` 列出指令的所有選項。

```bash
principle-viz tax \
  --demand-intercept 10 --demand-slope -1 \
  --supply-intercept 2 --supply-slope 1 \
  --tax-type per_unit --amount 1 --tax-on producer
```

輸出包含未課稅的均衡（`baseline_equilibrium`）、課稅後的均衡（`post_tax`）與各項變動，與 `compare_tax_scenario()` 的回傳值相同：本例數量為 3.5，消費者價格 6.5，生產者價格 5.5。
