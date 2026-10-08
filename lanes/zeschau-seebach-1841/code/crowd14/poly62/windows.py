#!/usr/bin/env python3
from build_stream import load_stream
pairs = load_stream()
seq = [g for g,_,_ in pairs]
hits = [360, 425, 1315, 1349, 1464, 1569]
for h in hits:
    lo, hi = max(0,h-3), min(len(seq), h+5)
    ctx = [(i, seq[i], pairs[i][1]) for i in range(lo, hi)]
    mark = " ".join(f"[{g}@{i}]" if i in (h,h+1) else f"{g}@{i}" for i,g,_ in ctx)
    print(f"@{h} ({h+1}): {mark}")
    print("   row:", ", ".join(sorted(set(pairs[i][1] for i in range(lo,hi)))))
