#!/usr/bin/env python3
"""Round-16 ce47 allophone-verification battery. Pre-registered bars in next-token-ce47.md."""
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
chk('n47', s.G[47], 28)
chk('all 47 starts', s.starts(47),
    [4, 23, 151, 194, 269, 357, 363, 423, 498, 526, 548, 611, 818, 864, 981,
     1004, 1013, 1104, 1203, 1231, 1272, 1344, 1396, 1578, 1591, 1659, 1718, 1789])
chk('24->47 single', [i for i in s.starts(47) if P[i-1] == 24], [548])
chk('47->46', s.starts(47, 46), [151, 548, 864])
chk('47->11', s.starts(47, 11), [269, 357, 498])
chk('47->64 zero', s.starts(47, 64), [])
chk('87->64 n', len(s.starts(87, 64)), 5)
chk('47->78', s.starts(47, 78), [363, 818, 981, 1104, 1396])
chk('29->47', s.starts(29, 47), [22, 422, 1230, 1590])  # bigram starts; finder cited 47-cells +1
chk('64->47', s.starts(64, 47), [1271, 1717])  # bigram starts; finder cited 47-cells +1
chk('@611 window', P[608:615], [64, 2, 58, 47, 77, 87, 83])
chk('@864 window', P[861:868], [74, 74, 48, 47, 46, 0, 86])  # POUR-adverse: 48-47-46-00-86
chk('47->33', s.starts(47, 33), [23, 1231])
chk('47->77', s.starts(47, 77), [611])
chk('@151 window', P[148:155], [87, 64, 96, 47, 46, 66, 84])  # 4th "par ce que"
chk('@1659 window', P[1656:1663], [11, 24, 48, 47, 98, 98, 80])  # 2nd "a ce [98]"
# "ce [78]" total across 47 and 87
chk('47-78+87-78 total', len(s.starts(47, 78)) + len(s.starts(87, 78)), 7)
if fails:
    print(f"FAILURES: {fails}"); sys.exit(1)
print("CE47 BATTERY: all checks PASS")
