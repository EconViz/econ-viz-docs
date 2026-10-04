---
seo_title: "從 econ-viz 遷移"
description: "econ-viz 在 2.0 更名為 utility-viz：有哪些變動、該安裝哪個套件，以及相容層在 3.0 之前如何運作。"
---

# 從 econ-viz 遷移

`econ-viz` 在 2.0.0 更名為 **utility-viz**。

!!! warning "utility-viz 2.0 目前為 Beta 版"

    2.0.0b1 是預先發行版（pre-release）。在 2.0 正式版釋出之前，穩定版仍是 `econ-viz` 1.x。
    安裝預先發行版需要加上 `--pre`，例如 `pip install --pre utility-viz`。

## 變動一覽

| | 1.x | 2.x |
|---|---|---|
| 發行套件 | `pip install econ-viz` | `pip install utility-viz` |
| 匯入 | `import econ_viz` | `import utility_viz` |
| 命令列 | `econ-viz` | `utility-viz` |
| 設定檔 | `econ-viz.toml` | `utility-viz.toml`（區段名稱不變） |

## 該安裝哪個套件

`utility-viz` 只包含 `utility_viz` 與 `utility-viz` 指令，不含 `econ_viz` 套件，也沒有 `econ-viz` 指令。

`econ-viz` 2.x（版本號相同）是一個輕量的相容發行套件。執行 `pip install econ-viz` 會安裝同版本的 `utility-viz`，
再加上 `econ_viz` 套件與 `econ-viz` 指令，兩者都會提示已被棄用。因此，用
`pip install --upgrade econ-viz` 升級既有的 1.x 環境仍可正常運作，並會把你帶到 2.x。
預先發行版需要加上 `--pre`，例如 `pip install --pre --upgrade econ-viz`。

準備好不再依賴相容層時，再改裝 `pip install utility-viz` 即可。

## 相容層

在整個 2.x 期間，`econ-viz` 發行套件都會提供 `econ_viz` 套件與 `econ-viz` 指令，讓文件中記載的 1.x 程式碼繼續可用：

- `import econ_viz` 每個行程只會發出一次棄用警告。
- `from econ_viz import ...` 以及文件中記載的子模組（`econ_viz.models`、`econ_viz.optimizer`、
  `econ_viz.themes` 等）會對應到 `utility_viz` 中的同名項目；名稱沒有變動的，就是同一個物件。
- 建立 `econ_viz.Canvas`、`econ_viz.Figure` 或 `econ_viz.animation.Animator`，或存取 `econ_viz.Layout` 時，
  會發出 `utility_viz.UtilityVizDeprecationWarning`（屬於 `FutureWarning`），訊息會註明
  「deprecated since 2.0.0, removed in 3.0.0」以及替代寫法。`Figure`、`Layout` 與 `Animator` 會對應到 2.x 現有的
  等價物件；它們的宣告式替代方案（`CanvasGrid`、`Animation`）尚在規劃中，訊息中也會如此標示。
- 設定檔的查找順序：明確指定的路徑、`utility-viz.toml`、舊版 `econ-viz.toml`（會發出警告），最後是預設值。
  兩個檔案同時存在時，以新檔案為準，並以警告提示舊檔案已被忽略。
  不帶引數的 `Config.load()` 依上述檔案順序查找，兩個檔案都不存在時會拋出錯誤（與 1.x 相同）；
  `Config.discover()` 則會退回預設值；`Config.load("file.toml")` 只讀取該檔案。
  未指定 `--config` 時，`utility-viz plot` 會在目前目錄套用相同的查找順序。
- `econ-viz` 指令會印出棄用警告，然後轉交給 `utility-viz` 執行。
- `utility-viz init --migrate` 會依據 `econ-viz.toml` 產生 `utility-viz.toml`，並保留舊檔案。

## 移除時程（3.0.0）

`econ_viz` 套件、`econ-viz` 指令與 `econ-viz.toml` 的查找功能會在 3.0.0 移除，而不是 2.0.0。

相容範圍僅限文件中記載的 1.x 公開 API。未記載的深層模組路徑（例如 `econ_viz.canvas.renderers.*`）
只會盡力對應，隨時可能消失。`utility_viz.core.*` 內部模組屬於進階 API，不在相容保證之內。
