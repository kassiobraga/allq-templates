# Changelog

## v1.3.1 · 23/09/2026

- Gem passa a agir como Analista de Marketing Sênior: propõe temas, títulos de post, pilares, datas relevantes e prazos, em vez de devolver o template com lacunas.
- Colchetes só para dado factual do cliente (números medidos, verba, preços, contatos, links, eventos internos).
- Regra de feriado nacional no calendário e conferência dos spans restantes antes de entregar.

## v1.3.0 · 23/09/2026

- Templates do Gem sem CSS embutido: o visual vem de `allq-templates.css`, publicado em allq.com.br/id-visual/design/. O Gem só copia uma linha do `<head>` e escreve o `<body>` com as classes oficiais. Arquivos caíram pela metade.
- Aviso no `<head>` de cada template do Gem proibindo `<style>` próprio.
- `assets/allq-templates.css` gerado a cada push. Sempre que mudar, subir no site junto com o timbrado.
- Instruções do Gem com checklist obrigatório e template anexado na conversa.

## v1.2.0 · 23/09/2026

- Pasta `gem/`: versão dos templates para o Gem, com o timbrado por link (allq.com.br) em vez de embutido. O Gem passa a devolver o documento completo em HTML.
- O Drive recebe os 9 templates em HTML mais o Guia em PDF. Os PDFs de prévia ficam só no repositório.
- Timbrado novo exportado do Affinity (81 KB, antes 306 KB), sem máscara nem pattern, abre igual no Chrome e no Affinity. Templates de trabalho caíram de ~450 KB para ~110 KB.
- Guia com a seção "Como entregar o documento em HTML".

## v1.1.0 · 23/09/2026

- Sincronização automática com o Google Drive via GitHub Action a cada push na `main`.
- Validação bloqueante: template que estoura o A4, fica abaixo de 55% ou tem travessão não é publicado.
- Guia dos Templates passa a ser publicado como PDF, gerado do `GUIA-GEMINI.md`.

## v1.0.0 · 23/09/2026

Primeira versão definitiva, validada com o Administrativo.

- 9 templates A4: Planejamento Semestral, Planejamento Mensal, Calendário Editorial, Calendário Editorial Trimestral, Direção de Arte Redes Sociais, Direção de Arte Anúncios, Plano de Tráfego Pago, Plano de Tráfego Orgânico e Landing Page.
- Timbrado All.Q com pontilhado só no cabeçalho, embutido em cada arquivo para abrir offline.
- Capa com faixa azul de 4 colunas e índice "Neste documento". Páginas internas com barra azul de identificação.
- Departamentos no lugar de nomes, com cor e ícone do Notion: Administrativo, Sucesso do Cliente, Desenvolvimento, Tráfego Pago, Criativos, Tráfego Orgânico e Design.
- 6 formatos com cor fixa: Estático azul, Carrossel roxo, Reels laranja, Vídeo vermelho, Stories rosa, Texto verde.
- Grade de posts com fundo da linha na cor do formato. Dia com duas peças aparece dividido na diagonal no calendário trimestral.
- Ficha de peça no padrão do calendário CRP Tecnologia, com legenda e hashtags.
- Direção de Arte Anúncios separada da Direção de Arte Redes Sociais.
- Landing Page com wireframe de referência em desktop e mobile.
