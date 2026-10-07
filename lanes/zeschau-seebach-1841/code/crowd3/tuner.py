#!/usr/bin/env python3
"""
THE TUNER — crowd3 executor, zeschau-seebach-1841 lane.

Job: find what the three contact phases (A/B/C from the contactor's k=12
Jaccard cut) MEAN linguistically, via an era "tune template".

Method
------
1. PHASE MAP: recompute the contactor's phase assignments (k=12 Jaccard
   clusters -> A/B/C/R) from the pair stream, and re-verify the rotation
   numbers (block transition matrix, chi2) independently.
2. TUNE TEMPLATE: syllabify the Tocqueville era corpus (1835/1840, formal
   prose — the lane's era reference) with a DOCUMENTED rule, and count
   P(syllable | word-position) for initial / medial / final positions.
   Monosyllabic words count as both initial and final. This positional
   syllable distribution is the "tune".
3. PHASE HYPOTHESIS (fixed a priori, from the cycle shape + anchor roles,
   NOT from the corpus):
       C = word-final syllables   (29=er: prev A 0.77, next B 0.89)
       B = word-initial syllables (82=m [elided m'], 87=ce [proclitic],
                                   40=e [initial e as in etait/ecole]:
                                   prev C ~0.6-0.8 = prev word's final)
       A = word-medial syllables  (11=la, 34=i, 70=pre, 46=que)
4. LEAVE-ONE-OUT: hide each anchored group in turn; rank ALL corpus syllable
   types by their count in the hidden group's phase-position (phase-
   constrained) vs by total count (unconstrained baseline). Report top-k
   hit rates for k=1,5,10. Run with 7 ground-truth anchors and with all 10
   (incl. provisional 87=ce, 64=qui, 96=par), under TWO syllabification
   rules (maximal-onset R1, coda-maximal R2).
5. SHORTLISTS only if LOO validates.

Nulls are first-class. No crack claim. No invention of ciphertext or keys.
"""
import json, math, os, re, sys, unicodedata, collections

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.normpath(os.path.join(HERE, '..', '..'))
DATA = os.path.join(LANE, 'data')
sys.path.insert(0, os.path.join(LANE, 'code'))
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd'))
from crib_attack import load_pairs
from anneal import syllabify_word as syllabify_R1  # maximal-onset, documented in anneal.py

# ---------------------------------------------------------------- anchors
GT = {'11': 'la', '70': 'pre', '82': 'm', '34': 'i',
      '29': 'er', '40': 'e', '46': 'que'}            # 7 pencil cribs (ground truth)
PROV = {'87': 'ce', '64': 'qui', '96': 'par'}        # lane-inferred provisional
ALL10 = dict(GT, **PROV)

# Phase map: contactor k=12 Jaccard cut (verified below against JSON)
PHASE_A = set("01 06 11 14 16 30 32 33 34 35 36 38 39 43 44 46 48 61 63 64 66 68 70 81 83 84 86 92 93 94".split())
PHASE_B = set("02 07 12 15 19 20 21 31 37 40 42 45 47 49 53 60 62 65 69 71 74 80 82 85 87 89".split())
PHASE_C = set("03 08 09 17 23 24 26 29 41 50 51 52 56 59 67 76 77 78 79 88 91 96 98".split())
PHASE = {}
for g in PHASE_A: PHASE[g] = 'A'
for g in PHASE_B: PHASE[g] = 'B'
for g in PHASE_C: PHASE[g] = 'C'

# A-priori phase -> word-position hypothesis (fixed before touching the corpus)
PHASE_POS = {'A': 'medial', 'B': 'initial', 'C': 'final'}

# ---------------------------------------------------------------- rule R2: coda-maximal
VOWELS = set('aeiouy~AUIEVOW')
DIGRAPH_SUBS = [('eau', '~'), ('ai', 'A'), ('au', 'U'), ('ei', 'I'),
                ('eu', 'V'), ('oi', 'O'), ('ou', 'W')]
DIGRAPH_BACK = {v: k for k, v in DIGRAPH_SUBS}
ONSET2 = {'bl', 'br', 'cl', 'cr', 'dr', 'fl', 'fr', 'gl', 'gr', 'pl', 'pr',
          'tr', 'vr', 'ch', 'ph', 'th', 'gn', 'sc', 'sp', 'st', 'sm', 'sn',
          'sl', 'qu'}

def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')

def syllabify_R2(w):
    """Coda-maximal variant of the annealer's rule.

    DIFFERS from R1 in exactly two places:
      (1) single intervocalic consonant attaches LEFT  (VC|V, not V|CV);
      (2) final mute 'e' is NOT merged (stays its own final syllable).
    Digraph collapsing, ONSET2 set, and 'qu' handling identical to R1.
    Everything else: same code path as R1 (copy, not import, to keep the
    two rules independently auditable)."""
    w = strip_accents(w.lower())
    w = re.sub(r'[^a-z]', '', w)
    if not w:
        return []
    w = w.replace('qu', 'Q')
    for k, v in DIGRAPH_SUBS:
        w = w.replace(k, v)
    n = len(w)
    is_v = [c in VOWELS for c in w]
    if not any(is_v):
        return [w.replace('Q', 'qu')]
    bounds = []
    vpos = [i for i, v in enumerate(is_v) if v]
    for a, b in zip(vpos, vpos[1:]):
        run = w[a + 1:b]
        if len(run) == 0:
            if w[a] not in 'iu':
                bounds.append(b)          # hiatus (same as R1)
        elif len(run) == 1:
            bounds.append(a)              # *** VC|V (R1: V|CV at a+1)
        elif len(run) == 2:
            if run in ONSET2 or (run[0] == 'Q'):
                bounds.append(a + 1)      # V|CCV (same as R1)
            else:
                bounds.append(a + 2)      # VC|CV (same as R1)
        else:
            bounds.append(a + 2)          # VC|CCV (same as R1)
    syls, prev = [], 0
    for bnd in bounds:
        if bnd > prev:
            syls.append(w[prev:bnd]); prev = bnd
    syls.append(w[prev:])
    def restore(s):
        for k, v in DIGRAPH_BACK.items():
            s = s.replace(k, v)
        return s.replace('Q', 'qu')
    syls = [restore(s) for s in syls if s]
    # *** NO final mute-e merge (R1 merges pre|mi|re|e -> pre|mi|re)
    return syls

SPLIT_RE = re.compile(r"[\s'\-–—«»\".,;:!?()\[\]0-9]+")

def build_tune(paths, sylfn):
    """Tune: pos_counts[pos][syllable] over the era corpus.

    Tokenization mirrors the annealer (split on whitespace/punct incl.
    apostrophes and hyphens, so elided l'/d'/m'/s' become their own
    vowelless tokens). Each word's syllables get position flags:
    initial (index 0), medial (0<i<n-1), final (index n-1);
    monosyllabic words count as both initial and final."""
    pos_counts = {'initial': collections.Counter(),
                  'medial': collections.Counter(),
                  'final': collections.Counter()}
    n_words, n_syl_toks = 0, 0
    for path in paths:
        with open(path, encoding='utf-8', errors='replace') as f:
            for line in f:
                for frag in SPLIT_RE.split(line):
                    if not frag:
                        continue
                    syls = sylfn(frag)
                    if not syls:
                        continue
                    n_words += 1
                    n = len(syls)
                    for i, s in enumerate(syls):
                        n_syl_toks += 1
                        if i == 0:
                            pos_counts['initial'][s] += 1
                        if i == n - 1:
                            pos_counts['final'][s] += 1
                        if 0 < i < n - 1:
                            pos_counts['medial'][s] += 1
    return pos_counts, n_words, n_syl_toks

def rank_of(true_syl, scores):
    """Best-case rank (1-based): 1 + #syllables scoring strictly higher."""
    s = scores.get(true_syl, 0)
    return 1 + sum(1 for v in scores.values() if v > s)

def loo(anchors, tune, pos_of_phase):
    """Leave-one-out: hide each anchor, rank its true syllable.

    phase-constrained: rank by count in the anchor's phase-position.
    baseline:         rank by total count (initial+medial+final).
    Returns per-anchor ranks and top-k hit counts."""
    total = collections.Counter()
    for p in ('initial', 'medial', 'final'):
        total.update(tune[p])
    res, hits_pc, hits_bl = {}, {'1': 0, '5': 0, '10': 0}, {'1': 0, '5': 0, '10': 0}
    for g, true_syl in anchors.items():
        pos = pos_of_phase[PHASE[g]]
        r_pc = rank_of(true_syl, tune[pos])
        r_bl = rank_of(true_syl, total)
        res[g] = {'true': true_syl, 'phase': PHASE[g], 'pos': pos,
                  'rank_phase_constrained': r_pc, 'rank_baseline': r_bl}
        for k in (1, 5, 10):
            if r_pc <= k: hits_pc[str(k)] += 1
            if r_bl <= k: hits_bl[str(k)] += 1
    return res, hits_pc, hits_bl, len(anchors)

def main():
    pairs, odd_lines, off1 = load_pairs()
    assert len(pairs) == 1846 and len(set(pairs)) == 96, "pair-stream mismatch"
    assert set(PHASE) < set(pairs), "phase map must be a subset of observed groups"
    assert len(set(PHASE)) == 79, "A+B+C must cover 79 groups"
    uncovered = set(pairs) - set(PHASE)
    n_uncovered = sum(1 for p in pairs if p in uncovered)

    # --- verify contactor phase assignments + rotation from the pair stream
    cj = json.load(open(os.path.join(LANE, 'code', 'crowd',
                                     'contactor_results.json')))
    k12 = {g: None for c in cj['jaccard_clusters']['12'] for g in c['members']}
    # map contactor cluster -> our label by anchor content
    cmap = {}
    for c in cj['jaccard_clusters']['12']:
        an = set(c.get('anchors', []))
        if an == {'11', '34', '46', '70'}: cmap[id(c)] = 'A'
        elif an == {'40', '82', '87'}: cmap[id(c)] = 'B'
        elif an == {'29'}: cmap[id(c)] = 'C'
        else: cmap[id(c)] = 'R'
    agree = all(PHASE.get(g) == cmap[id(c)]
                for c in cj['jaccard_clusters']['12'] for g in c['members']
                if g in PHASE)
    blk = lambda g: PHASE.get(g, 'R')
    trans = collections.Counter((blk(a), blk(b))
                                for a, b in zip(pairs, pairs[1:]))
    rows = collections.Counter(blk(a) for a in pairs[:-1])
    cols = collections.Counter(blk(b) for b in pairs[1:])
    n = sum(trans.values())
    chi2, contrib = 0.0, {}
    for x in 'ABC':
        for y in 'ABC':
            exp = rows[x] * cols[y] / n
            obs = trans[(x, y)]
            chi2 += (obs - exp) ** 2 / exp
            contrib[f'{x}->{y}'] = {'obs': obs, 'exp': round(exp, 1),
                                    'ratio': round(obs / exp, 3)}
    # anchor block signatures
    sig = {}
    for g, v in ALL10.items():
        nxt = collections.Counter(blk(b) for a, b in zip(pairs, pairs[1:]) if a == g)
        prv = collections.Counter(blk(a) for a, b in zip(pairs, pairs[1:]) if b == g)
        tn, tp = sum(nxt.values()), sum(prv.values())
        sig[g] = {'value': v, 'phase': PHASE[g], 'freq': tn,
                  'next': {k: round(nxt[k] / tn, 3) for k in sorted(nxt)},
                  'prev': {k: round(prv[k] / tp, 3) for k in sorted(prv)}}

    # --- build the tune under both rules
    corpus = [os.path.join(DATA, 'gutenberg-30513-tocqueville-t1.txt'),
              os.path.join(DATA, 'gutenberg-30514-tocqueville-t2.txt')]
    tunes = {}
    for name, fn in (('R1_maximal_onset', syllabify_R1),
                     ('R2_coda_maximal', syllabify_R2)):
        tune, n_words, n_syl = build_tune(corpus, fn)
        inv = set(tune['initial']) | set(tune['medial']) | set(tune['final'])
        missing = [v for v in ALL10.values() if v not in inv]
        tunes[name] = (tune, n_words, n_syl, len(inv), missing)

    # --- anchor positional profiles (descriptive, from the tune)
    profiles = {}
    for name, (tune, *_rest) in tunes.items():
        profiles[name] = {}
        for g, v in ALL10.items():
            ci = tune['initial'][v]; cm = tune['medial'][v]; cf = tune['final'][v]
            t = ci + cm + cf
            profiles[name][f'{g}={v}'] = {
                'phase': PHASE[g], 'hyp_pos': PHASE_POS[PHASE[g]],
                'P': {'initial': round(ci / t, 3), 'medial': round(cm / t, 3),
                      'final': round(cf / t, 3)} if t else None,
                'modal': max((('initial', ci), ('medial', cm), ('final', cf)),
                             key=lambda x: x[1])[0] if t else None,
                'total': t}

    # --- leave-one-out under 4 configs
    loo_out = {}
    for tname, (tune, n_words, n_syl, inv_n, missing) in tunes.items():
        for aname, anchors in (('GT7', GT), ('ALL10', ALL10)):
            res, hpc, hbl, m = loo(anchors, tune, PHASE_POS)
            loo_out[f'{tname}__{aname}'] = {
                'n_anchors': m, 'hits_phase_constrained': hpc,
                'hits_baseline': hbl, 'per_anchor': res,
                'inventory_size': inv_n, 'anchors_missing_from_inventory': missing,
                'corpus_words': n_words, 'corpus_syl_tokens': n_syl}

    # --- shortlist candidates (only to be emitted if LOO validates)
    freq = collections.Counter(pairs)
    shortlists = {}
    for tname, (tune, *_rest) in tunes.items():
        shortlists[tname] = {}
        valued_syls = set(ALL10.values())
        for g, f in freq.most_common():
            if g in ALL10 or g not in PHASE:
                continue
            pos = PHASE_POS[PHASE[g]]
            ranked = sorted(((s, tune[pos][s]) for s in tune[pos]
                             if s not in valued_syls),
                            key=lambda x: -x[1])[:10]
            shortlists[tname][g] = {'freq': f, 'phase': PHASE[g], 'pos': pos,
                                    'top10': [(s, c) for s, c in ranked]}

    out = {
        'counts_verified': {'pairs': len(pairs), 'distinct': len(set(pairs)),
                            'odd_lines': odd_lines, 'off1': off1},
        'phase_map_matches_contactor_k12': agree,
        'uncovered_groups_in_R': sorted(uncovered),
        'uncovered_pair_tokens': n_uncovered,
        'block_transition_recompute': {
            'matrix': {f'{x}->{y}': trans[(x, y)] for x in 'ABCR' for y in 'ABCR'},
            'row_n': dict(rows), 'chi2_3x3': round(chi2, 1), 'df': 4,
            'contributions': contrib},
        'anchor_block_signatures': sig,
        'phase_position_hypothesis': PHASE_POS,
        'tune_rules': {
            'R1_maximal_onset': 'anneal.py syllabify_word: maximal-onset '
            '(V|CV), vowel digraphs collapsed, qu->Q, final mute-e merged '
            'into previous syllable.',
            'R2_coda_maximal': 'tuner.py syllabify_R2: identical except '
            'single intervocalic consonant attaches LEFT (VC|V) and final '
            "mute-e kept as its own syllable."},
        'anchor_positional_profiles': profiles,
        'leave_one_out': loo_out,
        'shortlists_pending_validation': shortlists,
    }
    jp = os.path.join(HERE, 'tuner_results.json')
    with open(jp, 'w') as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
    print('wrote', jp)
    return out

if __name__ == '__main__':
    main()
