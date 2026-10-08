#!/usr/bin/env python3
"""Round-16 m battery. Pre-registered bars in next-token-m.md."""
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
g1, g2, g3 = P[227:232], P[1060:1065], P[1783:1788]
chk('P1 5-gram x3 identical', (g1, g2, g3),
    ([98,83,82,96,21],[98,83,82,96,21],[98,83,82,96,21]))
chk('P1 thirds', (P[232], P[1065], P[1788]), (60, 62, 68))
chk('96-21 formula-bound', s.starts(96,21), [230,1063,1786])
chk('@227 left ctx', P[224:230], [96,87,46,98,83,82])
chk('94-82-06-06 x2', s.starts(94,82,6,6), [578,1182])
chk('52-82-94 x3', s.starts(52,82,94), [649,1100,1574])
chk('@649', P[648:655], [78,52,82,94,76,49,24])
chk('@1100', P[1099:1106], [86,52,82,94,74,47,78])
chk('@1574', P[1573:1580], [28,52,82,94,76,47,98])
chk('82-16', s.BIG[(82,16)], 11)
chk('16-91 x2', s.starts(16,91), [537,1370])  # finder cited 16-cells [536,1369]
chk('82-40 zero', s.BIG[(82,40)], 0)
chk('@396 wide', P[384:402],
    [38,37,43,91,36,62,91,84,73,34,67,64,79,82,48,6,11,45])
chk('@1227 wide', P[1215:1235],
    [36,77,83,92,61,24,48,30,9,20,57,64,79,82,48,29,47,33,29,85])
chk('@166 mon', P[162:170], [24,87,11,24,82,84,53,12])
chk('@20 43-verb-stem', P[16:26], [53,17,64,98,82,43,29,47,33,55])
chk('@1743 m-que', P[1741:1747], [34,94,82,46,56,40])
if fails:
    print(f"FAILURES: {fails}"); sys.exit(1)
print("M BATTERY: all checks PASS")
