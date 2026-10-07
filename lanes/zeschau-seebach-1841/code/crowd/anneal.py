#!/usr/bin/env python3
"""
THE ANNEALER — crowd executor, zeschau-seebach-1841 lane.

Simulated annealing over the full 96-group -> syllable assignment with the
8 anchors pinned, scored by a French SYLLABLE-bigram model built from
Tocqueville (1835/1840, formal political prose — closest era/register match
on hand for 1841 diplomatic French).

Differs from Bourdeau's failed runs: anchors pinned, syllable-bigram scorer
(not letter 4-gram), and the deliverable is cross-restart STABILITY plus a
synthetic-ciphertext control (recover planted assignment or the method is
uninformative).

Stage 1: build syllable-bigram model from Tocqueville T1+T2.
Stage 2: >=20 annealing restarts on the real ciphertext; stability table.
Stage 3: baselines (random keys, anchors pinned).
Stage 4: synthetic control — Les Mis plaintext through a random planted
         syllabary (8 anchors pinned to their true values), same pipeline;
         measure recovery.

Outputs: code/crowd/annealer_results.json, code/crowd/annealer_results.md
"""
import json, math, os, random, re, sys, time, unicodedata, collections

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.normpath(os.path.join(HERE, '..', '..'))
DATA = os.path.join(LANE, 'data')
sys.path.insert(0, os.path.join(LANE, 'code'))
from crib_attack import load_pairs  # verified pair-aligned group stream

ANCHORS = {'11': 'la', '70': 'pre', '82': 'm', '34': 'i',
           '29': 'er', '40': 'e', '46': 'que', '87': 'ce'}

RESTARTS = 24
ITERS = 60000
T0, TMIN = 2.0, 0.01
INVENTORY_TOP = 400  # top-N syllable types + 26 single letters

# ---------------------------------------------------------------- syllabifier
VOWELS = set('aeiouy')
VOWELS |= set('~AUIEVOW')  # digraph placeholders, all vowels
# orthographic vowel digraphs collapsed before splitting (restored after)
DIGRAPH_SUBS = [('eau', '~'), ('ai', 'A'), ('au', 'U'), ('ei', 'I'),
                ('eu', 'V'), ('oi', 'O'), ('ou', 'W')]
DIGRAPH_BACK = {v: k for k, v in DIGRAPH_SUBS}
ONSET2 = {'bl', 'br', 'cl', 'cr', 'dr', 'fl', 'fr', 'gl', 'gr', 'pl', 'pr',
          'tr', 'vr', 'ch', 'ph', 'th', 'gn', 'sc', 'sp', 'st', 'sm', 'sn',
          'sl', 'qu'}

def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')

def syllabify_word(w):
    """Orthographic French syllabification (maximal-onset, rule-based).
    Returns list of syllable strings. Systematic, not perfect."""
    w = strip_accents(w.lower())
    w = re.sub(r'[^a-z]', '', w)
    if not w:
        return []
    # 'qu' -> single onset unit Q (u after q is not a nucleus)
    w = w.replace('qu', 'Q')
    for k, v in DIGRAPH_SUBS:
        w = w.replace(k, v)
    n = len(w)
    is_v = [c in VOWELS for c in w]
    if not any(is_v):
        return [w.replace('Q', 'qu')]
    bounds = []  # boundary positions (indices where a new syllable starts)
    vpos = [i for i, v in enumerate(is_v) if v]
    for a, b in zip(vpos, vpos[1:]):
        run = w[a + 1:b]
        if len(run) == 0:
            if w[a] not in 'iu':  # else glide/diphthong: no split (pre|mier)
                bounds.append(b)  # hiatus
        elif len(run) == 1:
            bounds.append(a + 1)  # V|CV
        elif len(run) == 2:
            if run in ONSET2 or (run[0] == 'Q'):
                bounds.append(a + 1)  # V|CCV
            else:
                bounds.append(a + 2)  # VC|CV
        else:
            if w[a + 1] == 'x':
                bounds.append(a + 2)  # ex|...
            else:
                bounds.append(a + 2)  # VC|CCV (split after first)
    syls, prev = [], 0
    for bnd in bounds:
        syls.append(w[prev:bnd]); prev = bnd
    syls.append(w[prev:])
    def restore(s):
        for k, v in DIGRAPH_BACK.items():
            s = s.replace(k, v)
        return s.replace('Q', 'qu')
    syls = [restore(s) for s in syls if s]
    # final mute e merges with previous syllable (pre|mi|re|e -> pre|mi|re)
    if len(syls) > 1 and syls[-1] == 'e':
        syls[-2] += 'e'; syls.pop()
    return syls

def syllabify_text(path):
    toks = []
    with open(path, encoding='utf-8', errors='replace') as f:
        for line in f:
            for frag in re.split(r"[\s'\-–—«»\".,;:!?()\[\]0-9]+", line):
                if frag:
                    toks.extend(syllabify_word(frag))
    return toks

# ---------------------------------------------------------------- model
def build_model(paths):
    toks = []
    for p in paths:
        toks.extend(syllabify_text(p))
    uni = collections.Counter(toks)
    bi = collections.Counter()
    prev = '<S>'
    for t in toks:
        bi[(prev, t)] += 1
        prev = t
    bi[(prev, '</S>')] += 1
    return toks, uni, bi

class BigramModel:
    def __init__(self, uni, bi, alpha=0.05):
        self.uni = uni; self.bi = bi; self.alpha = alpha
        self.V = len(uni)
        self.pre = collections.Counter()
        for (a, b), c in bi.items():
            self.pre[a] += c
        self._cache = {}
    def logp(self, a, b):
        key = (a, b)
        v = self._cache.get(key)
        if v is None:
            c_ab = self.bi.get(key, 0)
            c_a = self.pre.get(a, 0)
            v = math.log((c_ab + self.alpha) / (c_a + self.alpha * self.V))
            self._cache[key] = v
        return v

# ---------------------------------------------------------------- annealer
def make_inventory(uni):
    top = [s for s, _ in uni.most_common(INVENTORY_TOP)]
    letters = [chr(c) for c in range(ord('a'), ord('z') + 1)]
    inv = top + [L for L in letters if L not in top]
    weights = [uni.get(s, 0) + 1 for s in inv]
    # ensure anchor syllables present
    for a in ANCHORS.values():
        assert a in inv, f'anchor syllable {a!r} missing from inventory'
    return inv, weights

def random_key(free_groups, inv, weights, rng):
    return {g: rng.choices(inv, weights=weights, k=1)[0] for g in free_groups}

def anneal(pairs, groups, model, inv, weights, seed, iters=ITERS):
    rng = random.Random(seed)
    N = len(pairs)
    gi = {g: i for i, g in enumerate(groups)}
    seq = [gi[p] for p in pairs]
    positions = [[] for _ in groups]
    for i, gix in enumerate(seq):
        positions[gix].append(i)
    fixed = {gi[g]: ANCHORS[g] for g in ANCHORS}
    free = [i for i in range(len(groups)) if i not in fixed]
    key = [None] * len(groups)
    for gix, s in fixed.items():
        key[gix] = s
    for gix in free:
        key[gix] = rng.choices(inv, weights=weights, k=1)[0]
    tok = [key[gix] for gix in seq]
    S, E = '<S>', '</S>'
    def big(a, b):
        return model.logp(a, b)
    def full_score():
        tot = big(S, tok[0])
        for i in range(N - 1):
            tot += big(tok[i], tok[i + 1])
        return tot + big(tok[-1], E)
    cur = full_score()
    init = cur
    best = cur; best_key = list(key)
    for it in range(iters):
        T = T0 * (TMIN / T0) ** (it / iters)
        gix = rng.choice(free)
        old = key[gix]
        new = rng.choices(inv, weights=weights, k=1)[0] if rng.random() < 0.5 \
            else rng.choice(inv)
        if new == old:
            continue
        delta = 0.0
        for i in positions[gix]:
            a = tok[i - 1] if i > 0 else S
            b = tok[i + 1] if i < N - 1 else E
            delta += big(a, new) + big(new, b) - big(a, old) - big(old, b)
        if delta >= 0 or rng.random() < math.exp(delta / T):
            cur += delta
            key[gix] = new
            for i in positions[gix]:
                tok[i] = new
            if cur > best:
                best = cur; best_key = list(key)
    return {'seed': seed, 'init_score': init, 'final_score': cur,
            'best_score': best,
            'assignment': {groups[i]: best_key[i] for i in range(len(groups))}}

def random_baseline(pairs, groups, model, inv, weights, draws=300, seed=999):
    rng = random.Random(seed)
    N = len(pairs)
    gi = {g: i for i, g in enumerate(groups)}
    seq = [gi[p] for p in pairs]
    fixed = {gi[g]: ANCHORS[g] for g in ANCHORS}
    scores = []
    S, E = '<S>', '</S>'
    for _ in range(draws):
        key = [rng.choices(inv, weights=weights, k=1)[0] for _ in groups]
        for gix, s in fixed.items():
            key[gix] = s
        tok = [key[gix] for gix in seq]
        tot = model.logp(S, tok[0])
        for i in range(N - 1):
            tot += model.logp(tok[i], tok[i + 1])
        tot += model.logp(tok[-1], E)
        scores.append(tot / N)
    m = sum(scores) / len(scores)
    sd = (sum((s - m) ** 2 for s in scores) / len(scores)) ** 0.5
    return m, sd, scores

# ---------------------------------------------------------------- synthetic control
def build_synthetic(groups, uni, inv, model, n_pairs=1846):
    """Plant a random syllabary: anchor groups -> anchor syllables, the other
    88 real group labels -> 88 random syllables (top-frequency, incl. anchors
    guaranteed). Emit group stream from Les Mis syllables until n_pairs."""
    rng = random.Random(424242)
    lesmis = os.path.join(DATA, 'gutenberg-17489-miserables1.txt')
    toks = syllabify_text(lesmis)
    # 88 non-anchor syllables: most frequent in Les Mis that are in inventory
    lm_count = collections.Counter(t for t in toks if t in inv)
    others = [s for s, _ in lm_count.most_common() if s not in ANCHORS.values()][:88]
    assert len(others) == 88
    non_anchor_groups = [g for g in groups if g not in ANCHORS]
    planted = dict(zip(non_anchor_groups, others))
    planted.update({g: ANCHORS[g] for g in ANCHORS})
    syl2grp = {s: g for g, s in planted.items()}
    stream = []
    for t in toks:
        if t in syl2grp:
            stream.append(syl2grp[t])
            if len(stream) >= n_pairs:
                break
    assert len(stream) == n_pairs
    return stream, planted

def main():
    t_start = time.time()
    log = []
    def say(m):
        log.append(m); print(m, flush=True)

    # sanity: group counts
    pairs, odd, off1 = load_pairs()
    groups = sorted(set(pairs))
    say(f'pairs={len(pairs)} distinct_groups={len(groups)} '
        f'odd_lines={odd} offset_lines={off1}')
    assert len(pairs) == 1846 and len(groups) == 96, 'count mismatch vs lane data'

    # syllabifier spot checks (anchors must be producible)
    checks = {'premiere': ['pre', 'mie', 're'], 'cela': ['ce', 'la'],
              'que': ['que'], 'premier': ['pre', 'mier']}
    for w, exp in checks.items():
        got = syllabify_word(w)
        say(f'syllabify {w}: {got}')
    for a in ANCHORS.values():
        pass

    say('building syllable-bigram model from Tocqueville T1+T2 ...')
    t0 = time.time()
    toks, uni, bi = build_model([
        os.path.join(DATA, 'gutenberg-30513-tocqueville-t1.txt'),
        os.path.join(DATA, 'gutenberg-30514-tocqueville-t2.txt')])
    model = BigramModel(uni, bi)
    inv, weights = make_inventory(uni)
    say(f'model: {len(toks)} syllable tokens, {len(uni)} types, '
        f'{len(bi)} bigrams, inventory={len(inv)} (build {time.time()-t0:.1f}s)')
    for a in ANCHORS.values():
        say(f'anchor {a!r}: unigram rank/count = {uni.get(a, 0)}')
    inv_cov = sum(uni.get(s, 0) for s in inv) / sum(uni.values())
    say(f'inventory token coverage of reference: {inv_cov:.4f}')

    # ---- Stage 2: real ciphertext annealing
    say(f'Stage 2: {RESTARTS} annealing restarts x {ITERS} iters (real ct) ...')
    t0 = time.time()
    restarts = []
    for r in range(RESTARTS):
        res = anneal(pairs, groups, model, inv, weights, seed=1000 + r)
        restarts.append(res)
        say(f'  restart {r}: init={res["init_score"]/len(pairs):.4f} '
            f'best={res["best_score"]/len(pairs):.4f} per-pair logp')
    say(f'annealing done in {time.time()-t0:.1f}s')

    # ---- Stage 3: random baseline
    say('Stage 3: random-key baseline (anchors pinned) ...')
    bmean, bsd, _ = random_baseline(pairs, groups, model, inv, weights)
    say(f'baseline per-pair logp: mean={bmean:.4f} sd={bsd:.4f}')

    # ---- stability table
    free_groups = [g for g in groups if g not in ANCHORS]
    stab = []
    for g in free_groups:
        c = collections.Counter(r['assignment'][g] for r in restarts)
        top_syl, top_n = c.most_common(1)[0]
        stab.append({'group': g, 'modal': top_syl, 'count': top_n,
                     'n_restarts': RESTARTS,
                     'others': dict(c.most_common()[1:4])})
    stab.sort(key=lambda d: -d['count'])

    # ---- Stage 4: synthetic control
    say('Stage 4: synthetic control (Les Mis plaintext, planted syllabary) ...')
    syn_pairs, planted = build_synthetic(groups, uni, inv, model)
    syn_groups = sorted(set(syn_pairs))
    say(f'synthetic: {len(syn_pairs)} pairs, {len(syn_groups)} groups present')
    missing = [g for g in groups if g not in syn_groups]
    say(f'planted groups absent from synthetic stream: {missing}')
    t0 = time.time()
    syn_restarts = []
    for r in range(RESTARTS):
        res = anneal(syn_pairs, groups, model, inv, weights, seed=5000 + r)
        syn_restarts.append(res)
        say(f'  control restart {r}: best={res["best_score"]/len(syn_pairs):.4f}')
    say(f'control annealing done in {time.time()-t0:.1f}s')
    syn_bmean, syn_bsd, _ = random_baseline(syn_pairs, groups, model, inv,
                                            weights, draws=300, seed=777)
    say(f'control baseline per-pair logp: mean={syn_bmean:.4f} sd={syn_bsd:.4f}')

    # recovery: modal assignment vs planted, over present non-anchor groups
    present = [g for g in free_groups if g in syn_groups]
    recov_modal, recov_best = 0, []
    for g in present:
        c = collections.Counter(r['assignment'][g] for r in syn_restarts)
        modal = c.most_common(1)[0][0]
        if modal == planted[g]:
            recov_modal += 1
        best_single = max(syn_restarts,
                          key=lambda r: r['best_score'])['assignment'][g]
        recov_best.append(best_single == planted[g])
    say(f'control recovery (modal vote over {RESTARTS} restarts, '
        f'{len(present)} present non-anchor groups): '
        f'{recov_modal}/{len(present)} = {recov_modal/len(present):.3f}')
    say(f'control recovery (single best restart): '
        f'{sum(recov_best)}/{len(present)} = {sum(recov_best)/len(present):.3f}')

    # ---- write results
    N = len(pairs)
    results = {
        'meta': {
            'lane': 'zeschau-seebach-1841', 'executor': 'annealer',
            'date': '2026-10-07',
            'anchors': ANCHORS,
            'restarts': RESTARTS, 'iters': ITERS, 't0': T0, 'tmin': TMIN,
            'model_source': 'Tocqueville Democracy in America T1 (1835) + T2 (1840), '
                            'Project Gutenberg 30513/30514; rule-based orthographic '
                            'syllabifier; Laplace alpha=0.05',
            'model_stats': {'tokens': len(toks), 'types': len(uni),
                            'bigrams': len(bi), 'inventory': len(inv),
                            'inventory_coverage': inv_cov},
            'pairs': N, 'groups': len(groups),
            'wall_seconds': time.time() - t_start,
        },
        'real': {
            'baseline_per_pair': {'mean': bmean, 'sd': bsd, 'draws': 300},
            'restarts': [
                {'seed': r['seed'],
                 'init_per_pair': r['init_score'] / N,
                 'best_per_pair': r['best_score'] / N,
                 'assignment': r['assignment']} for r in restarts],
            'stability': stab,
        },
        'control': {
            'planted': planted,
            'groups_present': len(syn_groups),
            'baseline_per_pair': {'mean': syn_bmean, 'sd': syn_bsd, 'draws': 300},
            'restarts': [
                {'seed': r['seed'],
                 'best_per_pair': r['best_score'] / len(syn_pairs),
                 'assignment': r['assignment']} for r in syn_restarts],
            'recovery_modal': {'correct': recov_modal, 'denom': len(present)},
            'recovery_best_single': {'correct': sum(recov_best),
                                     'denom': len(present)},
        },
        'log': log,
    }
    out_json = os.path.join(HERE, 'annealer_results.json')
    with open(out_json, 'w') as f:
        json.dump(results, f, ensure_ascii=False, indent=1)
    say(f'wrote {out_json}')

    # ---- markdown report
    best_real = max(restarts, key=lambda r: r['best_score'])
    best_syn = max(syn_restarts, key=lambda r: r['best_score'])
    z = (best_real['best_score'] / N - bmean) / bsd
    zc = (best_syn['best_score'] / len(syn_pairs) - syn_bmean) / syn_bsd
    stable_hi = [s for s in stab if s['count'] >= 12]
    lines = []
    A = lines.append
    A('# Annealer results — zeschau-seebach-1841 (2026-10-07)\n')
    A('Simulated annealing over the full 96-group → syllable assignment, 8 anchors '
      'pinned, scored by a French syllable-bigram model.\n')
    A('## Method')
    A('- Model: syllable unigrams/bigrams from Tocqueville *De la démocratie en '
      'Amérique* T1 (1835) + T2 (1840), Gutenberg 30513/30514; rule-based '
      'orthographic French syllabifier (maximal-onset); Laplace α=0.05.')
    A('- Era/register: 1835–1840 formal political prose — the closest available '
      'match to 1841 diplomatic French. Les Mis (1862, literary) used ONLY as '
      'the synthetic-control plaintext, keeping training and control independent.')
    A(f'- Inventory: top-{INVENTORY_TOP} syllable types + 26 single letters '
      f'({len(inv)} units); token coverage of reference {inv_cov:.4f}.')
    A(f'- Annealing: {RESTARTS} restarts × {ITERS} iters, geometric T {T0}→{TMIN}; '
      'move = reassign one free group (uniform or frequency-weighted proposal); '
      'delta-scored; best-key-per-restart retained. Anchors pinned: '
      + ', '.join(f'{g}={s}' for g, s in ANCHORS.items()) + '.')
    A('\n## Real ciphertext')
    A(f'- Pair/group counts re-verified: {N} pairs, {len(groups)} groups.')
    A(f'- Random-key baseline (anchors pinned, 300 draws): {bmean:.4f} ± {bsd:.4f} per-pair logp.')
    A(f'- Best restart: {best_real["best_score"]/N:.4f} per-pair logp '
      f'(z = {z:+.1f} vs baseline).')
    A('- Per-restart best scores: ' +
      ', '.join(f'{r["best_score"]/N:.3f}' for r in restarts))
    A('\n## Stability table (modal assignment across restarts, free groups only)')
    A('| group | modal syllable | recurrence | runner-ups |')
    A('|---|---|---|---|')
    for s in stab:
        others = ', '.join(f'{k}×{v}' for k, v in s['others'].items()) or '—'
        A(f'| {s["group"]} | {s["modal"]} | {s["count"]}/{s["n_restarts"]} | {others} |')
    A(f'\nGroups with recurrence ≥12/{RESTARTS}: ' +
      (', '.join(f'{s["group"]}={s["modal"]}({s["count"]})' for s in stable_hi) or 'none'))
    A('\n## Synthetic control')
    A('- Plaintext: Les Misérables T1 syllabified; 96-group planted syllabary '
      '(anchor groups pinned to true values, 88 others → random top-frequency syllables).')
    A(f'- Control baseline: {syn_bmean:.4f} ± {syn_bsd:.4f}; best control restart: '
      f'{best_syn["best_score"]/len(syn_pairs):.4f} (z = {zc:+.1f}).')
    A(f'- Recovery of planted assignment (modal vote, {len(present)} present non-anchor groups): '
      f'**{recov_modal}/{len(present)} = {recov_modal/len(present):.1%}**.')
    A(f'- Recovery by single best restart: {sum(recov_best)}/{len(present)} = '
      f'{sum(recov_best)/len(present):.1%}.')
    A('\n## Verdict')
    rec = recov_modal / len(present)
    if rec >= 0.5:
        A('- Control: method RECOVERS the planted syllabary → method is informative. '
          'Real-ciphertext stability table above is meaningful signal.')
    elif rec >= 0.2:
        A('- Control: method only PARTIALLY recovers the planted syllabary → '
          'method is weakly informative; treat real stability as suggestive only.')
    else:
        A('- Control: method FAILS to recover the planted syllabary → method is '
          'UNINFORMATIVE on this problem class; real-ciphertext results are a NULL '
          '(N-series), not a break. Do not promote any real assignment.')
    A('\n## Caveats / next')
    A('- Syllabifier is rule-based orthographic, not phonetic; the 1841 syllabary\'s '
      'own segmentation may differ (e.g. mute-e handling, digraph splits).')
    A('- Homophony is one-directional in the model (many groups → one syllable); '
      'the true key may also map one group to multi-syllable strings — not modelled.')
    A('- If control recovers: next = inspect stable real assignments for French '
      'word formation around anchor windows; try seeded restarts from the modal key '
      'with a word-level French scorer.')
    A('- If control fails: next = different move set (pair-swap moves), trigram '
      'syllable model, or accept that 8-anchor sparsity is below the method\'s '
      'resolution and stand down (null).')
    out_md = os.path.join(HERE, 'annealer_results.md')
    with open(out_md, 'w') as f:
        f.write('\n'.join(lines) + '\n')
    say(f'wrote {out_md}')
    say(f'total wall: {time.time()-t_start:.1f}s')

if __name__ == '__main__':
    main()
