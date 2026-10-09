"""Render explicitly placed API references from versioned, multilingual data.

Use <!-- api: canvas.add_budget --> in Markdown. No package imports are
needed at build time. Keep signatures and translations in api_data/*.json.
"""
from __future__ import annotations

import html
import json
from pathlib import Path
import re
import posixpath
import ast
import builtins
import keyword

import markdown as md
from mkdocs.exceptions import PluginError

DATA = Path(__file__).with_name("api_data")
LABELS = {
    "en": ("Required", "Default:", "or", "Keyword arguments"),
    "zh-TW": ("必填", "預設值：", "或", "其他關鍵字參數"),
    "zh-CN": ("必填", "默认值：", "或", "其他关键字参数"),
}
_catalog = {}
_symbols = {}
_parameters = {}
_sections = []
_class_categories = {
    'model': set('CobbDouglas CES Translog Leontief PerfectSubstitutes MaximumUtility QuasiLinear StoneGeary Satiation CustomUtility MultiGoodCD Haagsma UtilityFunction LinearDemand LinearSupply DiscreteDemand DiscreteSupply PiecewiseLinear ProductionPossibilitiesFrontier IndividualBenefit'.split()),
    'data': set('Point Vector PointSet Interval ParameterValues CanvasSpec AxisSpec Equilibrium EquilibriumResult TaxEquilibriumResult MarketOutcome Sample PathDocument EndpointDerivatives TangentDirections PlanarSlopes Rect Span Placement SurplusPolygons ShiftScenario ShiftSpec TaxScenario SubsidyScenario PriceControlScenario TradeScenario ExternalityScenario LoanableFundsScenario PPFGrowthScenario'.split()),
    'enum': set('ArrowStyle LineStyle LabelPosition ArrowPlacement TaxOn TaxType SubsidyTo PriceControlType AnchorMode EquilibriumPriceRule QuotaRentRecipient DecompositionMethod Effect'.split()),
    'style': set('Stroke Fill Marker Label Legend LegendStyle TextStyle Theme PlotTheme StyleBundle Config Color Palette SaveOptions'.split()),
}
_custom_classes = set()
API_TOKEN_PATTERN = r'''"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*'|[A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*|(?<![\w.])[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?'''
# Explicitly selected reference tables; comparison/migration tables stay tabular.
REFERENCE_TABLES = {
    'utility-viz/guides/canvas.md': {0},
    'utility-viz/guides/config.md': {0},
    'utility-viz/guides/themes.md': {0, 1},
    'utility-viz/tools/analysis.md': {0},
    'utility-viz/models/advanced.md': {1},
    'utility-viz/getting-started/cli.md': {0, 1},
    'principle-viz/cli.md': {0},
    'principle-viz/guides/figures.md': {0},
    'principle-viz/guides/markets.md': {0},
    'mosaickit/guides/canvas.md': {0},
    'mosaickit/guides/layers.md': {0},
    'mosaickit/guides/styles.md': {0},
    'mosaickit/guides/themes.md': {0},
    'bezierkit/guides/geometry.md': {1},
    'bezierkit/guides/export.md': {0},
}
TABLE_PATTERN = re.compile(r'^(?P<indent> *)\|.+\n(?P=indent)\|[-: |]+\n(?:(?P=indent)\|.*(?:\n|$))+', re.M)
REFERENCE_HEADERS = {
    'parameter', 'field', 'property', 'attribute', 'method', 'object', 'class',
    'exception', 'command', 'flag', 'style', 'layer', 'role', 'key', 'name',
    '參數', '参数', '欄位', '字段', '屬性', '属性', '方法', '物件', '对象',
    '類別', '类', '例外', '异常', '指令', '命令', '旗標', '标志',
    '樣式', '样式', '圖層', '图层', '角色', '鍵', '键', '名稱', '名称',
}


def reference_tables(source, src):
    plain = re.sub(r'^zh-(?:TW|CN)/', '', src)
    # Ignore fenced examples so table-like example text is never transformed.
    fenced = list(re.finditer(r'^\s*```[^\n]*\n.*?^\s*```[^\n]*$', source, re.M | re.S))
    matches = [m for m in TABLE_PATTERN.finditer(source)
               if not any(f.start() <= m.start() < f.end() for f in fenced)]
    root_index = nested_index = 0
    for match in matches:
        if match['indent']:
            index = f'nested-{nested_index}'
            nested_index += 1
        else:
            index = root_index
            root_index += 1
        rows = [re.split(r'(?<!\\)\|', line.strip().strip('|')) for line in match[0].splitlines()]
        rows = [[cell.strip() for cell in row] for row in rows]
        is_reference = rows[0][0].strip('`* ').casefold() in REFERENCE_HEADERS
        if index in REFERENCE_TABLES.get(plain, set()) or (is_reference and not plain.endswith('migrating.md')):
            yield index, match, rows[0], rows[2:]


def reference_anchor(index, row):
    return f'api-entry-{index}-' + re.sub(r'[^a-z0-9]+', '-', row[0].lower()).strip('-')


def render_reference_tables(source, src):
    language = src.split('/')[0] if src.startswith(('zh-TW/', 'zh-CN/')) else 'en'
    type_headers = {'type', 'types', '型別', '類型', '类型'}
    default_headers = {'default', 'defaults', 'default value', '預設值', '默认值'}
    description_headers = {
        'meaning', 'description', 'checks', 'styles', 'properties', 'values', 'value',
        'draws', 'raised when', 'raised or emitted when', 'calculation and extra options',
        '意義', '意义', '含義', '含义', '說明', '说明', '描述', '控制項目', '控制项目',
        '引發或發出的時機', '引发或发出的时机', '引發時機', '引发时机',
    }
    for index, match, headers, rows in reversed(list(reference_tables(source, src))):
        sections = ['<div class="ev-api ev-reference-list" markdown="1">\n']
        for row in rows:
            if len(row) != len(headers):
                raise PluginError(f'{src}: mismatched reference table columns')
            anchor = reference_anchor(index, row)
            label = row[0].strip('`')
            sections.append(f'<section class="ev-api__parameter" id="{anchor}" tabindex="-1" markdown="1">\n')
            types = ''
            default = ''
            description = []
            for heading, cell in zip(headers[1:], row[1:]):
                kind = heading.strip('`* ').casefold()
                if kind in type_headers:
                    values = re.split(r'\s+(?:or|或)\s+|\s*\\?\|\s*', cell)
                    types = f' <span class="ev-api__or">{LABELS[language][2]}</span> '.join(_type(value.strip('` ')) for value in values)
                elif kind in default_headers:
                    value = _python_badges(cell.strip('`'))
                    default = f'<span class="ev-api__default">{LABELS[language][1]} <code>{value}</code></span>'
                else:
                    description.append((heading, cell, kind in description_headers))
            sections.append(f'<div class="ev-api__meta"><a class="ev-api__name" href="#{anchor}">{_parameter_label(label)}</a>'
                            f'<span class="ev-api__types">{types}</span>{default}</div>\n')
            for heading, cell, is_description in description:
                sections.append((cell if is_description or len(description) == 1 else f'**{heading}** — {cell}') + '\n')
            sections.append('</section>\n')
        sections.append('</div>\n')
        rendered = '\n'.join(sections)
        indent = match['indent']
        rendered = '\n'.join(indent + line if line else '' for line in rendered.split('\n'))
        source = source[:match.start()] + rendered + source[match.end():]
    return source


def on_config(config, **kwargs):
    _catalog.clear()
    for path in sorted(DATA.glob("*.json")):
        entries = json.loads(path.read_text(encoding="utf-8"))
        for symbol, item in entries.items():
            if symbol in _catalog:
                raise PluginError(f"{path}: duplicate API definition {symbol}")
            names = [p["name"].lstrip("*") for p in item["parameters"]]
            if len(names) != len(set(names)):
                raise PluginError(f"{symbol}: duplicate parameter names")
            for p in item["parameters"]:
                if any(not p["description"].get(lang) for lang in LABELS):
                    raise PluginError(f'{symbol}.{p["name"]}: missing translation')
            _catalog[symbol] = item
    if str(DATA) not in config.watch:
        config.watch.append(str(DATA))
    _symbols.clear()
    _parameters.clear()
    _custom_classes.clear()
    for names in _class_categories.values():
        _custom_classes.update(names)
    for item in _catalog.values():
        for signature in item.get('signatures', [item.get('name', '')]):
            match = re.match(r'([A-Z][A-Za-z0-9_]*)(?:[.(]|$)', signature)
            if match:
                _custom_classes.add(match[1])
    _sections[:] = json.loads(DATA.with_name('api_sections.json').read_text())
    _custom_classes.update(name for section in _sections for name in section['names'] if name[:1].isupper())
    if getattr(config, 'docs_dir', None):
        for entry in _sections:
            for locale in ('', 'zh-TW/', 'zh-CN/'):
                path = locale + entry['page']
                if not (Path(config.docs_dir) / path).exists():
                    raise PluginError(f'Missing API definition page: {path}')
                for name in entry['names']:
                    _symbols.setdefault(name, set()).add((path, entry['anchor']))
        for path in Path(config.docs_dir).rglob('*.md'):
            src = path.relative_to(config.docs_dir).as_posix()
            for name, anchor in re.findall(r'<!-- api-target: ([\w.]+) ([\w-]+) -->', path.read_text()):
                _symbols.setdefault(name, set()).add((src, anchor))
            for key in re.findall(r'^<!-- api: ([\w.]+) -->', path.read_text(), re.M):
                item = _catalog.get(key)
                if not item:
                    continue
                names = [item['name']] if 'signatures' not in item else [
                    m[1] for signature in item['signatures']
                    if (m := re.match(r'\s*([A-Za-z_]\w*(?:\.\w+)*)\s*(?:\(|$)', signature))
                ]
                for name in names:
                    for alias in {name, name.rsplit('.', 1)[-1]}:
                        _symbols.setdefault(alias, set()).add((src, 'api-' + item['anchor']))
                    for signature in item.get('signatures', []):
                        if signature.lstrip().startswith(name + '('):
                            for arg in re.findall(r'(?:\(|,)\s*([A-Za-z_]\w*)\s*(?=[=,:)])', signature):
                                _parameters.setdefault((name, arg), set()).add((src, 'api-' + item['anchor']))
                owner = next((n for n in names if n[:1].isupper() and '.' not in n), None)
                for i, parameter in enumerate(item['parameters']):
                    target = item['anchor'] + '-' + (str(i) if 'signatures' in item else parameter['name'].lstrip('*'))
                    param = parameter['name'].lstrip('*')
                    if re.fullmatch(r'\w+', param):
                        for name in names:
                            values = _parameters.setdefault((name, param), set())
                            values.discard((src, 'api-' + item['anchor']))
                            values.add((src, target))
                    for method in re.findall(r'([A-Za-z_]\w*)\s*\(', parameter['name']):
                        aliases = {method, owner + '.' + method} if owner else {method}
                        for alias in aliases:
                            _symbols.setdefault(alias, set()).add((src, target))
                        for call in re.finditer(re.escape(method) + r'\(([^)]*)\)', parameter['name']):
                            for arg in re.findall(r'(?:^|,)\s*\**([A-Za-z_]\w*)', call[1]):
                                for alias in aliases:
                                    _parameters.setdefault((alias, arg), set()).add((src, target))
        # A named row is a more precise destination than its containing section.
        for path in Path(config.docs_dir).rglob('*.md'):
            src = path.relative_to(config.docs_dir).as_posix()
            for index, _, _, rows in reference_tables(path.read_text(), src):
                for row in rows:
                    label = row[0].strip('`')
                    name = re.sub(r'\(.*\)$', '', label)
                    if not re.fullmatch(r'[A-Za-z_]\w*(?:\.\w+)*', name):
                        continue
                    targets = _symbols.setdefault(name, set())
                    if any(target[0] == src and target[1].startswith('api-') for target in targets):
                        continue
                    targets.difference_update({target for target in targets if target[0] == src})
                    targets.add((src, reference_anchor(index, row)))
    return config


def on_page_content(html, page, config, **kwargs):
    """Link inline API names, leaving examples and existing links untouched."""
    src = page.file.src_uri
    parts = src.split('/')
    locale = parts.pop(0) if parts[0] in LABELS else 'en'
    package = parts[0]
    prefix = (locale + '/' if locale != 'en' else '') + package + '/'
    blocked = []
    from html import unescape

    def replace(match):
        text = match[0]
        if text.startswith('<code'):
            if any(tag in blocked for tag in ('pre', 'script', 'style')):
                return text
            value = re.sub(r'^<code[^>]*>|</code>$', '', text)
            if '<' in value:
                return text
            value = unescape(value)
            styled = _reference_name(value)
            # Bare member/parameter references have no call parentheses or type
            # marker. Give them their own surface without inventing a link.
            if '<span ' not in styled and re.fullmatch(r'[A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*', value):
                styled = f'<span class="ev-api__attribute">{styled}</span>'
            if '<span ' in styled:
                text = f'<code class="ev-api-inline-code">{styled}</code>'
            if 'a' in blocked:
                return text
            name = re.sub(r'\([^<>]*\)$', '', value)
            if not re.fullmatch(r'[A-Za-z_]\w*(?:\.\w+)*', name):
                return text
            targets = {t for t in _symbols.get(name, ()) if t[0].startswith(prefix)}
            local = {t for t in targets if t[0] == src}
            targets = local or targets
            if len(targets) != 1:
                return text
            target, anchor = next(iter(targets))
            if target == src:
                href = '#' + anchor
            else:
                def url(path):
                    stem = path[:-3]
                    if config.use_directory_urls:
                        return stem[:-5] if stem.endswith('index') else stem + '/'
                    return stem + '.html'
                current = url(src)
                base = current if current.endswith('/') else posixpath.dirname(current)
                href = posixpath.relpath(url(target), base or '.')
                if config.use_directory_urls:
                    href += '/'
                href += '#' + anchor
            return f'<a class="ev-api-inline" href="{href}">{text}</a>'
        tag = re.match(r'<(/?)(a|pre|script|style)\b', text)
        if tag:
            if tag[1]:
                if blocked and blocked[-1] == tag[2]:
                    blocked.pop()
            else:
                blocked.append(tag[2])
        return text

    result = re.sub(r'<code\b[^>]*>.*?</code>|<[^>]+>', replace, html, flags=re.S)
    return link_examples(result, src, config)


def link_examples(markup, src, config):
    """Use Python call context to link highlighted tokens, without executing code."""
    locale = src.split('/')[0] if src.split('/')[0] in LABELS else ''
    current_package = src.split('/')[1 if locale else 0]

    def destination(symbol, parameter=None):
        bits = symbol.split('.')
        package = current_package
        if bits[0].replace('_', '-') in {'utility-viz', 'principle-viz', 'bezierkit', 'mosaickit'}:
            package = bits.pop(0).replace('_', '-')
        name = '.'.join(bits)
        prefix = (locale + '/' if locale else '') + package + '/'
        index = _symbols if parameter is None else _parameters
        candidates = index.get(name if parameter is None else (name, parameter), set())
        candidates = {v for v in candidates if v[0].startswith(prefix)}
        local = {v for v in candidates if v[0] == src}
        candidates = local or candidates
        if len(candidates) != 1:
            return None
        path, anchor = next(iter(candidates))
        if path == src:
            return '#' + anchor
        def url(path):
            if not config.use_directory_urls:
                return path[:-3] + '.html'
            return path[:-8] if path.endswith('index.md') else path[:-3] + '/'
        base = url(src)
        relative = posixpath.relpath(url(path), base if base.endswith('/') else posixpath.dirname(base))
        return relative + ('/' if config.use_directory_urls else '') + '#' + anchor

    def block(match):
        content = match[2]
        if '<a ' in re.sub(r'<a\b[^>]*></a>', '', content) or 'class="' not in content:
            return match[0]
        source = html.unescape(re.sub(r'<[^>]+>', '', content))
        try:
            tree = ast.parse(source)
        except SyntaxError:
            return match[0]
        bindings = {}
        lines = source.splitlines(keepends=True)
        offsets = [0]
        for line in lines:
            offsets.append(offsets[-1] + len(line))
        links = {}

        def offset(row, column):
            return offsets[row - 1] + len(lines[row - 1].encode()[:column].decode())

        def mark(node, label, symbol, parameter=None, at_end=False):
            href = destination(symbol, parameter)
            if href:
                start = (offset(node.end_lineno, node.end_col_offset) - len(label)
                         if at_end else offset(node.lineno, node.col_offset))
                links[start] = (start + len(label), href)

        def resolve(node):
            if isinstance(node, ast.Name):
                return bindings.get(node.id, node.id)
            if isinstance(node, ast.Attribute):
                return resolve(node.value) + '.' + node.attr
            if isinstance(node, ast.Call):
                name = resolve(node.func)
                for item in _catalog.values():
                    declared = item.get('name', '')
                    returns = item.get('returns', '')
                    if declared and (name == declared or name.endswith('.' + declared)) and re.fullmatch(r'[A-Z]\w*', returns):
                        package = name.split('.')[0]
                        return package + '.' + returns if package.replace('_', '-') in {'utility-viz', 'principle-viz', 'bezierkit', 'mosaickit'} else returns
                # Constructors and the documented fluent Canvas/MarketFigure API.
                if name.rsplit('.', 1)[-1][:1].isupper():
                    return name
                if isinstance(node.func, ast.Attribute):
                    owner = resolve(node.func.value)
                    if owner.rsplit('.', 1)[-1] in {'Canvas', 'MarketFigure'}:
                        return owner
            return ''

        class Visitor(ast.NodeVisitor):
            def visit_ImportFrom(self, node):
                for item in node.names:
                    bindings[item.asname or item.name] = (node.module or '').split('.')[0] + '.' + item.name
                    mark(item, item.name, bindings[item.asname or item.name])

            def visit_Import(self, node):
                for item in node.names:
                    bindings[item.asname or item.name] = item.name

            def visit_Assign(self, node):
                self.visit(node.value)
                value = resolve(node.value)
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        bindings[target.id] = value

            def visit_Call(self, node):
                symbol = resolve(node.func)
                if isinstance(node.func, ast.Name):
                    mark(node.func, node.func.id, symbol)
                elif isinstance(node.func, ast.Attribute):
                    mark(node.func, node.func.attr, symbol, at_end=True)
                for keyword in node.keywords:
                    if keyword.arg:
                        mark(keyword, keyword.arg, symbol, keyword.arg)
                self.generic_visit(node)

        Visitor().visit(tree)
        position = 0
        output = []
        for piece in re.split(r'(<[^>]+>)', content):
            if piece.startswith('<'):
                output.append(piece)
                continue
            decoded = html.unescape(piece)
            end = position + len(decoded)
            cursor = position
            for start, (stop, href) in sorted(links.items()):
                if position <= start < stop <= end:
                    output.append(html.escape(decoded[cursor-position:start-position]))
                    output.append(f'<a class="ev-code-link" href="{href}">' + html.escape(decoded[start-position:stop-position]) + '</a>')
                    cursor = stop
            output.append(html.escape(decoded[cursor-position:]))
            position = end
        return match[1] + ''.join(output) + match[3]

    return re.sub(r'(<pre[^>]*>\s*(?:<span></span>)?\s*<code[^>]*>)(.*?)(</code>\s*</pre>)', block, markup, flags=re.S)


def _type(value):
    kind = "none" if value == "None" else "bool" if value == "bool" else "value"
    if any(_python_kind(word) or word in _custom_classes or re.fullmatch(r'[A-Z]\w*(?:Error|Warning|Exception)', word)
           for word in re.findall(r'\b\w+\b', value)):
        return _python_badges(value)
    return f'<span class="ev-api__type ev-api__type--{kind}">{html.escape(value)}</span>'


def _python_kind(word):
    if word in {'None', 'True', 'False'}:
        return 'constant'
    if keyword.iskeyword(word):
        return 'keyword'
    if word in vars(builtins) and not word.startswith('_'):
        return 'builtin'
    return None


def _reference_name(value):
    """Style callable names in compact method lists, including overloads."""
    pieces = []
    last = 0
    for match in re.finditer(API_TOKEN_PATTERN, value):
        word = match[0]
        pieces.append(html.escape(value[last:match.start()]))
        owner, sep, member = word.rpartition('.')
        label = member if sep else word
        callable_name = value[match.end():].lstrip().startswith('(') or (
            word == value and any(anchor.startswith('api-') and not anchor.startswith('api-entry-')
                                  for _, anchor in _symbols.get(word, ())))
        if callable_name and label[:1].islower() and not _python_kind(label):
            prefix = _python_badges(owner) + '.' if sep else ''
            pieces.append(prefix + f'<span class="ev-api__method">{html.escape(label)}</span>')
        else:
            pieces.append(_python_badges(word))
        last = match.end()
    return ''.join(pieces) + html.escape(value[last:])


def _parameter_label(value):
    assignment = re.fullmatch(r'([A-Za-z_]\w*)\s*=(.*)', value)
    if assignment:
        return f'<span class="ev-api__attribute">{html.escape(assignment[1])}</span>=' + _python_badges(assignment[2])
    if re.fullmatch(r'--?[A-Za-z][\w-]*', value):
        return f'<span class="ev-api__attribute">{html.escape(value)}</span>'
    styled = _reference_name(value)
    if '<span ' not in styled and re.fullmatch(r'\**[A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*', value):
        return f'<span class="ev-api__attribute">{styled}</span>'
    return styled


def _python_badges(value):
    # Literal numeric defaults use the Python number highlight color.
    try:
        literal = ast.literal_eval(value)
    except (ValueError, SyntaxError):
        literal = None
    if type(literal) in (int, float, complex):
        return f'<span class="ev-api__python ev-api__python--number">{html.escape(value)}</span>'
    # Strings remain literals, even when they contain a built-in name.
    def replace(match):
        word = match[0]
        if re.fullmatch(r'[A-Z]\w*(?:Error|Warning|Exception)', word):
            category = 'warning' if word.endswith('Warning') else 'error'
            return f'<span class="ev-api__custom ev-api__custom--{category}">{html.escape(word)}</span>'
        kind = _python_kind(word)
        if kind:
            return f'<span class="ev-api__python ev-api__python--{kind}">{html.escape(word)}</span>'
        if word in _custom_classes:
            category = next((kind for kind, names in _class_categories.items() if word in names),
                            'data' if word.endswith(('Result', 'Outcome')) else 'class')
            return f'<span class="ev-api__custom ev-api__custom--{category}">{html.escape(word)}</span>'
        return html.escape(word)
    pieces = []
    last = 0
    for match in re.finditer(r'''"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*'|\b[A-Za-z_]\w*\b''', value):
        pieces.extend([html.escape(value[last:match.start()]), replace(match)])
        last = match.end()
    return ''.join(pieces) + html.escape(value[last:])


def render(symbol, language):
    item = _catalog[symbol]
    if "signatures" in item:
        return render_manual(item, language)
    required, default, either, keywords = LABELS[language]
    anchor = item["anchor"]
    esc = html.escape
    parameters = item["parameters"]
    signature = []
    details = []
    keyword_separator = False
    for p in parameters:
        name = p["name"]
        target = f'{anchor}-{name.lstrip("*")}'
        types = p.get("types", [])
        badges = ' <span class="ev-api__union">|</span> '.join(map(_type, types))
        annotation = f": {badges}" if badges else ""
        if p.get("keyword_only") and not keyword_separator:
            signature.append("    *,")
            keyword_separator = True
        signature.append(f'    <a class="ev-api__argument" href="#{esc(target)}">{_parameter_label(name)}</a>{annotation},')
        types_html = f' <span class="ev-api__or">{either}</span> '.join(map(_type, types))
        if "default" in p:
            status = f'<span class="ev-api__default">{default} <code>{_python_badges(p["default"])}</code></span>'
        else:
            label = keywords if name.startswith("**") else required
            status = f'<span class="ev-api__qualifier">{label}</span>'
        description = md.markdown(
            p["description"][language], extensions=["pymdownx.arithmatex"],
            extension_configs={"pymdownx.arithmatex": {"generic": True}},
        )
        details.append(
            f'<section class="ev-api__parameter" id="{esc(target)}" tabindex="-1">'
            f'<div class="ev-api__meta"><a class="ev-api__name" href="#{esc(target)}">{_parameter_label(name)}</a>'
            f'<span class="ev-api__types">{types_html}</span>{status}</div>{description}</section>'
        )
    name = esc(item["name"])
    body = "\n".join(signature)
    owner, separator, member = item["name"].rpartition(".")
    if separator:
        display = f'<span class="ev-api__owner">{_python_badges(owner)}.</span>'
        display += f'<a class="ev-api__function" href="#api-{esc(anchor)}"><span class="ev-api__method">{esc(member)}</span></a>'
    else:
        kind = "constructor" if item["name"][:1].isupper() else "function"
        label = _python_badges(item['name']) if kind == 'constructor' else _reference_name(item['name'] + '()')[:-2]
        display = f'<a class="ev-api__{kind}" href="#api-{esc(anchor)}">{label}</a>'
    signature_html = display + '('
    signature_html += f'\n{body}\n)' if parameters else ')'
    signature_html += f' → {_type(item["returns"])}'
    return (
        f'<div class="ev-api" id="api-{esc(anchor)}">\n'
        f'<pre class="ev-api__signature" aria-label="{name}"><code>{signature_html}</code></pre>\n'
        + "\n".join(details) + "\n</div>"
    )


def render_manual(item, language):
    """Render manual signatures without inventing unspecified types/defaults."""
    esc = html.escape
    anchor = item["anchor"]
    parameters = item["parameters"]
    targets = {p["name"]: f'{anchor}-{i}' for i, p in enumerate(parameters)}
    signature_parameters = set()
    for signature in item['signatures']:
        signature_parameters.update(re.findall(r'(?:\(|,)\s*\**([A-Za-z_]\w*)\s*(?=[=,:)])', signature))
    def token(match):
        word = match[0]
        if _python_kind(word):
            return _python_badges(word)
        if word in targets:
            return f'<a class="ev-api__argument" href="#{targets[word]}">{_parameter_label(word)}</a>'
        if word in signature_parameters and not match.string[match.end():].lstrip().startswith('('):
            return _parameter_label(word)
        if match.string[match.end():].lstrip().startswith("("):
            owner, sep, member = word.rpartition(".")
            prefix = f'<span class="ev-api__owner">{_python_badges(owner)}.</span>' if sep else ""
            label = member if sep else word
            kind = "constructor" if label[:1].isupper() else "function"
            styled = _python_badges(label) if kind == 'constructor' else f'<span class="ev-api__method">{esc(label)}</span>'
            return prefix + f'<a class="ev-api__{kind}" href="#api-{anchor}">{styled}</a>'
        return _python_badges(word)
    signatures = []
    for signature in item["signatures"]:
        # Escape non-token text separately, including literal defaults.
        pieces = []
        previous = 0
        for match in re.finditer(API_TOKEN_PATTERN, signature):
            pieces.extend([esc(signature[previous:match.start()]), token(match)])
            previous = match.end()
        pieces.append(esc(signature[previous:]))
        signatures.append(''.join(pieces))
    result = [f'<div class="ev-api" id="api-{anchor}">']
    if signatures:
        result.append('<pre class="ev-api__signature"><code>' + '\n'.join(signatures) + '</code></pre>')
    for i, p in enumerate(parameters):
        badges = ' | '.join(_type(t) for t in p.get("types", []))
        default = ''
        if "default" in p:
            default = f'<span class="ev-api__default">{LABELS[language][1]} <code>{_python_badges(p["default"])}</code></span>'
        description = md.markdown(p['description'][language], extensions=['pymdownx.arithmatex'],
                                  extension_configs={'pymdownx.arithmatex': {'generic': True}})
        result.append(f'<section class="ev-api__parameter" id="{anchor}-{i}" tabindex="-1">'
                      f'<div class="ev-api__meta"><a class="ev-api__name" href="#{anchor}-{i}">{_parameter_label(p["name"])}</a>'
                      f'<span class="ev-api__types">{badges}</span>{default}</div>{description}</section>')
    result.append('</div>')
    return '\n'.join(result)


def on_page_markdown(markdown, page, config, **kwargs):
    src = page.file.src_uri
    plain_src = re.sub(r'^zh-(?:TW|CN)/', '', src)
    for entry in _sections:
        if entry['page'] != plain_src or 'heading' not in entry:
            continue
        headings = []
        fenced = False
        for match in re.finditer(r'^.*$', markdown, re.M):
            if match[0].lstrip().startswith(('```', '~~~')):
                fenced = not fenced
            if not fenced and re.match(r'^#{1,6} ', match[0]):
                headings.append(match)
        heading = headings[entry['heading']]
        markdown = markdown[:heading.start()] + f'<span id="{entry["anchor"]}"></span>\n\n' + markdown[heading.start():]
    language = "zh-TW" if src.startswith("zh-TW/") else "zh-CN" if src.startswith("zh-CN/") else "en"
    seen = set()
    aliases = set()

    def replace(match):
        symbol = match[1]
        if symbol not in _catalog:
            raise PluginError(f"{src}: unknown API reference {symbol}")
        if symbol in seen:
            raise PluginError(f"{src}: duplicate API reference {symbol}")
        seen.add(symbol)
        result = render(symbol, language)
        item = _catalog[symbol]
        if 'signatures' in item:
            names = {m[1] for signature in item['signatures']
                     if (m := re.match(r'\s*([\w.]+)\s*\(', signature))}
            for old in _catalog.values():
                if old.get('name') in names:
                    anchor = 'api-' + old['anchor']
                    if anchor not in aliases:
                        result = f'<span id="{anchor}"></span>\n' + result
                        aliases.add(anchor)
        # Markdown inside raw API HTML is rendered before MkDocs' link pass.
        # Resolve those .md links to directory URLs at the same time.
        if config is not None and config.use_directory_urls:
            def relative_link(link):
                path, fragment = link[1], link[2] or ''
                if '://' in path or path.startswith('/'):
                    return link[0]
                prefix = '' if page.file.name == 'index' else '../'
                target = path[:-3]
                if target.endswith('/index'):
                    target = target[:-5]
                elif target == 'index':
                    target = ''
                else:
                    target += '/'
                return f'href="{prefix}{target}{fragment}"'
            result = re.sub(r'href="([^"#]+\.md)(#[^"]*)?"', relative_link, result)
        return result

    # Process only standalone directives, never fenced code examples.
    parts = re.split(r'(^```[^\n]*\n.*?^```[ \t]*$|^~~~[^\n]*\n.*?^~~~[ \t]*$)', markdown, flags=re.M | re.S)
    for i in range(0, len(parts), 2):
        parts[i] = re.sub(r'^<!-- api: ([\w.]+) -->[ \t]*$', replace, parts[i], flags=re.M)
    return render_reference_tables("".join(parts), src)
