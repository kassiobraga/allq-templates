import base64, os

HERE = os.path.dirname(__file__)
SCR = os.path.join(HERE, 'timbrado.svg')
# ALLQ_TIMB_URL: versão para o Gem, com o timbrado por link em vez de embutido
TIMB = os.environ.get('ALLQ_TIMB_URL') or ('data:image/svg+xml;base64,' + base64.b64encode(open(SCR, 'rb').read()).decode())
OUTDIR = os.environ.get('ALLQ_OUT', 'templates')
# ALLQ_CSS_URL: versão para o Gem, com o CSS num arquivo hospedado em vez de embutido.
# O Gem só precisa copiar uma linha do <head> e escrever o <body> com as classes oficiais.
CSS_URL = os.environ.get('ALLQ_CSS_URL')

FONTS = 'https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Albert+Sans:wght@400;500;600&display=swap'

CSS = """
@page{size:210mm 297mm;margin:0}
*{box-sizing:border-box;margin:0;padding:0;-webkit-print-color-adjust:exact;print-color-adjust:exact}
:root{--bd:#052E7D;--bc:#0070FE;--hn:#F0AD0C;--or:#EE8C0D;--jet:#2F2F2F;--lbl:#C1C4CC;--nv:#0A1730;--off:#EBEBEB;--g:#F5F5F7;--mut:rgba(47,47,47,.62);--brd:rgba(47,47,47,.10)}
body{background:#D9DCE3;font-family:'Albert Sans',sans-serif;color:var(--jet);font-size:8.4pt;line-height:1.42}
h1,h2,h3,h4,.kick,.bl,.bv,.num,.sec-n,.kv-val,.kv-lbl,.pill,.tagline,.idx-l,.idx-n,.idx-t,.tbl th,.ihd,.own-n,.own-mk,.st,.chip,.cal th,.cal .dn,.cal .ft,.pc-h,.lg{font-family:'DM Sans',sans-serif}
.pg{width:210mm;height:297mm;margin:10mm auto;position:relative;overflow:hidden;background:#fff url(TIMB) center/100% 100% no-repeat}
@media print{body{background:#fff}.pg{margin:0;break-after:page;page-break-after:always}}

/* capa */
.band{position:absolute;left:0;right:0;top:40mm;min-height:17mm;background:var(--bd);display:grid;grid-template-columns:repeat(4,1fr);align-items:start;padding:4.4mm 0 4mm}
.band .c{padding:0 7mm;position:relative;min-width:0}
.band .c:first-child{padding-left:15mm}
.band .c+.c::before{content:"";position:absolute;left:0;top:.4mm;width:1px;height:9.4mm;background:rgba(255,255,255,.22)}
.bl{display:block;font-size:6.6pt;font-weight:700;letter-spacing:.15em;text-transform:uppercase;color:var(--lbl);margin-bottom:1.6mm}
.bv{display:block;font-size:9.2pt;font-weight:700;color:#fff;line-height:1.24}
.band .ph{color:#AFC3EE}
.cv-top{position:absolute;top:74mm;left:15mm;right:15mm;display:flex;justify-content:space-between;align-items:baseline}
.kick{font-size:7pt;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--bd)}
.tagline{font-size:7pt;font-weight:600;color:var(--mut);letter-spacing:.04em}
.cv-main{position:absolute;top:84mm;left:15mm;width:160mm}
.cv-main h1{font-size:33pt;font-weight:500;line-height:1.06;color:var(--bd);letter-spacing:-.01em}
.cv-main h1 b{display:block;font-weight:800;color:var(--bc)}
.rule{width:34mm;height:3px;background:var(--hn);margin-top:4mm}
.lead{margin-top:8mm;font-size:10.5pt;line-height:1.5;max-width:134mm}
.by{margin-top:4mm;font-size:8pt;color:rgba(47,47,47,.55)}
.idx{position:absolute;left:15mm;right:15mm;bottom:40mm}
.idx-t{font-size:6.6pt;font-weight:700;letter-spacing:.15em;text-transform:uppercase;color:var(--mut);margin-bottom:3mm}
.idx-g{display:grid;grid-template-columns:repeat(5,1fr);gap:4mm}
.idx-g div{border-top:1px solid rgba(47,47,47,.25);padding-top:2.6mm}
.idx-n{display:block;font-size:7pt;font-weight:800;color:var(--bc);margin-bottom:1mm}
.idx-l{display:block;font-size:8pt;font-weight:600;line-height:1.25}

/* paginas internas */
.idb{position:absolute;left:0;right:0;top:37mm;height:8mm;background:var(--bd);display:flex;align-items:center;justify-content:space-between;padding:0 15mm;font-family:'DM Sans',sans-serif}
.idb .l{font-size:7.6pt;font-weight:700;color:#fff;letter-spacing:.03em}
.idb .l .ph{color:#AFC3EE}
.idb .r{font-size:6.6pt;font-weight:700;color:var(--lbl);letter-spacing:.14em;text-transform:uppercase}
.idb .r b{color:#fff;margin-left:2.4mm;letter-spacing:.06em}
.body{position:absolute;top:50mm;left:15mm;right:15mm;height:212mm;overflow:hidden}
.sec{margin-bottom:5.5mm}
.sec:last-child{margin-bottom:0}
.sec-h{display:flex;align-items:center;gap:3mm;margin-bottom:3mm}
.sec-n{flex:none;width:7mm;height:7mm;background:var(--nv);color:#fff;font-size:7.6pt;font-weight:700;display:flex;align-items:center;justify-content:center}
.sec-h h2{font-size:12.5pt;font-weight:700;color:var(--bd);line-height:1.15}
.sec-s{font-size:7.8pt;color:var(--mut);margin-top:.4mm}
h3{font-size:9pt;font-weight:700;color:var(--bd);margin:0 0 2mm}

.tbl{width:100%;border-collapse:collapse;font-size:7.9pt;line-height:1.35}
.tbl th{background:var(--bd);color:#fff;font-size:6.4pt;letter-spacing:.08em;text-transform:uppercase;font-weight:700;text-align:left;padding:1.8mm 2.2mm;vertical-align:bottom}
.tbl td{padding:1.7mm 2.2mm;border-bottom:1px solid var(--brd);vertical-align:top}
.tbl tr:nth-child(even) td{background:var(--g)}
.tbl td.k{font-family:'DM Sans',sans-serif;font-weight:700;color:var(--bd);white-space:nowrap}
.tbl td.c,.tbl th.c{text-align:center}
.tbl td.bar{padding:1.7mm .8mm}
.tbl td.bar i{display:block;height:3.2mm;border-radius:2px;background:var(--bc)}
.tbl td.bar i.y{background:var(--hn)}
.tbl tr.tot td{background:rgba(5,46,125,.07)!important;font-family:'DM Sans',sans-serif;font-weight:700;color:var(--bd)}

.kv{display:grid;grid-template-columns:repeat(5,1fr);gap:2.5mm}
.kv.k4{grid-template-columns:repeat(4,1fr)}
.kv.k3{grid-template-columns:repeat(3,1fr)}
.kvb{background:var(--g);border-radius:6px;padding:3mm 3mm 2.6mm}
.kv-val{font-size:15pt;font-weight:800;color:var(--bd);line-height:1.1}
.kv-lbl{display:block;font-size:6.4pt;font-weight:700;letter-spacing:.1em;text-transform:uppercase;margin-top:1.2mm}
.kv-src{display:block;font-size:6.6pt;color:var(--mut);margin-top:.6mm}

.two{display:grid;grid-template-columns:1fr 1fr;gap:5mm}
.chips{display:flex;flex-wrap:wrap;gap:1.6mm}
.chip{background:rgba(0,112,254,.08);color:var(--bd);border-radius:20px;padding:1mm 3mm;font-size:7.4pt;font-weight:600}
.chip.neg{background:rgba(238,140,13,.13);color:#8A4F05}
.note{display:flex;gap:2.5mm;align-items:flex-start;border:1px solid rgba(47,47,47,.16);border-radius:6px;padding:2.6mm 3mm;font-size:7.8pt}
.note svg{flex:none;width:4mm;height:4mm;color:var(--bc);margin-top:.2mm}
.note b{font-family:'DM Sans',sans-serif;color:var(--bd)}
.ph{color:#8C93A3;font-style:italic}
.cb{display:inline-block;width:3mm;height:3mm;border:1px solid rgba(47,47,47,.45);border-radius:1px;margin-right:2mm;vertical-align:-.5mm;flex:none}
ul.chk{list-style:none;display:grid;gap:1.6mm}
ul.chk li{display:flex;align-items:flex-start;font-size:7.9pt}
ul.chk li .cb{margin-top:.3mm}
ul.bl{padding-left:4mm;display:grid;gap:1mm;font-size:7.9pt}
.st{display:inline-block;font-size:6.4pt;font-weight:700;padding:.5mm 2mm;border-radius:10px;background:var(--off);color:var(--jet);white-space:nowrap}

.own{display:flex;align-items:center;gap:3mm;background:var(--g);border-radius:6px;padding:2.4mm 3mm;margin-bottom:2.5mm}
.own-mk{flex:none;width:8mm;height:8mm;background:var(--nv);color:#fff;font-size:7.6pt;font-weight:700;display:flex;align-items:center;justify-content:center}
.own-n{font-size:10pt;font-weight:700;color:var(--bd);line-height:1.1}
.own-r{font-size:7.4pt;color:var(--mut)}

.cal{width:100%;border-collapse:separate;border-spacing:1.2mm;table-layout:fixed}
.cal th{font-size:6.4pt;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--mut);text-align:left;padding:0 1mm}
.cal td{height:15mm;background:var(--g);border-radius:4px;vertical-align:top;padding:1.4mm 1.6mm}
.cal td.x{background:transparent}
.cal .dn{display:block;font-size:8pt;font-weight:700;color:var(--mut)}
.cal .ft{display:inline-block;margin-top:1.4mm;font-size:6.2pt;font-weight:700;padding:.4mm 1.6mm;border-radius:3px}
.f-car{background:rgba(0,112,254,.14);color:var(--bd)}
.f-vid{background:rgba(240,173,12,.26);color:#6B4A00}
.f-sta{background:rgba(238,140,13,.18);color:#7A4300}
.f-txt{background:rgba(5,46,125,.14);color:var(--bd)}
.cal td.on .dn{color:var(--bd)}
.lg{display:flex;gap:4mm;font-size:7pt;font-weight:600;margin-top:2mm}
.lg span{display:flex;align-items:center;gap:1.4mm}
.lg i{width:3mm;height:3mm;border-radius:1px;display:inline-block}

.pc{background:var(--g);border-radius:6px;padding:3mm;margin-bottom:3.5mm}
.pc-h{display:flex;gap:3mm;align-items:center;margin-bottom:2.2mm}
.pc-h .own-mk{width:9mm;height:9mm}
.pc-h b{font-size:10pt;color:var(--bd);display:block;line-height:1.1}
.pc-h small{font-size:7pt;color:var(--mut);font-family:'Albert Sans',sans-serif}
.pc .tbl td{background:#fff!important}
.pc .tbl td.k{width:26mm}
.sw{display:flex;gap:2.5mm}
.sw div{flex:1;border-radius:6px;overflow:hidden;background:var(--g);font-size:7pt}
.sw i{display:block;height:13mm;background:repeating-linear-gradient(45deg,#E4E6EB 0 4px,#F0F1F4 4px 8px)}
.sw span{display:block;padding:1.6mm 2mm}
.flow{display:grid;grid-template-columns:repeat(5,1fr);gap:2mm}
.flow div{background:var(--g);border-radius:6px;padding:2.6mm}
.flow .num{display:block;font-size:7pt;font-weight:800;color:var(--bc);margin-bottom:.8mm}
.flow b{display:block;font-family:'DM Sans',sans-serif;font-size:8.4pt;color:var(--bd)}
.flow small{display:block;font-size:7pt;color:var(--mut);margin-top:.6mm}
""".replace('TIMB', TIMB)

CSS2 = open(os.path.join(HERE, 'extra.css')).read()

ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg>'


def ph(t):
    return f'<span class="ph">[{t}]</span>'


def P(t):
    """texto com [placeholders] convertidos"""
    import re
    return re.sub(r'\[([^\]]+)\]', lambda m: ph(m.group(1)), t)


def table(heads, rows, cls='', col=None):
    cg = ''
    if col:
        cg = '<colgroup>' + ''.join(f'<col style="width:{w}">' if w else '<col>' for w in col) + '</colgroup>'
    th = ''.join(f'<th{" class=c" if h.startswith("^") else ""}>{h.lstrip("^")}</th>' for h in heads)
    body = []
    for r in rows:
        trc = ''
        if r and r[0] == '__tot__':
            trc = ' class="tot"'; r = r[1:]
        tds = []
        for i, cell in enumerate(r):
            c = ''
            if isinstance(cell, tuple):
                cell, c = cell
            elif i == 0 and 'firstk' in cls:
                c = 'k'
            tds.append(f'<td{" class=" + chr(34) + c + chr(34) if c else ""}>{P(cell)}</td>')
        body.append(f'<tr{trc}>' + ''.join(tds) + '</tr>')
    return f'<table class="tbl">{cg}<thead><tr>{th}</tr></thead><tbody>{"".join(body)}</tbody></table>'


def sec(n, title, inner, sub=''):
    s = f'<div class="sec-s">{P(sub)}</div>' if sub else ''
    return f'<div class="sec"><div class="sec-h"><div class="sec-n">{n:02d}</div><div><h2>{title}</h2>{s}</div></div>{inner}</div>'


def kv(items, cls=''):
    b = ''.join(f'<div class="kvb"><div class="kv-val">{P(v)}</div><span class="kv-lbl">{l}</span><span class="kv-src">{P(s)}</span></div>' for v, l, s in items)
    return f'<div class="kv {cls}">{b}</div>'


def chips(items, neg=False):
    return '<div class="chips">' + ''.join(f'<span class="chip{" neg" if neg else ""}">{P(i)}</span>' for i in items) + '</div>'


def note(body):
    return f'<div class="note">{ICON}<div>{P(body)}</div></div>'


def chk(items):
    return '<ul class="chk">' + ''.join(f'<li><span class="cb"></span><span>{P(i)}</span></li>' for i in items) + '</ul>'


def own(ini, name, role):
    return f'<div class="own"><div class="own-mk">{ini}</div><div><div class="own-n">{name}</div><div class="own-r">{P(role)}</div></div></div>'


def cover(doc, col4, kicker, title, lead, index):
    l1, l2 = title
    idx = ''.join(f'<div><span class="idx-n">{i+1:02d}</span><span class="idx-l">{t}</span></div>' for i, t in enumerate(index))
    return f'''<section class="pg cover">
<div class="band">
<div class="c"><span class="bl">Cliente</span><span class="bv">{ph("Nome completo do cliente")}</span></div>
<div class="c"><span class="bl">Documento</span><span class="bv">{doc}</span></div>
<div class="c"><span class="bl">Período</span><span class="bv">{P(col4[2])}</span></div>
<div class="c"><span class="bl">{col4[0]}</span><span class="bv">{P(col4[1])}</span></div>
</div>
<div class="cv-top"><span class="kick">{P(kicker)}</span><span class="tagline">Menos Vaidade, Mais Resultados</span></div>
<div class="cv-main"><h1>{l1}<b>{l2}</b></h1><div class="rule"></div>
<p class="lead">{P(lead)}</p>
<p class="by">Por Kassio Braga · All.Q Agência · {ph("dd/mm/aaaa")}</p></div>
<div class="idx"><div class="idx-t">Neste documento</div><div class="idx-g">{idx}</div></div>
</section>'''


def page(label, n, total, inner, sub=''):
    return f'''<section class="pg">
<div class="idb"><span class="l">{label} · {ph("Cliente")}</span><span class="r">{sub}<b>Pág. {n:02d} / {total:02d}</b></span></div>
<div class="body"><div class="fill">{inner}</div></div>
</section>'''


GEM_NOTE = '''<!-- MODELO OFICIAL ALL.Q · não altere o <head>. Copie a linha do CSS exatamente como está.
Escreva só dentro de <body>, usando apenas as classes deste arquivo. Não crie <style>. -->
'''


def doc(title, pages):
    if CSS_URL:
        HEADCSS = f'<link href="{CSS_URL}" rel="stylesheet">'
        note = GEM_NOTE
    else:
        HEADCSS = f'<style>{CSS}{CSS2}</style>'
        note = ''
    return f'''<!DOCTYPE html>
<html lang="pt-BR"><head>{note}<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{FONTS}" rel="stylesheet">
{HEADCSS}</head>
<body>
{"".join(pages)}
</body></html>'''


def write_css(path):
    """CSS único dos templates, publicado em allq.com.br para a versão do Gem."""
    open(path, 'w').write('/* All.Q · Templates de Planejamento · gerado por gerador/base.py, não editar */\n' + CSS + CSS2)


def build(fname, title, cov, inner_pages, label):
    total = len(inner_pages) + 1
    pages = [cov]
    for i, p in enumerate(inner_pages):
        sub = ''
        if isinstance(p, tuple):
            sub, p = p
        pages.append(page(label, i + 2, total, p, sub))
    out = os.path.join(HERE, '..', OUTDIR, fname)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w').write(doc(title, pages))
    return out


# ---------- departamentos (cores e icones do Notion All.Q Departamentos) ----------
_SV = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">{}</svg>'
DEPT = {
    'adm': ('Administrativo', '#9F6B53', '<path d="M6 22V4a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v18Z"/><path d="M6 12H4a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h2"/><path d="M18 9h2a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2h-2"/><path d="M10 6h4M10 10h4M10 14h4M10 18h4"/>'),
    'cs': ('Sucesso do Cliente', '#CB912F', '<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>'),
    'dev': ('Desenvolvimento', '#D44C47', '<rect width="18" height="18" x="3" y="3" rx="2"/><path d="m7 11 2-2-2-2"/><path d="M11 13h4"/>'),
    'tp': ('Tráfego Pago', '#337EA9', '<rect width="20" height="14" x="2" y="7" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>'),
    'cri': ('Criativos', '#C14C8A', '<path d="M7 10v12"/><path d="M15 5.88 14 10h5.83a2 2 0 0 1 1.92 2.56l-2.33 8A2 2 0 0 1 17.5 22H4a2 2 0 0 1-2-2v-8a2 2 0 0 1 2-2h2.76a2 2 0 0 0 1.79-1.11L12 2a3.13 3.13 0 0 1 3 3.88Z"/>'),
    'org': ('Tráfego Orgânico', '#448361', '<path d="M3 6h11M3 12h7M3 18h4"/><path d="m14 19 7-7-2.5-2.5-7 7V19Z"/>'),
    'des': ('Design', '#9065B0', '<circle cx="13.5" cy="6.5" r="1"/><circle cx="17.5" cy="10.5" r="1"/><circle cx="8.5" cy="7.5" r="1"/><circle cx="6.5" cy="12.5" r="1"/><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10c.9 0 1.6-.7 1.6-1.7 0-.4-.2-.8-.4-1.1-.3-.3-.4-.7-.4-1.1a1.6 1.6 0 0 1 1.7-1.7h2c3 0 5.5-2.5 5.5-5.5C22 6 17.5 2 12 2z"/>'),
}


def dp(k, label=None):
    n, c, i = DEPT[k]
    return f'<span class="dp" style="--dc:{c}"><i>{_SV.format(i)}</i>{label or n}</span>'


def own(k, role):
    n, c, i = DEPT[k]
    return f'<div class="own"><div class="own-mk" style="background:{c}">{_SV.format(i)}</div><div><div class="own-n">{n}</div><div class="own-r">{P(role)}</div></div></div>'


_P0 = P
def P(t):
    import re
    t = _P0(t)
    return re.sub(r'@(adm|cs|dev|tp|cri|org|des)\b', lambda m: dp(m.group(1)), t)
