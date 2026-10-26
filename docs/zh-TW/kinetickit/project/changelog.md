---
seo_title: "變更紀錄"
---

# 變更紀錄

<span id="sec-changelog"></span>

本文件涵蓋的 `kinetickit` 版本。

## 1.0.0b2（2026-10-19）

- GlyphKit（`>=1.0.0b2,<2`）隨 KineticKit 一起安裝，並負責所有字型處理。`kinetickit.integrations.glyphkit` 轉接器仍是唯一的匯入界線，核心匯入維持延遲載入，中性的文字契約也沒有改變（參見[文字排版](../guides/typography.md#sec-typography)）。
- 新增 `export_png_frames(...)`，把已編碼的 PNG 影格串流寫成 GIF，並精確分配百分之一秒的誤差（參見[輸出格式](../guides/outputs.md#sec-outputs)）。

## 1.0.0b1（2026-10-13）

- 第一個 1.0 測試版。[相容性](../compatibility.md)中的動作、場景、繪圖端、匯出器與成品契約都打算保持穩定，但在預發行版本之間仍可能改變。
- 可重現的時間軸、標準與三次 Bézier 緩動、關鍵影格與流暢的動作樹（參見[時間與緩動](../guides/time-easing.md#sec-kinetic-time)）。
- 2D 與 3D 場景、路徑、網格與曲面變形，以及依穩定編號配對的場景轉場（參見[場景與動作](../guides/scenes-motion.md#sec-scenes-motion)）。
- 動態 SVG、串流 GIF 與互動 HTML 輸出，寫檔前先做能力檢查（參見[輸出格式](../guides/outputs.md#sec-outputs)）。
- 互動、無障礙中繼資料與一致性測試套件（參見[無障礙與互動](../guides/accessibility.md#sec-accessibility)）。

測試版已知的限制列在[輸出格式](../guides/outputs.md#sec-outputs)。
