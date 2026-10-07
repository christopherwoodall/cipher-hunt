#!/usr/bin/env python3
"""Resumable builder for the 6 FRESH synthetic control instances (seeds 184201-184206)
for the Seebach homophonic-solver REBUILD fleet.

Same semantics as side-homophonic/control/generator.py --build-all, but:
  - imports the generator from THIS directory (re-seeded to 184201-184206)
  - checkpoints after each seed so a SIGTERM / infra kill loses at most one
    in-progress instance; re-running resumes from the checkpoint.

Writes:
  instances/SYNTHETIC-{ct,key,crib,meta}-<seed>.*
  build_checkpoint.json  (resume state: calibrated q_cycle/T, per-seed summary)
  chance_baseline.json   (incremental)
  build_summary.json     (final)
  calibration.json       (from calibrate)
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import generator  # noqa: E402

p = dict(generator.PARAMS)
CKPT = os.path.join(HERE, 'build_checkpoint.json')
CRIB6 = ['11', '70', '82', '34', '29', '40']  # crib phrase pair sequence


def load_ckpt():
    if os.path.exists(CKPT):
        return json.load(open(CKPT))
    return {'calibrated': None, 'seeds_done': {}}


def save_ckpt(c):
    tmp = CKPT + '.tmp'
    json.dump(c, open(tmp, 'w'), indent=1)
    os.replace(tmp, CKPT)


def main():
    c = load_ckpt()
    tokens = generator.load_lesmis_tokens()
    group_labels = generator.real_group_labels()
    print(f"lesmis tokens={len(tokens)} real groups={len(group_labels)}",
          flush=True)

    if c['calibrated'] is None:
        try:
            q_cycle, T = generator.calibrate(p, tokens, group_labels)
        except SystemExit as e:
            print(f"CALIBRATION FAILED (exit {e.code}); checkpointing and "
                  f"aborting", flush=True)
            save_ckpt(c)
            sys.exit(3)
        c['calibrated'] = {'q_cycle': q_cycle, 'T': T}
        save_ckpt(c)
    q_cycle, T = c['calibrated']['q_cycle'], c['calibrated']['T']
    p['q_cycle'] = q_cycle
    print(f"certified q_cycle={q_cycle} T={T}", flush=True)

    chance_path = os.path.join(HERE, 'chance_baseline.json')
    chance = json.load(open(chance_path)) if os.path.exists(chance_path) else {}
    summary = dict(c['seeds_done'])

    for seed in p['seeds']:
        skey = str(seed)
        if skey in summary:
            print(f"seed {seed}: already built (checkpoint), skipping",
                  flush=True)
            continue
        inst = generator.build_instance(seed, tokens, group_labels, p, T,
                                        verbose=True)
        meta = generator.write_instance(inst, p)
        cb = generator.chance_baseline(inst, p)
        chance[skey] = cb
        summary[skey] = {
            'T': T, 'q_cycle': q_cycle,
            'occurrence_chi2': generator.occurrence_chi2(inst['pclasses']),
            'unsupervised_chi2': inst['chi2'],
            'keep_rate': round(inst['keep_rate'], 4),
            'n_islets': inst['n_islets'],
            'crib_pair_offset': inst['crib_pair_offset'],
            'chance_primary_mean': round(cb['primary']['mean'], 5),
            'chance_primary_sd': round(cb['primary']['sd'], 5),
            'chance_secondary_mean': round(cb['secondary']['mean'], 5),
            'chance_secondary_sd': round(cb['secondary']['sd'], 5),
            'oracle_decode_accuracy': round(cb['oracle_decode_accuracy'], 5),
        }
        json.dump(chance, open(chance_path, 'w'), indent=1)
        c['seeds_done'] = summary
        save_ckpt(c)
        print(f"seed {seed}: CHECKPOINTED chance_primary="
              f"{cb['primary']['mean']:.4f}±{cb['primary']['sd']:.4f} "
              f"chance_secondary={cb['secondary']['mean']:.4f}±"
              f"{cb['secondary']['sd']:.4f} "
              f"oracle={cb['oracle_decode_accuracy']:.4f}", flush=True)

    json.dump({'certified_q_cycle': q_cycle, 'T': T, 'params': p,
               'instances': summary},
              open(os.path.join(HERE, 'build_summary.json'), 'w'), indent=1)

    # ---- verification ----
    OUTD = os.path.join(HERE, 'instances')
    ok = True
    print("\n=== VERIFICATION ===", flush=True)
    for seed in p['seeds']:
        skey = str(seed)
        ct_path = os.path.join(OUTD, f"SYNTHETIC-ct-{seed}.pairs.txt")
        pairs = []
        for line in open(ct_path):
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            pairs.extend(line.split())
        n_pairs = len(pairs)
        n_groups = len(set(pairs))
        hits = [i for i in range(n_pairs - 5)
                if pairs[i:i + 6] == CRIB6]
        key_path = os.path.join(OUTD, f"SYNTHETIC-key-{seed}.json")
        key_data = json.load(open(key_path))
        sealed = ('sealed_meta' in key_data and
                  key_data.get('SEALED', '').startswith('Runner'))
        meta_path = os.path.join(OUTD, f"SYNTHETIC-meta-{seed}.json")
        meta = json.load(open(meta_path))
        chi2 = summary[skey]['occurrence_chi2']
        chi2_ok = 181.0 <= chi2 <= 320.0
        crib_ok = len(hits) == 1
        row_ok = (n_pairs == 1846 and n_groups == 96 and crib_ok and chi2_ok
                  and sealed)
        ok = ok and row_ok
        print(f"  seed {seed}: pairs={n_pairs} groups={n_groups} "
              f"crib_hits={len(hits)}@{hits[0] if hits else '-'} "
              f"chi2={chi2:.1f} {'INBAND' if chi2_ok else 'OUTOFBAND'} "
              f"sealed={'yes' if sealed else 'NO'} "
              f"-> {'OK' if row_ok else 'FAIL'}", flush=True)
    print(f"VERIFICATION: {'ALL OK' if ok else 'FAILURES PRESENT'}", flush=True)
    if not ok:
        sys.exit(4)


if __name__ == '__main__':
    main()
