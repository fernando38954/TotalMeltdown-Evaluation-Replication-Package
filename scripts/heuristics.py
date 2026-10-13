"""Full severity matrix and counts under explicitly distinct thresholds."""
import argparse
import statistics
from collections import Counter
from pathlib import Path
from common import ROOT, read_csv, write_csv, write_json

def run(output):
    records=read_csv(ROOT/'data/raw_anonymized/heuristics.csv')
    items=read_csv(ROOT/'instruments/heuristic_items.csv')
    summary=[]
    assert len({(r['evaluator_id'],r['item']) for r in records})==len(records)
    for item in items:
        values=[int(r['severity']) for r in records if r['item']==item['item']]
        assert len(values)==5 and all(0<=v<=4 for v in values)
        c=Counter(values)
        summary.append({**item,'n':5,**{f'severity_{k}_n':c[k] for k in range(5)},'any_problem_n':sum(v>0 for v in values),'high_severity_n':sum(v>=3 for v in values),'median_severity':statistics.median(values),'max_severity':max(values)})
    write_csv(Path(output)/'full_inspection.csv',summary)
    write_json(Path(output)/'summary.json',{'evaluators_n':5,'items_n':len(items),'ratings_n':len(records),'high_severity_definition':'severity >= 3','no_problem_definition':'severity = 0'})
    print(f'Heuristics: {len(items)} items, {len(records)} severity ratings')
    return summary

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,default=ROOT/'results/heuristics');a=p.parse_args();run(a.output)
