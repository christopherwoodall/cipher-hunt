#!/usr/bin/env python3
"""value52 deep-dive: era candidacy for 'la 52', allophone frame detail,
per-window est-frame table, and the la-frame inversion."""
import json, os, re, unicodedata
from collections import Counter

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
OUTDIR = os.path.join(LANE, 'code', 'crowd14', 'value52')

def load_stream():
    offsets = json.load(open(os.path.join(LANE, 'code', 'side-keyhunt', 'repaired_offsets.json')))
    pairs = []
    for line in open(os.path.join(LANE, 'data', 'upstream-ct_R5005.txt')):
        line = line.strip()
        if not line:
            continue
        lid, digits = line.split()
        digits = re.sub(r'\D', '', digits)
        d = digits[offsets.get(lid, 0):]
        for i in range(0, len(d) - 1, 2):
            pairs.append(int(d[i:i + 2]))
    assert len(pairs) == 1847
    return pairs

s = load_stream()
def win_of(g):
    return [(i, s[i-1] if i > 0 else None, s[i+1] if i < len(s)-1 else None) for i, v in enumerate(s) if v == g]
w52 = win_of(52); w59 = win_of(59)
res = {}

# la-frame census for 11
w11 = win_of(11)
res['n11'] = len(w11)
res['la_suc_dist'] = {k: v for k, v in Counter(q for _, _, q in w11).most_common()}
res['la52_pos'] = [i for i, p, q in w52 if p == 11]
res['la59_pos'] = [i for i, p, q in w59 if p == 11]
res['la52_detail'] = [{'pos': i, 'pre2': s[i-2] if i > 1 else None, 'suc': q,
                       'suc2': s[i+2] if i < len(s)-2 else None,
                       'win': s[max(0,i-3):i+4]} for i, p, q in w52 if p == 11]
res['la59_detail'] = [{'pos': i, 'pre2': s[i-2] if i > 1 else None, 'suc': q,
                       'suc2': s[i+2] if i < len(s)-2 else None,
                       'win': s[max(0,i-3):i+4]} for i, p, q in w59 if p == 11]

# shared predecessors detail with counts
p52 = Counter(p for _, p, _ in w52); p59 = Counter(p for _, p, _ in w59)
q52 = Counter(q for _, _, q in w52); q59 = Counter(q for _, _, q in w59)
res['pre_shared_detail'] = {p: {'n52': p52[p], 'n59': p59[p]}
                            for p in sorted(set(p52) & set(p59))}
res['suc_shared_detail'] = {q: {'n52': q52[q], 'n59': q59[q]}
                            for q in sorted(set(q52) & set(q59))}
# for each shared predecessor: do the (pre,suc) frames differ?
res['shared_pre_frame_split'] = {}
for p in sorted(set(p52) & set(p59)):
    s52 = sorted(set(q for i, pp, q in w52 if pp == p))
    s59 = sorted(set(q for i, pp, q in w59 if pp == p))
    res['shared_pre_frame_split'][p] = {'suc_after_52': s52, 'suc_after_59': s59,
                                       'overlap': sorted(set(s52) & set(s59))}
# est-arm frames for 59 vs 52
res['estarm_52'] = [(i, p, q) for i, p, q in w52 if p in (64, 94, 93)]
res['estarm_59'] = [(i, p, q) for i, p, q in w59 if p in (64, 94, 93)]

# era: full P(w|la) ranking + in-band list
FRENCH_CLEAN = ['guizot-memoires-t1-gutenberg.txt', 'guizot-memoires-t2-gutenberg.txt',
                'guizot-memoires-t3-gutenberg.txt', 'guizot-memoires-t5-t6.txt',
                'metternich-papiere-v4.txt', 'metternich-papiere-v6.txt',
                'pozzo-di-borgo-correspondance-v1.txt',
                'levant-correspondence-1841-p3.txt', 'talleyrand-memoires-v1.txt',
                'revue-deux-mondes-1841-q1.txt', 'revue-deux-mondes-1841-q2.txt',
                'revue-deux-mondes-1841-q3.txt', 'revue-deux-mondes-1841-q4.txt']
WORD = re.compile(r"[a-z\xe0\xe2\xe4\xe9\xe8\xea\xeb\xee\xef\xf4\xf6\xf9\xfb\xfc\xff\xe7\u0153\xe6]+(?:'[a-z\xe0\xe2\xe4\xe9\xe8\xea\xeb\xee\xef\xf4\xf6\xf9\xfb\xfc\xff\xe7\u0153\xe6]+)*")
def tokenize(text):
    text = unicodedata.normalize('NFC', text.lower().replace('\u2019', "'").replace('\u2018', "'"))
    toks = []
    for m in WORD.finditer(text):
        w = m.group(0)
        parts = w.split("'")
        for i, p in enumerate(parts):
            if not p: continue
            toks.append(p + "'" if i < len(parts) - 1 else p)
    return toks
toks = []
for f in FRENCH_CLEAN:
    toks += tokenize(open(os.path.join(LANE, 'code', 'side-period', 'corpus', f),
                          encoding='utf-8', errors='replace').read())
la_next = Counter(); n_la = 0
for i, t in enumerate(toks):
    if t == 'la':
        n_la += 1
        if i + 1 < len(toks): la_next[toks[i+1]] += 1
target = 3/45
inband = [(w, c, c/n_la, (c/n_la)/target) for w, c in la_next.most_common(200)
          if 0.5 <= (c/n_la)/target <= 2.0]
res['era_P_w_given_la_inband'] = inband
res['era_n_la'] = n_la
# trigram-level: era "la W X" for in-band W, to see what follows
res['era_laW_suc'] = {}
for w, c, p, r in inband:
    fol = Counter()
    for i, t in enumerate(toks):
        if t == 'la' and i + 1 < len(toks) and toks[i+1] == w and i + 2 < len(toks):
            fol[toks[i+2]] += 1
    res['era_laW_suc'][w] = fol.most_common(8)

json.dump(res, open(os.path.join(OUTDIR, 'value52_deep.json'), 'w'), indent=1, ensure_ascii=False)
print('n11 =', res['n11'])
print('la52:', res['la52_detail'])
print('la59:', res['la59_detail'])
print('shared-pre frame split:')
for p, d in res['shared_pre_frame_split'].items():
    print('  pre=%d  suc|52=%s  suc|59=%s  overlap=%s' % (p, d['suc_after_52'], d['suc_after_59'], d['overlap']))
print('estarm_52:', res['estarm_52'])
print('estarm_59:', res['estarm_59'])
print('in-band P(w|la):', [(w, c, round(p,4), round(r,2)) for w, c, p, r in inband])
print('laW successors:', json.dumps(res['era_laW_suc'], ensure_ascii=False))
