#!/usr/bin/env python3
"""Apply an archival key table (certain single-plain mappings only) to the cipher.

Usage: apply_archival_key.py <key.json> <out.txt>
- status 'certain' with one plain value -> substituted
- 'certain-ambiguous' (homophone shared across letters) -> bracketed with candidates
- 'uncertain' -> never applied, bracketed plain
Also prints glyph-overlap stats vs the 40 cipher glyphs.
"""
import json
import sys
from collections import Counter
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
    key_path = Path(sys.argv[1])
    out_path = Path(sys.argv[2])
    key = json.loads(key_path.read_text(encoding='utf-8'))
    certain = {}
    ambiguous = {}
    for g, v in key.get('mappings', {}).items():
        if v.get('status') == 'certain' and v.get('plain'):
            certain[g] = v['plain']
        elif v.get('status') == 'certain-ambiguous':
            ambiguous[g] = v.get('candidates', [])
    rows = load_cipher(LANE / 'data' / 'medici-1567-cipher.txt')
    mapped = unmapped = 0
    lines = [f'# Keyed attempt: {key_path.name} certain row-1 mappings applied to Catherine 1567 cipher',
             f'# certain single-plain: {len(certain)}; certain-ambiguous: {len(ambiguous)}; uncertain: never applied',
             '# bracketed tokens unmapped; [g:c1/c2] = homophone shared across letters, not resolved', '']
    for label, toks in rows:
        out = []
        for t in toks:
            if t in certain:
                out.append(certain[t]); mapped += 1
            elif t in ambiguous:
                out.append(f"[{t}:{'/'.join(ambiguous[t])}]"); unmapped += 1
            else:
                out.append(f'[{t}]'); unmapped += 1
        lines.append(f'{label}: ' + ' '.join(out))
    # overlap stats
    all_toks = [t for _, ts in rows for t in ts]
    freq = Counter(all_toks)
    key_glyphs = set(key.get('mappings', {})) | set(key.get('uncertain', {}))
    overlap = [g for g in freq if g in key_glyphs]
    cov = sum(freq[g] for g in overlap)
    top = ['p','g','z','a','o','E','f']
    lines += ['', '# --- overlap stats ---',
              f'# cipher glyphs in key inventory (certain+uncertain): {len(overlap)}/40',
              f'# token coverage of key inventory: {cov}/{len(all_toks)} ({cov/len(all_toks)*100:.1f}%)',
              f'# top-glyph mapping status:']
    for g in top:
        st = 'MISSING'
        if g in certain: st = f"certain -> {certain[g]}"
        elif g in ambiguous: st = f"ambiguous {ambiguous[g]}"
        elif g in key.get('uncertain', {}):
            st = f"uncertain {key['uncertain'][g].get('candidates')}"
        lines.append(f'#   {g} ({freq[g]}x): {st}')
    lines += ['', f'# apply stats: {mapped} mapped, {unmapped} unmapped ({mapped/(mapped+unmapped)*100:.1f}% decoded)']
    out_path.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print('\n'.join(lines))
    print(f'\nwrote {out_path}', file=sys.stderr)

if __name__ == '__main__':
    main()
