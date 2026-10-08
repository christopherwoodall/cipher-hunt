#!/usr/bin/env python3
"""Round-16 er battery. Pre-registered bars in next-token-er.md."""
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
chk('n29', s.G[29], 45)
pc47 = s.pre_c(47)
chk('29 joint-top pre of 47', (pc47[29], pc47[76]), (4, 4))
chk('29-47', s.starts(29,47), [22,422,1230,1590])
chk('@22', P[20:27], [82,43,29,47,33,55,81])
chk('@1230', P[1228:1235], [82,48,29,47,33,29,85])
chk('29-47-33', s.starts(29,47,33), [22,1230])
chk('29-40-65', s.starts(29,40,65), [291,685,1710])
chk('86-29', s.starts(86,29), [431,1375,1391,1825])
chk('29-89-84', s.starts(29,89,84), [274,1376])
chk('29-87', s.starts(29,87), [147,627,1425])
chk('29-82-16', s.starts(29,82,16), [432,1478])
chk('46-85-29 zero', s.starts(46,85,29), [])
chk('@95 actual 46-29-85', P[93:100], [81,97,46,29,85,8,21])
chk('46-29', s.starts(46,29), [95,217])
chk('11-29', s.starts(11,29), [77,499])
chk('@1031', P[1029:1036], [1,3,29,80,77,11,70])
chk('@1155', P[1153:1160], [0,92,29,80,17,77,82])
chk('@274', P[272:279], [67,33,29,89,84,91,37])
chk('@1389', P[1387:1394], [16,6,29,67,86,29,89])
chk('29 pre top', s.pre_c(29).most_common(3), [(33,5),(86,4),(6,4)])
if fails:
    print(f"FAILURES: {fails}"); sys.exit(1)
print("ER BATTERY: all checks PASS")
