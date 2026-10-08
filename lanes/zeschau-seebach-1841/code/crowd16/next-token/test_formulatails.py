#!/usr/bin/env python3
"""Round-16 formula-tails battery. Pre-registered bars in next-token-formula-tails.md."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import streamkit as s

fails = []
def chk(name, got, want):
    ok = got == want
    print(f"[{'OK' if ok else 'FAIL'}] {name}: got={got} want={want}")
    if not ok: fails.append(name)

P = s.P
chk('F-qui-par tails', (P[346:349], P[1030:1033]), ([6,70,12],[3,29,80]))
chk('87-11 starts', s.starts(87,11), [74,163,201,461,830,1242,1403])
chk('87-11-00 x3', [i for i in s.starts(87,11) if P[i+2]==0], [74,1242,1403])
chk('06-70 x1', s.starts(6,70), [346])
chk('@146 window', P[144:151], [64,77,84,29,87,64,96])
chk('84->29', s.starts(84,29), [146])
chk('@1290', P[1288:1295], [11,17,84,59,35,94,52])
chk('@1799', P[1799:1806], [79,87,64,77,84,59,35])
chk('@754', P[754:762], [11,70,82,34,29,40,20,62])
chk('@1041', P[1039:1046], [40,17,77,82,63,11,67])
chk('82-63', s.starts(82,63), [1042])
chk('toutefois tails distinct', (P[453:456], P[1462:1465]), ([77,60,65],[1,21,62]))
chk('par-ce-que tails distinct', (P[227:230], P[955:958], P[1529:1532]),
    ([98,83,82],[24,85,4],[21,65,63]))
chk('24-87-64', s.starts(24,87,64), [179,1766,1774])
if fails:
    print(f"FAILURES: {fails}"); sys.exit(1)
print("FORMULA-TAILS BATTERY: all checks PASS")
