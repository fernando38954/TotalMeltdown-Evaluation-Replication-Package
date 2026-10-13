#!/usr/bin/env python3
"""Generate IMI and IMMS figures and dimension scores for the 18-person cohort."""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
import statistics


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data/raw_anonymized/imi_imms.csv'
ITEMS = ROOT / 'instruments/motivation_items.csv'
CONFIG = ROOT / 'instruments/motivation_scoring.json'


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
    if len(data) != config['expected_n']:
        raise ValueError(f"Expected {config['expected_n']} input records, found {len(data)}.")
    item_ids = [item['item_id'] for item in items]
    if len(item_ids) != 73 or len(set(item_ids)) != 73:
        raise ValueError('Expected 73 uniquely named items: 37 IMI and 36 IMMS.')
    expected_fields = {'participant_id', 'included', 'exclusion_reason', *item_ids}
    if any(set(row) != expected_fields for row in data):
        raise ValueError('Dataset columns differ from the published item dictionary.')
    ids = [row['participant_id'] for row in data]
    if len(set(ids)) != len(ids) or set(ids) != {f'M{i:03d}' for i in range(1, config['expected_n'] + 1)}:
        raise ValueError('Expected unique identifiers M001 through M018.')
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
        if row['included'] != '1' or row['exclusion_reason']:
            raise ValueError('The input must contain only the already selected 18 participants.')
        row['included'] = int(row['included'])
    return data, items, config


def recode(value, item, constants):
    return constants[item['instrument']] - value if item['reverse_scored'] else value


def analyze(rows, items, constants):
    """Scores are computed per participant before between-participant summaries."""
    scored = []
    dimensions = list(dict.fromkeys((i['instrument'], i['dimension']) for i in items))
    dimension_rows = []
    for row in rows:
        for item in items:
            scored.append({'participant_id': row['participant_id'],
                           'instrument': item['instrument'], 'item_id': item['item_id'],
                           'raw_response': row[item['item_id']],
                           'scored_response': recode(row[item['item_id']], item, constants),
                           'reverse_scored': item['reverse_scored']})
        for instrument, dimension in dimensions:
            selected = [item for item in items if item['instrument'] == instrument and item['dimension'] == dimension]
            values = [recode(row[item['item_id']], item, constants) for item in selected]
            dimension_rows.append({'participant_id': row['participant_id'],
                                   'instrument': instrument, 'dimension': dimension,
                                   'n_items': len(values), 'score': statistics.mean(values)})
    summaries = []
    for instrument, dimension in dimensions:
        selected = [r for r in dimension_rows if r['instrument'] == instrument and r['dimension'] == dimension]
        values = [r['score'] for r in selected]
        summaries.append({'instrument': instrument, 'dimension': dimension,
                          'n': len(values), 'n_items': selected[0]['n_items'],
                          'mean': statistics.mean(values), 'sample_sd': statistics.stdev(values),
                          'mean_2dp': f'{statistics.mean(values):.2f}',
                          'sample_sd_2dp': f'{statistics.stdev(values):.2f}'})
    distributions = []
    for item in items:
        values = [recode(r[item['item_id']], item, constants) for r in rows]
        categories = range(item['scale_min'], item['scale_max'] + 1)
        for category in categories:
            count = values.count(category)
            distributions.append({'instrument': item['instrument'],
                                  'item_id': item['item_id'], 'figure_question_id': item['figure_question_id'],
                                  'dimension': item['dimension'], 'scored_category': category,
                                  'n': count, 'n_total': len(values), 'percent': 100 * count / len(values)})
    return scored, dimension_rows, summaries, distributions


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
    parser.add_argument('--output', '--output-dir', dest='output', type=Path, default=ROOT / 'results/motivation')
    parser.add_argument('--no-plots', action='store_true', help='Produce tables without importing matplotlib.')
    args = parser.parse_args(argv)
    data, items, config = read_inputs(args.data, args.items, args.config)
    rows = data
    args.output.mkdir(parents=True, exist_ok=True)
    scored, dimensions, summaries, distributions = analyze(rows, items, config['reverse_constants'])
    write_csv(args.output / 'scored_items.csv', scored)
    write_csv(args.output / 'participant_dimension_scores.csv', dimensions)
    write_csv(args.output / 'dimension_summary.csv', summaries)
    write_csv(args.output / 'item_distribution.csv', distributions)
    result = {'analyzed_n': len(rows), 'reverse_constants': config['reverse_constants'],
              'dimensions': summaries}
    (args.output / 'summary.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    if not args.no_plots:
        plot_distribution(items, rows, config['reverse_constants'], args.output, 'IMI', 6)
        plot_distribution(items, rows, config['reverse_constants'], args.output, 'IMMS', 7)
    print(f"IMI/IMMS: {len(data)} input records; {len(rows)} analyzed. Outputs: {args.output}")
    return result


if __name__ == '__main__':
    main()
