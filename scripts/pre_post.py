"""Replay the author's existing scoring engine using the public CSV snapshot."""
import argparse
from pathlib import Path
import pre_post_engine as engine
from common import ROOT, read_csv, write_json

def run(output, figures=True):
    config = engine.load_key(ROOT/'instruments/pre_post_key.json')
    source = read_csv(ROOT/'data/raw_anonymized/pre_post.csv')
    headers = [config['metadata_headers'][k] for k in ('id','consent','knowledge')]
    keys = []
    for item in config['items']:
        for form, prefix in [('pre','A'),('post','B')]:
            headers.append(item[form]['header'])
            keys.append(f'{prefix}{item["pair"]}')
    rows = [[r['participant_id'],config['accepted_consent'],r['prior_knowledge']] + [r[k] for k in keys] for r in source]
    records, scored, _, blank = engine.score_rows(headers, rows, config)
    # Locations refer to the distributed public CSV, not a reconstructed Excel.
    for rec in records:
        rec['source_row'] = next(i for i,r in enumerate(source,2) if r['participant_id']==rec['participant_id'])
    for rec in scored:
        row=next(i for i,r in enumerate(source,2) if r['participant_id']==rec['participant_id'])
        rec['source_cell']=f'pre_post.csv:row={row};column={rec["item"]}'
    result = engine.analyze(records, config)
    output=Path(output);output.mkdir(parents=True,exist_ok=True)
    engine.write_tables(output,records,scored,result,config)
    engine.write_summary(output,result,config)
    write_json(output/'resultados.json', result)
    if figures:
        engine.plot_results(output,result,config)
    assert blank==0
    print(f'Pre/post: {len(records)} participants, {len(scored)} scored responses')
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path,default=ROOT/'results/pre_post')
    p.add_argument('--no-figures',action='store_true')
    a=p.parse_args();run(a.output,not a.no_figures)
