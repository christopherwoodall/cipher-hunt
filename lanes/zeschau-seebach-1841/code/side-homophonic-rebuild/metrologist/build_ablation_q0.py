#!/usr/bin/env python3
"""Metrologist task 2: build the q_cycle=0 (phase-rhythm scrubbed) ablation set.

Same generator code as the rebuild control (byte-identical except the seed
list), same 6 slices (idx 0..5), T=56, but q_cycle=0 -> occurrence phases are
pure uniform noise; the occurrence-phase chi2 should collapse to the noise
floor (~df=4, E=4).

Seeds 184213-184218: fresh, never materialized before (the 184207-184212
replacement-walk probes were in-memory only, keys never persisted).

Writes to metrologist/ablation-q0/:
  SYNTHETIC-{ct,key,crib,meta}-<seed>.*   (keys SEALED: Runner scoring only)
  ablation-chance-baseline.json
  ablation-build-summary.json  (with sha256 + scrub verification)

The Runner scores the REBUILT solver on this set and compares against the
fresh (q_cycle=0.5) set: a solver that needs the rhythm to beat the bar is
leaning on a synthetic crutch.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUTD = os.path.join(HERE, 'ablation-q0')
REBUILD_CTL = os.path.normpath(os.path.join(
    HERE, '..', 'control'))
sys.path.insert(0, REBUILD_CTL)
import generator  # noqa: E402  (rebuild control's generator; seeds overridden)

SEEDS = [184213, 184214, 184215, 184216, 184217, 184218]
T = 56
Q = 0.0


def load_pairs(path):
    pairs = []
    for line in open(path):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        pairs.extend(line.split())
    return pairs


def main():
    os.makedirs(OUTD, exist_ok=True)
    generator.OUTD = OUTD  # write_instance targets this dir
    p = dict(generator.PARAMS)
    p['seeds'] = SEEDS
    p['q_cycle'] = Q  # SCRUBBED rhythm (certified 0.5 deliberately NOT used)
    tokens = generator.load_lesmis_tokens()
    group_labels = generator.real_group_labels()
    print(f'q_cycle={Q} (scrubbed) T={T} seeds={SEEDS}', flush=True)

    chance, summary = {}, {}
    for seed in SEEDS:
        inst = generator.build_instance(seed, tokens, group_labels, p, T,
                                        verbose=True)
        meta = generator.write_instance(inst, p)
        cb = generator.chance_baseline(inst, p)
        chance[str(seed)] = cb
        occ = generator.occurrence_chi2(inst['pclasses'])
        summary[str(seed)] = {
            'T': T, 'q_cycle': Q,
            'occurrence_chi2': occ,
            'unsupervised_chi2': inst['chi2'],
            'keep_rate': round(inst['keep_rate'], 4),
            'n_islets': inst['n_islets'],
            'crib_pair_offset': inst['crib_pair_offset'],
            'chance_primary_mean': round(cb['primary']['mean'], 5),
            'chance_primary_sd': round(cb['primary']['sd'], 5),
            'chance_secondary_mean': round(cb['secondary']['mean'], 5),
            'chance_secondary_sd': round(cb['secondary']['sd'], 5),
            'oracle_decode_accuracy': round(cb['oracle_decode_accuracy'], 5),
            'sha256': meta['sha256'],
        }
        oracle = cb["oracle_decode_accuracy"]
        print(f'  seed {seed}: occ_chi2={occ} (scrub target: noise floor ~4) '
              f'oracle={oracle:.4f}', flush=True)

    json.dump(chance, open(os.path.join(OUTD, 'ablation-chance-baseline.json'),
                           'w'), indent=1)
    json.dump({'q_cycle': Q, 'T': T, 'seeds': SEEDS,
               'purpose': 'phase-rhythm ablation: q_cycle=0 scrubs the '
                          'occurrence-phase rotation. The rebuilt solver must '
                          'beat the bar on the fresh q=0.5 set WITHOUT '
                          'depending on the rhythm (see FINDINGS.md).',
               'generator': 'code/side-homophonic-rebuild/control/generator.py '
                            '(byte-identical to frozen except seed list)',
               'instances': summary},
              open(os.path.join(OUTD, 'ablation-build-summary.json'), 'w'),
              indent=1)

    # ---- scrub verification ----
    CRIB6 = ['11', '70', '82', '34', '29', '40']
    ok = True
    print('\n=== SCRUB VERIFICATION ===', flush=True)
    for seed in SEEDS:
        pairs = load_pairs(os.path.join(
            OUTD, f'SYNTHETIC-ct-{seed}.pairs.txt'))
        hits = [i for i in range(len(pairs) - 5)
                if pairs[i:i + 6] == CRIB6]
        occ = summary[str(seed)]['occurrence_chi2']
        scrubbed = occ < 20.0  # noise floor: df=4 chi2, E=4; 20 is generous
        struct = (len(pairs) == 1846 and len(set(pairs)) == 96
                  and len(hits) == 1)
        stat = 'SCRUBBED' if scrubbed else '*** RHYTHM STILL PRESENT ***'
        print(f'  {seed}: pairs={len(pairs)} groups={len(set(pairs))} '
              f'crib_hits={len(hits)} occ_chi2={occ} -> {stat} '
              f'struct={struct}', flush=True)
        ok = ok and scrubbed and struct
    print('ABLATION SET:', 'OK - rhythm scrubbed on all 6'
          if ok else 'FAILURES PRESENT', flush=True)
    sys.exit(0 if ok else 2)


if __name__ == '__main__':
    main()
