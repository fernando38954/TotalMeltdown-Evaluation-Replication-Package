# Dicionário de dados

CSV públicos: UTF-8, cabeçalho simples, separador vírgula, ponto decimal. Saídas herdadas dos scripts do autor, em `results/pre_post/tabelas` e nas tabelas MEEGA+, usam UTF-8 com BOM e separador ponto e vírgula. O formato de cada arquivo é constante.

| Arquivo | Unidade | Campos e interpretação |
|---|---|---|
| `data/raw_anonymized/pre_post.csv` | Participante | `participant_id`; `prior_knowledge` autodeclarado; `A1–A14` e `B1–B14`, respostas textuais observadas, sem pontuação embutida. |
| `data/raw_anonymized/meega.csv` | Participante | `participant_id`; `Q01–Q31`, ratings inteiros 1–5. Q01–Q26: usabilidade/experiência; Q27: aprendizagem percebida geral; Q28–Q31: objetivos específicos criados para o estudo. |
| `data/raw_anonymized/imi_imms.csv` | Respondente | IDs M da coorte de motivação; itens IMI e IMMS observados; inclusão e motivo de exclusão. Consulte `instruments/motivation_items.csv` para cada código, dimensão e inversão. |
| `data/raw_anonymized/heuristics.csv` | Avaliador × item | `evaluator_id`, `item`, `severity` 0 nenhum problema, 1 estético, 2 baixa prioridade, 3 grave, 4 catastrófico. |
| `data/raw_anonymized/heuristic_form_comments.csv` | Comentário de avaliador | Código H, tipo de fonte e texto. Campos sem resposta não foram fabricados. |
| `data/raw_anonymized/heuristic_chat_feedback.csv` | Unidade qualitativa reconstruída | W: unidade; S: interlocutor; `kind`, `topic`, texto parafraseado e nota de consolidação. Não ligar S a H sem evidência. |
| `data/raw_anonymized/open_feedback.csv` | Participante × pergunta | `question`: liked/difficulty/improvement; `response`; `missing` 1 se vazio; `redaction` registra revisão. |
| `data/raw_anonymized/final_characteristics_aggregated.csv` | Categoria demográfica | `characteristic`, `category`, `n`, `denominator`, `percent`. Nenhuma combinação demográfica por pessoa. |
| `data/processed/core_cleaning_log.csv` | Transformação | Coorte, registro, campo, ação e razão. Não registra nomes nem texto livre de gênero. |
| `data/processed/heuristic_redesign_trace.csv` | Achado priorizado | Correspondência de IDs PT/EN, contagem do artigo, limiares de severidade e resposta de redesign. Reconstrução atual, não ata histórica. |
| `data/processed/logs/*.json` | Participante / sessão saneada | Eventos em ordem e tempos relativos; ver `docs/logs.md` para esquema e limitações. |

`instruments/pre_post_key.json`: 14 pares, enunciados completos, conceito, bloco, gabarito informado pelo autor e vocabulário de alternativas observado na exportação. O vocabulário observado não assegura recuperar todas as alternativas originalmente oferecidas. Comparação: Unicode NFKC, casefold e redução de espaços. Sem aproximação semântica.

`instruments/meega_items.json`: enunciados, nomes curtos, painéis, dimensões e origem de cada item. Não é calculado um escore total MEEGA+ nem validade de escala para os itens específicos.

`instruments/heuristic_items.csv`: 42 enunciados, código português e código do artigo. Correspondências: JG→GP, HJ→NR, ED→EE, CN→EC, AE→EA; IN/MM mantêm sigla.

`instruments/heuristic_guide.pdf` e `.txt`: snapshot do guia de exploração identificado pelo autor como fornecido aos avaliadores. O PDF preserva três imagens; o TXT preserva apenas o texto exportado. `heuristic_guide_metadata.json` registra URL, hashes e limite de correspondência com uma revisão histórica.

`game/pattern-attribute-conceptual.csv`: 63 relações qualitativas fornecidas pelo autor, com sinais `+`, `-`, `=` e chave bibliográfica por padrão. A comparação com os multiplicadores implementados e o estado das referências são documentados em `docs/pattern_traceability.md`. Esses sinais não justificam por si só os pesos numéricos do jogo.

Pré/pós: um ponto por acerto, máximo 14. `change = post_score − pre_score`. Aumentou/diminuiu/empate são classificações de pontuação. `unchanged_at_max` = 14 nos dois momentos. `wrong_right`, `right_wrong`, `right_right`, `wrong_wrong` referem-se às respostas nos pares A/B. Desvios-padrão usam n−1.

Heurística: `any_problem_n` conta severidade >0; `high_severity_n` conta severidade ≥3. São contagens de avaliadores, não uma média de severidade. As contagens da Tabela 3 coincidem com ≥3 e diferem de >0 em vários itens.

Logs: contratos iniciados distintos não significam contratos concluídos. Padrões em registros de conclusão de minigame não demonstram compreensão. Tempo do Notebook só é acumulado em eventos de fechamento, não mede atenção sustentada nem inclui uma consulta aberta sem fechamento.
