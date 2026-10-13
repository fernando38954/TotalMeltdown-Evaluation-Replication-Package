# TotalMeltdown — Reproducibility Package

Deidentified data, applied instruments, study materials, and executable analyses supporting **“TotalMeltdown: a Digital Educational Game for Teaching Software Architectural Trade-offs.”** This repository reproduces the descriptive analyses from the distributed files. After installing the dependencies, it runs offline without access to private spreadsheets or participant identities.

Package version: **0.2.1, 2026-10-13**. The supplied manuscript is preserved in [`docs/article.pdf`](docs/article.pdf). Original study files were read without modification. Applied instruments, consent forms, the evaluator guide, and participant responses retain their original Portuguese wording.

## Quick start

Use **Python 3.13**. The delivered analyses were verified with Python 3.13.12, NumPy 2.4.2, Matplotlib 3.10.6, and openpyxl 3.1.5.

Run these commands from the repository root.

**Windows**

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-lock.txt
.\.venv\Scripts\python.exe scripts/verify.py --manifest
.\.venv\Scripts\python.exe scripts/run_all.py --output results_replay
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

**Linux or macOS**

```sh
python3.13 -m venv .venv
.venv/bin/python -m pip install -r requirements-lock.txt
.venv/bin/python scripts/verify.py --manifest
.venv/bin/python scripts/run_all.py --output results_replay
.venv/bin/python -m unittest discover -s tests -v
```

`results/` contains the delivered outputs. `--output results_replay` writes a separate reproduction run; without `--output`, the pipeline regenerates `results/`. Add `--no-figures` to generate tables and summaries only. Verify the release manifest **before** regenerating delivered outputs: environment differences can affect figure serialization and execution metadata.

`requirements.txt` pins the three direct dependencies. `requirements-lock.txt` also pins the indirect dependencies used for the delivered outputs. Calculations are deterministic and involve no random sampling. Figure appearance can vary with operating system and fonts. The [GitHub workflow](.github/workflows/reproduce.yml) installs dependencies, checks release integrity, regenerates results, and runs tests; remote execution of that workflow has not been verified in this preparation.

## Repository contents

```text
data/
  raw_anonymized/     observed responses, public IDs, and aggregate demographics
  processed/         sanitized logs, cleaning records, and reconstructed traceability
instruments/         item wording, answer key, scoring maps, consent forms, evaluator guide
game/                content JSON, implemented weights, qualitative model, and references
scripts/             analyses, verification, and release packaging
results/             CSV/LaTeX tables, JSON summaries, and PNG/SVG figures
docs/                manuscript, methods, data dictionary, provenance, and coverage audit
tests/               scoring, reverse-coding, and exclusion checks
.github/             automated reproduction workflow
CITATION.cff         package citation metadata
MANIFEST.sha256.json release file checksums
```

Input CSV files use UTF-8 and comma separators. Tables inherited from the authors' pre/post and MEEGA+ scripts use semicolon separators; see the [data dictionary](docs/data_dictionary.md). Existing analysis engines were retained with adapters for the public inputs, preserving the supplied answer key and calculations.

| Study | Distributed data | Analytical sample |
|---|---|---:|
| AHJED heuristic evaluation | 42 items × 5 evaluators; severity ratings 0–4 | 5 |
| IMI/IMMS motivation study | 37 + 36 items; 19 records with an explicit exclusion flag | 18 |
| Final evaluation | Paired 14-item tests, 31-item adapted MEEGA+, and open feedback | 44 |
| Final-evaluation logs | 44 sanitized files preserving 1,747 events | 44 |

These are independent cohorts. H01–H05, M001–M019, and P001–P044 do not establish participant correspondence across studies. Within the final evaluation, P040 corresponds to P40 in the manuscript and links that participant's feedback, questionnaires, and log.

## Cleaning and verified results

The last IMI/IMMS respondent, M019, remains in the distributed input with `included=0` and is excluded from the main analysis following the author's explicit instruction. The 18 retained item matrices exactly match the historical local export, which was already filtered. No additional exclusion is applied to that export, and no empirical reason for the exclusion is inferred.

Repeated quotations and administrative messages in the heuristic chat were consolidated. Blank feedback fields remain missing. A nonstandard free-text gender response in the final evaluation is summarized as `Other (free-text)`, retaining the participant. The [cleaning documentation](docs/cleaning.md) explains these decisions and the distinction between participant identifiers removed from the data and researcher contacts preserved in historical consent forms.

The numerical analyses passed **89 comparisons against the manuscript and 10 tests**. Repeated complete runs in the same environment produced identical result files. Key reproduced quantities include:

- Mean pre/post scores: **12.5909 → 12.9318**, out of 14; 17 participants increased, 20 were unchanged, and 7 decreased.
- All ten IMI/IMMS dimension means and sample standard deviations match the published values to two decimal places.
- Median of 9 distinct contracts started; 37/44 participants with records covering all seven patterns; 42/44 with Notebook closure events.
- P040: ten Notebook closures and 10.38495 recorded minutes.
- All nine Table 3 counts match the number of severity ratings ≥3. Counts of any positive severity are also retained.

See [`results/verification.json`](results/verification.json), [`results/article_comparison.csv`](results/article_comparison.csv), and the individual analysis folders for the outputs and comparisons.

## Evaluator guide and pattern traceability

The [heuristic evaluator guide](instruments/heuristic_guide.pdf), identified by the author as the document supplied to evaluators, is included as an unchanged Google Docs PDF export with its three illustrations. A [plain-text export](instruments/heuristic_guide.txt) and [provenance record](instruments/heuristic_guide_metadata.json) are also included. It describes the interface, contract mechanics, and five evaluation tasks: consult the Notebook, recruit a developer, learn a pattern, inspect resource management, and execute a contract. The supplied snapshot has not independently been matched to a document revision from the evaluation date.

The author also supplied a qualitative pattern–attribute table and bibliographic entries. The [traceability documentation](docs/pattern_traceability.md) preserves the seven patterns, nine attributes, `+`/`−`/`=` directions, and citation keys alongside the game's implemented multipliers and JSON locations.

Qualitative directions do not determine the exact numerical weights. Several supplied directions differ from the implementation, including Event-Driven Architecture's Compatibility and Maintainability. Those differences are recorded without changing the game configuration. All four bibliographic entries are now supplied, including **`Liu2021`**, *A Survey of Operating System Microkernel*, for the Microkernel row. Bibliographic attribution is complete; support for each assigned sign and applicability across contexts have not been independently verified.

## Documented discrepancies and remaining gaps

The package preserves the observations and records discrepancies:

1. **IMMS reverse coding:** the manuscript prints `5 − x`; the historical script uses `6 − x`, which preserves the 1–5 scale and reproduces the published results. A separate diagnostic run applies the printed formula and retains its seven zero values.
2. **Table 4:** the manuscript reports 13 men, 4 women, and 1 nonbinary participant; the retained source records contain 12, 5, and 1. Source counts are preserved.
3. **Figure 11:** its caption, legend, and panel references do not fully match the displayed image. Regenerated figures identify the five applied response categories and item wording.
4. **Game version:** the local manuscript content assigns EDA/Maintainability a multiplier of 0.8, whereas the recovered source archive assigns 1.4. The exact commit/build used in each evaluation remains unverified.
5. **Final-study consent:** the historical text describes anonymous collection, while the manuscript describes linking logs through participant names before deidentification. Both historical descriptions are preserved.

The three consent forms, the evaluator guide, the author's qualitative traceability table, and all four cited bibliographic records are included. Remaining gaps concern the **separate AHJED training materials**, **contemporaneous consolidation records**, **complete original answer options for Forms A/B**, and **justifications for exact numerical weights**. Independent verification of scholarly support for individual signs remains incomplete. The evaluated builds also need immutable identifiers. The recovered game source is a separate artifact documented in [`game/README.md`](game/README.md).

The [article coverage audit](docs/article_requirements.md) identifies which promises are covered or partial. The [study protocols](docs/study_protocols.md) distinguish manuscript procedures from recovered materials. Supporting historical documentation remains in Portuguese. Analyses are descriptive: they do not establish causality, equivalent difficulty of Forms A/B, retention, or thematic prevalence in open feedback.

## GitHub and release use

Use this folder as the repository root. Preserve `.github`, deidentified inputs, instruments, and results; keep original spreadsheets and the nominal linkage key outside the repository. Release packaging excludes private sources, caches, environments, and Git metadata. `.gitattributes` preserves release bytes so checkout does not invalidate checksums.

Update `CITATION.cff` with the repository URL and DOI when assigned. Its author entries identify the researchers responsible for the supplied study materials. [`LICENSE.md`](LICENSE.md) records the recovered game license and the absence of an explicit license for the analytical package; it does not extend the game license automatically to data, third-party instruments, or the manuscript.

To rebuild the manifest, ZIP archive, and archive checksum:

```sh
python scripts/package_release.py --output ../TotalMeltdown-reproducibility.zip
```

When inputs, scoring rules, or outputs change, record the change in `CHANGELOG.md`, rerun the relevant analyses and tests, and regenerate the release manifest. Version and document additions to the literature mapping or evaluated-build evidence.
