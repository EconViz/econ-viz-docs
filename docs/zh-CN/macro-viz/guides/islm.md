---
seo_title: "IS-LM"
---

# IS-LM

<span id="sec-islm"></span>

IS 曲线表示商品市场均衡，LM 曲线表示货币市场均衡，两者都画在产出 $Y$ 与利率 $R$ 的平面上。各节对应 `islm.py`、`islm_expectations.py` 与 `liquidity_trap.py`。

## 模型

<!-- api: macro_viz.guides_islm_1 -->

IS 是 $Y = m (X - e R)$，其中 `m` 是乘数、`X` 是自发性支出、`e` 是利率敏感度；LM 是 $M/p = k Y - h R$。`ISLM(autonomous, sensitivity, real_money, income_demand, rate_demand, multiplier=1.0, zero_bound=False)` 接受这些系数。`analyze_fiscal_policy` 改变 `autonomous`，使 IS 移动；`analyze_monetary_policy` 改变 `real_money`，使 LM 移动。

## 均衡与政策

<span id="sec-ex-equilibrium"></span>


<!-- api: macro_viz.guides_islm_2 -->

```python
from macro_viz.islm import (
    ISLM,
    analyze_fiscal_policy,
    analyze_monetary_policy,
)
from macro_viz.visuals import islm_canvas

model = ISLM(100, 25, 20, 0.5, 10)
islm_canvas(model).save("islm.svg")

tax = analyze_fiscal_policy(model, autonomous=80)
islm_canvas(tax).save("islm_tax_increase.svg")

money = analyze_monetary_policy(model, real_money=32)
islm_canvas(money).save("islm_monetary_expansion.svg")
```

<span id="fig-islm"></span>

<figure class="ev-fig" markdown>

![IS 与 LM 相交于 A](../../../assets/macro-viz/islm/islm.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/macro-viz/islm/islm.py" download aria-label="下载生图原始档"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图原始档</span></a></div>

<figcaption markdown>IS 与 LM 相交于 A</figcaption>

</figure>

<span id="fig-islm-tax-increase"></span>

<figure class="ev-fig" markdown>

![增税：IS 左移，利率与产出下降](../../../assets/macro-viz/islm/islm_tax_increase.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/macro-viz/islm/islm.py" download aria-label="下载生图原始档"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图原始档</span></a></div>

<figcaption markdown>增税：IS 左移，利率与产出下降</figcaption>

</figure>

<span id="fig-islm-monetary-expansion"></span>

<figure class="ev-fig" markdown>

![货币扩张：LM 右移](../../../assets/macro-viz/islm/islm_monetary_expansion.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/macro-viz/islm/islm.py" download aria-label="下载生图原始档"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图原始档</span></a></div>

<figcaption markdown>货币扩张：LM 右移</figcaption>

</figure>


箭头从 A 出发，沿旧利率水平指向移动后的曲线。新的交点是 A'。

## 排挤效果

<span id="sec-ex-crowding"></span>



```python
spending = analyze_fiscal_policy(model, autonomous=120)
islm_canvas(spending, show_crowding=True).save(
    "islm_crowding_out.svg"
)
```

<span id="fig-islm-crowding-out"></span>

<figure class="ev-fig" markdown>

![B 是新 IS 在旧利率处的位置；B 到 A' 就是被排挤的产出](../../../assets/macro-viz/islm/islm_crowding_out.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/macro-viz/islm/islm.py" download aria-label="下载生图原始档"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图原始档</span></a></div>

<figcaption markdown>B 是新 IS 在旧利率处的位置；B 到 A' 就是被排挤的产出</figcaption>

</figure>


## 平坦与陡峭的曲线

<span id="sec-ex-shapes"></span>



```python
steep = ISLM(100, 25, 20, 0.5, 2)
flat = ISLM(100, 25, 20, 0.5, 60)
islm_canvas(analyze_fiscal_policy(steep, 120)).save("islm_steep_lm.svg")
islm_canvas(analyze_fiscal_policy(flat, 120)).save("islm_flat_lm.svg")
```

<span id="fig-islm-steep-lm"></span>

<figure class="ev-fig" markdown>

![陡峭的 LM：财政政策主要改变利率](../../../assets/macro-viz/islm/islm_steep_lm.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/macro-viz/islm/islm.py" download aria-label="下载生图原始档"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图原始档</span></a></div>

<figcaption markdown>陡峭的 LM：财政政策主要改变利率</figcaption>

</figure>

<span id="fig-islm-flat-lm"></span>

<figure class="ev-fig" markdown>

![平坦的 LM：财政政策主要改变产出](../../../assets/macro-viz/islm/islm_flat_lm.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/macro-viz/islm/islm.py" download aria-label="下载生图原始档"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图原始档</span></a></div>

<figcaption markdown>平坦的 LM：财政政策主要改变产出</figcaption>

</figure>


## 流动性陷阱

<span id="sec-ex-trap"></span>



```python
trap = ISLM(80, 25, 60, 0.5, 8, zero_bound=True)
shift = analyze_monetary_policy(trap, real_money=90)
islm_canvas(shift, x_max=300).save("islm_zero_bound.svg")
```

<span id="fig-islm-zero-bound"></span>

<figure class="ev-fig" markdown>

![利率为零时，货币扩张不改变产出](../../../assets/macro-viz/islm/islm_zero_bound.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/macro-viz/islm/liquidity_trap.py" download aria-label="下载生图原始档"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图原始档</span></a></div>

<figcaption markdown>利率为零时，货币扩张不改变产出</figcaption>

</figure>


## 预期通膨

<span id="sec-ex-expectations"></span>


<!-- api: macro_viz.guides_islm_3 -->

```python
from macro_viz.islm import ISLMExpectations
from macro_viz.visuals import islm_expectations_canvas

inflation = ISLMExpectations(model, expected_inflation=0.2)
islm_expectations_canvas(inflation).save(
    "islm_expected_inflation.svg"
)
```

<span id="fig-islm-expected-inflation"></span>

<figure class="ev-fig" markdown>

![坐标轴为名目利率，实质利率是其下方的差距](../../../assets/macro-viz/islm/islm_expected_inflation.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/macro-viz/islm/islm_expectations.py" download aria-label="下载生图原始档"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图原始档</span></a></div>

<figcaption markdown>坐标轴为名目利率，实质利率是其下方的差距</figcaption>

</figure>

<span id="fig-islm-expected-inflation-money"></span>

<figure class="ev-fig" markdown>

![预期通膨给定下的货币扩张](../../../assets/macro-viz/islm/islm_expected_inflation_money.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/macro-viz/islm/islm_expectations.py" download aria-label="下载生图原始档"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图原始档</span></a></div>

<figcaption markdown>预期通膨给定下的货币扩张</figcaption>

</figure>


## 动画

<span id="sec-ex-animation"></span>



<span id="fig-islm-animation"></span>

<figure class="ev-fig" markdown>

![实质货币增加，LM 右移](../../../assets/macro-viz/islm/islm_animation.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/macro-viz/islm/islm_animation.py" download aria-label="下载生图原始档"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图原始档</span></a></div>

<figcaption markdown>实质货币增加，LM 右移</figcaption>

</figure>

