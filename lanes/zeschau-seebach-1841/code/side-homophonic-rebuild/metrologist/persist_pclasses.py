#!/usr/bin/env python3
"""Close the pclasses provenance gap (R7 provenance note).

pclasses — the per-position occurrence-phase sequence the calibrated
occurrence-phase chi2 is computed from — was build-time-only (kept in
generator memory, never persisted). This tool re-derives it by deterministic
rebuild (certified q_cycle=0.5, T=56) and persists it SEALED: per-occurrence
phases are planted truth (like the key) — the solver must estimate phase
structure itself via its own contactor; the true phases stay sealed.

Writes metrologist/sealed-pclasses.json:
  {seed: {'pclasses': 'ABCBAC...', 'occurrence_chi2': X, 'sha256_ct': ...}}

The Runner re-runs this after the 184205->184207 swap to cover the final 6.
Usage: python3 persist_pclasses.py [seed ...]
"""
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REBUILD_CTL = os.path.normpath(os.path.join(HERE, '..', 'control'))
INST = os.path.join(REBUILD_CTL, 'instances')
sys.path.insert(0, REBUILD_CTL)
import generator as g  # noqa: E402

DEFAULT_SEEDS = [184201, 184202, 184203, 184204, 184206, 184207]
Q_CERTIFIED = 0.5
T_CERTIFIED = 56


def main():
    seeds = [int(s) for s in sys.argv[1:]] or DEFAULT_SEEDS
    tokens = g.load_lesmis_tokens()
    group_labels = g.real_group_labels()
    out = {}
    for seed in seeds:
        p = dict(g.PARAMS)
        p['q_cycle'] = Q_CERTIFIED
        if seed not in p['seeds']:
            p['seeds'] = [184201, 184202, 184203, 184204, seed, 184206]
        inst = g.build_instance(seed, tokens, group_labels, p, T_CERTIFIED)
        pc = inst['pclasses']
        assert all(c in 'ABC' for c in pc) and len(pc) == 1846
        meta = json.load(open(os.path.join(
            INST, f'SYNTHETIC-meta-{seed}.json')))
        assert g.occurrence_chi2(pc) == meta['occurrence_chi2'], \
            f'seed {seed}: rederived chi2 != meta'
        ct_path = os.path.join(INST, f'SYNTHETIC-ct-{seed}.pairs.txt')
        out[str(seed)] = {
            'pclasses': ''.join(pc),
            'occurrence_chi2': meta['occurrence_chi2'],
            'sha256_ct': hashlib.sha256(open(ct_path, 'rb').read()).hexdigest(),
            'derived': 'deterministic rebuild, q_cycle=0.5, T=56',
        }
        print(f'{seed}: pclasses persisted ({len(pc)} phases), '
              f'chi2={meta["occurrence_chi2"]}', flush=True)
    doc = {
        'SEALED': 'Planted truth (like the key). NEVER show to the solver. '
                  'Runner/diagnostic use only.',
        'seeds': out,
    }
    path = os.path.join(HERE, 'sealed-pclasses.json')
    json.dump(doc, open(path, 'w'), indent=1)
    print(f'wrote {path} '
          f'(sha256 {hashlib.sha256(open(path, "rb").read()).hexdigest()[:16]}...)')
    

if __name__ == '__main__':
    main()
