#!/usr/bin/env python3
"""Era (Tocqueville) word-space rates for the key-structure battery.

Word-space comparisons are established lane practice (F45 S4, attempt-3
re-validations). F30 bars era-SYLLABLE-conditional legs on morphological
fragments (er/i/e/m) -- so rate legs apply only to whole-syllable words
(ce/le/me/est/que/qui/la/se/pas/ne...); fragment cells get no rate leg.
"""
import json, math, re, sys
from collections import Counter
from pathlib import Path

LANE = Path('/home/hatch/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
OUT = LANE / 'code' / 'crowd7' / 'keystruct'


def load_tocqueville():
    toks = []
    for fn in ['gutenberg-30513-tocqueville-t1.txt', 'gutenberg-30514-tocqueville-t2.txt']:
        txt = (LANE / 'data' / fn).read_text(encoding='utf-8', errors='replace')
        m1 = re.search(r'\*\*\* START OF.*?\*\*\*', txt)
        m2 = re.search(r'\*\*\* END OF.*?\*\*\*', txt)
        if m1:
            txt = txt[m1.end():]
        if m2:
            txt = txt[:m2.start()]
        toks += re.findall(r"[a-zàâäéèêëîïôöùûüÿçœæ]+", txt.lower())
    return toks


def main():
    toks = load_tocqueville()
    N = len(toks)
    uni = Counter(toks)
    bi = Counter(zip(toks[:-1], toks[1:]))
    vocab = ['ce', 'le', 'la', 'les', 'me', 'te', 'se', 'est', 'que', 'qui',
             'ne', 'pas', 'en', 'de', 'je', 'il', 'on', 'nous', 'vous',
             'même', 'plus', 'tout', 'comme', 'dans', 'par', 'pour', 'sans',
             'cela', 'cette', 'mon', 'son', 'leur', 'leurs', 'y', 'a']
    out = {'N': N, 'uni': {}, 'foll': {}, 'pred': {}}
    for w in vocab:
        out['uni'][w] = {'n': uni[w], 'p': uni[w] / N}
        f = Counter(); p_ = Counter()
        for (w1, w2), c in bi.items():
            if w1 == w:
                f[w2] += c
            if w2 == w:
                p_[w1] += c
        tf, tp = sum(f.values()), sum(p_.values())
        out['foll'][w] = {'top': [[w2, c, round(c / tf, 4)] for w2, c in f.most_common(12)],
                          'full': {w2: c for w2, c in f.most_common(400)}, 'tot': tf}
        out['pred'][w] = {'top': [[w1, c, round(c / tp, 4)] for w1, c in p_.most_common(12)],
                          'full': {w1: c for w1, c in p_.most_common(400)}, 'tot': tp}
    (OUT / 'era_rates.json').write_text(json.dumps(out, indent=1, ensure_ascii=False))
    print('N =', N)
    for w in ['ce', 'le', 'me', 'est', 'que', 'qui']:
        u = out['uni'][w]
        print(f"{w}: n={u['n']} p={u['p']:.4f}")
        print('   foll:', [(w2, c) for w2, c, _ in out['foll'][w]['top'][:6]])
        print('   pred:', [(w1, c) for w1, c, _ in out['pred'][w]['top'][:6]])


if __name__ == '__main__':
    main()


def syllable_unigrams():
    import sys
    sys.path.insert(0, str(LANE / 'code' / 'crowd2'))
    from scorer_smith import syllabify
    toks = load_tocqueville()
    syl = Counter()
    tot = 0
    for w in toks:
        try:
            ss = syllabify(w)
        except Exception:
            ss = [w]
        for s in ss:
            syl[s] += 1
            tot += 1
    return syl, tot
