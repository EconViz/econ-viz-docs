---
seo_title: "更新紀錄"
---

<span id="sec-changelog"></span>

# 更新紀錄

本章列出影響套件使用的版本變更，不列僅修改文件的版本。依 l3doc 慣例，每個條目都標註在它所描述的功能旁，因此所列頁碼就是該功能的實際頁碼。

## 1.0.0rc6

- 各套件宣告 `econ_toml.Schema`，由 mosaickit 解析 `econ-viz.toml`；新增共用主題（`mosaickit.themes`）與標籤微調（`Nudge`） [簡介](../guides/introduction.md)
- `Nudge` — 新增 [區域標籤與點標籤](../guides/labels.md)
- `Schema` — 新增；套件宣告自己的鍵，由 mosaickit 解析檔案 [主題與設定](../guides/themes.md)
- `get_tokens` — 新增 [主題與設定](../guides/themes.md)

## 1.0.0rc5

- 新增 `mosaickit.econ_toml`，讀取每個 EconViz 套件共用的 `econ-viz.toml` 區段 [簡介](../guides/introduction.md)

## 1.0.0rc4

- 已解析的字型可跨符號連結共用；設定字型後的標題基線與 Matplotlib 的標題一致 [簡介](../guides/introduction.md)

## 1.0.0rc3

- 標題與夾有 `$...$` 數學式的文字改用設定的文字字型排版，中文不再顯示為方框 [簡介](../guides/introduction.md)

## 1.0.0rc2

- 繪製更快，輸出不變：標籤配置、點的檢查與 Matplotlib 的 mathtext 解析改用陣列，並使用只在單次繪製或儲存期間有效的快取 [簡介](../guides/introduction.md)

## 1.0.0rc1

- 移除已棄用的 `Animation` 與 `TextStyle.family`（詳見參數與樣式兩章） [簡介](../guides/introduction.md)
- `TextStyle` — 移除 `family`；改以 `font` 選擇字型，並用 `TextFonts` 換成自己的字型檔。欄位請以名稱傳入；含 `"family": null` 的場景文件仍可載入，指定字型家族名稱的則會被拒絕 [樣式與顏色](../guides/styles.md)
- `Animation` — 移除 0.6.0 起棄用的 `Animation`、`Animation.sweep()` 與 Matplotlib 播放輔助函式；動畫改由 `kinetickit` 負責，`CanvasGrid.sweep()` 與 `canvas.bind()` 仍為每個值畫一格 [參數與網格](../guides/parameters.md)

## 0.9.2

- `TikZ` — `font` 對應到 TeX 字型家族 [樣式與顏色](../guides/styles.md)

## 0.9.1

- `TextStyle` — 新增 `font` 欄位；`family` 棄用 [樣式與顏色](../guides/styles.md)
- `TextFonts` — 新增 `serif` 與 `mono`；預設為 DejaVu [樣式與顏色](../guides/styles.md)

## 0.9.0

- `TextStyle` — `weight` 不再棄用 [樣式與顏色](../guides/styles.md)
- `TextFonts` — 新增；sans 接一份檔案清單 [樣式與顏色](../guides/styles.md)
- `Config` — 新增 `Config.math_font` 與 `Config.fonts` [主題與設定](../guides/themes.md)

## 0.8.0

- `DashStyle` — `DashStyle` 與 `ArrowStyle` 接受簡寫，讓其他套件可直接當作自己的線型與箭頭列舉 [樣式與顏色](../guides/styles.md)

## 0.5.1

- 繪圖區邊緣的標記完整畫出；中心在繪圖區外的標記略過 [圖層與座標軸](../guides/layers.md)

## 0.5.0

- 虛線、點線或點劃線套用在箭身；箭頭維持實線 [圖層與座標軸](../guides/layers.md)
- `CanvasGrid` — 新增 `links` [參數與網格](../guides/parameters.md)

## 0.4.0

- 內側大括號的標籤在尖端外沒有空位時改以引線拉出（先前會重疊並發出警告） [座標軸註記](../guides/annotations.md)

## 0.3.2

- 只有點嚴格位於區域內部時，該區域才算是點自己的區域；位於區域邊上的點，標籤仍放在區域外 [區域標籤與點標籤](../guides/labels.md)

## 0.3.1

- 點標籤可以位於包含其點的填色區域內 [區域標籤與點標籤](../guides/labels.md)

## 0.3.0

- 座標軸標題改放在箭頭尖端之外，不再置中於尖端 [圖層與座標軸](../guides/layers.md)
- `mosaickit` — 座標軸外的文字依欄排列：標記、外側大括號（每條軌道一欄）、註記；標記與註記會沿軸分散，互不重疊 [座標軸註記](../guides/annotations.md)
- 預設主題新增 `axes.note` 角色 [座標軸註記](../guides/annotations.md)
- `mosaickit` — 點標籤先於區域標籤配置，區域的引線標註因此會避開它們；標籤文字依旋轉角度量測 [區域標籤與點標籤](../guides/labels.md)
- `Placement.leader` 可以是 `None` [區域標籤與點標籤](../guides/labels.md)
- 新增 `place_point_label` 與 `place_beside` [區域標籤與點標籤](../guides/labels.md)
- `Palette` — 主題與樣式以色盤名稱指稱顏色，在建立繪製計畫時依 `Config.palette` 解析；未知名稱引發指明角色、欄位與色盤的 `ConfigurationError` [樣式與顏色](../guides/styles.md)
- 新增 `Config.palette`，預設為 `DEFAULT_PALETTE` [主題與設定](../guides/themes.md)
- `Config.load` — TOML 接受 `[palette]` 表，樣式顏色可以是色盤名稱，並在載入檔案時檢查 [主題與設定](../guides/themes.md)
- 新增 `expand`（預設 `True`） [繪製](../guides/rendering.md)

## 0.2.0

- `mosaickit` — 內建繪製器在第一次使用時依名稱載入；核心不再匯入 Matplotlib 後端 [安裝](../installation.md)
- `LayoutWarning` — 新增，在沒有任何引線標註位置能避開所有障礙物時發出 [畫布與場景](../guides/canvas.md)
- 新增 `clip`（預設 `True`）；箭頭不再於路徑末端重畫實線，虛線箭頭因此保持虛線 [圖層與座標軸](../guides/layers.md)
- `anchor` 接受四個角 `top-left`、`top-right`、`bottom-left`、`bottom-right` [圖層與座標軸](../guides/layers.md)
- 箭頭不再被座標軸裁切 [圖層與座標軸](../guides/layers.md)
- 座標軸預設組改畫實心三角箭頭；軸線不受裁切，在繪圖區邊緣保持完整寬度 [圖層與座標軸](../guides/layers.md)
- `mosaickit.layout` — 新增：標籤配置背後的純幾何模組 [配置幾何](../guides/geometry.md)
- `DEFAULT_PALETTE` — 新增：灰階、`white`、`blue`、`red` 與 `teal`；預設主題的顏色取自此色盤，`primary`、`secondary` 與 `accent` 改為藍、紅、青綠 [樣式與顏色](../guides/styles.md)
- `resolve` — `themes.resolve` 接受 `overrides`，在主題之後依序套用 [主題與設定](../guides/themes.md)
- `Layer` — 圖層宣告 `style_slots`；Matplotlib 繪製改由各型別的登錄表驅動 [繪製](../guides/rendering.md)

## 0.1.1

- PyPI 上的套件資訊連結首頁、儲存庫、問題追蹤、更新紀錄與發布說明 [簡介](../guides/introduction.md)

## 0.1.0

- 首次發布：不可變的場景與圖層、稀疏樣式、具命名空間的主題、畫布、可跨格的網格、參數運算式、動畫、以工作為範圍快取的 Matplotlib 繪製，以及嚴格的 TOML 設定 [簡介](../guides/introduction.md)

