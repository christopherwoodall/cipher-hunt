#!/usr/bin/env python3
"""Metrologist task 1: band check for the FRESH rebuild-control instances.

R7 FIX (2026-10-07): the original version of this tool used the per-GROUP
label phase (key[g]['phase'], the round-robin alias deal) — the WRONG
quantity (it reads 1-13, not the calibrated rotation). The calibrated
quantity per CONTROL-DESIGN.md section 3 is the OCCURRENCE-phase chi2:
  occurrence_chi2(inst['pclasses'])
where pclasses is the per-position diluted-cycle phase sequence. pclasses
is not persisted in the instance files, so this tool re-derives it by
deterministic rebuild: the generator is seeded and deterministic, so
re-running build_instance with the CERTIFIED params (q_cycle=0.5, T=56)
reproduces pclasses exactly. The check then compares the recomputed chi2
against the meta file's reported value (persistence/determinism check)
and against the pre-registered band [181, 320].

Usage: python3 band_check.py [seed ...]  (default: the 6 fresh seeds)
Exit 0 if all in-band and all recomputed==reported; 2 otherwise.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REBUILD_CTL = os.path.normpath(os.path.join(HERE, '..', 'control'))
INST = os.path.join(REBUILD_CTL, 'instances')
sys.path.insert(0, REBUILD_CTL)
import generator as g  # noqa: E402  (rebuild control's generator)

BAND = (181.0, 320.0)
CRIB6 = ['11', '70', '82', '34', '29', '40']
DEFAULT_SEEDS = [184201, 184202, 184203, 184204, 184207, 184206]  # 2026-10-07: 184205->184207 swap per adjudication
Q_CERTIFIED = 0.5
T_CERTIFIED = 56


def load_pairs(path):
    pairs = []
    for line in open(path):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        pairs.extend(line.split())
    return pairs


def main():
    seeds = [int(s) for s in sys.argv[1:]] or DEFAULT_SEEDS
    lo, hi = BAND
    tokens = g.load_lesmis_tokens()
    group_labels = g.real_group_labels()
    rows = []
    for seed in seeds:
        # deterministic re-derivation of the per-occurrence phase sequence
        p = dict(g.PARAMS)
        p['q_cycle'] = Q_CERTIFIED  # certified value, NOT raw PARAMS default
        if seed not in p['seeds']:
            # replacement/extra seed: put it at the vacated slice slot
            # (index determines the plaintext slice; see FINDINGS.md)
            p['seeds'] = [184201, 184202, 184203, 184204, seed, 184206]
        inst = g.build_instance(seed, tokens, group_labels, p, T_CERTIFIED)
        chi2_recomputed = g.occurrence_chi2(inst['pclasses'])

        meta = json.load(open(os.path.join(
            INST, f'SYNTHETIC-meta-{seed}.json')))
        chi2_reported = meta['occurrence_chi2']
        pairs = load_pairs(os.path.join(INST, f'SYNTHETIC-ct-{seed}.pairs.txt'))
        hits = [i for i in range(len(pairs) - 5)
                if pairs[i:i + 6] == CRIB6]
        in_band = lo <= chi2_recomputed <= hi
        match = chi2_recomputed == chi2_reported
        struct_ok = (len(pairs) == 1846 and len(set(pairs)) == 96
                     and len(hits) == 1)
        rows.append({
            'seed': seed,
            'occ_chi2_reported': chi2_reported,
            'occ_chi2_recomputed': chi2_recomputed,
            'recomputed_matches_reported': bool(match),
            'in_band': bool(in_band),
            'structural_ok': bool(struct_ok),
        })
        flag = 'INBAND' if in_band else '*** OUT-OF-BAND ***'
        print(f"{seed}: reported={chi2_reported} recomputed={chi2_recomputed} "
              f"match={match} struct={struct_ok} -> {flag}", flush=True)
    json.dump({'band': list(BAND), 'method': 'per-occurrence phase '
              '(pclasses) via deterministic rebuild, q_cycle=0.5, T=56; '
              'R7-fixed 2026-10-07',
               'rows': rows},
              open(os.path.join(HERE, 'band_check_results.json'), 'w'),
              indent=1)
    bad = [r['seed'] for r in rows
           if not (r['in_band'] and r['recomputed_matches_reported']
                   and r['structural_ok'])]
    print(f"\nBAND [{lo}, {hi}]: "
          f"{'ALL CHECKS PASS' if not bad else 'FLAGGED: ' + str(bad)}")
    sys.exit(0 if not bad else 2)


if __name__ == '__main__':
    main()
