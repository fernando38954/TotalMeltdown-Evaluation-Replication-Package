# Filtering and de-identification

The package retains the observations needed to repeat the analyses. `raw_anonymized` means an extraction of the observed values with identifiers removed, rather than the original, unmodified export. The complete spreadsheets and the mapping between names and codes are kept outside the repository.

| Source | Input | Analysis | Decision |
|---|---:|---:|---|
| AHJED | 5 evaluators, 42 items | 5, 210 ratings | No evaluator excluded. Severity ratings 0–4 preserved. |
| IMI/IMMS | 18 responses in Google | 18 | Last response excluded at the author's explicit instruction. The local export already contains only the 18 included responses. |
| Pre/post | 44 complete pairs | 44 | No exclusion for ceiling scores, declining scores, or small changes. |
| Adapted MEEGA+ | 44 responses, 31 items | 44, 1,364 ratings | No automatic exclusion for identical responses. |
| Final comments | 132 fields | Answered and missing fields preserved | Empty fields do not become negative ratings. |
| Heuristic discussion | Transcript of the discussion with the author | 10 paraphrased units | Repeated messages, quotations in replies, isolated punctuation, and administrative messages do not duplicate evidence. |


The codes `H01–H05`, `M001–M018`, and `P001–P044` belong to independent cohorts. P001 corresponds to P1 in the article's final evaluation, and P040 to P40. Individuals are not linked across the three evaluations. The codes S1–S3 identify only distinct speakers in the supplied discussion, without assuming their identities among the five evaluators.

Form timestamps, participant names and phone numbers, upload links, and log filenames were removed. Detailed demographics at the individual level were replaced with aggregate counts; prior knowledge by participant was retained only to reproduce the test groupings. In the logs, absolute times and session identifiers are replaced with relative offsets. 


The free-text gender response that does not match the standardized categories was summarized as `Other (free-text)`, following Table 5. It was not converted into a gender identity or used to exclude the participant. Missing values, invalid values, and zero are distinct.

A repeated response does not establish that a participant is duplicated. Unique study IDs and consent were checked during ingestion. The routines stop the analysis when unexpected quantitative values occur. There is no imputation, removal based on undesired results, inference of the answer key from response frequencies, or adjustment of data to match the article.

Open-ended comments were reviewed for names, contact details, and personal links. A researcher first name in one final-evaluation response was replaced with `[researcher]`, and its `redaction` field records `researcher_name_redacted`. The numerical responses were not changed. The discussion paraphrases are not verbatim transcripts and must not be used as direct quotations. Form comments are retained as source text. The editorial synthesis does not constitute thematic coding with frequency counts or agreement between evaluators.
