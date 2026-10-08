#!/usr/bin/env python3
"""D1: independent double-pour re-check (round 13 carry-rest). PREREG.md section D.

Re-runs strict DP patterns on RDM-1841-q1 + Guizot-DIP, fresh in this worker,
independent of round-12's scan. Lane tokenizer verbatim (round-10/11 arm1248).
Constituency-read any hit (printed for adjudication).
"""
import json, re
from pathlib import Path
LANE = Path.home() / 'workspace/cipher-hunt/lanes/zeschau-seebach-1841'
CORP = LANE / 'code/side-period/corpus'

def load(p):
    return (CORP / p).read_text(encoding='utf-8', errors='replace')

def tok(text):
    text = text.lower().replace('\u2019', "'").replace('\u2018', "'")
    text = re.sub(r"([a-z\u00e0-\u00ff])'([a-z\u00e0-\u00ff])", r'\1 \2', text)
    return re.findall(r'[a-z\u00e0-\u00ff]+', text)

def is_inf(w):
    return w.endswith(('er', 'ir', 're')) and len(w) > 3

def ctx(t, i, half=25):
    return ' '.join(t[max(0, i-half):i+half+1])

res = {}
for name, fn in [('RDM-1841-q1', 'revue-deux-mondes-1841-q1.txt'),
                 ('Guizot-DIP', 'guizot-memoires-t5-t6.txt')]:
    t = tok(load(fn))
    peu_hits, inf_hits = [], []
    for i in range(len(t) - 5):
        if t[i] == 'pour' and t[i+3] == 'pour':
            if t[i+4] == 'peu' and t[i+5] == 'que':
                peu_hits.append((i, ctx(t, i)))
            elif is_inf(t[i+4]) and i + 5 < len(t) and t[i+5] == 'que':
                inf_hits.append((i, t[i+4], ctx(t, i)))
    res[name] = {"tokens": len(t), "bytes": len(load(fn)),
                 "strict_dp_peu": peu_hits, "strict_dp_inf": inf_hits}

out = LANE / 'code/crowd13/carry-rest/dp_verify_raw.json'
out.write_text(json.dumps(res, ensure_ascii=False, indent=1))
for name, r in res.items():
    print(name, "| tokens:", r["tokens"],
          "| dp_peu:", len(r["strict_dp_peu"]), "| dp_inf:", len(r["strict_dp_inf"]))
    for h in r["strict_dp_peu"] + r["strict_dp_inf"]:
        print("  HIT:", h)
