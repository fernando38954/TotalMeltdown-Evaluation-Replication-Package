# Motivation study: IMI and IMMS

This analysis generates the IMI and IMMS figures for Section 7.2 of the manuscript. The input file `data/raw_anonymized/imi_imms.csv` contains the **18 participants used in the article**, with 37 IMI responses and 36 IMMS responses per participant. The final respondent has already been removed from this dataset; the script does not exclude another row.

The item dictionary in `instruments/motivation_items.csv` maps each data column to its instrument, dimension, original Portuguese wording, reverse-scoring flag, and figure question number. IMMS questions are grouped by dimension in the figure, so their figure numbers differ from the original form order.

## Scoring

| Instrument | Dimension | Figure items | Reverse-scored figure items |
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

IMI uses a 1–7 scale and reverse scoring is `8 - response`. IMMS uses a 1–5 scale and reverse scoring is `6 - response`. The historical scoring script uses `6 - response`. The `5 - response` formula printed in the manuscript would generate values outside the 1–5 scale and does not reproduce the reported dimension scores. The correct formulas above reproduce the reported means and standard deviations.

For each participant, a dimension score is the arithmetic mean of its recoded items. The group mean and sample standard deviation are then calculated across the 18 participant scores, with the standard deviation denominator `n - 1`. No overall score is calculated across dimensions. **Pressure/Tension keeps its negative orientation:** lower scores indicate less tension.

The script rejects missing, non-integer, or out-of-range responses. It does not impute values or select participants by prior knowledge. `instruments/motivation_scoring.json` records the scoring parameters and article values.

## Run and outputs

From the repository root, after installing the dependencies:

```sh
python scripts/motivation.py
```

Outputs are written to `results/motivation`:

- `figure_06_imi_distribution.png` and `.svg`: IMI response distributions.
- `figure_07_imms_distribution.png` and `.svg`: IMMS response distributions.
- `dimension_summary.csv`: group means and sample standard deviations.
- `participant_dimension_scores.csv`: dimension scores by anonymous participant code.
- `scored_items.csv`: original and recoded item responses.
- `item_distribution.csv`: counts and percentages by item and scored category.
- `summary.json`: cohort size, scoring constants, and dimension summaries.

Use `--output DIRECTORY` to choose another destination. Use `--no-plots` to calculate tables with the Python standard library alone.

The figures retain the original item and dimension order and put the neutral category to the right of zero. Bar widths use exact percentages; labels are shown only for segments of at least 10% and are rounded to one decimal place. The CSV contains all percentages. Rounding may prevent displayed labels from adding up to exactly 100%.

These questionnaires measure retrospective perceptions of motivation. They do not directly measure learning or sustained attention during the session.
