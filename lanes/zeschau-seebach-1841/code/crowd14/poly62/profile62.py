#!/usr/bin/env python3
from build_stream import load_stream
pairs = load_stream()
seq = [g for g,_,_ in pairs]
w62 = [i for i,g in enumerate(seq) if g=="62"]
print("n62 =", len(w62))
print("positions (1-based):", [i+1 for i in w62])
from collections import Counter
pre = Counter(seq[i-1] for i in w62 if i>0)
post = Counter(seq[i+1] for i in w62 if i+1 < len(seq))
print("pre-62:", pre.most_common())
print("post-62:", post.most_common())
