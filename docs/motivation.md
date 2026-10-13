# Motivation study: IMI and IMMS

This module reproduces the results in Section 7.2 and Figures 6 and 7 of the manuscript. Item responses are preserved in the CSV without recoding. The analysis applies the exclusion specified by the author and calculates scores from these responses.


## Dictionaries and rules

`data/raw_anonymized/imi_imms.csv` has one row per respondent and one column per item. All 1,387 numeric responses, including the excluded record, are complete and within the corresponding scale. The directory name is shared across the package; the codes in the file are surrogate identifiers for the cohort.

`instruments/motivation_items.csv` maps each column to the source's Portuguese item wording, instrument, dimension, original column, reverse-scoring indicator, and the figure's `Q` identifier. Spaces and line breaks were normalized only when matching headers. The source wording was preserved, including any wording errors. For IMMS, the figure order groups the dimensions and differs from the order in which items were presented in the form.

`instruments/motivation_data_dictionary.csv` describes the format of each dataset column. `instruments/motivation_scoring.json` contains the parameters and published values used for comparison.

| Instrument | Dimension | Figure items | Reverse-scored items |
| --- | --- | --- | --- |
| IMI | Interest/Enjoyment | Q1–Q7 | Q3, Q4 |
| IMI | Perceived Competence | Q8–Q13 | Q13 |
| IMI | Effort/Importance | Q14–Q18 | Q15, Q18 |
| IMI | Pressure/Tension | Q19–Q23 | Q19, Q21 |
| IMI | Perceived Choice | Q24–Q30 | Q25, Q26, Q27, Q28, Q30 |
| IMI | Value/Usefulness | Q31–Q37 | None |
| IMMS | Confidence | Q1–Q9 | Q2, Q4, Q6, Q8 |
| IMMS | Attention | Q10–Q21 | Q13, Q14, Q17, Q20, Q21 |
| IMMS | Satisfaction | Q22–Q27 | None |
| IMMS | Relevance | Q28–Q36 | Q34 |

For IMI, the original scale is 1–7 and reverse scoring is `8 - resposta`. For IMMS, the original scale is 1–5 and reverse scoring is `6 - resposta`. For each participant, a dimension score is the arithmetic mean of its recoded items. The mean of these scores and the sample standard deviation across participants are then calculated, using the denominator `n - 1`. The items are not all combined into a single overall score. **Pressure/Tension retains its negative orientation**: lower values indicate less tension.

No responses are imputed, no items are removed, and no cases are filtered by prior knowledge. The program stops if it detects missing, non-integer, or out-of-range values, unexpected fields, or inclusion indicators that are inconsistent with the documented cohort.



## Execution and outputs

From the repository root, with Python 3.10 or later and Matplotlib installed:

```sh
python scripts/motivation.py
```

The default destination is `results/motivation`. To generate tables only, using the Python standard library without Matplotlib:

```sh
python scripts/motivation.py --no-plots
```

The `--output` argument changes the destination directory. For a diagnostic analysis of all 19 cases, use a separate directory:

```sh
python scripts/motivation.py --include-excluded --output results/motivation_unfiltered --no-plots
```

This option does not change the inclusion indicators in the dataset and does not correspond to the article's cohort. The demographic counts remain the snapshot of the main cohort of 18 cases.

The main outputs are:

- `scored_items.csv`: original and recoded responses from the 18 included cases, for auditing.
- `participant_dimension_scores.csv`: individual scores for each dimension.
- `dimension_summary.csv`: means and sample standard deviations, without intermediate rounding.
- `item_distribution.csv`: counts and percentages for every category of each item, with a denominator of 18.
- `article_comparison.csv`: comparison of both scenarios with the published numbers.
- `paper_literal_dimension_summary.csv` and `paper_literal_item_distribution.csv`: a separate diagnostic analysis of the `5 - x` formula, including category 0 when present.
- `table_04_demographics.csv`: source counts, recalculated percentages, and published counts.
- `excluded_records.csv`: an explicit record of the exclusion.
- `summary.json`: analyzed population, parameters, hashes of the distributed inputs, and results.
- `figure_06_imi_distribution.png/.svg` and `figure_07_imms_distribution.png/.svg`: figures regenerated from the main analysis.

The figures use the same item and dimension order as the local scripts, preserve the calculated widths, and keep the neutral category to the right of zero. The layout was redesigned for standalone reading, without aiming for visual identity with the PDF. Percentage labels are shown only for segments of at least 10%; all percentages, including those for smaller segments, are in the CSV files. The labels use ordinary rounding to one decimal place and may not add up to exactly 100%; the counts and bar widths retain the full values.

The tests in `tests/test_motivation.py` check the exclusion, the reverse-scoring endpoints, agreement between the dimensions and the article, preservation of category 0 in the diagnostic analysis, and the distribution denominators:

```sh
python -m unittest discover -s tests -p test_motivation.py
```

These instruments measure retrospective perceptions of motivation. The results do not directly measure learning or sustained attention during the session, in accordance with the limitations described in the article.

