---
seo_title: "參數、網格與動畫"
---

# 參數、網格與動畫

<span id="sec-parameters"></span>

## 參數與運算式

圖層座標不一定是數字，也可以是由具名參數組成的運算式。此時，場景描述一族圖形，每組參數值對應一張圖；綁定參數就是從中選出一張。

<!-- api: agora.mosaickit.guides_parameters_1 -->

具名的佔位符。設定 `value_type` 後，綁定值必須是該型別的實例；所有綁定值都必須可雜湊。`values(seq)` 回傳 `ParameterValues`，並立即檢查每個值。

<!-- api: agora.mosaickit.guides_parameters_2 -->

不可變的運算式樹。參數與常數可以透過 `+`、`-`、`*`、`/`、`**`、一元 `-`，以及比較運算 `<`、`<=`、`>`、`>=` 與 `equals()` 組合；一般數字會包裝成常數。運算式採結構相等：`==` 比較兩棵運算式樹，要建立比較運算式時應改用 `equals()`。把運算式當成真假值使用會引發 `BindingError`；使用前須先求值。`evaluate(bindings)` 根據參數到值的對應計算結果；`free_parameters()` 回傳樹中所有參數的集合。

<span id="def-binding"></span>

!!! abstract "定義 · 運算式與綁定"

    *運算式*是常數、參數，或對運算式 $e_1, e_2$ 與運算 $\circ$ 而言的 $e_1 \circ e_2$。其自由參數為 $\text{free}(c) = \emptyset$、$\text{free}(p) = \lbrace p\rbrace$、$\text{free}(e_1 \circ e_2) = \text{free}(e_1) \cup \text{free}(e_2)$。*綁定* $\beta$ 是從參數到值的有限對應，而 $\text{bind}(e, \beta)$ 定義為：若 $\text{free}(e) \subseteq \text{dom} \beta$，則為值 $e(\beta)$；否則若 $e$ 為參數，則為 $e$ 本身；否則為 $\text{bind}(e_1, \beta) \circ \text{bind}(e_2, \beta)$。一般值 $v$ 沒有自由參數，求值結果為其本身。

<span id="thm-binding"></span>

!!! abstract "定理 · 部分綁定"

    對每個運算式 $e$ 與綁定 $\beta$，
    (i) $\text{free}(\text{bind}(e, \beta)) = \text{free}(e) \setminus \text{dom} \beta$；
    (ii) 對每個滿足 $\text{dom} \gamma \cap \text{dom} \beta = \emptyset$ 且 $\text{dom} \gamma \supseteq \text{free}(e) \setminus \text{dom} \beta$ 的綁定 $\gamma$，$\text{bind}(e, \beta)(\gamma) = e(\beta \cup \gamma)$。

<span id="cor-stages"></span>

!!! abstract "推論 · 分階段綁定"

    對定義域不相交的綁定 $\beta_1, \beta_2$，$\text{bind}(\text{bind}(e, \beta_1), \beta_2)$ 與 $\text{bind}(e, \beta_1 \cup \beta_2)$ 有相同的自由參數，且在這些參數的每個綁定下有相同的值。特別地，`canvas.bind(p, 1).bind(q, 2)` 與 `canvas.bind({p: 1, q: 2})` 畫出相同的圖。

`bind` 會走訪 tuple、mapping 與所有 `mosaickit` dataclass，因此能一次綁定整個場景；圖層的 `model` 則保持不變。若繪製的場景仍含自由參數，會引發指名這些參數的 `BindingError`。

```python
from mosaickit import Canvas, Parameter, TextLayer

x = Parameter("x", value_type=float)
template = Canvas().add(TextLayer((x, 2 * x + 1), "moving"))
frame = template.bind(x, 3.0)
# (3.0, 7.0)
print(frame.snapshot().layers[0].position)
```

## 網格

<!-- api: agora.mosaickit.guides_parameters_3 -->

在同一張圖中放入多個畫布。`cells` 可以是由畫布、`Span` 與 `None`（空格）組成的平面清單，並逐列填入；也可以是列的清單，此時允許跨列，且每列必須涵蓋所有欄。`shape=(rows, cols)` 等同於同時傳入兩者。每個畫布都會複製，因此之後修改原畫布不會影響網格。跨格重疊、跨格超出邊界、格子過多，或混用平面與巢狀格子，都會引發 `ConfigurationError`。`render()` 與 `save()` 的用法與畫布相同。

<span id="prop-grid-shape"></span>

!!! abstract "命題 · 推斷的網格形狀"

    對 $n \ge 1$ 個一般格子組成的平面清單，若未給 `rows` 與 `cols`，網格有 $c = \left\lceil \sqrt\lbrace n\rbrace \right\rceil$ 欄、$r = \left\lceil n / c \right\rceil$ 列。此時 $r c \ge n$、$r \le c$，且空格少於 $c$ 個，全部位於最後一列。

只給 `cols` 時 $r = \left\lceil n / c \right\rceil$；只給 `rows` 時 $c = \left\lceil n / r \right\rceil$。

<!-- api: agora.mosaickit.guides_parameters_4 -->

常見的排列：`SINGLE`、`STACKED`（兩列）、`SIDE_BY_SIDE`、`GRID_2X2`、`GRID_3X3`，以及三個畫布的 `TOP_TWO_BOTTOM_ONE` 與 `TOP_ONE_BOTTOM_TWO`，其中單獨的畫布橫跨兩欄。

<!-- api: agora.mosaickit.guides_parameters_5 -->

`ParameterValues` 的每個值一格，每格是綁定該值的範本。

<!-- api: agora.mosaickit.guides_parameters_6 -->

從某格的 `start` 畫到另一格 `end` 的直線；兩點分別以所在格子的資料座標表示。直線畫在整張圖上，會橫越格子間的空隙。格子依配置順序編號。樣式先在起點格子的主題中解析 `role`，再疊上 `stroke`。格子編號超出範圍時，建立網格就會引發 `ConfigurationError`。

```python
from mosaickit import (
    Canvas,
    CanvasGrid,
    GridLink,
    MarkerLayer,
    Parameter,
    Stroke,
)

shift = Parameter("shift", value_type=float)
template = Canvas().add(MarkerLayer([(5, 2.5 + shift)]))
cells = [template.bind(shift, v) for v in (0.0, 2.0, 4.0)]
link = GridLink(
    0, (5, 2.5), 2, (5, 6.5), stroke=Stroke(dash="dashed")
)
CanvasGrid(cells, cols=3, links=[link]).save("sweep.pdf")
```

<span id="fig-sweep"></span>

![三個值的掃描與跨格連線。](../../../assets/mosaickit/agora/grids/sweep.svg){ .ev-figure-sm }

## 動畫

<!-- api: agora.mosaickit.guides_parameters_7 -->

每個值對應一個畫面，由範本綁定該參數值而成。`frames()` 逐一產生與繪製器無關的場景；`save(path)` 寫出 GIF（透過 Pillow）或 MP4（透過 `ffmpeg`）。建立動畫時就會依參數檢查各值；值清單為空或 `fps` 非正時，會引發 `ConfigurationError`。

```python
from mosaickit import Animation

values = shift.values([0.0, 1.0, 2.0, 3.0])
Animation.sweep(template, values, fps=4).save("sweep.gif")
```
