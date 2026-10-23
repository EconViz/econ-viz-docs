---
seo_title: "更新紀錄"
---

<span id="sec-changelog"></span>

# 更新紀錄

本章列出影響套件使用的版本變更，不含僅修改文件的版本；各條目依 l3doc 慣例標註於它所描述的功能旁，頁碼即該功能的實際頁碼。

## 2.0.0b8

- `Label` — 新增 `top`、`bottom`、`left` 與 `right`，可微調已定位的單一標籤 [Canvas 畫布](../guides/canvas.md)
- `themes` — 內建主題改為 EconViz 共用主題，同一名稱在各 EconViz 套件中外觀一致；新增 `manual` 主題 [主題與設定](../guides/themes.md)
- `themes` — 移除 `dark` 主題：`themes.dark` 與 `base = "dark"` 會發出警告並改用 `default` [主題與設定](../guides/themes.md)
- `Config` — utility-viz 自身的設定移至 `[utility]` 下；改由 `mosaickit` 讀取並檢查檔案；舊格式仍可讀取，但會發出警告 [主題與設定](../guides/themes.md)
- `utility-viz init` — 改寫出新格式，utility-viz 的表格位於 `[utility]` 下；`--migrate` 會把表格移到該處 [命令列工具](../getting-started/cli.md)
- `utility-viz plot` — `--theme` 接受所有內建主題，包括 `colorblind` 與 `manual`；`dark` 會發出警告並改用 `default` [命令列工具](../getting-started/cli.md)

## 2.0.0b7

- `Config` — 設定檔恢復為 `econ-viz.toml`，由所有 EconViz 套件共用；`utility-viz.toml` 仍可讀取，但會發出警告 [主題與設定](../guides/themes.md)
- `utility-viz plot` — 未指定 `--config` 時，讀取目前目錄的 `econ-viz.toml`（或 `utility-viz.toml`，並發出警告） [命令列工具](../getting-started/cli.md)

## 2.0.0b1

- 由 `econ-viz` 更名為 `utility-viz`：發行套件、匯入名稱、指令與設定檔一併更名 [簡介](../guides/introduction.md)
- 內部結構重整為 `core` 與 `models`；公開 API 為套件根目錄與 `utility_viz.models` [簡介](../guides/introduction.md)
- 新增依賴 `mosaickit` 與 `bezierkit` [簡介](../guides/introduction.md)
- 整個儲存庫通過 `mypy` 檢查；Ruff 限制行長、複雜度與陳述式數量 [簡介](../guides/introduction.md)
- `utility-viz` — 新增依賴 `mosaickit>=0.5.1,<0.6.0` 與 `bezierkit>=0.5.0rc1,<0.6.0` [安裝](../getting-started/installation.md)
- `utility-viz` — 儲存庫改為 `uv` workspace，`utility-viz` 與 `econ-viz` 同步發布 [安裝](../getting-started/installation.md)
- `econ-viz` — 更名為 `utility-viz`；`econ_viz` 套件、`econ-viz` 指令與 `econ-viz.toml` 查找保留為已棄用的相容層，於 3.0.0 移除 [安裝](../getting-started/installation.md)
- `econ-viz` — 相容層改由獨立的 `econ-viz` 發行套件提供，升級 1.x 安裝時不再刪除與 `utility-viz` 共用的檔案 [安裝](../getting-started/installation.md)
- `UtilityVizError` — `UtilityVizError` 成為基礎例外類別；`EconVizError` 保留為同一類別的別名 [快速開始](../getting-started/quickstart.md)
- `Leontief` — 折角效用函數的無異曲線在 Matplotlib 與 TikZ 輸出中保留精確直角 [核心模型](../models/index.md)
- `core.scenes` — 新增與後端無關的 `mosaickit` 圖層工廠，涵蓋預算線、均衡與無異曲線，並可匯出原生 Bézier TikZ [進階模型](../models/advanced.md)
- `Config` — 預設設定檔更名為 `utility-viz.toml`；舊的 `econ-viz.toml` 仍可讀取，但會發出警告 [主題與設定](../guides/themes.md)
- `Config.discover` — 新增 `Config.discover()`，找不到檔案時改用內建預設值 [主題與設定](../guides/themes.md)
- `utility-viz` — 指令改為 `utility-viz`；`econ-viz` 會印出棄用警告並轉交給新指令 [命令列工具](../getting-started/cli.md)
- `utility-viz plot` — 未指定 `--config` 時，讀取目前目錄的 `utility-viz.toml`（或舊的 `econ-viz.toml`） [命令列工具](../getting-started/cli.md)
- `utility-viz init` — 新增 `--migrate` 選項 [命令列工具](../getting-started/cli.md)
- `Animator` — 移至 `utility_viz.core.animation` [動畫](../guides/animation.md)
- `WidgetViewer` — 移至 `utility_viz.core.interactive` [互動元件](../guides/interactive.md)

## 1.12.0

- 新增無異曲線主次層級、焦點曲線及數值或序數標籤 [簡介](../guides/introduction.md)
- `Canvas.add_utility` — 新增焦點效用層級、次要曲線樣式及序數標籤 [Canvas 畫布](../guides/canvas.md)
- `Theme` — 新增次要無異曲線的顏色、線寬與透明度設定 [主題與設定](../guides/themes.md)

## 1.11.0

- 完成主題系統，統一畫布、多面板圖、需求圖、效果分解與 Edgeworth 箱形圖的視覺設定 [簡介](../guides/introduction.md)
- `Canvas` — 背景、標籤、線條與標記均由主題提供預設值 [Canvas 畫布](../guides/canvas.md)
- `Figure` — 面板背景、標籤、線條與標記完整套用主題 [多面板圖與需求圖](../guides/consumer.md)
- `EdgeworthBox` — 箱框、契約曲線、核、稟賦、價格線與 Walras 均衡完整套用主題 [多面板圖與需求圖](../guides/consumer.md)
- `Theme` — 完成主題系統，新增背景色、標籤比例及所有經濟圖層的預設樣式 [主題與設定](../guides/themes.md)
- `themes` — 新增 `paper`、`monochrome`、`presentation` 與 `dark` [主題與設定](../guides/themes.md)
- `Config` — 設定檔可選用所有內建主題，並在各種圖形間保留相同的視覺語意 [主題與設定](../guides/themes.md)
- `econ-viz plot` — `--theme` 支援所有命令列內建主題 [命令列工具](../getting-started/cli.md)

## 1.10.1

- 套件加入 `py.typed`，並在 CI 執行 Ruff 與 Mypy 檢查 [簡介](../guides/introduction.md)

## 1.10.0

- `econ-viz` — Python 3.10 使用 `tomli` 讀取 TOML 設定檔 [安裝](../getting-started/installation.md)
- `Figure` — 未指定主題與字型時，使用目前的 `Config` [多面板圖與需求圖](../guides/consumer.md)
- `EdgeworthBox` — 未指定主題與字型時，使用目前的 `Config` [多面板圖與需求圖](../guides/consumer.md)
- `Config` — 新增 `Config`、`econ-viz.toml`、`econ-viz init` 與 `plot --config` [主題與設定](../guides/themes.md)
- `econ-viz init` — 新增設定檔範本指令與 `plot --config` [命令列工具](../getting-started/cli.md)

## 1.9.0

- `Canvas` — 座標軸、原點、標題與其他文字元素接受 `Label` [Canvas 畫布](../guides/canvas.md)
- `Stroke` — 新增 `opacity` 透明度 [Canvas 畫布](../guides/canvas.md)
- `DemandDiagram` — 支援 `Legend`、`Marker`、`Label` 與各圖層的 `Stroke` [多面板圖與需求圖](../guides/consumer.md)
- `Canvas.add_decomposition` — 預設繪製 A、B、C 所在的無異曲線，並支援曲線標籤與 `Legend` [多面板圖與需求圖](../guides/consumer.md)
- `Canvas.add_decomposition` — 橫軸下方的效果箭頭依 A→B、B→C 方向繪製；效果為零時不繪製箭頭 [多面板圖與需求圖](../guides/consumer.md)
- `Haagsma` — 新增具有閉式解的 Haagsma 效用模型，用於劣等財與季芬財分析 [核心模型](../models/index.md)

## 1.8.0

- `Canvas` — 新增 `Axis`、`Marker`、`Label` 與 `Fill` 樣式物件 [Canvas 畫布](../guides/canvas.md)
- `Stroke` — 線條樣式統一由 `Stroke` 表示；個別樣式參數保留為簡寫 [Canvas 畫布](../guides/canvas.md)
- `Canvas.add_decomposition` — 新增 `Effect`、`Marker` 與 `Label` 樣式物件 [多面板圖與需求圖](../guides/consumer.md)
- `EdgeworthBox` — 標記點、文字與座標軸接受 `Marker`、`Label` 與 `Axis` [多面板圖與需求圖](../guides/consumer.md)

## 1.7.0

- CI 測試 Python 3.10–3.13，強制分支覆蓋率，並對可執行的範例做冒煙測試 [簡介](../guides/introduction.md)
- 版本標籤須通過測試後才會觸發發布 [簡介](../guides/introduction.md)
- `econ-viz` — 套件管理與建置改用 `uv` [安裝](../getting-started/installation.md)
- `econ-viz` — 修正範例腳本，使其可在新簽出的原始碼目錄中直接執行 [安裝](../getting-started/installation.md)
- `Canvas` — 支援個別設定各圖的文字與數學字型，不影響 `matplotlib` 的全域設定 [Canvas 畫布](../guides/canvas.md)
- `Canvas` — `Canvas` 與 `Figure` 支援分別設定座標軸標籤位置、線條樣式與箭頭樣式 [Canvas 畫布](../guides/canvas.md)
- `Stroke` — 統一控制畫布、多面板圖、需求圖與 Edgeworth 箱形圖中線條的粗細、樣式、顏色與箭頭 [Canvas 畫布](../guides/canvas.md)
- `CobbDouglas` — 修正效用模型的定義域、非對稱 CES 的擴張路徑、Cobb-Douglas 的極限情況，以及所得未花完時的飽和最適解 [核心模型](../models/index.md)
- `CobbDouglas` — 修正效用值接近零或為負時的等高線水準計算 [核心模型](../models/index.md)
- `comparative_statics` — 修正價格、所得接近零或基本需求限制時，比較靜態計算超出定義域的問題 [分析](../tools/analysis.md)
- `econ-viz` — 新增 `econ-viz --version`，顯示已安裝的套件版本 [命令列工具](../getting-started/cli.md)

## 1.6.0

- `examples/output/` 的產出檔案不再納入版本控制 [簡介](../guides/introduction.md)
- `Canvas` — 無異曲線的預設線寬從 `2.0` 降為 `1.8` [Canvas 畫布](../guides/canvas.md)
- `themes.default` — 預設配色改為色盲友善，並提供 `COLORBLIND_CYCLE_RGB` 與 `COLORBLIND_CYCLE_HEX` [主題與設定](../guides/themes.md)
- `Canvas.save` — TikZ 座標軸的回歸測試不再依賴顏色索引 [匯出](../guides/export.md)
- `Animator` — 動畫範例移到 `examples/scripts/animation.py` [動畫](../guides/animation.md)

## 1.5.0

- 新增效果分解、需求圖、PCC/ICC 路徑、多面板版面與 TikZ 匯出的範例腳本 [簡介](../guides/introduction.md)
- 新增 TikZ 匯出與價格效果分解的回歸測試 [簡介](../guides/introduction.md)
- `econ-viz` — Colab 上的筆記本安裝流程在重新啟動後也能正常運作 [安裝](../getting-started/installation.md)
- `Figure` — 改善共用面板版面中座標軸標籤的位置與可見度 [多面板圖與需求圖](../guides/consumer.md)
- `decompose_price_effect` — 價格效果分解：`decompose_price_effect()`、`PriceEffectDecomposition` 與 `Canvas.add_decomposition()`，可畫出 A/B/C 消費組合以及替代與所得效果 [多面板圖與需求圖](../guides/consumer.md)
- `decompose_price_effect` — 效果分解的 API 可以直接從套件根目錄匯入 [多面板圖與需求圖](../guides/consumer.md)
- `Canvas.save` — 純 TikZ 匯出後端；`Canvas.save()` 與 `Figure.save()` 接受 `.tex` [匯出](../guides/export.md)

## 1.4.0

- 新增 `Animator` 與 `WidgetViewer` 的測試 [簡介](../guides/introduction.md)
- `econ-viz[extras]` — 新增選用依賴 `animation`、`interactive` 與 `all` [安裝](../getting-started/installation.md)
- `Animator.save` — 匯出前將影格合成至不透明背景，改善 GIF 匯出穩定性 [匯出](../guides/export.md)
- `Animator` — `Animator` 以 `Pillow` 產生 GIF 參數變動動畫，不需要 `ffmpeg` [動畫](../guides/animation.md)
- `Animator` — 新增效用參數、價格、所得與僅顯示預算線的 GIF 範例 [動畫](../guides/animation.md)
- `WidgetViewer` — `WidgetViewer` 在 Jupyter 筆記本中提供滑桿控制 [互動元件](../guides/interactive.md)
- `WidgetViewer` — 筆記本互動元件新增數值輸入欄位 [互動元件](../guides/interactive.md)

## 1.3.2

- 發布流程略過 PyPI 上已有的版本 [簡介](../guides/introduction.md)
- `EdgeworthBox` — Edgeworth 契約曲線與價格線預設為黑色虛線 [多面板圖與需求圖](../guides/consumer.md)

## 1.3.1

- 套件根目錄的匯出改為延遲載入，公開 API 不變 [簡介](../guides/introduction.md)
- `Canvas` — Canvas 的繪製拆成 `canvas.renderers` 與 `canvas.primitives` [Canvas 畫布](../guides/canvas.md)
- `EdgeworthBox` — Edgeworth 的內部實作拆成 compute、state 與 plotter 三個模組 [多面板圖與需求圖](../guides/consumer.md)
- `models.registry` — 新增模型註冊表（`models.registry`），供命令列工具建立模型 [核心模型](../models/index.md)
- `CobbDouglas` — 等高線水準的規則集中在 `contours.level_policies` [核心模型](../models/index.md)
- `Canvas.save` — `Canvas`、`Figure` 與 `EdgeworthBox` 共用同一個圖形匯出器（`io.exporter`） [匯出](../guides/export.md)
- `econ-viz` — 命令列錯誤改為拋出 `CliConfigError`，結束處理集中在 `cli.main` [命令列工具](../getting-started/cli.md)

## 1.3.0

- `examples/edgeworth_box.py` 涵蓋常見的效用函數組合 [簡介](../guides/introduction.md)
- 新增 Edgeworth 測試 [簡介](../guides/introduction.md)
- `EdgeworthBox` — 新增 `EdgeworthBox` 與 `EquilibriumFocusConfig`，支援兩人交換經濟繪圖 [多面板圖與需求圖](../guides/consumer.md)
- `EdgeworthBox` — 契約曲線、核、Walras 均衡疊圖，以及聚焦於均衡的無異曲線 [多面板圖與需求圖](../guides/consumer.md)

## 1.2.3

- `slutsky_matrix` — `SlutskyMatrix` 會檢查對稱性、負半定性與齊次性，條件不成立時發出警告 [分析](../tools/analysis.md)
- `econ-viz models` — 命令列工具支援 `QuasiLinear`、`StoneGeary` 與 `Translog` [命令列工具](../getting-started/cli.md)

## 1.2.2

- 新增 PCC/ICC 範例產生器與測試 [簡介](../guides/introduction.md)
- `PricePath` — PCC/ICC 路徑預設經過平滑處理，端點略微延長，除非指定否則不顯示標記 [多面板圖與需求圖](../guides/consumer.md)
- `PricePath` — PCC/ICC 路徑改用獨立配色，並增加需求圖商品空間的留白 [多面板圖與需求圖](../guides/consumer.md)

## 1.2.0

- `Layout` — 多面板 `Figure` 版面與 `Layout` 列舉 [多面板圖與需求圖](../guides/consumer.md)
- `PricePath` — 新增 `PricePath`、`IncomePath` 與 `Canvas.add_path()`，支援 PCC/ICC 繪圖 [多面板圖與需求圖](../guides/consumer.md)
- `DemandDiagram` — 新增 `DemandDiagram`，連動顯示商品空間與 Marshall 需求 [多面板圖與需求圖](../guides/consumer.md)

## 1.1.0

- `Translog` — `Translog` 模型，以及圖例與無異曲線標籤 [核心模型](../models/index.md)
- `comparative_statics` — `comparative_statics` 輔助函數 [分析](../tools/analysis.md)
- `HomogeneityAnalyzer` — 分析模組中的 `HomogeneityAnalyzer` 與 `ReturnsToScale` [分析](../tools/analysis.md)

## 1.0.2

- `econ-viz` — 移除 NumPy 的版本上限，避免在 Colab 上發生衝突 [安裝](../getting-started/installation.md)
- `Canvas` — 數學式的座標軸標籤不再被重複包裝 [Canvas 畫布](../guides/canvas.md)

## 1.0.1

- `econ-viz` — 固定 `numpy<2`，避免 Colab 與本機安裝時 ABI 不相容 [安裝](../getting-started/installation.md)
- `econ-viz` — 放寬 Python 與 NumPy 的版本限制；`pytest` 固定在 8.x [安裝](../getting-started/installation.md)

## 1.0.0

- 首次發布 [更新紀錄](changelog.md)

