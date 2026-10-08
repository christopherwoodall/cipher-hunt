#!/usr/bin/env python3
"""Round-16 tout battery tests. Pre-registered bars in next-token-tout.md.
Every cipher-side number asserted; nonzero exit on mismatch."""
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
chk('n79', s.G[79], 18)
chk('79->17 starts', s.starts(79, 17), [451, 1460])
chk('79->87->11', s.starts(79, 87, 11), [460])
chk('79->87->64', s.starts(79, 87, 64), [1799])
chk('79->80', s.starts(79, 80), [468, 1010, 1089])
g1 = P[466:466+6]; g2 = P[1087:1087+6]
chk('00-33-79-80-06 @466', g1[:5], [0, 33, 79, 80, 6])
chk('00-33-79-80-06 @1087 identical', g2[:5], g1[:5])
chk('@466 6th cell', g1[5], 67); chk('@1087 6th cell', g2[5], 43)
chk('79-82-48', s.starts(79, 82, 48), [396, 1227])
chk('@394 6-mer (79@396)', P[394:400], [67, 64, 79, 82, 48, 6])
chk('@1225 6-mer (79@1227)', P[1225:1231], [57, 64, 79, 82, 48, 29])
chk('@494 (79@496)', P[494:500], [94, 2, 79, 88, 47, 11])
chk('all 18 starts', s.starts(79), [50,53,396,451,460,468,496,594,883,1010,1089,1227,1364,1419,1460,1682,1688,1799])
chk('@1010 full', P[1008:1014], [35, 18, 79, 80, 78, 47])
chk('79->14 x2', s.starts(79, 14), [1364, 1688])
# "tout en" proxy: 79->24 (en) count; "tout à coup" proxy: no phrase needed, just census
chk('79->24 count', s.BIG[(79, 24)], 0)
chk('79->46 (tout que) count', s.BIG[(79, 46)], 0)
# successors/predecessors census vs finder table
chk('79 pre spread count', len(s.pre_c(79)), 13)
chk('79 suc spread count', len(s.suc_c(79)), 11)

if fails:
    print(f"FAILURES: {fails}"); sys.exit(1)
print("TOUT BATTERY: all checks PASS")
