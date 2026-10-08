#!/usr/bin/env python3
"""Round-16 classes battery. Pre-registered bars in next-token-classes.md."""
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
chk('n31', s.G[31], 8); chk('n33', s.G[33], 25)
chk('67-33 x6 correction', s.starts(67,33), [272,1148,1423,1450,1476,1623])
chk('33-29 x5', s.starts(33,29), [273,626,1232,1424,1477])
chk('00-33 x8', s.starts(0,33), [185,407,466,845,935,1087,1244,1629])
chk('64-33 zero', s.starts(64,33), [])
chk('67-33-46 x2', s.starts(67,33,46), [1450,1623])
chk('47-33 x2', s.starts(47,33), [23,1231])
chk('33-21', s.starts(33,21), [936,1421,1630])
chk('33-21-64-37 x2', s.starts(33,21,64,37), [936,1630])
chk('31 followers distinct', sorted(s.suc_c(31).items()),
    [(10,1),(11,1),(14,1),(24,1),(29,1),(76,1),(79,1),(92,1)])
chk('31 lefts', sorted(s.pre_c(31).items()), [(8,3),(11,1),(48,1),(61,1),(64,2)])
chk('31-79', s.starts(31,79), [882])
chk('11-31-11', s.starts(11,31,11), [1515])
chk('31-24', s.starts(31,24), [1521])
chk('03-64-31', s.starts(3,64,31), [336,1645])
chk('33-00-86-56 x2', s.starts(33,0,86,56), [1000,1504])
chk('67-33-29 x3', s.starts(67,33,29), [272,1423,1476])
if fails:
    print(f"FAILURES: {fails}"); sys.exit(1)
print("CLASSES BATTERY: all checks PASS")
