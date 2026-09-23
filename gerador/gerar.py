import os
from base import *

B = ('<i></i>', 'bar')
Y = ('<i class="y"></i>', 'bar')
E = ('', 'bar')

# ============ 1. PLANEJAMENTO SEMESTRAL ============
def semestral():
    cov = cover('Planejamento Semestral', ('Objetivo do semestre', '[Objetivo central em até 6 palavras]', '[Mês] a [Mês] de [Ano]'),
                '[Cliente] · [Grupo]', ('Planejamento de', 'Marketing Semestral'),
                '[Uma frase dizendo o que este semestre precisa entregar para o negócio do cliente, com o indicador principal.]',
                ['Ponto de partida', 'Objetivos e metas', 'Departamentos', 'Roadmap do semestre', 'Verba e governança'])
    p2 = sec(1, 'Ponto de partida', kv([
        ('[000]', 'Leads / mês', '[Fonte] · [período]'),
        ('R$ [00]', 'Custo por lead', '[Fonte] · [período]'),
        ('[0.000]', 'Sessões orgânicas', 'GA4 · [período]'),
        ('[0,0%]', 'Conversão da LP', 'GA4 · [período]'),
        ('[00]', 'Oportunidades / mês', 'CRM · [período]')]), 'Números de base que as metas usam como referência.') + \
        sec(2, 'Diagnóstico por frente', table(['Frente', 'Situação hoje', 'Problema principal', 'Oportunidade'], [
            ['Tráfego pago', '[Canais ativos, verba atual]', '[O que trava resultado]', '[Onde ganhar]'],
            ['SEO e blog', '[Posição, volume de artigos]', '[O que trava resultado]', '[Onde ganhar]'],
            ['Redes sociais', '[Frequência, alcance]', '[O que trava resultado]', '[Onde ganhar]'],
            ['Site e LPs', '[Estado do site, conversão]', '[O que trava resultado]', '[Onde ganhar]'],
            ['E-mail e inbound', '[Base, fluxos ativos]', '[O que trava resultado]', '[Onde ganhar]'],
            ['Comercial', '[Como o lead é atendido]', '[O que trava resultado]', '[Onde ganhar]']], 'firstk', ['22mm', None, None, None])) + \
        sec(3, 'Referências de mercado', table(['Concorrente', 'Canal forte', 'O que fazem bem', 'Brecha para o cliente'], [
            ['[Concorrente 1]', '[Google / Instagram / SEO]', '[Observação]', '[Oportunidade]'],
            ['[Concorrente 2]', '[Canal]', '[Observação]', '[Oportunidade]'],
            ['[Concorrente 3]', '[Canal]', '[Observação]', '[Oportunidade]']], 'firstk')) + \
        note('<b>Regra:</b> todo número deste documento cita fonte e período. Número sem origem não entra.')
    p3 = sec(4, 'Objetivos e metas', table(['Objetivo', 'Indicador', 'Base', 'Meta mês 3', 'Meta mês 6', 'Fonte'], [
        ['[Objetivo 1]', '[Indicador]', '[000]', '[000]', '[000]', '[GA4 / CRM]'],
        ['', '[Indicador]', '[000]', '[000]', '[000]', '[Fonte]'],
        ['[Objetivo 2]', '[Indicador]', '[000]', '[000]', '[000]', '[Fonte]'],
        ['', '[Indicador]', '[000]', '[000]', '[000]', '[Fonte]'],
        ['[Objetivo 3]', '[Indicador]', '[000]', '[000]', '[000]', '[Fonte]'],
        ['', '[Indicador]', '[000]', '[000]', '[000]', '[Fonte]']], 'firstk', ['34mm', None, '18mm', '20mm', '20mm', '24mm']),
        'Máximo 3 objetivos, até 2 indicadores cada.') + \
        '<div class="two">' + sec(5, 'Premissas', chk(['[Verba de mídia aprovada até o dia X de cada mês]', '[Cliente responde aprovações em até 48h]',
                                                          '[Acesso a GA4, Ads, RD e CRM liberado]', '[Comercial atende o lead em até 1h útil]',
                                                          '[Premissa específica do cliente]'])) + \
        sec(6, 'Fora do escopo', chk(['[Item que o cliente pode achar que está incluso]', '[Produção de vídeo com equipe externa]',
                                       '[Atendimento de leads e vendas]', '[Item fora do escopo]'])) + '</div>' + \
        sec(7, 'Riscos', table(['Risco', 'Impacto', 'Mitigação', 'Departamento'], [
            ['[Atraso de aprovação do cliente]', '[Alto]', '[Calendário aprovado com 10 dias de antecedência]', '@cs'],
            ['[Verba abaixo do planejado]', '[Médio]', '[Priorizar campanha de fundo de funil]', '@tp'],
            ['[Risco específico]', '[Nível]', '[Ação]', '[Pessoa]']], 'firstk'))
    p4 = sec(8, 'Departamentos envolvidos', table(['Departamento', 'Entregas recorrentes', 'Cadência', 'Documento operacional'], [
        ['@adm', 'Estratégia, aprovação final, reunião de resultado', 'Mensal', 'Planejamento Mensal'],
        ['@tp', 'Campanhas Google e Meta, otimização, relatório', 'Semanal', 'Plano de Tráfego Pago'],
        ['@org', 'Blog, e-books, copy de posts, RD Station, e-mail', 'Semanal', 'Plano de Tráfego Orgânico'],
        ['@cri', 'Posts, stories, vídeos, criativos de anúncio', 'Semanal', 'Direção de Arte Redes Sociais e Anúncios'],
        ['@dev', 'Site, LPs, GTM, integrações', 'Por demanda', 'Briefing de Landing Page'],
        ['@cs', 'Aprovações, publicação, relacionamento', 'Contínua', 'Calendário Editorial']], '', ['40mm', None, '20mm', '44mm'])) + \
        sec(9, 'Entregas do semestre', table(['Entrega', 'Departamento', 'Quantidade', 'Prazo'], [
            ['[Landing page de conversão]', '@dev', '[1]', '[Mês 1]'],
            ['[Artigos de blog]', '@org', '[24]', '[4 por mês]'],
            ['[Material rico]', '@org', '[1]', '[Mês 2]'],
            ['[Fluxo de nutrição]', '@org', '[1]', '[Mês 3]'],
            ['[Posts em redes]', '@cri', '[96]', '[16 por mês]'],
            ['[Campanhas de mídia]', '@tp', '[3]', '[Mês 1]'],
            ['[Entrega específica]', '[Frente]', '[0]', '[Mês]']], 'firstk'))
    m = ['[Mês 1]', '[Mês 2]', '[Mês 3]', '[Mês 4]', '[Mês 5]', '[Mês 6]']
    p5 = sec(10, 'Roadmap do semestre', table(['Iniciativa', 'Departamento'] + ['^' + x for x in m], [
        ['[Setup de mensuração e GTM]', '@dev', B, E, E, E, E, E],
        ['[LP de conversão]', '@dev', B, B, E, E, E, E],
        ['[Campanhas de fundo de funil]', '@tp', E, B, B, B, B, B],
        ['[Campanhas de topo e remarketing]', '@tp', E, E, B, B, B, B],
        ['[Cluster de conteúdo 1]', '@org', B, B, B, E, E, E],
        ['[Cluster de conteúdo 2]', '@org', E, E, E, B, B, B],
        ['[Material rico]', '@org', E, B, B, E, E, E],
        ['[Fluxo de nutrição]', '@org', E, E, B, B, E, E],
        ['[Newsletter mensal]', '@org', E, B, B, B, B, B],
        ['[Calendário editorial]', '@cri', B, B, B, B, B, B],
        ['[Revisão trimestral]', '@adm', E, E, Y, E, E, Y]], 'firstk', [None, '36mm'] + ['13mm'] * 6),
        'Azul: execução. Amarelo: marco de revisão.') + \
        sec(11, 'Marcos', table(['Marco', 'Data', 'Critério de sucesso'], [
            ['[Mensuração validada]', '[dd/mm]', '[Todas as conversões registrando no GA4 e Ads]'],
            ['[LP no ar]', '[dd/mm]', '[Conversão da LP acima de X%]'],
            ['[Revisão do trimestre 1]', '[dd/mm]', '[Meta mês 3 atingida ou plano de correção]'],
            ['[Fechamento do semestre]', '[dd/mm]', '[Meta mês 6 e plano do próximo semestre]']], 'firstk', [None, '20mm', None]))
    p6 = sec(12, 'Verba de mídia', table(['Canal'] + ['^' + x for x in m] + ['^Total'], [
        ['Google Ads', 'R$ [0]', 'R$ [0]', 'R$ [0]', 'R$ [0]', 'R$ [0]', 'R$ [0]', 'R$ [0]'],
        ['Meta Ads', 'R$ [0]', 'R$ [0]', 'R$ [0]', 'R$ [0]', 'R$ [0]', 'R$ [0]', 'R$ [0]'],
        ['LinkedIn Ads', 'R$ [0]', 'R$ [0]', 'R$ [0]', 'R$ [0]', 'R$ [0]', 'R$ [0]', 'R$ [0]'],
        ['__tot__', 'Total', 'R$ [0]', 'R$ [0]', 'R$ [0]', 'R$ [0]', 'R$ [0]', 'R$ [0]', 'R$ [0]']], 'firstk'),
        'Verba paga direto às plataformas pelo cliente. Não inclui fee da agência.') + \
        sec(13, 'Rituais', table(['Ritual', 'Frequência', 'Departamentos', 'Entregável'], [
            ['Aprovação do calendário', 'Mensal, até dia [20]', '@cs + cliente', 'Calendário Editorial aprovado'],
            ['Otimização de campanhas', 'Semanal', '@tp', 'Registro de ajustes'],
            ['Relatório de performance', 'Mensal, até dia [5]', '@tp + @cs', 'Relatório de Performance'],
            ['Reunião de resultado', 'Mensal', '@adm + @cs + cliente', 'Planejamento Mensal seguinte'],
            ['Revisão do semestre', 'Mês 3 e mês 6', '@adm + diretoria do cliente', 'Ajuste de metas']], 'firstk')) + \
        sec(14, 'Prazos de aprovação do cliente', table(['Item', 'Prazo de resposta', 'Se atrasar'], [
            ['Calendário editorial', '[48h]', '[Publicação do mês desloca na mesma proporção]'],
            ['Peças e copy', '[24h]', '[Peça sai da semana]'],
            ['Landing page', '[72h]', '[Campanha de conversão não sobe]']], 'firstk'))
    return build('Template - Planejamento Semestral.html', 'Template - Planejamento Semestral', cov, [p2, p3, p4, p5, p6], 'Planejamento Semestral')


# ============ 2. PLANEJAMENTO MENSAL ============
def tarefas(rows):
    return table(['Entrega', 'Detalhe', 'Prazo', 'Status'], rows, 'firstk', ['46mm', None, '18mm', '20mm'])

def mensal():
    cov = cover('Planejamento Mensal', ('Foco do mês', '[Foco em até 6 palavras]', '[Mês] de [Ano]'),
                '[Cliente] · [Grupo]', ('Planejamento de', 'Marketing Mensal'),
                '[Uma frase com o que precisa acontecer neste mês e qual número vai provar que aconteceu.]',
                ['Resumo do mês', 'Entregas por pessoa', 'Cronograma semanal', 'Pendências do cliente', 'Datas e aprovações'])
    st = '<span class="st">A fazer</span>'
    p2 = sec(1, 'Resumo do mês', kv([
        ('R$ [0]', 'Verba de mídia', '[Google + Meta]'),
        ('[16]', 'Posts', 'Calendário Editorial'),
        ('[4]', 'Artigos de blog', 'Plano Orgânico'),
        ('[2]', 'Disparos de e-mail', 'RD Station'),
        ('[1]', 'Landing pages', 'Desenvolvimento')])) + \
        sec(2, 'Metas do mês', table(['Indicador', 'Meta do semestre', 'Meta do mês', 'Mês anterior', 'Fonte'], [
            ['[Leads]', '[000]', '[000]', '[000]', '[CRM]'],
            ['[Custo por lead]', 'R$ [00]', 'R$ [00]', 'R$ [00]', '[Ads]'],
            ['[Sessões orgânicas]', '[0.000]', '[0.000]', '[0.000]', 'GA4'],
            ['[Conversão da LP]', '[0,0%]', '[0,0%]', '[0,0%]', 'GA4'],
            ['[Indicador do cliente]', '[000]', '[000]', '[000]', '[Fonte]']], 'firstk')) + \
        sec(3, 'O que muda em relação ao mês anterior', table(['Frente', 'Ajuste', 'Motivo'], [
            ['[Tráfego pago]', '[O que muda]', '[Dado que justifica]'],
            ['[Conteúdo]', '[O que muda]', '[Dado que justifica]'],
            ['[Redes sociais]', '[O que muda]', '[Dado que justifica]']], 'firstk', ['30mm', None, None])) + \
        note('<b>Foco do mês:</b> [uma frase com a prioridade que desempata qualquer conflito de agenda].')
    p3 = sec(4, 'Entregas por departamento', own('tp', 'Campanhas, otimização e relatório') + tarefas([
        ['[Subir campanha X]', '[Plataforma, verba/dia, LP]', '[dd/mm]', st],
        ['[Otimização semanal]', '[Termos, lances, criativos]', 'Semanal', st],
        ['[Relatório do mês anterior]', '[Enviar ao Sucesso do Cliente]', '[dd/mm]', st]]) +
        '<div style="height:3mm"></div>' + own('org', 'Conteúdo · blog, e-book, copy') + tarefas([
        ['[Artigo 1]', '[Palavra-chave]', '[dd/mm]', st],
        ['[Artigo 2]', '[Palavra-chave]', '[dd/mm]', st],
        ['[Copy dos posts do mês seguinte]', '[16 peças]', '[dd/mm]', st]]) +
        '<div style="height:3mm"></div>' + own('org', 'Inbound · RD Station, e-mail') + tarefas([
        ['[Disparo newsletter]', '[Segmento, assunto]', '[dd/mm]', st],
        ['[Fluxo de nutrição]', '[Etapa do fluxo]', '[dd/mm]', st],
        ['[Formulário da LP no RD]', '[Campos e mapeamento]', '[dd/mm]', st]]))
    p4 = own('cri', 'Posts, stories, vídeos e criativos de anúncio') + tarefas([
        ['[Artes semana 1 e 2]', '[Ver Direção de Arte Redes Sociais]', '[dd/mm]', st],
        ['[Artes semana 3 e 4]', '[8 peças]', '[dd/mm]', st],
        ['[Criativos de anúncio]', '[Ver Direção de Arte Anúncios]', '[dd/mm]', st]]) + \
        '<div style="height:3mm"></div>' + own('dev', 'Site, landing page e GTM') + tarefas([
        ['[Landing page X]', '[Ver briefing de LP]', '[dd/mm]', st],
        ['[Eventos de conversão]', '[GTM, GA4, Ads, Meta]', '[dd/mm]', st],
        ['[Manutenção do site]', '[Atualizações e backup]', '[dd/mm]', st]]) + \
        '<div style="height:3mm"></div>' + own('cs', 'Aprovação e publicação') + tarefas([
        ['[Aprovação do calendário]', '[Enviar ao cliente]', '[dd/mm]', st],
        ['[Agendamento dos posts]', '[Todas as redes]', '[dd/mm]', st],
        ['[Reunião de resultado]', '[Pauta e ata]', '[dd/mm]', st]]) + \
        '<div style="height:3mm"></div>' + own('adm', 'Aprovação final') + tarefas([
        ['[Aprovar peças e LP]', '[Antes do envio ao cliente]', '[dd/mm]', st],
        ['[Reunião de resultado]', '[Com a diretoria do cliente]', '[dd/mm]', st]])
    p5 = sec(5, 'Cronograma semanal', table(['Semana', 'Período', 'Entregas-chave', 'Aprovação do cliente'], [
        ['Semana 1', '[dd a dd/mm]', '[Campanhas no ar, artigo 1, posts sem. 1]', '[Peças da semana 2]'],
        ['Semana 2', '[dd a dd/mm]', '[LP em homologação, artigo 2, newsletter]', '[LP e peças da semana 3]'],
        ['Semana 3', '[dd a dd/mm]', '[LP no ar, artigo 3, otimização]', '[Peças da semana 4]'],
        ['Semana 4', '[dd a dd/mm]', '[Artigo 4, calendário do mês seguinte]', '[Calendário do mês seguinte]']], 'firstk', ['18mm', '24mm', None, None])) + \
        sec(6, 'Pendências do cliente', table(['Item', 'O que precisamos', 'Prazo', 'Impacto se atrasar'], [
            ['[Acesso]', '[Ex: admin do Meta Business]', '[dd/mm]', '[Campanha não sobe]'],
            ['[Material]', '[Ex: fotos da fábrica]', '[dd/mm]', '[Posts com banco de imagem]'],
            ['[Informação]', '[Ex: tabela de preços]', '[dd/mm]', '[LP sem oferta]'],
            ['[Aprovação]', '[Ex: copy da LP]', '[dd/mm]', '[Publicação atrasa]']], 'firstk')) + \
        sec(7, 'Datas do mês', table(['Data', 'Evento', 'Ação'], [
            ['[dd/mm]', '[Data comemorativa do setor]', '[Post ou campanha]'],
            ['[dd/mm]', '[Feira, evento, lançamento]', '[Ação prevista]'],
            ['[dd/mm]', '[Reunião de resultado]', '[Pauta]']], 'firstk', ['20mm', None, None]))
    return build('Template - Planejamento Mensal.html', 'Template - Planejamento Mensal', cov, [p2, p3, p4, p5], 'Planejamento Mensal')


from docs_cal_arte import calendario, calendario_tri, arte, anuncios, wireframe


# ============ 5. TRÁFEGO PAGO (ROSANE) ============
def pago():
    cov = cover('Plano de Tráfego Pago', ('Verba de mídia', 'R$ [0.000] / mês', '[Mês] de [Ano]'),
                '[Cliente] · Documento interno', ('Plano de', 'Tráfego Pago'),
                '[Uma frase com o objetivo da mídia no período e o custo por lead que torna a operação viável.]',
                ['Objetivos e KPIs', 'Verba e distribuição', 'Estrutura de campanhas', 'Públicos e palavras', 'Mensuração e rotina'])
    p2 = own('tp', 'Entrega e prazos deste documento') + \
        sec(1, 'Objetivos e KPIs', kv([('R$ [0]', 'Verba mensal', '[Mês]'), ('[000]', 'Leads', 'Meta do mês'), ('R$ [00]', 'CPL máximo', 'Meta do mês'),
                                      ('[0,0%]', 'CTR mínimo', 'Pesquisa'), ('[0,0%]', 'Conversão LP', 'GA4')]) + '<div style="height:3mm"></div>' +
            table(['KPI', 'Base', 'Meta', 'Fonte', 'Ação se ficar abaixo'], [
                ['[Leads]', '[000]', '[000]', '[CRM]', '[Revisar LP e oferta]'],
                ['[CPL]', 'R$ [00]', 'R$ [00]', '[Ads]', '[Cortar termos e públicos caros]'],
                ['[Taxa de lead qualificado]', '[00%]', '[00%]', '[CRM]', '[Ajustar segmentação e negativas]']], 'firstk')) + \
        sec(2, 'Verba e distribuição', table(['Plataforma', 'Campanha', '^%', 'Mensal', 'Diário'], [
            ['Google Ads', '[Pesquisa · fundo de funil]', ('[40%]', 'c'), 'R$ [0]', 'R$ [0]'],
            ['Google Ads', '[Performance Max / Display remarketing]', ('[15%]', 'c'), 'R$ [0]', 'R$ [0]'],
            ['Meta Ads', '[Cadastro · público frio]', ('[25%]', 'c'), 'R$ [0]', 'R$ [0]'],
            ['Meta Ads', '[Remarketing]', ('[10%]', 'c'), 'R$ [0]', 'R$ [0]'],
            ['LinkedIn Ads', '[Decisores · cargos]', ('[10%]', 'c'), 'R$ [0]', 'R$ [0]'],
            ['__tot__', 'Total', '', ('100%', 'c'), 'R$ [0]', 'R$ [0]']], 'firstk', ['24mm', None, '12mm', '22mm', '20mm']))
    p3 = sec(3, 'Estrutura de campanhas', table(['Campanha', 'Tipo e lance', 'Segmentação', 'Anúncios', 'Destino'], [
        ['[G · Pesquisa · Produto]', '[Pesquisa · CPA desejado]', '[Palavras do grupo 1, [Região]]', '[3 RSA]', '[LP X]'],
        ['[G · Pesquisa · Marca]', '[Pesquisa · parcela de impr.]', '[Nome da marca]', '[1 RSA]', '[Home]'],
        ['[G · PMax]', '[Maximizar conversões]', '[Sinais: lista de clientes]', '[Grupo de recursos]', '[LP X]'],
        ['[M · Cadastro · Frio]', '[Leads · formulário ou site]', '[Interesses ou semelhante 1%]', '[3 criativos]', '[LP X]'],
        ['[M · Remarketing]', '[Conversões]', '[Visitantes 30 dias sem lead]', '[2 criativos]', '[LP X]'],
        ['[LI · Decisores]', '[Lead Gen Form]', '[Cargo, setor, porte]', '[2 criativos]', '[Formulário nativo]']], 'firstk', ['30mm', '28mm', None, '20mm', '18mm']),
        'Nomenclatura: Plataforma · Tipo · Tema.') + \
        sec(4, 'Criativos de anúncio', table(['Código', 'Campanha', 'Formatos', 'Mensagem', 'Arte até'], [
            ['A01', '[M · Cadastro · Frio]', '1080 × 1350 e 1080 × 1920', '[Dor principal + oferta]', '[dd/mm]'],
            ['A02', '[M · Remarketing]', '1080 × 1080 e 1200 × 628', '[Prova social]', '[dd/mm]'],
            ['A03', '[LI · Decisores]', '1200 × 1200', '[Dado de mercado]', '[dd/mm]']], 'firstk', ['14mm', None, None, None, '18mm']),
            'Controle do Tráfego Pago. O briefing de cada código vai para o Criativos no template Direção de Arte Anúncios.') + \
        sec(5, 'Copy de anúncios', table(['Campanha', 'Títulos', 'Descrições'], [
            ['[G · Pesquisa · Produto]', '[Até 15 títulos · 30 caracteres]', '[Até 4 descrições · 90 caracteres]'],
            ['[Meta]', '[Texto principal · 125 caracteres]', '[Título · 40 caracteres]']], 'firstk', ['36mm', None, None]))
    p4 = sec(6, 'Públicos', table(['Público', 'Plataforma', 'Definição', 'Uso'], [
        ['[Clientes atuais]', 'Google, Meta', '[Lista do CRM, atualizada em dd/mm]', '[Exclusão e semelhante]'],
        ['[Visitantes do site]', 'Google, Meta', '[Últimos 30 dias, sem conversão]', '[Remarketing]'],
        ['[Semelhante 1%]', 'Meta', '[Base: leads qualificados]', '[Prospecção]'],
        ['[Decisores]', 'LinkedIn', '[Cargos, setores, porte]', '[Prospecção B2B]']], 'firstk')) + \
        sec(7, 'Palavras-chave', chips(['[palavra-chave 1]', '[palavra-chave 2]', '[palavra-chave 3]', '[palavra-chave 4]', '[palavra-chave 5]',
                                       '[palavra-chave 6]', '[palavra-chave 7]', '[palavra-chave 8]']), 'Correspondência de frase e exata. Ampla só com Smart Bidding e histórico.') + \
        sec(8, 'Negativas', chips(['grátis', 'curso', 'vaga', 'emprego', 'o que é', 'pdf', '[negativa do cliente]', '[concorrente]'], neg=True)) + \
        sec(9, 'Segmentação geral', table(['Item', 'Definição'], [
            ['Região', '[Cidades, raio ou estados]'], ['Horário', '[Seg a sex, 7h a 19h]'],
            ['Dispositivo', '[Ajuste de lance mobile]'], ['Idioma', 'Português']], 'firstk', ['26mm', None]))
    p5 = sec(10, 'Mensuração', table(['Evento', 'Plataformas', 'Origem', 'Status'], [
        ['[generate_lead]', 'GA4, Google Ads, Meta', 'GTM · envio do formulário', '<span class="st">Validar</span>'],
        ['[click_whatsapp]', 'GA4, Google Ads, Meta', 'GTM · clique no botão', '<span class="st">Validar</span>'],
        ['[Lead qualificado]', 'Google Ads (offline)', 'CRM · importação', '<span class="st">Validar</span>'],
        ['[Evento do cliente]', '[Plataformas]', '[Origem]', '<span class="st">Validar</span>']], 'firstk'),
        'Eventos configurados pelo Desenvolvimento. Campanha só sobe com conversão validada.') + \
        sec(11, 'Padrão de UTM', note('utm_source=<b>google | meta | linkedin</b> · utm_medium=<b>cpc | paid_social</b> · utm_campaign=<b>nome da campanha</b> · utm_content=<b>criativo</b>')) + \
        sec(12, 'Rotina de otimização', table(['Frequência', 'Ação'], [
            ['Diária', 'Checar gasto, reprovações e campanhas paradas'],
            ['Semanal', 'Termos de pesquisa e negativas, pausa de anúncio fraco, ajuste de lance'],
            ['Quinzenal', 'Troca de criativo com frequência acima de [3] ou CTR em queda'],
            ['Mensal', 'Relatório para o Sucesso do Cliente até dia [5], redistribuição de verba']], 'firstk', ['24mm', None])) + \
        sec(13, 'Acessos', chk(['Google Ads com acesso admin', 'Meta Business com acesso à conta de anúncios e ao pixel', 'LinkedIn Campaign Manager', 'GA4 como editor', 'Forma de pagamento do cliente ativa']))
    return build('Template - Plano de Tráfego Pago.html', 'Template - Plano de Tráfego Pago', cov, [p2, p3, p4, p5], 'Plano de Tráfego Pago')


# ============ 6. TRÁFEGO ORGÂNICO (BRUNO E DUDA) ============
def organico():
    cov = cover('Plano de Tráfego Orgânico', ('Departamento', 'Tráfego Orgânico', '[Mês] de [Ano]'),
                '[Cliente] · Documento interno', ('Plano de', 'Tráfego Orgânico'),
                '[Uma frase com o que o orgânico precisa gerar no período: posição, tráfego ou leads por e-mail.]',
                ['Metas orgânicas', 'Palavras-chave', 'Blog e conteúdo', 'Inbound e e-mail', 'Rotina e dependências'])
    p2 = sec(1, 'Metas orgânicas', kv([('[0.000]', 'Sessões orgânicas', 'GA4 · meta do mês'), ('[00]', 'Palavras no top 10', 'Search Console'),
                                     ('[00]', 'Leads orgânicos', 'RD Station'), ('[00%]', 'Abertura de e-mail', 'RD Station'), ('[0,0%]', 'Clique em e-mail', 'RD Station')]) +
                                   '<div style="height:3mm"></div>' + table(['Indicador', 'Base', 'Meta', 'Fonte'], [
                                       ['[Sessões orgânicas]', '[0.000]', '[0.000]', 'GA4'], ['[Cliques do Google]', '[0.000]', '[0.000]', 'Search Console'],
                                       ['[Leads por conversão orgânica]', '[00]', '[00]', 'RD Station'], ['[Citações em busca por IA]', '[0]', '[0]', '[Ferramenta]']], 'firstk')) + \
        sec(2, 'Clusters e palavras-chave', table(['Cluster', 'Palavra principal', 'Secundárias', 'Intenção', 'Página destino'], [
            ['[Cluster 1]', '[palavra]', '[palavra, palavra]', '[Transacional]', '[URL do pilar]'],
            ['[Cluster 1]', '[palavra]', '[palavra, palavra]', '[Informacional]', '[Artigo novo]'],
            ['[Cluster 2]', '[palavra]', '[palavra, palavra]', '[Comercial]', '[URL]'],
            ['[Cluster 2]', '[palavra]', '[palavra, palavra]', '[Informacional]', '[Artigo novo]'],
            ['[Cluster 3]', '[palavra]', '[palavra, palavra]', '[Informacional]', '[Artigo novo]']], 'firstk'),
        'Uma página por palavra principal. Sem duas páginas disputando o mesmo termo.')
    p3 = own('org', 'Conteúdo · blog, materiais ricos e copy') + \
        sec(3, 'Pauta de artigos', table(['#', 'Título provisório', 'Palavra-chave', 'Tamanho', 'Rascunho', 'Publica', 'Status'], [
            [f'{i:02d}', '[Título]', '[palavra]', '[1.200]', '[dd/mm]', '[dd/mm]', '<span class="st">Pauta</span>'] for i in range(1, 5)] +
            [['05', '[Refresh: artigo antigo]', '[palavra]', '[ajuste]', '[dd/mm]', '[dd/mm]', '<span class="st">Pauta</span>']], 'firstk', ['8mm', None, '28mm', '16mm', '17mm', '17mm', '15mm'])) + \
        sec(4, 'Material rico', table(['Material', 'Tema', 'Páginas', 'Entrega', 'Uso'], [
            ['[E-book / checklist]', '[Tema]', '[12]', '[dd/mm]', '[Isca do fluxo de nutrição]']], 'firstk'), 'Texto do Conteúdo. A arte do e-book sai por tarefa avulsa no Notion, fora deste plano.') + \
        sec(5, 'Padrão de entrega do artigo', '<div class="two">' + chk(['Palavra no título, na URL e no primeiro parágrafo', 'Meta description de até 155 caracteres',
                                                                         'H2 e H3 respondendo perguntas reais', 'Resumo direto no topo para busca por IA']) +
            chk(['3 links internos e 1 externo de autoridade', 'CTA para o material rico ou contato', 'Imagem de capa do banco do cliente, 1200 × 630', 'Rank Math verde, sem perseguir 100']) + '</div>') + \
        sec(6, 'Copy para o Inbound', table(['Entrega', 'Para', 'Prazo'], [
            ['[Copy dos e-mails do fluxo]', 'Inbound', '[dd/mm]'], ['[Copy da newsletter]', 'Inbound', '[dd/mm]']], 'firstk'))
    p4 = own('org', 'Inbound · RD Station, automação e e-mail') + \
        sec(7, 'Fluxos de automação', table(['Fluxo', 'Gatilho', 'E-mails', 'Objetivo', 'Status'], [
            ['[Boas-vindas]', '[Conversão na LP X]', '[3]', '[Entregar material e apresentar a empresa]', '<span class="st">Ativo</span>'],
            ['[Nutrição cluster 1]', '[Download do e-book]', '[5]', '[Levar ao contato comercial]', '<span class="st">Criar</span>'],
            ['[Reengajamento]', '[90 dias sem abertura]', '[2]', '[Limpar base]', '<span class="st">Criar</span>']], 'firstk', ['28mm', '30mm', '14mm', None, '16mm'])) + \
        sec(8, 'Disparos do mês', table(['Data', 'Assunto', 'Segmento', 'Objetivo', 'Status'], [
            ['[dd/mm]', '[Newsletter do mês]', '[Base ativa]', '[Tráfego para o blog]', '<span class="st">Pauta</span>'],
            ['[dd/mm]', '[Oferta ou evento]', '[Leads qualificados]', '[Contato comercial]', '<span class="st">Pauta</span>']], 'firstk', ['17mm', None, '28mm', None, '16mm'])) + \
        sec(9, 'Formulários e lead scoring', table(['Item', 'Definição'], [
            ['Formulários ativos', '[LP X, contato do site, blog]'], ['Campos obrigatórios', '[Nome, e-mail, empresa, cargo, telefone]'],
            ['Lead qualificado', '[Perfil A ou B + interesse acima de X]'], ['Passagem ao comercial', '[Como e para quem o lead vai]']], 'firstk', ['34mm', None])) + \
        sec(10, 'Saúde da base', chk(['Bounce abaixo de [2%] no último disparo', 'Descadastros abaixo de [0,5%]', 'Domínio autenticado (SPF, DKIM, DMARC)', 'Base higienizada nos últimos 90 dias']))
    p5 = sec(11, 'Rotina', table(['Frequência', 'Conteúdo', 'Inbound'], [
        ['Semanal', 'Publicar artigo, conferir indexação', 'Conferir fluxos e novos leads'],
        ['Quinzenal', 'Search Console: queda e oportunidade', 'Disparo e leitura de resultado'],
        ['Mensal', 'Refresh de 1 artigo antigo', 'Relatório de e-mail e leads para o Sucesso do Cliente']], 'firstk', ['24mm', None, None])) + \
        sec(12, 'Dependências', table(['Preciso de', 'Quem entrega', 'O quê', 'Prazo'], [
            ['Conteúdo', 'Cliente via @cs', '[Aprovação da pauta do mês]', '[dd/mm]'], ['Conteúdo', 'Cliente via @cs', '[Validação técnica do conteúdo]', '[dd/mm]'],
            ['Inbound', 'Conteúdo', '[Copy dos e-mails]', '[dd/mm]'], ['Inbound', 'Cliente via @cs', '[Lista de contatos atualizada]', '[dd/mm]']], 'firstk')) + \
        sec(13, 'Onde fica cada coisa', table(['Item', 'Local'], [
            ['Artigos em rascunho', '[Drive / Cliente / Blog]'], ['Publicação', '[WordPress do cliente]'],
            ['Fluxos e e-mails', '[RD Station da conta X]'], ['Tarefas', 'Notion · Tarefas Gerais']], 'firstk', ['36mm', None])) + \
        note('<b>Regra:</b> nenhum artigo sobe sem revisão do Administrativo e nenhum e-mail dispara sem teste enviado ao Sucesso do Cliente.')
    return build('Template - Plano de Tráfego Orgânico.html', 'Template - Plano de Tráfego Orgânico', cov, [p2, p3, p4, p5], 'Plano de Tráfego Orgânico')


# ============ 7. LANDING PAGE (GEORGES) ============
def lp():
    cov = cover('Briefing de Landing Page', ('Conversão principal', '[Envio do formulário]', 'Publicação até [dd/mm/aaaa]'),
                '[Cliente] · Documento interno', ('Briefing de', 'Landing Page'),
                '[Uma frase com a oferta da página, para quem ela fala e qual ação o visitante precisa tomar.]',
                ['Dados do projeto', 'Estrutura e copy', 'Wireframe', 'Formulário e integrações', 'Publicação'])
    p2 = own('dev', 'Entrega e prazos deste documento') + \
        sec(1, 'Dados do projeto', table(['Item', 'Definição'], [
            ['URL final', '[dominio.com.br/pagina]'], ['Plataforma', '[WordPress + Elementor / Strapi + Astro / HTML]'],
            ['Hospedagem', '[Onde está e quem tem acesso]'], ['Origem do tráfego', '[Google Ads, Meta, e-mail, orgânico]'],
            ['Oferta', '[O que o visitante recebe ao converter]'], ['Público', '[Cargo, setor, porte]'],
            ['Copy', '[Link do documento aprovado · Tráfego Orgânico]'], ['Layout', 'Desenvolvimento, a partir do wireframe da pág. 04'],
            ['Prazo', '[Homologação dd/mm · Publicação dd/mm]']], 'firstk', ['30mm', None])) + \
        sec(2, 'Meta da página', kv([('[0,0%]', 'Conversão', 'GA4 · 30 dias'), ('[90+]', 'PageSpeed mobile', 'PSI'),
                                    ('[< 2,5 s]', 'LCP', 'PSI'), ('[000]', 'Leads / mês', 'RD Station')], 'k4'))
    p3 = sec(3, 'Estrutura e copy', table(['#', 'Seção', 'Objetivo', 'Conteúdo', 'Assets'], [
        ['01', 'Hero', 'Dizer a oferta em 5 segundos', '[Título, sub, CTA, formulário ou botão]', '[Imagem real]'],
        ['02', 'Prova', 'Gerar confiança imediata', '[Logos de clientes, números]', '[Logos]'],
        ['03', 'Dor', 'Gerar identificação', '[3 problemas do público]', '[Ícones]'],
        ['04', 'Solução', 'Mostrar o que muda', '[3 a 6 benefícios]', '[Ícones]'],
        ['05', 'Como funciona', 'Tirar o medo do processo', '[3 passos]', '[Nenhum]'],
        ['06', 'Depoimentos', 'Prova social', '[2 ou 3 depoimentos com nome e cargo]', '[Fotos]'],
        ['07', 'FAQ', 'Quebrar objeções', '[5 perguntas]', '[Nenhum]'],
        ['08', 'CTA final', 'Converter quem rolou tudo', '[Repetir oferta e formulário]', '[Nenhum]'],
        ['09', 'Rodapé', 'Dados legais', '[CNPJ, endereço, política de privacidade]', '[Logo]']], 'firstk', ['8mm', '24mm', '38mm', None, '22mm']),
        'Ordem padrão. Remover seção sem conteúdo real, nunca preencher com texto genérico.') + \
        sec(4, 'Mensagem', table(['Item', 'Definição'], [
            ['Promessa', '[Resultado que o visitante tem ao converter, em uma frase]'],
            ['Prova principal', '[Número, cliente ou certificação que sustenta a promessa]'],
            ['Objeções', '[Preço, prazo, confiança: como a página responde cada uma]'],
            ['Termos proibidos', '[Palavras e marcas vetadas pelo cliente]']], 'firstk', ['30mm', None])) + \
        note('<b>Menu:</b> LP de campanha não tem menu de navegação. Único link de saída é a política de privacidade.')
    p4 = sec(6, 'Formulário', table(['Campo', 'Tipo', '^Obrigatório', 'Campo no RD'], [
        ['Nome', 'Texto', ('Sim', 'c'), 'name'], ['E-mail corporativo', 'E-mail', ('Sim', 'c'), 'email'],
        ['Telefone / WhatsApp', 'Telefone com máscara', ('Sim', 'c'), 'mobile_phone'], ['Empresa', 'Texto', ('Sim', 'c'), 'company'],
        ['Cargo', 'Seleção', ('[Sim]', 'c'), 'job_title'], ['[Campo do cliente]', '[Tipo]', ('[Não]', 'c'), '[cf_campo]'],
        ['Consentimento LGPD', 'Checkbox', ('Sim', 'c'), '[cf_lgpd]']], 'firstk'),
        'Após o envio: página de obrigado em [URL/obrigado], nunca só mensagem na mesma tela.') + \
        sec(7, 'Integrações e eventos', table(['Ferramenta', 'Configurar', 'ID / evento', 'Status'], [
            ['Google Tag Manager', 'Container na página e na de obrigado', '[GTM-XXXX]', '<span class="st">Validar</span>'],
            ['GA4', 'Evento generate_lead no envio', '[G-XXXX]', '<span class="st">Validar</span>'],
            ['Google Ads', 'Conversão com rótulo e valor', '[AW-XXXX/rótulo]', '<span class="st">Validar</span>'],
            ['Meta', 'Pixel + API de conversões, evento Lead', '[ID do pixel]', '<span class="st">Validar</span>'],
            ['RD Station', 'Formulário integrado, identificador da conversão', '[lp-nome-mes]', '<span class="st">Validar</span>'],
            ['WhatsApp', 'Botão com evento click_whatsapp', '[Número]', '<span class="st">Validar</span>'],
            ['UTM', 'Capturar utm_* em campo oculto', 'utm_source, medium, campaign', '<span class="st">Validar</span>']], 'firstk'))
    p5 = sec(8, 'Requisitos técnicos', '<div class="two">' + chk(['Imagens em WEBP e com lazy load', 'Fontes com font-display: swap', 'Sem slider no hero',
                                                                   'Layout testado em 360 px, 768 px e 1440 px', 'Botões com área de toque mínima de 44 px']) +
        chk(['Title e meta description definidos', 'Um único H1, igual à promessa do hero', 'Open Graph com imagem 1200 × 630',
             'Favicon e política de privacidade', '[noindex se a página for só de mídia paga]']) + '</div>') + \
        sec(9, 'Checklist de publicação', chk(['Envio de teste com lead chegando no RD Station', 'Evento visto no DebugView do GA4 e no Tag Assistant',
                                              'Conversão registrada no Google Ads e evento Lead no Gerenciador da Meta', 'PageSpeed mobile acima da meta',
                                              'Revisão de texto contra a copy aprovada', 'Aprovação do Administrativo antes de enviar ao cliente',
                                              'Aviso ao Tráfego Pago com a URL final para subir as campanhas', 'Card do Notion movido para Concluído'])) + \
        sec(10, 'Acessos necessários', table(['Acesso', 'Quem libera', 'Status'], [
            ['[Painel da hospedagem / WordPress]', 'Cliente via @cs', '<span class="st">Pendente</span>'],
            ['[DNS para subdomínio]', '[Cliente]', '<span class="st">Pendente</span>'],
            ['[GTM e GA4]', '[Cliente]', '<span class="st">Pendente</span>'],
            ['[RD Station]', '@org', '<span class="st">Pendente</span>']], 'firstk'))
    pw = sec(5, 'Wireframe de referência', wireframe(), 'Ordem e hierarquia, não layout final. Números iguais aos da tabela de estrutura. Blocos cinza escuro mudam o fundo da seção.')
    return build('Template - Landing Page.html', 'Template - Landing Page', cov, [p2, p3, pw, p4, p5], 'Briefing de Landing Page')


if __name__ == '__main__':
    import base
    if base.CSS_URL:
        base.write_css(os.path.join(os.path.dirname(__file__), '..', 'assets', 'allq-templates.css'))
    for f in (semestral, mensal, calendario, calendario_tri, arte, anuncios, pago, organico, lp):
        print(f())
