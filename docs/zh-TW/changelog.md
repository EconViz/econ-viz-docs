---
seo_title: "更新紀錄"
description: "econ-viz Python 套件的版本歷史：每個版本的新功能、修正與變更。"
---

# 更新紀錄

本頁同步自專案的 `CHANGELOG.md`。

## v1.4.0 (2026-04-10)

### 新功能

- 新增 `Animator` GIF 匯出範例，涵蓋四種標準效用函數的參數、價格與所得變動
- 新增只有預算線的變動範例，讓教學頁面能單獨呈現預算限制的移動
- `WidgetViewer` 在滑桿旁邊新增數字輸入框，方便在筆記本中使用

### 修正

- 匯出前先把每一格疊在白色背景上，避免 GIF 影格殘影堆疊
- 讓安裝儲存格可以安全地重新啟動，改善 Playground 筆記本在 Colab 上的安裝流程

<div class="media-grid" markdown>
  <figure class="gif-card">
    <img src="../../assets/animation/price_sweeps/cobb_douglas_price_sweep.gif" alt="Cobb-Douglas 價格變動 GIF">
    <figcaption>Cobb-Douglas 價格變動：效用函數固定，預算線移動。</figcaption>
  </figure>
  <figure class="gif-card">
    <img src="../../assets/animation/income_sweeps/budget_only_income_sweep.gif" alt="只有預算線的所得變動 GIF">
    <figcaption>只有預算線的所得變動，用來單獨呈現預算線的移動。</figcaption>
  </figure>
</div>

## v1.2.0 (2026-03-30)

### 新功能

- 新增多面板 `Figure` 版面與 `Layout` 列舉（closes #7）
- 新增連動的 `DemandDiagram`，用於 Marshall 需求教學圖（closes #31）
- 新增 `PricePath` / `IncomePath` 工具與 `Canvas.add_path()`，用來畫 PCC / ICC（closes #5）

![v1.2.0 需求圖功能](../assets/consumer/demand_cobb_douglas.png)

## v1.1.0 (2026-03-30)

### 新功能

- 新增 `comparative_statics` 工具（closes #12）
- 在分析子模組新增 `HomogeneityAnalyzer` 與 `ReturnsToScale`（closes #14）
- 新增 `Translog` 模型（#9），並支援圖例與無異曲線標籤（#11）

## v1.0.2 (2026-03-29)

### 錯誤修正

- 避免數學座標軸標籤被重複包裝（closes #2）
- 移除 NumPy 的版本上限，避免在 Colab 環境中發生衝突

## v1.0.1 (2026-03-29)

### 錯誤修正

- 鎖定 `numpy<2`，避免在 Colab 與本機安裝時發生 ABI 不相容

### 雜項

- 放寬 Python / NumPy 版本限制，並把 `pytest` 鎖定在 8.x

### 文件

- 在 README 加入 Stone-Geary，並更新測試數量徽章

## v1.0.0 (2026-03-28)

- 首次發布
