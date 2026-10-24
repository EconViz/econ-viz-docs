---
seo_title: "生產可能曲線"
---

# 生產可能曲線

<span id="sec-ppf"></span>

<!-- api: agora.principle_viz.guides_ppf_1 -->

通過截距 $X$ 與 $Y$ 的生產可能曲線

$$
y = Y (1 - (x / X)^c).
$$

曲率 $c = 1$ 為直線（機會成本固定）；$c > 1$ 時曲線向外凸出（機會成本遞增）。截距與曲率必須為正且 $c \ge 1$，否則拋出 `PPFError`。

<!-- api: agora.principle_viz.guides_ppf_2 -->

點相對於邊界的位置。

```python
from principle_viz import ProductionPossibilitiesFrontier

ppf = ProductionPossibilitiesFrontier(
    10,
    8,
    curvature=2,
    x_good="Consumer goods",
    y_good="Capital goods",
)
# 5.12 0.96
print(ppf.y_at(6), ppf.opportunity_cost_x(6))
print(ppf.assess(4, 3), ppf.assess(7, 6))
# PointStatus.INEFFICIENT PointStatus.UNATTAINABLE
```

<!-- api: agora.principle_viz.guides_ppf_3 -->

在曲線上取樣，並評估以 `(x, y, label)` 三元組給定的點；`principle_viz.visuals.ppf` 中的 `ppf_canvas()` 畫出曲線、為可達成的區域填色並標出各點（參見[有效率與無效率的點](ppf.md#fig-ppf)）。圖標題由 `title` 參數決定：預設為 "Production Possibilities Frontier"，**傳入 `None` 則不畫標題**，其他文字照原樣畫出；預設的英文標題會依圖形語言翻譯。

```python
from principle_viz import analyze_ppf
from principle_viz.visuals.ppf import ppf_canvas

points = ((6, ppf.y_at(6), "A"), (4, 3, "B"), (7, 6, "C"))
result = analyze_ppf(ppf, points=points)
ppf_canvas(result, title=None).save("ppf_points.png")
```

<span id="fig-ppf"></span>

<figure class="ev-fig" markdown>

![有效率與無效率的點](../../../assets/principle-viz/agora/ppf/points.zh-TW.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/principle-viz/agora/ppf/ppf.py" download aria-label="下載生圖原始檔"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下載生圖原始檔</span></a></div>

<figcaption markdown>有效率與無效率的點</figcaption>

</figure>

<!-- api: agora.principle_viz.guides_ppf_4 -->

經濟成長使各截距乘以一加上對應的成長率；結果包含 `baseline` 與 `shifted` 兩條曲線及其取樣點。`ppf_growth_canvas()` 畫出兩條曲線並命名為 $P P F_0$ 與 $P P F_1$（參見[消費財與資本財成長](ppf.md#fig-ppf-growth)）。其 `title` 的用法與 `ppf_canvas()` 相同，預設為 "Economic Growth"。

<span id="fig-ppf-growth"></span>

<figure class="ev-fig" markdown>

![消費財與資本財成長](../../../assets/principle-viz/agora/ppf/growth.zh-TW.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/principle-viz/agora/ppf/ppf.py" download aria-label="下載生圖原始檔"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下載生圖原始檔</span></a></div>

<figcaption markdown>消費財與資本財成長</figcaption>

</figure>

## 比較利益

<span id="sec-comparative-advantage"></span>

<!-- api: agora.principle_viz.guides_ppf_5 -->

比較兩條直線型生產可能曲線：各生產者生產 $x$ 的機會成本，以及各商品的比較利益歸屬（成本相同時為 `"tie"`）。曲線型的生產可能曲線會拋出 `PPFError`。

```python
from principle_viz import compare_linear_ppfs

# x costs 0.5 y
ann = ProductionPossibilitiesFrontier(10, 5)
# x costs 1 y
bob = ProductionPossibilitiesFrontier(6, 6)
result = compare_linear_ppfs("Ann", ann, "Bob", bob)
print(
    result.comparative_advantage_x,
    result.comparative_advantage_y,
)
# Ann Bob
```

$x$ 的比較利益屬於 Ann（0.5 對 1），$y$ 屬於 Bob（1 對 2）。
