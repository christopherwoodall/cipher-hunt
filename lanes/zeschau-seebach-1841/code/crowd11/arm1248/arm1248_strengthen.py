#!/usr/bin/env python3
"""@1248 ARM STRENGTHENER (round 11, WO5). Implements PREREG.md bars.

New legs for the two weak fenced arms ("peu" 2/4, infinitive-"empêcher" 2/4):
  P-A: "pour peu que" attestation in new-corpus pool {RDM-1841, Guizot-DIP}
  P-B: construction-shape stability (verb-offset 3, clause-length 4) on P-A hits
  P-C: @471 "X peu que" hostability in v8 (discriminating both ways)
  P-D: "pour W1 W2 pour peu que" stacked license in {v8,RDM,Guizot}
  E-A: "pour INF que" class breadth (>=2 distinct infinitives) in {RDM,Guizot}
  E-B: "MODAL empêcher que" @471 license in v8
  E-C: "pour W1 W2 pour INF que" stacked license in {v8,RDM,Guizot}

Writes arm1248_strengthen_raw.json (all hit contexts for reading).
The worker READS every hit (constituency standard) and records the
adjudication in arm1248_strengthen_results.json (separate step).
"""
import json, os, re, sys
from collections import Counter

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
HERE = os.path.dirname(os.path.abspath(__file__))
CORP = os.path.join(LANE, 'code', 'side-period', 'corpus')

# ---------- lane tokenizer verbatim (round-10 arm1248.py) ----------
def tok(text):
    text = text.lower().replace('\u2019', "'").replace('\u2018', "'")
    text = re.sub(r"([a-z\u00e0-\u00ff])'([a-z\u00e0-\u00ff])", r'\1 \2', text)
    return re.findall(r'[a-z\u00e0-\u00ff]+', text)

def is_inf(w):
    return w.endswith(('er', 'ir', 're')) and len(w) > 3

# ---------- corpora ----------
def load(p):
    return open(os.path.join(CORP, p), encoding='utf-8', errors='replace').read()

raw_v8_full = load('nesselrode-v8.txt')
# v8 doc split (round-10 splitter, for hit provenance)
months = 'janvier|février|fevrier|mars|avril|mai|juin|juillet|août|aout|septembre|octobre|novembre|décembre|decembre'
pat = re.compile(r'^((?:Saint-Pétersbourg|Berlin|Paris|Londres|Vienne|Varsovie|Constantinople|Munich|Dresde)[ ,\.\u00a0]*\d{1,2}\s+(?:%s)\s+184[0-6])\.?,?\s*$' % months, re.M)
bounds = [m.start() for m in pat.finditer(raw_v8_full)]
v8_docs = [raw_v8_full[a:b] for a, b in zip(bounds, bounds[1:] + [len(raw_v8_full)])]
assert len(v8_docs) == 97, len(v8_docs)

pool = {}   # name -> raw text
for q in ['q1', 'q2', 'q3', 'q4']:
    pool['RDM-1841-%s' % q] = load('revue-deux-mondes-1841-%s.txt' % q)
pool['Guizot-DIP'] = load('guizot-memoires-t5-t6.txt')
pool_tok = {k: tok(v) for k, v in pool.items()}
v8_tok = [tok(d) for d in v8_docs]

def ctx(tokens, i, half=15):
    lo, hi = max(0, i - half), min(len(tokens), i + half + 1)
    return ' '.join(tokens[lo:hi])

# ---------- P-A: "pour peu que" in pool ----------
pa_hits = []
for name, t in pool_tok.items():
    for i in range(len(t) - 2):
        if t[i] == 'pour' and t[i+1] == 'peu' and t[i+2] == 'que':
            pa_hits.append({'corpus': name, 'tokpos': i,
                            'context': ctx(t, i, 18)})

# clause raw-text extraction for P-B: raw substring from "pour peu que"
# to next sentence-terminal punctuation (fallback: 25 tokens)
def clause_after(raw, start_hint):
    low = raw.lower()
    idx = low.find('pour peu que', start_hint - 200 if start_hint > 200 else 0)
    # find the occurrence nearest start_hint: search all, take closest
    best, bestd = -1, None
    s = 0
    while True:
        j = low.find('pour peu que', s)
        if j < 0:
            break
        d = abs(j - start_hint)
        if bestd is None or d < bestd:
            best, bestd = j, d
        s = j + 1
    if best < 0:
        return None
    seg = raw[best:best + 1200]
    m = re.search(r'[.;:!?]', seg)
    cut = m.start() if m else 1200
    clause_raw = seg[:cut]
    ct = tok(clause_raw)
    # locate 'que' index of the locution inside clause tokens
    qi = None
    for k in range(len(ct) - 2):
        if ct[k] == 'pour' and ct[k+1] == 'peu' and ct[k+2] == 'que':
            qi = k + 2
            break
    return {'raw': clause_raw[:400], 'tokens': ct[:30], 'que_idx': qi}

# map token positions to approx char offsets for clause_after
pa_clauses = []
for h in pa_hits:
    name = h['corpus']
    approx_char = int(h['tokpos'] / max(1, len(pool_tok[name])) * len(pool[name]))
    pa_clauses.append(clause_after(pool[name], approx_char))

# ---------- E-A: "pour INF que" middles in pool ----------
ea_hits = []
for name, t in pool_tok.items():
    for i in range(len(t) - 2):
        if t[i] == 'pour' and t[i+2] == 'que' and is_inf(t[i+1]):
            ea_hits.append({'corpus': name, 'tokpos': i, 'inf': t[i+1],
                            'context': ctx(t, i, 18)})

# ---------- E-C: "pour W1 W2 pour INF que" in {v8 docs, pool} ----------
def stacked_hits(t, name, inf_required):
    out = []
    for i in range(len(t) - 5):
        if (t[i] == 'pour' and t[i+3] == 'pour' and t[i+5] == 'que'
                and is_inf(t[i+4]) == inf_required
                and (inf_required or t[i+4] == 'peu')):
            out.append({'corpus': name, 'tokpos': i,
                        'w1': t[i+1], 'w2': t[i+2], 'head': t[i+4],
                        'context': ctx(t, i, 20)})
    return out

ec_hits, pd_hits = [], []
for di, t in enumerate(v8_tok):
    ec_hits += stacked_hits(t, 'v8-doc%d' % di, True)
    pd_hits += stacked_hits(t, 'v8-doc%d' % di, False)
for name, t in pool_tok.items():
    ec_hits += stacked_hits(t, name, True)
    pd_hits += stacked_hits(t, name, False)

# ---------- E-B: "MODAL empêcher que" in v8 (raw regex, constituency-read) ----------
modals = ('veut|veulent|voulait|voulaient|voudrait|voudraient|veux|'
          'peut|peuvent|pouvait|pouvaient|pourrait|pourraient|peux|'
          'doit|doivent|devait|devaient|devrait|devraient|dois|'
          'faut|fallait|faudrait')
eb_pat = re.compile(r'\b(%s)\s+emp[eê]cher\s+que\b' % modals)
eb_hits = []
for di, raw in enumerate(v8_docs):
    low = raw.lower()
    for m in eb_pat.finditer(low):
        s = max(0, m.start() - 300)
        e = min(len(raw), m.end() + 300)
        eb_hits.append({'corpus': 'v8-doc%d' % di, 'charpos': m.start(),
                        'modal': m.group(1),
                        'context': re.sub(r'\s+', ' ', raw[s:e])[:600]})

# ---------- P-C: "X peu que" in v8 (raw regex, enumerate all X) ----------
pc_pat = re.compile(r'\b([a-zàâäéèêëîïôöùûüç]+)\s+peu\s+que\b')
pc_hits = []
for di, raw in enumerate(v8_docs):
    low = raw.lower()
    for m in pc_pat.finditer(low):
        s = max(0, m.start() - 250)
        e = min(len(raw), m.end() + 250)
        pc_hits.append({'corpus': 'v8-doc%d' % di, 'charpos': m.start(),
                        'x': m.group(1),
                        'context': re.sub(r'\s+', ' ', raw[s:e])[:500]})
pc_x_counts = Counter(h['x'] for h in pc_hits)

# ---------- cipher side: 06 profile (descriptive, for E-B / P-C compatibility) ----------
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd4'))
from repaired_parse import load_pairs_repaired
pairs, _, _ = load_pairs_repaired()
N = len(pairs)
pos06 = [i for i in range(N) if pairs[i] == '06']
fol06 = Counter(pairs[i+1] for i in range(N-1) if pairs[i] == '06')
pre06 = Counter(pairs[i-1] for i in range(1, N) if pairs[i] == '06')
# 06 as 67-predecessor positions
pos06_pre67 = [i for i in range(1, N) if pairs[i] == '67' and pairs[i-1] == '06']
# @471 window
w471 = [(i, pairs[i]) for i in range(465, 480)]

raw_out = {
    'corpora': {k: {'chars': len(v), 'tokens': len(pool_tok[k])} for k, v in pool.items()},
    'v8_docs': 97,
    'P-A': {'n': len(pa_hits), 'hits': pa_hits, 'clauses': pa_clauses},
    'E-A': {'n': len(ea_hits), 'hits': ea_hits},
    'E-C': {'n': len(ec_hits), 'hits': ec_hits},
    'P-D': {'n': len(pd_hits), 'hits': pd_hits},
    'E-B': {'n': len(eb_hits), 'hits': eb_hits},
    'P-C': {'n': len(pc_hits), 'x_counts': dict(pc_x_counts), 'hits': pc_hits},
    'cipher06': {'n06': len(pos06), 'positions': pos06,
                 'followers': dict(fol06), 'predecessors': dict(pre06),
                 'as_67_predecessor': pos06_pre67},
    'w471': ['%d:%s' % (i, g) for i, g in w471],
}
json.dump(raw_out, open(os.path.join(HERE, 'arm1248_strengthen_raw.json'), 'w'),
          indent=1, ensure_ascii=False)

print('=== corpus sizes ===')
for k, v in raw_out['corpora'].items():
    print(' ', k, v)
print('=== hit counts ===')
print(' P-A pour-peu-que (pool):', len(pa_hits))
print(' E-A pour-INF-que (pool):', len(ea_hits))
print(' E-C stacked pour-INF (v8+pool):', len(ec_hits))
print(' P-D stacked pour-peu (v8+pool):', len(pd_hits))
print(' E-B MODAL-empecher-que (v8):', len(eb_hits))
print(' P-C X-peu-que (v8):', len(pc_hits), '| distinct X:', len(pc_x_counts))
print('  X counts:', dict(pc_x_counts.most_common(20)))
print('=== cipher 06 === n06 =', len(pos06))
print(' 06 as 67-predecessor at:', pos06_pre67)
print(' w471:', ' '.join(raw_out['w471']))
