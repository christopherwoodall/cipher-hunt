#!/usr/bin/env python3
"""Round-16 par-rest battery. Pre-registered bars in next-token-par-rest.md."""
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
chk('n96', s.G[96], 21); chk('n45', s.G[45], 22)
chk('96-00 x3', s.starts(96,0), [47,465,960])
chk('96-87-46 x3', s.starts(96,87,46), [224,952,1526])
chk('96-47-46', s.starts(96,47,46), [150])
chk('@314', P[310:320], [84,24,37,78,45,64,59,32,94,6])
chk('45-64', s.starts(45,64), [314,340,1024])
chk('96-45', s.starts(96,45), [602,1213])
chk('@602', P[600:607], [39,26,96,45,93,54,64])
chk('@1213', P[1211:1218], [32,48,96,45,36,77,83])
chk('@437', P[435:442], [78,63,45,46,43,98,80])
chk('45-46 x1', s.starts(45,46), [437])
chk('96-43-87-01', s.starts(96,43,87,1), [342,1026])
chk('11-43', s.starts(11,43), [562])
chk('43-00', s.starts(43,0), [244,1126,1544])
chk('@1544', P[1542:1549], [77,78,43,0,46,70,12])
chk('83-82 only x3', s.starts(83,82), [228,1061,1784])
chk('98-83 x5', s.starts(98,83), [227,897,930,1060,1783])
chk('@109', P[107:114], [46,11,21,67,93,29,89])
chk('96-86', s.starts(96,86), [947])
chk('@947', P[945:953], [62,98,96,86,1,77,86,96])
chk('82-16-96', s.starts(82,16,96), [1194])
chk('@1196 doubled', P[1194:1202], [82,16,96,82,16,64,29,45])
chk('96-48', s.starts(96,48), [927])
chk('@927', P[925:933], [17,61,96,48,82,98,83,56])
if fails:
    print(f"FAILURES: {fails}"); sys.exit(1)
print("PAR-REST BATTERY: all checks PASS")
