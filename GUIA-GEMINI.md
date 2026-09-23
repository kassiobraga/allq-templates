# Guia dos Templates de Planejamento · All.Q Agência · v1.3.0

Este guia explica cada template de planejamento da All.Q: quando usar, quem preenche e o que vai em cada seção. Os arquivos "Template - ... .html" desta pasta são os templates oficiais em código. Ao ajudar alguém do time, a entrega é sempre o documento completo em HTML, feito a partir do template correspondente.

## Como entregar o documento em HTML

1. Abra o arquivo "Template - [tipo].html" correspondente ao pedido.
2. Copie o `<head>` sem nenhuma mudança, exceto o `<title>`. O visual vem da linha `<link href="https://allq.com.br/id-visual/design/allq-templates.css">`. Nunca crie `<style>` nem classes novas.
3. No `<body>`, mantenha a mesma sequência de `<section class="pg">` (uma por página A4) e as mesmas classes.
4. Substitua cada `<span class="ph">[...]</span>` pelo conteúdo real, em texto simples, sem o span e sem os colchetes. Se o dado não existir, mantenha o span com o colchete.
5. Linhas de tabela, fichas de peça e blocos de departamento podem ser duplicados ou removidos para caber o conteúdo real, sempre copiando a estrutura de uma linha ou ficha existente.
6. Cada página comporta o conteúdo do template. Se o conteúdo real for maior, crie uma nova `<section class="pg">` copiando a estrutura de uma página interna e ajuste a numeração "Pág. N / Total" em todas as páginas.
7. Entregue o HTML completo, do `<!DOCTYPE html>` ao `</html>`, em um único bloco, pronto para salvar como `.html`, abrir no Chrome e exportar em PDF (Ctrl+P, Salvar como PDF, com "Gráficos de segundo plano" marcado).

## Regras que valem para todos

- Português correto, tom direto. Nunca usar travessão (—). Trocar por vírgula, ponto ou "·".
- Todo número cita fonte e período. Exemplo: "312 leads · CRM · agosto 2026". Número sem origem não entra.
- Parágrafo com no máximo 4 linhas. Lista com mais de 3 itens vira tabela.
- Citar departamento, nunca o nome da pessoa.
- O documento veste a marca da All.Q. A cor e a fonte do cliente só aparecem nas peças dele, nunca na estrutura do documento.
- Campos entre [colchetes] no template são para substituir. Nenhum colchete pode sobrar na entrega.
- Nome do arquivo: `Nome Completo do Cliente - Tipo de Material - Período`.

## Departamentos

| Departamento | Cor | Faz |
|---|---|---|
| Administrativo | Marrom | Estratégia, revisão e aprovação final, reunião de resultado |
| Sucesso do Cliente | Amarelo | Aprovação com o cliente, publicação, relacionamento |
| Desenvolvimento | Vermelho | Site, landing page, GTM, integrações |
| Tráfego Pago | Azul | Campanhas Google, Meta e LinkedIn, otimização, relatório |
| Criativos | Rosa | Posts, stories, vídeos, criativos de anúncio |
| Tráfego Orgânico | Verde | Blog, e-book, copy de posts e e-mails, RD Station |
| Design | Roxo | Identidade visual, branding, material impresso |

## Formatos de publicação

| Formato | Cor | O que é | Redes | Dimensão |
|---|---|---|---|---|
| Estático | Azul | Imagem única com título e sub | Instagram, Facebook, Google Meu Negócio | 1080 × 1350 |
| Carrossel | Roxo | 6 lâminas: capa, 4 de conteúdo, último com CTA | Instagram, LinkedIn, Facebook | 1080 × 1350 |
| Reels | Laranja | Vídeo vertical de 30 a 45 s com legenda na tela | Instagram, TikTok, YouTube | 1080 × 1920 |
| Vídeo | Vermelho | Vídeo horizontal de 3 a 10 min com capa | YouTube, LinkedIn | 1920 × 1080 |
| Stories | Rosa | 3 a 5 telas, enquete, caixa de pergunta, link | Instagram, Facebook | 1080 × 1920 |
| Texto | Verde | Post só texto, imagem opcional | LinkedIn | Sem arte |

Pilares editoriais: Quebra de crença (Carrossel), Educação (Carrossel, Vídeo), Bastidor (Reels), Diagnóstico (Estático), Relacionamento (Stories), Autoridade (Texto).

## Fluxo mensal de conteúdo

| Etapa | Departamento | Prazo |
|---|---|---|
| Copy | Tráfego Orgânico | Até dia 10 |
| Arte | Criativos | Até dia 15 |
| Revisão | Administrativo | Até dia 17 |
| Aprovação do cliente | Sucesso do Cliente | Resposta em 48h |
| Agendamento | Sucesso do Cliente | Até dia 25 |

---

## 1. Planejamento Semestral

**Quando:** início de cada semestre do cliente. **Quem preenche:** Administrativo.
**Capa · 4ª coluna da faixa:** Objetivo do semestre.

| Seção | O que preencher |
|---|---|
| Ponto de partida | 5 números de base com fonte e período: leads/mês, custo por lead, sessões orgânicas, conversão da LP, oportunidades/mês |
| Diagnóstico por frente | Para tráfego pago, SEO, redes, site, e-mail e comercial: situação hoje, problema principal, oportunidade |
| Referências de mercado | 3 concorrentes: canal forte, o que fazem bem, brecha para o cliente |
| Objetivos e metas | Até 3 objetivos, até 2 indicadores cada: base, meta do mês 3, meta do mês 6, fonte |
| Premissas / Fora do escopo | Condições que o cliente precisa cumprir e o que não está incluso |
| Riscos | Risco, impacto, mitigação, departamento |
| Departamentos envolvidos | Entregas recorrentes, cadência e documento operacional de cada departamento |
| Entregas do semestre | Entrega, departamento, quantidade, prazo |
| Roadmap | Iniciativas por departamento distribuídas nos 6 meses, com marcos de revisão |
| Marcos | Data e critério de sucesso |
| Verba de mídia | Valor por canal e por mês. Verba paga direto às plataformas, sem fee |
| Rituais e prazos de aprovação | Frequência, departamentos, entregável, prazo de resposta do cliente |

## 2. Planejamento Mensal

**Quando:** até o dia 25 do mês anterior. **Quem preenche:** Administrativo.
**Capa · 4ª coluna:** Foco do mês.

| Seção | O que preencher |
|---|---|
| Resumo do mês | Verba, posts, artigos, disparos de e-mail, landing pages |
| Metas do mês | Indicador, meta do semestre, meta do mês, resultado do mês anterior, fonte |
| O que muda | Ajuste por frente e o dado que justifica |
| Entregas por departamento | Um bloco por departamento: entrega, detalhe, prazo, status |
| Cronograma semanal | Entregas-chave e aprovações do cliente por semana |
| Pendências do cliente | O que precisamos, prazo, impacto se atrasar |
| Datas do mês | Datas comemorativas, eventos, reunião de resultado |

## 3. Calendário Editorial (mensal) e 4. Calendário Editorial Trimestral

**Quando:** mensal até o dia 20 do mês anterior; trimestral no início do trimestre. **Quem preenche:** Sucesso do Cliente, com copy do Tráfego Orgânico.
**Capa · 4ª coluna:** Cadência (peças no mês).

| Seção | O que preencher |
|---|---|
| Visão do mês / trimestre | Calendário com o formato de cada dia na cor do formato. No trimestral, 3 calendários lado a lado; dia com duas peças fica dividido na diagonal |
| Tema de cada mês | Só no trimestral: tema, objetivo, destaque |
| Formatos do mês | Quantidade de cada formato |
| Pilares | Objetivo de cada pilar para o cliente |
| Grade de posts | Uma linha por peça: número, data, dia, formato, pilar, tema, redes, status. A linha tem o fundo na cor do formato |
| Fluxo de aprovação e datas | Prazos do fluxo e datas relevantes |

A copy completa não entra no calendário. Ela vai na Direção de Arte Redes Sociais.

## 5. Direção de Arte Redes Sociais

**Quando:** junto com o calendário do mês. **Quem usa:** Criativos. **Capa · 4ª coluna:** Departamento Criativos.

| Seção | O que preencher |
|---|---|
| Diretrizes do cliente | Cores (hex), fontes, logo, estilo, banco de imagens, templates aprovados, faça e evite |
| Especificações | Dimensão, área segura e exportação por formato |
| Fichas das peças | Uma ficha por peça com arte, na ordem do calendário (Texto não tem ficha) |
| Entrega, prazos, checklist | Pasta, nomenclatura, prazos, conferência final |

Campos da ficha por formato:
- **Carrossel:** 6 lâminas, cada uma com título e sub (Capa, Lâminas 2 a 5, Último com CTA), legenda, hashtags, direção de imagem.
- **Reels:** gancho dos 2 primeiros segundos, texto na tela, capa, legenda, hashtags, link do material bruto, orientação de edição.
- **Estático:** título, sub, legenda, hashtags, direção de imagem.
- **Stories:** conteúdo de cada tela, tipo de interação (enquete, pergunta, link).
- **Vídeo:** título do vídeo, texto da thumbnail, legenda, material bruto, orientação de edição.

Toda ficha leva: pilar, redes, template usado e prazo "Arte até".

## 6. Direção de Arte Anúncios

**Quando:** a cada nova campanha ou troca de criativo. **Quem pede:** Tráfego Pago. **Quem executa:** Criativos.

| Seção | O que preencher |
|---|---|
| Pedido de criativos | Código (A01, A02...), campanha, plataforma, formatos, arte até, data de subida |
| Especificações | Dimensões e regras por plataforma (Meta, Google Display, PMax, LinkedIn) |
| Regras de anúncio | Oferta igual à da landing page, um CTA, legível no celular |
| Fichas dos anúncios | Texto na arte, sub, botão, variações, formatos, copy do anúncio, direção, URL de destino |
| Entrega, prazos, checklist | Nomenclatura `A01_meta_1080x1350_v1`, variações A01a, A01b |
| Retorno de performance | CTR, CPL e decisão após 7 dias no ar |

## 7. Plano de Tráfego Pago

**Quando:** mensal. **Quem preenche:** Tráfego Pago. **Capa · 4ª coluna:** Verba de mídia.

Seções: objetivos e KPIs · verba e distribuição por campanha · estrutura de campanhas (nomenclatura Plataforma · Tipo · Tema) · criativos de anúncio (só o controle por código; o briefing vai na Direção de Arte Anúncios) · copy de anúncios · públicos · palavras-chave e negativas · segmentação · mensuração e eventos · padrão de UTM · rotina de otimização · acessos.

## 8. Plano de Tráfego Orgânico

**Quando:** mensal. **Quem preenche:** Tráfego Orgânico. **Capa · 4ª coluna:** Departamento.

Seções: metas orgânicas · clusters e palavras-chave · Conteúdo (pauta de artigos, material rico, padrão de entrega, copy para o Inbound) · Inbound (fluxos de automação, disparos do mês, formulários e lead scoring, saúde da base) · rotina · dependências · onde fica cada coisa.
Não passa por Criativos nem Desenvolvimento. A arte de e-book sai por tarefa avulsa no Notion.

## 9. Landing Page

**Quando:** por projeto. **Quem executa:** Desenvolvimento. **Capa · 4ª coluna:** Conversão principal.

Seções: dados do projeto · meta da página · estrutura e copy (9 seções: Hero, Prova, Dor, Solução, Como funciona, Depoimentos, FAQ, CTA final, Rodapé) · mensagem (promessa, prova, objeções, termos proibidos) · wireframe de referência numerado igual à estrutura · formulário e mapeamento no RD Station · integrações e eventos (GTM, GA4, Google Ads, Meta, RD, WhatsApp, UTM) · requisitos técnicos · checklist de publicação · acessos.
O layout final é feito pelo Desenvolvimento a partir do wireframe, sem Figma do Criativos. Landing page de campanha não tem menu.
