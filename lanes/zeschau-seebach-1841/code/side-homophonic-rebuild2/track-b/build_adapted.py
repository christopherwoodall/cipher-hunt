#!/usr/bin/env python3
"""Track B step 7: build the ADAPTED salad (T1 threat model).

Constrained local search under the CURRENT objective (verifier's J):
  - values from the 296-item rebuilt crib inventory
  - projected forms NOT in the 3,546-word lm_ref lexicon (byte-exact check)
  - all-distinct projected values (89 free groups + 7 pins)
  - n_poly = 0, pins fixed
Then: verification checklist, strawman check
(J_current(adapted) >= -2552.3, i.e. within ~200 nats of frozen -2352.3),
freeze to adapted_salad.json.

Deterministic: fixed move ordering, no RNG. NO R5005 contact.
"""
import collections
import hashlib
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
REBUILD = os.path.join(LANE, 'code', 'side-homophonic-rebuild')

sys.path.insert(0, os.path.join(REBUILD, 'solver'))
sys.path.insert(0, os.path.join(REBUILD, 'verifier'))
from solver import load_inventory          # noqa: E402
from rescore import (Rescorer, project, load_pairs,  # noqa: E402
                     load_anchors)

SEED = '184101'
MAX_EVALS = 4000
MAX_WALL_S = 45 * 60
STRAWMAN_FLOOR = -2552.3  # frozen salad -2352.3 minus ~200 nats


def main():
    t0 = time.time()
    pairs = load_pairs(SEED)
    cfg = json.load(open(os.path.join(REBUILD, 'solver', 'config.json')))
    pilot = json.load(open(os.path.join(
        REBUILD, 'pilot', 'rebuild-pilot-final', 'result.json')))
    pins = pilot['meta']['pins']
    lm_data = json.load(open(os.path.join(REBUILD, 'solver', 'lm_ref', 'lm.json')))
    lex_wt = {e['w']: e['wt'] for e in lm_data['lexicon']}
    lexset = set(lex_wt)

    # ---- 1. inventory + pool ----
    inv, _ = load_inventory('crib', pins, {}, lex_wt)
    assert len(inv) == 296, f'inventory size {len(inv)} != 296'
    pin_forms = {project(v) for v in pins.values()}
    pool = {}  # projected form -> raw item (first wins)
    for v in inv:
        p = project(v)
        if not p or p in lexset or p in pin_forms or p in pool:
            continue
        pool[p] = v
    pool_forms = sorted(pool)  # fixed order
    print(f'[pool] inventory=296 distinct non-lexicon non-pin forms={len(pool_forms)}',
          flush=True)
    assert len(pool_forms) >= 89

    r = Rescorer(pairs, cfg)
    groups = r.groups
    free = sorted(g for g in groups if g not in pins)
    assert len(free) == 89, len(free)
    occ = {g: len(r.occ[g]) for g in free}

    def J_of(assign):
        """assign: dict group->raw value (all 96 groups). Returns verifier total."""
        v1 = dict(assign)
        v2 = {g: None for g in groups}
        return r.score(v1, v2, {}, label='adapted')['total']

    # ---- 2. greedy init ----
    rates = sorted(pool_forms,
                   key=lambda p: r.lm.F('^', p) / len(p), reverse=True)
    v1 = dict(pins)
    for g, p in zip(sorted(free, key=lambda g: -occ[g]), rates):
        v1[g] = pool[p]
    cur = J_of(v1)
    evals = 1
    print(f'[init] J={cur:.1f} evals={evals}', flush=True)

    # ---- 3. first-improvement local search (fixed order, no RNG) ----
    used = {project(v1[g]) for g in free}
    improved = True
    while improved and evals < MAX_EVALS and time.time() - t0 < MAX_WALL_S:
        improved = False
        for g in free:  # fixed group order
            if evals >= MAX_EVALS or time.time() - t0 >= MAX_WALL_S:
                break
            cur_form = project(v1[g])
            for p in pool_forms:  # fixed candidate order
                if p == cur_form or p in used:
                    continue
                old_raw = v1[g]
                v1[g] = pool[p]
                j = J_of(v1)
                evals += 1
                if j > cur + 1e-9:
                    cur = j
                    used.discard(cur_form)
                    used.add(p)
                    improved = True
                    break
                v1[g] = old_raw
        # pairwise swaps
        if not improved:
            for ii in range(len(free)):
                for jj in range(ii + 1, len(free)):
                    if evals >= MAX_EVALS or time.time() - t0 >= MAX_WALL_S:
                        break
                    gi, gj = free[ii], free[jj]
                    v1[gi], v1[gj] = v1[gj], v1[gi]
                    j = J_of(v1)
                    evals += 1
                    if j > cur + 1e-9:
                        cur = j
                        improved = True
                        break
                    v1[gi], v1[gj] = v1[gj], v1[gi]
                if improved or evals >= MAX_EVALS:
                    break
        print(f'[search] J={cur:.1f} evals={evals} wall={time.time()-t0:.0f}s',
              flush=True)

    # ---- 4. final full rescore with parts ----
    v2 = {g: None for g in groups}
    res = r.score(dict(v1), v2, {}, label='adapted-final', verbose=True)
    J = res['total']

    # ---- 5. verification checklist ----
    forms = [project(v1[g]) for g in free]
    checks = {
        'all_values_in_inventory': all(v1[g] in inv for g in free),
        'all_projected_nonlexicon': all(f not in lexset for f in forms),
        'all_distinct_free': len(set(forms)) == 89,
        'distinct_from_pins': not (set(forms) & pin_forms),
        'n_poly_zero': all(v2[g] is None for g in groups),
        'pins_unchanged': all(v1[g] == pins[g] for g in pins),
        'n_groups': len(v1) == 96,
    }
    print('[checks]', json.dumps(checks), flush=True)
    assert all(checks.values()), f'VERIFICATION FAILED: {checks}'

    # ---- 6. strawman check ----
    strawman = J < STRAWMAN_FLOOR
    print(f'[strawman] J_current(adapted)={J:.1f} vs frozen -2352.3; '
          f'floor={STRAWMAN_FLOOR} -> {"STRAWMAN (VOID (b))" if strawman else "credible adversary"}',
          flush=True)

    blob = {'seed': SEED, 'v1': v1,
            'projected_forms': {g: project(v1[g]) for g in groups},
            'J_current': J,
            'parts': {k: res[k] for k in
                      ('S_char', 'S_cov', 'S_single', 'S_word', 'S_potts',
                       'S_conc', 'n_poly', 'total')},
            'checks': checks, 'strawman': strawman,
            'search': {'evals': evals, 'wall_s': round(time.time() - t0, 1)},
            'decode_sha256': hashlib.sha256(
                res['decode'].encode()).hexdigest()}
    json.dump(blob, open(os.path.join(HERE, 'adapted_salad.json'), 'w'), indent=1)
    print('[done] adapted_salad.json written', flush=True)


if __name__ == '__main__':
    main()
