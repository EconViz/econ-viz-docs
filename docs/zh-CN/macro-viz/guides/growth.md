---
seo_title: "梭罗成长"
---

# 梭罗成长

<span id="sec-growth"></span>

只要储蓄 $s f(K/N)$ 大于维持资本不变所需的 $(\delta + g_N) K/N$，每位劳工的资本就会成长。各节对应 `growth.py`。

## 模型

<!-- api: macro_viz.guides_growth_1 -->

`Solow` 接受每位劳工资本的生产函数，以及储蓄率、折旧率、人口成长率与技术成长率。方法可回答 `steady_state`、`steady_output`、`golden_rule_capital` 与 `consumption_at`；`with_saving`、`with_population_growth`、`with_tech_growth` 与 `with_production` 返回变动后的模型。`simulate` 仿真在指定期间发生变动后的转换路径。

## 生产函数

<span id="sec-ex-production"></span>


<!-- api: macro_viz.guides_growth_2 -->

```python
from macro_viz.growth import Solow
from macro_viz.visuals import production_function_canvas

model = Solow.cobb_douglas(0.33, saving=0.2, depreciation=0.1)
better = Solow.cobb_douglas(
    0.33, saving=0.2, depreciation=0.1, productivity=1.4
)
production_function_canvas(model, points=[1.0, 2.0, 3.5]).save(
    "production_function.svg"
)
production_function_canvas(model, shifted=better).save(
    "production_function_shift.svg"
)
```

<span id="fig-production-function"></span>

<figure class="ev-fig" markdown>

![每位劳工产出随资本增加，但增幅递减](../../../assets/macro-viz/growth/production_function.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/macro-viz/growth/growth.py" download aria-label="下载生图原始档"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图原始档</span></a></div>

<figcaption markdown>每位劳工产出随资本增加，但增幅递减</figcaption>

</figure>

<span id="fig-production-function-shift"></span>

<figure class="ev-fig" markdown>

![技术进步：f 上移到 f'，以直线垂直箭头表示](../../../assets/macro-viz/growth/production_function_shift.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/macro-viz/growth/growth.py" download aria-label="下载生图原始档"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图原始档</span></a></div>

<figcaption markdown>技术进步：f 上移到 f'，以直线垂直箭头表示</figcaption>

</figure>


## 稳定状态

<span id="sec-ex-steady"></span>


<!-- api: macro_viz.guides_growth_3 -->

```python
from macro_viz.growth import analyze_change
from macro_viz.visuals import solow_canvas

solow_canvas(model).save("solow.svg")
more_saving = model.with_saving(0.35)
solow_canvas(analyze_change(model, more_saving)).save(
    "solow_saving_increase.svg"
)
```

<span id="fig-solow"></span>

<figure class="ev-fig" markdown>

![储蓄线与折旧线交于稳定状态 A](../../../assets/macro-viz/growth/solow.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/macro-viz/growth/growth.py" download aria-label="下载生图原始档"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图原始档</span></a></div>

<figcaption markdown>储蓄线与折旧线交于稳定状态 A</figcaption>

</figure>

<span id="fig-solow-saving-increase"></span>

<figure class="ev-fig" markdown>

![储蓄率上升使 $s f$ 上移，资本升到 $K^*{}'$](../../../assets/macro-viz/growth/solow_saving_increase.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/macro-viz/growth/growth.py" download aria-label="下载生图原始档"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图原始档</span></a></div>

<figcaption markdown>储蓄率上升使 $s f$ 上移，资本升到 $K^*{}'$</figcaption>

</figure>


`effective=True` 使用每有效劳工的变量，例如人口成长的情形。

<span id="fig-solow-population-growth"></span>

<figure class="ev-fig" markdown>

![人口成长加快，使所需投资线移动](../../../assets/macro-viz/growth/solow_population_growth.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/macro-viz/growth/growth.py" download aria-label="下载生图原始档"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图原始档</span></a></div>

<figcaption markdown>人口成长加快，使所需投资线移动</figcaption>

</figure>


## 黄金法则

<span id="sec-ex-golden"></span>


<!-- api: macro_viz.guides_growth_4 -->

<span id="fig-golden-rule"></span>

<figure class="ev-fig" markdown>

![在黄金法则储蓄率下，每位劳工的消费最高](../../../assets/macro-viz/growth/golden_rule.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/macro-viz/growth/growth.py" download aria-label="下载生图原始档"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图原始档</span></a></div>

<figcaption markdown>在黄金法则储蓄率下，每位劳工的消费最高</figcaption>

</figure>


## 转换路径

<span id="sec-ex-paths"></span>


<!-- api: macro_viz.guides_growth_5 -->

```python
from macro_viz.growth import simulate
from macro_viz.visuals import (
    solow_growth_rate_canvas,
    solow_level_path_canvas,
    solow_log_path_canvas,
)

path = simulate(
    model, model.with_saving(0.35), periods=60, change_period=5
)
solow_level_path_canvas(path).save("solow_level_path.svg")
solow_log_path_canvas(path).save("solow_log_path.svg")
solow_growth_rate_canvas(path).save("solow_growth_rate.svg")
```

<span id="fig-solow-level-path"></span>

<figure class="ev-fig" markdown>

![第 5 期变动后每位劳工的产出](../../../assets/macro-viz/growth/solow_level_path.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/macro-viz/growth/growth.py" download aria-label="下载生图原始档"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图原始档</span></a></div>

<figcaption markdown>第 5 期变动后每位劳工的产出</figcaption>

</figure>

<span id="fig-solow-log-path"></span>

<figure class="ev-fig" markdown>

![同一路径取对数](../../../assets/macro-viz/growth/solow_log_path.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/macro-viz/growth/growth.py" download aria-label="下载生图原始档"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图原始档</span></a></div>

<figcaption markdown>同一路径取对数</figcaption>

</figure>

<span id="fig-solow-growth-rate"></span>

<figure class="ev-fig" markdown>

![成长率先上升再回落](../../../assets/macro-viz/growth/solow_growth_rate.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/macro-viz/growth/growth.py" download aria-label="下载生图原始档"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图原始档</span></a></div>

<figcaption markdown>成长率先上升再回落</figcaption>

</figure>


## 动画

<span id="sec-ex-animation"></span>



<span id="fig-solow-animation"></span>

<figure class="ev-fig" markdown>

![储蓄率上升，稳定状态随之移动](../../../assets/macro-viz/animation/solow_animation.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/macro-viz/animation/growth_animation.py" download aria-label="下载生图原始档"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图原始档</span></a></div>

<figcaption markdown>储蓄率上升，稳定状态随之移动</figcaption>

</figure>

