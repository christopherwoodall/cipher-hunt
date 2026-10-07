#!/usr/bin/env python3
"""Track A: build the register-matched (diplomatic) reference LM.

Construction is VERBATIM the frozen Tocqueville pipeline
(code/side-homophonic/solver/build_lm.py), with only the corpus source
changed. Differences (all pre-registered in ../PREREG.md, all deterministic):

  corpus      : 9 diplomatic files in code/side-period/corpus/
                (guizot-memoires-t5-t6, nesselrode v7/v8/v9/v10,
                 revue-deux-mondes-1841 q1/q2/q3/q4)
                enumerated with sha256 in PREREG.md
  exclude     : guizot word offsets [100000,104000) and [200000,204000)
                are REMOVED before any other step (reserved as Track-A
                instance truth plaintext; the reference must never see them)
  subsample   : deterministic shuffle (random.Random(184101)) of the
                concatenated, span-excluded word list; first 215000 words
                kept -- size-matched to Tocqueville's 214861 (isolates
                REGISTER from corpus SIZE)

Everything else (token regex, projection, spaceless stream, char 1..5-gram
nested counts, lexicon rule freq>=3 / proj-len>=4 / dedup freq-summed /
top-40000 / wt=log1p(freq), held-out perplexity on first-90% train /
last-10% test with order-5 alpha=0.5) is copied verbatim from build_lm.py.

Phonetics: the rebuild solver's phonetics.py is BYTE-IDENTICAL to the
frozen one (verified: diff empty, 2026-10-07), so the projection matches
the Tocqueville lm_ref build exactly.

Outputs: lm_ref_diplo/lm.json, lm_ref_diplo/lm_stats.md, and a sha256 of
lm.json printed at the end. Read-only wrt every other lane dir.
"""
import collections
import hashlib
import json
import math
import os
import random
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.abspath(os.path.join(HERE, '..', '..'))
REBUILD = os.path.join(LANE, 'side-homophonic-rebuild')
sys.path.insert(0, os.path.join(REBUILD, 'solver'))
from phonetics import project  # noqa: E402  (byte-identical to frozen)

CORPUS_DIR = os.path.join(HERE, '..', '..', 'side-period', 'corpus')
CORPUS_FILES = [
    'guizot-memoires-t5-t6.txt',
    'nesselrode-v7.txt',
    'nesselrode-v8.txt',
    'nesselrode-v9.txt',
    'nesselrode-v10.txt',
    'revue-deux-mondes-1841-q1.txt',
    'revue-deux-mondes-1841-q2.txt',
    'revue-deux-mondes-1841-q3.txt',
    'revue-deux-mondes-1841-q4.txt',
]

# Track-A instance truth spans (guizot word offsets), excluded from the build.
EXCLUDE_SPANS = [(100000, 104000), (200000, 204000)]
SHUFFLE_SEED = 184101
N_WORDS = 215000

NGRAM_ORDER = 5
LEXICON_MINLEN = 4
LEXICON_TOP = 40000
LEXICON_MINFREQ = 3
HELDOUT_FRAC = 0.10
WORD_RE = re.compile(r"[a-zàâäéèêëîïôöùûüÿçœæ]+")


def load_words():
    per_file = {}
    for fn in CORPUS_FILES:
        path = os.path.join(CORPUS_DIR, fn)
        txt = open(path, encoding='utf-8', errors='replace').read()
        m1 = re.search(r'\*\*\* START OF.*?\*\*\*', txt)
        m2 = re.search(r'\*\*\* END OF.*?\*\*\*', txt)
        body = txt[m1.end():m2.start()] if m1 and m2 else txt
        body = body.replace("'", ' ').replace('’', ' ')
        per_file[fn] = WORD_RE.findall(body.lower())
    # exclude Track-A instance-truth spans from guizot (by word offset)
    g = per_file['guizot-memoires-t5-t6.txt']
    keep = [w for i, w in enumerate(g)
            if not any(a <= i < b for a, b in EXCLUDE_SPANS)]
    print(f'guizot: {len(g)} words, {len(g)-len(keep)} excluded '
          f'(spans {EXCLUDE_SPANS})', flush=True)
    per_file['guizot-memoires-t5-t6.txt'] = keep
    words = []
    for fn in CORPUS_FILES:
        words.extend(per_file[fn])
        print(f'  {fn}: {len(per_file[fn])} words', flush=True)
    rng = random.Random(SHUFFLE_SEED)
    rng.shuffle(words)
    words = words[:N_WORDS]
    print(f'shuffled (seed {SHUFFLE_SEED}), kept {len(words)} words', flush=True)
    return words


def build(words, verbose=True):
    t0 = time.time()
    n_words_in = len(words)
    wfreq = collections.Counter(words)
    chars = [project(w) for w in words]
    stream = ''.join(chars)
    n_chars = len(stream)
    alpha = sorted(set(stream))
    if verbose:
        print(f'words={n_words_in} distinct={len(wfreq)} '
              f'proj_chars={n_chars} alphabet={len(alpha)}', flush=True)
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
    # held-out perplexity: identical to build_lm.py
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
    tr_tot = {}
    for o in range(2, NGRAM_ORDER + 1):
        t = collections.Counter()
        for ng, n_ in tr_counts[o].items():
            t[ng[:-1]] += n_
        tr_tot[o] = t
    tr_uni_tot = max(sum(tr_counts[1].values()), 1)

    def lp_heldout(ch, ctx):
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
    # word lexicon (projected) -- identical rule
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
            'corpus': CORPUS_FILES,
            'provenance': 'code/side-period/corpus/ (sha256 in '
                          'track-a/PREREG.md); les-mis-free scan: 0 shared '
                          'word-20-grams vs data/gutenberg-17489-'
                          'miserables1.txt',
            'exclude_span': [list(s) for s in EXCLUDE_SPANS],
            'subsample': {'method': 'deterministic shuffle',
                          'seed': SHUFFLE_SEED, 'n_words': N_WORDS},
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
            'phonetics': 'side-homophonic-rebuild/solver/phonetics.py '
                         '(byte-identical to frozen)',
            'built_at': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
            'register_caveat': '1840-42 diplomatic French (Guizot despatches, '
                               'Nesselrode correspondence, Revue des Deux '
                               'Mondes 1841). Register-MATCHED to the 1841 '
                               'diplomatic task; register-GAPPED from the '
                               'Les Mis 1862 control plaintext (deliberate: '
                               'Les Mis is sealed-truth text and off-limits '
                               'for training).',
        },
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
    L = []
    A = L.append
    A('# LM build stats — Seebach homophonic solver (Track A, register-matched)')
    A('')
    A(f'- corpus: {"; ".join(m["corpus"])}')
    A(f'- exclude_span: {m["exclude_span"]} (Track-A instance truth)')
    A(f'- subsample: {m["subsample"]}')
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
    A('## Register note')
    A(m['register_caveat'])
    A('')
    A('## Top lexicon words (projected forms)')
    A(', '.join(f'{e["w"]}({e["wt"]})' for e in lm['lexicon'][:40]))
    with open(path, 'w') as f:
        f.write('\n'.join(L) + '\n')


def main():
    out = os.path.join(HERE, 'lm_ref_diplo')
    os.makedirs(out, exist_ok=True)
    words = load_words()
    lm = build(words)
    lp = os.path.join(out, 'lm.json')
    json.dump(lm, open(lp, 'w'), ensure_ascii=False)
    write_stats(lm, os.path.join(out, 'lm_stats.md'))
    h = hashlib.sha256(open(lp, 'rb').read()).hexdigest()
    print(f'wrote {lp} sha256={h}')


if __name__ == '__main__':
    main()
