# TotalMeltdown — Evaluation Replication Package

This package contains the data, applied instruments, and scripts needed to reproduce four outputs from the TotalMeltdown evaluation:

1. The article's heuristic findings and redesign table.
2. The IMI and IMMS response-distribution figures.
3. The adapted MEEGA+ response-distribution figure.
4. The descriptive analysis of the paired pre/post knowledge tests.

The analyses use local CSV inputs and do not require access to Google forms or private participant records. Historical instruments and participant responses retain their original Portuguese wording; the documentation and figure labels are in English.

## Run the analyses

Use Python 3.13, or a compatible Python environment. The delivered outputs were generated with Python 3.13.12 and Matplotlib 3.10.6.

From the package root, install the plotting and spreadsheet-library dependencies used by the included scoring engines:

```sh
python -m pip install -r requirements.txt
```

Then run the four scripts:

```sh
python scripts/heuristics.py
python scripts/motivation.py
python scripts/meega.py
python scripts/pre_post.py
```

Each script writes its outputs to the corresponding directory under `results/`. The included pre/post and MEEGA+ scoring engines are used directly by their scripts; no shared `common.py`, master pipeline, manifest, or test suite is needed. The same commands work in PowerShell, Linux, and macOS when `python` selects the intended environment.

Use `--output PATH` to choose another output directory. For tables only, use `--no-plots` with the motivation script or `--no-figures` with the pre/post and MEEGA+ scripts.

## Outputs

| Analysis | Main deliverables |
|---|---|
| Heuristics | The nine-row article table in CSV, LaTeX, and Markdown, plus the complete 42-item severity summary. |
| IMI/IMMS | Two figures in PNG/SVG, item distributions, participant dimension scores, and dimension means and sample standard deviations. |
| Adapted MEEGA+ | `results/meega/meega_items.png` and `.svg`, together with item distributions and descriptive statistics. |
| Pre/post | `results/pre_post/resultados.json`, a readable summary, participant scores, item transitions, group summaries, CSV/LaTeX tables, and three descriptive figures. |

The delivered outputs are included in `results/` and can be regenerated with the commands above. Public input CSV files use UTF-8 and comma separators. Tables inherited from the pre/post and MEEGA+ scoring engines use semicolon separators; see [the data dictionary](docs/data_dictionary.md).

## Data and scoring

The three evaluations use independent cohorts: five heuristic evaluators, 18 motivation respondents, and 44 final-evaluation participants. Codes do not identify the same people across studies.

- **Heuristics:** Table 3 counts evaluators who assigned severity 3 or 4 to each prioritized finding. Counts are recalculated from the individual ratings; problem descriptions and redesign responses come from the supplied traceability table.
- **IMI/IMMS:** the distributed CSV already contains the 18 included respondents. The excluded nineteenth response is absent and is not excluded again. Reverse-scored items use `8 − x` for IMI and `6 − x` for IMMS. Scores are averaged within each participant and dimension; standard deviations use `n − 1`. Lower Pressure/Tension is more favorable.
- **MEEGA+:** 31 items are summarized individually on a 1–5 scale. Q28–Q31 are study-specific learning-objective items. No overall validated MEEGA+ score is assigned.
- **Pre/post:** each correct answer receives one point, out of 14. The supplied answer key is used without inference from response frequencies. All 44 paired records are retained, including ceiling scores and declines.

The pre/post means are 12.5909 and 12.9318; 17 participants increased, 20 were unchanged, and 7 decreased. The motivation figures reproduce the ten reported dimension means and sample standard deviations. The reported motivation gender counts differ from the retained source counts; neither the observations nor demographic categories are adjusted to force agreement with the manuscript.

## Blind-review distribution

The review files use participant codes, aggregate demographics, and sanitized logs. Researcher references in feedback and identifying copyright-holder names are replaced by blind-review markers; the remaining license terms are retained. Historical consent texts already omit names, institutions, and contact details. Original attribution notices are retained privately for the eventual identified release.

**Use the supplied blind-review ZIP for review.** It contains the current files without `.git`, commit history, local caches, or private backups. The working repository's existing Git history and personal-account remote are not anonymized by changes to the current files and must not be supplied to reviewers.

This preparation checks the distributed files for direct author and participant identifiers. Study codes and linked free text are pseudonymous records; the package does not claim that all possible external reidentification has been ruled out.

## Interpretation and supporting material

The analyses are descriptive and exploratory. Forms A and B assess corresponding concepts through different scenarios, and their empirical equivalence in difficulty was not established. The results do not establish causal learning gains, retention, or thematic prevalence in open comments.

The [study protocols](docs/study_protocols.md), [cleaning notes](docs/cleaning.md), [motivation methods](docs/motivation.md), and [pattern traceability](docs/pattern_traceability.md) describe the study materials and their limits. The evaluator guide, consent texts, conceptual pattern–attribute table, game contents, and sanitized logs are retained as supporting material. Log analysis and game-content generation are outside the four scripts listed here.
