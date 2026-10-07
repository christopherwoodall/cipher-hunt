#!/usr/bin/env python3
"""Diplomatic-register rate battery for 59='est' (round-7 closer, pre-registered L1/L3/L4/L5).

Corpus: code/side-period/corpus/ French files (Allgemeine Zeitung German excluded).
Elision-split tokenization per round-5 convention ('c'est' -> c', est).
Outputs JSON + prints the rate table.
"""
import json, re, unicodedata
from pathlib import Path
from collections import Counter

LANE = Path(__file__).resolve().parents[3]
CORP = LANE / 'code' / 'side-period' / 'corpus'

FRENCH = {
    'guizot-t5t6': 'guizot-memoires-t5-t6.txt',          # Guizot's 1840-42 despatches (primary)
    'guizot-t1': 'guizot-memoires-t1-gutenberg.txt',
    'guizot-t2': 'guizot-memoires-t2-gutenberg.txt',
    'guizot-t3': 'guizot-memoires-t3-gutenberg.txt',
    'nesselrode-v7': 'nesselrode-v7.txt',
    'nesselrode-v8': 'nesselrode-v8.txt',                # 1840-46 incl. full 1841 run (primary)
    'nesselrode-v9': 'nesselrode-v9.txt',
    'nesselrode-v10': 'nesselrode-v10.txt',
    'pozzo': 'pozzo-di-borgo-correspondance-v1.txt',
    'metternich-v4': 'metternich-papiere-v4.txt',
    'metternich-v6': 'metternich-papiere-v6.txt',
    'talleyrand': 'talleyrand-memoires-v1.txt',
    'rdm-q1': 'revue-deux-mondes-1841-q1.txt',
    'rdm-q2': 'revue-deux-mondes-1841-q2.txt',
    'rdm-q3': 'revue-deux-mondes-1841-q3.txt',
    'rdm-q4': 'revue-deux-mondes-1841-q4.txt',
    'levant': 'levant-correspondence-1841-p3.txt',
}

WORD = re.compile(r"[a-zàâäéèêëîïôöùûüÿçœæ]+(?:'[a-zàâäéèêëîïôöùûüÿçœæ]+)*")

def tokenize(text):
    text = unicodedata.normalize('NFC', text.lower().replace('’', "'").replace('‘', "'"))
    toks = []
    for m in WORD.finditer(text):
        w = m.group(0)
        # elision split: "c'est" -> ["c'", "est"]; keep "'"-prefix on first piece
        parts = w.split("'")
        for i, p in enumerate(parts):
            if not p:
                continue
            toks.append(p + "'" if i < len(parts) - 1 else p)
    return toks

def rates(toks):
    n = len(toks)
    uni = Counter(toks)
    bi = Counter(zip(toks[:-1], toks[1:]))
    def P(a, b):  # P(b|a)
        d = uni.get(a, 0)
        return (bi.get((a, b), 0) / d) if d else None
    return {
        'n_tokens': n,
        'P_est': uni.get('est', 0) / n,
        'n_est': uni.get('est', 0),
        'P_que_given_est': P('est', 'que'),
        'n_que_given_est': bi.get(('est', 'que'), 0),
        'P_est_given_qui': P('qui', 'est'),
        'n_est_given_qui': bi.get(('qui', 'est'), 0),
        'n_qui': uni.get('qui', 0),
        'P_est_given_ne': P('ne', 'est'),
        'n_est_given_ne': bi.get(('ne', 'est'), 0),
        'n_ne': uni.get('ne', 0),
        'P_est_given_n': P("n'", 'est'),
        'n_est_given_n': bi.get(("n'", 'est'), 0),
        'n_n': uni.get("n'", 0),
        'P_doute': uni.get('doute', 0) / n,
        'P_dit': uni.get('dit', 0) / n,
        'P_fait': uni.get('fait', 0) / n,
        'P_veut': uni.get('veut', 0) / n,
        'P_peut': uni.get('peut', 0) / n,
        'n_doute': uni.get('doute', 0), 'n_dit': uni.get('dit', 0),
        'n_fait': uni.get('fait', 0), 'n_veut': uni.get('veut', 0),
        'n_peut': uni.get('peut', 0),
    }

def main():
    out = {}
    all_toks = []
    guizot_toks, ness8_toks = [], []
    for name, fn in FRENCH.items():
        p = CORP / fn
        if not p.exists():
            print('MISSING', fn); continue
        toks = tokenize(p.read_text(encoding='utf-8', errors='replace'))
        r = rates(toks)
        out[name] = r
        all_toks += toks
        if name == 'guizot-t5t6':
            guizot_toks = toks
        if name == 'nesselrode-v8':
            ness8_toks = toks
        print(f"{name:16s} n={r['n_tokens']:8d} P(est)={r['P_est']:.5f} "
              f"P(que|est)={r['P_que_given_est']:.5f} P(est|qui)={r['P_est_given_qui']:.4f} "
              f"P(est|ne)={r['P_est_given_ne']:.4f}")
    out['diplomatic_all'] = rates(all_toks)
    out['guizot_t5t6_only'] = rates(guizot_toks)
    out['nesselrode_v8_only'] = rates(ness8_toks)
    d = out['diplomatic_all']
    print(f"\n{'diplomatic_all':16s} n={d['n_tokens']:8d} P(est)={d['P_est']:.5f} "
          f"P(que|est)={d['P_que_given_est']:.5f} P(est|qui)={d['P_est_given_qui']:.4f} "
          f"P(est|ne)={d['P_est_given_ne']:.4f}")
    print('rivals (diplomatic_all):', {k: round(d['P_'+k], 6) for k in
          ['doute','dit','fait','veut','peut']})
    json.dump(out, open(Path(__file__).parent / 'diplomatic_rates.json', 'w'), indent=1)
    print('wrote diplomatic_rates.json')

if __name__ == '__main__':
    main()
