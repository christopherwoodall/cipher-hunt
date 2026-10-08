#!/usr/bin/env python3
"""FORK-78 resolver (round 14, WO6): positional polyvalence test for 78={ver,er}.

H1: 78="ver" word-INITIAL, 78="er" word-NON-INITIAL.
Per PREREG.md (written before the table was computed).
Repaired stream from code/side-keyhunt/repaired_offsets.json (NEVER canonical.py).
"""
import json, os, re, random
from collections import Counter

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
OUT = os.path.join(LANE, 'code', 'crowd14', 'fork78')

# ---------------- repaired stream (loader logic from code/crowd4/repaired_parse.py)
def load_pairs_repaired():
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
            pairs.append(d[i:i + 2])
    assert len(pairs) == 1847, len(pairs)
    assert pairs[754:760] == ['11', '70', '82', '34', '29', '40']
    assert pairs[1034:1040] == ['11', '70', '82', '34', '29', '40']
    return pairs

pairs = load_pairs_repaired()
N = len(pairs)

def windows_of(g):
    out = []
    for i, p in enumerate(pairs):
        if p == g:
            pre = pairs[i - 1] if i > 0 else '##'
            suc = pairs[i + 1] if i < N - 1 else '##'
            out.append((i, pre, suc))
    return out

w78 = windows_of('78')
w76 = windows_of('76')

# ---------------- F107 segments: coverage check
segs = json.load(open(os.path.join(LANE, 'code', 'crowd13', 'segmenter', 'word_boundaries.json')))['segments']
assert len(segs) == 32
def f107_classify(i):
    for s in segs:
        if s['start'] <= i < s['end']:
            cells = s['word']
            k = i - s['start']
            pos = 'INITIAL' if k == 0 else ('FINAL' if k == len(cells) - 1 else 'MEDIAL')
            return pos, s['gloss'], s['tier'], s['status']
    return None
cov78 = [(i, f107_classify(i)) for i, _, _ in w78 if f107_classify(i)]
cov76 = [(i, f107_classify(i)) for i, _, _ in w76 if f107_classify(i)]

# ---------------- position rules (PREREG)
GT_WORD = {'11', '46'}            # la, que — GT complete words
PROV_WORD = {'87', '64', '96'}    # ce, qui, par — provisional complete words
MED_WORD = {'37'}                 # le — MEDIUM
PROVCOND_WORD = {'77'}            # le — provisional-conditioned
WORD_CELLS = GT_WORD | PROV_WORD | MED_WORD | PROVCOND_WORD

def position_of(i, pre, suc, group):
    """Return (position, tier). 5-mer special cases for 78."""
    if group == '78' and i == 1181:
        return 'MEDIAL', 'special: gouv|er|ne|m|ent LEAD (F70)'
    if group == '78' and i == 1352:
        return 'CONTESTED', 'special: R-c granted solo vs killed R-b medial (F70)'
    pre_init = pre in WORD_CELLS
    suc_fin = suc in WORD_CELLS
    if pre_init and suc_fin:
        return 'SOLO', 'both'
    if pre_init:
        tier = 'GT' if pre in GT_WORD else ('prov' if pre in PROV_WORD else ('MED' if pre in MED_WORD else 'provcond'))
        return 'INITIAL', tier
    if suc_fin:
        return 'FINAL', 'prov-or-better'
    return 'UNCERTAIN', '-'

# ---------------- frame rules (PREREG)
MEME_WINDOWS = {313, 573, 982, 1164}   # 78-45, F50 "meme" LEAD — excluded from fork table
def frame_of(i, pre, suc, group):
    if group == '78' and i in MEME_WINDOWS:
        return 'meme-contested'
    if pre in {'37', '11', '87'}:
        return 'ver-frame'
    if suc == '94':
        return 'er-frame'
    return 'other'

def classify(w, group):
    rows = []
    for i, pre, suc in w:
        pos, ptier = position_of(i, pre, suc, group)
        fr = frame_of(i, pre, suc, group)
        rows.append({'i': i, 'pre': pre, 'suc': suc, 'pos': pos, 'ptier': ptier, 'frame': fr})
    return rows

c78 = classify(w78, '78')
c76 = classify(w76, '76')

# ---------------- Leg 1: primary contingency table
def contingency(rows, gt_only=False, drop_pre77=False, include_1352=False, include_meme=False):
    t = Counter()
    for r in rows:
        if r['i'] in MEME_WINDOWS and not include_meme:
            continue
        contested_as_initial = (r['i'] == 1352 and include_1352)
        if r['i'] == 1352 and not include_1352:
            continue
        if gt_only and r['ptier'] != 'GT' and r['pos'] == 'INITIAL':
            continue
        if drop_pre77 and r['pre'] == '77' and r['pos'] == 'INITIAL':
            continue
        if r['pos'] == 'INITIAL' or contested_as_initial:
            row = 'INITIAL'
        elif r['pos'] == 'MEDIAL':
            row = 'NON-INITIAL'
        else:
            continue
        if r['frame'] == 'ver-frame':
            col = 'ver-frame'
        elif r['frame'] == 'er-frame':
            col = 'er-frame'
        else:
            continue
        t[(row, col)] += 1
    a = t[('INITIAL', 'ver-frame')]; b = t[('INITIAL', 'er-frame')]
    c = t[('NON-INITIAL', 'ver-frame')]; d = t[('NON-INITIAL', 'er-frame')]
    return (a, b, c, d), t

from scipy.stats import fisher_exact
def report_table(name, abcd):
    a, b, c, d = abcd
    try:
        _, p = fisher_exact([[a, b], [c, d]], alternative='greater')
    except Exception:
        p = float('nan')
    return {'name': name, 'table': [[a, b], [c, d]], 'fisher_one_sided_p': p}

leg1 = report_table('primary', contingency(c78)[0])
leg1_s1 = report_table('S1:+@1352', contingency(c78, include_1352=True)[0])
leg1_s2 = report_table('S2:GT-only', contingency(c78, gt_only=True)[0])
leg1_s3 = report_table('S3:drop-pre77', contingency(c78, drop_pre77=True)[0])
leg1_s4 = report_table('S4:+meme-as-ver', contingency(c78, include_meme=True)[0])

# ---------------- Leg 2: H0-er kill via GT-anchored initial frames ("la 78")
gt_initial_78 = [r for r in c78 if r['pos'] == 'INITIAL' and r['ptier'] == 'GT']
# ---------------- Leg 3: 78-94 bigrams (er|ne diagnostic, cipher side)
bigrams_78_94 = [r for r in c78 if r['suc'] == '94']

# ---------------- Leg 4: 76 contrast
pos76 = Counter(r['pos'] for r in c76)
erframe76 = [r for r in c76 if r['frame'] == 'er-frame']
final76 = [r for r in c76 if r['pos'] == 'FINAL']

# ---------------- Leg 5 (Frenchman): era-corpus phonotactics, nesselrode-v8
corp_path = os.path.join(LANE, 'code', 'side-period', 'corpus', 'nesselrode-v8.txt')
text = open(corp_path, encoding='utf-8', errors='replace').read().lower()
toks = re.findall(r"[a-zàâäéèêëîïôöùûüÿçœæ]+", text)
GOUVFAM = ('gouvern', 'gouverne')
def is_gouv(t):
    return t.startswith('gouvern') or t.startswith('gouverne')
vern = Counter(t for t in toks if 'verne' in t and not is_gouv(t))
ern = Counter(t for t in toks if 'erne' in t and 'verne' not in t and not is_gouv(t))
ver_init = Counter(t for t in toks if t.startswith('ver'))
ver_fin = Counter(t for t in toks if t.endswith('ver') and not t.startswith('ver'))
er_init = Counter(t for t in toks if t.startswith('er'))
er_fin = Counter(t for t in toks if t.endswith('er') and len(t) > 2)
# genuine-common-word filter for ver|ne: drop proper nouns (capitalized in raw) — approx via raw case
raw_toks = re.findall(r"[A-Za-zÀ-ÿ]+", open(corp_path, encoding='utf-8', errors='replace').read())
verne_proper = Counter(t for t in raw_toks if 'verne' in t.lower() and not is_gouv(t.lower()) and t[0].isupper())

frenchman = {
    'corpus': 'nesselrode-v8.txt',
    'n_tokens': len(toks),
    'verne_non_gouv_tokens': sum(vern.values()), 'verne_non_gouv_types': len(vern),
    'erne_non_verne_tokens': sum(ern.values()), 'erne_non_verne_types': len(ern),
    'verne_proper_noun_tokens': sum(verne_proper.values()),
    'ver_initial_types': len(ver_init), 'ver_initial_tokens': sum(ver_init.values()),
    'ver_final_types': len(ver_fin), 'ver_final_tokens': sum(ver_fin.values()),
    'ver_final_examples': [t for t, _ in ver_fin.most_common(15)],
    'er_initial_types': len(er_init), 'er_initial_tokens': sum(er_init.values()),
    'er_initial_examples': [t for t, _ in er_init.most_common(15)],
    'er_final_tokens': sum(er_fin.values()),
}

# ---------------- verification: 5 random 78 windows re-derived (seed 1407)
random.seed(1407)
vrfy_idx = sorted(random.sample([i for i, _, _ in w78], 5))
vrfy = []
for i in vrfy_idx:
    # re-derive from raw digits: find row containing pair i by rebuilding row map
    vrfy.append({'i': i, 'triple': [pairs[i-1], pairs[i], pairs[i+1]]})

result = {
    'n78': len(w78), 'n76': len(w76),
    'f107_coverage_78': cov78, 'f107_coverage_76': cov76,
    'n_f107_segments': 32,
    'c78': c78, 'c76': c76,
    'leg1_tables': [leg1, leg1_s1, leg1_s2, leg1_s3, leg1_s4],
    'leg2_gt_initial_78': gt_initial_78,
    'leg3_bigrams_78_94': bigrams_78_94,
    'leg4_76_positions': dict(pos76),
    'leg4_76_erframes': erframe76,
    'leg4_76_finals': final76,
    'frenchman_corpus': frenchman,
    'verification_windows': vrfy,
}
with open(os.path.join(OUT, 'fork78_results.json'), 'w') as f:
    json.dump(result, f, indent=1, ensure_ascii=False)
print(json.dumps({
    'n78': len(w78), 'n76': len(w76),
    'f107_cov78': len(cov78), 'f107_cov76': len(cov76),
    'leg1': leg1, 'S1': leg1_s1, 'S2': leg1_s2, 'S3': leg1_s3, 'S4': leg1_s4,
    'leg2_gt_initial_78': [(r['i'], r['pre'], r['suc']) for r in gt_initial_78],
    'leg3_78_94': [(r['i'], r['pre'], r['suc'], r['pos']) for r in bigrams_78_94],
    'leg4_76_pos': dict(pos76),
    'leg4_76_erframes': [(r['i'], r['pre'], r['suc']) for r in erframe76],
    'frenchman': frenchman,
    'verification': vrfy,
}, indent=1, ensure_ascii=False))
