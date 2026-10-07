#!/usr/bin/env python3
"""GEOMETER WO3 — simulate the clerk (generative verification).

Pre-registered in code/side-rotation/prereg_geometer.md BEFORE running
(incl. the calibration amendment: match criteria apply to DERIVED-PHASE
measurements — the lane's Jaccard-k12 pipeline run on each simulated group
stream — since the observed 366.3/+5.6 are post-clustering quantities).

Toy 3-column printed table (~90 groups), era French syllable stream
(Tocqueville t1), 6 pre-registered clerk behaviors, 20 replicates each,
T=1847 per stream. Per replicate:
  true-column diagnostics: M1/M2/M3 on true columns
  derived-phase: Jaccard-k12 phases -> M1 (chi2 3x3 ABC), M2 (lag-3 z,
  E1-exact ABC-bounded), M3 (self-transition suppression), ARI(derived,true)
Match: median over replicates of DERIVED M1>=200 AND M2 z>=+3.0 AND M3<0.8,
  plus median ARI>=0.5.
Writes wo3.json.
"""
import json, os, sys, math, random, re, collections

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))

T_STREAM = 1847
N_REP = 20

# ---------------- text ----------------
def load_text():
    p = os.path.join(LANE, 'data', 'gutenberg-30513-tocqueville-t1.txt')
    t = open(p, encoding='utf-8').read()
    m = re.search(r'\*\*\* START OF.*?\*\*\*', t, re.S)
    m2 = re.search(r'\*\*\* END OF.*?\*\*\*', t, re.S)
    if m and m2:
        t = t[m.end():m2.start()]
    return t.lower()

VOW = set('aeiouyàâäéèêëîïôöùûü')

def syllabify(word):
    if not word:
        return []
    spans = []
    i = 0
    n = len(word)
    while i < n:
        if word[i] in VOW:
            j = i
            while j < n and word[j] in VOW:
                j += 1
            spans.append((i, j))
            i = j
        else:
            i += 1
    if not spans:
        return [word]
    bounds = [0]
    prev_end = 0
    for k, (s, e) in enumerate(spans):
        if k > 0:
            gaplen = s - prev_end
            bounds.append(prev_end if gaplen <= 1 else prev_end + 1)
        prev_end = e
    bounds.append(n)
    return [word[a:b] for a, b in zip(bounds, bounds[1:]) if b > a]

# ---------------- table ----------------
def build_table(rng, freq):
    top = [s for s, _ in freq.most_common(45)]
    table = {}
    var_of = collections.defaultdict(list)
    gid = 0
    for rank, s in enumerate(top):
        nvar = 3 if rank < 15 else (2 if rank < 30 else 1)
        cols = rng.sample([0, 1, 2], nvar)
        for c in cols:
            g = 'G%02d' % gid
            gid += 1
            table[g] = (s, c)
            var_of[s].append((g, c))
    bycol = collections.defaultdict(list)
    for g, (s, c) in table.items():
        bycol[c].append(g)
    nrows = max(len(bycol[c]) for c in (0, 1, 2))
    cell = {}
    for c in (0, 1, 2):
        for r, g in enumerate(bycol[c]):
            cell[(r, c)] = g
    return table, var_of, cell, nrows

def encipher(stream_sylls, table, var_of, cell, nrows, behavior, rng):
    cols_out, gids_out = [], []
    counters = collections.defaultdict(int)
    c_prev = rng.randrange(3)
    c_prev2 = rng.randrange(3)
    hand = 1
    scan = 0
    ncell = nrows * 3
    gid_at = {}
    for (r, c), g in cell.items():
        gid_at[r * 3 + c] = g
    for s in stream_sylls:
        variants = var_of.get(s)
        if not variants:
            continue
        vcols = {c: g for g, c in variants}
        if behavior == 'B0':
            g, c = rng.choice(variants)
        elif behavior == 'B1':
            vs = sorted(variants, key=lambda x: x[1])
            g, c = vs[counters[s] % len(vs)]
            counters[s] += 1
        elif behavior == 'B2':
            r = rng.random()
            c = c_prev if r < 0.18 else ((c_prev + 1) % 3 if r < 0.74 else (c_prev + 2) % 3)
            c_prev = c
            g = vcols.get(c)
            if g is None:
                for d in (1, 2):
                    for cc in ((c + d) % 3, (c - d) % 3):
                        if cc in vcols:
                            g, c = vcols[cc], cc
                            break
                    if g:
                        break
        elif behavior == 'B3':
            beta, gamma = 2.0, 0.7
            w = [math.exp(-beta * ((c == c_prev) + gamma * (c == c_prev2))) for c in (0, 1, 2)]
            tot = sum(w)
            r = rng.random() * tot
            c = 2
            acc = 0.0
            for cc in (0, 1, 2):
                acc += w[cc]
                if r <= acc:
                    c = cc
                    break
            c_prev2, c_prev = c_prev, c
            g = vcols.get(c)
            if g is None:
                for d in (1, 2):
                    for cc in ((c + d) % 3, (c - d) % 3):
                        if cc in vcols:
                            g, c = vcols[cc], cc
                            break
                    if g:
                        break
        elif behavior == 'B4':
            need = set(g for g, _ in variants)
            g = None
            for k in range(ncell):
                pos = (scan + k) % ncell
                gg = gid_at.get(pos)
                if gg in need:
                    g = gg
                    scan = (pos + 1) % ncell
                    break
            assert g is not None, 'B4 scan failed to find variant'
            c = table[g][1]
        elif behavior == 'B5':
            r = rng.random()
            hand = hand if r < 0.5 else ((hand + 1) % 3 if r < 0.75 else (hand + 2) % 3)
            d0 = min(min(abs(cc - hand), 3 - abs(cc - hand)) for cc in vcols)
            tied = [cc for cc in vcols if min(abs(cc - hand), 3 - abs(cc - hand)) == d0]
            c = rng.choice(tied)
            g = vcols[c]
        cols_out.append(c)
        gids_out.append(g)
    return cols_out, gids_out

# ---------------- lane instrument copies (from rotation_mystery.py) ----------------
def derive_phases(stream, k_cut=12):
    groups = sorted(set(stream))
    foll = collections.defaultdict(collections.Counter)
    pred = collections.defaultdict(collections.Counter)
    for a, b in zip(stream, stream[1:]):
        foll[a][b] += 1
        pred[b][a] += 1
    K = 10
    TOP = {g: (set(h for h, _ in foll[g].most_common(K)) |
               set(h for h, _ in pred[g].most_common(K))) for g in groups}

    def jac(a, b):
        sa, sb = TOP[a], TOP[b]
        u = sa | sb
        return len(sa & sb) / len(u) if u else 0.0

    clusters = [{g} for g in groups]
    merges = []
    while len(clusters) > 1:
        best, bi, bj = -1.0, None, None
        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                c1, c2 = clusters[i], clusters[j]
                s = sum(jac(a, b) for a in c1 for b in c2) / (len(c1) * len(c2))
                if s > best:
                    best, bi, bj = s, i, j
        merges.append((sorted(clusters[bi]), sorted(clusters[bj])))
        new = clusters[bi] | clusters[bj]
        clusters = [c for k, c in enumerate(clusters) if k not in (bi, bj)] + [new]
    cs = [{g} for g in groups]
    for c1l, c2l in merges:
        if len(cs) <= k_cut:
            break
        c1, c2 = set(c1l), set(c2l)
        cs = [c for c in cs if c != c1 and c != c2] + [c1 | c2]
    cs = sorted(cs, key=len, reverse=True)
    block = {}
    for x, lbl in ((cs[0], 'A'), (cs[1], 'B'), (cs[2], 'C')):
        for g in x:
            block[g] = lbl
    for c in cs[3:]:
        for g in c:
            block[g] = 'R'
    return block

def derived_measures(gid_stream, block):
    """M1/M2/M3 on derived phases, E1-exact ABC-bounded method."""
    lab = [block[g] for g in gid_stream]
    n = len(lab)
    states = 'ABC'
    cnt = collections.Counter()
    row = collections.Counter()
    for a, b in zip(lab, lab[1:]):
        if a in states and b in states:
            cnt[(a, b)] += 1
            row[a] += 1
    nT = sum(cnt.values())
    colm = collections.Counter()
    for (a, b), c in cnt.items():
        colm[b] += c
    x2 = sum((cnt[(a, b)] - row[a] * colm[b] / nT) ** 2 / (row[a] * colm[b] / nT)
             for a in states for b in states if row[a] and colm[b])
    pi = {s: row[s] / nT for s in states}
    Pm = {s: {t: cnt[(s, t)] / row[s] if row[s] else 0.0 for t in states} for s in states}

    def mm(M1, M2):
        return {s: {t: sum(M1[s][u] * M2[u][t] for u in states) for t in states} for s in states}

    Pk = {s: {t: (1.0 if s == t else 0.0) for t in states} for s in states}
    for _ in range(3):
        Pk = mm(Pk, Pm)
    exp = sum(pi[s] * Pk[s][s] for s in states)
    idx = [i for i in range(n - 3) if lab[i] in states and lab[i + 3] in states]
    obs = sum(1 for i in idx if lab[i] == lab[i + 3]) / len(idx)
    se = math.sqrt(exp * (1 - exp) / len(idx))
    z = (obs - exp) / se if se else 0.0
    psame = sum(cnt[(s, s)] for s in states) / nT
    m3 = psame / sum(pi[s] ** 2 for s in states)
    return {'M1': x2, 'M2_z': z, 'M2_obs': obs, 'M2_exp': exp, 'M3': m3,
            'nT': nT, 'sizes': {s: sum(1 for g, l in block.items() if l == s) for s in 'ABCR'}}

def ari(labels_true, labels_pred):
    """Adjusted Rand index."""
    n = len(labels_true)
    ct = collections.Counter(zip(labels_true, labels_pred))
    sum_comb = sum(v * (v - 1) / 2 for v in ct.values())
    row = collections.Counter(labels_true)
    col = collections.Counter(labels_pred)
    sr = sum(v * (v - 1) / 2 for v in row.values())
    sc = sum(v * (v - 1) / 2 for v in col.values())
    nc = n * (n - 1) / 2
    expected = sr * sc / nc
    maxv = (sr + sc) / 2
    return (sum_comb - expected) / (maxv - expected) if maxv != expected else 0.0

def true_measures(colstream):
    n = len(colstream)
    states = (0, 1, 2)
    cnt = collections.Counter(zip(colstream, colstream[1:]))
    row = collections.Counter(colstream[:-1])
    colm = collections.Counter(colstream[1:])
    nT = n - 1
    x2 = sum((cnt[(a, b)] - row[a] * colm[b] / nT) ** 2 / (row[a] * colm[b] / nT)
             for a in states for b in states if row[a] and colm[b])
    pi = {s: row[s] / nT for s in states}
    Pm = {s: {t: cnt[(s, t)] / row[s] if row[s] else 0.0 for t in states} for s in states}

    def mm(M1, M2):
        return {s: {t: sum(M1[s][u] * M2[u][t] for u in states) for t in states} for s in states}

    Pk = {s: {t: (1.0 if s == t else 0.0) for t in states} for s in states}
    for _ in range(3):
        Pk = mm(Pk, Pm)
    exp = sum(pi[s] * Pk[s][s] for s in states)
    obs = sum(1 for i in range(n - 3) if colstream[i] == colstream[i + 3]) / (n - 3)
    se = math.sqrt(exp * (1 - exp) / (n - 3))
    z = (obs - exp) / se if se else 0.0
    psame = sum(1 for a, b in zip(colstream, colstream[1:]) if a == b) / nT
    m3 = psame / sum(pi[s] ** 2 for s in states)
    return {'M1': x2, 'M2_z': z, 'M3': m3}

def main():
    OUT = {}
    text = load_text()
    words = re.findall(r"[a-zàâäéèêëîïôöùûüç']+", text)
    words = [w for w in words if w.strip("'")]
    sylls = []
    for w in words:
        sylls.extend(syllabify(w.strip("'")))
    freq = collections.Counter(sylls)
    OUT['text_stats'] = {'words': len(words), 'syll_tokens': len(sylls),
                         'distinct_sylls': len(freq),
                         'top': freq.most_common(8)}
    print('text: words=%d syll_tokens=%d distinct=%d' % (len(words), len(sylls), len(freq)))

    BEHAVIORS = ['B0', 'B1', 'B2', 'B3', 'B4', 'B5']
    summary = {}
    for b in BEHAVIORS:
        drep, trep, arep = [], [], []
        for rep in range(N_REP):
            rng = random.Random(1000 + {'B0':0,'B1':1,'B2':2,'B3':3,'B4':4,'B5':5}[b] * 100 + rep)
            table, var_of, cell, nrows = build_table(rng, freq)
            start = rng.randrange(0, max(1, len(sylls) - T_STREAM - 1))
            syl_stream = sylls[start:start + T_STREAM]
            cols_out, gids_out = encipher(syl_stream, table, var_of, cell, nrows, b, rng)
            tm = true_measures(cols_out)
            trep.append(tm)
            block = derive_phases(gids_out)
            dm = derived_measures(gids_out, block)
            drep.append(dm)
            true_lab = [table[g][1] for g in table]
            # ARI over groups present in stream
            gs = sorted(set(gids_out))
            arep.append(ari([table[g][1] for g in gs], [block[g] for g in gs]))
            if rep == 0:
                print('  %s rep0: true M1=%.1f z=%.2f M3=%.3f | derived M1=%.1f z=%.2f M3=%.3f ARI=%.2f sizes=%s'
                      % (b, tm['M1'], tm['M2_z'], tm['M3'], dm['M1'], dm['M2_z'], dm['M3'],
                         arep[-1], dm['sizes']))
        med = lambda rs, k: sorted(r[k] for r in rs)[N_REP // 2]
        med_ari = sorted(arep)[N_REP // 2]
        summary[b] = {
            'true_med': {'M1': round(med(trep, 'M1'), 1), 'M2_z': round(med(trep, 'M2_z'), 2),
                         'M3': round(med(trep, 'M3'), 3)},
            'derived_med': {'M1': round(med(drep, 'M1'), 1), 'M2_z': round(med(drep, 'M2_z'), 2),
                            'M3': round(med(drep, 'M3'), 3), 'ARI': round(med_ari, 3)},
            'passes': bool(med(drep, 'M1') >= 200 and med(drep, 'M2_z') >= 3.0
                           and med(drep, 'M3') < 0.8 and med_ari >= 0.5),
        }
        s = summary[b]
        print('%s: derived med M1=%.1f z=%.2f M3=%.3f ARI=%.3f -> %s' %
              (b, s['derived_med']['M1'], s['derived_med']['M2_z'], s['derived_med']['M3'],
               s['derived_med']['ARI'], 'REACHES' if s['passes'] else 'fails'))
    OUT['summary'] = summary
    json.dump(OUT, open(os.path.join(HERE, 'wo3.json'), 'w'), indent=1)
    print('done')

if __name__ == '__main__':
    main()
