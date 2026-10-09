"""Sync the three reference manuals from a sibling agora checkout.

This is an explicit authoring command, never a MkDocs build dependency.
Run with `uv run --frozen python scripts/sync_agora.py /path/to/agora`.
Unknown Typst constructs fail conversion rather than leaking into the site.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import textwrap
import tomllib

import bibtexparser

ROOT = Path(__file__).resolve().parents[1]
LANGS = ('en', 'zh-TW', 'zh-CN')
MAPPING = {
    'principle-viz': {
        '01-introduction': 'guides/introduction', '02-installation': 'installation',
        '03-quickstart': 'quickstart', '04-markets': 'guides/markets',
        '05-discrete': 'guides/discrete', '06-aggregation': 'guides/aggregation',
        '07-elasticity': 'guides/elasticity', '08-welfare': 'guides/welfare',
        '09-taxes': 'guides/taxes', '10-controls': 'guides/controls',
        '11-trade': 'guides/trade', '12-failures': 'guides/failures',
        '13-factor-markets': 'guides/factor-markets', '14-ppf': 'guides/ppf',
        '15-figures': 'guides/figures', '16-cli': 'cli', '17-changelog': 'changelog',
    },
    'mosaickit': {
        '01-introduction': 'guides/introduction', '02-installation': 'installation',
        '03-quickstart': 'quickstart', '04-canvas': 'guides/canvas',
        '05-layers': 'guides/layers', '06-annotations': 'guides/annotations',
        '07-geometry': 'guides/geometry', '08-labels': 'guides/labels',
        '09-styles': 'guides/styles', '10-themes': 'guides/themes',
        '11-parameters': 'guides/parameters', '12-rendering': 'guides/rendering',
        'a-proofs': 'project/proofs', 'changelog': 'project/changelog',
    },
    'bezierkit': {
        '01-introduction': 'guides/introduction', '02-installation': 'installation',
        '03-quickstart': 'quickstart', '04-geometry': 'guides/geometry',
        '05-curves': 'guides/curves', '06-operations': 'guides/operations',
        '07-paths': 'guides/paths', '08-construction': 'guides/construction',
        '09-fitting': 'guides/fitting', '10-implicit': 'guides/implicit',
        '11-export': 'guides/export', '12-cli': 'cli',
        'a-proofs': 'project/proofs', 'a-proofs-b': 'project/proofs-approximation',
        'changelog': 'project/changelog',
    },
}


def balanced(text, start):
    """Read one nested Typst argument/content block, respecting raw code."""
    pairs = {'(': ')', '[': ']', '{': '}'}
    stack = [pairs[text[start]]]
    i = start + 1
    while stack:
        if i >= len(text):
            raise ValueError(f'Unclosed block: {text[start:start+160]}')
        if text.startswith('```', i):
            i = text.index('```', i + 3) + 3
            continue
        if text[i] == '`':
            i = text.index('`', i + 1) + 1
            continue
        if text[i] == '$':
            i = text.index('$', i + 1) + 1
            continue
        if text[i] == '"':
            i += 1
            while text[i] != '"':
                i += 2 if text[i] == '\\' else 1
            i += 1
            continue
        if text[i] in pairs:
            stack.append(pairs[text[i]])
        elif text[i] == stack[-1]:
            stack.pop()
        i += 1
    return text[start+1:i-1], i


def split_args(text):
    args, begin, i = [], 0, 0
    while i < len(text):
        if text[i] in '([{':
            _, i = balanced(text, i)
            continue
        if text[i] == '"':
            match = re.match(r'"(?:\\.|[^"\\])*"', text[i:])
            i += len(match[0]); continue
        if text[i] == ',':
            args.append(text[begin:i].strip()); begin = i+1
        i += 1
    args.append(text[begin:].strip())
    return [a for a in args if a]


def string(text):
    return json.loads(text.strip())


def math_latex(value):
    """Translate the math vocabulary used by the pinned agora chapters."""
    # Typst braces denote visible sets; TeX braces would silently group them.
    parts = re.split(r'(\\text\{[^}]*\})', value)
    value = ''.join(p if i % 2 else p.replace('{', r'\lbrace ').replace('}', r'\rbrace ') for i,p in enumerate(parts))
    value = re.sub(r'"([^"]*)"', lambda m: r'\text{' + m[1] + '}', value.strip())
    for word, environment in [('cases', 'cases'), ('mat', 'pmatrix')]:
        while (m := re.search(r'\b'+word+r'\(', value)):
            inner, end = balanced(value, m.end()-1)
            rows = split_args(inner) if word == 'cases' else inner.split(';')
            rendered = [math_latex(row) if word == 'cases' else ' & '.join(math_latex(cell) for cell in split_args(row)) for row in rows]
            replacement = r'\begin{' + environment + '}' + r' \\ '.join(rendered) + r'\end{' + environment + '}'
            value = value[:m.start()] + replacement + value[end:]
    # Function arguments must be grouped before replacing identifiers.
    functions = {'binom': ('\\binom', 2), 'sqrt': ('\\sqrt', 1),
                 'abs': ('\\left|', 1), 'norm': ('\\left\\lVert', 1),
                 'ceil': ('\\left\\lceil', 1), 'floor': ('\\left\\lfloor', 1),
                 'overline': ('\\overline', 1), 'tilde': ('\\widetilde', 1),
                 'cal': ('\\mathcal', 1), 'text': ('\\text', 1)}
    for word, (command, arity) in functions.items():
        while (m := re.search(r'(?<![\\\w])'+word+r'\(', value)):
            args, end = balanced(value, m.end()-1)
            parts = split_args(args) if arity == 2 else [args]
            converted = [math_latex(p) for p in parts]
            ends = {'abs': r'\right|', 'norm': r'\right\rVert', 'ceil': r'\right\rceil', 'floor': r'\right\rfloor'}
            replacement = command + (' '+ ' '.join(converted) + ' '+ends[word] if word in ends else ''.join('{'+p+'}' for p in converted))
            value = value[:m.start()] + replacement + value[end:]
    # Parenthesized scripts in Typst are TeX brace groups.
    while (m := re.search(r'[_^]\(', value)):
        inner, end = balanced(value, m.end()-1)
        value = value[:m.start()+1] + '{' + inner + '}' + value[end:]
    symbols = {
        'RR': r'\mathbb{R}', 'dif': r'\mathrm{d}', 'slash': '/', 'dots': r'\ldots',
        'dots.c': r'\cdots', 'dot': r'\cdot', 'times': r'\times', 'quad': r'\quad',
        'thin': r'\,', 'oo': r'\infty', 'in.not': r'\notin', 'in': r'\in',
        'union': r'\cup', 'inter': r'\cap', 'without': r'\setminus',
        'subset.eq.not': r'\nsubseteq', 'subset.eq': r'\subseteq',
        'supset.eq': r'\supseteq', 'subset': r'\subset',
        'circle.small': r'\circ', 'triangle.r': r'\triangleright',
        'plus.minus': r'\pm', 'emptyset': r'\emptyset',
    }
    for word in 'sum int partial nabla alpha beta gamma delta epsilon lambda mu phi theta xi Gamma rho Omega omega psi Delta Pi pi tau ell sigma kappa min max log sin cos inf sup det mod approx'.split():
        symbols[word] = '\\'+word
    pattern = r'(?<![\\A-Za-z])(' + '|'.join(re.escape(w) for w in sorted(symbols, key=len, reverse=True)) + r')(?![A-Za-z])'
    # Protect existing TeX commands/text from recursive conversion.
    pieces = re.split(r'(\\text\{[^}]*\})', value)
    value = ''.join(p if i % 2 else re.sub(pattern, lambda m: symbols[m[0]], p) for i,p in enumerate(pieces))
    value = re.sub(r'([_^])(\\(?:min|max))\b', r'\1{\2}', value)
    value = value.replace('>=',r'\ge ').replace('<=',r'\le ').replace('!=',r'\ne ')
    value = value.replace('->',r'\to ').replace('=>',r'\Rightarrow ')
    value = re.sub(r'\\(?=\s|$)', r'\\\\', value)
    if '&' in value and r'\begin{' not in value:
        value = r'\begin{aligned}' + value + r'\end{aligned}'
    return re.sub(r'\s+', ' ', value).strip()


class Converter:
    def __init__(self, agora, package, locale, catalog, labels, bibliography):
        self.agora, self.package, self.locale = agora, package, locale
        self.catalog, self.labels, self.bibliography = catalog, labels, bibliography
        self.meta = tomllib.loads((agora/'packages'/package/'manual.toml').read_text())['package']
        self.destination = ''
        self.counter = 0
        self.current = None
        self.changes = []
        self.assets = set()

    def link(self, label):
        target, title = self.labels[label]
        relative = os.path.relpath(target+'.md', Path(self.destination).parent)
        title=self.convert(title).replace('\n',' ')
        return f'[{title}]({relative}#{label})'

    def convert(self, text):
        text = textwrap.dedent(text).strip()
        output, i = [], 0
        while i < len(text):
            if text.startswith('```', i):
                end = text.index('```', i+3)+3
                output.append(text[i:end]); i=end; continue
            if text[i] == '`':
                end=text.index('`',i+1)+1
                output.append(text[i:end]); i=end; continue
            if text[i] == '$':
                end=text.index('$',i+1)
                raw=text[i+1:end]
                latex=math_latex(raw)
                display = raw[:1].isspace() and raw[-1:].isspace()
                output.append('\n\n$$\n'+latex+'\n$$\n\n' if display else '$'+latex+'$')
                i=end+1; continue
            if text.startswith('#import ',i):
                end=text.find('\n',i)
                i=len(text) if end<0 else end+1; continue
            match=re.match(r'#([\w-]+)',text[i:]) if text[i]=='#' else None
            if match:
                name=match[1]; i+=len(match[0]); args=''; body=None
                if i<len(text) and text[i]=='(':
                    args,i=balanced(text,i)
                if i<len(text) and text[i]=='[':
                    body,i=balanced(text,i)
                label=re.match(r'[ \t]*<([\w-]+)>',text[i:])
                if label:
                    output.append('\n\n<span id="'+label[1]+'"></span>\n\n')
                    i+=len(label[0])
                output.append(self.macro(name,args,body)); continue
            if text[i]=='@':
                m=re.match(r'@([\w-]+)',text[i:])
                if m:
                    output.append(self.link(m[1])); i+=len(m[0]); continue
            if text[i]=='<' and (m:=re.match(r'<([\w-]+)>',text[i:])):
                output.append('\n\n<span id="'+m[1]+'"></span>\n\n'); i+=len(m[0]); continue
            if text.startswith('\\;',i):
                output.append(';'); i+=2; continue
            output.append(text[i]); i+=1
        result=''.join(output)
        result=re.sub(r'^(={1,6}) (.*)$',lambda m:'#'*len(m[1])+' '+m[2],result,flags=re.M)
        return re.sub(r'\n{3,}', '\n\n', '\n'.join(line.rstrip() for line in result.splitlines())).strip()

    def macro(self,name,args,body):
        if name in ('pkg','raw','meta'):
            return '`'+string(args)+'`'
        if name=='pkg-meta':
            return str(self.meta[string(args)])
        if name=='url':
            url=string(args); return '['+url+']('+url+')'
        if name=='ref':
            return self.link(re.search(r'<([\w-]+)>',args)[1])
        if name in ('citet','citep'):
            key=re.search(r'<([^>]+)>',args)[1]
            entry=self.bibliography[key]
            author=entry.get('author',entry.get('title',key)).split(' and ')[0].split(',')[0]
            year=entry.get('year','')
            title=f'{author} ({year})'
            url=os.path.relpath('project/references.md',Path(self.destination).parent)
            return '['+title+']('+url+'#'+key+')'
        if name in ('box','full-width'):
            return self.convert(body)
        if name in ('emph', 'strong'):
            marker='*' if name=='emph' else '**'
            return marker+self.convert(body)+marker
        if name=='footnote':
            return ' ('+self.convert(body)+')'
        if name=='heading':
            return '# '+self.convert(body)
        if name=='pagebreak': return ''
        if name=='LaTeX': return 'LaTeX'
        if name=='example': return '\n\n'+args.strip()+'\n\n'
        if name=='changed':
            version=string(split_args(args)[0]); description=self.convert(body)
            label=re.search(r'label:\s*("(?:\\.|[^"\\])*")',args)
            self.changes.append((version,string(label[1]) if label else '',description,self.destination))
            # Release history belongs exclusively on the project changelog.
            return ''
        if name=='changelog': return '<!-- agora-change-history -->'
        if name=='fig':
            parts=split_args(args); src=string(parts[0]).lstrip('/')
            caption=next((p[len('caption:'):].strip()[1:-1] for p in parts if p.startswith('caption:')), '')
            caption=self.convert(caption).replace('\n',' ')
            original=self.agora/'packages'/self.package/src
            dest=ROOT/'docs/assets'/self.package/'agora'/Path(src).relative_to('figures')
            if dest.suffix=='.pdf': dest=dest.with_suffix('.svg')
            dest.parent.mkdir(parents=True,exist_ok=True)
            if str(original) not in self.assets:
                if original.suffix=='.pdf':
                    subprocess.run(['pdftocairo','-svg',str(original),str(dest)],check=True)
                else: shutil.copyfile(original,dest)
                self.assets.add(str(original))
            pagepath=ROOT/'docs'/('' if self.locale=='en' else self.locale)/self.package/(self.destination+'.md')
            url=os.path.relpath(dest,pagepath.parent)
            return f'\n\n![{caption}]({url}){{ .ev-figure-sm }}\n\n'
        if name=='api':
            self.counter+=1
            parts=split_args(args)
            names=[string(p) for p in split_args(parts[0][1:-1])]
            syntax=next((p[len('syntax:'):].strip()[1:-1] for p in parts if p.startswith('syntax:')), '')
            signatures=[]
            for line in re.split(r'\\\s*\n',syntax.strip()):
                fragments=re.findall(r'#(?:raw|meta)\(("(?:\\.|[^"\\])*")\)',line)
                joined=''.join(string(p) for p in fragments)
                if joined: signatures.append(joined)
            if not signatures: signatures=names
            joined_signatures=[]
            for signature in signatures:
                if joined_signatures and joined_signatures[-1].count('(')>joined_signatures[-1].count(')'):
                    joined_signatures[-1]+=' '+signature.strip()
                else: joined_signatures.append(signature)
            signatures=joined_signatures
            for index, signature in enumerate(signatures):
                for full_name in names:
                    if '.' in full_name and signature.startswith(full_name.rsplit('.',1)[1]+'('):
                        signature=full_name.rsplit('.',1)[0]+'.'+signature
                # Long signatures use the same one-parameter-per-line layout.
                opening=signature.find('(')
                if opening>=0:
                    content,end=balanced(signature,opening)
                    arguments=split_args(content)
                    if len(arguments)>2 or len(signature)>75:
                        signature=signature[:opening+1]+'\n    '+',\n    '.join(arguments)+'\n'+signature[end-1:]
                signatures[index]=signature
            slug=self.destination.replace('/','-')+'-'+str(self.counter)
            key='agora.'+self.package.replace('-','_')+'.'+slug.replace('-','_')
            self.current=key
            if key not in self.catalog:
                self.catalog[key]={'name':names[0], 'anchor':self.package+'-'+slug,
                                   'signatures':signatures, 'parameters':[]}
            # Keep parameter translations grouped under the same API card.
            self.param_index=0
            description=self.convert(body)
            self.current=key
            return '\n\n<!-- api: '+key+' -->\n\n'+description+'\n\n'
        if name=='param':
            parts=split_args(args); parameter=string(parts[0])
            standalone=''
            if self.current is None:
                self.counter+=1
                slug=self.destination.replace('/','-')+'-'+str(self.counter)
                self.current='agora.'+self.package.replace('-','_')+'.'+slug.replace('-','_')
                self.param_index=0
                self.catalog.setdefault(self.current,{'name':parameter,'anchor':self.package+'-'+slug,'signatures':[], 'parameters':[]})
                standalone='\n\n<!-- api: '+self.current+' -->\n\n'
            description=self.convert(body)
            p={'name':parameter,'types':[], 'description':{}}
            for part in parts[1:]:
                k,v=part.split(':',1)
                if k.strip()=='type': p['types']=[string(v)]
                if k.strip()=='default': p['default']=string(v)
            entry=self.catalog[self.current]
            if self.locale=='en': entry['parameters'].append(p)
            target=entry['parameters'][self.param_index]
            if target['name']!=parameter:
                raise ValueError(f'Parameter mismatch: {self.current}: {target["name"]} != {parameter}')
            target['description'][self.locale]=description
            self.param_index+=1
            return standalone
        if name in ('definition','lemma','proposition','theorem','corollary','proof'):
            titles={'en':{'definition':'Definition','lemma':'Lemma','proposition':'Proposition','theorem':'Theorem','corollary':'Corollary','proof':'Proof'},
                    'zh-TW':{'definition':'定義','lemma':'引理','proposition':'命題','theorem':'定理','corollary':'推論','proof':'證明'},
                    'zh-CN':{'definition':'定义','lemma':'引理','proposition':'命题','theorem':'定理','corollary':'推论','proof':'证明'}}
            title=titles[self.locale][name]
            if args.startswith('name:'):
                title+=' · '+self.convert(args.split(':',1)[1].strip()[1:-1])
            if args.startswith('of:'):
                label=re.search(r'<([\w-]+)>',args)[1]
                content=self.link(label)+'\n\n'+self.convert(body)
            else: content=self.convert(body)
            kind='??? note' if name=='proof' else '!!! abstract'
            return '\n\n'+kind+' "'+title.replace('"','&quot;')+'"\n\n'+textwrap.indent(content,'    ')+'\n\n'
        if name=='tbl': return '\n\n'+self.convert(body)+'\n\n'
        if name=='booktabs':
            parts=split_args(args)
            header=next(p.split(':',1)[1].strip() for p in parts if p.startswith('header:'))
            headers=[self.convert(p[1:-1]) for p in split_args(header[1:-1])]
            cells=[self.convert(p[1:-1]).replace('\n',' ').replace('|','\\|') for p in parts if p.startswith('[')]
            rows=[headers,['---']*len(headers)]+[cells[i:i+len(headers)] for i in range(0,len(cells),len(headers))]
            return '\n'+'\n'.join('| '+' | '.join(row)+' |' for row in rows)+'\n'
        raise ValueError(f'Unsupported macro #{name} in {self.package}/{self.locale}/{self.destination}')


def run(agora):
    catalog={}; manifest={}; nav={}
    for package,mapping in MAPPING.items():
        package_root=agora/'packages'/package
        bibliography={e['ID']:e for e in bibtexparser.loads((package_root/'config/refs.bib').read_text()).entries}
        nav[package]={}
        for locale in LANGS:
            base=ROOT/'docs'/('' if locale=='en' else locale)/package
            labels={}
            for stem,destination in mapping.items():
                text=(package_root/'chapters'/locale/(stem+'.typ')).read_text()
                for label in re.findall(r'(?<!@)<([\w-]+)>',text):
                    # Only declarations, not references in macro arguments.
                    if not re.search(r'(?m)(?:\]|\)|[^\s])\s*<'+re.escape(label)+r'>\s*$',text): continue
                    title=re.search(r'^=+\s+(.+?)\s*<'+re.escape(label)+'>',text,re.M)
                    labels[label]=(destination,title[1] if title else label)
                for match in re.finditer(r'#(?:fig|definition|lemma|proposition|theorem|corollary|tbl)\(',text):
                    args,end=balanced(text,match.end()-1)
                    if end<len(text) and text[end]=='[':
                        _,end=balanced(text,end)
                    label=re.match(r'\s*<([\w-]+)>',text[end:])
                    if label:
                        title=next((p.split(':',1)[1].strip()[1:-1] for p in split_args(args) if p.startswith(('name:','caption:'))),label[1])
                        labels[label[1]]=(destination,title)
            converter=Converter(agora,package,locale,catalog,labels,bibliography)
            for stem,destination in mapping.items():
                source=package_root/'chapters'/locale/(stem+'.typ')
                raw=source.read_text()
                converter.destination=destination; converter.counter=0; converter.current=None
                body=converter.convert(raw)
                title_match=re.search(r'^# (.+)',body,re.M)
                if title_match:
                    title=title_match[1].strip()
                else:
                    title={'en':'Approximation proofs','zh-TW':'近似方法的證明','zh-CN':'近似方法的证明'}[locale]
                    body='# '+title+'\n\n'+body
                nav[package].setdefault(destination,{})[locale]=title
                header='---\nseo_title: '+json.dumps(title,ensure_ascii=False)+'\n---\n\n'
                path=base/(destination+'.md'); path.parent.mkdir(parents=True,exist_ok=True)
                path.write_text(header+body+'\n')
                manifest[str(path.relative_to(ROOT))]={'source':str(source.relative_to(agora)), 'sha256':hashlib.sha256(raw.encode()).hexdigest()}
            # Release entries point to the chapter where the change is documented.
            changelog=base/(next(v for k,v in mapping.items() if 'changelog' in k)+'.md')
            history=[]
            for version in sorted({c[0] for c in converter.changes},key=lambda v:tuple(int(n) for n in re.findall(r'\d+',v)),reverse=True):
                history.append('## '+version+'\n')
                for v,label,description,destination in converter.changes:
                    if v==version:
                        url=os.path.relpath(base/(destination+'.md'),changelog.parent)
                        history.append('- '+('`'+label+'` — ' if label else '')+description.replace('\n',' ')+' ['+nav[package][destination][locale]+']('+url+')')
                history.append('')
            changelog.write_text(changelog.read_text().replace('<!-- agora-change-history -->','\n'.join(history)))
            references=['# '+{'en':'References','zh-TW':'參考文獻','zh-CN':'参考文献'}[locale],'']
            for key,e in bibliography.items():
                references += [f'## {key} {{#{key}}}', '',
                    e.get('author','').replace(' and ','; ')+'. ('+e.get('year','')+'). *'+e.get('title','').replace('{','').replace('}','')+'*. '+e.get('publisher',e.get('journal',''))+'.', '']
                if e.get('doi'): references += ['[DOI](https://doi.org/'+e['doi']+')','']
                elif e.get('url'): references += ['[Source]('+e['url']+')','']
            (base/'project').mkdir(exist_ok=True)
            (base/'project/references.md').write_text('\n'.join(references))
    (ROOT/'hooks/api_data/agora.json').write_text(json.dumps(catalog,ensure_ascii=False,indent=2)+'\n')
    (ROOT/'scripts/agora-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    (ROOT/'scripts/agora-navigation.json').write_text(json.dumps(nav,ensure_ascii=False,indent=2)+'\n')
    print(f'Synced {len(manifest)} pages and {len(catalog)} API groups.')


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('agora',type=Path)
    run(parser.parse_args().agora.resolve())
