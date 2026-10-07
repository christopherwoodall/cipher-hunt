#!/usr/bin/env python3
"""Round-9 62-RESOLVER: N35 independent-cell on/il battery (WO3).

Pre-registration: PREREG.md (data-blind). Every number re-derived from the
repaired 1,847-pair stream. Era: Nesselrode v8 only.
"""
import json, math, re, collections, os
from pathlib import Path

LANE = Path.home() / 'workspace/cipher-hunt/lanes/zeschau-seebach-1841'
DATA = LANE / 'data'
OUT = Path(__file__).parent

# ---------- canonical repaired parse (frenchman/util.py loader, verbatim) ----------
def load_repaired():
    rows = []
    for line in open(DATA / 'upstream-ct_R5005.txt'):
        line = line.strip()
        if not line:
            continue
        lid, digits = line.split()
        rows.append((lid, re.sub(r'\D', '', digits)))
    off = json.loads((LANE / 'code/side-keyhunt/repaired_offsets.json').read_text())
    pairs = []
    for lid, digits in rows:
        o = off[lid]
        pairs += [digits[i:i+2] for i in range(o, len(digits)-1, 2)]
    p = [int(g) for g in pairs]
    assert len(p) == 1847, len(p)
    return p

PAIRS = load_repaired()
N = len(PAIRS)
UNI = collections.Counter(PAIRS)
assert UNI[62] == 35, f"n62={UNI[62]} (expected 35)"
print(f"stream OK: N={N} pairs, n62={UNI[62]}, n59={UNI[59]}, n01={UNI[1] if 1 in UNI else UNI.get(1)}, n93={UNI[93]}, n8={UNI[8]}")

# ---------- era: Nesselrode v8, frenchman tok_elision verbatim ----------
def tok_elision(text):
    text = text.replace('-\n','').replace('-\r\n','').lower()
    text = re.sub(r"[’‘`]", "'", text)
    text = re.sub(r"\b([a-zàâäéèêëîïôöùûüçœæ]+)'([a-zàâäéèêëîïôöùûüçœæ]+)", r"\1' \2", text)
    return re.findall(r"[a-zàâäéèêëîïôöùûüçœæ]+'?|[a-zàâäéèêëîïôöùûüçœæ]+", text)

CORP = LANE / 'code/side-period/corpus/nesselrode-v8.txt'
D = tok_elision(CORP.read_text(encoding='utf-8', errors='replace'))
ND = len(D)
EU = collections.Counter(D)
EB = collections.Counter(zip(D, D[1:]))
ET = collections.Counter(zip(D, D[1:], D[2:]))
print(f"era OK: nesselrode-v8 tokens={ND}, C(on)={EU['on']}, C(il)={EU['il']}, C(est)={EU['est']}, C(l')={EU[chr(108)+chr(39)]}")

def era_bi(a, b): return EB[(a, b)]
def era_tri(a, b, c): return ET[(a, b, c)]

# ---------- exact two-sided binomial ----------
def logpmf(n, k, p):
    if p <= 0: return 0.0 if k == 0 else float('-inf')
    if p >= 1: return 0.0 if k == n else float('-inf')
    return (math.lgamma(n+1)-math.lgamma(k+1)-math.lgamma(n-k+1)
            + k*math.log(p) + (n-k)*math.log(1-p))

def binom_two_sided(n, k, p):
    if n == 0: return {'p_two': None, 'note': 'n=0, void'}
    lp_obs = logpmf(n, k, p)
    tot = 0.0
    for j in range(n+1):
        if logpmf(n, j, p) <= lp_obs + 1e-12:
            tot += math.exp(logpmf(n, j, p))
    return {'p_two': min(1.0, tot)}

def judge(n, k, p_on, p_il, label):
    r_on = binom_two_sided(n, k, p_on); r_il = binom_two_sided(n, k, p_il)
    pO, pI = r_on['p_two'], r_il['p_two']
    if pO is None: verdict = 'VOID'
    elif pO >= 0.10 and (pI is not None and pI < 0.01): verdict = 'LEG-FOR-on'
    elif pI is not None and pI >= 0.10 and pO < 0.01: verdict = 'LEG-FOR-il'
    else: verdict = 'NULL'
    return {'cell': label, 'n': n, 'k': k,
            'p_on': p_on, 'p_il': p_il,
            'E_on': round(p_on*n, 3), 'E_il': round(p_il*n, 3),
            'p_two_on': None if pO is None else round(pO, 5),
            'p_two_il': None if pI is None else round(pI, 5),
            'verdict': verdict}

L = "l'"
res = {}

# ================= C1: 62 -> 59 =================
w1 = [i for i in range(N-1) if PAIRS[i] == 62 and PAIRS[i+1] == 59]
p_on = era_bi('on','est')/EU['on']; p_il = era_bi('il','est')/EU['il']
res['C1'] = judge(35, len(w1), p_on, p_il, '62->59')
res['C1']['windows'] = w1
res['C1']['era'] = {'C_on_est': era_bi('on','est'), 'C_on': EU['on'],
                    'C_il_est': era_bi('il','est'), 'C_il': EU['il']}

# ================= C2: 59 -> 62 =================
w2 = [i for i in range(N-1) if PAIRS[i] == 59 and PAIRS[i+1] == 62]
q_on = era_bi('est','on')/EU['est']; q_il = era_bi('est','il')/EU['est']
res['C2'] = judge(UNI[59], len(w2), q_on, q_il, '59->62')
res['C2']['windows'] = w2
res['C2']['era'] = {'C_est_on': era_bi('est','on'), 'C_est_il': era_bi('est','il'),
                    'C_est': EU['est']}

# ================= C3/C4: 62 -> (93|8) [-> 59] =================
w34 = [i for i in range(N-2) if PAIRS[i] == 62 and PAIRS[i+1] in (93, 8)]
n3 = len(w34); k3 = sum(1 for i in w34 if PAIRS[i+2] == 59)
w3 = [i for i in w34 if PAIRS[i+2] == 59]
d_on = era_bi('on', L); d_il = era_bi('il', L)
r_on = era_tri('on', L, 'est')/d_on if d_on else None
r_il = era_tri('il', L, 'est')/d_il if d_il else None
if d_on is not None and d_on >= 10 and d_il >= 10:
    res['C3'] = judge(n3, k3, r_on, r_il, '62-lp-59 | 62-lp')
else:
    res['C3'] = {'cell': '62-lp-59 | 62-lp', 'n': n3, 'k': k3, 'verdict': 'VOID',
                 'note': f'era denom on={d_on}, il={d_il} (<10)'}
res['C3']['windows'] = w3
res['C3']['denom_windows'] = w34
res['C3']['era'] = {'C_on_lp_est': era_tri('on',L,'est'), 'C_on_lp': d_on,
                    'C_il_lp_est': era_tri('il',L,'est'), 'C_il_lp': d_il}
s_on = era_bi('on', L)/EU['on']; s_il = era_bi('il', L)/EU['il']
res['C4'] = judge(35, n3, s_on, s_il, '62->lp')
res['C4']['windows'] = w34
res['C4']['era'] = {'C_on_lp': d_on, 'C_on': EU['on'], 'C_il_lp': d_il, 'C_il': EU['il']}

# ---------- overlap audit (N35): any shared pair position across leg cells ----------
pos_sets = {'C1': set(w1), 'C2': set(w2), 'C3': set(w3)}
# C3 windows also occupy i+1 (the lp bigram); check pair-position overlap incl. i+1/i+2
occ = {}
for c, ws in pos_sets.items():
    for i in ws:
        span = {i, i+1} if c in ('C1','C2') else {i, i+1, i+2}
        for p_ in span:
            occ.setdefault(p_, []).append((c, i))
overlap = {p_: v for p_, v in occ.items() if len({c for c, _ in v}) > 1}
res['overlap_audit'] = {'shared_positions': {str(k): v for k, v in overlap.items()},
                        'n_shared': len(overlap)}

# ================= S1: {59,01} pooled sensitivity (descriptive) =================
EST = {59, 1}
s1_w1 = [i for i in range(N-1) if PAIRS[i] == 62 and PAIRS[i+1] in EST]
s1_w2 = [i for i in range(N-1) if PAIRS[i] in EST and PAIRS[i+1] == 62]
res['S1'] = {'C1_pooled_62_to_est': {'n': 35, 'k': len(s1_w1), 'windows': s1_w1,
             'E_on_word': round(p_on*35, 3), 'E_il_word': round(p_il*35, 3)},
             'C2_pooled_est_to_62': {'n': UNI[59]+UNI[1], 'k': len(s1_w2), 'windows': s1_w2,
             'E_on_word': round(q_on*(UNI[59]+UNI[1]), 3),
             'E_il_word': round(q_il*(UNI[59]+UNI[1]), 3)}}

# ================= D1: all (93|8) -> 59 "l'est" windows =================
d1 = [(i, PAIRS[i], PAIRS[i-1] if i > 0 else None)
      for i in range(N-1) if PAIRS[i] in (93, 8) and PAIRS[i+1] == 59]
res['D1_lest_windows'] = [{'pos': i, 'lp': lp, 'pre': pre} for i, lp, pre in d1]
res['D1_note'] = ('predecessor of @101 (94-93-59 "ne l\'est", M_hom leg 3) = '
                  f"{PAIRS[100]} (n=1 observation; window re-entered for context only)")

# ================= D2: predecessors of the four L_A windows =================
LA = [10, 944, 1323, 1685]
d2 = [{'lp_pos': i, 'lp': PAIRS[i], 'follows_62': PAIRS[i+1] == 62,
       'pre': PAIRS[i-1], 'pre_is_46_que': PAIRS[i-1] == 46} for i in LA]
res['D2_LA_predecessors'] = d2
res['D2_note'] = 'shares windows with settled L_A; descriptive only ("que l\'on" check)'

json.dump(res, open(OUT / 'results.json', 'w'), indent=1,
          default=lambda o: f'<{type(o).__name__}>')
print(json.dumps({k: v for k, v in res.items() if k != 'overlap_audit'}, indent=1)[:6000])
print('OVERLAP:', json.dumps(res['overlap_audit']))
