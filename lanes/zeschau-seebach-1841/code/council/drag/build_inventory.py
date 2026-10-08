#!/usr/bin/env python3
"""Build the systematic-drag phrase inventory (systematic-drag.md §1).

Clean pool (v8 VOID for phrase queries — OCR word-splits):
  CORE (diplomatic): nesselrode-v7/v9/v10, guizot-memoires-t5-t6, levant-1841-p3
  POOL+: + revue-deux-mondes q1-q4, metternich v4/v6, talleyrand v1, pozzo v1
Keep: n-gram (n=2..4) iff >=5x in CORE or >=25x in POOL; subsumption dedup;
rank by freq*log(1+core_freq); top 500. Then seed (regardless of frequency):
  formulae inventory + live cribs + 117 adjudicated crib cards (3 kills excluded).
Output: inventory.json [{phrase, tokens, freq, core_freq, variants:[{name, syls}]}]
"""
import json
import math
import os
import re
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import LANE, CORPUS, tok_elision, phrase_variants, norm

CORE_FILES = [
    'nesselrode-v7.txt', 'nesselrode-v9.txt', 'nesselrode-v10.txt',
    'guizot-memoires-t5-t6.txt', 'levant-correspondence-1841-p3.txt',
]
POOL_EXTRA = [
    'revue-deux-mondes-1841-q1.txt', 'revue-deux-mondes-1841-q2.txt',
    'revue-deux-mondes-1841-q3.txt', 'revue-deux-mondes-1841-q4.txt',
    'metternich-papiere-v4.txt', 'metternich-papiere-v6.txt',
    'talleyrand-memoires-v1.txt', 'pozzo-di-borgo-correspondance-v1.txt',
]
POOL_FILES = CORE_FILES + POOL_EXTRA

KILLED_CARDS = {
    'mon cher comte',
    'daignez, je vous prie, m\u2019indiquer la conduite que je dois suivre',
    'votre excellence vient de m\u2019adresser',
}
LIVE_CRIBS = ['Méhémet-Ali', 'parmi', 'même', 'par ce que',
              'la première fois', 'ne ment pas']

def load_tokens(fn):
    p = os.path.join(CORPUS, fn)
    if not os.path.exists(p):
        return []
    with open(p, encoding='utf-8', errors='replace') as f:
        return tok_elision(f.read())

def parse_formulae_inventory():
    """French forms from the formulae miner's markdown tables (first col)."""
    out = []
    p = os.path.join(LANE, 'code', 'french-blitz', 'formulae-inventory.md')
    for line in open(p, encoding='utf-8', errors='replace'):
        line = line.strip()
        if not line.startswith('|') or line.startswith('|---'):
            continue
        cells = [c.strip() for c in line.strip('|').split('|')]
        if not cells:
            continue
        head = cells[0]
        if head.lower().startswith('french form') or not head:
            continue
        # strip parenthetical glosses: "Votre dépêche du [date]" -> keep as is
        # (bracketed slots can't drag; drop phrases with [...] or …)
        if '[' in head or ']' in head or '…' in head:
            continue
        out.append(head)
    return out

def parse_crib_cards():
    """Surviving 117 adjudicated crib cards (crib column)."""
    out = []
    p = os.path.join(LANE, 'code', 'side-period', 'cribs-adjudicated.md')
    for line in open(p, encoding='utf-8', errors='replace'):
        line = line.strip()
        if not line.startswith('|') or line.startswith('|---'):
            continue
        cells = [c.strip() for c in line.strip('|').split('|')]
        if len(cells) < 2 or cells[0] == '#':
            continue
        crib = cells[1].strip('"“”')
        if not crib:
            continue
        low = crib.lower().replace('’', "'")
        if any(k in low for k in ('mon cher comte', 'daignez', 'vient de m\u2019adresser',
                                          'vient de m\'adresser')):
            continue
        out.append(crib)
    return out

def main():
    t0 = __import__('time').time()
    core_toks, pool_toks = [], []
    for fn in CORE_FILES:
        core_toks.extend(load_tokens(fn))
    for fn in POOL_FILES:
        pool_toks.extend(load_tokens(fn))
    print(f'core tokens: {len(core_toks)}, pool tokens: {len(pool_toks)}',
          flush=True)

    def ngrams(toks, n):
        return Counter(tuple(toks[i:i + n]) for i in range(len(toks) - n + 1))

    cand = {}  # phrase-tuple -> [pool_freq, core_freq]
    pc_by_n, cc_by_n = {}, {}
    for n in (2, 3, 4):
        pc, cc = ngrams(pool_toks, n), ngrams(core_toks, n)
        pc_by_n[n], cc_by_n[n] = pc, cc
        for ph, f in pc.items():
            cf = cc.get(ph, 0)
            if f >= 25 or cf >= 5:
                # drop phrases that are pure punctuation/empty or single-char heavy
                toks = list(ph)
                if any(len(t) == 0 for t in toks):
                    continue
                cand[ph] = [f, cf]
    print(f'raw candidates (2-4g): {len(cand)}', flush=True)

    # subsumption dedup: bigram B contiguous-subseq of trigram T (or 3g of 4g),
    # freq(B) < 1.5*freq(T) -> drop B. Indexed (not O(n^2)).
    by_len = {2: [], 3: [], 4: []}
    for ph in cand:
        by_len[len(ph)].append(ph)
    drop = set()
    for n in (2, 3):
        # index: sub-phrase -> max freq of a super-phrase containing it
        sup_max = {}
        for q in by_len[n + 1]:
            fq = cand[q][0]
            for i in range(len(q) - n + 1):
                sub = q[i:i + n]
                if sup_max.get(sub, 0) < fq:
                    sup_max[sub] = fq
        for ph in by_len[n]:
            if ph in sup_max and cand[ph][0] < 1.5 * sup_max[ph]:
                drop.add(ph)
    kept = {ph: v for ph, v in cand.items() if ph not in drop}
    print(f'after subsumption: {len(kept)} (dropped {len(drop)})', flush=True)

    ranked = sorted(kept.items(),
                    key=lambda kv: kv[1][0] * math.log(1 + kv[1][1]),
                    reverse=True)
    top = ranked[:500]
    print(f'top n-gram phrases: {len(top)}', flush=True)

    inv = []
    seen_phrases = set()
    for ph, (f, cf) in top:
        phrase = ' '.join(ph)
        seen_phrases.add(norm(phrase))
        inv.append({'phrase': phrase, 'tokens': list(ph),
                    'freq': f, 'core_freq': cf, 'source': 'ngram'})

    # seeds (regardless of frequency)
    seeds = []
    seeds += [(s, 'formulae') for s in parse_formulae_inventory()]
    seeds += [(s, 'live-crib') for s in LIVE_CRIBS]
    seeds += [(s, 'crib-card') for s in parse_crib_cards()]
    n_new = 0
    for s, src in seeds:
        toks = tok_elision(s)
        if not toks:
            continue
        key = norm(' '.join(toks))
        if key in seen_phrases:
            continue
        seen_phrases.add(key)
        # corpus freq for hit ranking: O(1) lookup in the n-gram counters
        n_t = len(toks)
        if 2 <= n_t <= 4:
            f = pc_by_n[n_t].get(tuple(toks), 0)
        else:
            f = 0
        inv.append({'phrase': s, 'tokens': toks, 'freq': f,
                    'core_freq': 0, 'source': src})
        n_new += 1
    print(f'seed phrases added: {n_new} (total inventory: {len(inv)})', flush=True)

    # syllabify variants
    for e in inv:
        e['variants'] = [{'name': n_, 'syls': s}
                         for n_, s in phrase_variants(e['tokens'])]
    n_v = sum(len(e['variants']) for e in inv)
    print(f'total variants: {n_v}', flush=True)

    outp = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        'inventory.json')
    with open(outp, 'w') as f:
        json.dump({'meta': {'n_phrases': len(inv), 'n_variants': n_v,
                            'core_files': CORE_FILES, 'pool_files': POOL_FILES},
                   'phrases': inv}, f, ensure_ascii=False)
    print(f'wrote {outp} in {__import__("time").time()-t0:.1f}s', flush=True)

if __name__ == '__main__':
    main()
