#!/usr/bin/env python3
"""U3: identify an impersonal-verb cell (ranked unblocker #3 for 62="on").

Logic: an impersonal-only verb V (era: P(subject="il"|V)~1, P(subject="on"|V)=0)
with V->62 kills 62="on" outright ("faut-il" vs *"faut-on").
Screen: V with 94->V>=1 ("ne"+V, 94 prov-strong) and V->62>=1.
Impersonal fingerprint: V->46=que ("faut que", 46 GT); era calibration below.
"""
import json, collections
import util
from util import PAIRS, N, UNI, GT, followers, predecessors, window, positions

eu, eb = util.era_counters()
print('=== era impersonal-verb calibration ===')
for v in ['faut', 'semble', 'suffit', 'paraît', 'importe', 'arrive', 'reste']:
    n = eu[v]
    if n == 0:
        print(f'{v}: n=0'); continue
    p_il = sum(eb[(p, v)] for p in ['il']) / n
    p_on = sum(eb[(p, v)] for p in ['on']) / n
    p_que = sum(eb[(v, f)] for f in ['que', "qu'"]) / n
    p_ne = sum(eb[(p, v)] for p in ['ne', "n'"]) / n
    print(f'{v}: n={n} P(il|pre)={p_il:.3f} P(on|pre)={p_on:.3f} P(que|fol)={p_que:.3f} P(ne|pre)={p_ne:.3f}')
# faut-il inversion
t = util.toks()
n_fautil = sum(1 for i in range(len(t)-2) if t[i]=='faut' and t[i+1]=='il')
n_fauton = sum(1 for i in range(len(t)-2) if t[i]=='faut' and t[i+1]=='on')
print('era "faut il" bigrams:', n_fautil, ' "faut on":', n_fauton)

print('\n=== cipher screen: 94->V>=1 and V->62>=1 ===')
cands = []
for v in range(100):
    if v == 62: continue
    a = sum(1 for i in range(N-1) if PAIRS[i]==94 and PAIRS[i+1]==v)
    b = sum(1 for i in range(N-1) if PAIRS[i]==v and PAIRS[i+1]==62)
    if a >= 1 and b >= 1:
        fol = followers(v); pre = predecessors(v)
        cands.append((v, UNI[v], a, b, fol.get(46,0),
                      dict(sorted(fol.items(),key=lambda x:-x[1])[:5]),
                      dict(sorted(pre.items(),key=lambda x:-x[1])[:5])))
for v, n, a, b, q, fol5, pre5 in sorted(cands, key=lambda r: -(r[2]+r[3])):
    print(f'V={v:3d} n={n:3d} 94->V={a} V->62={b} V->46(que)={q}')
    print(f'    fol: {fol5}')
    print(f'    pre: {pre5}')
    for i in positions(v):
        if i+1<N and PAIRS[i+1]==62:
            print('     V->62 @', i, ':', window(i,4))
json.dump([{'v':v,'n':n,'ne_v':a,'v_62':b,'v_que':q} for v,n,a,b,q,_,_ in cands],
          open('u3_impersonal.json','w'), indent=1)
print('\nwrote u3_impersonal.json')
