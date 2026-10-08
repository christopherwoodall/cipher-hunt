#!/usr/bin/env python3
"""Round-16 pour battery. Pre-registered bars in next-token-pour.md."""
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
chk('n00', s.G[0], 55)
fc = s.suc_c(0)
chk('follower census', {k: fc[k] for k in (86,33,66,92,97,11,46,36)},
    {86:12, 33:8, 66:7, 92:6, 97:4, 11:4, 46:4, 36:3})
sing = sorted(k for k,v in fc.items() if v == 1)
chk('singletons', sing, [13,20,34,44,64,67,98])  # finder missed 67
chk('@106 window', P[106:111], [0,46,11,21,67])
chk('@1244 window', P[1244:1255], [0,33,16,0,67,46,26,30,6,65,46])
chk('@1545 flagship', P[1545:1550], [0,46,70,12,94])
chk('@1680', P[1680:1685], [0,46,79,65,13])
chk('@545', P[545:550], [0,46,24,47,46])
chk('@864 (ce47 handoff)', P[861:868], [74,74,48,47,46,0,86])
chk('00-86-56 x4', s.starts(0,86,56), [961,1001,1505,1791])
chk('00-86-29 x2', s.starts(0,86,29), [1374,1824])
chk('@552', P[552:557], [0,86,59,34,17])
chk('@667', P[667:672], [0,20,67,11,86])
chk('@1287', P[1287:1292], [0,11,17,84,59])
chk('@1822 double-00', P[1822:1827], [0,97,0,86,29])
chk('@76', P[76:81], [0,11,29,42,98])
chk('@845', P[845:850], [0,33,96,40,62])
chk('@185/@1244 00-33-16', (P[185:188], P[1244:1247]), ([0,33,16],[0,33,16]))
chk('@935/@1629 00-33-21', (P[935:938], P[1629:1632]), ([0,33,21],[0,33,21]))
chk('@378', P[378:383], [0,11,50,82,16])
chk('@1405', P[1405:1410], [0,11,95,46,52])
chk('@27', P[27:32], [0,34,24,30,3])
chk('@748', P[748:753], [0,64,2,97,40])
if fails:
    print(f"FAILURES: {fails}"); sys.exit(1)
print("POUR BATTERY: all checks PASS")
