"""Valida os templates: A4 sem estouro, preenchimento minimo, sem travessao, sem border-left colorido, tags balanceadas.
Sai com codigo 1 se algo falhar (bloqueia a sincronizacao com o Drive)."""
import sys, glob, re, os
from playwright.sync_api import sync_playwright

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
files = sorted(glob.glob(os.path.join(ROOT, 'templates', '*.html')))
erros = []
JS = '''()=>[...document.querySelectorAll('.pg')].map((p,i)=>{var b=p.querySelector('.body');if(!b)return {i:i+1,cover:1};
var fl=b.querySelector('.fill');return {i:i+1,h:Math.round(p.getBoundingClientRect().height),
over:Math.round(fl.scrollHeight-b.clientHeight),fill:Math.round(fl.getBoundingClientRect().height/b.clientHeight*100)}})'''

with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 900, 'height': 1200})
    for f in files:
        nome = os.path.basename(f)
        src = open(f, encoding='utf-8').read()
        if src.count('<div') != src.count('</div>'): erros.append(f'{nome}: div desbalanceada')
        if '—' in src: erros.append(f'{nome}: travessão encontrado')
        if re.search(r'border-left:[^;]*(#|var\(--b)', src): erros.append(f'{nome}: border-left colorido')
        pg.goto('file://' + os.path.abspath(f)); pg.wait_for_timeout(1500)
        for x in pg.evaluate(JS):
            if x.get('cover'): continue
            if x['h'] > 1123: erros.append(f'{nome} pág. {x["i"]}: altura {x["h"]}px acima do A4')
            if x['over'] > 0: erros.append(f'{nome} pág. {x["i"]}: conteúdo estoura {x["over"]}px')
            if x['fill'] < 55: erros.append(f'{nome} pág. {x["i"]}: preenchimento {x["fill"]}% abaixo de 55%')
        print('ok' if not any(e.startswith(nome) for e in erros) else 'FALHA', nome)
    b.close()

if erros:
    print('\n'.join(erros)); sys.exit(1)
print(f'{len(files)} templates validados')
