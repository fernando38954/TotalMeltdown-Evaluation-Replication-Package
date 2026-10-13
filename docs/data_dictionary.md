# Data dictionary

Public CSV files: UTF-8, a single header row, comma separator, and decimal point. Outputs inherited from the author's scripts, in `results/pre_post/tabelas` and the MEEGA+ tables, use UTF-8 with BOM and a semicolon separator. Each file uses a consistent format.

| File | Unit | Fields and interpretation |
|---|---|---|
| `data/raw_anonymized/pre_post.csv` | Participant | `participant_id`; self-reported `prior_knowledge`; `A1–A14` and `B1–B14`, observed textual responses without embedded scores. |
| `data/raw_anonymized/meega.csv` | Participant | `participant_id`; `Q01–Q31`, integer ratings 1–5. Q01–Q26: usability/experience; Q27: overall perceived learning; Q28–Q31: specific objectives created for the study. |
| `data/raw_anonymized/imi_imms.csv` | Respondent | M IDs from the motivation cohort; observed IMI and IMMS items; inclusion and reason for exclusion. See `instruments/motivation_items.csv` for each code, dimension, and reverse scoring. |
| `data/raw_anonymized/heuristics.csv` | Evaluator × item | `evaluator_id`, `item`, `severity`: 0 no problem, 1 cosmetic, 2 low priority, 3 major, 4 catastrophic. |
| `data/raw_anonymized/heuristic_form_comments.csv` | Evaluator comment | H code, source type, and text. Unanswered fields were not fabricated. |
| `data/raw_anonymized/heuristic_chat_feedback.csv` | Reconstructed qualitative unit | W: unit; S: speaker; `kind`, `topic`, paraphrased text, and consolidation note. Do not link S to H without evidence. |
| `data/raw_anonymized/open_feedback.csv` | Participant × question | `question`: liked/difficulty/improvement; `response`; `missing` 1 if empty; `redaction` records review. |
| `data/raw_anonymized/final_characteristics_aggregated.csv` | Demographic category | `characteristic`, `category`, `n`, `denominator`, `percent`. No demographic combinations at the individual level. |
| `data/processed/core_cleaning_log.csv` | Transformation | Cohort, record, field, action, and reason. Does not record names or free-text gender responses. |
| `data/processed/heuristic_redesign_trace.csv` | Prioritized finding | PT/EN ID mapping, article count, severity thresholds, and redesign response. A current reconstruction, rather than a historical record. |
| `data/processed/logs/*.json` | Participant / sanitized session | Ordered events and relative times; see `docs/logs.md` for the schema and limitations. |

`instruments/pre_post_key.json`: 14 pairs, complete question statements, concept, block, the answer key supplied by the author, and the vocabulary of answer choices observed in the export. The observed vocabulary does not guarantee recovery of all originally offered choices. Comparison: Unicode NFKC, casefold, and whitespace normalization. No semantic matching.

`instruments/meega_items.json`: question statements, short names, panels, dimensions, and the origin of each item. No total MEEGA+ score or scale validity is calculated for the specific items.

`instruments/heuristic_items.csv`: 42 question statements, Portuguese code, and article code. Mappings: JG→GP, HJ→NR, ED→EE, CN→EC, AE→EA; IN/MM retain their abbreviations.

`instruments/heuristic_guide.pdf` and `.txt`: snapshot of the exploration guide identified by the author as having been provided to the evaluators. The PDF preserves three images; the TXT preserves only the exported text. `heuristic_guide_metadata.json` records the URL, hashes, and limits on correspondence with a historical revision.

`game/pattern-attribute-conceptual.csv`: 63 qualitative relationships supplied by the author, with signs `+`, `-`, `=` and a bibliographic key for each pattern. Comparison with the implemented multipliers and the status of the references are documented in `docs/pattern_traceability.md`. These signs alone do not justify the game's numerical weights.

Pre/post: one point per correct answer, maximum 14. `change = post_score − pre_score`. Increased/decreased/tied are score classifications. `unchanged_at_max` = 14 at both time points. `wrong_right`, `right_wrong`, `right_right`, and `wrong_wrong` refer to responses in the A/B pairs. Standard deviations use n−1.

Heuristics: `any_problem_n` counts severity >0; `high_severity_n` counts severity ≥3. These are counts of evaluators, rather than mean severity ratings. The counts in Table 3 match ≥3 and differ from >0 for several items.

Logs: distinct contracts started do not imply contracts completed. Patterns in minigame completion records do not demonstrate understanding. Notebook time is accumulated only on close events; it does not measure sustained attention or include a consultation that remains open without a close event.
