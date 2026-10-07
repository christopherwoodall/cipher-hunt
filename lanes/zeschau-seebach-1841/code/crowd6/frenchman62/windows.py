#!/usr/bin/env python3
"""Key windows for the 62 battery: 62->46, 77->62, 62 X 46 trigrams, 21->62."""
import json, re, collections
from pathlib import Path
LANE = Path.home() / 'workspace/cipher-hunt/lanes/zeschau-seebach-1841'
DATA = LANE / 'data'
GT = {11:'la',70:'pre',82:'m',34:'i',29:'er',40:'e',46:'que'}
PROV = {87:'ce',64:'qui',96:'par',94:'ne',77:'le'}
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
def show(i, w=4):
    seg = pairs[max(0,i-w):i+w+1]
    lab = []
    for j,g in enumerate(seg):
        tag = GT.get(g, PROV.get(g, ''))
        lab.append(f'{g}{"="+tag if tag else ""}')
    mark = ' '.join(lab)
    return f'@{i-w+ (w if i-w>=0 else 0)}: {mark}   <62 @ {i}>'
print('=== 62->46 windows ===')
for i in range(n-1):
    if pairs[i]==62 and pairs[i+1]==46: print(show(i))
print('=== 77->62 windows ===')
for i in range(1,n):
    if pairs[i]==62 and pairs[i-1]==77: print(show(i))
print('=== 62 X 46 trigrams (X!=62) ===')
c=0
for i in range(n-2):
    if pairs[i]==62 and pairs[i+2]==46 and pairs[i+1]!=62:
        print(show(i)); c+=1
print('total 62-X-46:', c)
print('=== 21->62 windows (first 6) ===')
k=0
for i in range(1,n):
    if pairs[i]==62 and pairs[i-1]==21:
        print(show(i)); k+=1
        if k>=6: break
print('=== 46->29 windows (qu-er calibration) ===')
for i in range(n-1):
    if pairs[i]==46 and pairs[i+1]==29: print(show(i))
print('=== 94->29 windows ===')
for i in range(n-1):
    if pairs[i]==94 and pairs[i+1]==29: print(show(i))
