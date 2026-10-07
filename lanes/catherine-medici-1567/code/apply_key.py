#!/usr/bin/env python3
"""Apply the Charles IX key table (Lasry 2022) to the Catherine 1567 cipher.

Loads data/charlesIX-key-table.json, substitutes 'certain' mappings into
data/medici-1567-cipher.txt (normalized stream). Unmapped symbols are left
bracketed, e.g. [p]. Uncertain mappings are NOT applied.
"""
import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parent.parent

def load_cipher(path):
    toks = []
    with open(path, encoding='utf-8') as f:
        in_norm = False
        for line in f:
            s = line.strip()
            if s.startswith('## NORMALIZED'):
                in_norm = True
                continue
            if not in_norm:
                continue
            if s.startswith('L') and ':' in s:
                label, body = s.split(':', 1)
                toks.append((label.strip(), body.strip().split()))
            elif s.startswith('INLINE'):
                toks.append(('INLINE', ['X']))
    return toks

def main():
    key_path = LANE / 'data' / 'charlesIX-key-table.json'
    cipher_path = LANE / 'data' / 'medici-1567-cipher.txt'
    out_path = LANE / 'data' / 'keyed-attempt1.txt'
    key = json.loads(key_path.read_text(encoding='utf-8'))
    certain = {g: v['plain'] for g, v in key['mappings'].items()
               if v.get('status') == 'certain' and v.get('plain')}
    rows = load_cipher(cipher_path)
    mapped = unmapped = 0
    lines = []
    lines.append('# Keyed attempt 1: Charles IX (Lasry 2022) key applied to Catherine 1567 cipher')
    lines.append(f'# key table: {key_path.name}; certain mappings applied: {len(certain)}')
    lines.append('# bracketed tokens are unmapped; uncertain mappings NOT applied')
    lines.append('')
    for label, toks in rows:
        out = []
        for t in toks:
            if t in certain:
                out.append(certain[t])
                mapped += 1
            else:
                out.append(f'[{t}]')
                unmapped += 1
        lines.append(f'{label}: ' + ' '.join(out))
    lines.append('')
    lines.append(f'# stats: {mapped} tokens mapped, {unmapped} tokens unmapped '
                 f'({mapped/(mapped+unmapped)*100:.1f}% coverage)')
    out_path.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print('\n'.join(lines))
    print(f'\nwrote {out_path}', file=sys.stderr)

if __name__ == '__main__':
    main()
