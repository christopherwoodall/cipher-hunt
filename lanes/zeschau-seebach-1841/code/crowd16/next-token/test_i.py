#!/usr/bin/env python3
"""Round-16 i battery. Pre-registered bars in next-token-i.md."""
import sys
from collections import Counter
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import streamkit as s

fails = []
def chk(name, got, want):
    ok = got == want
    print(f"[{'OK' if ok else 'FAIL'}] {name}: got={got} want={want}")
    if not ok: fails.append(name)

P = s.P
chk('n34', s.G[34], 11)
chk('34 starts', s.starts(34), [28,61,393,404,555,757,1037,1348,1415,1741,1749])
chk('34-29-40', s.starts(34,29,40), [61,757,1037])
g1, g2 = P[754:760], P[1034:1040]
chk('la-premiere x2 identical', (g1,g2), ([11,70,82,34,29,40],[11,70,82,34,29,40]))
chk('@754 tail', P[760], 20); chk('@1034 tail', P[1040], 17)
chk('82-34 only x2', s.starts(82,34), [756,1036])
chk('70-82-34-29 x2', s.starts(70,82,34,29), [755,1035])
chk('@291', P[287:297], [0,97,9,64,29,40,65,16,1,11])
chk('@685', P[681:691], [7,0,92,64,29,40,65,94,29,60])
chk('@595', P[591:600], [9,0,92,79,85,1,29,40,3])
chk('@61', P[59:66], [41,8,34,29,40,12,94])
chk('73-34 x2', s.starts(73,34), [392,1347])  # finder cited 34-cells
chk('@393', P[391:398], [84,73,34,67,64,79,82])
chk('@1348', P[1346:1353], [66,73,34,62,48,77,78])
chk('29-40 n', s.BIG[(29,40)], 9)
chk('29-40 stems', dict(Counter(P[i-1] for i in s.starts(29,40))),
    {34:3,64:2,11:1,1:1,88:1,6:1})
chk('@28', P[24:34], [33,55,81,0,34,24,30,3,64,32])
chk('@555', P[553:560], [86,59,34,17,86,94,59])
chk('@1415', P[1413:1420], [69,74,34,52,32,84,79])
chk('@307 [20] fois', P[305:312], [2,88,20,17,46,84,24])
chk('85-1', s.starts(85,1), [595,1439])
if fails:
    print(f"FAILURES: {fails}"); sys.exit(1)
print("I BATTERY: all checks PASS")
