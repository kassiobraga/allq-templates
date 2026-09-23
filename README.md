# All.Q · Templates de Planejamento

Fonte da verdade dos documentos de planejamento da All.Q Agência. Toda alteração nasce aqui, vira versão nova e só depois é copiada para o Google Drive, que alimenta os Gems do Gemini.

## Fluxo

1. Ajuste pedido ao Administrativo.
2. Alteração feita em `gerador/`, templates regerados e validados.
3. Nova versão registrada no `CHANGELOG.md` (v1.1, v1.2...).
4. PDFs e `GUIA-GEMINI.md` substituídos na pasta do Drive.

O Drive é só leitura. Ninguém edita template fora deste repositório.

## Estrutura

| Pasta | Conteúdo |
|---|---|
| `templates/` | HTML de trabalho. Abrir no Chrome, preencher, Ctrl+P, Salvar como PDF com "Gráficos de segundo plano" marcado |
| `pdf/` | Prévia em PDF de cada template, a mesma que vai para o Drive |
| `gerador/` | Código que gera os HTML. Editar aqui, nunca direto no HTML |
| `GUIA-GEMINI.md` | Guia de uso para os Gems e para o time |

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
pip install playwright && playwright install chromium
python3 gerador/gerar.py         # gera templates/*.html
python3 gerador/validar.py       # altura A4, preenchimento, travessão, tags
python3 gerador/exportar_pdf.py  # gera pdf/*.pdf
```

Regra de validação: nenhuma página passa de 1123 px (A4), nenhuma fica abaixo de 55% de preenchimento, zero travessão, zero `border-left` colorido.

## Nome do arquivo de entrega

`Nome Completo do Cliente - Tipo de Material - Período.html`
Exemplo: `Acecar Auto Parts - Calendário Editorial - Outubro 2026.html`
