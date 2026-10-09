---
seo_title: "取樣與匯出"
---

# 取樣與匯出

<span id="sec-export"></span>

匯出器只寫出幾何資料，不選擇顏色、線寬、主題、座標軸、標籤或畫布，也絕不把三次曲線攤平成折線：TikZ 收到原生的 `.. controls ..` 曲線，SVG 收到原生的 `C` 指令。

## 取樣

<!-- api: agora.bezierkit.guides_export_1 -->

在曲線或路徑的定義域上，以 `count` 個等距參數求值（含兩端，`count` $\ge 2$），位於 `bezierkit.sampling`。

<!-- api: agora.bezierkit.guides_export_2 -->

取樣的結果：唯讀的參數 `t` 與 `points`，提供座標陣列 `x`、`y`，並可逐一取出 `(t, point)`。

```python
from bezierkit.sampling import UniformSampler

sample = UniformSampler(5).sample(curve)
# [0.      0.90625 2.      3.09375 4.     ]
print(sample.x)
```

## 四捨五入與座標變換

文字格式的匯出器以固定的小數位數 `precision` 寫出每個座標，並接受 `transform`：在寫出前把每個控制點（`Point`）對應到二維 `Point`，例如由資料座標轉為頁面座標。

<span id="prop-rounding"></span>

!!! abstract "命題 · 四捨五入誤差"

    設 $B$、$\widetilde{B}$ 是同為 $n$ 次的 $\mathbb{R}^d$ 中 Bézier 曲線，控制點分別為 $P_i$ 與 $\widetilde{P}_i$，且對每個 $i$ 與每個座標 $k$ 有 $|\widetilde{P}_{i,k} - P_{i,k}| \le \epsilon$。則對每個 $t \in [0, 1]$ 與每個 $k$，

    $$
    |\widetilde{B}_k (t) - B_k (t)| \le \epsilon, \quad \left\lVert \widetilde{B}(t) - B(t) \right\rVert_2 \le \sqrt{d} \epsilon.
    $$

    將每個座標四捨五入到小數點後 $p$ 位時，$\epsilon = 1/2 \cdot 10^{-p}$。

因此在預設的 `precision=6` 下，匯出的平面曲線處處與原曲線相差不超過 $0.71 \times 10^{-6}$，不只在控制點上成立。依[仿射不變性](curves.md#prop-affine)，仿射的 `transform` 是精確的；非仿射的變換能正確移動控制點，但一般不能正確移動控制點之間的曲線。

## JSON

<!-- api: agora.bezierkit.guides_export_3 -->

位於 `bezierkit.export.json`。以[JSON 路徑格式第 1 版](export.md#tab-json)的版本化格式寫出路徑，鍵依字母排序，不含 NaN 或無窮大。

<!-- api: agora.bezierkit.guides_export_4 -->

驗證文件並回傳 `PathDocument`，內含 `path` 與 `metadata`。格式或版本不明、線段不是恰好四個點、點的維度不符或數值非有限時，拋出 `ValueError`。

<!-- api: agora.bezierkit.guides_export_5 -->

路徑與呼叫端的 metadata，即 `loads()` 的回傳值。

<span id="tab-json"></span>

| 鍵 | 值 |
| --- | --- |
| `schema` | 字串 `"bezierkit.path"` |
| `version` | 整數 `1`；讀取端拒絕其他版本 |
| `dimension` | 每個點的維度 $d$ |
| `subpaths` | 非空陣列，元素為 `{"closed": bool, "segments": [...]}`，每個線段是四個含 $d$ 個數值的點 |
| `metadata` | JSON 物件，原樣傳遞、不解讀 |

```python
from bezierkit.export.json import dumps, loads

text = dumps(path, metadata={"name": "arch"})
# {"dimension":2,"metadata":{"name":"arch"},"schema":"bezierkit.path",
#  "subpaths":[{"closed":false,"segments":[[[0.0,0.0],[1.0,2.0],...]]}],"version":1}
assert loads(text).path.segments == path.segments
```

第 1 版已凍結：新增必要的鍵、改變封閉的語意或控制點的排列方式，都需要第 2 版。

## SVG

<!-- api: agora.bezierkit.guides_export_6 -->

位於 `bezierkit.export.svg`。回傳平面路徑的路徑資料字串（即 `d` 屬性），只使用絕對座標的 `M`、`C` 與 `Z` 指令，每條子路徑一個 `M`；不產生 SVG 文件或樣式。`from_svg_path_data()` 解析同一子集；相對指令、直線與圓弧拋出 `ValueError`。

```python
from bezierkit.export.svg import to_svg_path_data

# M 0.00 0.00 C 1.00 2.00 3.00 2.00 4.00 0.00
print(to_svg_path_data(path, precision=2))
```

## TikZ

<!-- api: agora.bezierkit.guides_export_7 -->

位於 `bezierkit.export.tikz`。每條子路徑一個 `\draw` 指令，每個線段寫成 `.. controls (P1) and (P2) .. (P3)`，封閉子路徑以 `-- cycle` 結尾。`options` 原樣放入 `\draw[options]`；預設不加任何選項。`segment_to_tikz()` 只寫出一個線段、不含 `\draw`，供需要自行組合指令的呼叫端使用。

```python
from bezierkit.export.tikz import to_tikz

print(to_tikz(path, precision=2, options="thick"))
# \draw[thick] (0.00,0.00) .. controls (1.00,2.00) and (3.00,2.00) .. (4.00,0.00);
```

本手冊的每張圖都是這樣產生的：腳本以 `bezierkit` 建立曲線，用 `to_tikz()` 寫進 `standalone` LaTeX 文件，與座標軸、標籤放在一起，再編譯成 PDF。每張圖的 `.tex` 原始檔都隨手冊提供。

## Matplotlib

<span id="sec-matplotlib"></span>

<!-- api: agora.bezierkit.guides_export_8 -->

位於 `bezierkit.adapters.matplotlib`，需安裝 `matplotlib` 選用依賴。`from_path()` 精確轉換 Matplotlib `Path`：`MOVETO`、`LINETO`、`CURVE3`、`CURVE4` 與 `CLOSEPOLY` 都轉為三次曲線，直線與二次曲線依[直線與二次曲線的三次表示](paths.md#prop-elevation)升階。仿射的 `transform` 直接套用在控制點上，結果精確（詳見[仿射不變性](curves.md#prop-affine)）；非仿射的變換拋出 `ValueError`。`to_path()` 反向轉換，每個線段一個 `CURVE4`。

非仿射變換（例如對數座標軸）不會把三次曲線對應到三次曲線。`approximate_path()` 是明確的選擇：它細分每個變換後的線段，直到中點與弦的距離在 `tolerance / 2` 以內，再以 `tolerance / 2` 對這些點呼叫 `fit_polyline`。它不宣稱結果精確。
