#!/usr/bin/env python3
"""Round-16 est battleground battery. Pre-registered bars in next-token-est.md."""
import sys, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import streamkit as s

fails = []
def chk(name, got, want):
    ok = got == want
    print(f"[{'OK' if ok else 'FAIL'}] {name}: got={got} want={want}")
    if not ok: fails.append(name)

P = s.P
CLS = json.loads((s.LANE / 'code/crowd10/conditioner59/classification.json').read_text())
cls = lambda k: CLS[str(k)]['class']

chk('37 legs LEFTOVER x6', [cls(k) for k in (528,624,912,1178,1443,1796)], ['LEFTOVER']*6)
chk('59->37', s.starts(59, 37), [528,624,912,1178,1443,1796])
chk('@1794 single window', P[1794:1798], [42,94,59,37])
chk('32: 316/1210 EST, 448 ESTE', (cls(316), cls(1210), cls(448)), ('EST','EST','ESTE'))
chk('59->32', s.starts(59, 32), [316,448,1210])
chk('42: 463 LEFTOVER, 1186 ESTE', (cls(463), cls(1186)), ('LEFTOVER','ESTE'))
chk('59->42', s.starts(59, 42), [463,1186])
chk('19: 1777 EST', cls(1777), 'EST')
chk('59->19', s.starts(59, 19), [1777])
chk('30: 559 EST, 1715 ESTE', (cls(559), cls(1715)), ('EST','ESTE'))
chk('59->30', s.starts(59, 30), [559,1715])
chk('39: 763 EST; 45: 103 EST', (cls(763), cls(103)), ('EST','EST'))
chk('EST-class keys exactly 6', sorted(k for k,v in CLS.items() if v['class']=='EST'),
    ['103','1210','1777','316','559','763'])
# 32's verb-position tension: 64->32 direct (59 not between)
direct = [i for i in s.starts(64,32)]
chk('64->32 direct starts', direct, [32,854])  # bigram starts; finder cited 32-cells +1
chk('26->32 count', s.BIG[(26,32)], 2)
chk('56->32 count', s.BIG[(56,32)], 2)
chk('91->32 count', s.BIG[(91,32)], 2)
# 37 unfenced-position anchors for the TIER-2 lead
chk('37-01 starts', s.starts(37,1), [939,1633,1817])  # finder said x2; A12 grant is x3
chk('37-78 starts', s.starts(37,78), [312,414,475,1770])  # finder cited only the en-pre x2
chk('32->48 count', s.BIG[(32,48)], 4)
if fails:
    print(f"FAILURES: {fails}"); sys.exit(1)
print("EST BATTERY: all checks PASS")
