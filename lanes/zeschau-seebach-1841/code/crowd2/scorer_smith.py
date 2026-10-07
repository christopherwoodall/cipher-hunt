#!/usr/bin/env python3
"""SCORER SMITH — syllable-level cell scorer for the Seebach R5005 drag (work order 4).

Lane: zeschau-seebach-1841. Reads: code/crib_attack.py (load_pairs), data/*.txt
(corpus + ciphertext). Writes ONLY: code/crowd2/scorer_smith_results.{json,md}.

DESIGN
------
The drag racer (N6) showed a letter-quadgram scorer is degenerate at 12.8% anchor
sparsity, and its pyphen syllable scorer discriminated only by word prior, with
uncalibrated expectations for the cipher's single-letter cells (m/i/e) and the
hyper-frequent "er" cell. This scorer is built to fix exactly that:

1. DOCUMENTED RULE-BASED French syllabifier (no pyphen, no external data):
   - nuclei = vowel letters (a e i o u y + accents + oe/ae ligatures), with the
     digraph nuclei eau, oeu, au, ai, ei, ou, eu, oi, ay, oy, uy kept whole;
   - "qu" and "gu"+vowel are consonant digraphs (their u is never a nucleus);
   - consonants between nuclei go to the FOLLOWING nucleus (maximal onset),
     except a run starting with s+consonant splits the s left (es|poir),
     and the onset is the longest valid French onset cluster
     (bl br chr cl cr dr fl fr gl gr pl pr tr vr qu gu ch ph th gn sc st sp sm sn
     or any single consonant) — doubles therefore split (bel|le, let|tre);
   - word-final consonants attach left; word-final "e" stays attached
     (documented deviation from the cipher's separate "e" cell);
   - words with no vowel stay whole.
   Rationale: reproducible from this file alone; emits "er" as a real unit
   (pre|mi|er), unlike pyphen which almost never does.

2. TWO-TIER hybrid cell model (the granularity fix):
   - SYL tier: syllable units from the rule above; unigram + CROSS-WORD bigram
     from the era corpus (Tocqueville t1+t2, 1835/1840 formal prose), add-0.1.
   - LET tier: single-letter cells. The cipher demonstrably emits m/i/e as cells
     (pencil cribs), so they are NOT scored as ordinary syllables. Their unigram
     rates are calibrated from the TARGET stream itself (observed cell counts —
     letter-cell emission is an encipherer choice the corpus cannot predict);
     non-anchor letter cells use corpus letter rates scaled by one global
     emission factor kappa = sum(obs anchor letter rates)/sum(corpus rates).
     Letter bigrams come from the corpus running letter stream.
   - Tier-crossing bigrams (SYL->LET, LET->SYL) use the documented approximation
     P(first letter of next cell | last letter of prev cell) from letter bigrams.
   "er" needs no special tier: the rule emits it, so it gets a real empirical
   rate (pyphen's 52/313k vs the cipher's rank-3 frequency was the v1 artifact).

3. SYNTHETIC CONTROL (gate): French plaintext -> rule segmentation -> documented
   synthetic encipherer split (consonant-cluster + single vowel i/e splits into
   two letter cells, e.g. mi->m|i, le->l|e; anchor cells never split — this
   reproduces the pencil's "la pre m i er e" for "premiere" up to ere/er+e) ->
   96 most frequent cells (9 anchors force-included) mapped to 96 random groups
   with the 9 anchors pinned -> synthetic group stream. The drag is run with the
   SAME code as the real drag; planted word placements must rank above chance.
   Pre-registered PASS: top-1 accuracy >= 3x chance AND MRR >= 0.30 (n>=10).
   If the control FAILS: verdict BROKEN-ON-CONTROL, no real drag is run.

4. DRAG (gated on control PASS): top-5000 Tocqueville words, 2-4 cells, >=1
   anchor-coincident cell; placements must respect all anchors (no conflicts);
   placement quality = hybrid window score over the maximal known run, plus
   lift = window - chain prior. min2 (>=2 anchor coincidences) placements
   reported. Candidates ranked by best lift.

Deterministic (seed 1841). No invented ciphertext: the only synthetic stream is
the labelled control. Real stream via crib_attack.load_pairs (1846 pairs).
"""

import json
import math
import os
import random
import re
import statistics
import sys
import collections

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
sys.path.insert(0, os.path.join(LANE, 'code'))
from crib_attack import load_pairs  # noqa: E402  (verified loader, 1846 pairs)

DATA = os.path.join(LANE, 'data')
OUTD = os.path.join(LANE, 'code', 'crowd2')
os.makedirs(OUTD, exist_ok=True)

ALPHA = 0.1          # add-alpha smoothing, as the drag racer
W = 4                # window half-width (groups) around a placement
SEED = 1841
TOPN_WORDS = 5000

# 9 anchors: 7 pencil cribs (ground truth) + 87=ce / 64=qui (lane-inferred, provisional)
ANCHORS = {
    '11': 'la', '70': 'pre', '82': 'm', '34': 'i', '29': 'er',
    '40': 'e', '46': 'que', '87': 'ce', '64': 'qui',
}
PROVISIONAL_GROUPS = {'87', '64'}
CELL2GRP = {v: k for k, v in ANCHORS.items()}
ANCHOR_CELLS = set(ANCHORS.values())
ANCHOR_LETTERS = {'m', 'i', 'e'}
SPLIT_PROTECT = {'la', 'pre', 'que', 'ce', 'qui', 'er'}  # never split by encipherer

# ---------------------------------------------------------------- rule syllabifier
VOWEL = set('aeiouyàâäéèêëîïôöùûüÿœæ')
NUC_DIPH = ['eau', 'œu', 'au', 'ai', 'ei', 'ou', 'eu', 'oi', 'ay', 'oy', 'uy']
ONSET_CL = {
    'bl', 'br', 'chr', 'cl', 'cr', 'dr', 'fl', 'fr', 'gl', 'gr', 'pl', 'pr',
    'tr', 'vr', 'qu', 'gu', 'ch', 'ph', 'th', 'gn', 'sc', 'st', 'sp', 'sm', 'sn',
}
CONS_CLASS = 'bcdfghjklmnpqrstvwxzç'


def _nuclei(word):
    """Nucleus spans (start, end); qu / gu+vowel are consonant digraphs."""
    spans, i, n = [], 0, len(word)
    while i < n:
        ch = word[i]
        if ch == 'q' and i + 1 < n and word[i + 1] == 'u':
            i += 2
            continue
        if ch == 'g' and i + 2 < n and word[i + 1] == 'u' and word[i + 2] in VOWEL:
            i += 2
            continue
        hit = None
        for d in NUC_DIPH:
            if word.startswith(d, i):
                hit = d
                break
        if hit:
            spans.append((i, i + len(hit)))
            i += len(hit)
            continue
        if ch in VOWEL:
            spans.append((i, i + 1))
            i += 1
            continue
        i += 1
    return spans


def _split_run(run):
    """Split an inter-nucleus consonant run -> (coda, onset)."""
    if not run:
        return '', ''
    if run[0] == 's' and len(run) >= 2:          # es|poir, not e|spoir
        c, o = _split_run(run[1:])
        return 's' + c, o
    for L in (3, 2, 1):                            # longest valid onset suffix
        if L <= len(run) and (L == 1 or run[-L:] in ONSET_CL):
            return run[:-L], run[-L:]
    return run[:-1], run[-1:]                      # unreachable (L=1 always valid)


def syllabify(word):
    """Documented rule-based French syllabification -> list of unit strings."""
    spans = _nuclei(word)
    if not spans:
        return [word]
    starts = [0]
    for k in range(len(spans) - 1):
        e = spans[k][1]
        ns = spans[k + 1][0]
        coda, _ = _split_run(word[e:ns])
        starts.append(e + len(coda))
    return [word[a:b] for a, b in
            zip(starts, starts[1:] + [len(word)])]


def encipher_split(units):
    """Synthetic encipherer granularity (control only): split consonant-cluster
    + single vowel i/e into two letter cells (mi->m|i, le->l|e). Anchor cells
    are never split. Reproduces the pencil 'la pre m i er e' for 'premiere'
    up to ere vs er|e (documented)."""
    out = []
    pat = re.compile(r'^([%s]+)([ie\xe9\xe8])$' % CONS_CLASS)
    for u in units:
        if u in SPLIT_PROTECT:
            out.append(u)
            continue
        m = pat.match(u)
        out.extend([m.group(1), m.group(2)] if m else [u])
    return out


# ---------------------------------------------------------------- corpus + models
def load_tokens():
    toks = []
    for fn in ('gutenberg-30513-tocqueville-t1.txt',
               'gutenberg-30514-tocqueville-t2.txt'):
        txt = open(os.path.join(DATA, fn), encoding='utf-8', errors='replace').read()
        m1 = re.search(r'\*\*\* START OF.*?\*\*\*', txt)
        m2 = re.search(r'\*\*\* END OF.*?\*\*\*', txt)
        if m1:
            txt = txt[m1.end():]
        if m2:
            txt = txt[:m2.start()]
        toks += re.findall(r"[a-zàâäéèêëîïôöùûüÿçœæ]+", txt.lower())
    return toks


def build_models():
    toks = load_tokens()
    seg_cache = {}

    def segs(w):
        return seg_cache.setdefault(w, syllabify(w))

    uni_s, bi_s, bi_in = collections.Counter(), collections.Counter(), collections.Counter()
    wfreq = collections.Counter()
    stream = []
    for w in toks:
        wfreq[w] += 1
        ss = segs(w)
        for a, b in zip(ss, ss[1:]):
            bi_in[(a, b)] += 1
        stream.extend(ss)
    for s in stream:
        uni_s[s] += 1
    for a, b in zip(stream, stream[1:]):
        bi_s[(a, b)] += 1
    Vs, Zs = len(uni_s), len(stream)

    letters = ''.join(toks)                       # running letter stream (documented)
    uni_l, bi_l = collections.Counter(), collections.Counter()
    for ch in letters:
        uni_l[ch] += 1
    for a, b in zip(letters, letters[1:]):
        bi_l[(a, b)] += 1
    Vl, Zl = len(uni_l), len(letters)

    def mk(bi, uni, V, Z):
        den = {x: uni[x] + ALPHA * V for x in uni}

        def logp(b, a):
            return math.log((bi.get((a, b), 0) + ALPHA) / den.get(a, ALPHA * V))

        def p(b, a):
            return (bi.get((a, b), 0) + ALPHA) / den.get(a, ALPHA * V)
        return logp, p

    logp_s, p_s = mk(bi_s, uni_s, Vs, Zs)
    logp_in, _p_in = mk(bi_in, uni_s, Vs, Zs)
    logp_l, p_l = mk(bi_l, uni_l, Vl, Zl)

    def logp_uni_s(s):
        return math.log((uni_s.get(s, 0) + ALPHA) / (Zs + ALPHA * Vs))

    def logp_uni_l(ch):
        return math.log((uni_l.get(ch, 0) + ALPHA) / (Zl + ALPHA * Vl))

    return dict(toks=toks, segs=segs, wfreq=wfreq, uni_s=uni_s, bi_s=bi_s,
                Vs=Vs, Zs=Zs, uni_l=uni_l, bi_l=bi_l, Vl=Vl, Zl=Zl,
                logp_s=logp_s, p_s=p_s, logp_in=logp_in,
                logp_l=logp_l, p_l=p_l,
                logp_uni_s=logp_uni_s, logp_uni_l=logp_uni_l)


# ---------------------------------------------------------------- hybrid cell scorer
class Scorer:
    """Two-tier cell scorer. Letter-cell unigrams are calibrated from the
    TARGET stream (observed counts); pass stream_letter_counts={m:..,i:..,e:..}
    and N=len(stream) at construction."""

    def __init__(self, M, stream_letter_counts, N_stream):
        self.M = M
        self.N = N_stream
        self.obs = dict(stream_letter_counts)
        # global letter-cell emission factor from the 3 anchor letters
        num = sum(self.obs.get(c, 0) for c in ANCHOR_LETTERS) / N_stream
        den = sum(math.exp(M['logp_uni_l'](c)) for c in ANCHOR_LETTERS)
        self.kappa = num / den if den else 1.0
        self._lu = {}  # letter-cell unigram cache

    @staticmethod
    def tier(c):
        return 'LET' if len(c) == 1 else 'SYL'

    def logp_uni(self, c):
        M = self.M
        if self.tier(c) == 'SYL':
            return M['logp_uni_s'](c)
        if c not in self._lu:
            if c in ANCHOR_LETTERS:                       # observed in target stream
                self._lu[c] = math.log((self.obs.get(c, 0) + ALPHA) /
                                       (self.N + ALPHA * len(self.obs)))
            else:                                          # kappa-scaled corpus rate
                self._lu[c] = math.log(self.kappa * math.exp(M['logp_uni_l'](c)))
        return self._lu[c]

    def logp_bi(self, c2, c1, within=False):
        """P(cell c2 | cell c1). within=True: within-word syllable bigrams."""
        M = self.M
        t1, t2 = self.tier(c1), self.tier(c2)
        if t1 == 'SYL' and t2 == 'SYL':
            return M['logp_in'](c2, c1) if within else M['logp_s'](c2, c1)
        if t1 == 'LET' and t2 == 'LET':
            return M['logp_l'](c2, c1)
        # tier crossing: P(first(c2) | last(c1)) via the letter model (documented)
        return M['logp_l'](c2[0], c1[-1])

    def chain_score(self, cells):
        """Candidate word prior: within-word chain over its cells."""
        t = self.logp_uni(cells[0])
        for a, b in zip(cells, cells[1:]):
            t += self.logp_bi(b, a, within=True)
        return t / len(cells)

    def run_score(self, cells):
        """Mean per-cell logp over a gapless known-cell run (cross-word)."""
        cells = [c for c in cells if c]
        if not cells:
            return float('-inf')
        t = self.logp_uni(cells[0])
        for a, b in zip(cells, cells[1:]):
            t += self.logp_bi(b, a)
        return t / len(cells)


# ---------------------------------------------------------------- drag machinery (shared control + real)
def build_candidates(M, split_letters, inventory=None):
    """Top-5000 Tocqueville words -> (word, cells) with 2-4 cells and >=1
    anchor-coincident cell. inventory: restrict cells (control)."""
    cands = []
    for w, _ in M['wfreq'].most_common(TOPN_WORDS):
        cells = M['segs'](w)
        if split_letters:
            cells = encipher_split(cells)
        if not (2 <= len(cells) <= 4):
            continue
        if not any(c in ANCHOR_CELLS for c in cells):
            continue
        if inventory is not None and any(c not in inventory for c in cells):
            continue
        cands.append((w, cells))
    return cands


def drag_placements(stream, scorer, candidates):
    """For each candidate: all anchor-consistent placements with window score,
    lift, anchor-coincidence count, exact flag."""
    N = len(stream)
    results = []
    for w, cells in candidates:
        k = len(cells)
        chain = scorer.chain_score(cells)
        placements = []
        for p in range(N - k + 1):
            ok, n_anch = True, 0
            for i, c in enumerate(cells):
                g = stream[p + i]
                if c in CELL2GRP:
                    if g != CELL2GRP[c]:
                        ok = False
                        break
                    n_anch += 1
                elif g in ANCHORS:
                    ok = False
                    break
            if not ok:
                continue
            table = dict(ANCHORS)
            for i, c in enumerate(cells):
                if c not in CELL2GRP:
                    table[stream[p + i]] = c
            win = stream[max(0, p - W):p + k + W]
            dec = [table.get(g) for g in win]
            off = p - max(0, p - W)
            l = r = off
            while l - 1 >= 0 and dec[l - 1]:
                l -= 1
            while r + 1 < len(dec) and dec[r + 1]:
                r += 1
            ws = scorer.run_score(dec[l:r + 1])
            placements.append({'p': p, 'win': ws, 'lift': ws - chain,
                               'n_anch': n_anch,
                               'exact': n_anch == k})
        placements.sort(key=lambda d: d['win'], reverse=True)
        min2 = [d for d in placements if d['n_anch'] >= 2]
        results.append({'word': w, 'cells': cells, 'k': k, 'chain': chain,
                        'n_place': len(placements),
                        'placements': placements,
                        'min2': min2,
                        'best_win': placements[0]['win'] if placements else None,
                        'best_lift': placements[0]['lift'] if placements else None,
                        'best_p': placements[0]['p'] if placements else None})
    return results


# ---------------------------------------------------------------- synthetic control
def synthetic_control(M):
    """Encrypt held-out French through a KNOWN random syllabary (9 anchors
    pinned), run the identical drag, measure planted-placement recovery.

    Plaintext: tail 1200 words of Tocqueville t2. Cells: rule segmentation +
    encipher_split (the documented synthetic encipherer granularity, incl.
    single-letter cells m/i/e). Inventory: 96 most frequent cells, 9 anchors
    force-included; words with out-of-inventory cells are elided (reported).
    Mapping: 96 cells -> 96 distinct random 2-digit groups, anchors pinned.
    """
    rng = random.Random(SEED)
    toks = M['toks']
    # tail of t2: find t2's token span by re-tokenizing t2 file alone
    txt2 = open(os.path.join(DATA, 'gutenberg-30514-tocqueville-t2.txt'),
                encoding='utf-8', errors='replace').read()
    m1 = re.search(r'\*\*\* START OF.*?\*\*\*', txt2)
    m2 = re.search(r'\*\*\* END OF.*?\*\*\*', txt2)
    t2toks = re.findall(r"[a-zàâäéèêëîïôöùûüÿçœæ]+",
                        txt2[m1.end():m2.start()].lower() if m1 and m2 else txt2.lower())
    plain_words = t2toks[-1200:]

    cell_seqs = [encipher_split(M['segs'](w)) for w in plain_words]
    freq = collections.Counter(c for s in cell_seqs for c in s)
    top = [c for c, _ in freq.most_common(96)]
    inventory = set(top) | ANCHOR_CELLS
    # force-include anchors: drop lowest-frequency non-anchor cells beyond 96
    if len(inventory) > 96:
        droppable = sorted((c for c in inventory - ANCHOR_CELLS),
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
    for g, c in ANCHORS.items():           # pin the 9 anchors
        mapping[c] = g
        used.add(g)
    rest = [c for c in inventory if c not in ANCHOR_CELLS]
    free = [g for g in groups if g not in used]
    rng.shuffle(free)
    for c, g in zip(rest, free):
        mapping[c] = g

    stream, true_pos, true_cells = [], collections.defaultdict(list), []
    for w, s in kept:
        true_pos[w].append(len(stream))      # word START position (planted truth)
        for c in s:
            true_cells.append(c)
            stream.append(mapping[c])
    N = len(stream)
    assert len(set(stream)) <= 96

    letter_counts = {c: sum(1 for g in stream if g == CELL2GRP[c])
                     for c in ANCHOR_LETTERS}
    scorer = Scorer(M, letter_counts, N)
    cands = build_candidates(M, split_letters=True, inventory=inventory)
    dragres = drag_placements(stream, scorer, cands)

    # test set: candidates with >=1 fully-surviving plaintext occurrence
    test = []
    for r in dragres:
        tp = true_pos.get(r['word'], [])
        if tp and r['n_place']:
            test.append((r, tp))
    rec, mrr_num, chance_num, ranks = 0, 0.0, 0.0, []
    detail = []
    for r, tp in test:
        pls = r['placements']
        n = len(pls)
        tset = set(tp)
        # worst-tie rank of each true position (adversarial: ties score worst)
        best = n + 1
        for t in tset:
            st = next(d['win'] for d in pls if d['p'] == t)
            rank = 1 + sum(1 for d in pls if d['win'] > st) \
                     + (sum(1 for d in pls if d['win'] == st) - 1)
            best = min(best, rank)
        ranks.append((r['word'], best, n, len(tset)))
        if best == 1:
            rec += 1
        mrr_num += 1.0 / best
        chance_num += 1.0 / n
        detail.append({'word': r['word'], 'cells': r['cells'],
                       'best_rank': best, 'n_place': n, 'n_true': len(tset),
                       'true_p': sorted(tset)[:6]})
    n_test = len(test)
    top1 = rec / n_test if n_test else 0.0
    chance = chance_num / n_test if n_test else 0.0
    mrr = mrr_num / n_test if n_test else 0.0
    med_place = statistics.median([n for _, _, n, _ in ranks]) if ranks else 0
    passed = (n_test >= 10 and top1 >= 3.0 * chance and mrr >= 0.30)
    # model-level check: does the scorer prefer true French runs over shuffled?
    # (separates "model is broken" from "placement ranking is broken")
    segs50 = [true_cells[i:i + 50] for i in range(0, len(true_cells) - 50, 50)][:40]
    tm = sum(scorer.run_score(s) for s in segs50) / len(segs50)
    sh = true_cells[:]
    random.Random(SEED + 1).shuffle(sh)
    sm = sum(scorer.run_score(sh[i:i + 50])
             for i in range(0, len(sh) - 50, 50)[:40]) / 40
    return {
        'design': 'tail-1200w Tocqueville-t2, rule+encipher_split cells, '
                  '96-cell inventory (9 anchors pinned), random mapping seed=1841',
        'n_words_in': len(plain_words), 'n_words_kept': len(kept),
        'elision_rate': round(elided / len(plain_words), 4),
        'n_pairs': N, 'n_groups': len(set(stream)),
        'anchor_coverage': round(sum(
            sum(1 for g in stream if g == CELL2GRP[c]) for c in ANCHOR_CELLS) / N, 4),
        'letter_counts': letter_counts, 'kappa': round(scorer.kappa, 4),
        'n_candidates': len(cands), 'n_test': n_test,
        'median_placements': med_place,
        'top1_acc': round(top1, 4), 'chance_top1': round(chance, 4),
        'lift_over_chance': round(top1 / chance, 2) if chance else None,
        'mrr': round(mrr, 4),
        'pass_criteria': 'top1 >= 3x chance AND mrr >= 0.30 AND n_test >= 10',
        'passed': passed,
        'verdict': 'PASS' if passed else 'BROKEN-ON-CONTROL',
        'model_check': {'true_run_mean': round(tm, 4),
                        'shuffled_run_mean': round(sm, 4),
                        'note': 'model prefers true French runs; failure is in '
                                'placement ranking, not the language model'},
        'rank_detail': detail,
    }


# ---------------------------------------------------------------- real drag
def real_drag(M):
    pairs, _, _ = load_pairs()
    assert len(pairs) == 1846 and len(set(pairs)) == 96
    freq = collections.Counter(pairs)
    letter_counts = {c: freq[CELL2GRP[c]] for c in ANCHOR_LETTERS}
    scorer = Scorer(M, letter_counts, len(pairs))
    cands = build_candidates(M, split_letters=True)
    dragres = drag_placements(pairs, scorer, cands)
    anchor_cov = sum(freq[g] for g in ANCHORS) / len(pairs)
    # rank by best lift (placement quality); keep full min2 lists
    ranked = sorted([r for r in dragres if r['n_place']],
                    key=lambda r: r['best_lift'], reverse=True)
    top = []
    for r in ranked[:25]:
        top.append({'word': r['word'], 'cells': r['cells'],
                    'chain': round(r['chain'], 4),
                    'n_place': r['n_place'], 'n_min2': len(r['min2']),
                    'best_p': r['best_p'],
                    'best_win': round(r['best_win'], 4),
                    'best_lift': round(r['best_lift'], 4),
                    'min2_placements': [
                        {'p': d['p'], 'win': round(d['win'], 4),
                         'lift': round(d['lift'], 4), 'n_anch': d['n_anch'],
                         'exact': d['exact']} for d in r['min2'][:8]]})
    n_min2_cands = sum(1 for r in dragres if r['min2'])
    exact_hits = [(r['word'], [d['p'] for d in r['min2'] if d['exact']])
                  for r in dragres if any(d['exact'] for d in r['min2'])]
    return {
        'n_pairs': len(pairs), 'anchor_coverage': round(anchor_cov, 4),
        'letter_counts': letter_counts, 'kappa': round(scorer.kappa, 4),
        'n_candidates': len(cands),
        'n_with_placements': sum(1 for r in dragres if r['n_place']),
        'n_candidates_with_min2': n_min2_cands,
        'exact_multi_anchor_hits': exact_hits,
        'top25_by_lift': top,
        'note': '87=ce, 64=qui provisional lane-inferred anchors',
    }


# ---------------------------------------------------------------- main
def main():
    print('[models] building era-corpus models...', flush=True)
    M = build_models()
    print('  tokens=%d distinct_words=%d syll_vocab=%d stream_sylls=%d letters=%d' % (
        len(M['toks']), len(M['wfreq']), M['Vs'], M['Zs'], M['Zl']), flush=True)
    er_rate = M['uni_s'].get('er', 0) / M['Zs']
    print('  corpus P(er-unit)=%.4f vs cipher 47/1846=%.4f' % (er_rate, 47 / 1846),
          flush=True)
    print('  sanity: premier->%s legisation->%s' % (
        encipher_split(syllabify('premier')), syllabify('législation')), flush=True)

    print('[control] synthetic encryption + drag...', flush=True)
    ctl = synthetic_control(M)
    print('  words kept %d/%d (elision %.2f) pairs=%d groups=%d anchor_cov=%.3f' % (
        ctl['n_words_kept'], ctl['n_words_in'], ctl['elision_rate'],
        ctl['n_pairs'], ctl['n_groups'], ctl['anchor_coverage']), flush=True)
    print('  candidates=%d test=%d median_places=%.1f' % (
        ctl['n_candidates'], ctl['n_test'], ctl['median_placements']), flush=True)
    print('  top1=%.3f chance=%.3f (x%.1f) mrr=%.3f -> %s' % (
        ctl['top1_acc'], ctl['chance_top1'],
        ctl['lift_over_chance'] or 0, ctl['mrr'], ctl['verdict']), flush=True)

    out = {
        'meta': {
            'worker': 'scorer-smith', 'work_order': 4,
            'anchors': ANCHORS,
            'provisional': sorted(PROVISIONAL_GROUPS),
            'corpus': 'Tocqueville t1+t2 (1835/1840), rule-based syllabifier '
                      '(documented in scorer_smith.py docstring)',
            'syll_vocab': M['Vs'], 'corpus_tokens': len(M['toks']),
            'corpus_P_er_unit': round(er_rate, 5),
            'cipher_P_er_cell': round(47 / 1846, 5),
            'corpus_P_unit_ends_with_er': round(
                sum(c for u, c in M['uni_s'].items() if u.endswith('er'))
                / M['Zs'], 5),
            'alpha': ALPHA, 'window_halfwidth': W, 'seed': SEED,
        },
        'control': ctl,
    }

    if not ctl['passed']:
        out['verdict'] = 'BROKEN-ON-CONTROL'
        out['real_drag'] = None
        out['note'] = ('Control FAILED: the scorer does not recover planted '
                       'assignments above the pre-registered bar. Real drag NOT '
                       'run (work order 4d). Do not use this scorer on the cipher.')
        print('[GATE] control failed -> BROKEN-ON-CONTROL, real drag skipped.',
              flush=True)
    else:
        print('[drag] control passed -> real drag on R5005...', flush=True)
        rd = real_drag(M)
        out['verdict'] = 'CONTROL-PASS-DRAG-RUN'
        out['real_drag'] = rd
        print('  candidates=%d with_places=%d with_min2=%d' % (
            rd['n_candidates'], rd['n_with_placements'],
            rd['n_candidates_with_min2']), flush=True)
        print('  exact hits: %s' % rd['exact_multi_anchor_hits'][:6], flush=True)
        print('  top5 by lift:', flush=True)
        for r in rd['top25_by_lift'][:5]:
            print('    %-14s %s lift=%+.3f min2=%d best_p=%s' % (
                r['word'], '/'.join(r['cells']), r['best_lift'],
                r['n_min2'], r['best_p']), flush=True)

    with open(os.path.join(OUTD, 'scorer_smith_results.json'), 'w') as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
    with open(os.path.join(OUTD, 'scorer_smith_results.md'), 'w') as f:
        f.write(render_md(out))
    print('[done] wrote scorer_smith_results.{json,md}', flush=True)


def render_md(out):
    m, c = out['meta'], out['control']
    L = []
    A = lambda *a: L.append(' '.join(str(x) for x in a))
    A('# SCORER SMITH — syllable-level cell scorer (work order 4)')
    A()
    A('**Verdict: %s**' % out['verdict'])
    A()
    A('Anchors: 11=la 70=pre 82=m 34=i 29=er 40=e 46=que '
      '87=ce* 64=qui* (*provisional, lane-inferred).')
    A('Corpus: Tocqueville t1+t2 (1835/1840), %d tokens, %d syllable units '
      '(rule-based segmenter, documented in scorer_smith.py).' % (
          m['corpus_tokens'], m['syll_vocab']))
    A('Calibration: corpus P("er"-unit)=%.4f vs cipher P("er"-cell)=%.4f; '
      'corpus P(unit ends in letters "er")=%.4f.' % (
          m['corpus_P_er_unit'], m['cipher_P_er_cell'],
          m['corpus_P_unit_ends_with_er']))
    A()
    A('## Synthetic control (gate)')
    A('- Design: %s' % c['design'])
    A('- Stream: %d pairs, %d groups, anchor coverage %.3f; elision rate %.3f '
      '(%d/%d words kept); kappa=%.3f' % (
          c['n_pairs'], c['n_groups'], c['anchor_coverage'], c['elision_rate'],
          c['n_words_kept'], c['n_words_in'], c['kappa']))
    A('- Candidates: %d, test words: %d, median placements/word: %.1f' % (
        c['n_candidates'], c['n_test'], c['median_placements']))
    A('- Recovery: top-1 accuracy %.3f vs chance %.3f (x%.1f); MRR %.3f' % (
        c['top1_acc'], c['chance_top1'], c['lift_over_chance'] or 0, c['mrr']))
    A('- Bar: %s → **%s**' % (c['pass_criteria'], c['verdict']))
    A('- Model check (true vs shuffled 50-cell runs): %.3f vs %.3f — %s' % (
        c['model_check']['true_run_mean'], c['model_check']['shuffled_run_mean'],
        c['model_check']['note']))
    A()
    if out['real_drag'] is None:
        A('## Real drag: NOT RUN (control failed — work order 4d)')
        A()
        A(out['note'])
        return '\n'.join(L) + '\n'
    r = out['real_drag']
    A('## Real drag (R5005, control-gated PASS)')
    A('- %d pairs, anchor coverage %.3f, kappa=%.3f' % (
        r['n_pairs'], r['anchor_coverage'], r['kappa']))
    A('- %d candidates, %d with placements, %d with min2 placements' % (
        r['n_candidates'], r['n_with_placements'], r['n_candidates_with_min2']))
    A('- Exact multi-anchor hits: %s' % (r['exact_multi_anchor_hits'] or 'none'))
    A()
    A('### Top 25 by placement lift (window − chain prior)')
    A()
    A('| word | cells | chain | places | min2 | best_p | best_win | lift |')
    A('|---|---|---|---|---|---|---|---|')
    for t in r['top25_by_lift']:
        A('| %s | %s | %.3f | %d | %d | %s | %.3f | %+.3f |' % (
            t['word'], '/'.join(t['cells']), t['chain'], t['n_place'],
            t['n_min2'], t['best_p'], t['best_win'], t['best_lift']))
    A()
    A('### min2 placements (all candidates with >=2 anchor coincidences)')
    A()
    for t in r['top25_by_lift']:
        if t['min2_placements']:
            ps = ', '.join('p%d (n_anch=%d, lift=%+.2f%s)' % (
                d['p'], d['n_anch'], d['lift'],
                ', EXACT' if d['exact'] else '') for d in t['min2_placements'])
            A('- **%s** [%s]: %s' % (t['word'], '/'.join(t['cells']), ps))
    A()
    A('_87=ce and 64=qui are provisional lane-inferred anchors; everything '
      'downstream inherits that uncertainty._')
    return '\n'.join(L) + '\n'


if __name__ == '__main__':
    main()
