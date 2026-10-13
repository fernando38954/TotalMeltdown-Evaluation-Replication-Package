# Estudo de motivação: IMI e IMMS

Este módulo reproduz os resultados da Seção 7.2 e das Figuras 6 e 7 do manuscrito. As respostas aos itens são preservadas sem recodificação no CSV. A análise aplica a exclusão indicada pelo autor e calcula os escores a partir dessas respostas.


## Dicionários e regras

`data/raw_anonymized/imi_imms.csv` possui uma linha por respondente e uma coluna por item. Todas as 1.387 respostas numéricas, incluindo o registro excluído, estão completas e dentro da escala correspondente. O nome do diretório é compartilhado pelo pacote; os códigos do arquivo são identificadores substitutos da coorte.

`instruments/motivation_items.csv` associa cada coluna ao enunciado português da fonte, ao instrumento, à dimensão, à coluna original, ao indicador de inversão e ao identificador `Q` da figura. Espaços e quebras de linha foram normalizados apenas durante a correspondência entre cabeçalhos. Os enunciados da fonte foram preservados, inclusive eventuais erros de redação. No IMMS, a ordem da figura reúne as dimensões e difere da ordem de apresentação do formulário.

`instruments/motivation_data_dictionary.csv` descreve o formato de cada coluna do dataset. `instruments/motivation_scoring.json` contém os parâmetros e os valores publicados utilizados na comparação.

| Instrumento | Dimensão | Itens da figura | Itens invertidos |
| --- | --- | --- | --- |
| IMI | Interest/Enjoyment | Q1–Q7 | Q3, Q4 |
| IMI | Perceived Competence | Q8–Q13 | Q13 |
| IMI | Effort/Importance | Q14–Q18 | Q15, Q18 |
| IMI | Pressure/Tension | Q19–Q23 | Q19, Q21 |
| IMI | Perceived Choice | Q24–Q30 | Q25, Q26, Q27, Q28, Q30 |
| IMI | Value/Usefulness | Q31–Q37 | Nenhum |
| IMMS | Confidence | Q1–Q9 | Q2, Q4, Q6, Q8 |
| IMMS | Attention | Q10–Q21 | Q13, Q14, Q17, Q20, Q21 |
| IMMS | Satisfaction | Q22–Q27 | Nenhum |
| IMMS | Relevance | Q28–Q36 | Q34 |

No IMI, a escala original é 1–7 e a inversão é `8 - resposta`. No IMMS, a escala original é 1–5 e a inversão é `6 - resposta`. Para cada participante, o escore de uma dimensão é a média aritmética de seus itens já recodificados. Em seguida, calculam-se a média desses escores e o desvio padrão amostral entre participantes, com denominador `n - 1`. Não se agrega todos os itens em um único escore global. **Pressure/Tension mantém orientação negativa**: valores menores indicam menor tensão.

Não se imputam respostas, não se eliminam itens e não se filtram casos por conhecimento prévio. O programa interrompe a execução se detectar valores ausentes, não inteiros, fora da escala, campos inesperados ou indicadores de inclusão incompatíveis com a coorte documentada.



## Execução e saídas

Na raiz do repositório, com Python 3.10 ou superior e Matplotlib instalado:

```sh
python scripts/motivation.py
```

O destino padrão é `results/motivation`. Para gerar somente tabelas com a biblioteca padrão de Python, sem Matplotlib:

```sh
python scripts/motivation.py --no-plots
```

O argumento `--output` altera a pasta de destino. Para uma análise diagnóstica com os 19 casos, use uma pasta distinta:

```sh
python scripts/motivation.py --include-excluded --output results/motivation_unfiltered --no-plots
```

Essa opção não altera os indicadores de inclusão no dataset nem corresponde à coorte do artigo. As contagens demográficas continuam sendo o snapshot da coorte principal com 18 casos.

As saídas principais são:

- `scored_items.csv`: respostas originais e recodificadas dos 18 casos incluídos, para auditoria.
- `participant_dimension_scores.csv`: escores individuais de cada dimensão.
- `dimension_summary.csv`: médias e desvios padrão amostrais, sem arredondamento intermediário.
- `item_distribution.csv`: contagens e percentuais para todas as categorias de cada item, com denominador 18.
- `article_comparison.csv`: comparação de ambos os cenários com os números publicados.
- `paper_literal_dimension_summary.csv` e `paper_literal_item_distribution.csv`: diagnóstico separado da fórmula `5 - x`, incluindo categoria 0 quando presente.
- `table_04_demographics.csv`: contagens da fonte, percentuais recalculados e contagens publicadas.
- `excluded_records.csv`: registro explícito da exclusão.
- `summary.json`: população analisada, parâmetros, hashes dos insumos distribuídos e resultados.
- `figure_06_imi_distribution.png/.svg` e `figure_07_imms_distribution.png/.svg`: figuras regeneradas a partir da análise principal.

As figuras usam a mesma ordem dos itens e dimensões dos scripts locais, preservam as larguras calculadas e mantêm a categoria neutra à direita do zero. A diagramação foi refeita para leitura independente, sem pretensão de identidade visual com o PDF. Mostram-se rótulos percentuais apenas nos segmentos de pelo menos 10%; todos os percentuais, incluindo segmentos menores, estão nos CSVs. Os rótulos usam arredondamento comum a uma casa decimal e podem não somar exatamente 100%; as contagens e larguras das barras mantêm os valores completos.

Os testes `tests/test_motivation.py` verificam a exclusão, os extremos da inversão, a concordância das dimensões com o artigo, a preservação das categorias 0 no diagnóstico e os denominadores das distribuições:

```sh
python -m unittest discover -s tests -p test_motivation.py
```

Esses instrumentos medem percepções retrospectivas de motivação. Os resultados não medem diretamente aprendizagem ou atenção sustentada durante a sessão, conforme os limites descritos no artigo.
