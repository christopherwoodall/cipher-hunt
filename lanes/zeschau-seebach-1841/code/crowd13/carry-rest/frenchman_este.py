#!/usr/bin/env python3
"""E-trans: Frenchman transitivity battery (round 13 carry-rest). PREREG.md section E.

For each -este candidate {manifeste, atteste, proteste, conteste, déteste} + reste:
clean-diplo counts of ("le",V3sg), ("l'",V3sg), ("qui","le",V3sg), (V3sg,"que").
V3sg forms: manifeste/atteste/proteste/conteste/déteste/reste (1st&3rd sg identical
for -er verbs). Also ("le",Vinf) as transitivity support.
"""
import json, re, unicodedata
from pathlib import Path
from collections import Counter
LANE = Path.home() / 'workspace/cipher-hunt/lanes/zeschau-seebach-1841'
CORP = LANE / 'code/side-period/corpus'
FILES = ['guizot-memoires-t1-gutenberg.txt', 'guizot-memoires-t2-gutenberg.txt',
         'guizot-memoires-t3-gutenberg.txt', 'guizot-memoires-t5-t6.txt',
         'metternich-papiere-v4.txt', 'metternich-papiere-v6.txt',
         'pozzo-di-borgo-correspondance-v1.txt', 'levant-correspondence-1841-p3.txt',
         'talleyrand-memoires-v1.txt', 'revue-deux-mondes-1841-q1.txt',
         'revue-deux-mondes-1841-q2.txt', 'revue-deux-mondes-1841-q3.txt',
         'revue-deux-mondes-1841-q4.txt']
WORD = re.compile(r"[^\W\d_]+(?:'[^\W\d_]+)?", re.UNICODE)
def tokenize(text):
    text = unicodedata.normalize('NFC', text.lower().replace('\u2019', "'").replace('\u2018', "'"))
    toks = []
    for m in WORD.finditer(text):
        w = m.group(0)
        parts = w.split("'")
        for i, p in enumerate(parts):
            if not p:
                continue
            toks.append(p + "'" if i < len(parts) - 1 else p)
    return toks

toks = []
for f in FILES:
    toks.extend(tokenize((CORP / f).read_text(encoding='utf-8', errors='replace')))
print("tokens:", len(toks))

VERBS = {"manifeste": "manifester", "atteste": "attester", "proteste": "protester",
         "conteste": "contester", "déteste": "détester", "reste": "rester"}
INFS = {"manifeste": "manifester", "atteste": "attester", "proteste": "protester",
        "conteste": "contester", "déteste": "détester", "reste": "rester"}
res = {"tokens": len(toks), "verbs": {}}
for v3 in VERBS:
    le_v = sum(1 for i in range(len(toks)-1)
               if toks[i+1] == v3 and toks[i] in ('le', "l'"))
    qui_le_v = sum(1 for i in range(len(toks)-2)
                   if toks[i] == 'qui' and toks[i+1] == 'le' and toks[i+2] == v3)
    v_que = sum(1 for i in range(len(toks)-1)
                if toks[i] == v3 and toks[i+1] == 'que')
    le_vinf = sum(1 for i in range(len(toks)-1)
                  if toks[i+1] == INFS[v3] and toks[i] in ('le', "l'"))
    n_v3 = sum(1 for w in toks if w == v3)
    ctxs = [' '.join(toks[max(0,i-6):i+4]) for i in range(len(toks)-1)
            if toks[i+1] == v3 and toks[i] in ('le', "l'")][:6]
    res["verbs"][v3] = {"n_v3sg": n_v3, "le_v3sg": le_v, "qui_le_v3sg": qui_le_v,
                        "v3sg_que": v_que, "le_vinf": le_vinf,
                        "le_v3sg_contexts": ctxs}

out = LANE / 'code/crowd13/carry-rest/frenchman_este_raw.json'
out.write_text(json.dumps(res, ensure_ascii=False, indent=1))
for v3, r in res["verbs"].items():
    print(f"{v3:10s} n={r['n_v3sg']:4d} le_V={r['le_v3sg']:3d} qui_le_V={r['qui_le_v3sg']:2d} "
          f"V_que={r['v3sg_que']:3d} le_Vinf={r['le_vinf']:3d}")
