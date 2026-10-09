#!/usr/bin/env python3
"""Extract plain text from the downloaded fr-wikipedia parquet shards.
Writes wiki-fr-<shard>.txt per shard; prints sha256 + char counts."""
import pyarrow.parquet as pq, glob, hashlib, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
for p in sorted(glob.glob(os.path.join(HERE, "wiki-fr-*.parquet"))):
    t = pq.read_table(p, columns=["text"])
    texts = t.column("text").to_pylist()
    body = "\n\n".join(texts)
    out = p.replace(".parquet", ".txt")
    with open(out, "w", encoding="utf-8") as f:
        f.write(body)
    h = hashlib.sha256(body.encode("utf-8")).hexdigest()
    print(f"{os.path.basename(out)}: {len(body)} chars, sha256={h}")
