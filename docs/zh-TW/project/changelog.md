---
seo_title: "更新紀錄"
description: "econ-viz Python 套件的版本歷史：每個版本的新功能、修正與變更。"
---

# 更新紀錄

`econ-viz` 的版本歷史，不列出只有文件更新的項目。

<table class="ev-changelog">
  <thead>
  <tr><th>版本</th><th>更新內容</th></tr>
  </thead>
  <tbody>
  <tr id="v1100">
    <td class="ev-changelog__version"><strong>v1.10.0</strong><br><span>2026-09-26</span></td>
    <td>
      <p class="ev-changelog__type">新功能</p>
      <ul>
        <li>新增 <code>Config</code>，從 <code>econ-viz.toml</code> 設定檔載入圖形設定；<code>Config.load(...).use()</code> 會把它設為預設</li>
        <li>新增 <code>econ-viz init</code> 產生附註解的設定檔範本，<code>econ-viz plot --config</code> 可讀取設定檔</li>
      </ul>
      <p class="ev-changelog__type">變更</p>
      <ul>
        <li>沒有指定 theme 或字體時，圖形改用目前生效的 <code>Config</code>；沒有設定檔時輸出不變</li>
        <li>Python 3.10 需要安裝 <code>tomli</code></li>
      </ul>
    </td>
  </tr>
  <tr id="v190">
    <td class="ev-changelog__version"><strong>v1.9.0</strong><br><span>2026-09-26</span></td>
    <td>
      <p class="ev-changelog__type">新功能</p>
      <ul>
        <li>價格效果分解預設畫出無異曲線：通過 A 的 U<sub>0</sub>、通過 C 的 U<sub>1</sub>，Slutsky 分解還有通過 B 的曲線</li>
        <li>新增 <code>Haagsma</code> 效用模型，其商品 x 一定是劣等財，所得夠高時成為季芬財</li>
        <li>新增 <code>Legend</code>，自動放在最不擋到圖形的位置，也可指定角落或圖外的上下左右</li>
        <li>所有文字都能用 <code>Label</code> 調整：座標軸標籤、原點、標題、效果標籤、Edgeworth 箱形圖文字</li>
        <li><code>Stroke</code>、<code>Marker</code>、<code>Label</code>、<code>Legend</code>、<code>Effect</code>、<code>Fill</code> 都支援 <code>opacity</code></li>
      </ul>
      <p class="ev-changelog__type">變更</p>
      <ul>
        <li>既有的效果分解圖會多出無異曲線；傳入 <code>show_curves=False</code> 即可回到原本的圖</li>
        <li>效果範圍箭頭改為單向，從 A 指向 B、從 B 指向 C</li>
      </ul>
      <p class="ev-changelog__type">錯誤修正</p>
      <ul>
        <li>提高最適化的精度，比較靜態與 Slutsky 矩陣更準確</li>
        <li>效用為負值的無異曲線改畫實線</li>
      </ul>
    </td>
  </tr>
  <tr id="v180">
    <td class="ev-changelog__version"><strong>v1.8.0</strong><br><span>2026-09-26</span></td>
    <td>
      <p class="ev-changelog__type">新功能</p>
      <ul>
        <li><code>Effect</code> 可設定價格效果分解中每個效果的顏色、範圍箭頭高度與標籤</li>
        <li><code>Marker</code> 可設定畫布、需求圖與 Edgeworth 箱形圖中點的顏色、大小與形狀</li>
        <li><code>Label</code> 可設定點標籤的文字、位置（上下左右與四個角落）、位移、顏色、大小與是否顯示，也能隱藏效果分解的 A/B/C 標籤</li>
        <li><code>Fill</code> 讓預算集合的陰影可以有自己的顏色與透明度</li>
        <li><code>Axis</code> 用一個物件設定單一座標軸的標籤、標籤位置與線條</li>
        <li>新增標記點、標籤與陰影的主題預設值，例如 <code>theme.eq_marker</code>、<code>theme.point_label</code> 與 <code>theme.budget_fill</code></li>
      </ul>
      <p class="ev-changelog__type">變更</p>
      <ul>
        <li>均衡點的預設大小從 6 縮小為 4</li>
        <li>建議用 <code>Stroke</code> 設定線條樣式，另外的顏色、粗細與線型參數保留為簡寫</li>
      </ul>
      <p class="ev-changelog__type">錯誤修正</p>
      <ul>
        <li>楔形箭頭在畫面上維持固定大小，不再沿整條線拉長</li>
        <li>Edgeworth 箱形圖均衡點的無異曲線會套用 <code>stroke_a</code> / <code>stroke_b</code></li>
      </ul>
    </td>
  </tr>
  <tr id="v170">
    <td class="ev-changelog__version"><strong>v1.7.0</strong><br><span>2026-09-25</span></td>
    <td>
      <p class="ev-changelog__type">新功能</p>
      <ul>
        <li><code>Canvas</code> 與 <code>Figure</code> 可分別設定座標軸標籤位置、線條樣式與箭頭樣式</li>
        <li>可為單張圖設定文字與數學字體，不會改動 Matplotlib 的全域設定</li>
        <li><code>Stroke</code> 統一控制畫布、多面板圖、需求圖與 Edgeworth 箱形圖中的線條粗細、線條樣式、顏色與箭頭樣式</li>
        <li><code>econ-viz --version</code> 可顯示已安裝的套件版本</li>
      </ul>
      <p class="ev-changelog__type">錯誤修正</p>
      <ul>
        <li>修正效用模型的參數定義域、非對稱 CES 擴張路徑、Cobb-Douglas 極限，以及所得未用盡時的飽和偏好最適解</li>
        <li>等高線水準可正確處理零與負效用值</li>
        <li>比較靜態在價格、所得或最低消費限制附近改用邊界安全的有限差分</li>
        <li>所有範例腳本皆可從全新 checkout 直接執行</li>
      </ul>
      <p class="ev-changelog__type">維護</p>
      <ul>
        <li>套件管理與建置流程遷移至 <code>uv</code></li>
        <li>CI 測試 Python 3.10–3.13、檢查分支覆蓋率，並執行所有可執行範例</li>
        <li>版本標籤觸發的發佈流程只有在測試通過後才會上傳套件</li>
      </ul>
    </td>
  </tr>
  <tr id="v160">
    <td class="ev-changelog__version"><strong>v1.6.0</strong><br><span>2026-04-24</span></td>
    <td>
      <p class="ev-changelog__type">新功能</p>
      <ul>
        <li>預設配色改為色盲友善配色，並提供可重複使用的 <code>themes.COLORBLIND_CYCLE_RGB</code> 與 <code>themes.COLORBLIND_CYCLE_HEX</code></li>
        <li>無異曲線的預設線寬從 <code>2.0</code> 調整為 <code>1.8</code></li>
      </ul>
      <p class="ev-changelog__type">維護</p>
      <ul>
        <li>動畫範例移至 <code>examples/scripts/animation.py</code></li>
        <li>不再追蹤 <code>examples/output/</code> 底下產生的檔案</li>
      </ul>
      <p class="ev-changelog__type">測試</p>
      <ul>
        <li>TikZ 座標軸回歸測試不再依賴顏色索引</li>
      </ul>
    </td>
  </tr>
  <tr id="v150">
    <td class="ev-changelog__version"><strong>v1.5.0</strong><br><span>2026-04-21</span></td>
    <td>
      <p class="ev-changelog__type">新功能</p>
      <ul>
        <li>新增純 TikZ 匯出後端，<code>Canvas.save()</code> 與 <code>Figure.save()</code> 支援 <code>.tex</code></li>
        <li>新增價格效果分解：<code>decompose_price_effect()</code>、<code>PriceEffectDecomposition</code>，以及繪製 A/B/C 消費組合與替代／所得效果的 <code>Canvas.add_decomposition()</code></li>
        <li>分解相關 API 可直接從套件根目錄匯入</li>
        <li>新增分解、需求圖、PCC/ICC 路徑、多面板版面與 TikZ 匯出的範例腳本</li>
      </ul>
      <p class="ev-changelog__type">錯誤修正</p>
      <ul>
        <li>筆記本在 Colab 上的安裝流程可安全重新啟動</li>
      </ul>
      <p class="ev-changelog__type">重構</p>
      <ul>
        <li>改善共用面板版面中座標軸標籤的位置與顯示控制</li>
      </ul>
      <p class="ev-changelog__type">測試</p>
      <ul>
        <li>新增 TikZ 匯出與價格效果分解的回歸測試</li>
      </ul>
    </td>
  </tr>
  <tr id="v140">
    <td class="ev-changelog__version"><strong>v1.4.0</strong><br><span>2026-04-09</span></td>
    <td>
      <p class="ev-changelog__type">新功能</p>
      <ul>
        <li>新增 <code>Animator</code>，透過 Pillow 匯出參數變動的 GIF，不需要 ffmpeg</li>
        <li>新增 <code>WidgetViewer</code>，在 Jupyter 筆記本中用滑桿調整參數</li>
        <li>新增選用依賴 <code>animation</code>、<code>interactive</code> 與 <code>all</code></li>
        <li>新增常見效用函數的參數、價格、所得與只有預算線的 GIF 範例</li>
        <li>影格先疊在純色背景上再匯出，GIF 更穩定</li>
        <li>筆記本互動元件除了滑桿，也能直接輸入數值</li>
      </ul>
      <p class="ev-changelog__type">測試</p>
      <ul>
        <li>新增 <code>Animator</code> 與 <code>WidgetViewer</code> 的測試</li>
      </ul>
    </td>
  </tr>
  <tr id="v132">
    <td class="ev-changelog__version"><strong>v1.3.2</strong><br><span>2026-04-03</span></td>
    <td>
      <p class="ev-changelog__type">錯誤修正</p>
      <ul>
        <li>Edgeworth 契約線與價格線預設為黑色虛線</li>
      </ul>
      <p class="ev-changelog__type">維護</p>
      <ul>
        <li>發佈流程會略過 PyPI 上已存在的版本</li>
      </ul>
    </td>
  </tr>
  <tr id="v131">
    <td class="ev-changelog__version"><strong>v1.3.1</strong><br><span>2026-04-03</span></td>
    <td>
      <p class="ev-changelog__type">新功能</p>
      <ul>
        <li>Edgeworth 內部拆分為計算、狀態與繪圖三個模組</li>
        <li>新增模型登錄表（<code>models.registry</code>），命令列工具改由它建立模型</li>
      </ul>
      <p class="ev-changelog__type">重構</p>
      <ul>
        <li>命令列工具的錯誤改為拋出 <code>CliConfigError</code>，並統一在 <code>cli.main</code> 處理結束流程</li>
        <li>等高線水準的共用規則集中到 <code>contours.level_policies</code></li>
        <li><code>Canvas</code>、<code>Figure</code> 與 <code>EdgeworthBox</code> 共用同一個匯出器（<code>io.exporter</code>）</li>
        <li>Canvas 的繪製邏輯拆分到 <code>canvas.renderers</code> 與 <code>canvas.primitives</code></li>
        <li>套件根目錄的匯出改為延遲載入，公開 API 不變</li>
      </ul>
    </td>
  </tr>
  <tr id="v130">
    <td class="ev-changelog__version"><strong>v1.3.0</strong><br><span>2026-04-03</span></td>
    <td>
      <p class="ev-changelog__type">新功能</p>
      <ul>
        <li>新增 <code>EdgeworthBox</code> 與 <code>EquilibriumFocusConfig</code>，繪製兩人交換的 Edgeworth 箱形圖</li>
        <li>新增契約線、核、Walras 均衡疊圖，以及聚焦於均衡的無異曲線</li>
        <li>新增涵蓋常見效用函數組合的 <code>examples/edgeworth_box.py</code></li>
        <li>新增 Edgeworth 專屬測試</li>
      </ul>
    </td>
  </tr>
  <tr id="v123">
    <td class="ev-changelog__version"><strong>v1.2.3</strong><br><span>2026-03-31</span></td>
    <td>
      <p class="ev-changelog__type">新功能</p>
      <ul>
        <li><code>SlutskyMatrix</code> 新增對稱性、半負定性與齊次性檢查，條件不成立時會發出警告</li>
        <li>命令列工具支援 <code>QuasiLinear</code>、<code>StoneGeary</code> 與 <code>Translog</code></li>
      </ul>
    </td>
  </tr>
  <tr id="v122">
    <td class="ev-changelog__version"><strong>v1.2.2</strong><br><span>2026-03-31</span></td>
    <td>
      <p class="ev-changelog__type">錯誤修正</p>
      <ul>
        <li>PCC/ICC 路徑預設平滑化，端點稍微延伸，標記點預設不顯示</li>
        <li>PCC/ICC 路徑改用獨立顏色，需求圖的商品空間邊距加大</li>
        <li>新增 PCC/ICC 範例產生器與測試</li>
      </ul>
    </td>
  </tr>
  <tr id="v120">
    <td class="ev-changelog__version"><strong>v1.2.0</strong><br><span>2026-03-30</span></td>
    <td>
      <p class="ev-changelog__type">新功能</p>
      <ul>
        <li>新增多面板 <code>Figure</code> 版面與 <code>Layout</code> 列舉</li>
        <li>新增連動的 <code>DemandDiagram</code>，繪製 Marshall 需求</li>
        <li>新增 <code>PricePath</code>、<code>IncomePath</code> 與 <code>Canvas.add_path()</code>，繪製 PCC/ICC</li>
      </ul>
    </td>
  </tr>
  <tr id="v110">
    <td class="ev-changelog__version"><strong>v1.1.0</strong><br><span>2026-03-30</span></td>
    <td>
      <p class="ev-changelog__type">新功能</p>
      <ul>
        <li>新增比較靜態工具 <code>comparative_statics</code></li>
        <li>分析模組新增 <code>HomogeneityAnalyzer</code> 與 <code>ReturnsToScale</code></li>
        <li>新增 <code>Translog</code> 模型，並支援圖例與無異曲線標籤</li>
      </ul>
    </td>
  </tr>
  <tr id="v102">
    <td class="ev-changelog__version"><strong>v1.0.2</strong><br><span>2026-03-29</span></td>
    <td>
      <p class="ev-changelog__type">錯誤修正</p>
      <ul>
        <li>數學式座標軸標籤不再被重複包裝</li>
        <li>移除 NumPy 版本上限，避免在 Colab 上發生衝突</li>
      </ul>
    </td>
  </tr>
  <tr id="v101">
    <td class="ev-changelog__version"><strong>v1.0.1</strong><br><span>2026-03-29</span></td>
    <td>
      <p class="ev-changelog__type">錯誤修正</p>
      <ul>
        <li>鎖定 <code>numpy&lt;2</code>，避免在 Colab 與本機安裝時 ABI 不相容</li>
      </ul>
      <p class="ev-changelog__type">維護</p>
      <ul>
        <li>放寬 Python 與 NumPy 版本限制，<code>pytest</code> 鎖定在 8.x</li>
      </ul>
    </td>
  </tr>
  <tr id="v100">
    <td class="ev-changelog__version"><strong>v1.0.0</strong><br><span>2026-03-28</span></td>
    <td>
      <ul>
        <li>首次發布</li>
      </ul>
    </td>
  </tr>
  </tbody>
</table>
