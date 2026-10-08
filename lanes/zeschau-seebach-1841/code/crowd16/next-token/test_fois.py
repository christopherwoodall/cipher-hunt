#!/usr/bin/env python3
"""Round-16 fois battery. Pre-registered bars in next-token-fois.md."""
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
chk('n17', s.G[17], 15)
chk('17 starts', s.starts(17),
    [17,238,308,369,452,556,837,880,925,1040,1157,1289,1461,1558,1757])
chk('17-11-26', s.starts(17,11,26), [238,1558])
chk('@238', P[236:243], [98,41,17,11,26,12,16])
chk('@1558', P[1556:1563], [61,40,17,11,26,30,6])
chk('17-77-82', s.starts(17,77,82), [1040,1157])
chk('77-82 frozen', s.starts(77,82), [1041,1158])
chk('26-12', s.BIG[(26,12)], 4)
chk('26-30 x4 (finder said 3)', s.BIG[(26,30)], 4)
chk('44/63 shared', set(s.suc_c(44)) & set(s.suc_c(63)), {0,74,11,77,29})
chk('@369', P[367:374], [61,70,17,6,21,65,63])
chk('70-17 sole', s.starts(70,17), [368])
chk('@308', P[306:313], [88,20,17,46,84,24,37])
chk('17-46 x1', s.starts(17,46), [308])
chk('01-24 x3', s.starts(1,24), [40,828,984])
chk('@1461', P[1459:1466], [66,79,17,1,21,62,48])
chk('@452', P[450:457], [48,79,17,77,60,65,13])
chk('@925', P[923:930], [65,71,17,61,96,48,82])
chk('@1757', P[1755:1762], [85,58,17,78,41,15,93])
chk('@17', P[15:22], [91,53,17,64,98,82,43])
chk('@880', P[878:885], [86,78,17,8,31,79,68])
if fails:
    print(f"FAILURES: {fails}"); sys.exit(1)
print("FOIS BATTERY: all checks PASS")
