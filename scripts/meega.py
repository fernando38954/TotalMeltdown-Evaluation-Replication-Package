"""Adapted MEEGA+: item distributions, without an invented overall scale."""
import argparse
import json
from pathlib import Path
import meega_engine as engine
from common import ROOT, read_csv, write_json

def run(output,figures=True):
    config=json.loads((ROOT/'instruments/meega_items.json').read_text(encoding='utf-8'))
    rows=read_csv(ROOT/'data/raw_anonymized/meega.csv')
    assert len({r['participant_id'] for r in rows})==len(rows)
    responses=[]
    for n,r in enumerate(rows,2):
        for item in config['items']:
            v=int(r[item['item']]);assert 1<=v<=5
            responses.append({'participant_id':r['participant_id'],'item':item['item'],'rating':v,'source_cell':f'meega.csv:row={n};column={item["item"]}'})
    summary=engine.resumir(config['items'],responses)
    output=Path(output);output.mkdir(parents=True,exist_ok=True)
    engine.salvar_tabelas(output,config['items'],responses,summary)
    write_json(output/'summary.json',summary)
    if figures:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        from matplotlib.patches import Patch
        plt.rcParams.update({'svg.hashsalt':'totalmeltdown-meega-v1','font.family':'DejaVu Sans'})
        colors=['#d66a24','#e3ae52','#dcdcd5','#93c990','#40663e']
        fig,ax=plt.subplots(figsize=(11,11.8))
        fig.subplots_adjust(left=.50,right=.98,top=.94,bottom=.09)
        left=[0.0]*len(summary)
        for k,c in enumerate(colors,1):
            vals=[r[f'pct_{k}'] for r in summary]
            ax.barh(range(len(summary)),vals,left=left,color=c,edgecolor='white',height=.76)
            for y,(v,l) in enumerate(zip(vals,left)):
                if v>=7:ax.text(l+v/2,y,f'{v:.1f}',ha='center',va='center',fontsize=7,color='white' if k==5 else '#222222')
            left=[l+v for l,v in zip(left,vals)]
        ax.set_yticks(range(len(summary)),[f'{r["item"]}  {r["label"]}' for r in summary],fontsize=8)
        ax.invert_yaxis();ax.set_xlim(0,100);ax.set_xlabel('Responses (%)');ax.spines[['top','right']].set_visible(False)
        fig.suptitle(f'Adapted MEEGA+ item responses (n={len(rows)})',fontsize=15)
        fig.legend([Patch(facecolor=c) for c in colors],[f'Rating {k}' for k in range(1,6)],loc='lower center',ncol=5,frameon=False)
        for ext in ('png','svg'):
            fig.savefig(output/f'meega_items.{ext}',dpi=220,metadata={'Date':None} if ext=='svg' else None)
        plt.close(fig)
    print(f'MEEGA+: {len(rows)} participants, {len(responses)} ratings')
    return summary

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,default=ROOT/'results/meega');p.add_argument('--no-figures',action='store_true')
    a=p.parse_args();run(a.output,not a.no_figures)
