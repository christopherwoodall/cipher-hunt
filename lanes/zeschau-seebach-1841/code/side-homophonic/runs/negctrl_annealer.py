#!/usr/bin/env python3
"""Negative control (Runner): dead round-1 annealer on the 6 synthetic instances.

Reuses code/crowd/anneal.py's anneal() + bigram model unchanged, except the
pin set is monkey-patched to the 7 TRUE synthetic anchors from the crib file
(the annealer's own 8th pin 87=ce is NOT a synthetic anchor and would be a
false pin). Truth is loaded only at scoring time; anneal() never sees it.

Expectation (CONTROL-DESIGN.md §8): ≈chance (chance primary ≈ 0.021).
If the dead annealer beats chance here, the control is miscalibrated — flag.
"""
import sys, os, json, time, collections, random

LANE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                     '..', '..', '..'))
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd'))
import anneal as A  # noqa: E402

SH = os.path.join(LANE, 'code', 'side-homophonic')
INST = os.path.join(SH, 'control', 'instances')
DATA = os.path.join(LANE, 'data')
OUT = os.path.join(SH, 'runs', 'negative-control')
os.makedirs(OUT, exist_ok=True)

SEEDS = [184101, 184102, 184103, 184104, 184105, 184106]
RESTARTS = 12
ITERS = 60000

log = open(os.path.join(OUT, 'negctrl.log'), 'w')


def say(m):
    log.write(m + '\n'); log.flush(); print(m, flush=True)


def load_ct(path):
    pairs = []
    for l in open(path):
        if l.startswith('#') or not l.strip():
            continue
        pairs += l.split()
    return pairs


def strip_comment_lines(path):
    txt = open(path).read()
    return json.loads('\n'.join(l for l in txt.splitlines()
                                if not l.lstrip().startswith('//')))


def main():
    t_start = time.time()
    say('[negctrl] building Tocqueville syllable-bigram model (shared) ...')
    t0 = time.time()
    toks, uni, bi = A.build_model([
        os.path.join(DATA, 'gutenberg-30513-tocqueville-t1.txt'),
        os.path.join(DATA, 'gutenberg-30514-tocqueville-t2.txt')])
    model = A.BigramModel(uni, bi)
    inv, weights = A.make_inventory(uni)
    say(f'[negctrl] model built in {time.time()-t0:.1f}s, inventory={len(inv)}')
    inv_set = set(inv)

    results = []
    for seed in SEEDS:
        say(f'[negctrl] ---- seed {seed} ----')
        pairs = load_ct(os.path.join(INST, f'SYNTHETIC-ct-{seed}.pairs.txt'))
        groups = sorted(set(pairs))
        crib = json.load(open(os.path.join(INST, f'SYNTHETIC-crib-{seed}.json')))
        anchors = crib['anchors']
        assert len(anchors) == 7 and len(pairs) == 1846 and len(groups) == 96
        # truth-free section: pin only the 7 true anchors
        A.ANCHORS = dict(anchors)
        t0 = time.time()
        restarts = []
        for r in range(RESTARTS):
            res = A.anneal(pairs, groups, model, inv, weights,
                           seed=9000 + r, iters=ITERS)
            restarts.append(res)
        say(f'[negctrl]   {RESTARTS} restarts x {ITERS} in {time.time()-t0:.1f}s')
        # modal assignment (as round-1 did)
        free = [g for g in groups if g not in anchors]
        modal = {}
        for g in free:
            c = collections.Counter(r['assignment'][g] for r in restarts)
            modal[g] = c.most_common(1)[0][0]
        # ---- scoring only now: unseal the key ----
        truth = strip_comment_lines(
            os.path.join(INST, f'SYNTHETIC-key-{seed}.json'))
        key = truth['key']
        nonpin = [g for g in key if g not in anchors]
        in_inv = [g for g in nonpin if key[g]['primary'] in inv_set]
        hits = sum(1 for g in nonpin if modal.get(g) == key[g]['primary'])
        hits_inv = sum(1 for g in in_inv if modal.get(g) == key[g]['primary'])
        primary = hits / len(nonpin)
        primary_inv = hits_inv / len(in_inv) if in_inv else 0.0
        chance = json.load(open(os.path.join(SH, 'control', 'chance_baseline.json'))
                           )[str(seed)]['primary']['mean']
        results.append({'seed': seed, 'restarts': RESTARTS, 'iters': ITERS,
                        'n_nonpin': len(nonpin), 'hits': hits,
                        'primary': round(primary, 4),
                        'primary_in_inventory': round(primary_inv, 4),
                        'n_truth_primary_in_inventory': len(in_inv),
                        'chance_mean': round(chance, 4)})
        say(f'[negctrl]   seed {seed}: primary {hits}/{len(nonpin)} = {primary:.4f} '
            f'(chance {chance:.4f}); truth-primary-in-inventory {hits_inv}/{len(in_inv)} = {primary_inv:.4f}')
        # restore module anchors for hygiene
        A.ANCHORS = {'11': 'la', '70': 'pre', '82': 'm', '34': 'i',
                     '29': 'er', '40': 'e', '46': 'que', '87': 'ce'}

    mean_primary = sum(r['primary'] for r in results) / len(results)
    max_primary = max(r['primary'] for r in results)
    verdict = 'NEGATIVE-CONTROL-OK (≈chance)' if max_primary < 0.10 \
        else 'MISCALIBRATED — DEAD ANNEALER BEATS CHANCE'
    out = {'wall_seconds': round(time.time() - t_start, 1),
           'restarts': RESTARTS, 'iters': ITERS,
           'mean_primary': round(mean_primary, 4),
           'max_primary': round(max_primary, 4),
           'verdict': verdict, 'per_seed': results}
    json.dump(out, open(os.path.join(OUT, 'negctrl_results.json'), 'w'), indent=1)
    say(f'[negctrl] mean_primary={mean_primary:.4f} max={max_primary:.4f}')
    say(f'[negctrl] VERDICT: {verdict}')
    say(f'[negctrl] wall {time.time()-t_start:.1f}s')
    log.close()


if __name__ == '__main__':
    main()
