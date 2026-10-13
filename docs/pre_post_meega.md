# Pre/post, MEEGA+, and comments

The Google snapshot of 44 participants was compared with the local export used in the article. All analytical values and IDs matched; timestamps and upload links were not used in the comparison. The export order and IDs 1–44 match; the public codes are P001–P044.

The `pre_post_engine.py` and `meega_engine.py` engines were reused from scripts supplied in the local sources, with minimal adaptation for PNG/SVG graphical outputs. The public adapters read sanitized CSV files and preserve the answer key and original calculation. Location fields in the outputs point to the distributed CSV, rather than cells in a private spreadsheet.

The answer key was found in `analise_reproduzivel/gabarito.json`, with an explicit note that it had been supplied by the author. The package preserves both the official wording and the exported wording. It is not a reconstruction based on the class's response patterns. The observed answer choices do not replace the complete original form: choices never selected may be missing.

Forms A/B: corresponding content, different scenarios, 14 possible correct answers. All pairs and both self-reported prior-knowledge groups are included. No participant was excluded for a ceiling score. Psychometric equivalence between the forms has not been demonstrated. The analyses are descriptive, without inferential testing, normalized gain, regression, or causal attribution.

MEEGA+: 31 items rated 1–5, with counts by category, mean, median, and sample SD for each item. The specific objectives Q28–Q31 are study items, rather than a validated MEEGA+ scale. The reproduction does not invent an overall score or attribute measured learning to a response about perceptions.

Final comments: all three fields are retained even when empty. `results/feedback/coverage.csv` reproduces coverage of 35/44, 32/44, and 31/44. The article's analysis selects accounts to illustrate problems and suggestions. No codebook for thematic coding with independent evaluators was found; the package does not claim theme prevalence or agreement.
