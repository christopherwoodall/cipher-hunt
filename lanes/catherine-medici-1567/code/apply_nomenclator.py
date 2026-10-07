#!/usr/bin/env python3
"""Apply an archival key table's alphabet AND nomenclature rows to the cipher.

New script (2026-10-07, attempt4/5 work order); apply_archival_key.py is left
untouched so attempts 2/3 stay reproducible.

Usage: apply_nomenclator.py <key.json> <out.txt>

Application rules (documented disambiguation):
- status 'certain' ONLY. 'certain-ambiguous', 'uncertain', 'null' are never
  applied (bracketed with their status in output).
- Pass 1 (nomenclature bigrams): certain nomenclature entries whose cipher
  form is exactly 2 cipher tokens are matched left-to-right, non-overlapping,
  on the RAW token stream. Nomenclator words take precedence over spelling
  the same tokens as alphabet letters (standard nomenclator behavior).
  Matches render as {word} and consume both tokens.
- Pass 2 (alphabet): certain single-plain alphabet mappings, as before.
- Pass 3 (nomenclature singletons): certain nomenclature entries whose cipher
  form is exactly 1 cipher token render as {word}.
- A nomenclature entry whose cipher glyph does not occur in the cipher token
  inventory is recorded but cannot apply (reported in stats).
- Homograph conflicts inside a table (same glyph -> two words, or a glyph
  already mapped in the alphabet row) are marked 'uncertain' in the JSON and
  never applied here.
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

    # alphabet: certain single-plain only
    alpha = {}
    alpha_amb = {}
    for g, v in key.get('mappings', {}).items():
        if v.get('status') == 'certain' and v.get('plain'):
            alpha[g] = v['plain']
        elif v.get('status') == 'certain-ambiguous':
            alpha_amb[g] = v.get('candidates', [])

    # nomenclature: certain only; split singletons vs bigrams
    nom_single = {}   # cipher_token -> word
    nom_bigram = {}   # (t1, t2) -> word
    nom_inapplicable = []  # certain but glyph absent from cipher
    nom_uncertain = []
    for e in key.get('nomenclature', []):
        st = e.get('status')
        if st != 'certain':
            nom_uncertain.append(e)
            continue
        c = e.get('cipher') or ''
        w = e.get('word')
        if len(c) == 1:
            nom_single[c] = w
        elif len(c) == 2:
            nom_bigram[(c[0], c[1])] = w
        else:
            nom_inapplicable.append(e)

    rows = load_cipher(LANE / 'data' / 'medici-1567-cipher.txt')
    all_toks = [t for _, ts in rows for t in ts]
    freq = Counter(all_toks)
    n_total = len(all_toks)

    lines = [f'# Keyed attempt (full): {key_path.name} alphabet + nomenclature applied to Catherine 1567 cipher',
             f'# alphabet certain single-plain: {len(alpha)}; certain-ambiguous: {len(alpha_amb)}',
             f'# nomenclature certain singletons: {len(nom_single)}; certain bigrams: {len(nom_bigram)}; '
             f'certain-but-inapplicable: {len(nom_inapplicable)}; non-certain/null: {len(nom_uncertain)}',
             '# pass order: (1) nomenclature bigrams {word} on raw stream, (2) alphabet letters, (3) nomenclature singletons {word}',
             '# [t] = unmapped; [t:c1/c2] = homophone, not resolved', '']
    bigram_hits = Counter()
    mapped = unmapped = 0
    for label, toks in rows:
        out = []
        i = 0
        while i < len(toks):
            pair = (toks[i], toks[i + 1]) if i + 1 < len(toks) else None
            if pair in nom_bigram:
                w = nom_bigram[pair]
                out.append('{' + w + '}')
                bigram_hits[w] += 1
                mapped += 2
                i += 2
                continue
            t = toks[i]
            if t in alpha:
                out.append(alpha[t]); mapped += 1
            elif t in nom_single:
                out.append('{' + nom_single[t] + '}'); mapped += 1
            elif t in alpha_amb:
                out.append(f"[{t}:{'/'.join(alpha_amb[t])}]"); unmapped += 1
            else:
                out.append(f'[{t}]'); unmapped += 1
            i += 1
        lines.append(f'{label}: ' + ' '.join(out))

    lines += ['', '# --- bigram nomenclature hits ---']
    if bigram_hits:
        for w, n in bigram_hits.most_common():
            lines.append(f'#   {{{w}}}: {n} occurrence(s)')
    else:
        lines.append('#   (none)')
    lines += ['', '# --- nomenclature coverage detail ---']
    for g, w in sorted(nom_single.items()):
        n = freq.get(g, 0)
        lines.append(f'#   {{{w}}}: cipher token {g!r} occurs {n}x -> {"APPLIED" if n else "no target in cipher"}')
    if nom_inapplicable:
        lines.append('#   certain but glyph absent from cipher inventory (not applied):')
        for e in nom_inapplicable:
            lines.append(f"#     {e['word']!r} cipher={e['cipher']!r}")
    lines += ['', '# --- overlap stats ---']
    key_glyphs = set(key.get('mappings', {})) | set(key.get('uncertain', {})) | set(nom_single)
    overlap = [g for g in freq if g in key_glyphs]
    cov = sum(freq[g] for g in overlap)
    lines.append(f'# cipher glyphs in key inventory (certain+uncertain+nom): {len(overlap)}/39')
    lines.append(f'# token coverage of key inventory: {cov}/{n_total} ({cov/n_total*100:.1f}%)')
    top = ['#', 'p', 'g', 'z', 'a', 'o', 'E', 'f']
    lines.append('# top-glyph mapping status:')
    for g in top:
        st = 'MISSING'
        if g in alpha:
            st = f"alphabet certain -> {alpha[g]}"
        elif g in alpha_amb:
            st = f"alphabet ambiguous {alpha_amb[g]}"
        elif g in nom_single:
            st = f"nomenclature certain -> {{{nom_single[g]}}}"
        elif g in key.get('uncertain', {}):
            st = f"uncertain {key['uncertain'][g].get('candidates')}"
        lines.append(f'#   {g} ({freq[g]}x): {st}')
    lines.append(f'# apply stats: {mapped} mapped, {unmapped} unmapped '
                 f'({mapped/(mapped+unmapped)*100:.1f}% decoded)')
    out_path.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print('\n'.join(lines))
    print(f'\nwrote {out_path}', file=sys.stderr)


if __name__ == '__main__':
    main()
