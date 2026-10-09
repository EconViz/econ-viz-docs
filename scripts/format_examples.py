"""Format Python Markdown examples using the authoring tool `black`.

Run after syncing manuals: python scripts/format_examples.py
Only complete Python snippets are changed; AST equivalence is checked.
"""
import ast
import io
from pathlib import Path
import re
import subprocess
import tokenize
from functools import lru_cache

ROOT = Path(__file__).resolve().parents[1]


@lru_cache(maxsize=None)
def format_python(source):
    try:
        before = ast.dump(ast.parse(source))
    except SyntaxError:
        return source
    lines = source.splitlines()
    comments = {}
    for token in tokenize.generate_tokens(io.StringIO(source).readline):
        if token.type == tokenize.COMMENT:
            row, col = token.start
            if lines[row - 1][:col].strip():
                comments[row - 1] = (col, token.string)
    expanded = []
    for i, line in enumerate(lines):
        if i in comments:
            col, comment = comments[i]
            # Keep directives attached to their statement.
            if not re.match(r'#\s*(?:type:|noqa|fmt:)', comment):
                indent = line[:len(line) - len(line.lstrip())]
                expanded.append(indent + comment)
                line = line[:col].rstrip()
        expanded.append(line)
    result = subprocess.run(
        ['black', '--quiet', '--line-length', '64', '-'],
        input='\n'.join(expanded) + '\n', text=True,
        capture_output=True, check=True,
    ).stdout
    if ast.dump(ast.parse(result)) != before:
        raise ValueError('Formatting changed Python semantics')
    return result


def run():
    changed = 0
    pattern = re.compile(r'^(?P<indent> *)```python[^\n]*\n(?P<body>.*?)^(?P=indent)```', re.M | re.S)
    for path in (ROOT / 'docs').rglob('*.md'):
        original = path.read_text()
        def replace(match):
            indent = match['indent']
            body = '\n'.join(line[len(indent):] if line.startswith(indent) else line
                             for line in match['body'].splitlines()) + '\n'
            formatted = format_python(body)
            return match[0][:match[0].index('\n') + 1] + ''.join(
                indent + line + '\n' if line else '\n' for line in formatted.splitlines()
            ) + indent + '```'
        result = pattern.sub(replace, original)
        if result != original:
            path.write_text(result)
            changed += 1
    print(f'Formatted examples in {changed} pages; Python ASTs preserved.')


if __name__ == '__main__':
    run()
