#!/usr/bin/env python3
"""Round-16 pre battery. Pre-registered bars in next-token-pre.md."""
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
chk('62-94', s.BIG[(62,94)], 9)
chk('94-59', s.starts(94,59), [558,762,1795])
chk('94-82', s.starts(94,82), [578,1182,1353,1742])
chk('94-82 followers', [P[580],P[1184],P[1355],P[1744]], [6,6,6,46])
chk('70-12-94', s.starts(70,12,94), [347,1547])
chk('@347', P[345:353], [1,6,70,12,94,74,67,78])
chk('@1547', P[1545:1553], [0,46,70,12,94,92,45,23])
chk('12-48 count (finder said 7)', s.BIG[(12,48)], 5)
chk('12-48 starts', s.starts(12,48), [169,709,809,1075,1736])
chk('@64', P[62:67], [29,40,12,94,92])
chk('12-34', s.starts(12,34), [1740])
chk('70-12-06', s.starts(70,12,6), [1118])
chk('64-39 x1 (finder implied frame)', s.starts(64,39), [606])
chk('70-39-11', s.starts(70,39,11), [1067,1604])
chk('59-39', s.starts(59,39), [763,1511])
chk('@763', P[761:766], [62,94,59,39,88])
chk('03-39', s.BIG[(3,39)], 3)
chk('70-98-41', s.starts(70,98,41), [235])
chk('98-41 global', s.BIG[(98,41)], 1)
chk('70-91-77', s.starts(70,91,77), [519])
chk('91-11', s.BIG[(91,11)], 2)
chk('70-88-10', s.starts(70,88,10), [615])
chk('@1067', P[1065:1072], [62,18,70,39,11,44,74])
chk('82-48 followers', [P[i+2] for i in s.starts(82,48)], [11,0,6,29])
chk('@368', P[366:372], [49,61,70,17,6,21])
chk('@1586', P[1584:1590], [0,36,70,64,65,48])
if fails:
    print(f"FAILURES: {fails}"); sys.exit(1)
print("PRE BATTERY: all checks PASS")
