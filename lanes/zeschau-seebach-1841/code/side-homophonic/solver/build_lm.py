#!/usr/bin/env python3
"""Build the era language model for the Seebach homophonic solver.

Corpus: Tocqueville, De la democratie en Amerique, T1 (1835) + T2 (1840),
Project Gutenberg 30513/30514 -- the lane's era reference (formal political
prose, 1835-1840; the closest available match to 1841 diplomatic French).

REGISTER CAVEAT (standing): formal published prose vs a diplomatic despatch.
Tocqueville argues about America; Zeschau writes about the Kuhnel succession.
Function words and morphology transfer well; content vocabulary does not. The
character n-gram and the word-salad bonus both degrade gracefully: content
words the model never saw simply contribute no word bonus, while the
character model still scores their letter sequences.

Pipeline (deterministic):
  1. Extract the Gutenberg body (between *** START/END markers).
  2. Tokenize words (apostrophes split: l'homme -> l, homme).
  3. Optionally exclude a word span (--exclude-span A B) so a synthetic
     control's plaintext never contaminates the reference (independence).
  4. Project every word through phonetics.project -> spaceless char stream.
     (No word boundaries: the deciphered stream has none either.)
  5. Count character 1..5-grams -> lm.json (interpolated scoring at run time).
  6. Word lexicon: pre-projection word frequencies -> projected forms,
     len>=4, dedup (freq summed), top 40000 by freq, weight=log(1+freq).
     The lexicon is the word-salad bonus of solver.py (Aho-Corasick).

Outputs: <out>/lm.json and <out>/lm_stats.md. Prints a build summary.
"""

import collections
import json
import math
import os
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from phonetics import project, alphabet  # noqa: E402

LANE = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
DATA = os.path.join(LANE, 'data')

CORPUS_FILES = [
    (os.path.join(DATA, 'gutenberg-30513-tocqueville-t1.txt'), 'Tocqueville T1 (1835), PG 30513'),
    (os.path.join(DATA, 'gutenberg-30514-tocqueville-t2.txt'), 'Tocqueville T2 (1840), PG 30514'),
]
NGRAM_ORDER = 5
LEXICON_MINLEN = 4
LEXICON_TOP = 40000
LEXICON_MINFREQ = 3
HELDOUT_FRAC = 0.10
WORD_RE = re.compile(r"[a-zàâäéèêëîïôöùûüÿçœæ]+")


def load_words(exclude_span=None):
    words = []
    for path, label in CORPUS_FILES:
        if not os.path.exists(path):
            raise SystemExit(f'corpus file missing: {path}')
        txt = open(path, encoding='utf-8', errors='replace').read()
        m1 = re.search(r'\*\*\* START OF.*?\*\*\*', txt)
        m2 = re.search(r'\*\*\* END OF.*?\*\*\*', txt)
        body = txt[m1.end():m2.start()] if m1 and m2 else txt
        # split apostrophes first (l'homme -> l homme), like the lane's tuner
        body = body.replace("'", ' ').replace('’', ' ')
        words.extend(WORD_RE.findall(body.lower()))
    if exclude_span:
        a, b = exclude_span
        words = words[:a] + words[b:]
    return words


def build(exclude_span=None, verbose=True):
    t0 = time.time()
    words = load_words(exclude_span)
    n_words_in = len(words)
    wfreq = collections.Counter(words)
    # project -> spaceless char stream
    chars = []
    for w in words:
        chars.append(project(w))
    stream = ''.join(chars)
    n_chars = len(stream)
    alpha = sorted(set(stream))
    if verbose:
        print(f'words={n_words_in} distinct={len(wfreq)} '
              f'proj_chars={n_chars} alphabet={len(alpha)}', flush=True)

    # character n-gram counts, orders 1..NGRAM_ORDER
    counts = {}
    for order in range(1, NGRAM_ORDER + 1):
        c = collections.Counter()
        if order == 1:
            c.update(stream)
        else:
            for i in range(len(stream) - order + 1):
                c[stream[i:i + order]] += 1
        counts[order] = c
        if verbose:
            print(f'  order {order}: {len(c)} distinct', flush=True)

    # held-out perplexity: train on first 90%, score last 10% (order-5, alpha)
    k = int(len(stream) * (1 - HELDOUT_FRAC))
    tr_counts = {}
    for order in range(1, NGRAM_ORDER + 1):
        c = collections.Counter()
        seg = stream[:k]
        if order == 1:
            c.update(seg)
        else:
            for i in range(len(seg) - order + 1):
                c[seg[i:i + order]] += 1
        tr_counts[order] = c
    V = len(alpha)
    # precompute context totals for the interpolated scorer
    tr_tot = {}
    for o in range(2, NGRAM_ORDER + 1):
        t = collections.Counter()
        for ng, n_ in tr_counts[o].items():
            t[ng[:-1]] += n_
        tr_tot[o] = t
    tr_uni_tot = max(sum(tr_counts[1].values()), 1)

    def lp_heldout(ch, ctx):
        # interpolated, alpha=0.5, computed on train counts
        p = tr_counts[1].get(ch, 0) / tr_uni_tot
        for o in range(2, NGRAM_ORDER + 1):
            cc = ctx[-(o - 1):]
            num = tr_counts[o].get(cc + ch, 0)
            den = tr_tot[o].get(cc, 0)
            p = (num + 0.5 * p) / (den + 0.5)
        return math.log(max(p, 1e-12))

    test = stream[k:]
    tot, n = 0.0, 0
    for i, ch in enumerate(test):
        tot += lp_heldout(ch, test[max(0, i - 4):i])
        n += 1
    heldout_per_char = tot / n
    if verbose:
        print(f'  held-out order-5 per-char logp: {heldout_per_char:.4f} '
              f'(perplexity {math.exp(-heldout_per_char):.1f})', flush=True)

    # word lexicon (projected)
    lex = collections.Counter()
    for w, f in wfreq.items():
        if f < LEXICON_MINFREQ:
            continue
        pw = project(w)
        if len(pw) >= LEXICON_MINLEN:
            lex[pw] += f
    top = lex.most_common(LEXICON_TOP)
    lexicon = [{'w': w, 'wt': round(math.log1p(f), 4)} for w, f in top]
    if verbose:
        print(f'  lexicon: {len(lexicon)} words '
              f'(top: {" ".join(w for w, _ in top[:8])})', flush=True)

    lm = {
        'meta': {
            'corpus': [label for _, label in CORPUS_FILES],
            'provenance': 'data/SHA256SUMS.txt; data/PROVENANCE-tocqueville.txt',
            'exclude_span': list(exclude_span) if exclude_span else None,
            'n_words': n_words_in,
            'n_distinct_words': len(wfreq),
            'n_proj_chars': n_chars,
            'alphabet': alpha,
            'ngram_order': NGRAM_ORDER,
            'heldout_per_char_logp': round(heldout_per_char, 4),
            'heldout_perplexity': round(math.exp(-heldout_per_char), 2),
            'lexicon_size': len(lexicon),
            'lexicon_minlen': LEXICON_MINLEN,
            'lexicon_top': LEXICON_TOP,
            'phonetics': 'solver/phonetics.py (project)',
            'built_at': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
            'register_caveat': 'formal 1835-1840 prose vs 1841 diplomatic '
                               'despatch; function words/morphology transfer, '
                               'content vocabulary does not',
        },
        # nested {ctx: {ch: count}} for orders 2..5; {ch: count} for order 1
        'counts': {},
        'lexicon': lexicon,
    }
    for order in range(1, NGRAM_ORDER + 1):
        c = counts[order]
        if order == 1:
            lm['counts']['1'] = dict(c)
        else:
            nest = {}
            for ng, n_ in c.items():
                nest.setdefault(ng[:-1], {})[ng[-1]] = n_
            lm['counts'][str(order)] = nest
    if verbose:
        print(f'build wall: {time.time()-t0:.1f}s', flush=True)
    return lm


def write_stats(lm, path):
    m = lm['meta']
    top_proj = collections.Counter()
    L = []
    A = L.append
    A('# LM build stats — Seebach homophonic solver')
    A('')
    A(f'- corpus: {"; ".join(m["corpus"])}')
    A(f'- exclude_span: {m["exclude_span"]}')
    A(f'- words: {m["n_words"]} (distinct {m["n_distinct_words"]})')
    A(f'- projected chars: {m["n_proj_chars"]}; alphabet ({len(m["alphabet"])}): '
      f'{"".join(m["alphabet"])}')
    A(f'- n-gram order: {m["ngram_order"]}')
    A(f'- held-out per-char logp: {m["heldout_per_char_logp"]} '
      f'(perplexity {m["heldout_perplexity"]})')
    A(f'- lexicon: {m["lexicon_size"]} words (minlen {m["lexicon_minlen"]}, '
      f'top {m["lexicon_top"]})')
    A(f'- built: {m["built_at"]}')
    A('')
    A('## Register caveat')
    A(m['register_caveat'])
    A('')
    A('## Top lexicon words (projected forms)')
    A(', '.join(f'{e["w"]}({e["wt"]})' for e in lm['lexicon'][:40]))
    with open(path, 'w') as f:
        f.write('\n'.join(L) + '\n')


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', required=True, help='output dir for lm.json')
    ap.add_argument('--exclude-span', nargs=2, type=int, default=None,
                    metavar=('A', 'B'),
                    help='exclude word indices [A,B) (control independence)')
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    lm = build(exclude_span=tuple(a.exclude_span) if a.exclude_span else None)
    with open(os.path.join(a.out, 'lm.json'), 'w') as f:
        json.dump(lm, f, ensure_ascii=False)
    write_stats(lm, os.path.join(a.out, 'lm_stats.md'))
    print(f'wrote {a.out}/lm.json + lm_stats.md')


if __name__ == '__main__':
    main()
