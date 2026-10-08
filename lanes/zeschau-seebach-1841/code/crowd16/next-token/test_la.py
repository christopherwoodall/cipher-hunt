#!/usr/bin/env python3
"""Round-16 la battery. Pre-registered bars in next-token-la.md."""
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
chk('n11', s.G[11], 45)
chk('87-11 x7', s.starts(87,11), [74,163,201,461,830,1242,1403])
chk('47-11 x3', s.starts(47,11), [269,357,498])
st = s.starts(11)
chk('standalone 35', len([i for i in st if P[i-1] not in (87,47)]), 35)
chk('@320', P[318:324], [94,6,11,92,60,15])
chk('@1123', P[1121:1128], [14,6,11,52,37,43,0])
chk('@1721', P[1719:1726], [68,6,11,52,37,43,98])
chk('11-52-37-43 x2', s.starts(11,52,37,43), [1123,1721])
chk('@296', P[294:301], [16,1,11,78,40,97,86])
chk('@1669', P[1667:1674], [6,91,11,78,55,81,92])
chk('11-78 x2', s.starts(11,78), [296,1669])
chk('11-24 standalone x3', [i for i in s.starts(11,24) if P[i-1] not in (87,)], [731,782,1656])
chk('@164 is cela', (P[163],P[164]), (87,11))
chk('11-26 x2', s.starts(11,26), [239,1559])
chk('@239', P[237:244], [41,17,11,26,12,16,56])
chk('@1559', P[1557:1564], [40,17,11,26,30,6,60])
chk('@106 full', P[106:114], [0,46,11,21,67,93,29,89])
chk('@1523', P[1521:1529], [31,24,11,11,48,96,87,46])
chk('11-11 x1', s.starts(11,11), [1523])
chk('@1288', P[1286:1294], [68,0,11,17,84,59,35,94])
chk('@997', P[995:1002], [60,67,11,96,82,33,0])
chk('06->77 x6', s.BIG[(6,77)], 6)
chk('06->11 x4', s.BIG[(6,11)], 4)
chk('@1044', P[1042:1049], [82,63,11,67,76,85,41])
chk('@498 flagback', P[496:503], [79,88,47,11,29,40,56])
chk('@562', P[560:567], [30,67,11,43,24,80,97])
chk('@670', P[668:675], [20,67,11,86,24,80,3])
chk('@731', P[729:736], [48,88,11,24,85,93,76])
chk('@782', P[780:787], [29,89,11,24,42,94,74])
chk('@1656', P[1654:1661], [56,37,11,24,48,47,98])
if fails:
    print(f"FAILURES: {fails}"); sys.exit(1)
print("LA BATTERY: all checks PASS")
