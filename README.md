# All.Q · Templates de Planejamento

Fonte da verdade dos documentos de planejamento da All.Q Agência. Toda alteração nasce aqui, vira versão nova e só depois é copiada para o Google Drive, que alimenta os Gems do Gemini.

## Fluxo

1. Ajuste pedido ao Administrativo.
2. Alteração feita em `gerador/` ou no `GUIA-GEMINI.md`, com nova versão no `CHANGELOG.md`.
3. Push na `main`. A Action **Sincronizar com o Google Drive** regera os templates, valida, exporta os PDFs, grava de volta no repositório e envia ao Drive os 9 templates HTML da pasta `gem/` e o Guia em PDF (10 arquivos, o limite de conhecimento do Gem).
4. Se a validação falhar, nada vai para o Drive.

O Drive é só leitura. Ninguém edita template fora deste repositório. Os arquivos do Drive mantêm o mesmo ID a cada atualização, então os Gems continuam apontando para eles.

## Configuração da sincronização (uma vez)

Secrets em Settings > Secrets and variables > Actions:

| Secret | Valor |
|---|---|
| `DRIVE_FOLDER_ID` | ID da pasta "All.Q · Templates de Planejamento" no Drive |
| `DRIVE_TOKEN` | JSON gerado por `rclone authorize "drive"` com a conta dona da pasta |

Para rodar sem push: aba Actions > Sincronizar com o Google Drive > Run workflow.

## Estrutura

| Pasta | Conteúdo |
|---|---|
| `templates/` | HTML de trabalho. Abrir no Chrome, preencher, Ctrl+P, Salvar como PDF com "Gráficos de segundo plano" marcado |
| `gem/` | Mesmos templates com o timbrado por link, mais leves, para o Gem copiar e preencher. É o que vai para o Drive |
| `pdf/` | Prévia em PDF de cada template |
| `assets/` | Timbrado leve, publicado em allq.com.br/id-visual/design/timbrado-a4-cabecalho.svg |
| `gerador/` | Código que gera os HTML. Editar aqui, nunca direto no HTML |
| `GUIA-GEMINI.md` | Guia de uso para os Gems e para o time, publicado no Drive como PDF |
| `.github/workflows/` | Sincronização automática com o Drive |

## Templates

| Template | Departamento que usa | Período |
|---|---|---|
| Planejamento Semestral | Administrativo | Semestre |
| Planejamento Mensal | Administrativo | Mês |
| Calendário Editorial | Sucesso do Cliente | Mês |
| Calendário Editorial Trimestral | Sucesso do Cliente | Trimestre |
| Direção de Arte Redes Sociais | Criativos | Mês |
| Direção de Arte Anúncios | Criativos, pedido pelo Tráfego Pago | Por campanha |
| Plano de Tráfego Pago | Tráfego Pago | Mês |
| Plano de Tráfego Orgânico | Tráfego Orgânico | Mês |
| Landing Page | Desenvolvimento | Por projeto |

## Gerar e validar

```bash
pip install playwright markdown && playwright install chromium
python3 gerador/gerar.py         # gera templates/*.html
python3 gerador/validar.py       # altura A4, preenchimento, travessão, tags
python3 gerador/exportar_pdf.py  # gera pdf/*.pdf
python3 gerador/guia_pdf.py      # gera pdf/Guia dos Templates de Planejamento.pdf
```

Regra de validação: nenhuma página passa de 1123 px (A4), nenhuma fica abaixo de 55% de preenchimento, zero travessão, zero `border-left` colorido.

## Nome do arquivo de entrega

`Nome Completo do Cliente - Tipo de Material - Período.html`
Exemplo: `Acecar Auto Parts - Calendário Editorial - Outubro 2026.html`
