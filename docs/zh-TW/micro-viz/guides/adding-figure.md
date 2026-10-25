---
seo_title: "新增圖形"
---

# 新增圖形

<span id="sec-adding"></span>

要做哪些圖由儲存庫的 issue 與里程碑決定。統計資料圖與方塊加箭頭的流程圖不畫。新增一張圖有五個步驟。

1. **模型。** 把方程式放進 `micro_viz/<主題>.py` 的凍結 dataclass，檢查輸入並丟出套件錯誤的子類別，不引入任何繪圖套件。
2. **繪圖函式。** 寫 `micro_viz/visuals/<主題>.py`。`Plane` 收集曲線、輔助線、點、標記、區域與箭頭，並給它們穩定的圖層編號（`micro.<前綴>.<種類>.<序號>`）。
3. **文字。** 把文字加進 `locale/labels.json` 的三種語言，繪圖函式裡**不寫**顯示文字。
4. **匯出與範例。** 把名稱加進 `micro_viz/__init__.py`、`visuals/__init__.py` 與 `tests/test_package.py`；用 `common.py` 共用的 `parser` 與 `Session` 寫 `examples/scripts/<主題>.py`，讓範圍與選項都是參數。
5. **測試與更新紀錄。** 測模型、參數改變時圖會跟著變、`title=None` 不畫標題、標籤找得到空位，以及範例能執行。

```python
from micro_viz.visuals.plane import Plane, linear, sample


def demand_canvas(intercept: float, slope: float, x_max: float, *, title: str | None = None):
    plane = Plane(
        prefix="demo",
        x_label="Q",
        y_label="p",
        x_max=x_max,
        y_max=intercept,
        title=title,
    )
    plane.line(linear(intercept, -slope, x_max), plane.t("monopoly.demand"))
    return plane.finish()
```

## 慣例

- 變動後的曲線是細實線，**不用虛線**。平行移動用直的箭頭從舊的點指向新曲線；彎箭頭只代表旋轉。
- 曲線名稱放在線的末端，點標籤放在點旁，任何東西都不重疊。
- 移動方向的邏輯放在 `visuals/movement.py`。
- 主題一律白底，隨附範例使用 `manual`。

## 檢查

```bash
uv run ruff check . && uv run ruff format --check .
uv run mypy
uv run pytest
```
