import importlib.util
from pathlib import Path
from types import SimpleNamespace
import unittest
from html.parser import HTMLParser

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("api_reference", ROOT / "hooks/api_reference.py")
api = importlib.util.module_from_spec(spec)
spec.loader.exec_module(api)


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.targets = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.append(attrs["id"])
        if attrs.get("href", "").startswith("#"):
            self.targets.append(attrs["href"][1:])


class ApiReferenceTests(unittest.TestCase):
    def setUp(self):
        api.on_config(SimpleNamespace(watch=[]))

    def test_all_languages_have_unique_working_parameter_targets(self):
        for symbol in api._catalog:
            for language in api.LABELS:
                with self.subTest(symbol=symbol, language=language):
                    parser = Links()
                    parser.feed(api.render(symbol, language))
                    self.assertEqual(len(parser.ids), len(set(parser.ids)))
                    self.assertTrue(set(parser.targets) <= set(parser.ids))

    def test_none_default_is_not_required(self):
        html = api.render("canvas.add_budget", "zh-TW")
        fill_alpha = html.split('id="add_budget-fill_alpha"')[1].split('</section>')[0]
        self.assertIn('ev-api__python--constant">None</span>', fill_alpha)
        self.assertNotIn('必填', fill_alpha)

    def test_keyword_only_separator(self):
        html = api.render("bezierkit.fit_parametric", "en")
        self.assertIn('\n    *,\n', html)

    def test_python_badges_preserve_custom_names_and_strings(self):
        result = api._python_badges('dict[str, float] | None True False lambda PointSet "float"')
        self.assertEqual(result.count('ev-api__python--builtin'), 3)
        self.assertEqual(result.count('ev-api__python--constant'), 3)
        self.assertIn('ev-api__python--keyword">lambda</span>', result)
        self.assertIn('ev-api__custom--data">PointSet</span> &quot;float&quot;', result)
        result = api.render_manual({'anchor': 'test', 'parameters': [],
            'signatures': ['PointSet(points: list, enabled=True, label="None")']}, 'en')
        self.assertIn('ev-api__python--builtin">list</span>', result)
        self.assertIn('ev-api__python--constant">True</span>', result)
        self.assertIn('&quot;None&quot;', result)

    def test_code_examples_are_not_expanded(self):
        page = SimpleNamespace(file=SimpleNamespace(src_uri="zh-CN/example.md"))
        source = '```markdown\n<!-- api: canvas.add_budget -->\n```\n\n<!-- api: canvas.show -->'
        result = api.on_page_markdown(source, page, None)
        self.assertIn('```markdown\n<!-- api: canvas.add_budget -->\n```', result)
        self.assertIn('id="api-show"', result)

    def test_unknown_or_duplicate_directive_fails(self):
        page = SimpleNamespace(file=SimpleNamespace(src_uri="example.md"))
        for content in ['<!-- api: missing -->', '<!-- api: canvas.show -->\n<!-- api: canvas.show -->']:
            with self.assertRaises(api.PluginError):
                api.on_page_markdown(content, page, None)

    def test_manual_parameter_links_use_site_urls(self):
        page = SimpleNamespace(file=SimpleNamespace(src_uri="zh-TW/mosaickit/guides/canvas.md", name="canvas"))
        config = SimpleNamespace(use_directory_urls=True)
        result = api.on_page_markdown('<!-- api: agora.mosaickit.guides_canvas_3 -->', page, config)
        self.assertIn('href="../parameters/#sec-parameters"', result)
        self.assertNotIn('parameters.md#', result)

    def test_manual_methods_keep_owner_unaccented(self):
        result = api.render_manual({'anchor':'test', 'signatures':['Canvas.add(layer)'], 'parameters':[]}, 'en')
        self.assertIn('class="ev-api__owner"><span class="ev-api__custom ev-api__custom--class">Canvas</span>.</span>', result)
        self.assertIn('class="ev-api__function" href="#api-test"><span class="ev-api__method">add</span></a>', result)

    def test_errors_warnings_and_compact_methods_have_badges(self):
        for name in ('MosaicKitError', 'ConfigurationError', 'PrincipleVizError', 'BezierKitError'):
            self.assertIn(f'ev-api__custom--error">{name}</span>', api._type(name))
        self.assertIn('ev-api__custom--warning">LayoutWarning</span>', api._type('LayoutWarning'))
        result = api._reference_name('add(layer), extend(layers), render(cache=None)')
        self.assertEqual(result.count('class="ev-api__method"'), 3)
        self.assertIn('ev-api__python--constant">None</span>', result)
        self.assertEqual(api._reference_name('"ConfigurationError"'), '&quot;ConfigurationError&quot;')

    def test_custom_class_palette_across_packages(self):
        for name, category in [('Canvas', 'class'), ('MarketFigure', 'class'),
                               ('BezierCurve', 'class'), ('CobbDouglas', 'model'),
                               ('DiscreteSupply', 'model'), ('CanvasSpec', 'data'),
                               ('PointSet', 'data'), ('TaxEquilibriumResult', 'data'),
                               ('TaxOn', 'enum'), ('ArrowStyle', 'enum'),
                               ('StyleBundle', 'style'), ('Stroke', 'style')]:
            self.assertIn(f'ev-api__custom--{category}">{name}</span>', api._type(name))
        self.assertEqual(api._python_badges('"Canvas"'), '&quot;Canvas&quot;')

    def test_reference_tables_keep_content_and_stable_row_anchors(self):
        source = '| Object | Styles | Defaults |\n| --- | --- | --- |\n| `Stroke` | Line width | `theme.stroke` |\n'
        result = api.render_reference_tables(source, 'zh-TW/utility-viz/guides/canvas.md')
        self.assertIn('id="api-entry-0-stroke"', result)
        self.assertIn('ev-api__custom--style">Stroke</span>', result)
        self.assertIn('Line width', result)
        self.assertIn('ev-api__default">預設值： <code>theme.stroke</code>', result)
        self.assertNotIn('**Styles**', result)
        self.assertNotIn('| Object |', result)
        self.assertEqual(api.render_reference_tables(source, 'utility-viz/migrating.md'), source)
        fenced = '```markdown\n' + source + '```\n'
        self.assertEqual(api.render_reference_tables(fenced, 'utility-viz/guides/canvas.md'), fenced)

    def test_nested_parameter_tables_convert_in_every_language(self):
        for locale, heading in [('', 'Parameter'), ('zh-TW/', '參數'), ('zh-CN/', '参数')]:
            source = f'=== "Translog"\n\n    | {heading} | Default | Meaning |\n    | --- | --- | --- |\n    | `alpha_0` | `0.0` | Intercept |\n'
            result = api.render_reference_tables(source, locale + 'utility-viz/models/index.md')
            self.assertIn('    <div class="ev-api ev-reference-list"', result)
            self.assertIn('id="api-entry-nested-0-alpha-0"', result)
            self.assertIn('class="ev-api__default"', result)
            self.assertIn('ev-api__python--number">0.0</span></code></span></div>', result)
            self.assertIn('ev-api__attribute">alpha_0</span>', result)
            self.assertNotIn('**Default**', result)
            self.assertNotIn('| `alpha_0` |', result)

    def test_reference_parameter_metadata_matches_api_layout(self):
        source = '| Parameter | Type | Default | Meaning |\n| --- | --- | --- | --- |\n| `axis_stroke` | `Stroke` or `None` | `None` | Sets both axes. |\n'
        result = api.render_reference_tables(source, 'utility-viz/example.md')
        meta = result.split('class="ev-api__meta"')[1].split('</div>')[0]
        self.assertIn('ev-api__types', meta)
        self.assertIn('ev-api__custom--style">Stroke', meta)
        self.assertIn('ev-api__default', meta)
        self.assertIn('Sets both axes.', result.split('</div>')[1])
        self.assertNotIn('**Meaning**', result)

    def test_highlighted_calls_and_parameters_preserve_code(self):
        from pygments import highlight
        from pygments.lexers import PythonLexer
        from pygments.formatters import HtmlFormatter
        import html as html_module
        import re
        api.on_config(SimpleNamespace(watch=[], docs_dir=str(ROOT / 'docs')))
        source = 'from utility_viz import Canvas as Plot\ncvs = Plot(x_max=20)\ncvs.add_budget(2, 3, 30, fill=True)\n# Canvas(x_max=10)\ntext = "Canvas(x_max=10)"\n'
        highlighted = highlight(source, PythonLexer(), HtmlFormatter()).replace('<pre>', '<pre><span></span><code><a id="line-1" href="#line-1"></a>').replace('</pre>', '</code></pre>')
        result = api.link_examples(highlighted, 'zh-TW/utility-viz/index.md', SimpleNamespace(use_directory_urls=True))
        self.assertIn('#canvas-constructor-x_max', result)
        self.assertIn('#add_budget-fill', result)
        self.assertIn('#api-add_budget', result)
        self.assertEqual(html_module.unescape(re.sub('<[^>]+>', '', result)), html_module.unescape(re.sub('<[^>]+>', '', highlighted)))
        self.assertNotIn('ev-code-link', result.split('# Canvas')[1].split('\n')[0])

    def test_all_documented_package_imports_have_targets(self):
        import ast
        import re
        import textwrap
        api.on_config(SimpleNamespace(watch=[], docs_dir=str(ROOT / 'docs')))
        for path in (ROOT / 'docs').rglob('*.md'):
            src = path.relative_to(ROOT / 'docs').as_posix()
            locale = src.split('/')[0] + '/' if src.startswith(('zh-TW/', 'zh-CN/')) else ''
            for body in re.findall(r'```python[^\n]*\n(.*?)```', path.read_text(), re.S):
                try:
                    tree = ast.parse(textwrap.dedent(body))
                except SyntaxError:
                    continue
                for node in ast.walk(tree):
                    if not isinstance(node, ast.ImportFrom) or not node.module:
                        continue
                    package = node.module.split('.')[0].replace('_', '-')
                    if package not in {'utility-viz', 'principle-viz', 'mosaickit', 'bezierkit'}:
                        continue
                    for name in node.names:
                        targets = {t for t in api._symbols.get(name.name, ()) if t[0].startswith(locale + package + '/')}
                        self.assertTrue(targets, (src, node.module, name.name))

    def test_import_list_links_every_name(self):
        from pygments import highlight
        from pygments.lexers import PythonLexer
        from pygments.formatters import HtmlFormatter
        api.on_config(SimpleNamespace(watch=[], docs_dir=str(ROOT / 'docs')))
        for locale in ('', 'zh-TW/', 'zh-CN/'):
            source = 'from utility_viz import Canvas, levels, solve\n'
            markup = highlight(source, PythonLexer(), HtmlFormatter()).replace('<pre>', '<pre><code>').replace('</pre>', '</code></pre>')
            result = api.link_examples(markup, locale + 'utility-viz/index.md', SimpleNamespace(use_directory_urls=True))
            self.assertEqual(result.count('class="ev-code-link"'), 3)

    def test_inline_links_keep_locale_and_skip_examples_existing_links(self):
        api.on_config(SimpleNamespace(watch=[], docs_dir=str(ROOT / 'docs')))
        page = SimpleNamespace(file=SimpleNamespace(src_uri='zh-TW/mosaickit/quickstart.md'))
        config = SimpleNamespace(use_directory_urls=True)
        result = api.on_page_content('<p><code>Canvas</code> <code>Canvas.add(layer)</code></p>'
            '<pre><code>Canvas</code></pre><a href="custom"><code>Canvas</code></a>'
            '<code>not_an_api</code>', page, config)
        self.assertIn('href="../guides/canvas/#api-mosaickit-guides-canvas-3"', result)
        self.assertIn('href="../guides/canvas/#mosaickit-guides-canvas-3-0"', result)
        self.assertIn('<pre><code>Canvas</code></pre>', result)
        self.assertIn('<a href="custom"><code class="ev-api-inline-code"><span class="ev-api__custom ev-api__custom--class">Canvas</span></code></a>', result)
        self.assertIn('ev-api__attribute">not_an_api</span>', result)
        self.assertEqual(result.count('class="ev-api-inline"'), 2)

    def test_prose_badges_cover_errors_methods_and_builtins(self):
        page = SimpleNamespace(file=SimpleNamespace(src_uri='zh-TW/mosaickit/guides/canvas.md'))
        result = api.on_page_content('<code>ConfigurationError</code> <code>replace(**changes)</code> '
            '<code>float</code> <code>None</code> <code>lo &lt; hi</code>', page, SimpleNamespace(use_directory_urls=True))
        for badge in ('ev-api__custom--error', 'ev-api__method', 'ev-api__python--builtin', 'ev-api__python--constant'):
            self.assertIn(badge, result)
        self.assertIn('<code>lo &lt; hi</code>', result)

    def test_inline_attributes_have_a_surface_in_every_package_and_language(self):
        for locale in ('', 'zh-TW/', 'zh-CN/'):
            for package in ('utility-viz', 'principle-viz', 'mosaickit', 'bezierkit'):
                page = SimpleNamespace(file=SimpleNamespace(src_uri=locale + package + '/guides/canvas.md'))
                source = ' '.join(f'<code>{name}</code>' for name in
                                  ('x_range', 'y_range', 'width', 'height', 'dpi', 'x_min', 'theme.ic_stroke'))
                result = api.on_page_content(source, page, SimpleNamespace(use_directory_urls=True))
                self.assertEqual(result.count('class="ev-api__attribute"'), 7)

    def test_all_catalog_parameter_labels_have_badges(self):
        for symbol, item in api._catalog.items():
            for parameter in item['parameters']:
                self.assertIn('<span ', api._parameter_label(parameter['name']), (symbol, parameter['name']))

    def test_numeric_prose_and_manual_signatures_share_badges(self):
        page = SimpleNamespace(file=SimpleNamespace(src_uri='mosaickit/guides/canvas.md'))
        result = api.on_page_content('<p><code>0.5</code></p>', page, SimpleNamespace(use_directory_urls=True))
        self.assertIn('ev-api__python--number">0.5</span>', result)
        result = api.render_manual({'anchor':'test','parameters':[], 'signatures':['CanvasSpec(width=6.0, dpi=300)']}, 'en')
        self.assertIn('ev-api__attribute">width</span>', result)
        self.assertIn('ev-api__attribute">dpi</span>', result)
        self.assertIn('ev-api__python--number">6.0</span>', result)


if __name__ == "__main__":
    unittest.main()
