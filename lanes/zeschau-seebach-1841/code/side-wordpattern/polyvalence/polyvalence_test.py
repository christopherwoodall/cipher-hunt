#!/usr/bin/env python3
"""Polyvalence stress-test for the Seebach word-pattern matcher.

Gate question: does repetition-pattern matching survive the cipher's
polyvalence (same cipher group <- multiple plaintext syllables, and the
reverse)?

Polyvalence model (grounded in lane findings, see NOTES.md F24/F25/F31/N23):
  06 -> {/ma~/ (man,mant), /a~/ (an,ant)}      [WO1 /a~/ vs stem /ma~/, F25;
                                               restricted-"ent" PLAUSIBLE, 3 trigrams]
  94 -> {ne, en}                               [94="ne" provisional-strong F24;
                                               94="en" islets @1168/@1575 LEAD, F31]
  52 -> {pas, se}                              [52="pas" STRONG bounded F31;
                                               52="se" rival LEAD; K5 forces 52 polyvalence]
  59 -> {se}                                   [94->59 x2 "ne se", 59/52="se" LEAD, F31]
  i.e. "se" -> {52, 59} (split direction); "an" -> {06, 94} (split direction).

Forward test: for each lexicon word containing a polyvalent syllable, enumerate
ALL encipherments (per-position: poly group w.p. q*weight, else a unique
canonical placeholder). Pattern survival(q) = P(cipher pattern == lexicon
pattern). Exact enumeration (no sampling noise); Monte Carlo with two seeds
cross-validates.

Reverse test: for each cipher pattern P, the distortion closure =
plaintext patterns that can produce P under the model. Inflation(P) =
|union of naive lookups over closure| / |naive lookup of P|.

Weights: "se" -> 52/59 at 0.6/0.4 (observed 94->52 x3 vs 94->59 x2 in "ne se",
round-3 curation). "an" -> 06/94 uniform (no data). q swept (not identified).
"""
import json, math, random, itertools, sys
from collections import Counter, defaultdict
from pathlib import Path

LANE = Path.home() / 'workspace/cipher-hunt/lanes/zeschau-seebach-1841'
LEX = LANE / 'code' / 'side-wordpattern' / 'lexicon' / 'lexicon.jsonl'
OUT = Path(__file__).parent

# polyvalent phon syllable -> [(group, relative weight)]
POLY_PHON = {
    "man":  [("06", 1.0)],
    "mant": [("06", 1.0)],
    "an":   [("06", 0.5), ("94", 0.5)],
    "ant":  [("06", 1.0)],
    "n":    [("94", 1.0)],          # ne -> n after mute-e drop
    "pas":  [("52", 1.0)],
    "s":    [("52", 0.6), ("59", 0.4)],  # se -> s; 3/5 vs 2/5 observed
}
# orthographic variant
POLY_ORTH = {
    "man":  [("06", 1.0)],
    "ment": [("06", 1.0)],
    "an":   [("06", 1.0)],
    "ent":  [("06", 1.0)],
    "ne":   [("94", 1.0)],
    "en":   [("94", 1.0)],
    "pas":  [("52", 1.0)],
    "se":   [("52", 0.6), ("59", 0.4)],
}
QGRID = [0.05, 0.10, 0.20, 0.30, 0.50, 0.70, 0.90]


def pattern(seq):
    seen, out = {}, []
    for x in seq:
        if x not in seen:
            seen[x] = len(seen)
        k = seen[x]
        out.append(chr(65 + k) if k < 26 else chr(97 + k - 26))
    return ''.join(out)


def load():
    entries = [json.loads(l) for l in open(LEX, encoding='utf-8')]
    idx = defaultdict(list)   # (nsyl, ppat) -> [words]  (freq order kept)
    idx_o = defaultdict(list)
    for e in entries:
        idx[(e['nsyl'], e['ppat'])].append(e['w'])
        idx_o[(e['nsyl'], e['pat'])].append(e['w'])
    rank = {}
    for key, ws in list(idx.items()) + list(idx_o.items()):
        for r, w in enumerate(ws):
            rank.setdefault((key, w), r)
    return entries, idx, idx_o, rank


def enumerate_word(syllables, poly):
    """Yield (groups_tuple, n_poly_choices, weight_product_of_relative_weights).

    groups use real poly group labels and ('C', syllable) canonical tokens.
    n_poly_choices[k] counts positions using a poly group; the probability of
    an assignment at penetration q is prod(q*w_j)*(1-q)^(n-k)."""
    per_pos = []
    for s in syllables:
        opts = [(g, w) for g, w in poly.get(s, [])] + [(('C', s), None)]
        per_pos.append(opts)
    total = math.prod(len(o) for o in per_pos)
    for combo in itertools.product(*per_pos):
        groups, npoly, wprod = [], 0, 1.0
        for g, w in combo:
            groups.append(g)
            if w is not None:
                npoly += 1
                wprod *= w
        yield tuple(groups), npoly, wprod


def survival_curve(syllables, true_pat, poly, qgrid=QGRID, cap=20000):
    """Exact P(cipher pattern == true_pat) per q. Returns (dict q->p, reachable set).

    Per-position model: a polyvalent syllable uses a poly group w.p. q (split
    by relative weights) else its canonical placeholder w.p. 1-q; a
    non-polyvalent syllable always uses its canonical placeholder (prob 1)."""
    per_pos = []
    for s in syllables:
        per_pos.append([(g, w) for g, w in poly.get(s, [])] + [(('C', s), None)])
    total = math.prod(len(o) for o in per_pos)
    if total > cap:
        return None, None  # too big; caller falls back to Monte Carlo
    assigns = []  # (pattern, npoly, ncanon_poly, wprod)
    reachable = set()
    for combo in itertools.product(*per_pos):
        groups, npoly, ncanon, wprod = [], 0, 0, 1.0
        for (g, w), s in zip(combo, syllables):
            groups.append(g)
            if s in poly:          # polyvalent position: a real choice happened
                if w is not None:
                    npoly += 1
                    wprod *= w
                else:
                    ncanon += 1
            # non-polyvalent position: canonical forced, factor 1
        p = pattern(groups)
        reachable.add(p)
        assigns.append((p, npoly, ncanon, wprod))
    curve = {}
    for q in qgrid:
        s = 0.0
        for p, npoly, ncanon, wprod in assigns:
            if p == true_pat:
                s += (q ** npoly) * ((1 - q) ** ncanon) * wprod
        curve[q] = s
    return curve, reachable


def mc_check(syllables, true_pat, poly, q, trials=20000, seed=0):
    rng = random.Random(seed)
    hit = 0
    for _ in range(trials):
        groups = []
        for s in syllables:
            opts = poly.get(s, [])
            if opts and rng.random() < q:
                r, acc = rng.random(), 0.0
                tot = sum(w for _, w in opts)
                for g, w in opts:
                    acc += w / tot
                    if r <= acc:
                        groups.append(g)
                        break
            else:
                groups.append(('C', s))
        if pattern(groups) == true_pat:
            hit += 1
    return hit / trials


def main():
    entries, idx, idx_o, rank = load()
    by_word = {e['w']: e for e in entries}

    results = {'populations': {}, 'reverse': {}, 'control': {}, 'meta': {}}
    results['meta']['poly_phon'] = POLY_PHON
    results['meta']['poly_orth'] = POLY_ORTH
    results['meta']['qgrid'] = QGRID

    for tag, poly, patkey, idxmap in [('phon', POLY_PHON, 'ppat', idx),
                                      ('orth', POLY_ORTH, 'pat', idx_o)]:
        test = [e for e in entries if any(s in poly for s in e['syl' if tag == 'orth' else 'phon'])]
        sylkey = 'syl' if tag == 'orth' else 'phon'
        # islet subsets (overlapping)
        sets = {
            '06': [e for e in test if any(s in ("man", "mant", "an", "ant", "ment", "ent") for s in e[sylkey])],
            '94': [e for e in test if any(s in ("n", "an", "ne", "en") for s in e[sylkey])],
            '52': [e for e in test if any(s in ("pas", "s", "se") for s in e[sylkey])],
        }
        # at-risk: distortion structurally possible
        def atrisk(e):
            ph = e[sylkey]
            ii = [i for i, s in enumerate(ph) if s in poly]
            if len(ii) < 2:
                return False
            for a in range(len(ii)):
                for b in range(a + 1, len(ii)):
                    sa, sb = ph[ii[a]], ph[ii[b]]
                    ga = {g for g, _ in poly[sa]}
                    gb = {g for g, _ in poly[sb]}
                    if sa != sb and ga & gb:
                        return True
                    if sa == sb:
                        return True
            return False
        risk = [e for e in test if atrisk(e)]
        # repetition-bearing at-risk (the instrument's actual working set)
        rep_risk = [e for e in risk
                    if e[patkey] != ''.join(chr(65 + i) for i in range(len(e[sylkey])))]
        # repetition-bearing test words overall
        rep_all = [e for e in test
                   if e[patkey] != ''.join(chr(65 + i) for i in range(len(e[sylkey])))]

        pop = {}
        for name, words in [('all', test), ('atrisk', risk), ('rep_atrisk', rep_risk),
                            ('rep_all', rep_all),
                            ('islet06', sets['06']), ('islet94', sets['94']),
                            ('islet52', sets['52'])]:
            curves = []
            too_big = 0
            for e in words:
                c, _ = survival_curve(e[sylkey], e[patkey], poly)
                if c is None:
                    too_big += 1
                    continue
                curves.append(c)
            agg = {q: sum(c[q] for c in curves) / len(curves) if curves else None
                   for q in QGRID}
            # frequency-weighted (corpus freq) variant for 'all'
            fw = None
            if name == 'all' and curves:
                tot = sum(e['freq'] for e in words)
                fw = {q: sum(c[q] * e['freq'] for c, e in zip(curves, words)) / tot
                      for q in QGRID}
            pop[name] = {'n': len(words), 'mean_survival': agg,
                         'freq_weighted': fw, 'too_big': too_big}
        results['populations'][tag] = pop

        # ---- reverse test: distortion closure + inflation
        reachable = {}   # word -> set of cipher patterns
        for e in test:
            _, r = survival_curve(e[sylkey], e[patkey], poly)
            if r is not None:
                reachable[e['w']] = r
        # closure: cipher pattern -> set of plaintext patterns that can produce it
        closure = defaultdict(set)
        for w, rset in reachable.items():
            pt = by_word[w][patkey]
            for cp in rset:
                closure[cp].add(pt)
        infl = {}
        for cp, pset in closure.items():
            # find n: all words producing cp share len; take from any
            n = next(iter(len(by_word[w][sylkey]) for w in reachable
                          if cp in reachable[w]))
            naive = set(idxmap.get((n, cp), []))
            expanded = set()
            for pt in pset:
                expanded.update(idxmap.get((n, pt), []))
            infl[f"{n}|{cp}"] = {
                'naive': len(naive), 'expanded': len(expanded),
                'closure': sorted(pset),
                'inflation': (len(expanded) / len(naive)) if naive else None,
            }
        # focus: repetition-bearing cipher patterns
        rep_infl = {k: v for k, v in infl.items()
                    if v['closure'] != [k.split('|')[1]] or True}
        results['reverse'][tag] = {
            'n_cipher_patterns': len(infl),
            'inflation': infl,
        }

    # ---- control: 200 random words with NO polyvalent syllable (seed 1)
    rng = random.Random(1)
    ctrl_pool = [e for e in entries
                 if not any(s in POLY_PHON for s in e['phon'])]
    ctrl = rng.sample(ctrl_pool, 200)
    bad = 0
    for e in ctrl:
        c, _ = survival_curve(e['phon'], e['ppat'], POLY_PHON)
        if any(abs(c[q] - 1.0) > 1e-9 for q in QGRID):
            bad += 1
    results['control']['phon'] = {'n': 200, 'nonunit_survival': bad, 'seed': 1}

    # ---- Monte Carlo cross-validation on at-risk words (seeds 7 and 99)
    mc = []
    entries_phon = [e for e in entries if any(s in POLY_PHON for s in e['phon'])]
    def atrisk_p(e):
        ph = e['phon']
        ii = [i for i, s in enumerate(ph) if s in POLY_PHON]
        if len(ii) < 2: return False
        for a in range(len(ii)):
            for b in range(a + 1, len(ii)):
                sa, sb = ph[ii[a]], ph[ii[b]]
                ga = {g for g, _ in POLY_PHON[sa]}; gb = {g for g, _ in POLY_PHON[sb]}
                if (sa != sb and ga & gb) or sa == sb: return True
        return False
    risk = [e for e in entries_phon if atrisk_p(e)][:40]
    for e in risk:
        exact, _ = survival_curve(e['phon'], e['ppat'], POLY_PHON, qgrid=[0.5])
        m1 = mc_check(e['phon'], e['ppat'], POLY_PHON, 0.5, seed=7)
        m2 = mc_check(e['phon'], e['ppat'], POLY_PHON, 0.5, seed=99)
        mc.append({'w': e['w'], 'exact': exact[0.5], 'mc7': m1, 'mc99': m2})
    results['mc_validation'] = mc

    with open(OUT / 'results.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=1)
    print('wrote', OUT / 'results.json')
    # console summary
    for tag in ['phon', 'orth']:
        print(f'=== {tag} ===')
        for name in ['all', 'atrisk', 'rep_atrisk', 'rep_all', 'islet06', 'islet94', 'islet52']:
            p = results['populations'][tag][name]
            ms = p['mean_survival']
            def fmt(q):
                v = ms[q]
                return f"q={q}:{v:.3f}" if v is not None else f"q={q}:n/a"
            print(f"{name:10s} n={p['n']:5d} " + ' '.join(fmt(q) for q in [0.1, 0.3, 0.5, 0.9]))
    print('control non-unit:', results['control']['phon'])
    errs = [abs(d['exact'] - d['mc7']) for d in mc] + [abs(d['exact'] - d['mc99']) for d in mc]
    print(f'mc validation: max|exact-mc|={max(errs):.4f} over {len(mc)} words x2 seeds')
    # seed sensitivity of control sampling: rerun with seed 2
    rng2 = random.Random(2)
    ctrl2 = rng2.sample(ctrl_pool, 200)
    bad2 = 0
    for e in ctrl2:
        c, _ = survival_curve(e['phon'], e['ppat'], POLY_PHON)
        if any(abs(c[q] - 1.0) > 1e-9 for q in QGRID):
            bad2 += 1
    print('control seed2 non-unit:', bad2)


if __name__ == '__main__':
    main()
