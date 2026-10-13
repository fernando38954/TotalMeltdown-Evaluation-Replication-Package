"""Reproduce the article's nine-row heuristic table from the observed ratings."""

import argparse
import csv
import json
import statistics
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read_csv(path):
    with Path(path).open(encoding="utf-8-sig", newline="") as stream:
        # The edited traceability file has a trailing empty column. Ignore it.
        return [
            {key: value for key, value in row.items() if key}
            for row in csv.DictReader(stream)
        ]


def write_csv(path, rows):
    with Path(path).open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def latex_escape(value):
    substitutions = {
        "\\": r"\textbackslash{}", "&": r"\&", "%": r"\%",
        "$": r"\$", "#": r"\#", "_": r"\_", "{": r"\{",
        "}": r"\}", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}",
    }
    return "".join(substitutions.get(character, character) for character in str(value))


def markdown_escape(value):
    return str(value).replace("|", r"\|").replace("\r", " ").replace("\n", " ")


def run(output):
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    records = read_csv(ROOT / "data/raw_anonymized/heuristics.csv")
    items = read_csv(ROOT / "instruments/heuristic_items.csv")
    trace = read_csv(ROOT / "data/processed/heuristic_redesign_trace.csv")
    evaluator_ids = {row["evaluator_id"] for row in records}
    ratings = {}
    seen = set()
    for row in records:
        key = (row["evaluator_id"], row["item"])
        if key in seen:
            raise ValueError(f"Duplicate heuristic rating: {key}")
        seen.add(key)
        severity = int(row["severity"])
        if severity not in range(5):
            raise ValueError(f"Severity must be between 0 and 4: {key}")
        ratings.setdefault(row["item"], []).append(severity)

    summary = []
    for item in items:
        values = ratings.get(item["item"], [])
        if len(values) != len(evaluator_ids):
            raise ValueError(f"Incomplete ratings for {item['item']}")
        frequencies = Counter(values)
        summary.append({
            **item,
            "n": len(values),
            **{f"severity_{level}_n": frequencies[level] for level in range(5)},
            "any_problem_n": sum(value > 0 for value in values),
            "high_severity_n": sum(value >= 3 for value in values),
            "median_severity": statistics.median(values),
            "max_severity": max(values),
        })
    if set(ratings) != {item["item"] for item in items}:
        raise ValueError("Ratings and instrument item IDs do not match")

    # The trace provides the article's row selection and wording, not its counts.
    # Counts are recomputed from observations; the historical count columns
    # deliberately are not used as analytical inputs.
    table = []
    for row in trace:
        values = ratings[row["raw_item"]]
        table.append({
            "ID": row["paper_id"],
            "Identified problem": row["identified_problem"],
            "Reported by": f"{sum(value >= 3 for value in values)}/{len(values)}",
            "Redesign response": row["redesign_response"],
        })
    if not table:
        raise ValueError("The heuristic article table has no rows")

    write_csv(output / "article_table3.csv", table)
    write_csv(output / "full_inspection.csv", summary)

    headers = list(table[0])
    markdown = [
        "# Heuristic evaluation: article Table 3", "",
        "Reported by counts evaluators who assigned severity 3 or 4 to the issue.",
        "The issue descriptions and redesign responses come from the supplied traceability table.",
        "", "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    markdown.extend(
        "| " + " | ".join(markdown_escape(row[header]) for header in headers) + " |"
        for row in table
    )
    (output / "article_table3.md").write_text("\n".join(markdown) + "\n", encoding="utf-8")

    latex = [
        r"% Requires \usepackage{longtable} in the containing document.",
        r"\begin{longtable}{p{0.06\textwidth}p{0.28\textwidth}p{0.10\textwidth}p{0.43\textwidth}}",
        r"\caption{Heuristic issues identified and corresponding redesign responses.}\label{tab:heuristic-redesign}\\",
        r"\hline",
        " & ".join(r"\textbf{" + latex_escape(header) + "}" for header in headers) + r" \\",
        r"\hline", r"\endfirsthead", r"\hline",
        " & ".join(r"\textbf{" + latex_escape(header) + "}" for header in headers) + r" \\",
        r"\hline", r"\endhead",
    ]
    latex.extend(
        " & ".join(latex_escape(row[header]) for header in headers) + r" \\"
        for row in table
    )
    latex.extend([
        r"\hline", r"\end{longtable}",
        r"\noindent\footnotesize Reported by: evaluators assigning severity 3 or 4, divided by the number of evaluators.",
    ])
    (output / "article_table3.tex").write_text("\n".join(latex) + "\n", encoding="utf-8")

    metadata = {
        "evaluators_n": len(evaluator_ids),
        "items_n": len(items),
        "ratings_n": len(records),
        "article_table_rows_n": len(table),
        "high_severity_definition": "severity >= 3",
        "no_problem_definition": "severity = 0",
    }
    (output / "summary.json").write_text(
        json.dumps(metadata, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Heuristics: {len(items)} items, {len(records)} ratings; article Table 3: {len(table)} rows")
    return summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "results/heuristics")
    args = parser.parse_args()
    run(args.output)
