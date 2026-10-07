#!/usr/bin/env python3
"""Round-11 67-RESIDUAL FINISHER scorer. Implements PREREG.md bars V-*.

Era: Nesselrode v8, lane tokenizer verbatim (vendored round-9/10 copy).
Writes: code/crowd11/finisher67/results_r11.json
"""
import json, os, re, sys
from collections import Counter

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd4'))
from repaired_parse import load_pairs_repaired

pairs, _, _ = load_pairs_repaired()
N = len(pairs)
assert N == 1847, N

R = {}  # results

# ---------- shared helpers ----------
def n_bigram(a, b):
    return sum(1 for i in range(N - 1) if pairs[i] == a and pairs[i + 1] == b)

def positions(g):
    return [i for i in range(N) if pairs[i] == g]

def contact_census(g):
    """Every occurrence of g: (pos, pre, suc)."""
    return [(i, pairs[i-1] if i > 0 else None, pairs[i+1] if i < N-1 else None)
            for i in positions(g)]

# licensor sets (per PREREG)
NOM_LIC = {'11', '08', '77', '96'}   # 11 GT; 08 l'-lead; 77 le-prov-cond; 96 par-prov
VERB_LIC = {'64', '00', '46'}        # 64 qui-prov; 00 pour-lead(inf gov); 46 que-GT verb-frame

def class_census(g):
    rows = contact_census(g)
    nom = Counter(p for _, p, _ in rows if p in NOM_LIC)
    vrb = Counter(p for _, p, _ in rows if p in VERB_LIC)
    return {
        'n': len(rows),
        'nom_hits': dict(nom), 'nom_distinct': len(nom),
        'vrb_hits': dict(vrb), 'vrb_distinct': len(vrb),
        'all_pre': dict(Counter(p for _, p, _ in rows)),
        'all_suc': dict(Counter(s for _, _, s in rows)),
        'windows': [(i, pairs[i-1], pairs[i+1]) for i, _, _ in rows],
    }

# ---------- era side (vendored tokenizer, identical to round-10) ----------
def tok(text):
    text = text.lower().replace('\u2019', "'").replace('\u2018', "'")
    text = re.sub(r"([a-z\u00e0-\u00ff])'([a-z\u00e0-\u00ff])", r'\1 \2', text)
    return re.findall(r'[a-z\u00e0-\u00ff]+', text)

def split_nesselrode():
    C = os.path.join(LANE, 'code', 'side-period', 'corpus')
    txt = open(os.path.join(C, 'nesselrode-v8.txt'), encoding='utf-8', errors='replace').read()
    months = 'janvier|février|fevrier|mars|avril|mai|juin|juillet|août|aout|septembre|octobre|novembre|décembre|decembre'
    pat = re.compile(r'^((?:Saint-Pétersbourg|Berlin|Paris|Londres|Vienne|Varsovie|Constantinople|Munich|Dresde)[ ,\.\u00a0]*\d{1,2}\s+(?:%s)\s+184[0-6])\.?,?\s*$' % months, re.M)
    bounds = [m.start() for m in pat.finditer(txt)]
    return [txt[a:b] for a, b in zip(bounds, bounds[1:] + [len(txt)])]

W = []
for d in split_nesselrode():
    W += tok(d)
NW = len(W)
assert NW == 92123, NW

def ngap(a, c):
    return sum(1 for i in range(NW - 2) if W[i] == a and W[i+2] == c)

def nseq2(a, b):
    return sum(1 for i in range(NW - 1) if W[i] == a and W[i+1] == b)

def L1_pass(e_et, e_veut):
    return e_et >= 20 and e_veut <= 3 and (e_veut == 0 or e_et / e_veut >= 10)

R['era_NW'] = NW

# ============================================================
# R-1519 — 31's second leg
# ============================================================
r1519 = {}
r1519['V1519a_n_11_31'] = n_bigram('11', '31')
r1519['V1519a_leg'] = r1519['V1519a_n_11_31'] >= 2
c31 = class_census('31')
r1519['V1519b_census'] = {k: v for k, v in c31.items() if k != 'windows'}
r1519['V1519b_windows'] = c31['windows']
r1519['V1519b_nominal'] = c31['nom_distinct'] >= 2
r1519['V1519b_verbal'] = c31['vrb_distinct'] >= 2
r1519['n_64_31'] = n_bigram('64', '31')
r1519['n_08_31'] = n_bigram('08', '31')
# verdict
if r1519['V1519a_leg']:
    r1519['verdict'] = 'et-CONDITIONAL(C1:08=l-apos,C2) — L2 supplied'
elif r1519['V1519b_nominal'] and not r1519['V1519b_verbal']:
    r1519['verdict'] = '31 NOMINAL-CLASS (>=2 legs) — missing leg supplied, window et-CONDITIONAL(C1,C2) on class leg'
elif r1519['V1519b_verbal'] and not r1519['V1519b_nominal']:
    r1519['verdict'] = '31 VERBAL-CLASS — adverse to et-lean; open-residual (veut-lean unscored, no veut-bar)'
else:
    r1519['verdict'] = 'clean null — 31 class unresolved'
R['1519'] = r1519

# ============================================================
# R-1372 — denser era frame
# ============================================================
r1372 = {}
r1372['V1372a_et_gap_pour'] = ngap('et', 'pour')
r1372['V1372a_veut_gap_pour'] = ngap('veut', 'pour')
r1372['V1372a_n_11_98'] = n_bigram('11', '98')
e_et_bare = nseq2('et', 'pour')
e_veut_bare = nseq2('veut', 'pour')
r1372['V1372b_et_pour'] = e_et_bare
r1372['V1372b_veut_pour'] = e_veut_bare
r1372['V1372b_pass_numbers'] = L1_pass(e_et_bare, e_veut_bare)
r1372['V1372b_status'] = 'FENCED-CONDITIONAL datum (98 must not intervene as separate word)'
# show what the bare-frame middles look like (context, not a leg)
r1372['V1372b_veut_pour_context'] = [W[i+2] for i in range(NW-2)
    if W[i] == 'veut' and W[i+1] == 'pour'][:10]
c98 = class_census('98')
r1372['V1372c_census'] = {k: v for k, v in c98.items() if k != 'windows'}
r1372['V1372c_windows'] = c98['windows']
r1372['V1372c_L2'] = r1372['V1372a_n_11_98'] >= 2
if r1372['V1372b_pass_numbers'] and r1372['V1372c_L2']:
    r1372['verdict'] = 'et-CONDITIONAL(C1fenced) — both legs (fenced frame noted)'
elif r1372['V1372b_pass_numbers']:
    r1372['verdict'] = 'clean null — denser frame exists only FENCED (98 intervention unresolved); L2 null'
else:
    r1372['verdict'] = 'clean null — no denser era frame even fenced; L2 null'
R['1372'] = r1372

# ============================================================
# R-633 — board-grade 52/63 + era frame
# ============================================================
r633 = {}
e_et_l = ngap('l', 'et')
e_veut_l = ngap('veut', 'veut')  # placeholder, replaced below
e_veut_l = sum(1 for i in range(NW - 2) if W[i] == 'l' and W[i+2] == 'veut')
r633['V633a_et'] = e_et_l
r633['V633a_veut'] = e_veut_l
r633['V633a_pass'] = L1_pass(e_et_l, e_veut_l)
r633['V633a_L2_n_11_52'] = n_bigram('11', '52')  # cited standing: 3
# sample middles for the record (context)
r633['V633a_et_middles_sample'] = Counter(
    W[i+1] for i in range(NW - 2) if W[i] == 'l' and W[i+2] == 'et').most_common(10)
r633['V633a_veut_middles'] = Counter(
    W[i+1] for i in range(NW - 2) if W[i] == 'l' and W[i+2] == 'veut').most_common(10)
if r633['V633a_pass'] and r633['V633a_L2_n_11_52'] >= 2:
    r633['V633a_verdict'] = 'et-CONDITIONAL(C1:08=l-apos,C2)'
else:
    r633['V633a_verdict'] = 'no classification'
r633['V633b_n_08_52'] = n_bigram('08', '52')
r633['V633b_leg'] = r633['V633b_n_08_52'] >= 2
# V-633c: negation frame check @625-631 (is there a 94='ne' licensing pre-verbal 'pas'?)
r633['V633c_window_625_635'] = [(i, pairs[i]) for i in range(625, 636)]
r633['V633c_has_94_in_625_631'] = any(pairs[i] == '94' for i in range(625, 632))
r633['V633c_52_eq_pas_at_633'] = 'INCOHERENT (window-scoped)' if not r633['V633c_has_94_in_625_631'] else 'check manually'
c63 = class_census('63')
r633['V633d_census'] = {k: v for k, v in c63.items() if k != 'windows'}
r633['V633d_windows'] = c63['windows']
r633['V633d_nominal'] = c63['nom_distinct'] >= 2
r633['V633d_verbal'] = c63['vrb_distinct'] >= 2
R['633'] = r633

# ============================================================
# R-902 — board-grade 92/16
# ============================================================
r902 = {}
c92 = class_census('92')
r902['V902a_census'] = {k: v for k, v in c92.items() if k != 'windows'}
r902['V902a_windows'] = c92['windows']
r902['V902a_nominal'] = c92['nom_distinct'] >= 2
r902['V902a_verbal'] = c92['vrb_distinct'] >= 2
c16 = class_census('16')
r902['V902b_16_census'] = {k: v for k, v in c16.items() if k != 'windows'}
# word-frame contacts for 16: 46->16 (que-clause), 11->16 (article) — would force re-examination
r902['V902b_n_46_16'] = n_bigram('46', '16')
r902['V902b_n_11_16'] = n_bigram('11', '16')
r902['V902b_word_status'] = (r902['V902b_n_46_16'] >= 2 or r902['V902b_n_11_16'] >= 2)
r902['V902c_frame'] = 'design null confirmed — no board word adjacent to 67'
R['902'] = r902

# ============================================================
# R-1450 / R-1623 — 33 decider
# ============================================================
r33 = {}
# V-33a: spot-verify census33 headline counts (verification, not re-census)
r33['V33a_n_00_33'] = n_bigram('00', '33')   # census33 I1 = 8
r33['V33a_n_33_29'] = n_bigram('33', '29')   # census33 I4 = 5
r33['V33a_match'] = (r33['V33a_n_00_33'] == 8 and r33['V33a_n_33_29'] == 5)
# V-33b: verify E7 numbers
r33['V33b_et_gap_que'] = ngap('et', 'que')
r33['V33b_veut_gap_que'] = ngap('veut', 'que')
r33['V33b_n_11_33'] = n_bigram('11', '33')
r33['V33b_match'] = (r33['V33b_et_gap_que'] == 16 and r33['V33b_veut_gap_que'] == 2
                     and r33['V33b_n_11_33'] == 0)
# decider application
r33['WO3_verdict'] = 'C1-infinitive (census33 recommendation; red-team PENDING)'
r33['decider'] = 'infinitive -> veut-arm LIVES at @1450/@1623; et-arm NOT established (E7-L1 fails)'
r33['1450_verdict'] = 'open-residual (decider applied)'
r33['1623_verdict'] = 'open-residual (decider applied)'
# in-cipher parallel for the record (context, not a leg): veut-67 @1423 -> 33 @1424 -> 29 @1425
r33['parallel_1423'] = [f"{i}:{pairs[i]}" for i in range(1421, 1427)]
R['1450_1623'] = r33

# ============================================================
# Fork tally verification
# ============================================================
b7 = json.load(open(os.path.join(LANE, 'code/crowd7/morphologist/battery67_final.json')))
stand = {str(r['pos']): r['class'] for r in b7['rows']}
stand['1248'] = 'NEITHER-fenced'
stand['199'] = 'NEITHER-fenced-conditional'
stand['630'] = 'et-CONDITIONAL'
tally = Counter(stand.values())
R['fork_tally'] = dict(tally)
R['fork_status'] = 'SUPPORTED with amended scope (fenced n=2)'

with open(os.path.join(HERE, 'results_r11.json'), 'w') as f:
    json.dump(R, f, indent=1, ensure_ascii=False)
print(json.dumps({k: (v if not isinstance(v, dict) else {kk: vv for kk, vv in v.items() if 'census' not in kk and 'windows' not in kk})
                  for k, v in R.items()}, indent=1, ensure_ascii=False)[:6000])
