"""CONCERN-6 fix: move key-adjacent fields from open meta/ to sealed key files.

Moves 'polyvalent_groups' (the 6 islet labels) and 'params' (full generator
params) from SYNTHETIC-meta-<seed>.json (open) to SYNTHETIC-key-<seed>.json
(sealed, Runner-only). Meta keeps a sealed-note placeholder.

Usage: python3 seal_meta_leak.py
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUTD = os.path.join(HERE, 'instances')
SEEDS = [184201, 184202, 184203, 184204, 184207, 184206]


def main():
    for seed in SEEDS:
        meta_path = os.path.join(OUTD, f"SYNTHETIC-meta-{seed}.json")
        key_path = os.path.join(OUTD, f"SYNTHETIC-key-{seed}.json")

        meta = json.load(open(meta_path))
        key_data = json.load(open(key_path))

        moved = {}
        for field in ('polyvalent_groups', 'params'):
            if field in meta:
                moved[field] = meta.pop(field)
                meta[field + '_sealed'] = True

        if moved:
            # append to sealed key file
            key_data['sealed_meta'] = moved
            json.dump(key_data, open(key_path, 'w'), indent=1,
                      ensure_ascii=False)
            # write back meta without the key-adjacent fields
            json.dump(meta, open(meta_path, 'w'), indent=1,
                      ensure_ascii=False)
            print(f"seed {seed}: moved {list(moved)} to sealed key file")
        else:
            print(f"seed {seed}: already sealed (skipped)")

    print("CONCERN-6 fix complete: meta/ no longer exposes islet labels or "
          "full params.")


if __name__ == '__main__':
    main()
