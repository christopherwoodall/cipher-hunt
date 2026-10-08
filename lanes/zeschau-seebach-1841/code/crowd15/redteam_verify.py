#!/usr/bin/env python3
"""Red-team independent re-derivation of all next-token battery claims."""
import sys, json
from collections import Counter
from pathlib import Path
LANE = Path('/home/hatch/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
sys.path.insert(0, str(LANE / 'code' / 'crowd6' / 'redteam'))
from verify_baseline import load_stream
import math

pairs = load_stream()
assert len(pairs) == 1847, len(pairs)
n = len(pairs)
G = Counter(pairs)
BIG = Counter((pairs[i], pairs[i+1]) for i in range(n-1))
TRI = Counter((pairs[i], pairs[i+1], pairs[i+2]) for i in range(n-2))

def pos2(a,b): return [i for i in range(n-1) if pairs[i]==a and pairs[i+1]==b]
def pos3(a,b,c): return [i for i in range(n-2) if pairs[i]==a and pairs[i+1]==b and pairs[i+2]==c]
def pos5(*t): return [i for i in range(n-len(t)+1) if tuple(pairs[i:i+len(t)])==t]
def pre(x): return Counter(pairs[i-1] for i in range(1,n) if pairs[i]==x)
def suc(x): return Counter(pairs[i+1] for i in range(n-1) if pairs[i]==x)
def win(i, w=3):
    lo, hi = max(0,i-w), min(n,i+w+1)
    return '-'.join(f'{p:02d}' for p in pairs[lo:hi])

def fisher(a,b,c,d):
    # 2x2 table [[a,b],[c,d]] two-sided via log factorial sum
    from math import lgamma
    def lch(n,k):
        return lgamma(n+1)-lgamma(k+1)-lgamma(n-k+1)
    def ptab(x):
        # x = top-left given fixed margins
        n1,n2 = a+b, c+d; m1, m2 = a+c, b+d; N = n1+n2
        return math.exp(lch(n1,x)+lch(n2,m1-x)-lch(N,m1))
    obs = ptab(a)
    lo = max(0,(a+b)+(a+c)-(a+b+c+d)); hi = min(a+b,a+c)
    return sum(ptab(x) for x in range(lo,hi+1) if ptab(x) <= obs+1e-12)

R = {}
print('=== A1: est->X frames ===')
print('59->37:', pos2(59,37))
print('59->32:', pos2(59,32))
print('59->42:', pos2(59,42))
print('59->19:', pos2(59,19))
print('94->59:', pos2(94,59))
print('64->59:', pos2(64,59))
print('93->59:', pos2(93,59))
print('est-arm: 64-59 x%d, 94-59 x%d, 93-59 x%d' % (len(pos2(64,59)), len(pos2(94,59)), len(pos2(93,59))))
R['a1_37'] = len(pos2(59,37)); R['a1_32'] = len(pos2(59,32))
R['a1_42'] = len(pos2(59,42)); R['a1_19'] = len(pos2(59,19))
R['f71_arm'] = len(pos2(64,59))+len(pos2(94,59))+len(pos2(93,59))

print('=== A2: 23/26 ===')
print('n23', G[23], 'n26', G[26])
s23, s26 = suc(23), suc(26)
print('23 sucs:', dict(s23)); print('26 sucs:', dict(s26))
cls = {12,30,0}
a = sum(s23[x] for x in cls); b = sum(v for k,v in s23.items() if k not in cls)
c = sum(s26[x] for x in cls); d = sum(v for k,v in s26.items() if k not in cls)
p = fisher(a,b,c,d)
print(f'suc-class {{12,30,00}} 23:{a}/{a+b} 26:{c}/{c+d} p={p:.4f}')
R['a2_p'] = round(p,4)
sp23 = set((x, y) for x in pre(23) for y in [23])
# joint frames: shared pre-bigrams / suc-bigrams
pre_b_23 = set((p_, 23) for p_ in pre(23)); pre_b_26 = set((p_, 26) for p_ in pre(26))
suc_b_23 = set((23, s_) for s_ in suc(23)); suc_b_26 = set((26, s_) for s_ in suc(26))
# shared predecessor TYPES and successor types (beyond anchor windows 182,1769,531)
shared_pre = set(pre(23)) & set(pre(26)); shared_suc = set(suc(23)) & set(suc(26))
print('shared pre types:', shared_pre, '| shared suc types:', shared_suc)
R['a2_shared_pre'] = sorted(shared_pre); R['a2_shared_suc'] = sorted(shared_suc)

print('=== A3: parce qu-en ===')
print('96-87-46:', pos3(96,87,46))
tails = {i: pairs[i+3] for i in pos3(96,87,46)}
print('tails:', tails)
print('85 pre:', dict(pre(85)))
R['a3_85_pre24'] = pre(85)[24]
R['a3_24tail_at_952'] = (pairs[952+3] == 24)

print('=== A4: 47/87 ===')
print('87 pre=24:', pre(87)[24], '| 47 pre=24:', pre(47)[24])
p24 = pre(87)[24]; q24 = pre(47)[24]
pf = fisher(p24, G[87]-p24, q24, G[47]-q24)
print(f'Fisher p={pf:.4f}')
R['a4_87_pre24'] = p24; R['a4_47_pre24'] = q24; R['a4_p'] = round(pf,4)
print('47->46:', pos2(47,46)); print('87->46:', pos2(87,46))
print('47->11:', pos2(47,11)); print('47->77:', pos2(47,77))
R['a4_47_46'] = len(pos2(47,46)); R['a4_47_11'] = len(pos2(47,11))
# tail parity: how many 87->46 and 47->46 have pre=96 before the 87/47
for label, x in [('87',87),('47',47)]:
    idxs = pos2(x,46)
    tailed = [i for i in idxs if i>=1 and pairs[i-1]==96]
    print(f'{x}->46: {idxs} tailed(96): {tailed}')

print('=== A5: 79 ===')
print('79-17:', pos2(79,17)); print('79-87-11:', pos3(79,87,11)); print('79-87-64:', pos3(79,87,64))
print('79-80:', pos2(79,80)); print('64-79-82-48:', pos3(64,79,82) and pos5(64,79,82,48))
print('62-94-79:', pos3(62,94,79))
R['a5_79_17'] = len(pos2(79,17)); R['a5_79_87_11'] = len(pos3(79,87,11))
R['a5_79_87_64'] = len(pos3(79,87,64)); R['a5_79_80'] = len(pos2(79,80))

print('=== A6: 09/92 ===')
print('anchor09:', pos5(9,64,29,40,65)); print('anchor92:', pos5(92,64,29,40,65))
print('92 pre=00:', pre(92)[0], '| 09 pre=00:', pre(9)[0])
shared_pre = set(pre(9)) & set(pre(92)); shared_suc = set(suc(9)) & set(suc(92))
print('shared pre:', sorted(shared_pre), '| shared suc:', sorted(shared_suc))
R['a6_92_pre00'] = pre(92)[0]; R['a6_09_pre00'] = pre(9)[0]

print('=== A7: trigram + 48 ===')
print('79-82-48:', pos5(79,82,48))
print('48->{37,32,35}:', sum(suc(48)[x] for x in (37,32,35)), '/ n48=', G[48])
print('59->{37,32,35}:', sum(suc(59)[x] for x in (37,32,35)), '/ n59=', G[59])
print('82-48:', pos2(82,48))
R['a7_48_pred'] = sum(suc(48)[x] for x in (37,32,35))
R['a7_59_pred'] = sum(suc(59)[x] for x in (37,32,35))

print('=== A8: 80/89 ===')
print('87-77-80:', pos3(87,77,80)); print('87-77-89:', pos3(87,77,89))
print('80 pre:', dict(pre(80))); print('80 suc:', dict(suc(80)))
print('89 pre:', dict(pre(89))); print('89 suc:', dict(suc(89)))
s80, s89 = suc(80), suc(89)
# chi-square-ish permutation: fisher on "suc in shared classes" is weak; report distinctness
shared_suc = set(s80) & set(s89); shared_pre = set(pre(80)) & set(pre(89))
print('shared suc classes:', sorted(shared_suc), '| shared pre classes:', sorted(shared_pre))
R['a8_shared_suc'] = sorted(shared_suc); R['a8_shared_pre'] = sorted(shared_pre)

print('=== A9: 00 ===')
print('00->86:', len(pos2(0,86)), '| 00->33:', len(pos2(0,33)), '| n00:', G[0])
print('00-46:', pos2(0,46))
R['a9_00_inf'] = len(pos2(0,86))+len(pos2(0,33))
print('86: pre=00', pre(86)[0], 'suc=29', suc(86)[29], '| 33: pre=00', pre(33)[0], 'suc=29', suc(33)[29])

print('=== A10: 33 ===')
print('33-46:', pos2(33,46)); print('33-29:', pos2(33,29))
print('33 pre=00:', pre(33)[0], '/ n33:', G[33])
R['a10_33_46'] = len(pos2(33,46)); R['a10_33_29'] = len(pos2(33,29))

print('=== A11: 45 ===')
print('45 pre=24:', pre(45)[24], '/ n45:', G[45]); print('45-64:', pos2(45,64))
R['a11_45_pre24'] = pre(45)[24]; R['a11_45_64'] = len(pos2(45,64))
print('formula:', pos5(45,64,96,43,87,1))

print('=== A12: 37-01 ===')
print('37-01:', pos2(37,1))
print('21-64-37-01:', pos5(21,64,37,1))
R['a12_37_01'] = len(pos2(37,1))

print('=== A13/A15: 84 ===')
print('n84:', G[84]); print('84 pre:', dict(pre(84))); print('84 suc:', dict(suc(84)))
print('77-84:', pos2(77,84))
print('46-84-24-37-78:', pos5(46,84,24,37,78))
print('46-77-84-24-87:', pos5(46,77,84,24,87))
print('82-84:', pos2(82,84))
print('11-84:', pos2(11,84)); print('94-84:', pos2(94,84))
R['a15_77_84'] = len(pos2(77,84)); R['a15_quonen'] = len(pos5(46,84,24,37,78))
R['a15_lon_variant'] = len(pos5(46,77,84,24,87))
R['a15_11_84'] = pos2(11,84); R['a15_94_84'] = pos2(94,84)

print('=== A14: par le X ===')
print('96-00-92:', pos3(96,0,92)); print('96-00-33:', pos3(96,0,33)); print('96-00-86:', pos3(96,0,86))
print('92: pre=00', pre(92)[0], '->29', suc(92)[29], '/ n92', G[92])
R['a14_92_pre00'] = pre(92)[0]

print('=== P1 cela ===')
print('87-11:', pos2(87,11))

json.dump(R, open('/tmp/redteam_derived.json','w'), indent=1)
print('OK')
