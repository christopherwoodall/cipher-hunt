"""KILL-2 fix: deterministically rebuild 'planted' per position and persist to
the six sealed key files.

Verifies bit-identical pairs against the shipped files before writing.
The sealed key files are Runner-only; the solver never reads them.

Usage: python3 persist_planted.py
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from generator import (PARAMS, build_instance, load_lesmis_tokens,
                       real_group_labels)

# certified values from build_summary.json (do NOT re-calibrate)
Q_CYCLE = 0.5
T_EFF = 56


def main():
    p = dict(PARAMS)
    p['q_cycle'] = Q_CYCLE
    print("loading Les Mis tokens...", flush=True)
    tokens = load_lesmis_tokens()
    group_labels = real_group_labels()
    outd = os.path.join(HERE, 'instances')

    for seed in p['seeds']:
        print(f"seed {seed}: rebuilding...", flush=True)
        inst = build_instance(seed, tokens, group_labels, p, T_EFF)

        # verify bit-identical pairs against the shipped file
        ct_path = os.path.join(outd, f"SYNTHETIC-ct-{seed}.pairs.txt")
        with open(ct_path) as f:
            lines = [ln for ln in f if not ln.startswith('#')]
        shipped_pairs = ' '.join(lines).split()
        if shipped_pairs != inst['pairs']:
            print(f"  FAIL: rebuilt pairs differ from shipped file "
                  f"({len(shipped_pairs)} vs {len(inst['pairs'])})")
            # find first difference
            for i, (a, b) in enumerate(zip(shipped_pairs, inst['pairs'])):
                if a != b:
                    print(f"  first diff at position {i}: {a!r} vs {b!r}")
                    break
            sys.exit(1)
        print(f"  pairs bit-identical ({len(inst['pairs'])} pairs)")

        # append 'planted' to the sealed key file
        key_path = os.path.join(outd, f"SYNTHETIC-key-{seed}.json")
        with open(key_path) as f:
            key_data = json.load(f)
        if 'planted' in key_data:
            print(f"  'planted' already present, verifying length...")
            if len(key_data['planted']) != len(inst['pairs']):
                print(f"  FAIL: length mismatch")
                sys.exit(1)
        else:
            key_data['planted'] = inst['planted']
            # write back with a comment noting the KILL-2 fix
            with open(key_path, 'w') as f:
                json.dump(key_data, f, indent=1, ensure_ascii=False)
            print(f"  'planted' persisted ({len(inst['planted'])} positions)")

    print("KILL-2 fix complete: all 6 sealed key files have per-position "
          "'planted'.")


if __name__ == '__main__':
    main()
