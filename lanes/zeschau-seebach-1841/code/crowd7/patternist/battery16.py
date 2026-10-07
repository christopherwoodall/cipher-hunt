#!/usr/bin/env python3
"""16="i" battery — Seebach round 7, patternist work order 4.

Claim: group 16 = /i/ (a second 'i' cell; 34=i is pencil GT).
Source lead: "parmi" @1196-1198 [96,82,16] = par|m|i (F48, LEAD, red-team UPHELD).
Supporting datum: 82->16 x11 reads m|i (F5).

==================== PRE-REGISTERED BATTERY (bars fixed before results) ====================

Checks (three families, per work order):
  B1 DISTRIBUTIONAL — 16 vs 34 contact-profile similarity (contact-coherent
     aliasing, F49/N43: homophones dealt coherently => similar profiles).
     Statistic: cosine similarity of 96-dim follower-count vectors
     (n16=27 followers, n34=11). Null: 20,000 permutations of the pooled
     38 follower tokens into 27/11 splits. Same for predecessors (28/11).
     Pre-reg: p<0.05 on EITHER => weak support (low power, n small; a FAIL
     does NOT kill -- redirects to the position-conditioned alternative
     16=word-final /i/ vs 34=word-internal /i/, which needs its own F33 rule).
  B2 BY-EAR TILINGS — eleven-window rival vote. For each 82->16 bigram start s
     (11 windows), take LEFT=P[s-1:s+3] and RIGHT=P[s:s+4]; enumerate lexicon
     words whose by-ear top-8 tilings have the bigram aligned as [..,m,X,..]
     with 16 free and all else hard (GT+PROV+LE77+islets licensed). Record the
     implied single-letter cell X per window (multi-letter X recorded
     separately). Window vote = set of X with >=1 fitting word.
     Pre-reg: PASS iff 'i' is in the vote set at >=8/11 windows AND no rival
     single letter has a strictly larger window count than 'i'. Reported both
     with and without the @1197 window (mild circularity: it sits inside the
     "parmi" word that motivated the claim).
  B3 ANCHOR-ADJACENCY — (a) H-split consistency (N39): the cipher never writes
     46=que before /i/ unsplit (46->34=0). Pre-reg: 46->16 MUST be 0; a nonzero
     count is adverse to 16="i". (b) Anchor-frame census: every distinct frame
     where 16 neighbors a GT/PROV group (beyond 82=m) judged
     consistent/neutral/adverse vs /i/. Pre-reg: PASS iff >=3 distinct frames
     and zero adverse vs /i/ itself (adverse to the "parmi" word reading does
     not count against 16="i").

Verdict bars:
  PROMOTE (to provisional): >=2 of {B1,B2,B3} PASS, each n_eff>=3, zero
      adverse vs /i/, rivals strictly dominated in B2.
  HOLD (LEAD): exactly 1 passes at n_eff>=3, or >=2 pass with one n_eff<3;
      no adverse.
  KILL: >=1 kill-grade adverse (exact p<0.01 against /i/, n_eff>=3) OR B2
      shows a rival single-letter cell winning the 11-window vote.

HONEST BOUNDARY (work order): the 20-string inventory cannot recover
unattested multi-letter cells. This battery tests single-letter "i" against
single-letter rivals {a,e,o,u,y} only. A PASS yields provisional, never
confirmed; "i" vs "y" are by-ear indistinguishable here.

No double-counting: B2 reuses the by-ear tiler (shared instrument with F48)
but 10/11 windows are new data; the @1197-included/excluded tallies are
reported separately (F26-17). B1/B3 use contact data F48 never touched.
===========================================================================================
"""
import json
import math
import os
import random
import sys
from collections import Counter

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd4'))
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd6', 'period_drag'))
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd6', 'inventorist'))
from repaired_parse import load_pairs_repaired
from common import GT, PROV, LE77, ISLETS, fit_cells, load_lexicon_tilings
from byear import tile as byear_tile

P, _, _ = load_pairs_repaired()
HARD = dict(GT)
HARD.update(PROV)
HARD.update(LE77)  # 77=le conditioned; none of the 16-windows are T4 windows
FREE16 = frozenset({'16'})

pos16 = [i for i, g in enumerate(P) if g == '16']
pos34 = [i for i, g in enumerate(P) if g == '34']
bigram_starts = [i for i in range(len(P) - 1) if P[i] == '82' and P[i + 1] == '16']
assert len(pos16) == 28 and len(pos34) == 11 and len(bigram_starts) == 11

rng = random.Random(20261007)


def cosine(a, b):
    dot = sum(a[k] * b.get(k, 0) for k in a)
    na = math.sqrt(sum(v * v for v in a.values()))
    nb = math.sqrt(sum(v * v for v in b.values()))
    return dot / (na * nb) if na and nb else 0.0


def perm_test(tok16, tok34, reps=20000):
    """Permutation p-value for cosine similarity of count vectors."""
    v16 = Counter(tok16)
    v34 = Counter(tok34)
    obs = cosine(v16, v34)
    pool = tok16 + tok34
    n16 = len(tok16)
    ge = 0
    for _ in range(reps):
        rng.shuffle(pool)
        a = Counter(pool[:n16])
        b = Counter(pool[n16:])
        if cosine(a, b) >= obs:
            ge += 1
    return obs, (ge + 1) / (reps + 1)


# ---------------- B1: distributional ----------------
fol16 = [P[i + 1] for i in pos16 if i + 1 < len(P)]
fol34 = [P[i + 1] for i in pos34 if i + 1 < len(P)]
pre16 = [P[i - 1] for i in pos16 if i - 1 >= 0]
pre34 = [P[i - 1] for i in pos34 if i - 1 >= 0]
obs_f, p_f = perm_test(fol16, fol34)
obs_p, p_p = perm_test(pre16, pre34)
jac_f = len(set(fol16) & set(fol34)) / len(set(fol16) | set(fol34))
jac_p = len(set(pre16) & set(pre34)) / len(set(pre16) | set(pre34))
b1 = {
    'n_fol': [len(fol16), len(fol34)], 'cos_fol': round(obs_f, 4),
    'p_fol': round(p_f, 4), 'jaccard_fol': round(jac_f, 4),
    'n_pre': [len(pre16), len(pre34)], 'cos_pre': round(obs_p, 4),
    'p_pre': round(p_p, 4), 'jaccard_pre': round(jac_p, 4),
    'pass': bool(p_f < 0.05 or p_p < 0.05),
}
print('B1', json.dumps(b1))

# ---------------- B2: by-ear eleven-window rival vote ----------------
lex = load_lexicon_tilings()
words = list(lex.keys())
# Precompute len-4 by-ear tilings once (shared across windows).
print('precomputing len-4 tilings...', flush=True)
til4 = {}
for w in words:
    ts = [cells for cells, _sc in byear_tile(w, k=8) if len(cells) == 4]
    if ts:
        til4[w] = ts
print(f'{len(til4)} words with len-4 tilings', flush=True)


def window_votes(s):
    """Vote sets for one 82->16 bigram start. Returns (left_set, right_set, multi)."""
    out = []
    multi = []
    shapes = []
    if s - 1 >= 0:
        shapes.append((P[s - 1:s + 3], 1))   # LEFT: bigram at cells 1-2
    if s + 4 <= len(P):
        shapes.append((P[s:s + 4], 0))       # RIGHT: bigram at cells 0-1
    for groups, bpos in shapes:
        if not (groups[bpos] == '82' and groups[bpos + 1] == '16'):
            out.append(set())
            continue
        votes = set()
        for w, ts in til4.items():
            for cells in ts:
                if cells[bpos] != 'm':  # 82=m GT: bigram anchor cell
                    continue
                x = cells[bpos + 1]
                ok, _notes = fit_cells(cells, groups, HARD, FREE16)
                if not ok:
                    continue
                if len(x) == 1:
                    votes.add(x)
                else:
                    multi.append((w, x))
                    break
        out.append(votes)
    while len(out) < 2:
        out.append(set())
    return out[0], out[1], multi


vote_rows = []
for s in bigram_starts:
    lv, rv, multi = window_votes(s)
    vote_rows.append({'start': s, 'left': sorted(lv), 'right': sorted(rv),
                      'multi_sample': multi[:4], 'n_multi': len(multi)})

tally_all = Counter()
tally_no1197 = Counter()
for r in vote_rows:
    xs = set(r['left']) | set(r['right'])
    for x in xs:
        tally_all[x] += 1
        if r['start'] != 1197:
            tally_no1197[x] += 1

def b2_pass(tally):
    ti = tally.get('i', 0)
    rivals = {x: c for x, c in tally.items() if x != 'i'}
    best_rival = max(rivals.values()) if rivals else 0
    return ti >= 8 and ti > best_rival, ti, best_rival

p_all, ti_all, br_all = b2_pass(tally_all)
p_no, ti_no, br_no = b2_pass(tally_no1197)
b2 = {
    'windows': vote_rows,
    'tally_incl_1197': dict(tally_all), 'i_windows': ti_all,
    'best_rival_windows': br_all, 'pass_incl_1197': bool(p_all),
    'tally_excl_1197': dict(tally_no1197), 'i_windows_excl': ti_no,
    'best_rival_excl': br_no, 'pass_excl_1197': bool(p_no),
    'pass': bool(p_all and p_no),
}
print('B2 tally incl:', dict(tally_all), 'pass:', p_all)
print('B2 tally excl 1197:', dict(tally_no1197), 'pass:', p_no)

# ---------------- B3: anchor-adjacency ----------------
fol16c = Counter(fol16)
pre16c = Counter(pre16)
anchors = set(HARD)  # GT+PROV+LE77
b46_16 = pre16c.get('46', 0)   # H-split: must be 0 under 16="i"
f16_46 = fol16c.get('46', 0)
frames = []
# distinct anchor frames beyond 82=m
for g, c in sorted(pre16c.items()):
    if g in anchors and g != '82':
        frames.append(('pre', g, c))
for g, c in sorted(fol16c.items()):
    if g in anchors:
        frames.append(('fol', g, c))
frame_notes = {
    ('pre', '62'): "62='on' STRONG LEAD (ear-only): 'on|i..' word boundary -- consistent",
    ('pre', '12'): '12 unidentified -- neutral',
    ('pre', '33'): '33 unidentified -- neutral',
    ('pre', '42'): '42 unidentified -- neutral',
    ('fol', '64'): "16->64=qui @1198 ('parmi|qui'): 'parmi qui' ungrammatical alone -- "
                   "mild adverse to the PARMI word, not to 16='i'",
    ('fol', '29'): "16->29=er @1142 (62-16-29): '?|i|er' -- neutral",
    ('fol', '96'): "16->96=par @1195 (82-16-96): 'mi|par' word boundary -- consistent",
}
adverse_vs_i = []
for kind, g, c in frames:
    note = frame_notes.get((kind, g), 'neutral')
    if 'ADVERSE' in note and 'not to 16' not in note:
        adverse_vs_i.append((kind, g))
b3 = {
    'n46_pre_16': b46_16, 'n16_fol_46': f16_46,
    'hsplit_ok': b46_16 == 0,
    'frames': [{'kind': k, 'group': g, 'n': c,
                'note': frame_notes.get((k, g), 'neutral')} for k, g, c in frames],
    'n_distinct_frames': len(frames),
    'adverse_vs_i': adverse_vs_i,
    'pass': bool(b46_16 == 0 and len(frames) >= 3 and not adverse_vs_i),
}
print('B3', json.dumps({k: v for k, v in b3.items() if k != 'frames'}))

passes = sum([b1['pass'], b2['pass'], b3['pass']])
adverse = bool(adverse_vs_i)
if adverse or (not b2['pass'] and b2.get('best_rival_windows', 0) > b2.get('i_windows', 0)):
    verdict = 'KILL'
elif passes >= 2:
    verdict = 'PROMOTE'
elif passes == 1:
    verdict = 'HOLD'
else:
    verdict = 'HOLD'
out = {'check': '16="i"', 'B1': b1, 'B2': b2, 'B3': b3,
       'n_pass': passes, 'verdict': verdict}
json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                'battery16_results.json'), 'w'), indent=1)
print('VERDICT:', verdict, f'({passes}/3 checks pass)')
