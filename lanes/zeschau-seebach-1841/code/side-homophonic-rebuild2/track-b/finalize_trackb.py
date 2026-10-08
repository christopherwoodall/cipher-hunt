#!/usr/bin/env python3
"""Track B: finalize a killed-at-convergence (or wall) run.

Replicates train_lm.py's end-of-run finalization EXACTLY (same code path for
model.npz / loss_curve.json / manifest.json), using the best-by-held-out
params stored in ckpt.npz. Run only after the trainer is stopped.
Usage: finalize_trackb.py <stop_reason>
Writes model.npz, loss_curve.json, manifest.json + md5sums to sha256sums.txt.
"""
import hashlib
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import train_lm

REBUILD = os.path.join(os.path.dirname(HERE), '..', '..',
                       'side-homophonic-rebuild')


def md5(p):
    return hashlib.md5(open(p, 'rb').read()).hexdigest()


def main():
    stop_reason = sys.argv[1] if len(sys.argv) > 1 else 'manual_stop'
    ck = json.load(open(os.path.join(HERE, 'ckpt.json')))
    z = np.load(os.path.join(HERE, 'ckpt.npz'))

    lm_meta = json.load(open(os.path.join(
        REBUILD, 'solver', 'lm_ref', 'lm.json')))['meta']
    alphabet = lm_meta['alphabet']
    assert len(alphabet) == 30
    c2i = {ch: i for i, ch in enumerate(alphabet)}
    V = len(alphabet)

    print('[finalize] building line pool (same as train_lm)...', flush=True)
    train_lines, heldout_lines, stats, guizot_info = train_lm.build_lines()
    Harr = train_lm.words_to_ids(heldout_lines, c2i)
    n_train_chars = int(sum(len(w) for L in train_lines for w in L))
    n_ho_chars = int(len(Harr))
    per_file_chars = [{k: st[k] for k in (
        'file', 'sha256', 'train_lines', 'heldout_lines',
        'train_words', 'heldout_words')} for st in stats]

    H, T, B = 96, 64, 96
    net = train_lm.CharLSTM(V, H, seed=train_lm.SEED)
    best_params = {k: z['best_' + k] for k in net.pnames}
    net.set_params(best_params)
    final_held = train_lm.heldout_nll(net, Harr)
    print(f'[finalize] best_update={ck["best_update"]} '
          f'best_heldout={ck["best_heldout"]:.4f} '
          f'final_heldout(recomputed)={final_held:.4f}', flush=True)

    mp = os.path.join(HERE, 'model.npz')
    np.savez(mp, **{k: v for k, v in net.get_params().items()},
             H=np.array(H), V=np.array(V))
    lp = os.path.join(HERE, 'loss_curve.json')
    json.dump(ck['curve'], open(lp, 'w'), indent=1)
    last = ck['curve'][-1]
    manifest = {
        'track': 'b', 'seed': train_lm.SEED,
        'go_authorization': 'redteam/RULINGS.md R5 (2026-10-07)',
        'files': per_file_chars,
        'n_train_chars': n_train_chars, 'n_heldout_chars': n_ho_chars,
        'guizot_r5b_exclusion': guizot_info,
        'lesmis_scan': {'rule': 'word-8-grams on NFD-stripped trainable bodies',
                        'hits_total': 13,
                        'script': 'track-b/scan_lesmis_overlap.py'},
        'model': {'arch': 'char-LSTM 1 layer', 'H': H, 'T': T, 'B': B,
                  'params': sum(int(v.size) for v in net.get_params().values()),
                  'optimizer': 'Adam lr=2e-3 halve-on-plateau floor 2e-4, clip 5.0'},
        'training': {'updates': ck['update'],
                     'chars_seen': ck['update'] * T * B,
                     'stop_reason': stop_reason,
                     'wall_s_total': last['wall_s'],
                     'best_update': ck['best_update'],
                     'best_heldout_nll': round(float(ck['best_heldout']), 4),
                     'final_heldout_nll': round(float(final_held), 4)},
        'pins': {'python': '3.12.3', 'numpy': '1.26.4', 'torch': None,
                 'cpu_threads': 2},
        'r5005_contact': False,
        'finalized_by': 'finalize_trackb.py (replicates train_lm.py tail)',
        'finalized_at_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
    }
    mp2 = os.path.join(HERE, 'manifest.json')
    json.dump(manifest, open(mp2, 'w'), indent=1)
    sums = {os.path.basename(p): md5(p) for p in (mp, lp, mp2)}
    json.dump(sums, open(os.path.join(HERE, 'sha256sums_final.json'), 'w'),
              indent=1)
    for f, s in sums.items():
        print(f'[finalize] {s}  {f}', flush=True)
    print('[finalize] done', flush=True)


if __name__ == '__main__':
    main()
