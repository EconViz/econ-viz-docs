---
seo_title: "Changelog"
description: "Release history of the econ-viz Python package: new features, fixes, and changes in each version."
---

# Changelog

Release history of `econ-viz`. Documentation-only changes are not listed.

<table class="ev-changelog">
  <thead>
  <tr><th>Version</th><th>Changes</th></tr>
  </thead>
  <tbody>
  <tr id="v1101">
    <td class="ev-changelog__version"><strong>v1.10.1</strong><br><span>2026-09-26</span></td>
    <td>
      <p class="ev-changelog__type">Maintenance</p>
      <ul>
        <li>Add Ruff linting and formatting plus Mypy type checking to contributor tooling and CI</li>
        <li>Publish <code>econ-viz</code> as a PEP 561 typed package with <code>py.typed</code></li>
        <li>Standardize public exception messages in English</li>
      </ul>
      <p class="ev-changelog__type">Bug fixes</p>
      <ul>
        <li>Fix a missing NumPy import in contour-level annotations</li>
        <li>Bind each Edgeworth Pareto-search closure to its own weight</li>
      </ul>
    </td>
  </tr>
  <tr id="v1100">
    <td class="ev-changelog__version"><strong>v1.10.0</strong><br><span>2026-09-26</span></td>
    <td>
      <p class="ev-changelog__type">Features</p>
      <ul>
        <li><code>Config</code> loads diagram settings from an <code>econ-viz.toml</code> file; <code>Config.load(...).use()</code> makes them the default</li>
        <li><code>econ-viz init</code> writes a commented settings template, and <code>econ-viz plot --config</code> reads it</li>
      </ul>
      <p class="ev-changelog__type">Changes</p>
      <ul>
        <li>Diagrams take their theme and fonts from the active <code>Config</code> when none is passed; without one the output is unchanged</li>
        <li><code>tomli</code> is required on Python 3.10</li>
      </ul>
    </td>
  </tr>
  <tr id="v190">
    <td class="ev-changelog__version"><strong>v1.9.0</strong><br><span>2026-09-26</span></td>
    <td>
      <p class="ev-changelog__type">Features</p>
      <ul>
        <li>Price-effect decompositions draw their indifference curves by default: U<sub>0</sub> through A, U<sub>1</sub> through C, and the curve through B under Slutsky</li>
        <li><code>Haagsma</code> utility model with an always-inferior good that becomes Giffen at high enough income</li>
        <li><code>Legend</code> placed automatically where it covers the least of the diagram, or at a chosen corner or side</li>
        <li><code>Label</code> for every text element: axis labels, origin, titles, effect labels, Edgeworth box text</li>
        <li><code>opacity</code> on <code>Stroke</code>, <code>Marker</code>, <code>Label</code>, <code>Legend</code>, <code>Effect</code>, and <code>Fill</code></li>
      </ul>
      <p class="ev-changelog__type">Changes</p>
      <ul>
        <li>Existing decomposition figures now include their indifference curves; <code>show_curves=False</code> restores the previous figure</li>
        <li>Effect range arrows point one way, from A to B and from B to C</li>
      </ul>
      <p class="ev-changelog__type">Bug fixes</p>
      <ul>
        <li>Tighter optimisation tolerance, so comparative statics and Slutsky matrices are accurate</li>
        <li>Indifference curves at negative utility levels are drawn solid</li>
      </ul>
    </td>
  </tr>
  <tr id="v180">
    <td class="ev-changelog__version"><strong>v1.8.0</strong><br><span>2026-09-26</span></td>
    <td>
      <p class="ev-changelog__type">Features</p>
      <ul>
        <li><code>Effect</code> sets the colour, range-arrow height, and label of each price-effect decomposition effect</li>
        <li><code>Marker</code> sets point colour, size, and shape across canvases, demand diagrams, and Edgeworth boxes</li>
        <li><code>Label</code> sets point-label text, position (four sides and four corners), offset, colour, size, and visibility; decomposition A/B/C labels can be hidden</li>
        <li><code>Fill</code> gives the budget-set shading its own colour and opacity</li>
        <li><code>Axis</code> sets one axis's label, label position, and stroke in a single object</li>
        <li>Theme defaults for markers, labels, and fills, such as <code>theme.eq_marker</code>, <code>theme.point_label</code>, and <code>theme.budget_fill</code></li>
      </ul>
      <p class="ev-changelog__type">Changes</p>
      <ul>
        <li>Default equilibrium point size reduced from 6 to 4</li>
        <li><code>Stroke</code> is the preferred way to style lines; separate colour, width, and style arguments remain as shorthand</li>
      </ul>
      <p class="ev-changelog__type">Bug fixes</p>
      <ul>
        <li>Wedge arrowheads keep a fixed on-screen size instead of stretching along the line</li>
        <li>Edgeworth equilibrium indifference curves apply <code>stroke_a</code> / <code>stroke_b</code></li>
      </ul>
    </td>
  </tr>
  <tr id="v170">
    <td class="ev-changelog__version"><strong>v1.7.0</strong><br><span>2026-09-25</span></td>
    <td>
      <p class="ev-changelog__type">Features</p>
      <ul>
        <li>Independent axis-label positions, line styles, and arrowhead styles for <code>Canvas</code> and <code>Figure</code></li>
        <li>Per-figure text and math fonts without changing Matplotlib's global configuration</li>
        <li><code>Stroke</code> controls line width, style, colour, and arrowheads across canvases, figures, demand diagrams, and Edgeworth boxes</li>
        <li><code>econ-viz --version</code> prints the installed package version</li>
      </ul>
      <p class="ev-changelog__type">Bug fixes</p>
      <ul>
        <li>Correct utility-model domains, asymmetric CES expansion paths, Cobb-Douglas limits, and satiation optima with unspent income</li>
        <li>Robust contour levels around zero and negative utility values</li>
        <li>Boundary-safe comparative statics near zero prices, income, and subsistence constraints</li>
        <li>All example scripts run from a clean checkout</li>
      </ul>
      <p class="ev-changelog__type">Maintenance</p>
      <ul>
        <li>Package management and builds migrated to <code>uv</code></li>
        <li>CI tests Python 3.10–3.13, enforces branch coverage, and smoke-tests runnable examples</li>
        <li>Tagged releases publish only after tests pass</li>
      </ul>
    </td>
  </tr>
  <tr id="v160">
    <td class="ev-changelog__version"><strong>v1.6.0</strong><br><span>2026-04-24</span></td>
    <td>
      <p class="ev-changelog__type">Features</p>
      <ul>
        <li>Colour-blind-friendly default palette, with reusable <code>themes.COLORBLIND_CYCLE_RGB</code> and <code>themes.COLORBLIND_CYCLE_HEX</code></li>
        <li>Default indifference-curve line width reduced from <code>2.0</code> to <code>1.8</code></li>
      </ul>
      <p class="ev-changelog__type">Maintenance</p>
      <ul>
        <li>Animation example moved to <code>examples/scripts/animation.py</code></li>
        <li>Generated files under <code>examples/output/</code> are no longer tracked</li>
      </ul>
      <p class="ev-changelog__type">Tests</p>
      <ul>
        <li>TikZ axis regression test no longer depends on colour indices</li>
      </ul>
    </td>
  </tr>
  <tr id="v150">
    <td class="ev-changelog__version"><strong>v1.5.0</strong><br><span>2026-04-21</span></td>
    <td>
      <p class="ev-changelog__type">Features</p>
      <ul>
        <li>Pure TikZ export backend; <code>Canvas.save()</code> and <code>Figure.save()</code> accept <code>.tex</code></li>
        <li>Price-effect decomposition: <code>decompose_price_effect()</code>, <code>PriceEffectDecomposition</code>, and <code>Canvas.add_decomposition()</code> for A/B/C bundles and substitution/income overlays</li>
        <li>Decomposition APIs importable from the package root</li>
        <li>New example scripts for decomposition, demand diagrams, PCC/ICC paths, multi-panel layouts, and TikZ export</li>
      </ul>
      <p class="ev-changelog__type">Bug fixes</p>
      <ul>
        <li>Notebook install flow on Colab is restart-safe</li>
      </ul>
      <p class="ev-changelog__type">Refactoring</p>
      <ul>
        <li>Better axis-label placement and visibility in shared-panel layouts</li>
      </ul>
      <p class="ev-changelog__type">Tests</p>
      <ul>
        <li>Regression tests for TikZ export and price-effect decomposition</li>
      </ul>
    </td>
  </tr>
  <tr id="v140">
    <td class="ev-changelog__version"><strong>v1.4.0</strong><br><span>2026-04-09</span></td>
    <td>
      <p class="ev-changelog__type">Features</p>
      <ul>
        <li><code>Animator</code> for GIF parameter sweeps via Pillow, no ffmpeg required</li>
        <li><code>WidgetViewer</code> for slider controls in Jupyter notebooks</li>
        <li>Optional extras <code>animation</code>, <code>interactive</code>, and <code>all</code></li>
        <li>Parameter, price, income, and budget-only GIF examples for common utility functions</li>
        <li>More reliable GIF export by compositing frames onto a solid background</li>
        <li>Notebook widgets accept typed values alongside sliders</li>
      </ul>
      <p class="ev-changelog__type">Tests</p>
      <ul>
        <li>Tests for <code>Animator</code> and <code>WidgetViewer</code></li>
      </ul>
    </td>
  </tr>
  <tr id="v132">
    <td class="ev-changelog__version"><strong>v1.3.2</strong><br><span>2026-04-03</span></td>
    <td>
      <p class="ev-changelog__type">Bug fixes</p>
      <ul>
        <li>Edgeworth contract curves and price lines default to dashed black</li>
      </ul>
      <p class="ev-changelog__type">Maintenance</p>
      <ul>
        <li>Publish workflow skips versions already on PyPI</li>
      </ul>
    </td>
  </tr>
  <tr id="v131">
    <td class="ev-changelog__version"><strong>v1.3.1</strong><br><span>2026-04-03</span></td>
    <td>
      <p class="ev-changelog__type">Features</p>
      <ul>
        <li>Edgeworth internals split into compute, state, and plotter modules</li>
        <li>Model registry (<code>models.registry</code>), used by the CLI to build models</li>
      </ul>
      <p class="ev-changelog__type">Refactoring</p>
      <ul>
        <li>CLI errors raise <code>CliConfigError</code>, with exit handling centralized in <code>cli.main</code></li>
        <li>Shared contour-level policies in <code>contours.level_policies</code></li>
        <li>One figure exporter (<code>io.exporter</code>) shared by <code>Canvas</code>, <code>Figure</code>, and <code>EdgeworthBox</code></li>
        <li>Canvas rendering split into <code>canvas.renderers</code> and <code>canvas.primitives</code></li>
        <li>Package-root exports load lazily, with the public API unchanged</li>
      </ul>
    </td>
  </tr>
  <tr id="v130">
    <td class="ev-changelog__version"><strong>v1.3.0</strong><br><span>2026-04-03</span></td>
    <td>
      <p class="ev-changelog__type">Features</p>
      <ul>
        <li><code>EdgeworthBox</code> and <code>EquilibriumFocusConfig</code> for two-consumer exchange diagrams</li>
        <li>Contract curve, core, Walrasian equilibrium overlay, and equilibrium-focused indifference curves</li>
        <li><code>examples/edgeworth_box.py</code> covering common utility-function combinations</li>
        <li>Dedicated Edgeworth tests</li>
      </ul>
    </td>
  </tr>
  <tr id="v123">
    <td class="ev-changelog__version"><strong>v1.2.3</strong><br><span>2026-03-31</span></td>
    <td>
      <p class="ev-changelog__type">Features</p>
      <ul>
        <li><code>SlutskyMatrix</code> checks symmetry, negative semidefiniteness, and homogeneity, and warns when a condition fails</li>
        <li>CLI supports <code>QuasiLinear</code>, <code>StoneGeary</code>, and <code>Translog</code></li>
      </ul>
    </td>
  </tr>
  <tr id="v122">
    <td class="ev-changelog__version"><strong>v1.2.2</strong><br><span>2026-03-31</span></td>
    <td>
      <p class="ev-changelog__type">Bug fixes</p>
      <ul>
        <li>PCC/ICC paths are smoothed by default, with slightly extended endpoints and markers hidden unless requested</li>
        <li>PCC/ICC paths use their own colours, and demand diagrams have more goods-space padding</li>
        <li>Dedicated PCC/ICC example generator and tests</li>
      </ul>
    </td>
  </tr>
  <tr id="v120">
    <td class="ev-changelog__version"><strong>v1.2.0</strong><br><span>2026-03-30</span></td>
    <td>
      <p class="ev-changelog__type">Features</p>
      <ul>
        <li>Multi-panel <code>Figure</code> layouts and the <code>Layout</code> enum</li>
        <li>Linked <code>DemandDiagram</code> for Marshallian demand</li>
        <li><code>PricePath</code>, <code>IncomePath</code>, and <code>Canvas.add_path()</code> for PCC/ICC plots</li>
      </ul>
    </td>
  </tr>
  <tr id="v110">
    <td class="ev-changelog__version"><strong>v1.1.0</strong><br><span>2026-03-30</span></td>
    <td>
      <p class="ev-changelog__type">Features</p>
      <ul>
        <li><code>comparative_statics</code> helper</li>
        <li><code>HomogeneityAnalyzer</code> and <code>ReturnsToScale</code> in the analysis module</li>
        <li><code>Translog</code> model, plus legend and indifference-curve labels</li>
      </ul>
    </td>
  </tr>
  <tr id="v102">
    <td class="ev-changelog__version"><strong>v1.0.2</strong><br><span>2026-03-29</span></td>
    <td>
      <p class="ev-changelog__type">Bug fixes</p>
      <ul>
        <li>Math axis labels are no longer double-wrapped</li>
        <li>NumPy upper bound removed to avoid conflicts on Colab</li>
      </ul>
    </td>
  </tr>
  <tr id="v101">
    <td class="ev-changelog__version"><strong>v1.0.1</strong><br><span>2026-03-29</span></td>
    <td>
      <p class="ev-changelog__type">Bug fixes</p>
      <ul>
        <li>Pin <code>numpy&lt;2</code> to avoid ABI mismatches on Colab and local installs</li>
      </ul>
      <p class="ev-changelog__type">Maintenance</p>
      <ul>
        <li>Relaxed Python and NumPy bounds; <code>pytest</code> pinned to 8.x</li>
      </ul>
    </td>
  </tr>
  <tr id="v100">
    <td class="ev-changelog__version"><strong>v1.0.0</strong><br><span>2026-03-28</span></td>
    <td>
      <ul>
        <li>Initial release</li>
      </ul>
    </td>
  </tr>
  </tbody>
</table>
