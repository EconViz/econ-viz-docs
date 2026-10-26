---
seo_title: "生产与成本"
---

# 生产与成本

<span id="sec-production-costs"></span>

每一节是一支示例脚本与它画出的图。脚本在示例压缩包中提供，参数可用 `--help` 查看。

## 短期生产

<span id="sec-ex-production"></span>

一种变动投入与一种固定投入，得到总产量、平均产量与边际产量。边际报酬的区间由模型分类，图中以底色标出。

<!-- api: micro_viz.guides_production_costs_1 -->

`ShortRunProductionFunction` 是三次生产函数 $Q = a L + b L^2 + c L^3$；`analyze_production()` 采样 TP、AP 与 MP，并把范围分成边际报酬递增、递减与为负的区间。

<!-- api: micro_viz.guides_production_costs_2 -->

平均与边际产量图：含边际报酬区间，并标出 AP = MP 与 MP = 0 的点。

<!-- api: micro_viz.guides_production_costs_3 -->

总产量图：曲线、三个边际报酬区间与分界线。

```python
def production_examples(
    output_dir: Path,
    theme: PlotTheme,
    *,
    function: ShortRunProductionFunction,
    input_range: tuple[float, float],
    samples: int,
    region_colors: dict[str, str] | None = None,
    title: str | None = None,
) -> tuple[Path, Path]:
    """Write the two production examples into ``output_dir`` and return their paths."""
    analysis = analyze_production(
        function, input_range=input_range, samples=samples
    )
    output_dir.mkdir(parents=True, exist_ok=True)
    total_output = output_dir / "total_product.svg"
    products_output = (
        output_dir / "average_marginal_product.svg"
    )
    total_product_canvas(
        analysis,
        theme=theme,
        title=title,
        region_colors=region_colors,
    ).save(total_output)
    average_marginal_product_canvas(
        analysis,
        theme=theme,
        title=title,
        region_colors=region_colors,
    ).save(products_output)
    # The same figures with the shade stopping at the curve instead of reaching the top.
    under = replace(theme, region_extent="curve")
    total_product_canvas(
        analysis,
        theme=under,
        title=title,
        region_colors=region_colors,
    ).save(output_dir / "total_product_under_curve.svg")
    average_marginal_product_canvas(
        analysis,
        theme=under,
        title=title,
        region_colors=region_colors,
    ).save(
        output_dir / "average_marginal_product_under_curve.svg"
    )
    return total_output, products_output
```

<span id="fig-production-total-product"></span>

<figure class="ev-fig" markdown>

![*总产量曲线。* 短期总产量曲线，并标出边际报酬递增与递减的区间。](../../../assets/micro-viz/production/total_product.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/micro-viz/production/production.py" download aria-label="下载生图源文件"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图源文件</span></a></div>

<figcaption markdown>*总产量曲线。* 短期总产量曲线，并标出边际报酬递增与递减的区间。</figcaption>

</figure>

<span id="fig-production-average-marginal-product"></span>

<figure class="ev-fig" markdown>

![*平均与边际产量。* 平均产量与边际产量曲线，MP 通过 AP 的最高点。](../../../assets/micro-viz/production/average_marginal_product.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/micro-viz/production/production.py" download aria-label="下载生图源文件"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图源文件</span></a></div>

<figcaption markdown>*平均与边际产量。* 平均产量与边际产量曲线，MP 通过 AP 的最高点。</figcaption>

</figure>

<span id="fig-production-total-product-under-curve"></span>

<figure class="ev-fig" markdown>

![*总产量，底色在曲线下。* 区域底色只填到曲线为止。](../../../assets/micro-viz/production/total_product_under_curve.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/micro-viz/production/production.py" download aria-label="下载生图源文件"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图源文件</span></a></div>

<figcaption markdown>*总产量，底色在曲线下。* 区域底色只填到曲线为止。</figcaption>

</figure>

<span id="fig-production-average-marginal-product-under-curve"></span>

<figure class="ev-fig" markdown>

![*平均与边际产量，底色在曲线下。* 区域底色只填到 AP、MP 的上缘为止。](../../../assets/micro-viz/production/average_marginal_product_under_curve.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/micro-viz/production/production.py" download aria-label="下载生图源文件"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图源文件</span></a></div>

<figcaption markdown>*平均与边际产量，底色在曲线下。* 区域底色只填到 AP、MP 的上缘为止。</figcaption>

</figure>

## 短期成本

<span id="sec-ex-costs"></span>

三次成本函数得到总成本、变动成本、固定成本与四条单位成本曲线。MC 通过 AVC 与 ATC 的最低点。

<!-- api: micro_viz.guides_production_costs_4 -->

`CubicCost` 是 $\text{TC} = \text{FC} + b Q + c Q^2 + d Q^3$；`analyze_costs()` 在产量范围内计算各种成本，并找出 AVC 与 ATC 的最低点。

<!-- api: micro_viz.guides_production_costs_5 -->

上方是总成本、下方是单位成本，共用产量轴。

<!-- api: micro_viz.guides_production_costs_6 -->

把 `cost_curves_grid` 的两栏分成两张画布，各自可独立成图。

<!-- api: micro_viz.guides_production_costs_7 -->

TC、VC 与 FC 对产量。

<!-- api: micro_viz.guides_production_costs_8 -->

MC、ATC、AVC 与 AFC 对产量；`curves` 可选子集。

```python
def cost_examples(
    output_dir: Path,
    theme: PlotTheme,
    *,
    cost: CubicCost,
    min_output: float,
    max_output: float,
    samples: int,
    avc_reach: float = 1.15,
    title: str | None = None,
) -> list[Path]:
    """Write the cost-curve examples for ``cost`` into ``output_dir`` and return the paths."""
    analysis = analyze_costs(
        cost,
        output_range=(min_output, max_output),
        samples=samples,
    )
    no_fixed = analyze_costs(
        CubicCost(
            fixed_cost=0.0,
            linear=cost.linear,
            quadratic=cost.quadratic,
            cubic=cost.cubic,
            output_symbol=cost.output_symbol,
        ),
        output_range=(min_output, max_output * avc_reach),
        samples=samples,
    )
    total_panel, unit_panel = cost_curves_panels(
        analysis, theme=theme, titles=(title, None)
    )
    output_dir.mkdir(parents=True, exist_ok=True)
    figures = {
        "total_cost.svg": total_cost_canvas(
            analysis, theme=theme, title=title
        ),
        "unit_cost.svg": unit_cost_canvas(
            analysis, theme=theme, title=title
        ),
        "cubic_avc_mc.svg": unit_cost_canvas(
            no_fixed,
            curves=("mc", "avc"),
            theme=theme,
            title=title,
        ),
        "cost_curves_total.svg": total_panel,
        "cost_curves_unit.svg": unit_panel,
        "cost_curves.svg": cost_curves_grid(
            analysis, theme=theme, titles=(title, None)
        ),
    }
    paths = []
    for name, figure in figures.items():
        figure.save(output_dir / name)
        paths.append(output_dir / name)
    return paths
```

<span id="fig-costs-total-cost"></span>

<figure class="ev-fig" markdown>

![*总成本曲线。* 总成本、变动成本与固定成本曲线。](../../../assets/micro-viz/costs/total_cost.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/micro-viz/costs/costs.py" download aria-label="下载生图源文件"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图源文件</span></a></div>

<figcaption markdown>*总成本曲线。* 总成本、变动成本与固定成本曲线。</figcaption>

</figure>

<span id="fig-costs-unit-cost"></span>

<figure class="ev-fig" markdown>

![*单位成本曲线。* MC、ATC、AVC 与 AFC 曲线，MC 通过 AVC 与 ATC 的最低点。](../../../assets/micro-viz/costs/unit_cost.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/micro-viz/costs/costs.py" download aria-label="下载生图源文件"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图源文件</span></a></div>

<figcaption markdown>*单位成本曲线。* MC、ATC、AVC 与 AFC 曲线，MC 通过 AVC 与 ATC 的最低点。</figcaption>

</figure>

<span id="fig-costs-cubic-avc-mc"></span>

<figure class="ev-fig" markdown>

![*三次函数的 AVC 与 MC。* 三次成本函数的 AVC 与 MC。](../../../assets/micro-viz/costs/cubic_avc_mc.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/micro-viz/costs/costs.py" download aria-label="下载生图源文件"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图源文件</span></a></div>

<figcaption markdown>*三次函数的 AVC 与 MC。* 三次成本函数的 AVC 与 MC。</figcaption>

</figure>

<span id="fig-costs-cost-curves"></span>

<figure class="ev-fig" markdown>

![*成本曲在线下对照。* 总成本与单位成本的两栏对照图。](../../../assets/micro-viz/costs/cost_curves.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/micro-viz/costs/costs.py" download aria-label="下载生图源文件"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图源文件</span></a></div>

<figcaption markdown>*成本曲在线下对照。* 总成本与单位成本的两栏对照图。</figcaption>

</figure>

<span id="fig-costs-cost-curves-total"></span>

<figure class="ev-fig" markdown>

![*总成本图。* 两栏对照图中的总成本图，可单独使用。](../../../assets/micro-viz/costs/cost_curves_total.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/micro-viz/costs/costs.py" download aria-label="下载生图源文件"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图源文件</span></a></div>

<figcaption markdown>*总成本图。* 两栏对照图中的总成本图，可单独使用。</figcaption>

</figure>

<span id="fig-costs-cost-curves-unit"></span>

<figure class="ev-fig" markdown>

![*单位成本图。* 两栏对照图中的单位成本图，可单独使用。](../../../assets/micro-viz/costs/cost_curves_unit.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/micro-viz/costs/costs.py" download aria-label="下载生图源文件"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图源文件</span></a></div>

<figcaption markdown>*单位成本图。* 两栏对照图中的单位成本图，可单独使用。</figcaption>

</figure>

## 阶梯与折点成本

<span id="sec-ex-piecewise-costs"></span>

数个容量固定的厂房得到阶梯式边际成本；一个有产能限制的厂房得到折线边际成本。

<!-- api: micro_viz.guides_production_costs_9 -->

`PiecewiseCost` 把各有容量与边际成本的 `CostSegment` 接起来；它是 `CostFunction`，因此 `analyze_costs()` 可以使用。

<!-- api: micro_viz.guides_production_costs_10 -->

阶梯或折线边际成本，含容量与价格带。

```python
def piecewise_examples(
    output_dir: Path,
    theme: PlotTheme,
    *,
    stepped: PiecewiseCost,
    kinked: PiecewiseCost,
    prices: tuple[float, ...],
    kinked_prices: tuple[float, ...],
    kinked_y_min: float,
    samples: int,
    title: str | None = None,
) -> list[Path]:
    """Write the stepped and kinked marginal-cost examples into ``output_dir``."""
    output_dir.mkdir(parents=True, exist_ok=True)
    step_analysis = analyze_costs(
        stepped,
        output_range=(0.0, stepped.capacity),
        samples=samples,
    )
    kink_analysis = analyze_costs(
        kinked,
        output_range=(0.0, kinked.capacity),
        samples=samples,
    )
    kink_top = max(
        value for _, value in kink_analysis.marginal_cost_path
    )
    figures = {
        "stepped_cost.svg": piecewise_cost_canvas(
            step_analysis, theme=theme, title=title
        ),
        "stepped_cost_prices.svg": piecewise_cost_canvas(
            step_analysis,
            prices=prices,
            theme=theme,
            title=title,
        ),
        "kinked_marginal_cost.svg": piecewise_cost_canvas(
            kink_analysis,
            prices=kinked_prices,
            average=False,
            y_range=(
                kinked_y_min,
                kink_top + (kink_top - kinked_y_min) * 0.1,
            ),
            theme=theme,
            title=title,
        ),
    }
    for name, figure in figures.items():
        figure.save(output_dir / name)
    return [output_dir / name for name in figures]
```

<span id="fig-piecewise-costs-stepped-cost"></span>

<figure class="ev-fig" markdown>

![*阶梯式边际成本。* 多个厂房的阶梯式边际成本。](../../../assets/micro-viz/piecewise_costs/stepped_cost.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/micro-viz/piecewise_costs/piecewise_costs.py" download aria-label="下载生图源文件"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图源文件</span></a></div>

<figcaption markdown>*阶梯式边际成本。* 多个厂房的阶梯式边际成本。</figcaption>

</figure>

<span id="fig-piecewise-costs-stepped-cost-prices"></span>

<figure class="ev-fig" markdown>

![*阶梯成本与产量。* 价格穿过阶梯时产量随之跳动。](../../../assets/micro-viz/piecewise_costs/stepped_cost_prices.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/micro-viz/piecewise_costs/piecewise_costs.py" download aria-label="下载生图源文件"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图源文件</span></a></div>

<figcaption markdown>*阶梯成本与产量。* 价格穿过阶梯时产量随之跳动。</figcaption>

</figure>

<span id="fig-piecewise-costs-kinked-marginal-cost"></span>

<figure class="ev-fig" markdown>

![*折线边际成本。* 有产能限制的折线边际成本。](../../../assets/micro-viz/piecewise_costs/kinked_marginal_cost.zh-CN.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/micro-viz/piecewise_costs/piecewise_costs.py" download aria-label="下载生图源文件"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图源文件</span></a></div>

<figcaption markdown>*折线边际成本。* 有产能限制的折线边际成本。</figcaption>

</figure>
