"""Converte GUIA-GEMINI.md em pdf/Guia dos Templates de Planejamento.pdf (arquivo lido pelos Gems)."""
import os, re, markdown
from playwright.sync_api import sync_playwright

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
md = open(os.path.join(ROOT, 'GUIA-GEMINI.md'), encoding='utf-8').read()
versao = re.search(r'v\d+\.\d+\.\d+', md.splitlines()[0])
body = markdown.markdown(md, extensions=['tables'])
html = f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@500;700;800&family=Albert+Sans:wght@400;600&display=swap" rel="stylesheet">
<style>
@page{{size:A4;margin:16mm 15mm 18mm}}
body{{font-family:'Albert Sans',sans-serif;color:#2F2F2F;font-size:9.5pt;line-height:1.45}}
h1,h2,h3{{font-family:'DM Sans',sans-serif;color:#052E7D}}
h1{{font-size:18pt;border-bottom:3px solid #F0AD0C;padding-bottom:3mm}}
h2{{font-size:13pt;margin-top:7mm;break-after:avoid}}
table{{width:100%;border-collapse:collapse;margin:2mm 0 4mm;font-size:8.6pt;break-inside:auto}}
th{{background:#052E7D;color:#fff;font-family:'DM Sans',sans-serif;font-size:7.4pt;text-transform:uppercase;letter-spacing:.06em;text-align:left;padding:1.8mm 2mm}}
td{{padding:1.6mm 2mm;border-bottom:1px solid rgba(47,47,47,.12);vertical-align:top}}
tr:nth-child(even) td{{background:#F5F5F7}}
code{{background:#F5F5F7;padding:0 1mm;border-radius:2px}}
hr{{border:none;border-top:1px solid rgba(47,47,47,.18);margin:6mm 0}}
</style></head><body>{body}</body></html>'''

tmp = os.path.join(ROOT, 'pdf', '_guia.html')
open(tmp, 'w', encoding='utf-8').write(html)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page()
    pg.goto('file://' + os.path.abspath(tmp)); pg.wait_for_timeout(1500)
    pg.pdf(path=os.path.join(ROOT, 'pdf', 'Guia dos Templates de Planejamento.pdf'), format='A4', print_background=True,
           display_header_footer=True, header_template='<span></span>',
           footer_template=f'<div style="font-size:7pt;width:100%;text-align:center;color:#777">All.Q Agência · Guia dos Templates · {versao.group(0) if versao else ""} · <span class="pageNumber"></span>/<span class="totalPages"></span></div>',
           margin={'top': '16mm', 'bottom': '18mm', 'left': '15mm', 'right': '15mm'})
    b.close()
os.remove(tmp)
print('Guia gerado')
