---
seo_title: "競爭與長期"
---

# 競爭與長期

<span id="sec-competition"></span>

價格接受者廠商、產業供給、長期成本與進入。

每個小節是一支範例腳本和它產生的圖；腳本在儲存庫的 `examples/scripts/`，參數用 `--help` 查看。

## 完全競爭

```bash
uv run python examples/scripts/competition.py --output-dir out
```

### Revenue, cost and profit

總收益與總成本之差最大處即為利潤極大產量。

![Revenue, cost and profit](../../../assets/micro-viz/zh-CN/competition/revenue_cost_profit.svg){ .ev-figure-sm }

### Market and firm

市場需求決定價格，個別廠商面對水平需求線。

![Market and firm](../../../assets/micro-viz/zh-CN/competition/market_and_firm.svg){ .ev-figure-lg }

### Firm earning a profit

價格高於 ATC 時，利潤為價格與 ATC 之間的長方形。

![Firm earning a profit](../../../assets/micro-viz/zh-CN/competition/firm_profit.svg){ .ev-figure-sm }

### Profit lost off the optimum

少於或多於 MR = MC 的產量都會損失利潤。

![Profit lost off the optimum](../../../assets/micro-viz/zh-CN/competition/firm_lost_profit.svg){ .ev-figure-sm }

### Firm with a loss

價格介於 AVC 與 ATC 之間時，廠商繼續生產但虧損。

![Firm with a loss](../../../assets/micro-viz/zh-CN/competition/firm_loss.svg){ .ev-figure-sm }

### Shutdown

價格低於最低 AVC 時，廠商停止生產。

![Shutdown](../../../assets/micro-viz/zh-CN/competition/firm_shutdown.svg){ .ev-figure-sm }

### Firm supply curve

供給曲線是 MC 在最低 AVC 以上的部分。

![Firm supply curve](../../../assets/micro-viz/zh-CN/competition/firm_supply.svg){ .ev-figure-sm }

### Cost shift

成本上升使 MC 與 AVC 上移，產量減少。

![Cost shift](../../../assets/micro-viz/zh-CN/competition/cost_shift.svg){ .ev-figure-sm }

### Per-unit tax

從量稅使 MC 上移一個稅額，廠商減產。

![Per-unit tax](../../../assets/micro-viz/zh-CN/competition/unit_tax.svg){ .ev-figure-sm }

### Industry supply

產業供給為各廠商供給的水平加總。

![Industry supply](../../../assets/micro-viz/zh-CN/competition/industry_supply.svg){ .ev-figure-lg }

### Industry supply alone

只畫產業供給曲線與各價格下的產量。

![Industry supply alone](../../../assets/micro-viz/zh-CN/competition/industry_supply_total.svg){ .ev-figure-sm }

### Producer surplus

生產者剩餘為價格與 MC 之間的面積。

![Producer surplus](../../../assets/micro-viz/zh-CN/competition/producer_surplus.svg){ .ev-figure-sm }

## 長期成本

```bash
uv run python examples/scripts/long_run_costs.py --output-dir out
```

### LAC and LMC

LMC 通過 LAC 的最低點。

![LAC and LMC](../../../assets/micro-viz/zh-CN/long_run_costs/lac_lmc.svg){ .ev-figure-sm }

### Short-run envelope

LAC 是 SAC1 至 SAC3 的包絡線；各 SAC 與 LAC 相切，SMC 通過其 SAC 的最低點。

![Short-run envelope](../../../assets/micro-viz/zh-CN/long_run_costs/short_run_envelope.svg){ .ev-figure-lg }

### Plant family

各廠房的 SAC 與 LAC 相切，SMC 與 LMC 在切點相交。

![Plant family](../../../assets/micro-viz/zh-CN/long_run_costs/plant_family.svg){ .ev-figure-sm }

## 長期競爭

```bash
uv run python examples/scripts/long_run_competition.py --output-dir out
```

### Firm in the long run

長期產量在價格等於 LMC 處，利潤為價格與 LAC 之間的長方形。

![Firm in the long run](../../../assets/micro-viz/zh-CN/long_run_competition/long_run_firm.svg){ .ev-figure-sm }

### Entry

利潤吸引進入，產業供給右移直到價格降到最低 ATC。

![Entry](../../../assets/micro-viz/zh-CN/long_run_competition/entry.svg){ .ev-figure-lg }

### Economic rent

成本較低的廠商在零利潤價格下仍有經濟租。

![Economic rent](../../../assets/micro-viz/zh-CN/long_run_competition/economic_rent.svg){ .ev-figure-lg }

### Constant-cost industry

固定成本產業的長期供給為水平線。

![Constant-cost industry](../../../assets/micro-viz/zh-CN/long_run_competition/constant_cost.svg){ .ev-figure-lg }

### Increasing-cost industry

遞增成本產業的長期供給向右上傾斜。

![Increasing-cost industry](../../../assets/micro-viz/zh-CN/long_run_competition/increasing_cost.svg){ .ev-figure-lg }
