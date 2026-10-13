# Protocols reconstructed from the manuscript

This document describes the procedures reported in [`article.pdf`](article.pdf), with references to the article's numbered pages, and identifies materials subsequently supplied by the author. It was reconstructed on October 13, 2026, to make the package understandable. **This document is not the original approved or implemented protocol**, an original informed consent form, a historical exploration guide, or a historical record of the consolidation process. The consent texts and the guide snapshot are preserved separately, together with their provenance.

The article describes two versions: V1 underwent heuristic inspection; V2 was used in the motivation study and final evaluation. There are three independent convenience cohorts, with voluntary participation. The package codes are specific to each cohort: H for heuristics, M for motivation, and P for the final evaluation. They must not be linked across studies, and the participants must not be assumed to be the same people.

## Consent and data handling

According to §3.3, p4, the objectives, procedures, and data collection were presented before participation, with agreement to the informed consent form (ICF/TCLE). The exports contain consent fields. The author supplied the three full texts while this package was being prepared; they are preserved in `instruments/consent/heuristics.md`, `instruments/consent/motivation.md`, and `instruments/consent/final_evaluation.md`. These are texts supplied by the author, rather than signed forms recovered from each participant. No committee reference number or ethics approval was supplied; these details are neither inferred nor invented.

In the final evaluation, names in the log files enabled matching with the questionnaire, so collection was not anonymous according to the article. The consent text for this evaluation describes anonymous collection. This is a discrepancy between the consent text and the historical account in the manuscript; the package preserves both, without rewriting the consent text or concluding that ethics approval was obtained. The article reports that identifiers were replaced with codes before analysis and that only de-identified data are publicly distributed. The package preserves the matching within this cohort without distributing the name-to-code key. Personal fields and original files are kept outside the public repository; demographic characteristics are supplied in aggregate form.

## 1. Heuristic inspection — V1, N=5

**Participants (§5, p5–6).** Five master's students in Computing with professional software development experience. Four had approximately two to four years of experience; the fifth also worked as a Computing Education researcher and had teaching experience.

**Sequence described in the article:**

1. Provide introductory training in AHJED heuristics and a game exploration guide.
2. Have each evaluator examine V1 independently and record problems and severities according to the adopted AHJED procedure.
3. Review and consolidate overlapping findings together with the evaluators.
4. Prioritize findings of severity 3 or 4 when planning the redesign.

The article does not report session duration, a mandatory order of screens or activities, the format of consolidation meetings, or an additional rule for resolving disagreements. The consent text supplied by the author anticipates **30 to 40 minutes of total participation**, which is not an observed measure of gameplay time. The author identified the document preserved in `instruments/heuristic_guide.pdf` as the exploration guide supplied to the evaluators. The separate AHJED training material and contemporaneous consolidation records were not located.

**Tasks in the guide supplied by the author, in the order in which they appear:**

1. **Consult the Notebook:** locate and open the resource, and find the technical description of a pattern, such as Microservices or Event-Driven.
2. **Hire a developer:** access the Recruitment Fair, compare attributes, and hire someone.
3. **Learn a new pattern:** access the Study Session, work through the explanation, and select an architecture.
4. **Manage resources:** consult the Developer Panel, the team's point distribution, and the information about the ongoing contract.
5. **Execute a contract:** interpret the requirements, select and drag the pattern and developers, and sign the contract.

The guide also describes the three interface regions, recruitment/study/contract events, selection and removal interactions, and the attribute-combination formula. The PDF preserves three pages and three images; `instruments/heuristic_guide.txt` contains the exported Portuguese text, and `instruments/heuristic_guide_metadata.json` records its provenance. The original guide's terms are retained, without retroactively correcting the scientific terminology or adapting the document to match the manuscript. The author's identification establishes which document the author recognizes as the guide; the date and bytes of the current snapshot do not prove that it is identical to the version delivered during the historical evaluation. The task list also does not prove that all evaluators completed every task in a mandatory order.

**Recovered material.** The 42 administered items are in `instruments/heuristic_items.csv`; the 210 individual ratings are in `data/raw_anonymized/heuristics.csv`. The ID map translates ED→EE, JG→GP, HJ→NR, and AE→EA to the names used in the article; IN remains IN. The file `data/processed/heuristic_redesign_trace.csv` maps the nine items in Table 3 to the redesign responses described in the text, separately calculating positive ratings and ratings ≥3. It is a consolidation reconstructed now, with provenance, rather than a historical record of the discussion with the evaluators.

## 2. Motivation study — V2, N=18 included

**Participants and context (§7, p8–10).** Undergraduate and graduate students in Computing, with at least basic familiarity with Software Engineering and development. Voluntary recruitment through online Computing groups. Remote administration through a form.

**Five parts, in the reported order:**

1. Explanation of the experiment: objectives, consent, gameplay instructions, and evaluation procedure.
2. Demographic questionnaire: education, gaming habits, and prior experience with Software Engineering concepts.
3. Free-play session of approximately **20 to 30 minutes**, with instructions to explore the game's three quarters because they introduce different mechanics.
4. Motivation evaluation: completion of IMI and IMMS. The text presents them in this order but does not specify whether there was counterbalancing or other randomization.
5. Optional open-ended comments about the experience.

The reported instructions emphasized that there was no correct way to play, that the evaluation focused on the experience rather than individual performance, that the mechanics could be explored freely, and that the evaluation should continue even if all challenges were not completed. They recommended an environment with few distractions and, preferably, headphones. Remote administration did not control equipment, connectivity, or distractions. The consent text anticipates **30 to 60 minutes of total participation**; this interval does not replace the 20 to 30 minutes of gameplay described in the manuscript.

**Reconstructed filter.** The supplied export has 19 records. The author's current instruction states that the final respondent was not considered. The package identifies this record as `M019`, marks it `included=false`, and retains its items to make the exclusion auditable, without the respondent's personal data. No other reason for exclusion was supplied. The 18 included records match the historical analysis spreadsheet item by item. This filter must not be inferred from the quality of the ratings or extended to the other cohorts.

**Instruments and scoring (§7.2, p8–9).** IMI: 37 items, responses 1–7, grouped into Interest/Enjoyment, Perceived Competence, Effort/Importance, Pressure/Tension, Perceived Choice, and Value/Usefulness. IMMS: 36 items, responses 1–5, grouped in the administered instrument/figure into Confidence, Attention, Satisfaction, and Relevance. The exact mapping of wording, dimensions, and reverse-scored items is in `instruments/motivation_items.csv`; the canonical order of another version of the instruments must not replace this map.

The article describes reverse scoring of negative items before analysis, the arithmetic mean of the items in each dimension for each participant, and summaries using the mean and **sample** standard deviation of these scores. Pressure/Tension remains a negatively oriented dimension: a low value is favorable. `instruments/motivation_scoring.json` distinguishes `8−x` for IMI and the corrected `6−x` for IMMS from the `5−x` printed in the article. The literal analysis is a documented sensitivity analysis; the publication must not be silently altered. Missing or invalid values halt the current analysis, without imputation; this rule belongs to the package, since the manuscript does not specify a missing-data policy.

## 3. Final evaluation — V2, N=44

**Participants and context (§8, p10).** A Computer Engineering class with 44 undergraduate and graduate students, predominantly undergraduates. Classroom administration. Table 5 reports aggregate characteristics.

**Sequence described in the article:**

1. Informed consent.
2. Demographic questionnaire.
3. Knowledge pre-test: **Form A, 14 items**.
4. Brief introduction to TotalMeltdown.
5. Gameplay for **up to 50 minutes**, with the option to stop earlier. Fifty minutes must not be assigned to everyone as an observed duration.
6. Immediately after gameplay, the post-test: **Form B, 14 items**.
7. Player experience questionnaire.
8. Open-ended responses.

The consent text anticipates **45 to 70 minutes of total participation**. This interval includes the research activities and does not replace the gameplay limit of up to 50 minutes reported in the article.

### Knowledge tests

The forms address corresponding concepts through different scenarios. The authors reviewed content and intended difficulty before administration; **they did not establish empirical equivalence of difficulty between A and B**. Each correct answer receives one point, for a maximum total of 14. All 44 participants supplied complete paired responses. The answer key and the mapping between exported responses and items are in `instruments/pre_post_key.json`; the data are in `data/raw_anonymized/pre_post.csv`.

The article examines totals per participant, correct-answer counts per corresponding pair, incorrect→correct/correct→incorrect transitions, and changes by self-reported prior knowledge. The groups are none/basic (N=30) and intermediate/advanced (N=14). Unknown or missing responses halt the current analysis; they are not resolved by selecting the most frequent answer. The export does not automatically recover all unselected distractors from the original form.

### Experience questionnaire

The instrument has 31 statements with five response categories. It combines items adapted from MEEGA+, one general perceived-learning item, and four custom items for the game's educational objectives. The original social-interaction items were omitted because the activity was individual. The map in `instruments/meega_items.json` records Q01–Q09 as usability, Q10–Q26 as player experience, and Q27–Q31 as perceived learning. Q28–Q31 address identification of relevant attributes, advantages and disadvantages of patterns, analysis of trade-offs, and architectural suitability.

The reported analysis is item-based: the distribution across the five categories and the proportion selecting 4 or 5. **No overall MEEGA+ quality classification was assigned.** Do not convert this adapted questionnaire into a validated overall score without further justification.

### Logs and participation measures

All 44 participants have logs matched to their questionnaires. §8.2, p10, describes session metadata and events with timestamps, categories, and event-specific fields. The package distributes processed logs using the same code as the final evaluation, and documents their interpretation in `docs/logs.md`.

| Reported measure | Operation | Limitation |
|---|---|---|
| Distinct contracts started | Count distinct names in contract-start events per participant; repeated names count once | Starting does not prove completion. |
| Patterns with recorded contact | Count distinct patterns in minigame-completion events per participant; repeated patterns count once | The record proves contact with the activity, not understanding of the concept. |
| Notebook use | Count closing events and sum the duration reported in those events | Without a closing event, no duration is observed under this rule. Do not assume reading or learning. |

The article records Notebook use for 42 participants; the two without closing events are omitted from Figure 12. The article's highlighted P40 case corresponds to the observation of ten closing events and 10.38 cumulative minutes. This example contextualizes a participant comment, without estimating the Notebook's learning effect. The vertical displacement of points in the figure serves only to reduce overlap.

Additional events include quiz responses, correctness, and response time, as well as quarter summaries with finances, hires, and duration. The availability of these events does not imply that all of them were used in the article's analyses.

### Open-ended comments

§8.6, p13–14, reports a descriptive examination of the responses to contextualize the numbers and identify improvements. The selected excerpts are examples, with no reported formal coding of prevalence. The quotations were translated from Portuguese into English in the article and retain the codes from that evaluation. Reproduction must distinguish the original comment, translation, and researcher's interpretation.

## Scope of the reconstruction

The analyses described are descriptive and exploratory. The studies did not include a control group, random allocation to game versions, or delayed assessment. Do not attribute causality to the pre/post increase or interpret differences between A/B items as established conceptual gains or losses. High initial scores limit observable increases, and the prior-knowledge groups are small and unequal. Positive perceptions, puzzle completion, and recorded duration do not equate to transferable learning.

The recovered JSON content documents the game's representation. A Godot source file was located, and its provenance is recorded in `game/source-provenance.json`, but its correspondence with the evaluated V2 build has not been established; the complete project and builds are not distributed in the evaluation package. The three consent texts and the document identified as the evaluators' guide are supplied by the author. The separate AHJED training material and contemporaneous evaluator consolidation records were not located.

The conceptual table supplied by the author, preserved in `game/pattern-attribute-conceptual.csv`, contains 63 qualitative signs and reference keys for each pattern. `docs/pattern_traceability.md` distinguishes this table from the game's multipliers. Bibliographic entries have been supplied for all four keys, including `Liu2021`, *A Survey of Operating System Microkernel*. Independent access to this source was unavailable; the supplied bibliographic identification does not establish verified support for every sign, or for transferring the operating-system microkernel concept to the game's application-architecture context. The signs and the direction of the weights do not match for every relationship, and no specific justification was supplied for converting each relationship into a quantitative weight. These sources improve traceability without, on their own, establishing the validity of all scholarly links or the weight-calibration model. These limitations are preserved in `docs/article_requirements.md`; no new document is presented as a missing original.

