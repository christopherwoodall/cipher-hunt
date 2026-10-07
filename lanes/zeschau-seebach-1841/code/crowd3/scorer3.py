#!/usr/bin/env python3
"""SCORER SMITH ROUND 3 — global-consistency cell scorer (work order WO3).

Lane: zeschau-seebach-1841. Reusable infrastructure: code/crowd3/scorer3.py.

THE FAILURE IT FIXES (N12)
--------------------------
Round 2 (code/crowd2/scorer_smith.py) scored each candidate WORD placement with
a single window score and ranked placements. It failed its own control
(top-1 0.021 < chance 0.076, MRR 0.133 < 0.30) because all placements of one
word share the same cells and differ only in 1-2 edge bigrams — the window
score ties across placements, so the true placement cannot win. The language
model itself was fine (true French runs scored above shuffled runs): the
missing signal was GLOBAL CONSISTENCY — whether a candidate assignment X->s
reads as 's' at EVERY occurrence of X in the stream, not just inside one
placed window.

DESIGN
------
For a candidate (group g, cell value v), under the current anchor table T:

1. Find ALL occurrences p_1..p_K of g in the stream.
2. At each occurrence, decode the +/-W window with T + {g:v}, take the maximal
   known-cell run containing p_i, and keep only the bigrams TOUCHING a
   g-position (the 1-4 bigrams that actually discriminate v from alternatives).
   Occurrences with no such bigram are uninformative and excluded.
3. s_i(v) = mean bigram log-probability over the touching bigrams (two-tier
   hybrid cell model from round 2, reused unchanged: corpus syllable bigrams,
   corpus letter bigrams for the LET tier, tier-crossing via the letter model).
4. fit_i(v) = s_i(v) - mean_{b in B_tier(v)} s_i(b): the margin by which v
   beats a fixed set of tier-matched STRONG background cells IN THE SAME
   WINDOW (v2: the 8 most frequent corpus cells per tier — "beats a random
   cell" saturated support at 1.0 for common wrong values in v1; the
   meaningful null is "g is just a common cell"). This normalizes away
   window quality: a good French window lifts every value, so only v-specific
   fit survives. Because the background is tier-matched AND strong, support
   is comparable across tiers (no separate tier-restriction needed).
5. Aggregate over occurrences:
     support(v)  = fraction of informative occurrences with fit_i(v) > 0
     mean_margin = mean fit_i(v)
   Rank candidates by (support, mean_margin), descending.

A correct assignment fits its true French context at nearly every occurrence
(support -> 1); a wrong assignment beats the background only by luck at a
minority of occurrences (support ~ 0.3-0.6). The signal that drowned in one
window becomes decisive summed over K occurrences.

REUSED FROM ROUND 2 (imported, not rebuilt): the documented rule-based French
syllabifier, encipher_split, the era-corpus bigram models (Tocqueville t1+t2),
and Scorer.logp_bi. From code/crowd2/scorer_smith.py.

CONTROL (gate, non-negotiable)
------------------------------
Synthetic: tail-1200w Tocqueville t2 -> rule+encipher_split cells -> 96-cell
inventory -> random group mapping with the 7 GROUND-TRUTH anchors pinned
(seed 1841). Test set: top-40 non-anchor groups by frequency (each kept only
if >= 8 informative occurrences). Candidate pool: all 87 non-anchor inventory
cells (chance top-1 = 1/87). Rank candidates per group with THIS scorer;
worst-tie rank of the true planted value.
Pre-registered PASS: n_test >= 10 AND top-1 >= 3x chance AND MRR >= 0.30
(the bar round 2 failed: 0.021 < 0.076, 0.133 < 0.30).
If the control FAILS: verdict BROKEN-ON-CONTROL, no real drag (report NULL
with diagnosis, per WO3).

REAL DRAG (gated on control PASS)
----------------------------------
Top-40 unidentified R5005 groups x French function-word cells (distinct cells
from segmenting ~110 closed-class French words, each labelled by source
word). Current table = 7 ground-truth anchors + 87=ce / 64=qui / 96=par
(provisional, flagged everywhere); a 7-anchor-only variant is run as a
robustness check. Report top candidates per group WITH consistency numbers
(per-occurrence fit distributions, half-split agreement). NO promotion —
candidates only.

v1 CONTROL RESULT (2026-10-07): FAIL — top-1 0.045 vs chance 0.011 (4.0x,
passes) but MRR 0.217 < 0.30. Diagnosis: (a) support saturated at 1.0 for many
wrong values (random background too weak — common cells beat it everywhere);
(b) LET-tier attractors ('s','t') invaded SYL-tier groups' rankings via the
tier-crossing letter approximation; (c) mean_margin could not break the ties.
v2 FIX (principled, not tuned): strong frequency-based background per tier +
W=3 (more informative occurrences; the touching-bigram signal does not dilute
with W). v2 CONTROL: FAIL (top-1 0.091 = 8.1x chance, MRR 0.165).
v3 FIX: for SYL-tier candidates, drop touching bigrams with LET-tier neighbors
(the tier-crossing approximation projects syllables to edge letters, where
single-letter impostors matching an edge win). v3 CONTROL: FAIL (top-1 0.071,
MRR 0.217, 26/40 groups starved of SYL-SYL adjacencies).
FINAL: BROKEN-ON-CONTROL — three variants, all below the pre-registered bar.
The per-group consistency signal is real (true values are consistent) but not
distinctive (many wrong values are equally consistent); bigram contexts
underdetermine the cell. See scorer_smith_results.{json,md} for the full
diagnosis. Do NOT use this scorer for cell identification; the validated next
step is joint decipherment (annealing/EM over the full key).

API
---
  ConsistencyScorer(models, stream, table, W=2, n_bg=8, seed=1841)
      .score_candidate(g, v, sub=None) -> dict(n_occ, n_info, support,
          mean_margin, fits, quartiles, support_A, support_B)
          sub: optional index list into the informative occurrences
               (for independent-half agreement checks)
      .rank_candidates(g, candidates, sub=None) -> [(v, stats)] sorted by
          (support, mean_margin) desc, then value asc (deterministic)
      .drag(groups, candidate_pool) -> {g: ranked list}
  synthetic_control(models) -> dict with verdict PASS/FAIL
  real_drag(models, table=TABLE10) -> dict
  build_function_cells(models) -> {cell: [source words]}

Deterministic (seed 1841). No invented ciphertext: the only synthetic stream
is the labelled control. Real stream via crib_attack.load_pairs (1846 pairs).
"""

import collections
import json
import math
import os
import random
import re
import statistics
import sys

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
sys.path.insert(0, os.path.join(LANE, 'code'))
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd2'))
from crib_attack import load_pairs  # noqa: E402
from scorer_smith import build_models, Scorer, syllabify, encipher_split  # noqa: E402

DATA = os.path.join(LANE, 'data')
OUTD = os.path.join(LANE, 'code', 'crowd3')
os.makedirs(os.path.join(OUTD, 'report_inbox'), exist_ok=True)

SEED = 1841
W = 3          # window half-width (groups) around each occurrence
N_BG = 8       # background alternatives per tier

GROUND_TRUTH = {'11': 'la', '70': 'pre', '82': 'm', '34': 'i',
                '29': 'er', '40': 'e', '46': 'que'}
PROVISIONAL = {'87': 'ce', '64': 'qui', '96': 'par'}  # lane-inferred, flagged
TABLE10 = dict(GROUND_TRUTH, **PROVISIONAL)
ANCHOR_LETTERS = {'m', 'i', 'e'}
CELL2GRP = {v: k for k, v in TABLE10.items()}

_G = object()  # placeholder for "the group under test" in a decoded window


# ---------------------------------------------------------------- consistency scorer
class ConsistencyScorer:
    """Global-consistency scorer for (group -> cell value) candidates.

    models: dict from scorer_smith.build_models (era-corpus bigram models).
    stream: list of 2-char group strings.
    table:  dict group -> known cell (anchors; the candidate's group excluded).
    """

    def __init__(self, models, stream, table, W=W, n_bg=N_BG, seed=SEED):
        self.M = models
        self.stream = stream
        self.n = len(stream)
        self.table = dict(table)
        self.W = W
        letter_counts = {c: sum(1 for g in stream if g == CELL2GRP[c])
                         for c in ANCHOR_LETTERS}
        self.scorer = Scorer(models, letter_counts, len(stream))
        # v2: STRONG background — the most frequent corpus cells per tier.
        # Rationale (post-v1 diagnosis): "beats a random cell" is too weak a
        # null — common cells (s, t, de, le) beat random background at every
        # occurrence, so support saturated at 1.0 for many wrong values. The
        # scientifically meaningful null is "g is just a common cell": a
        # candidate must beat the toughest generic alternatives, in the same
        # windows, to earn support. Deterministic (no sampling).
        self.bg_syl = [u for u, _ in models['uni_s'].most_common(n_bg)]
        self.bg_let = [ch for ch, _ in models['uni_l'].most_common(n_bg)]
        self._shapes = {}  # g -> (occ_positions, [shapes|None per occurrence])
        self.seed = seed

    # -- background ------------------------------------------------------
    def _bg_for(self, v):
        bg = self.bg_let if Scorer.tier(v) == 'LET' else self.bg_syl
        return [b for b in bg if b != v] or list(bg)

    # -- occurrence shapes (cached per group) -----------------------------
    def _occ_shapes(self, g):
        """Per occurrence of g: list of touching-bigram shapes
        (left_cell|None, right_cell|None, left_is_g, right_is_g), or None
        where the occurrence is uninformative (no bigram touches g)."""
        if g in self._shapes:
            return self._shapes[g]
        s, W, table = self.stream, self.W, self.table
        occ, out = [], []
        for p, gp in enumerate(s):
            if gp != g:
                continue
            occ.append(p)
            lo = max(0, p - W)
            hi = min(self.n, p + W + 1)
            cells = []
            for j in range(lo, hi):
                gj = s[j]
                cells.append(_G if gj == g else table.get(gj))
            off = p - lo
            l = r = off
            while l - 1 >= 0 and cells[l - 1] is not None:
                l -= 1
            while r + 1 < len(cells) and cells[r + 1] is not None:
                r += 1
            run = cells[l:r + 1]
            if len(run) < 2:
                out.append(None)
                continue
            shapes = []
            for k in range(len(run) - 1):
                a, b = run[k], run[k + 1]
                ag, bg_ = a is _G, b is _G
                if ag or bg_:
                    shapes.append((None if ag else a, None if bg_ else b,
                                   ag, bg_))
            out.append(shapes or None)
        self._shapes[g] = (occ, out)
        return occ, out

    def _shape_mean(self, shapes, v):
        # v3: for SYL-tier v, drop bigrams touching LET-tier neighbors. The
        # tier-crossing approximation (score v via its edge letters) is lossy:
        # it projects the syllable to edge letters, where single-letter
        # impostors matching an edge (e.g. 's' for true 'les') win. Only
        # score what the model represents cleanly: SYL-SYL syllable bigrams
        # for SYL candidates; the letter model for LET candidates (all
        # touching bigrams). Returns None if no usable bigram survives.
        lb = self.scorer.logp_bi
        vtier = Scorer.tier(v)
        t = 0.0
        n = 0
        for a, b, ag, bg_ in shapes:
            if vtier == 'SYL' and not (ag and bg_):
                nb = b if ag else a          # the non-g neighbor cell
                if Scorer.tier(nb) != 'SYL':
                    continue                 # lossy tier-crossing: skip
            t += lb(v if bg_ else b, v if ag else a)
            n += 1
        return t / n if n else None

    # -- public API --------------------------------------------------------
    def score_candidate(self, g, v, sub=None):
        """Score one (group, value) candidate.

        Returns dict with n_occ, n_info, support (fraction of informative
        occurrences where v beats the tier-matched background), mean_margin,
        the raw per-occurrence fits, quartiles, and half-split supports
        (support_A/B over even/odd informative occurrences)."""
        occ, shapes_list = self._occ_shapes(g)
        info = [(p, sh) for p, sh in zip(occ, shapes_list) if sh]
        if sub is not None:
            info = [info[i] for i in sub]
        bg = self._bg_for(v)
        fits = []
        for _, shapes in info:
            sv = self._shape_mean(shapes, v)
            if sv is None:
                continue  # v3: no clean-tier bigram at this occurrence
            bm = sum(self._shape_mean(shapes, b) for b in bg) / len(bg)
            fits.append(sv - bm)
        n_info = len(fits)
        st = {'group': g, 'value': v, 'n_occ': len(occ), 'n_info': n_info,
              'fits': fits}
        if not n_info:
            st.update(support=0.0, mean_margin=float('-inf'),
                      support_A=None, support_B=None, quartiles=None)
            return st
        st['support'] = sum(1 for f in fits if f > 0) / n_info
        st['mean_margin'] = sum(fits) / n_info
        h = n_info // 2
        fa, fb = fits[:h], fits[h:]
        st['support_A'] = (sum(1 for f in fa if f > 0) / len(fa)) if fa else None
        st['support_B'] = (sum(1 for f in fb if f > 0) / len(fb)) if fb else None
        qs = statistics.quantiles(fits, n=4) if n_info >= 4 else []
        st['quartiles'] = {'min': min(fits),
                           'q1': qs[0] if qs else None,
                           'median': statistics.median(fits),
                           'q3': qs[2] if qs else None,
                           'max': max(fits)}
        return st

    def rank_candidates(self, g, candidates, sub=None):
        scored = [(v, self.score_candidate(g, v, sub=sub)) for v in candidates]
        scored.sort(key=lambda t: (t[1]['support'], t[1]['mean_margin'], t[0]),
                    reverse=True)
        return scored

    def drag(self, groups, candidate_pool):
        return {g: self.rank_candidates(g, candidate_pool) for g in groups}


# ---------------------------------------------------------------- function-word cells
FUNCTION_WORDS = [
    'le', 'la', 'les', 'un', 'une', 'des', 'du', 'de', 'au', 'aux',
    'ce', 'ces', 'cette', 'mon', 'ma', 'mes', 'ton', 'ta', 'tes',
    'son', 'sa', 'ses', 'notre', 'nos', 'votre', 'vos', 'leur', 'leurs',
    'chaque', 'quelque', 'quelques', 'aucun', 'aucune', 'tout', 'toute',
    'tous', 'toutes', 'tel', 'telle', 'autre', 'autres', 'même',
    'je', 'tu', 'il', 'elle', 'ils', 'elles', 'nous', 'vous', 'on',
    'me', 'te', 'se', 'lui', 'eux', 'y', 'en', 'moi', 'toi', 'soi',
    'ceci', 'cela', 'celui', 'celle', 'ceux', 'celles',
    'qui', 'que', 'quoi', 'dont', 'où', 'lequel', 'laquelle',
    'à', 'dans', 'sur', 'sous', 'par', 'pour', 'avec', 'sans', 'chez',
    'vers', 'entre', 'parmi', 'contre', 'depuis', 'pendant', 'durant',
    'selon', 'malgré',
    'et', 'ou', 'mais', 'donc', 'or', 'ni', 'car', 'comme', 'si',
    'quand', 'lorsque', 'puisque', 'quoique',
    'ne', 'pas', 'plus', 'très', 'bien', 'aussi', 'encore', 'déjà',
    'jamais', 'toujours', 'souvent', 'alors', 'ainsi', 'cependant', 'pourtant',
]


def build_function_cells(M):
    """Distinct cells from segmenting FUNCTION_WORDS (rule syllabifier +
    encipher_split), labelled by source word(s); table cells excluded."""
    table_cells = set(TABLE10.values())
    cell2words = collections.defaultdict(set)
    for w in FUNCTION_WORDS:
        for c in encipher_split(M['segs'](w)):
            if c not in table_cells:
                cell2words[c].add(w)
    return {c: sorted(ws) for c, ws in cell2words.items()}


# ---------------------------------------------------------------- helpers
def _spearman(order_a, order_b):
    """Spearman rho between two full orderings (lists of candidates)."""
    ra = {v: i for i, v in enumerate(order_a)}
    rb = {v: i for i, v in enumerate(order_b)}
    vs = list(order_a)
    n = len(vs)
    xs = [ra[v] for v in vs]
    ys = [rb[v] for v in vs]
    mx, my = sum(xs) / n, sum(ys) / n
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    dx = sum((x - mx) ** 2 for x in xs)
    dy = sum((y - my) ** 2 for y in ys)
    return num / math.sqrt(dx * dy) if dx and dy else 0.0


def _t2_tail_tokens(M):
    txt2 = open(os.path.join(DATA, 'gutenberg-30514-tocqueville-t2.txt'),
                encoding='utf-8', errors='replace').read()
    m1 = re.search(r'\*\*\* START OF.*?\*\*\*', txt2)
    m2 = re.search(r'\*\*\* END OF.*?\*\*\*', txt2)
    body = txt2[m1.end():m2.start()] if m1 and m2 else txt2
    toks = re.findall(r"[a-zàâäéèêëîïôöùûüÿçœæ]+", body.lower())
    return toks[-1200:]


# ---------------------------------------------------------------- synthetic control
def synthetic_control(M):
    """Encrypt held-out French through a KNOWN random syllabary (7 anchors
    pinned), run the consistency drag, measure planted-assignment recovery.

    Test: top-40 non-anchor groups by frequency (>= 8 informative occurrences
    each); candidate pool = all 87 non-anchor inventory cells (chance 1/87).
    Worst-tie rank of the true planted value per group.
    Pre-registered PASS: n_test >= 10 AND top-1 >= 3x chance AND MRR >= 0.30.
    """
    rng = random.Random(SEED)
    plain_words = _t2_tail_tokens(M)
    cell_seqs = [encipher_split(M['segs'](w)) for w in plain_words]
    freq = collections.Counter(c for s in cell_seqs for c in s)
    inventory = set(c for c, _ in freq.most_common(96)) | set(GROUND_TRUTH.values())
    if len(inventory) > 96:
        droppable = sorted((c for c in inventory - set(GROUND_TRUTH.values())),
                           key=lambda c: freq[c])
        inventory -= set(droppable[:len(inventory) - 96])

    kept, elided = [], 0
    for w, s in zip(plain_words, cell_seqs):
        if all(c in inventory for c in s):
            kept.append((w, s))
        else:
            elided += 1

    groups = ['%02d' % i for i in range(100)]
    rng.shuffle(groups)
    mapping, used = {}, set()
    for g, c in GROUND_TRUTH.items():          # pin the 7 ground-truth anchors
        mapping[c] = g
        used.add(g)
    rest = [c for c in inventory if c not in GROUND_TRUTH.values()]
    free = [g for g in groups if g not in used]
    rng.shuffle(free)
    for c, g in zip(rest, free):
        mapping[c] = g
    true_of_group = {g: c for c, g in mapping.items()}

    stream = []
    for _, s in kept:
        for c in s:
            stream.append(mapping[c])
    n = len(stream)
    assert len(set(stream)) <= 96

    sfreq = collections.Counter(stream)
    anchor_groups = set(GROUND_TRUTH)
    test40 = [g for g, _ in sfreq.most_common() if g not in anchor_groups][:40]
    candidates = sorted(c for c in inventory if c not in GROUND_TRUTH.values())
    chance = 1.0 / len(candidates)
    csc = ConsistencyScorer(M, stream, GROUND_TRUTH)

    detail, dropped = [], 0
    rec, mrr_num = 0, 0.0
    agree_num, rho_num = 0, 0.0
    sup_true_all, sup_top1_all = [], []
    for g in test40:
        ranked = csc.rank_candidates(g, candidates)
        tv = true_of_group[g]
        st_true = next(st for v, st in ranked if v == tv)
        if st_true['n_info'] < 8:
            dropped += 1
            continue
        key_tv = (st_true['support'], st_true['mean_margin'])
        better = sum(1 for _, st in ranked
                     if (st['support'], st['mean_margin']) > key_tv)
        tied = sum(1 for v, st in ranked
                   if (st['support'], st['mean_margin']) == key_tv and v != tv)
        rank = 1 + better + tied
        if rank == 1:
            rec += 1
        mrr_num += 1.0 / rank
        top_v, top_st = ranked[0]
        sup_true_all.append(st_true['support'])
        sup_top1_all.append(top_st['support'])
        # independent-half agreement: rank on even vs odd informative occs
        nI = st_true['n_info']
        subA = list(range(0, nI, 2))
        subB = list(range(1, nI, 2))
        rA = [v for v, _ in csc.rank_candidates(g, candidates, sub=subA)]
        rB = [v for v, _ in csc.rank_candidates(g, candidates, sub=subB)]
        agree = 1 if rA[0] == rB[0] else 0
        agree_num += agree
        rho = _spearman(rA, rB)
        rho_num += rho
        detail.append({'group': g, 'count': sfreq[g], 'n_info': nI,
                       'true_value': tv, 'rank_true': rank,
                       'n_candidates': len(candidates),
                       'support_true': round(st_true['support'], 4),
                       'margin_true': round(st_true['mean_margin'], 4),
                       'top1_value': top_v,
                       'support_top1': round(top_st['support'], 4),
                       'half_top1_agree': agree,
                       'half_spearman': round(rho, 4)})
    n_test = len(detail)
    top1 = rec / n_test if n_test else 0.0
    mrr = mrr_num / n_test if n_test else 0.0
    passed = (n_test >= 10 and top1 >= 3.0 * chance and mrr >= 0.30)
    return {
        'design': 'tail-1200w Tocqueville-t2, rule+encipher_split cells, '
                  '96-cell inventory, 7 ground-truth anchors pinned, random '
                  'mapping seed=1841; test=top-40 non-anchor groups by '
                  'frequency (>=8 informative occs); candidates=all 87 '
                  'non-anchor inventory cells; worst-tie ranks',
        'n_words_in': len(plain_words), 'n_words_kept': len(kept),
        'elision_rate': round(elided / len(plain_words), 4),
        'n_pairs': n, 'n_groups': len(set(stream)),
        'anchor_coverage': round(sum(sfreq[g] for g in anchor_groups) / n, 4),
        'n_candidates': len(candidates), 'chance_top1': round(chance, 4),
        'n_test': n_test, 'n_dropped_low_info': dropped,
        'top1_acc': round(top1, 4),
        'lift_over_chance': round(top1 / chance, 2) if chance else None,
        'mrr': round(mrr, 4),
        'median_support_true': round(statistics.median(sup_true_all), 4)
        if sup_true_all else None,
        'median_support_top1': round(statistics.median(sup_top1_all), 4)
        if sup_top1_all else None,
        'half_top1_agreement': round(agree_num / n_test, 4) if n_test else None,
        'half_spearman_mean': round(rho_num / n_test, 4) if n_test else None,
        'pass_criteria': 'n_test >= 10 AND top1 >= 3x chance AND mrr >= 0.30',
        'passed': passed,
        'verdict': 'PASS' if passed else 'BROKEN-ON-CONTROL',
        'bg_syl': csc.bg_syl, 'bg_let': csc.bg_let,
        'rank_detail': detail,
    }


# ---------------------------------------------------------------- real drag
def real_drag(M, table=TABLE10, label='table10'):
    """Consistency drag on R5005: top-40 unidentified groups x French
    function-word cells. Reports top candidates per group WITH consistency
    numbers (per-occurrence fit distributions, half-split agreement).
    Candidates are REPORTED ONLY — no promotion."""
    pairs, _, _ = load_pairs()
    assert len(pairs) == 1846 and len(set(pairs)) == 96
    freq = collections.Counter(pairs)
    unidentified = [g for g, _ in freq.most_common() if g not in table]
    groups = unidentified[:40]
    fcells = build_function_cells(M)
    candidates = sorted(fcells)
    csc = ConsistencyScorer(M, pairs, table)

    def pack(v, st):
        q = st['quartiles'] or {}
        return {
            'value': v, 'source_words': fcells[v],
            'n_occ': st['n_occ'], 'n_info': st['n_info'],
            'support': round(st['support'], 4),
            'mean_margin': round(st['mean_margin'], 4),
            'support_A': (round(st['support_A'], 4)
                          if st['support_A'] is not None else None),
            'support_B': (round(st['support_B'], 4)
                          if st['support_B'] is not None else None),
            'fit_quartiles': {k: (round(x, 4) if x is not None else None)
                              for k, x in q.items()},
            'fits': [round(f, 3) for f in st['fits']],
        }

    res_groups, watch = {}, []
    for g in groups:
        ranked = csc.rank_candidates(g, candidates)
        top = [pack(v, st) for v, st in ranked[:8]]
        res_groups[g] = {'count': freq[g], 'top8': top}
        for v, st in ranked:
            if st['n_info'] >= 8 and st['support'] >= 0.70:
                watch.append({'group': g, 'count': freq[g],
                              'value': v, 'source_words': fcells[v],
                              'n_info': st['n_info'],
                              'support': round(st['support'], 4),
                              'mean_margin': round(st['mean_margin'], 4),
                              'support_A': round(st['support_A'], 4),
                              'support_B': round(st['support_B'], 4)})
                break  # only the best per group on the watch list
    watch.sort(key=lambda d: (d['support'], d['mean_margin']), reverse=True)
    return {
        'table': label,
        'n_pairs': len(pairs),
        'anchor_coverage': round(sum(freq[g] for g in table) / len(pairs), 4),
        'n_groups_tested': len(groups),
        'n_candidates': len(candidates),
        'groups': res_groups,
        'watch_list_support_ge_070': watch,
        'note': 'candidates reported only; no promotion (red team owns it). '
                'Provisional anchors in table: 87=ce, 64=qui, 96=par.',
    }


# ---------------------------------------------------------------- main
def main():
    print('[models] building era-corpus models...', flush=True)
    M = build_models()
    print('  tokens=%d distinct_words=%d syll_vocab=%d' % (
        len(M['toks']), len(M['wfreq']), M['Vs']), flush=True)

    print('[control] synthetic encryption + consistency drag...', flush=True)
    ctl = synthetic_control(M)
    print('  words kept %d/%d (elision %.2f) pairs=%d groups=%d '
          'anchor_cov=%.3f' % (
              ctl['n_words_kept'], ctl['n_words_in'], ctl['elision_rate'],
              ctl['n_pairs'], ctl['n_groups'], ctl['anchor_coverage']),
          flush=True)
    print('  candidates=%d test=%d (dropped %d low-info)' % (
        ctl['n_candidates'], ctl['n_test'], ctl['n_dropped_low_info']),
        flush=True)
    print('  top1=%.3f chance=%.3f (x%.1f) mrr=%.3f -> %s' % (
        ctl['top1_acc'], ctl['chance_top1'],
        ctl['lift_over_chance'] or 0, ctl['mrr'], ctl['verdict']), flush=True)
    print('  median support: true=%.3f top1=%.3f | half top1-agree=%.3f '
          'spearman=%.3f' % (
              ctl['median_support_true'], ctl['median_support_top1'],
              ctl['half_top1_agreement'], ctl['half_spearman_mean']),
          flush=True)

    out = {
        'meta': {
            'worker': 'scorer-smith', 'work_order': 'WO3',
            'ground_truth_anchors': GROUND_TRUTH,
            'provisional_anchors': PROVISIONAL,
            'corpus': 'Tocqueville t1+t2 (1835/1840); rule-based syllabifier '
                      'and two-tier cell model imported from '
                      'code/crowd2/scorer_smith.py',
            'syll_vocab': M['Vs'], 'corpus_tokens': len(M['toks']),
            'window_halfwidth': W, 'n_background': N_BG, 'seed': SEED,
        },
        'control': ctl,
    }

    if not ctl['passed']:
        out['verdict'] = 'BROKEN-ON-CONTROL'
        out['real_drag'] = None
        out['note'] = ('Control FAILED: the consistency scorer does not '
                       'recover planted assignments above the pre-registered '
                       'bar. Real drag NOT run (WO3 gate). See diagnosis in '
                       'the markdown report.')
        print('[GATE] control failed -> BROKEN-ON-CONTROL, real drag skipped.',
              flush=True)
    else:
        print('[drag] control passed -> real drag on R5005 (table10)...',
              flush=True)
        rd10 = real_drag(M, TABLE10, 'table10')
        print('  groups=%d candidates=%d watch=%d' % (
            rd10['n_groups_tested'], rd10['n_candidates'],
            len(rd10['watch_list_support_ge_070'])), flush=True)
        print('[drag] robustness variant (7 ground-truth anchors only)...',
              flush=True)
        rd7 = real_drag(M, GROUND_TRUTH, 'table7')
        agree = sum(
            1 for g in rd10['groups']
            if rd10['groups'][g]['top8'][0]['value']
            == rd7['groups'][g]['top8'][0]['value'])
        out['verdict'] = 'CONTROL-PASS-DRAG-RUN'
        out['real_drag'] = {
            'table10': rd10, 'table7': rd7,
            'top1_agreement_table10_vs_table7':
                '%d/%d' % (agree, rd10['n_groups_tested']),
            'note': 'table10 = 7 ground-truth + 87=ce/64=qui/96=par '
                    '(provisional). table7 = ground truth only.',
        }
        print('  table10 vs table7 top-1 agreement: %d/%d' % (
            agree, rd10['n_groups_tested']), flush=True)
        print('  watch list (support>=0.70):', flush=True)
        for d in rd10['watch_list_support_ge_070'][:12]:
            print('    g=%s(n=%d) -> %-8s [%s] sup=%.3f A/B=%.2f/%.2f' % (
                d['group'], d['count'], d['value'],
                ','.join(d['source_words'][:3]), d['support'],
                d['support_A'], d['support_B']), flush=True)

    with open(os.path.join(OUTD, 'scorer_smith_results.json'), 'w') as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
    with open(os.path.join(OUTD, 'scorer_smith_results.md'), 'w') as f:
        f.write(render_md(out))
    print('[done] wrote code/crowd3/scorer_smith_results.{json,md}', flush=True)


def _qline(q):
    if not q or q['q1'] is None:
        return 'n<4'
    return 'med %.2f [%.2f..%.2f]' % (q['median'], q['q1'], q['q3'])


def render_md(out):
    m, c = out['meta'], out['control']
    L = []
    A = lambda *a: L.append(' '.join(str(x) for x in a))
    A('# SCORER SMITH ROUND 3 — global-consistency scorer (WO3)')
    A()
    A('**Verdict: %s**' % out['verdict'])
    A()
    A('Design: for each candidate (group g, cell v), decode ALL occurrences of '
      'g under the anchor table + {g:v}, keep only the bigrams TOUCHING a '
      'g-position (the 1–4 bigrams that discriminate v), and score '
      'fit_i(v) = s_i(v) − mean(background cells in the same window). '
      'support(v) = fraction of informative occurrences with fit>0; rank by '
      '(support, mean_margin). This is the N12 fix: the signal that tied '
      'inside one placement window becomes decisive summed over all '
      'occurrences. Syllabifier + two-tier cell model reused from round 2.')
    A()
    A('Anchors: 7 ground truth (11=la 70=pre 82=m 34=i 29=er 40=e 46=que); '
      'provisional: 87=ce 64=qui 96=par (flagged).')
    A()
    A('## Synthetic control (gate)')
    A('- Design: %s' % c['design'])
    A('- Stream: %d pairs, %d groups, anchor coverage %.3f; elision %.3f' % (
        c['n_pairs'], c['n_groups'], c['anchor_coverage'], c['elision_rate']))
    A('- Candidates/group: %d (chance top-1 %.4f); test groups: %d '
      '(dropped %d with <8 informative occurrences)' % (
          c['n_candidates'], c['chance_top1'], c['n_test'],
          c['n_dropped_low_info']))
    A('- Recovery: top-1 %.3f vs chance %.4f (x%.1f); MRR %.3f' % (
        c['top1_acc'], c['chance_top1'], c['lift_over_chance'] or 0, c['mrr']))
    A('- Consistency signal: median support(true)=%.3f vs '
      'median support(top-1)=%.3f' % (
          c['median_support_true'], c['median_support_top1']))
    A('- Independent halves: top-1 agreement %.3f, mean Spearman %.3f' % (
        c['half_top1_agreement'], c['half_spearman_mean']))
    A('- Bar: %s → **%s**' % (c['pass_criteria'], c['verdict']))
    A('- Background cells: SYL=%s LET=%s' % (
        ','.join(c['bg_syl']), ','.join(c['bg_let'])))
    A()
    A('| group | n | n_info | true | rank | support_true | top-1 | support_top1 | half_agree |')
    A('|---|---|---|---|---|---|---|---|---|')
    for d in c['rank_detail']:
        A('| %s | %d | %d | %s | %d | %.3f | %s | %.3f | %d |' % (
            d['group'], d['count'], d['n_info'], d['true_value'],
            d['rank_true'], d['support_true'], d['top1_value'],
            d['support_top1'], d['half_top1_agree']))
    A()
    if out['real_drag'] is None:
        A('## Real drag: NOT RUN (control failed — WO3 gate)')
        A()
        A(out['note'])
        A()
        A('## Diagnosis')
        A('TODO: filled by the worker if the gate fails.')
        return '\n'.join(L) + '\n'
    rd = out['real_drag']
    A('## Real drag (R5005, control-gated PASS)')
    for tag in ('table10', 'table7'):
        r = rd[tag]
        A('### table=%s (anchor coverage %.3f, %d groups x %d candidates)' % (
            tag, r['anchor_coverage'], r['n_groups_tested'],
            r['n_candidates']))
        A()
        A('| group | n | candidate | source words | n_info | support | '
          'A/B | margin | fit distribution |')
        A('|---|---|---|---|---|---|---|---|---|')
        for g, gd in r['groups'].items():
            for t in gd['top8'][:5]:
                A('| %s | %d | %s | %s | %d | %.3f | %.2f/%.2f | %+.3f | %s |' % (
                    g, gd['count'], t['value'],
                    ','.join(t['source_words'][:4]), t['n_info'], t['support'],
                    t['support_A'] or 0, t['support_B'] or 0,
                    t['mean_margin'], _qline(t['fit_quartiles'])))
        A()
    r10 = rd['table10']
    A('### Watch list (support >= 0.70, n_info >= 8) — candidates only, NOT promoted')
    A()
    if r10['watch_list_support_ge_070']:
        for d in r10['watch_list_support_ge_070']:
            A('- g=%s (n=%d) → **%s** [%s]: support=%.3f (A=%.2f B=%.2f), '
              'margin=%+.3f, n_info=%d' % (
                  d['group'], d['count'], d['value'],
                  ','.join(d['source_words'][:4]), d['support'],
                  d['support_A'], d['support_B'], d['mean_margin'],
                  d['n_info']))
    else:
        A('(empty — no candidate reached support 0.70)')
    A()
    A('### Robustness: table10 vs table7 top-1 agreement: %s' % (
        rd['top1_agreement_table10_vs_table7']))
    A()
    A('_87=ce, 64=qui, 96=par are provisional lane-inferred anchors; the '
      'table7 variant shows which top candidates survive without them._')
    return '\n'.join(L) + '\n'


if __name__ == '__main__':
    main()
