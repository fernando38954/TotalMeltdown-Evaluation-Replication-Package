# Pattern–attribute traceability

The article author supplied this table as a commented LaTeX fragment on 2026-10-13. It is recorded in [63 machine-readable cells](../game/pattern-attribute-conceptual.csv). It records the authors' conceptual model and stated sources, separate from the numerical game configuration.

| Pattern | FS | PE | CO | IC | RE | SE | MA | FL | SA | Author's reference |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MVC | = | = | - | + | = | = | + | = | = | Bi2018 |
| Layered | = | - | - | = | + | + | + | = | = | Bi2018 |
| Client-Server | = | = | = | + | - | + | - | + | = | Bi2018 |
| Pipe Filter | = | + | + | - | - | = | + | = | = | Bi2018 |
| Microservices | = | - | = | = | = | = | + | + | = | Li2021 |
| Microkernel | = | - | = | = | + | = | + | + | = | Liu2021 |
| Event-driven | = | + | - | = | = | = | + | = | = | Cabane2024 |

`+` = positive impact; `-` = negative impact; `=` = neutral or balanced impact. FS = Functional Suitability; PE = Performance Efficiency; CO = Compatibility; IC = Interaction Capability; RE = Reliability; SE = Security; MA = Maintainability; FL = Flexibility; SA = Safety. Names and signs follow the supplied table. Each row's citation is repeated across its nine cells; the original does not specify a passage or page per cell.

## Bibliographic attribution and verification limits

All four supplied records are preserved in [`game/pattern-references.bib`](../game/pattern-references.bib). The notes below distinguish author-supplied attribution from limited primary-source checks and unavailable independent retrieval. No cited key lacks a supplied bibliographic entry.

- **Bi2018**: Bi, Liang and Tang, *Architecture Patterns, Quality Attributes, and Design Contexts: How Developers Design with Them*, APSEC 2018. Publisher indexed metadata identifies the study and DOI, and describes relationships among patterns, attributes and contexts. The complete cell-level mapping was not audited against full text. [IEEE record](https://ieeexplore.ieee.org/abstract/document/8719565/), [DOI](https://doi.org/10.1109/APSEC.2018.00019).
- **Li2021**: Li et al., *Understanding and addressing quality attributes of microservices architecture: A Systematic literature review*, Information and Software Technology 131, 106449. Publisher indexed metadata and abstract identify the review and discuss attributes and trade-offs. These checks do not certify the nine signs or numerical weights. [Publisher record](https://www.sciencedirect.com/science/article/pii/S0950584920301993), [DOI](https://doi.org/10.1016/j.infsof.2020.106449).
- **Cabane2024**: Cabane and Farias, *On the impact of event-driven architecture on performance: An exploratory study*, Future Generation Computer Systems 153, 52–69. The publisher page was inaccessible. The author's accessible 2022 manuscript of this title reports lower resource consumption and better response times for the monolithic comparator in its studied application. This check does not establish an unconditional positive EDA performance sign; the supplied `+` is preserved for review. The manuscript is not claimed to be identical to the final publication. [Author-hosted manuscript](https://kleinnerfarias.github.io/pdf/manuscript/eda-2022.pdf), [DOI](https://doi.org/10.1016/j.future.2023.10.021).
- **Liu2021**: Liu, Buquan; Wu, Chunguang; and Guo, Hao, *A Survey of Operating System Microkernel*, IEEE ICAA 2021, pp. 743–748, June 2021. The author supplied the complete BibTeX entry and [DOI](https://doi.org/10.1109/ICAA53760.2021.00135). Independent DOI/IEEE retrieval was unavailable, so this record is identified as `author_supplied_complete_bibtex;doi_lookup_unavailable`; its full text has not been independently confirmed. The title concerns operating-system microkernels. Support for translating that context to the application-architecture pattern represented in the game, and for the nine attributed signs, has not been independently verified.

Lookups took place on 2026-10-13. Direct retrieval encountered a browser-verification page at IEEE and HTTP 403 responses at ScienceDirect. No full paper text is redistributed.


