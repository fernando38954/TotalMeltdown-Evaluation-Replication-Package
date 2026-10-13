#!/usr/bin/env python3
"""Reproduce the IMI/IMMS study from pseudonymized, unrecoded CSV data.

The main analysis uses IMI = 8-x and IMMS = 6-x for reversed items.
A separate diagnostic implements the manuscript's literal IMMS = 5-x.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path
import statistics


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data/raw_anonymized/imi_imms.csv'
ITEMS = ROOT / 'instruments/motivation_items.csv'
CONFIG = ROOT / 'instruments/motivation_scoring.json'
DEMOGRAPHICS = ROOT / 'data/processed/motivation_demographics_aggregate.csv'


def read_csv(path):
    with Path(path).open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))


def write_csv(path, rows, fields=None):
    with Path(path).open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fields or list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def read_inputs(data_path=DATA, items_path=ITEMS, config_path=CONFIG):
    config = json.loads(Path(config_path).read_text(encoding='utf-8'))
    items = read_csv(items_path)
    data = read_csv(data_path)
    if len(data) != config['expected_n_raw']:
        raise ValueError(f"Expected {config['expected_n_raw']} input records, found {len(data)}.")
    item_ids = [item['item_id'] for item in items]
    if len(item_ids) != 73 or len(set(item_ids)) != 73:
        raise ValueError('Expected 73 uniquely named items: 37 IMI and 36 IMMS.')
    expected_fields = {'participant_id', 'included', 'exclusion_reason', *item_ids}
    if any(set(row) != expected_fields for row in data):
        raise ValueError('Dataset columns differ from the published item dictionary.')
    ids = [row['participant_id'] for row in data]
    if len(set(ids)) != len(ids) or set(ids) != {f'M{i:03d}' for i in range(1, 20)}:
        raise ValueError('Expected unique identifiers M001 through M019.')
    for item in items:
        item['reverse_scored'] = int(item['reverse_scored'])
        item['scale_min'] = int(item['scale_min'])
        item['scale_max'] = int(item['scale_max'])
        if item['reverse_scored'] not in (0, 1):
            raise ValueError(f"Invalid reverse flag for {item['item_id']}.")
        for row in data:
            value = row[item['item_id']]
            if not value.isdigit() or not item['scale_min'] <= int(value) <= item['scale_max']:
                raise ValueError(f"Invalid or missing response: {row['participant_id']}, {item['item_id']}={value!r}")
            row[item['item_id']] = int(value)
    for row in data:
        if row['included'] not in ('0', '1'):
            raise ValueError(f"Invalid inclusion flag for {row['participant_id']}.")
        row['included'] = int(row['included'])
        if row['included'] == 1 and row['exclusion_reason']:
            raise ValueError('Included participants must not have an exclusion reason.')
        if row['included'] == 0 and row['exclusion_reason'] != config['excluded_reason']:
            raise ValueError('Unexpected exclusion reason.')
    included = [row for row in data if row['included']]
    excluded = [row['participant_id'] for row in data if not row['included']]
    if len(included) != config['expected_n_included'] or excluded != config['expected_excluded_ids']:
        raise ValueError('Inclusion flags differ from the documented 18-person cohort.')
    return data, items, config


def recode(value, item, constants):
    return constants[item['instrument']] - value if item['reverse_scored'] else value


def analyze(rows, items, constants, scenario):
    """Scores are computed per participant before between-participant summaries."""
    scored = []
    dimensions = list(dict.fromkeys((i['instrument'], i['dimension']) for i in items))
    dimension_rows = []
    for row in rows:
        for item in items:
            scored.append({'scenario': scenario, 'participant_id': row['participant_id'],
                           'instrument': item['instrument'], 'item_id': item['item_id'],
                           'raw_response': row[item['item_id']],
                           'scored_response': recode(row[item['item_id']], item, constants),
                           'reverse_scored': item['reverse_scored']})
        for instrument, dimension in dimensions:
            selected = [item for item in items if item['instrument'] == instrument and item['dimension'] == dimension]
            values = [recode(row[item['item_id']], item, constants) for item in selected]
            dimension_rows.append({'scenario': scenario, 'participant_id': row['participant_id'],
                                   'instrument': instrument, 'dimension': dimension,
                                   'n_items': len(values), 'score': statistics.mean(values)})
    summaries = []
    for instrument, dimension in dimensions:
        selected = [r for r in dimension_rows if r['instrument'] == instrument and r['dimension'] == dimension]
        values = [r['score'] for r in selected]
        summaries.append({'scenario': scenario, 'instrument': instrument, 'dimension': dimension,
                          'n': len(values), 'n_items': selected[0]['n_items'],
                          'mean': statistics.mean(values), 'sample_sd': statistics.stdev(values),
                          'mean_2dp': f'{statistics.mean(values):.2f}',
                          'sample_sd_2dp': f'{statistics.stdev(values):.2f}'})
    distributions = []
    for item in items:
        values = [recode(r[item['item_id']], item, constants) for r in rows]
        categories = range(min(item['scale_min'], min(values)), max(item['scale_max'], max(values)) + 1)
        for category in categories:
            count = values.count(category)
            distributions.append({'scenario': scenario, 'instrument': item['instrument'],
                                  'item_id': item['item_id'], 'figure_question_id': item['figure_question_id'],
                                  'dimension': item['dimension'], 'scored_category': category,
                                  'n': count, 'n_total': len(values), 'percent': 100 * count / len(values),
                                  'outside_instrument_scale': int(not item['scale_min'] <= category <= item['scale_max'])})
    return scored, dimension_rows, summaries, distributions


def compare_with_article(summaries, config):
    comparison = []
    for row in summaries:
        reported_mean, reported_sd = config['paper_reported_mean_sd'][row['instrument']][row['dimension']]
        comparison.append({'scenario': row['scenario'], 'instrument': row['instrument'],
                           'dimension': row['dimension'], 'n': row['n'],
                           'computed_mean': row['mean'], 'computed_sample_sd': row['sample_sd'],
                           'paper_mean': reported_mean, 'paper_sample_sd': reported_sd,
                           'mean_matches_2dp': int(row['mean_2dp'] == f'{reported_mean:.2f}'),
                           'sample_sd_matches_2dp': int(row['sample_sd_2dp'] == f'{reported_sd:.2f}'),
                           'mean_difference': row['mean'] - reported_mean,
                           'sample_sd_difference': row['sample_sd'] - reported_sd})
    return comparison


def summarize_demographics(path, expected_n):
    """Percentages are regenerated from an aggregate snapshot, without row-level attributes."""
    aggregates = read_csv(path)
    result = []
    for field in dict.fromkeys(r['characteristic'] for r in aggregates):
        selected = [r for r in aggregates if r['characteristic'] == field]
        if sum(int(r['n']) for r in selected) != expected_n:
            raise ValueError(f'Demographic aggregate total differs from {expected_n}: {field}')
        for row in selected:
            count, paper_n = int(row['n']), int(row['paper_reported_n'])
            if int(row['n_total']) != expected_n:
                raise ValueError('Inconsistent demographic denominator.')
            result.append({'characteristic': field, 'category': row['category'], 'n': count,
                           'n_total': expected_n, 'percent': 100 * count / expected_n,
                           'percent_1dp': f'{100 * count / expected_n:.1f}',
                           'paper_reported_n': paper_n,
                           'paper_percent_1dp': f'{100 * paper_n / expected_n:.1f}',
                           'count_matches_article': int(count == paper_n)})
    return result


def plot_distribution(items, rows, constants, output, instrument, figure_number):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.ticker import FuncFormatter
    from matplotlib.patches import Patch

    plt.rcParams.update({'font.family': 'DejaVu Sans', 'svg.hashsalt': 'total-meltdown-motivation'})
    selected = [item for item in items if item['instrument'] == instrument]
    maximum = selected[0]['scale_max']
    neutral = (maximum + 1) // 2
    colors = {1: '#DB6A16', 2: '#E2AE52', 3: '#F3D39B', 4: '#E0DBD1', 5: '#96CC93', 6: '#5C8E59', 7: '#40663E'}
    if maximum == 5:
        colors = {1: '#DB6A16', 2: '#E2AE52', 3: '#E0DBD1', 4: '#96CC93', 5: '#40663E'}
    fig, ax = plt.subplots(figsize=(12, 14.3), constrained_layout=True)
    for y, item in enumerate(selected):
        scores = [recode(row[item['item_id']], item, constants) for row in rows]
        percentages = {category: 100 * scores.count(category) / len(scores) for category in range(1, maximum + 1)}
        negative = 0
        # Neutral is on the positive side, matching the source plots' geometry.
        for category in range(neutral - 1, 0, -1):
            width = percentages[category]
            ax.barh(y, -width, left=-negative, color=colors[category], height=.8, linewidth=0)
            if width >= 10:
                ax.text(-negative - width / 2, y, f'{width:.1f}%', ha='center', va='center', fontsize=7)
            negative += width
        positive = 0
        for category in range(neutral, maximum + 1):
            width = percentages[category]
            ax.barh(y, width, left=positive, color=colors[category], height=.8, linewidth=0)
            if width >= 10:
                ax.text(positive + width / 2, y, f'{width:.1f}%', ha='center', va='center', fontsize=7,
                        color='white' if category == maximum else '#222222')
            positive += width
    starts = [0] + [i for i in range(1, len(selected)) if selected[i]['dimension'] != selected[i - 1]['dimension']]
    ends = starts[1:] + [len(selected)]
    for start, end in zip(starts, ends):
        values = [statistics.mean(recode(row[item['item_id']], item, constants) for item in selected[start:end]) for row in rows]
        label = selected[start]['dimension'].replace('/', '/\n')
        text = f'{label}\nM = {statistics.mean(values):.2f}\nSD = {statistics.stdev(values):.2f}'
        ax.text(-137, (start + end - 1) / 2, text, fontsize=9, ha='center', va='center')
        if start:
            ax.axhline(start - .5, color='#C8C8C8', linewidth=.7)
    ax.set_yticks(range(len(selected)), [item['figure_question_id'] for item in selected], fontsize=8)
    ax.set_xlim(-100, 100)
    ax.set_ylim(len(selected) - .3, -.7)
    ax.xaxis.set_major_formatter(FuncFormatter(lambda value, _: f'{abs(value):g}%'))
    ax.set_xticks(range(-100, 101, 20))
    ax.axvline(0, color='#444444', linewidth=1)
    ax.grid(axis='x', alpha=.15)
    ax.set_axisbelow(True)
    for side in ['left', 'right', 'top']:
        ax.spines[side].set_visible(False)
    fig.suptitle(f'{instrument}: item response distributions (n = {len(rows)})', fontsize=14)
    ax.set_xlabel('Percentage of responses')
    ax.legend(handles=[Patch(facecolor=colors[i], label=str(i)) for i in range(1, maximum + 1)],
              title='Scored Likert category', ncol=maximum, loc='upper center', bbox_to_anchor=(.5, 1.04), frameon=False)
    fig.text(.5, -.012, 'Reverse-coded items. Bar labels shown for segments ≥ 10%; all percentages are in the accompanying CSV.',
             ha='center', fontsize=8)
    for suffix in ['png', 'svg']:
        fig.savefig(output / f'figure_{figure_number:02d}_{instrument.lower()}_distribution.{suffix}',
                    dpi=180, bbox_inches='tight', metadata={'Date': None} if suffix == 'svg' else {})
    plt.close(fig)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data', type=Path, default=DATA)
    parser.add_argument('--items', type=Path, default=ITEMS)
    parser.add_argument('--config', type=Path, default=CONFIG)
    parser.add_argument('--demographics', type=Path, default=DEMOGRAPHICS)
    parser.add_argument('--output', '--output-dir', dest='output', type=Path, default=ROOT / 'results/motivation')
    parser.add_argument('--no-plots', action='store_true', help='Produce tables without importing matplotlib.')
    parser.add_argument('--include-excluded', action='store_true', help='Diagnostic n=19 run; not the manuscript cohort.')
    args = parser.parse_args(argv)
    data, items, config = read_inputs(args.data, args.items, args.config)
    rows = data if args.include_excluded else [row for row in data if row['included']]
    args.output.mkdir(parents=True, exist_ok=True)
    scored, dimensions, summaries, distributions = analyze(rows, items, config['main_reverse_constants'], 'main_corrected')
    hscored, hdimensions, hsummaries, hdistributions = analyze(rows, items, config['paper_literal_reverse_constants'], 'paper_literal_5_minus_x')
    write_csv(args.output / 'scored_items.csv', scored)
    write_csv(args.output / 'participant_dimension_scores.csv', dimensions)
    write_csv(args.output / 'dimension_summary.csv', summaries)
    write_csv(args.output / 'item_distribution.csv', distributions)
    write_csv(args.output / 'paper_literal_dimension_summary.csv', hsummaries)
    write_csv(args.output / 'paper_literal_item_distribution.csv', hdistributions)
    comparison = compare_with_article(summaries + hsummaries, config)
    write_csv(args.output / 'article_comparison.csv', comparison)
    demographics = summarize_demographics(args.demographics, config['expected_n_included'])
    write_csv(args.output / 'table_04_demographics.csv', demographics)
    excluded_rows = [{'participant_id': r['participant_id'], 'included': r['included'], 'exclusion_reason': r['exclusion_reason']} for r in data if not r['included']]
    write_csv(args.output / 'excluded_records.csv', excluded_rows)
    out_of_range = sum(r['scored_response'] < 1 or r['scored_response'] > (7 if r['instrument'] == 'IMI' else 5) for r in hscored)
    result = {'schema_version': 1, 'input_n': len(data), 'analyzed_n': len(rows),
              'excluded_ids': [r['participant_id'] for r in data if not r['included']],
              'include_excluded_diagnostic': args.include_excluded,
              'missing_responses': 0, 'reverse_constants': config['main_reverse_constants'],
              'paper_literal_reverse_constants': config['paper_literal_reverse_constants'],
              'paper_literal_out_of_scale_scored_responses': out_of_range,
              'paper_mean_sd_all_match_main_2dp': all(r['mean_matches_2dp'] and r['sample_sd_matches_2dp'] for r in comparison if r['scenario'] == 'main_corrected'),
              'table_04_demographics_all_counts_match': all(r['count_matches_article'] for r in demographics),
              'source_sha256': {p.relative_to(ROOT).as_posix() if p.is_relative_to(ROOT) else p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                                for p in (args.data.resolve(), args.items.resolve(), args.config.resolve(), args.demographics.resolve())},
              'dimensions': summaries, 'paper_literal_dimensions': hsummaries}
    (args.output / 'summary.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    if not args.no_plots:
        plot_distribution(items, rows, config['main_reverse_constants'], args.output, 'IMI', 6)
        plot_distribution(items, rows, config['main_reverse_constants'], args.output, 'IMMS', 7)
    print(f"IMI/IMMS: {len(data)} input records; {len(rows)} analyzed. Outputs: {args.output}")
    print(f"All manuscript dimension means/SDs match at 2 decimals: {result['paper_mean_sd_all_match_main_2dp']}")
    print(f'Literal IMMS 5-x produces {out_of_range} responses outside the 1–5 scale.')
    return result


if __name__ == '__main__':
    main()
