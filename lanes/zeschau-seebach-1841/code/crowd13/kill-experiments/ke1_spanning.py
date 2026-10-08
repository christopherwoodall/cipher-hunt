#!/usr/bin/env python3
"""KE1 — offset-model spanning-bigram test. Implements PREREG.md (locked 2026-10-07).

M1+1flip: continuous pairing from digit 0 of the 3,764-digit stream, single
digit dropped at adversarial row boundary b* in (2108,3453) maximizing GOLD.
For each of the 69 row boundaries: spanning pair -> anchored bigram tokens
(pre,p)/(p,suc) with both in the 12-set -> GOLD/IMPLAUSIBLE/UNINFORMATIVE.

STOP CONDITION: gold>=3 AND gold:implausible>=3:1 -> REJECT row-independence,
STOP IMMEDIATELY, report numbers, no further analysis.

Writes ke1_results.json (all 25 candidates + winner detail).
"""
import json, os, re, sys
from collections import Counter

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(LANE, 'code', 'council', 'drag'))
from common import CORPUS, tok_elision

KNOWN12 = {'11','70','82','34','29','40','46','87','64','96','59','77'}
CONFIRMED8 = {('11','70'),('70','82'),('82','34'),('34','29'),('29','40'),
              ('87','64'),('87','46'),('96','87')}
WORDVAL = {'11':'la','46':'que','87':'ce','64':'qui','96':'par','77':'le'}

# ---------------- digit stream + row boundaries ----------------
digits = ''.join(re.findall(r'\d', open(os.path.join(LANE,'data','upstream-ct_R5005.digits.txt')).read()))
assert len(digits) == 3764, len(digits)
bounds = [0]
for line in open(os.path.join(LANE,'data','upstream-ct_R5005.txt')):
    line = line.strip()
    if not line: continue
    _, d = line.split()
    d = re.sub(r'\D','',d)
    bounds.append(bounds[-1]+len(d))
assert len(bounds) == 71 and bounds[-1] == 3764
BOUNDARIES = bounds[1:70]  # 69 inter-row boundaries
CANDS = [b for b in BOUNDARIES if 2108 < b < 3453]
assert len(CANDS) == 25, len(CANDS)

def build_pairs(drop_at):
    """Continuous pairing with digit at raw offset drop_at removed.
    Returns list of (pair_str, orig_off1, orig_off2)."""
    d2 = digits[:drop_at] + digits[drop_at+1:]
    def orig(j): return j if j < drop_at else j+1
    out = []
    for k in range(0, len(d2)-1, 2):
        out.append((d2[k:k+2], orig(k), orig(k+1)))
    return out

def spanning_tokens(m1pairs):
    """For each boundary, the spanning pair; anchored bigram tokens."""
    # index pairs by span for quick lookup: a pair spans B iff o1 < B <= o2
    toks = []  # (boundary, direction, g1, g2, pre_pair_idx)
    for bi, B in enumerate(BOUNDARIES):
        # find pair spanning B
        sp = None
        for pi,(g,o1,o2) in enumerate(m1pairs):
            if o1 < B <= o2:
                sp = pi; break
            if o1 >= B: break
        if sp is None: continue
        g = m1pairs[sp][0]
        if g not in KNOWN12: continue
        for direction, ni in (('pre',sp-1),('suc',sp+1)):
            if 0 <= ni < len(m1pairs):
                ng = m1pairs[ni][0]
                if ng in KNOWN12:
                    g1,g2 = (ng,g) if direction=='pre' else (g,ng)
                    toks.append({'boundary':B,'direction':direction,
                                 'g1':g1,'g2':g2})
    return toks

# ---------------- corpus word bigrams (pool, v8 VOID) ----------------
CORE=['nesselrode-v7.txt','nesselrode-v9.txt','nesselrode-v10.txt','guizot-memoires-t5-t6.txt','levant-correspondence-1841-p3.txt']
EXTRA=['revue-deux-mondes-1841-q1.txt','revue-deux-mondes-1841-q2.txt','revue-deux-mondes-1841-q3.txt','revue-deux-mondes-1841-q4.txt','metternich-papiere-v4.txt','metternich-papiere-v6.txt','talleyrand-memoires-v1.txt','pozzo-di-borgo-correspondance-v1.txt']
W=[]
for fn in CORE+EXTRA:
    W+=tok_elision(open(os.path.join(CORPUS,fn),encoding='utf-8',errors='replace').read())
BIC=Counter(zip(W,W[1:]))
print('pool tokens:',len(W))

def french_words(g1,g2,m1pairs,pi):
    """French word pair if both word-valued (59 needs pre in {64,94,93})."""
    def wv(g, idx):
        if g in WORDVAL: return WORDVAL[g]
        if g=='59':
            pre = m1pairs[idx-1][0] if idx>0 else None
            if pre in {'64','94','93'}: return 'est'
        return None
    # find indices: need pi of g1; caller passes
    return None  # resolved inline below

def classify(tok, m1pairs, pi_of):
    g1,g2 = tok['g1'],tok['g2']
    if (g1,g2) in CONFIRMED8:
        return 'GOLD', 'confirmed8'
    def wv(g, idx):
        if g in WORDVAL: return WORDVAL[g]
        if g=='59':
            pre = m1pairs[idx-1][0] if idx>0 else None
            if pre in {'64','94','93'}: return 'est'
        return None
    i1 = pi_of[(tok['boundary'],tok['direction'],'g1')]
    i2 = pi_of[(tok['boundary'],tok['direction'],'g2')]
    w1,w2 = wv(g1,i1), wv(g2,i2)
    if w1 and w2:
        n = BIC.get((w1,w2),0)
        if n > 50: return 'GOLD', 'corpus>%d:%s %s'%(n,w1,w2)
        tok['french']=(w1,w2); tok['pool_n']=n
        return 'CANDIDATE', 'pool=%d:%s %s'%(n,w1,w2)
    return 'UNINFORMATIVE','syllable'

# sanity: no-drop continuous pairing should give ~38 spanning boundaries (pilot)
m0test = build_pairs(-1)  # drop_at=-1 -> digits[:-1]+digits[0:]? NO - handle separately
m0test = [(digits[k:k+2],k,k+1) for k in range(0,len(digits)-1,2)]
nspan = sum(1 for B in BOUNDARIES for (g,o1,o2) in m0test if o1 < B <= o2)
print('sanity no-drop spanning boundaries:',nspan,'(pilot: 38)')

results=[]
for bstar in CANDS:
    mp = build_pairs(bstar-1)
    toks = spanning_tokens(mp)
    # map (boundary,direction,slot) -> pair index for 59-rule
    pi_of={}
    for bi,B in enumerate(BOUNDARIES):
        for pi,(g,o1,o2) in enumerate(mp):
            if o1 < B <= o2:
                if g in KNOWN12:
                    if pi-1>=0 and mp[pi-1][0] in KNOWN12:
                        pi_of[(B,'pre','g1')]=pi-1; pi_of[(B,'pre','g2')]=pi
                    if pi+1<len(mp) and mp[pi+1][0] in KNOWN12:
                        pi_of[(B,'suc','g1')]=pi; pi_of[(B,'suc','g2')]=pi+1
                break
            if o1 >= B: break
    gold=0; detail=[]
    for t in toks:
        cls,why = classify(t,mp,pi_of)
        t['class']=cls; t['why']=why
        if cls=='GOLD': gold+=1
        detail.append(t)
    results.append({'bstar':bstar,'gold':gold,'n_tokens':len(toks),'tokens':detail})

results.sort(key=lambda r:-r['gold'])
best=results[0]
print('best b*=%d gold=%d tokens=%d'%(best['bstar'],best['gold'],best['n_tokens']))
print('top5:',[(r['bstar'],r['gold']) for r in results[:5]])
json.dump({'candidates':[{'bstar':r['bstar'],'gold':r['gold'],'n_tokens':r['n_tokens']} for r in results],
           'winner':best}, open(os.path.join(HERE,'ke1_results.json'),'w'), indent=1)
print('CANDIDATE (hand-judge) tokens on winner:')
for t in best['tokens']:
    if t['class']=='CANDIDATE':
        print('  B=%d %s (%s,%s) %s'%(t['boundary'],t['direction'],t['g1'],t['g2'],t['why']))
print('GOLD tokens on winner:')
for t in best['tokens']:
    if t['class']=='GOLD':
        print('  B=%d %s (%s,%s) %s'%(t['boundary'],t['direction'],t['g1'],t['g2'],t['why']))
