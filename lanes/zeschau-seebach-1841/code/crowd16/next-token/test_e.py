#!/usr/bin/env python3
"""Round-16 e battery. Pre-registered bars in next-token-e.md."""
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
chk('n40', s.G[40], 21)
chk('40-65-94', s.starts(40,65,94), [686,1711])
chk('65-94 exclusive', s.starts(65,94), [687,1712])
chk('20-62', s.starts(20,62), [760,839,1135,1703])
chk('20-62-94', s.starts(20,62,94), [760,839,1703])
chk('@760', P[758:766], [29,40,20,62,94,59,39,88])
chk('62-94', s.BIG[(62,94)], 9)
chk('62-48', s.BIG[(62,48)], 6)
chk('67-77-81', s.starts(67,77,81), [743,1239,1400,1597])
chk('@1239', P[1237:1245], [3,40,67,77,81,87,11,0])
chk('@1400', P[1398:1406], [48,40,67,77,81,87,11,0])
chk('08-31', s.starts(8,31), [881,1488,1520])
chk('65-64', s.BIG[(65,64)], 3)
chk('21-65', s.BIG[(21,65)], 4)
chk('@848', P[844:852], [16,0,33,96,40,62,21,67])
chk('96-40 x1', s.starts(96,40), [847])
chk('33-96-40', s.starts(33,96,40), [846])
chk('@60 08-iere', P[58:65], [12,41,8,34,29,40,12])
chk('@1557', P[1555:1562], [93,61,40,17,11,26,30])
if fails:
    print(f"FAILURES: {fails}"); sys.exit(1)
print("E BATTERY: all checks PASS")
