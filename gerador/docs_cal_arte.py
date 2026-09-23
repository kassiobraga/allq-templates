from base import *

# ---------- formatos ----------
FMT = {
    'sta': ('Estático', 'f-sta'), 'car': ('Carrossel', 'f-car'), 'vid': ('Reels', 'f-vid'),
    'lng': ('Vídeo', 'f-lng'), 'sto': ('Stories', 'f-sto'), 'txt': ('Texto', 'f-txt'),
}
ORDER = ['sta', 'car', 'vid', 'lng', 'sto', 'txt']
NETS = {'sta': 'IG · FB · GMN', 'car': 'IG · LI · FB', 'vid': 'IG · TT · YT', 'lng': 'YT · LI', 'sto': 'IG · FB', 'txt': 'LI'}
# semana modelo: 4 posts de feed + 1 stories + 1 texto; 1 video no mes
WEEKS = [
    [['car'], ['sto'], ['vid'], [], ['car', 'txt'], ['sta'], []],
    [['car'], ['vid'], ['lng'], ['car', 'sto'], ['sta', 'txt'], [], []],
    [[], ['car', 'sto'], [], ['vid'], ['txt'], ['car'], ['sta']],
    [['car'], ['sto'], ['vid'], [], ['car', 'txt'], ['sta'], []],
    [[], [], [], [], [], [], []],
]
TINT = {'sta': 'rgba(0,112,254,.26)', 'car': 'rgba(124,58,237,.26)', 'vid': 'rgba(238,140,13,.36)', 'lng': 'rgba(220,38,38,.24)', 'sto': 'rgba(236,72,153,.28)', 'txt': 'rgba(26,127,85,.26)'}
DIAS = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom']


def pilar(f, n):
    return {'car': 'Quebra de crença' if n % 2 == 0 else 'Educação', 'vid': 'Bastidor', 'sta': 'Diagnóstico',
            'sto': 'Relacionamento', 'txt': 'Autoridade', 'lng': 'Educação'}[f]


def month_posts():
    out, d, cc = [], 1, 0
    for w in WEEKS:
        for i, fs in enumerate(w):
            if d > 31:
                break
            for f in fs:
                out.append((d, DIAS[i], f, pilar(f, cc)))
                if f == 'car':
                    cc += 1
            d += 1
    return out


def count(posts):
    c = {k: 0 for k in ORDER}
    for p in posts:
        c[p[2]] += 1
    return c


def fmt_chip(f):
    return f'<span class="fmt {FMT[f][1]}">{FMT[f][0]}</span>'


def grade(posts, start=1, mm='[mm]'):
    h = ['#', 'Data', 'Dia', 'Formato', 'Pilar', 'Tema / título', 'Redes', 'Status']
    w = ['7mm', '16mm', '9mm', '19mm', '26mm', None, '21mm', '14mm']
    th = ''.join(f'<th>{x}</th>' for x in h)
    cg = ''.join(f'<col style="width:{x}">' if x else '<col>' for x in w)
    rows = ''
    for i, (d, dia, f, pil) in enumerate(posts):
        rows += (f'<tr class="r-{f}"><td class="k">{start + i:02d}</td><td>{d:02d}/{P(mm)}</td><td>{dia}</td><td>{fmt_chip(f)}</td>'
                 f'<td>{pil}</td><td>{ph("Tema do post")}</td><td>{NETS[f]}</td><td><span class="st">Pauta</span></td></tr>')
    return f'<table class="tbl g"><colgroup>{cg}</colgroup><thead><tr>{th}</tr></thead><tbody>{rows}</tbody></table>'


LEG = ('<div class="lg" style="flex-wrap:wrap">' + ''.join(f'<span><i class="{FMT[k][1]}"></i>{FMT[k][0]}</span>' for k in ORDER) +
       '<span><i style="background:var(--g);border:1px solid var(--brd)"></i>Sem publicação</span></div>')


def big_cal():
    rows, d = '', 1
    for w in WEEKS:
        rows += '<tr>'
        for fs in w:
            if d > 31:
                rows += '<td class="x"></td>'; continue
            chips = ''.join(f'<span class="ft {FMT[f][1]}">{FMT[f][0]}</span>' for f in fs)
            rows += f'<td class="{"on" if fs else ""}"><span class="dn">{d:02d}</span>{chips}</td>'
            d += 1
        rows += '</tr>'
    return '<table class="cal"><thead><tr>' + ''.join(f'<th>{x}</th>' for x in DIAS) + f'</tr></thead><tbody>{rows}</tbody></table>' + LEG


def mini_cal(title, n):
    rows, d = '', 1
    for w in WEEKS:
        rows += '<tr>'
        for fs in w:
            if d > 31:
                rows += '<td class="x"></td>'; continue
            cls = FMT[fs[0]][1] if fs else ''
            dots = ''
            if len(fs) > 1:
                cls = 'spl'
                dots = ''
                split = f'background:linear-gradient(135deg,{TINT[fs[0]]} 50%,{TINT[fs[1]]} 50%)'
            st = f' style="{split}"' if len(fs) > 1 else ''
            rows += f'<td class="{cls}"{st}>{d}</td>'; d += 1
        rows += '</tr>'
    return (f'<div class="mcal"><div class="mcal-t">{P(title)}<small>{n} peças</small></div><table class="mc"><thead><tr>'
            + ''.join(f'<th>{x[0]}</th>' for x in DIAS) + f'</tr></thead><tbody>{rows}</tbody></table></div>')


def formatos(c, mult=1):
    rows = [
        ('sta', 'Imagem única com título e sub', '1080 × 1350'),
        ('car', 'Sequência de 6 lâminas: capa, 4 de conteúdo e último com CTA', '1080 × 1350'),
        ('vid', 'Vídeo vertical curto, 30 a 45 s, legenda na tela', '1080 × 1920'),
        ('lng', 'Vídeo horizontal longo, 3 a 10 min, com capa', '1920 × 1080'),
        ('sto', 'Sequência de 3 a 5 telas, enquete, caixa de pergunta, link', '1080 × 1920'),
        ('txt', 'Post só texto no LinkedIn, imagem opcional', 'Sem arte'),
    ]
    body = ''.join(f'<tr class="r-{k}"><td>{fmt_chip(k)}</td><td>{d}</td><td>{NETS[k]}</td><td>{s}</td><td class="c">{ph(str(c[k] * mult))}</td></tr>' for k, d, s in rows)
    return ('<table class="tbl"><colgroup><col style="width:22mm"><col><col style="width:24mm"><col style="width:22mm"><col style="width:16mm"></colgroup>'
            '<thead><tr><th>Formato</th><th>O que é</th><th>Redes</th><th>Dimensão</th><th class="c">Qtd.</th></tr></thead>'
            f'<tbody>{body}<tr class="tot"><td>Total</td><td></td><td></td><td></td><td class="c">{ph(str(sum(c.values()) * mult))}</td></tr></tbody></table>')


PILARES = table(['Pilar', 'Objetivo', 'Formato preferencial'], [
    ['Quebra de crença', '[Contrariar um senso comum do setor]', 'Carrossel'],
    ['Educação', '[Ensinar algo que o cliente final usa]', 'Carrossel, Vídeo'],
    ['Bastidor', '[Mostrar como a empresa trabalha]', 'Reels'],
    ['Diagnóstico', '[Pergunta que gera identificação]', 'Estático'],
    ['Relacionamento', '[Conversa diária, enquete, caixa de pergunta]', 'Stories'],
    ['Autoridade', '[Opinião do porta-voz sobre o mercado]', 'Texto']], 'firstk', ['30mm', None, '34mm'])

FLUXO = '<div class="flow">' + ''.join(
    f'<div><span class="num">{i+1:02d}</span><b>{a}</b><small>{P(b)}</small></div>' for i, (a, b) in enumerate([
        ('Copy', '@org<br>até dia [10]'), ('Arte', '@cri<br>até dia [15]'), ('Revisão', '@adm<br>até dia [17]'),
        ('Cliente', '@cs<br>resposta em [48h]'), ('Agendamento', '@cs<br>até dia [25]')])) + '</div>'

DATAS = table(['Data', 'Ocasião', 'Uso no calendário'], [
    ['[dd/mm]', '[Data comemorativa do setor]', '[Substitui o post do dia ou entra extra]'],
    ['[dd/mm]', '[Evento do cliente]', '[Cobertura em stories]'],
    ['[dd/mm]', '[Feriado]', '[Sem publicação]']], 'firstk', ['20mm', None, None])

REGRA = note('<b>Regra de mudança:</b> post aprovado só muda de data com aviso do Sucesso do Cliente ao time e ao cliente.')


# ============ CALENDARIO MENSAL ============
def calendario():
    posts = month_posts(); c = count(posts); n = len(posts)
    cov = cover('Calendário Editorial', ('Cadência', f'[{n} peças no mês]', '[Mês] de [Ano]'),
                '[Cliente] · [Grupo]', ('Calendário', 'Editorial'),
                '[Uma frase com o tema do mês e o que o conteúdo precisa gerar: autoridade, lead ou relacionamento.]',
                ['Visão do mês', 'Formatos e pilares', 'Grade de posts', 'Fluxo de aprovação', 'Datas relevantes'])
    p2 = sec(1, 'Visão do mês', big_cal(), 'Grade base: mês iniciando na segunda. Ajustar os dias ao mês real.') + \
        sec(2, 'Formatos do mês', formatos(c))
    p3 = sec(3, 'Pilares', PILARES) + sec(4, 'Fluxo de aprovação', FLUXO) + sec(5, 'Datas relevantes', DATAS) + REGRA
    p4 = sec(6, 'Grade de posts', grade(posts), 'A cor da linha é a mesma do formato no calendário. Copy completa fica no Notion/Drive.')
    return build('Template - Calendário Editorial.html', 'Template - Calendário Editorial', cov, [p2, p3, p4], 'Calendário Editorial')


# ============ CALENDARIO TRIMESTRAL ============
def calendario_tri():
    posts = month_posts(); c = count(posts); n = len(posts)
    cov = cover('Calendário Editorial Trimestral', ('Cadência', f'[{n} peças por mês · {n*3} no trimestre]', '[Mês] a [Mês] de [Ano]'),
                '[Cliente] · [Grupo]', ('Calendário Editorial', 'Trimestral'),
                '[Uma frase com o tema do trimestre e o que cada mês precisa construir até o resultado final.]',
                ['Visão do trimestre', 'Grade do mês 1', 'Grade do mês 2', 'Grade do mês 3', 'Fluxo e datas'])
    temas = table(['Mês', 'Tema do mês', 'Objetivo', 'Destaque'], [
        ['[Mês 1]', '[Tema]', '[Autoridade / lead / relacionamento]', '[Data ou campanha do mês]'],
        ['[Mês 2]', '[Tema]', '[Objetivo]', '[Destaque]'],
        ['[Mês 3]', '[Tema]', '[Objetivo]', '[Destaque]']], 'firstk', ['18mm', None, None, None])
    p2 = sec(1, 'Visão do trimestre', '<div class="mcals">' + ''.join(mini_cal(f'[Mês {i}]', n) for i in (1, 2, 3)) + '</div>' + LEG,
             'Dia com duas peças aparece dividido na diagonal, uma cor para cada formato.') + \
        sec(2, 'Tema de cada mês', temas) + sec(3, 'Formatos do trimestre', formatos(c, 3))
    pg = [(f'Mês {i+1}', sec(4 + i, f'Grade de posts · {ph(f"Mês {i+1}")}', grade(posts, 1 + n * i),
                             'A cor da linha é a mesma do formato no calendário. Copy completa fica no Notion/Drive.')) for i in range(3)]
    p6 = sec(7, 'Pilares', PILARES) + sec(8, 'Fluxo de aprovação', FLUXO, 'Repete todo mês. Aprovação do mês seguinte fecha até o dia [25].') + \
        sec(9, 'Datas relevantes do trimestre', DATAS) + REGRA
    return build('Template - Calendário Editorial Trimestral.html', 'Template - Calendário Editorial Trimestral', cov,
                 [('Visão geral', p2)] + pg + [('Fluxo', p6)], 'Calendário Editorial')


# ============ FICHA DE PECA ============
NETMAP = {'ig': 'Instagram', 'li': 'LinkedIn', 'fb': 'Facebook', 'tt': 'TikTok', 'yt': 'YouTube', 'gmn': 'Google Meu Negócio', 'meta': 'Meta Ads', 'gads': 'Google Ads'}


def ficha(lbl, code, f, pills, nets, body, nota, day=True, tpl=True):
    left = (f'<div class="pc">{lbl}</div>' +
            (f'<div class="pd">{ph("DIA")}</div><div class="pdt">{code}</div><div class="pm">{ph("mês")}</div>' if day
             else f'<div class="pdt" style="margin-top:2mm;font-size:15pt">{code}</div>') +
            (f'<span class="fmt {FMT[f][1]}">{FMT[f][0]}</span>' if f in FMT else '<span class="fmt f-lng">Anúncio</span>') +
            f'<div class="due">Arte até<b>{ph("dd/mm")}</b></div>')
    meta = ''.join(f'<span class="pill">{P(p)}</span>' for p in pills) + ''.join(f'<span class="np np-{x}">{NETMAP[x]}</span>' for x in nets)
    notas = '<br>'.join(f'<b>{k}:</b> {P(v)}' for k, v in nota)
    t = f'<span class="sp"></span><span class="tpl">Template <b>{ph("nome")}</b></span>' if tpl else ''
    return (f'<div class="post"><div class="pl">{left}</div><div class="pb"><div class="pmeta">{meta}{t}</div>'
            f'{body}<div class="nota">{notas}</div></div></div>')


def tsg(items, cls=''):
    return f'<div class="tsg {cls}">' + ''.join(
        f'<div><span class="fl">{k}</span><div class="{"f-t" if big else "f-s"}">{P(v)}</div></div>' for k, v, big in items) + '</div>'


def laminas(n=6):
    out = []
    for i in range(n):
        lb = 'CAPA' if i == 0 else ('ÚLTIMO' if i == n - 1 else f'LÂMINA {i+1}')
        t = '[Título da capa]' if i == 0 else ('[CTA]' if i == n - 1 else '[Título]')
        out.append(f'<div class="sl"><div class="sl-n{" hl" if i in (0, n - 1) else ""}">{lb}</div><div class="sl-t">{P(t)}</div><div class="sl-s">{P("[Sub de apoio]")}</div></div>')
    return '<span class="fl">Lâminas · título e sub</span><div class="sls">' + ''.join(out) + '</div>'


def legenda(tags='#[Hashtag1] #[Hashtag2] #[MarcaDoCliente]'):
    return (f'<span class="fl">Legenda</span><div class="lgd"><p>{P("[Legenda completa do post, com quebra de parágrafo a cada 1 ou 2 frases.]")}</p>'
            f'<p>{P("[Chamada para ação da legenda.]")}</p><p class="ht">{P(tags)}</p></div>')


def diretrizes(extra_specs):
    sw = '<div class="sw">' + ''.join(f'<div><i></i><span><b>{a}</b><br>{ph("#HEX")}</span></div>' for a in ['Primária', 'Secundária', 'Apoio', 'Texto']) + '</div>'
    return sec(1, 'Diretrizes do cliente', sw + '<div style="height:3mm"></div>' + table(['Item', 'Definição'], [
        ['Fontes', '[Título: fonte e peso] · [Corpo: fonte]'],
        ['Logo', '[Versão para fundo claro e escuro, link do arquivo]'],
        ['Estilo', '[Ex: flat, fotos reais da operação, fundo claro]'],
        ['Imagens', '[Banco próprio do cliente, link da pasta]'],
        ['Templates', '[Link dos templates aprovados]']], 'firstk', ['24mm', None]),
        'Cor e fonte do cliente valem nas peças dele, nunca nos documentos da All.Q.') + \
        '<div class="two">' + sec(2, 'Faça', chk(['[Foto real da operação do cliente]', '[Título com no máximo 8 palavras]', '[Logo em toda peça]', '[Contraste AA em todo texto]'])) + \
        sec(3, 'Evite', chk(['[Banco de imagem genérico]', '[Mais de 2 fontes na peça]', '[Termos proibidos do cliente]', '[Emoji como ícone]'])) + '</div>' + \
        sec(4, 'Especificações', table(['Formato', 'Dimensão', 'Área segura', 'Exportar'], extra_specs, 'firstk'))


# ============ DIRECAO DE ARTE · REDES SOCIAIS ============
def arte():
    cov = cover('Direção de Arte · Redes Sociais', ('Departamento', 'Criativos', '[Mês] de [Ano]'),
                '[Cliente] · Documento interno', ('Direção de Arte', 'Redes Sociais'),
                '[Uma frase com o conceito visual do mês e o que as peças precisam transmitir.]',
                ['Diretrizes do cliente', 'Especificações', 'Peças do mês', 'Entrega de arquivos', 'Checklist'])
    p2 = diretrizes([
        [fmt_chip('sta'), '1080 × 1350 px', '[60 px nas bordas]', 'PNG'],
        [fmt_chip('car'), '1080 × 1350 px', '[60 px nas bordas]', 'PNG por lâmina + PDF LinkedIn'],
        [fmt_chip('vid'), '1080 × 1920 px', 'Livre 250 px topo e base', 'MP4 + capa PNG'],
        [fmt_chip('lng'), '1920 × 1080 px', '[Título fora do canto inferior direito]', 'MP4 + thumbnail 1280 × 720'],
        [fmt_chip('sto'), '1080 × 1920 px', 'Livre 250 px topo e base', 'PNG / MP4 por tela']])
    car = ficha('PEÇA 01', ph('01'), 'car', ['[Pilar]'], ['ig', 'li'], laminas() + legenda(),
                [('Imagem', '[Uma ideia por lâmina, ícone linear, linha de progresso no rodapé. Fundo claro.]'), ('Publicação', '[Redes e observação de publicação]')])
    vid = ficha('PEÇA 02', ph('03'), 'vid', ['[Pilar]'], ['ig', 'tt', 'yt'],
                tsg([('Gancho · 0 a 2 s', '[Texto do gancho]', False), ('Texto na tela', '[Frases que entram como legenda]', False),
                     ('Capa', '[Título da capa]', False)], 't3') + legenda(),
                [('Material', '[Link do vídeo bruto]'), ('Edição', '[30 a 45 s, cortes rápidos, legenda fora do terço inferior]')])
    est = ficha('PEÇA 03', ph('06'), 'sta', ['[Pilar]'], ['ig', 'fb'],
                tsg([('Título', '[Título da peça]', True), ('Sub', '[Linha de apoio]', False)]) + legenda(),
                [('Imagem', '[Tipografia grande, fundo claro, composição centrada]'), ('Publicação', '[Redes]')])
    sto = ficha('PEÇA 04', ph('02'), 'sto', ['Relacionamento'], ['ig', 'fb'],
                tsg([('Tela 1', '[Gancho]', False), ('Tela 2', '[Conteúdo ou enquete]', False), ('Tela 3', '[CTA, link ou caixa de pergunta]', False)], 't3'),
                [('Interação', '[Enquete, caixa de pergunta ou link]'), ('Imagem', '[Foto real ou fundo da paleta, texto no centro]')])
    lng = ficha('PEÇA 05', ph('10'), 'lng', ['Educação'], ['yt', 'li'],
                tsg([('Título do vídeo', '[Título para o YouTube]', True), ('Thumbnail', '[Texto curto da thumb, até 4 palavras]', False)]) + legenda('#[Hashtag1] #[MarcaDoCliente]'),
                [('Material', '[Link do vídeo bruto]'), ('Edição', '[Vinheta de abertura, lower third com nome e cargo, tela final]')])
    p3 = sec(5, 'Peças do mês', car + vid, 'Uma ficha por peça, na ordem do Calendário Editorial. Texto de LinkedIn não tem ficha: não leva arte.')
    p4 = est + sto + lng + note('<b>Para montar o mês:</b> duplicar as fichas até cobrir todas as peças com arte do calendário, na mesma ordem e com o mesmo número.')
    p5 = sec(6, 'Entrega de arquivos', table(['Item', 'Padrão'], [
        ['Pasta', '[Drive / Cliente / Artes / AAAA-MM]'],
        ['Nomenclatura', 'P01_carrossel_ddmm_v1 · versões v2, v3 após ajuste'],
        ['Editável', '[Link do arquivo no Figma / Affinity / Canva]'],
        ['Carrossel', 'Um PNG por lâmina, numerados 01 a 06, e PDF único para LinkedIn'],
        ['Vídeo', 'MP4 H.264 · Reels e Stories 1080 × 1920 · Vídeo 1920 × 1080'],
        ['Aviso', 'Mover o card no Notion para Revisão e marcar o @cs']], 'firstk', ['26mm', None])) + \
        sec(7, 'Prazos', table(['Etapa', 'Até', 'Departamento'], [
            ['Copy recebida', 'Dia [10]', '@org'], ['Artes semana 1 e 2', 'Dia [13]', '@cri'],
            ['Artes semana 3 e 4', 'Dia [15]', '@cri'], ['Revisão interna', 'Dia [17]', '@adm'],
            ['Ajustes do cliente', '24h após retorno', '@cri']], 'firstk')) + \
        sec(8, 'Checklist antes de entregar', chk(['Texto revisado contra a copy aprovada, sem erro de digitação', 'Cores e fontes do cliente, nada fora da paleta dele',
                                                  'Logo aplicada na versão certa para o fundo', 'Texto dentro da área segura do formato',
                                                  'Contraste legível no celular', 'Arquivo nomeado no padrão e salvo na pasta do mês',
                                                  'Nenhum termo proibido ou marca vetada pelo cliente']))
    return build('Template - Direção de Arte Redes Sociais.html', 'Template - Direção de Arte Redes Sociais', cov, [p2, p3, p4, p5], 'Direção de Arte · Redes Sociais')


# ============ DIRECAO DE ARTE · ANUNCIOS ============
def anuncio(code, camp, nets, fmts):
    body = (tsg([('Texto na arte', '[Título curto da oferta]', True), ('Sub', '[Prova ou benefício]', False)]) +
            tsg([('Botão / CTA', '[Saiba mais / Cadastre-se]', False), ('Variações', '[3 versões de título, mesma base]', False),
                 ('Formatos', fmts, False)], 't3') +
            '<span class="fl">Copy do anúncio · referência</span><div class="lgd">' +
            f'<p><b>Texto principal:</b> {ph("Texto que acompanha a arte na plataforma")}</p><p><b>Título:</b> {ph("Título do anúncio")}</p></div>')
    return ficha('ANÚNCIO', code, 'ads', [camp], nets, body,
                 [('Direção', '[Imagem real do produto ou operação, oferta legível no celular]'),
                  ('Destino', '[URL da landing page, a arte precisa bater com a promessa dela]')], day=False)


def anuncios():
    cov = cover('Direção de Arte · Anúncios', ('Departamento', 'Criativos', '[Mês] de [Ano]'),
                '[Cliente] · Documento interno · pedido do Tráfego Pago', ('Direção de Arte', 'Anúncios'),
                '[Uma frase com a campanha, a oferta e o que o criativo precisa fazer o público sentir para clicar.]',
                ['Pedido de criativos', 'Especificações', 'Fichas dos anúncios', 'Entrega de arquivos', 'Checklist'])
    p2 = own('tp', 'Pede os criativos e define campanha, oferta e prazo de subida') + \
        sec(1, 'Pedido de criativos', table(['Código', 'Campanha', 'Plataforma', 'Formatos', 'Arte até', 'Sobe em'], [
            ['A01', '[Cadastro · público frio]', 'Meta Ads', '1080 × 1350 · 1080 × 1920', '[dd/mm]', '[dd/mm]'],
            ['A02', '[Remarketing]', 'Meta, Google Display', '1080 × 1080 · 1200 × 628', '[dd/mm]', '[dd/mm]'],
            ['A03', '[Decisores]', 'LinkedIn Ads', '1200 × 1200', '[dd/mm]', '[dd/mm]']], 'firstk', ['14mm', None, '26mm', '38mm', '16mm', '16mm'])) + \
        sec(2, 'Especificações', table(['Plataforma', 'Formato', 'Dimensão', 'Regra'], [
            ['Meta Ads', 'Feed', '1080 × 1350', 'Texto em até 20% da área'],
            ['Meta Ads', 'Stories e Reels', '1080 × 1920', 'Livre 250 px topo e base'],
            ['Google Display', 'Paisagem e quadrado', '1200 × 628 · 1200 × 1200', 'Logo 1200 × 1200 e 1200 × 300 à parte'],
            ['Google PMax', 'Grupo de recursos', 'Paisagem, quadrado e retrato 960 × 1200', 'Até 20 imagens, sem texto sobreposto'],
            ['LinkedIn Ads', 'Imagem única', '1200 × 1200', 'Título na arte com até 6 palavras']], 'firstk', ['26mm', '28mm', None, None])) + \
        sec(3, 'Regras de anúncio', chk(['A oferta da arte é a mesma da landing page de destino', 'Logo do cliente visível, sem competir com a oferta',
                                        'Um único CTA por peça', 'Legível no celular sem zoom', '[Termos proibidos e marcas vetadas pelo cliente]']))
    p3 = sec(4, 'Fichas dos anúncios', anuncio('A01', '[Campanha]', ['meta'], '1080 × 1350 · 1080 × 1920') +
             anuncio('A02', '[Remarketing]', ['meta', 'gads'], '1080 × 1080 · 1200 × 628'),
             'Um código por conjunto de criativos. Variações do mesmo anúncio ficam na mesma ficha.')
    p4 = anuncio('A03', '[Decisores]', ['li'], '1200 × 1200') + \
        note('<b>Para montar o pedido:</b> duplicar as fichas até cobrir todos os códigos da tabela de pedido, na mesma ordem.') + '<div style="height:5mm"></div>' + \
        sec(5, 'Entrega de arquivos', table(['Item', 'Padrão'], [
            ['Pasta', '[Drive / Cliente / Anúncios / AAAA-MM]'],
            ['Nomenclatura', 'A01_meta_1080x1350_v1 · A01_meta_1080x1920_v1'],
            ['Variações', 'Letra no fim: A01a, A01b, A01c'],
            ['Editável', '[Link do arquivo]'],
            ['Aviso', 'Mover o card no Notion para Revisão e marcar o @tp']], 'firstk', ['26mm', None]))
    p5 = sec(6, 'Prazos', table(['Etapa', 'Até', 'Departamento'], [
            ['Pedido com oferta e destino', '[5 dias úteis antes da subida]', '@tp'], ['Criativos', '[3 dias úteis antes da subida]', '@cri'],
            ['Revisão interna', '[2 dias úteis antes]', '@adm'], ['Aprovação do cliente', '[1 dia útil antes]', '@cs']], 'firstk')) + \
        sec(7, 'Checklist antes de entregar', chk(['Todos os formatos pedidos exportados, nenhum faltando', 'Texto revisado, sem erro de digitação',
                                                   'Oferta igual à da landing page', 'Texto dentro da área segura de cada formato',
                                                   'Arquivos nomeados com código, plataforma e dimensão', 'Nenhum termo proibido ou marca vetada pelo cliente'])) + \
        sec(8, 'Retorno de performance', table(['Código', 'CTR', 'CPL', 'Decisão'], [
            ['A01', '[0,0%]', 'R$ [00]', '[Manter / trocar / pausar]'], ['A02', '[0,0%]', 'R$ [00]', '[Decisão]'], ['A03', '[0,0%]', 'R$ [00]', '[Decisão]']], 'firstk'),
            'Preenchido pelo Tráfego Pago após 7 dias no ar. Orienta a próxima leva de criativos.') + \
        note('<b>Troca de criativo:</b> quando a frequência passa de [3] ou o CTR cai [30%] em relação à primeira semana, o Tráfego Pago abre novo pedido.')
    return build('Template - Direção de Arte Anúncios.html', 'Template - Direção de Arte Anúncios', cov, [p2, p3, p4, p5], 'Direção de Arte · Anúncios')


# ============ wireframe da LP ============
def L(cls='', w=100):
    return f'<span class="wl {cls}" style="width:{w}%"></span>'


def wireframe():
    btn = '<span class="wbtn"></span>'
    form = lambda n: '<div class="wbox" style="padding:2mm">' + ''.join(f'<div class="wbox" style="height:3.4mm;background:#fff;margin-bottom:1.2mm"></div>' for _ in range(n)) + '<span class="wbtn" style="width:100%;margin-top:.4mm"></span></div>'
    cards = lambda n, cols, h: f'<div class="wg" style="grid-template-columns:repeat({cols},1fr)">' + ''.join(
        f'<div class="wbox" style="padding:1.6mm;height:{h}mm"><div class="wimg" style="width:4mm;height:4mm"></div>{L("s",80)}{L("",95)}{L("",70)}</div>' for _ in range(n)) + '</div>'
    d = [
        ('01', '<div class="wt">Logo · sem menu</div><div class="wg" style="grid-template-columns:1.25fr 1fr;align-items:center">'
               f'<div>{L("t",92)}{L("t",70)}<div style="height:1.4mm"></div>{L("s",88)}{L("s",75)}{btn}</div>{form(3)}</div>', ''),
        ('02', '<div class="wt">Prova · logos e números</div><div class="wg" style="grid-template-columns:repeat(6,1fr)">' +
               ''.join('<div class="wimg" style="height:5mm"></div>' for _ in range(6)) + '</div>', 'dk'),
        ('03', f'<div class="wt">Dor</div>{L("t",55)}<div style="height:1.6mm"></div>{cards(3, 3, 10.5)}', ''),
        ('04', f'<div class="wt">Solução · benefícios</div>{L("t",60)}<div style="height:1.6mm"></div>{cards(6, 3, 9)}', ''),
        ('05', '<div class="wt">Como funciona · 3 passos</div><div class="wg" style="grid-template-columns:repeat(3,1fr)">' +
               ''.join(f'<div><div style="width:5mm;height:5mm;border-radius:50%;background:var(--bd);opacity:.35"></div>{L("s",70)}{L("",90)}</div>' for _ in range(3)) + '</div>', 'dk'),
        ('06', '<div class="wt">Depoimentos</div><div class="wg" style="grid-template-columns:1fr 1fr">' +
               ''.join(f'<div class="wbox" style="padding:1.8mm;display:flex;gap:2mm"><div class="wimg" style="flex:none;width:7mm;height:7mm;border-radius:50%"></div><div style="flex:1">{L("",95)}{L("",80)}{L("s",45)}</div></div>' for _ in range(2)) + '</div>', ''),
        ('07', '<div class="wt">FAQ · 5 perguntas</div>' + ''.join('<div class="wbox" style="height:3.6mm;margin-bottom:1mm"></div>' for _ in range(3)), ''),
        ('08', f'<div class="wt">CTA final</div><div class="wg" style="grid-template-columns:1.25fr 1fr;align-items:center"><div>{L("t",85)}{L("s",70)}</div>{form(2)}</div>', 'dk'),
        ('09', f'<div class="wt">Rodapé</div>{L("",40)}{L("",30)}', ''),
    ]
    desk = '<div><div class="wf-cap">Desktop · 1440 px</div><div class="wf">' + ''.join(f'<div class="wb {c}"><span class="wn">{n}</span>{b}</div>' for n, b, c in d) + '</div></div>'
    m = [
        ('01', f'{L("t",95)}{L("t",70)}{L("s",90)}{form(3)}', ''),
        ('02', '<div class="wg" style="grid-template-columns:repeat(3,1fr)">' + ''.join('<div class="wimg" style="height:4mm"></div>' for _ in range(6)) + '</div>', 'dk'),
        ('03', f'{L("t",80)}' + ''.join(f'<div class="wbox" style="height:5mm;margin-top:1.2mm"></div>' for _ in range(3)), ''),
        ('04', f'{L("t",80)}<div class="wg" style="grid-template-columns:1fr 1fr;margin-top:1.2mm">' + ''.join('<div class="wbox" style="height:6mm"></div>' for _ in range(4)) + '</div>', ''),
        ('05', ''.join(f'{L("s",60)}{L("",90)}' for _ in range(3)), 'dk'),
        ('06', '<div class="wbox" style="height:9mm"></div><div class="wt" style="margin-top:1mm">Arrastar para o lado</div>', ''),
        ('07', ''.join('<div class="wbox" style="height:3.2mm;margin-bottom:1mm"></div>' for _ in range(3)), ''),
        ('08', f'{L("t",85)}{form(2)}', 'dk'),
        ('09', f'{L("",60)}', ''),
    ]
    mob = '<div><div class="wf-cap">Mobile · 360 px</div><div class="wf m">' + ''.join(f'<div class="wb {c}"><span class="wn">{n}</span>{b}</div>' for n, b, c in m) + '</div></div>'
    return f'<div class="wfw">{desk}{mob}</div>'
