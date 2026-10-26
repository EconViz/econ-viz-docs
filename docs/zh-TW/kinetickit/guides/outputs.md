---
seo_title: "輸出格式"
---

# 輸出格式

<span id="sec-outputs"></span>

同一個場景與同一段動作可以驅動所有輸出，由目的檔的副檔名決定格式。

| 格式 | 能力 | 2D | 3D | 互動 | 保留向量 |
| --- | --- | :-: | :-: | :-: | :-: |
| 動態 SVG | `vector` | 是 | 投影（取樣） | 否 | 是（2D） |
| GIF | `raster` | 是 | 投影 | 否 | 否 |
| HTML | `interactive` | 是（原生 SVG 與播放器） | 是（原生 3D，可旋轉與縮放） | 是 | 2D 是 |

<!-- api: kinetickit.guides_outputs_1 -->

不可變的匯出報告，記錄格式、繪圖端、輸出目標、尺寸、長度、保留或降級的功能、警告與網路依賴。

<!-- api: kinetickit.guides_outputs_2 -->

回傳已登錄的輸出格式 `('gif', 'html', 'svg')`。它不檢查選用依賴：沒有 `kinetickit[raster]` 時存成 GIF，會拋出附有安裝提示的 `CapabilityError`。

<!-- api: kinetickit.guides_outputs_3 -->

匯出器登錄表的底層入口。一般使用者通常呼叫 `Animation.save()`。

<!-- api: kinetickit.guides_outputs_4 -->

宣告繪圖端支援哪些場景維度、幾何、功能、輸出與互動。

<!-- api: kinetickit.guides_outputs_5 -->

KineticKit 由場景、動作、互動與無障礙資料推算出的動畫所需能力。

<!-- api: kinetickit.guides_outputs_6 -->

在寫入任何檔案之前，先算出動畫的 `Requirements`。每次匯出都會先拿它和繪圖端的能力比對：不支援的組合會拋出 `CapabilityError`，指出缺少的能力並附上提示，匯出失敗時也不會留下任何檔案。

動態 SVG 採用 SVG 的向量場景模型 [{W3C} (2018)](../project/references.md#svg2) 與宣告式 SMIL 時序 [{W3C} (2008)](../project/references.md#smil3)。KineticKit 會寫入明確的數值與時間，播放時不需要 Python。

## 選項
<span id="sec-options"></span>

`save()` 會把關鍵字選項交給所選的輸出。

| 輸出 | 選項 |
| --- | --- |
| SVG | `width`、`height`、`loop`（預設 `False`）、`title`、`description`、`samples`、`embed_fonts`、`reduced_motion`、`degradation` |
| GIF | `width`、`height`、`fps`、`dpi`、`loop`、`colors`、`dither`、`palette`、`disposal`、`accessibility`、`description` |
| HTML | `width`、`height`、`packaging`、`autoplay`、`loop`、`speed`、`controls`、`fps`、`max_frames`、`title`、`description`、`lang` |

`loop=True` 讓 SVG 無限重播，放在網頁上的動畫通常需要這個。GIF 預設無限重播，除非設成 `loop=None`。不認得的選項名稱會拋出錯誤。

## GIF 設定

<!-- api: kinetickit.guides_outputs_7 -->

選項中屬於 GIF 的部分：影格率、調色盤、遞色、循環、處置方式與無障礙文字。

<!-- api: kinetickit.guides_outputs_8 -->

把已編碼的 PNG 影格串流寫入 GIF，不必把所有解碼後的影格留在記憶體。

點陣輸出一次只畫一張影格，所以記憶體不會隨長度成長。DPI 最高到 1200。GIF 不接受短於 10 毫秒的影格間隔。時間會分配到整數百分之一秒，並把誤差往後帶，所以總長度維持正確。點陣工作量過大時會發出 `RenderCostWarning`，不會偷偷降低尺寸或 DPI。

## HTML 封裝

`packaging="offline"` 會內嵌執行環境，不需要網路；`packaging="compact"` 會引用固定版本的 CDN 資源，並把網址寫進 `ExportManifest.network_dependencies`。2D 場景是內嵌的動態 SVG，由一個沒有外部依賴的小型播放器驅動：播放、暫停、跳轉、逐格、速度、循環與標記，可用鍵盤操作，也能平移與縮放。3D 場景會依 `fps`（預設 30，最多 `max_frames` 張）預先取樣，由私有的繪圖執行環境顯示，並支援原生的旋轉與縮放。

## 能力說明

- **向量 3D** 是隨時間變化的 2D 投影，著色是平面烘焙的，繪製順序（畫家演算法）在 $t = 0$ 固定。如果有圖元進入或離開視野，它會失敗，而不是亂猜。
- **1.0.0b2 不支援：**影片編碼、音訊、物理、多面板版面、隱函數曲面、3D 文字、拖曳互動，以及 3D 場景上的動態疊層。

## 沒有 JavaScript 或動態時的替代方案

| 情況 | 行為 |
| --- | --- |
| 沒有 JavaScript 的 2D HTML | 內嵌的 SVG 以原生方式（SMIL）播放一次；控制項無作用 |
| 沒有 JavaScript 的 3D HTML | `<noscript>` 區塊顯示最後狀態的靜態 SVG |
| 當作 `<img>` 使用的 SVG | 動畫會播放；腳本（包括減少動態的處理）會被忽略 |
| GIF | 沒有執行時的語意；使用輸出清單的說明與代表性 PNG |
| `prefers-reduced-motion` | 不自動播放；顯示代表性狀態（預設是最後一格）；仍可按播放 |

## 各格式保留什麼

每次匯出的 `ExportManifest.preserved` 與 `.degraded` 都會列出這份資訊。

| 語意 | SVG | HTML | GIF |
| --- | --- | --- | --- |
| 標題、說明 | 有 | 有 | 只在輸出清單 |
| 角色、標籤、說明文字 | 有（`role`、`aria-label`、`<title>`、`<desc>`） | 有 | 無 |
| 閱讀順序 | `data-kk-order`（DOM 順序是疊放順序） | 有（依序的文字清單） | 無 |
| 可用鍵盤操作的控制項 | 不適用 | 有（原生按鈕、滑桿、選單） | 不適用 |
| 互動 | 依政策捨棄，標為 `required` 時報錯 | 有 | 依政策捨棄，或報錯 |
| 字型 | 以 `@font-face` 嵌入子集 | 透過內嵌的 SVG | 畫進像素 |
| 穩定的物件編號 | `data-kk-id` | `data-kk-id` 與 `objects` 對照表 | 不適用 |

投影後的 3D 輸出只保留可繪製節點的編號，群組與光源沒有自己的元素。
