#!/usr/bin/env python3
"""Same-phase-dealing simulator: validates the within-phase similarity
instrument's POWER and false-positive rate.

Model: C cells, each with 1-3 aliases; each cell has a HOME phase. Occurrence
phases follow a diluted 3-cycle (q=0.6). When a cell occurs at its home phase,
emit a uniform-random alias (free variation = classical homophony); at other
phases emit the home-phase alias anyway with prob `leak` (encipherer noise),
else resample (rare). Cell sequence from a random bigram model.

Then run the within_phase2 pipeline: true alias pairs should rank at top
(power); fraction of non-alias pairs at z>2.8 = false-positive rate.
"""
import json, math, random, sys
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

sys.path.insert(0, '/home/hatch/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/crowd7/keystruct')
from within_phase2 import jac, cos_raw, topk  # noqa: E402

OUT = Path('/home/hatch/workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/crowd7/keystruct')


def simulate(seed=7, n_cells=40, n_tokens=4000, q=0.6, leak=0.15):
    rng = random.Random(seed)
    phases = ['A', 'B', 'C']
    nxt = {'A': 'B', 'B': 'C', 'C': 'A'}
    cells = list(range(n_cells))
    # aliases per cell: 60% 1 alias, 30% 2, 10% 3
    aliases = {}
    g = 0
    home = {}
    for c in cells:
        k = 1 if rng.random() < 0.6 else (2 if rng.random() < 0.75 else 3)
        aliases[c] = list(range(g, g + k)); g += k
        home[c] = rng.choice(phases)
    # cell bigram model
    trans = {c: [rng.random() for _ in cells] for c in cells}
    # occurrence phases: diluted cycle
    pclasses = []
    p = rng.choice(phases)
    for _ in range(n_tokens):
        pclasses.append(p)
        p = nxt[p] if rng.random() < q else rng.choice(phases)
    # cell sequence
    seq = [rng.choice(cells)]
    for _ in range(n_tokens - 1):
        w = trans[seq[-1]]
        seq.append(rng.choices(cells, weights=w)[0])
    # emit
    pairs = []
    for c, ph in zip(seq, pclasses):
        al = aliases[c]
        if ph == home[c] or rng.random() < leak:
            pairs.append(rng.choice(al))
        else:
            # out-of-home occurrence: encipherer still uses a home alias (leak) w.p. leak else random alias of cell
            pairs.append(rng.choice(al))
    truth = {}  # frozenset pair -> True alias
    for c, al in aliases.items():
        for i in range(len(al)):
            for j in range(i + 1, len(al)):
                truth[(al[i], al[j])] = c
    return pairs, truth, home, aliases


def run_one(pairs, truth, minn=12, K=10):
    # phase labels: use TRUE home phases mapped to groups? No -- replicate the
    # instrument: Jaccard clustering. Cheaper: assign group phase = home phase
    # of its cell (oracle labels) AND also test with noisy labels (flip 30%).
    # Here we test the similarity metric itself, so oracle labels are fine;
    # label noise is a separate (flagged) issue.
    raise NotImplementedError


def main(minn=12):
    import within_phase2 as wp
    rows = []
    for seed in (7, 8, 9):
        pairs, truth, home, aliases = simulate(seed)
        # oracle group->phase from home
        gphase = {}
        for c, al in aliases.items():
            for a in al:
                gphase[a] = home[c]
        groups = sorted(set(pairs))
        # contact profiles
        succ = defaultdict(Counter); pred = defaultdict(Counter)
        for a, b in zip(pairs[:-1], pairs[1:]):
            succ[a][b] += 1; pred[b][a] += 1
        freq = Counter(pairs)
        by_phase = defaultdict(list)
        for gg in groups:
            by_phase[gphase[gg]].append(gg)
        for ph, gs in by_phase.items():
            gs_n = [x for x in gs if freq[x] >= minn]
            sims = []
            for a, b in combinations(sorted(gs), 2):
                key = tuple(sorted((a, b)))
                js = jac(topk(succ[a]) | topk(pred[a]), topk(succ[b]) | topk(pred[b]))
                sims.append((key, js, key in truth))
            null = [js for key, js, t in sims]
            mu = sum(null) / len(null)
            sd = math.sqrt(sum((v - mu) ** 2 for v in null) / len(null))
            tp = fp = 0; ntrue = sum(1 for _, _, t in sims if t)
            top_true_ranks = []
            sims.sort(key=lambda t: -t[1])
            for rank, (key, js, t) in enumerate(sims):
                z = (js - mu) / sd if sd else 0
                if t:
                    top_true_ranks.append((rank, round(z, 2)))
                if z > 2.8:
                    if t:
                        tp += 1
                    else:
                        fp += 1
            rows.append({'seed': seed, 'phase': ph, 'n_true': ntrue,
                         'true_ranks_z': top_true_ranks,
                         'tp@z2.8': tp, 'fp@z2.8': fp,
                         'fp_rate': round(fp / max(1, len(sims) - ntrue), 4)})
    json.dump(rows, open(OUT / 'samephase_power.json', 'w'), indent=1)
    for r in rows:
        print(f"seed={r['seed']} phase={r['phase']} n_true={r['n_true']} "
              f"true_ranks(z)={r['true_ranks_z'][:8]} tp@2.8={r['tp@z2.8']} "
              f"fp@2.8={r['fp@z2.8']} fp_rate={r['fp_rate']}")


if __name__ == '__main__':
    main()
