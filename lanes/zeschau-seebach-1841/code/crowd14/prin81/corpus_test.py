#!/usr/bin/env python3
"""Battery PRIN-81 corpus tests (crowd14/prin81). PREREG.md frozen before run.

Tests (lane tokenizer verbatim from round-10/11 arm1248, cf. dp_verify.py):
  T1 "la pour" bigram   -- the post-context adverse; reading A needs >=1 legit hit
  T2 "cela pour" bigram -- reading B grammaticality control
  T3 "le prince la"     -- reading-A exact frame (pre+window+post)
  T4 "le prince"        -- sanity baseline (must be >0 or corpus is wrong pool)
  T5 "prince pour"      -- alt post-context sanity
  T6 "et le prince"    -- pre-context frame sanity
Every hit is constituency-read (printed) to catch OCR/sentence-boundary noise.
"""
import re
from pathlib import Path

LANE = Path.home() / 'workspace/cipher-hunt/lanes/zeschau-seebach-1841'
CORP = LANE / 'code/side-period/corpus'

def tok(text):
    text = text.lower().replace('\u2019', "'").replace('\u2018', "'")
    text = re.sub(r"([a-z\u00e0-\u00ff])'([a-z\u00e0-\u00ff])", r'\1 \2', text)
    return re.findall(r'[a-z\u00e0-\u00ff]+', text)

files = sorted(CORP.glob('*.txt'))
print(f"pool: {len(files)} files")

def ctx(t, i, half=12):
    return ' '.join(t[max(0, i - half):i + half + 1])

def ngram_hits(tokens_list, pat):
    k = len(pat)
    hits = []
    for fn, t in tokens_list:
        for i in range(len(t) - k + 1):
            if tuple(t[i:i + k]) == pat:
                hits.append((fn, i, ctx(t, i)))
    return hits

tokens_list = []
total_tok = 0
for f in files:
    t = tok(f.read_text(encoding='utf-8', errors='replace'))
    tokens_list.append((f.name, t))
    total_tok += len(t)
print(f"total tokens: {total_tok}")

tests = {
    'T1 la+pour': ('la', 'pour'),
    'T2 cela+pour': ('cela', 'pour'),
    'T3 le+prince+la': ('le', 'prince', 'la'),
    'T4 le+prince': ('le', 'prince'),
    'T5 prince+pour': ('prince', 'pour'),
    'T6 et+le+prince': ('et', 'le', 'prince'),
}
results = {}
for name, pat in tests.items():
    hits = ngram_hits(tokens_list, pat)
    results[name] = hits
    print(f"\n=== {name}: {len(hits)} hits ===")
    for fn, i, c in hits[:8]:
        print(f"  [{fn}@{i}] ...{c}...")
    if len(hits) > 8:
        print(f"  ... +{len(hits) - 8} more")

import json
out = LANE / 'code/crowd14/prin81/corpus_results.json'
out.write_text(json.dumps(
    {k: [{'file': fn, 'idx': i, 'ctx': c} for fn, i, c in v]
     for k, v in results.items()},
    ensure_ascii=False, indent=1))
print(f"\nwrote {out}")
