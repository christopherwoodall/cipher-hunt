#!/usr/bin/env python3
"""1690 uniformity checks for 62-polyvalence (cipher-side, no era assumptions).
SIX = the six 62->48 windows (hypothesized syllable-'on'); REST = other 29 62-windows (pronoun-'on')."""
from build_stream import load_stream
from collections import Counter
import math

pairs = load_stream()
seq = [g for g,_,_ in pairs]
w62 = [i for i,g in enumerate(seq) if g=="62"]
SIX = {360,425,1315,1349,1464,1569}
six = sorted(SIX); rest = [i for i in w62 if i not in SIX]
assert len(six)==6 and len(rest)==29

def ctx(ws, d):
    return Counter(seq[i+d] for i in ws if 0 <= i+d < len(seq))

pre6, preR = ctx(six,-1), ctx(rest,-1)
post6, postR = ctx(six,1), ctx(rest,1)
print("pre-62  SIX :", dict(pre6))
print("pre-62  REST:", dict(preR))
print("post-62 SIX :", dict(post6))
print("post-62 REST:", dict(postR))

# Fisher exact: is pre=21/74/24/47 overrepresented in SIX vs REST? (the lead-valued pres)
for gv in ["21","74","24","47","20","93"]:
    a = pre6.get(gv,0); b = 6-a; c = preR.get(gv,0); d = 29-c
    # Fisher exact two-sided via hypergeometric
    from math import comb
    def hyper(k): return comb(a+c,k)*comb(b+d,6-k)/comb(35,6) if 0<=k<=6 and 0<=a+c-k<=29 else 0
    p_obs = hyper(a)
    p = sum(hyper(k) for k in range(7) if hyper(k) <= p_obs+1e-12)
    print(f"pre={gv}: six {a}/6 vs rest {c}/29 -> Fisher p={p:.3f}")

# Chi-square homogeneity on pre distribution (collapsed: top cats + other)
cats = ["21","74","20","93","other"]
def collapsed(c):
    d = {k: c.get(k,0) for k in cats[:4]}
    d["other"] = sum(v for k,v in c.items() if k not in cats[:4])
    return [d[k] for k in cats]
o1, o2 = collapsed(pre6), collapsed(preR)
n1, n2 = sum(o1), sum(o2)
chi2 = 0
for x, y in zip(o1,o2):
    e1 = (x+y)*n1/(n1+n2); e2 = (x+y)*n2/(n1+n2)
    chi2 += (x-e1)**2/e1 + (y-e2)**2/e2 if e1 and e2 else 0
print(f"pre-homogeneity chi2(4df) = {chi2:.2f} (n=6: low power, descriptive only)")

# residual legs check: 62->94 rate in REST (constraint: STRONG LEAD must survive conditioning)
r94 = sum(1 for i in rest if seq[i+1]=="94")
print(f"62->94 in REST: {r94}/29 = {r94/29:.3f} (all-62: 9/35={9/35:.3f})")
# 62->98, 62->16 in REST
for gv in ["98","16","06","61"]:
    r = sum(1 for i in rest if seq[i+1]==gv)
    print(f"62->{gv} in REST: {r}/29")
