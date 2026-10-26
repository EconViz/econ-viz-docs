---
seo_title: "標籤與位置"
---

# 標籤與位置

<span id="sec-labels"></span>

## 語系表

`macro-viz` 放進圖中的每個字都在 `src/macro_viz/locale/labels.json`，先依語言（`en`、`zh-TW`、`zh-CN`）、再依穩定的編號（`islm.curve.is`）索引。語言來自設定的 `[macro] language`。

含欄位的文字使用大括號，例如 `$AS({capital})$`。數學式寫在 `$...$` 中，不使用 Unicode 下標。

符號在各圖之間固定：只有價格 $p$ 用小寫，其他變數（$Y$、$R$、$W$、$N$、$K$）一律用大寫斜體。縮寫（`IS`、`LM`、`AD`、`AS`）與點名保留原有的大小寫。

<!-- api: macro_viz.guides_labels_1 -->

| 前綴 | 編號數 | 圖形 |
| --- | --- | --- |
| `keynesian` | 16 | 消費函數、凱因斯十字、乘數 |
| `money` | 17 | 貨幣市場與央行貨幣 |
| `adas` | 18 | 總合供給與需求及其調整 |
| `islm` | 17 | IS-LM 與含預期通膨的 IS-LM |
| `solow` | 40 | 生產函數與梭羅成長 |
| `labor` | 14 | 工資設定與價格設定 |
| `parity` | 7 | 利率平價與開放經濟 IS-LM |
| `panels` | 20 | 連動面板 |
| `axis, open` | 2 | 原點與開放經濟商品市場 |

```python
from macro_viz.i18n import label_ids

label_ids()
```

## 取代文字

<span id="sec-replace"></span>

你傳入的文字照原樣使用，不會翻譯。`labels` 把編號對應到文字；未知的編號會引發 `ValidationError`。

```python
from macro_viz.visuals import islm_canvas

islm_canvas(
    tax,
    title="A tax increase",
    labels={"islm.curve.is": "$IS_0$", "islm.curve.is_shifted": "$IS_1$"},
).save("islm_tax_increase.svg")
```

`title=None`（預設）不畫標題。

## 名稱放在哪裡

曲線的名稱放在線的末端，依序試右下、左上、左下、右上，再試其他空位。文字沒有碰到任何曲線、輔助線、箭頭、圓點、座標軸或其他標籤，這個位置才算空。點的名稱放在圓點旁邊。

## 預設移動標籤

<span id="sec-nudges"></span>

`[macro.label.<group>]` 預設移動一組中的每個標籤。分組依標籤所指的對象而定。

| 分組 | 對象 |
| --- | --- |
| `point` | 圓點：均衡點與路徑點（`A`、`A'`、`B`） |
| `curve` | 在末端命名的曲線（`IS`、`LM`、`AD`、`AS`、`ZZ`） |
| `mark` | 圖上的數值與記號 |
| `region` | 填色區域中的名稱 |
| `annotation` | 其他所有文字：大括號、移動量、註記 |

```toml
[macro.label.point]
top = "2pt"      # 還有 bottom、left、right；單位 pt、mm、cm 或 in
```

座標軸標題與軸上記號不屬於任何分組，不能移動。
