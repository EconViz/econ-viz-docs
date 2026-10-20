---
seo_title: "輸出格式"
---

# 輸出格式

<span id="sec-outputs"></span>

| 格式 | 能力 | 保留內容 |
| --- | --- | --- |
| 動態 SVG | `vector` | 原生 2D 向量；可重現的 3D 投影 |
| GIF | `raster` | 串流影格，最高 1200 DPI |
| HTML | `interactive` | 播放器控制、互動，以及原生 2D 或 3D 顯示 |

<!-- api: agora.kinetickit.guides_outputs_1 -->

不可變的匯出報告，記錄格式、產生的檔案、尺寸、長度、保留的語意、降級功能、警告與網路依賴。

<!-- api: agora.kinetickit.guides_outputs_2 -->

回傳目前已安裝選用依賴所能提供的輸出格式。

<!-- api: agora.kinetickit.guides_outputs_3 -->

透過匯出器登錄表輸出動畫的底層入口；一般使用者通常呼叫 `Animation.save()`。

<!-- api: agora.kinetickit.guides_outputs_4 -->

宣告繪圖端支援哪些場景維度、互動、字型功能與封裝方式。

<!-- api: agora.kinetickit.guides_outputs_5 -->

KineticKit 分析場景、動作、互動與無障礙資料後，整理出的動畫需求。

<!-- api: agora.kinetickit.guides_outputs_6 -->

在寫入任何目的檔之前，計算動畫所需的 `Requirements`。

動態 SVG 採用 SVG 的向量場景模型 [{W3C} (2018)](../project/references.md#svg2) 與宣告式 SMIL 時序元素 [{W3C} (2008)](../project/references.md#smil3)。KineticKit 會寫入明確的數值與時間，播放時不需要 Python。

## GIF 設定

<!-- api: agora.kinetickit.guides_outputs_7 -->

控制 GIF 的影格率、調色盤、遞色、循環、處置方式、尺寸與 DPI。

<!-- api: agora.kinetickit.guides_outputs_8 -->

把已編碼的 PNG 影格串流寫入 GIF，不必把所有解碼後的影格留在記憶體。

GIF 不接受短於 10 毫秒的影格間隔。時間會分配到整數百分之一秒，同時維持指定的總長度。點陣工作量過大時會發出 `RenderCostWarning`，不會暗中降低尺寸或 DPI。

## HTML 封裝

`packaging="offline"` 會內嵌執行環境，不需要網路；`packaging="compact"` 會引用固定版本的 CDN 資源，並把網址寫進清單。沒有 JavaScript 時仍有替代內容：2D 使用內嵌 SVG，3D 則顯示最後狀態的靜態 SVG。
