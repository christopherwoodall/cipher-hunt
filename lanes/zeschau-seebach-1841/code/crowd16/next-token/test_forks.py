#!/usr/bin/env python3
"""Round-16 forks battery. Pre-registered bars in next-token-forks.md."""
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
chk('n67', s.G[67], 38); chk('n78', s.G[78], 31)
chk('n48', s.G[48], 38); chk('n94', s.G[94], 37)
voul = [i for i in s.starts(67) if P[i+1]==33 or (i+2<1847 and P[i+2]==29)]
chk('67 veut x8', voul, [110,272,1148,1390,1423,1450,1476,1623])
det = {11,77,47,87}
p78 = [P[i-1] for i in s.starts(78) if i>0]
p29 = [P[i-1] for i in s.starts(29) if i>0]
chk('78 det-pred', sum(1 for x in p78 if x in det), 16)
chk('29 det-pred', sum(1 for x in p29 if x in det), 2)
chk('78 after 33', sum(1 for i in s.starts(78) if i>0 and P[i-1]==33), 0)
chk('29 after 33', sum(1 for i in s.starts(29) if i>0 and P[i-1]==33), 5)
chk('78-45 x4', s.starts(78,45), [313,573,982,1164])
chk('@573 ce-verdict', P[571:579], [52,87,78,45,13,55,61,94])
chk('@982 ce-verdict', P[980:988], [76,47,78,45,1,24,89,48])
chk('@313/314 overlap', P[311:320],
    [24,37,78,45,64,59,32,94,6])
chk('94-59 nest x3', s.starts(94,59), [558,762,1795])
chk('94-82 neme x4', s.starts(94,82), [578,1182,1353,1742])
chk('62-48', s.BIG[(62,48)], 6); chk('62-94', s.BIG[(62,94)], 9)
chk('12-48', s.BIG[(12,48)], 5); chk('12-94', s.BIG[(12,94)], 3)
chk('82-48', s.BIG[(82,48)], 4); chk('82-94', s.BIG[(82,94)], 3)
chk('96-45', s.starts(96,45), [602,1213])
if fails:
    print(f"FAILURES: {fails}"); sys.exit(1)
print("FORKS BATTERY: all checks PASS")
