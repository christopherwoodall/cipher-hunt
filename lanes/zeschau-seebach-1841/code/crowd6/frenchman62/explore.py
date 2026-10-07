#!/usr/bin/env python3
"""Round 6 frenchman: explore 62's geometry on the repaired 1,847-pair parse."""
import json, re, collections
from pathlib import Path
LANE = Path.home() / 'workspace/cipher-hunt/lanes/zeschau-seebach-1841'
DATA = LANE / 'data'

def load_repaired():
    rows = []
    for line in open(DATA / 'upstream-ct_R5005.txt'):
        line = line.strip()
        if not line: continue
        lid, digits = line.split()
        rows.append((lid, re.sub(r'\D', '', digits)))
    off = json.loads((LANE / 'code/side-keyhunt/repaired_offsets.json').read_text())
    pairs = []
    for lid, digits in rows:
        o = off[lid]
        pairs += [digits[i:i+2] for i in range(o, len(digits)-1, 2)]
    return [int(g) for g in pairs]

pairs = load_repaired(); n = len(pairs)
assert n == 1847, n
big = collections.Counter(zip(pairs[:-1], pairs[1:]))
uni = collections.Counter(pairs)
GT = {11:'la',70:'pre',82:'m',34:'i',29:'er',40:'e',46:'que'}
PROV = {87:'ce',64:'qui',96:'par',94:'ne',77:'le'}

n62 = uni[62]
fol62 = collections.Counter(pairs[i+1] for i in range(n-1) if pairs[i]==62)
pre62 = collections.Counter(pairs[i-1] for i in range(1,n) if pairs[i]==62)
pos62 = [i for i in range(n) if pairs[i]==62]
print('n62 =', n62, '| rank:', sorted(uni.values(), reverse=True).index(n62)+1)
print('62->94 =', big[(62,94)], '/', n62)
print('46->62 =', big[(46,62)], '/', sum(1 for i in range(n-1) if pairs[i]==46))
print('followers of 62:', dict(sorted(fol62.items(), key=lambda kv:-kv[1])))
print('predecessors of 62:', dict(sorted(pre62.items(), key=lambda kv:-kv[1])))
print('62->46 =', big[(62,46)], '| 62->21 =', big[(62,21)], '| 62->11 =', big[(62,11)])
print('87->62 =', big[(87,62)], '| 96->62 =', big[(96,62)], '| 77->62 =', big[(77,62)], '| 24->62 =', big[(24,62)], '| 00->62 =', big[(00,62)])
print('62->87 =', big[(62,87)], '| 62->64 =', big[(62,64)], '| 64->62 =', big[(64,62)], '| 62->24 =', big[(62,24)])
# 46's followers in GT vowel/consonant sets
fol46 = collections.Counter(pairs[i+1] for i in range(n-1) if pairs[i]==46)
V = {34,40}; C = {11,82,70,29}
print('46 followers:', dict(sorted(fol46.items(), key=lambda kv:-kv[1])))
print('46->V(i,e) =', sum(fol46[g] for g in V), '| 46->C(la,m,pre,er) =', sum(fol46[g] for g in C))
# 94's followers in GT vowel set (n' elision calibration)
fol94 = collections.Counter(pairs[i+1] for i in range(n-1) if pairs[i]==94)
print('94 followers:', dict(sorted(fol94.items(), key=lambda kv:-kv[1])))
print('94->V(i,e) =', sum(fol94[g] for g in V))
# 62-94-X frames
xframes = collections.Counter(pairs[i+2] for i in range(n-2) if pairs[i]==62 and pairs[i+1]==94)
print('62-94-X frames:', dict(xframes))
# 59 profile
n59 = uni[59]
fol59 = collections.Counter(pairs[i+1] for i in range(n-1) if pairs[i]==59)
pre59 = collections.Counter(pairs[i-1] for i in range(1,n) if pairs[i]==59)
print('n59 =', n59, '| fol59:', dict(sorted(fol59.items(), key=lambda kv:-kv[1])), '| pre59:', dict(sorted(pre59.items(), key=lambda kv:-kv[1])))
print('59->46 =', big[(59,46)], '| 94->59 =', big[(94,59)], '| 59->29 =', big[(59,29)], '| 59->52 =', big[(59,52)])
print('contexts of 94->59:', [(i-1, pairs[i-1]) for i in range(1,n-1) if pairs[i]==94 and pairs[i+1]==59])
# 62/64 context overlap
fol64 = collections.Counter(pairs[i+1] for i in range(n-1) if pairs[i]==64)
pre64 = collections.Counter(pairs[i-1] for i in range(1,n) if pairs[i]==64)
jf = len(set(fol62)&set(fol64))/len(set(fol62)|set(fol64))
jp = len(set(pre62)&set(pre64))/len(set(pre62)|set(pre64))
print('n64 =', uni[64], '| Jaccard fol(62,64) =', round(jf,3), '| Jaccard pre(62,64) =', round(jp,3))
print('fol64:', dict(sorted(fol64.items(), key=lambda kv:-kv[1])))
print('positions of 62:', pos62)
