#!/usr/bin/env python3
from build_stream import load_stream
pairs = load_stream()
seq = [g for g,_,_ in pairs]
w62 = [i for i,g in enumerate(seq) if g=="62"]
KNOWN = {"11":"la","29":"er","40":"e","46":"que","47":"ce","77":"le","96":"par",
         "00":"pour","59":"est","62":"on","82":"m","24":"en","64":"qui","87":"ce","70":"pre"}
SIX = {360,425,1315,1349,1464,1569}
for i in w62:
    pre = seq[i-1] if i>0 else "##"
    post = seq[i+1] if i+1 < len(seq) else "##"
    p2 = seq[i+2] if i+2 < len(seq) else "##"
    tag = " <== 62-48" if i in SIX else ""
    print(f"@{i+1}: {pre}({KNOWN.get(pre,'?')}) [62] {post}({KNOWN.get(post,'?')}) {p2}({KNOWN.get(p2,'?')}){tag}")
