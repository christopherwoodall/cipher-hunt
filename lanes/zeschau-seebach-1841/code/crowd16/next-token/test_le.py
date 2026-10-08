#!/usr/bin/env python3
"""Round-16 le battery. Pre-registered bars in next-token-le.md."""
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
CLS = json.loads(Path(s.LANE / 'code/crowd10/conditioner59/classification.json').read_text())
chk('n77', s.G[77], 44)
chk('@832 cela-boundary', P[828:838], [1,24,87,11,77,76,59,35,56,17])
chk('@1034', P[1030:1042], [3,29,80,77,11,70,82,34,29,40,17,77])
chk('@1042', P[1040:1048], [17,77,82,63,11,67,76,85])
chk('@516 ce-le-80', P[514:521], [56,87,77,80,9,70,91])
chk('@870 ce-le-89', P[868:875], [70,87,77,89,48,20,74])
chk('87-77-80', s.starts(87,77,80), [515])
chk('87-77-89', s.starts(87,77,89), [869])
chk('77-76', s.starts(77,76), [832,891,968])
chk('@1189', P[1186:1194], [59,42,6,84,59,46,7,24])
chk('class(59@1190)', CLS['1190']['class'], 'ESTE')
chk('@1447', P[1445:1452], [64,77,84,59,36,67,33])
chk('class(59@1448)', CLS['1448']['class'], 'ESTE')
chk('@1803', P[1801:1808], [64,77,84,59,35,94,52])
chk('class(59@1804)', CLS['1804']['class'], 'ESTE')
chk('class(59@1291)', CLS['1291']['class'], 'FENCED')
chk('84-59-46 x1', s.starts(84,59,46), [1189])
chk('77-81', s.starts(77,81), [744,1240,1401,1598])
chk('81-87-11', s.starts(81,87,11), [1241,1402])
chk('77-86', s.starts(77,86), [430,798,877,950,1133])
chk('86-29', s.starts(86,29), [431,1375,1391,1825])
chk('06-77-76', s.starts(6,77,76), [890,967])
chk('@1046', P[1044:1051], [11,67,76,85,41,88,29])
chk('77 suc top', s.suc_c(77).most_common(5),
    [(78,7),(84,7),(86,5),(81,4),(76,3)])
if fails:
    print(f"FAILURES: {fails}"); sys.exit(1)
print("LE BATTERY: all checks PASS")
