#!/usr/bin/env python3
"""Pattern matcher re-drive on the F44 by-ear alphabet (crowd6/inventorist).

Instrument: for each segmenter cipher word (crowd3 STRUCT words, re-indexed
to the canonical 1,847-pair repaired parse), look up (n_groups, pattern) in
the by-ear subsequence index (build_index.py); filter by anchor-cell
consistency across 4 tiers; rank by era frequency.

Anchor statuses (round-5, red-team adjudicated):
  GT          11=la 70=pre 82=m 34=i 29=er 40=e 46=que   (pencil cribs)
  PROV-STRONG 87=ce 94=ne 96=par
  PROV        64=qui 67=veut 77=le
  LEAD        62=on 78=me 47=ce 52=pas|so|se 24=en
  06 = verb-stem-class (no cell string): NOT an anchor; proposals touching 06
       (or 94/52/78/47 polyvalent groups) are flagged per R4.
Polyvalent anchor readings: 52->{pas,so,se}, 94->{ne,en}, 78->{me,ver}.

Controls (run FIRST; proposals are void if these fail):
  C1 GT-full: cipher [70,82,34,29,40] (pre|m|i|er|e @1035-1039 / @755-759,
      5 GT anchors) must return "premiere" top-1 (whole-word by-ear match).
  C2 GT-tail: cipher [82,34,29,40] (m|i|er|e @1036-1039 / @756-759, 4 GT
      anchors) must return candidates incl. "premiere" (subsequence match --
      the old instrument's zero is the repaired failure).
  C3 anchor-preserving specificity: C2 with one anchor corrupted (82->99)
      must NOT return "premiere" (the instrument is anchor-driven, not
      frequency-driven).

Proposal bar (unchanged): unique survivor, or top freq >=2x next AND >=2
anchor-fixed positions. Every proposal needs >=2 independent checks.
The 12 killed words (N32/Ruling 2) are blocklisted and can never propose.
"""
import json
import os
import re
import collections

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
INVD = os.path.join(LANE, 'code', 'crowd6', 'inventorist')

# group -> (cell-string readings, status)
ANCHORS = {
    '11': (('la',), 'GT'), '70': (('pre',), 'GT'), '82': (('m',), 'GT'),
    '34': (('i',), 'GT'), '29': (('er',), 'GT'), '40': (('e',), 'GT'),
    '46': (('que',), 'GT'),
    '87': (('ce',), 'PROV-STRONG'), '94': (('ne', 'en'), 'PROV-STRONG'),
    '96': (('par',), 'PROV-STRONG'),
    '64': (('qui',), 'PROV'), '67': (('veut',), 'PROV'),
    '77': (('le',), 'PROV'),
    '62': (('on',), 'LEAD'), '78': (('me', 'ver'), 'LEAD'),
    '47': (('ce',), 'LEAD'), '52': (('pas', 'so', 'se'), 'LEAD'),
    '24': (('en',), 'LEAD'),
}
POLYVALENT_GROUPS = {'06', '94', '52', '78', '47'}  # R4 flag set

TIERS = [
    ('T0', {'GT'}),
    ('T1', {'GT', 'PROV-STRONG'}),
    ('T2', {'GT', 'PROV-STRONG', 'PROV'}),
    ('T3', {'GT', 'PROV-STRONG', 'PROV', 'LEAD'}),
]

# N32/Ruling 2: the 12 dead words — blocklisted, can never propose
BLOCKLIST = {'quiconque', 'morcela', 'laborieusement', 'outrepassé', 'envahi',
             'apercevrions', 'susquehanna', 'ancêtres', 'perfectionnement',
             'prévienne', 'nécessairement', 'pionnier'}


def pattern_of(seq):
    seen = {}
    out = []
    for x in seq:
        if x not in seen:
            seen[x] = len(seen)
        out.append(chr(65 + seen[x]))
    return ''.join(out)


def load_index():
    d = json.load(open(os.path.join(INVD, 'byear_index.json')))
    words = d['words']  # idx -> [word, freq]
    raw = d['index']  # "n|pat" -> [[widx, cells, start], ...]
    # entries_by_key[(n,pat)] = list of (widx, cells_tuple, start)
    entries_by_key = {}
    # inverted: inv[(n,pat,pos,cell)] = list of entry indices
    inv = collections.defaultdict(list)
    for key, entries in raw.items():
        n, pat = key.split('|')
        n = int(n)
        elist = []
        for widx, cells, start in entries:
            ct = tuple(cells)
            idx = len(elist)
            elist.append((widx, ct, start))
            for pos, cell in enumerate(ct):
                inv[(n, pat, pos, cell)].append(idx)
        entries_by_key[(n, pat)] = elist
    return d['meta'], words, entries_by_key, inv


def lookup(words, entries_by_key, inv, groups, tier_statuses):
    """Anchor-consistent candidates for a cipher group sequence (fast)."""
    n = len(groups)
    pat = pattern_of(groups)
    elist = entries_by_key.get((n, pat))
    if not elist:
        return [], {}
    anch = {}
    for i, g in enumerate(groups):
        if g in ANCHORS and ANCHORS[g][1] in tier_statuses:
            anch[i] = ANCHORS[g][0]
    if not anch:
        return [], {}
    # drive from the anchor with the fewest postings
    # for polyvalent anchors (multiple allowed cells), union the postings
    def postings(i):
        out = []
        for cell in anch[i]:
            out.extend(inv.get((n, pat, i, cell), []))
        return out
    order = sorted(anch, key=lambda i: len(postings(i)))
    cand = {}
    for idx in postings(order[0]):
        widx, cells, start = elist[idx]
        ok = True
        ev = []
        for i in anch:
            if cells[i] not in anch[i]:
                ok = False
                break
            ev.append((i, groups[i], cells[i], ANCHORS[groups[i]][1]))
        if not ok:
            continue
        w, freq = words[widx]
        prev = cand.get(w)
        if prev is None or freq > prev[0]:
            cand[w] = (freq, cells, start, ev)
    ranked = sorted(cand.items(), key=lambda kv: (-kv[1][0], kv[0]))
    return ranked, anch


def norm(w):
    import unicodedata
    w = unicodedata.normalize('NFD', w.lower())
    return ''.join(c for c in w if unicodedata.category(c) != 'Mn')


def run_control(words, entries_by_key, inv):
    """C1/C2/C3. Returns (pass_dict, detail)."""
    res = {}
    # C1: full "premiere" word [70,82,34,29,40], 5 GT anchors
    ranked, anch = lookup(words, entries_by_key, inv,
                          ['70', '82', '34', '29', '40'],
                          {'GT', 'PROV-STRONG', 'PROV', 'LEAD'})
    top = [w for w, _ in ranked[:5]]
    res['C1'] = {'pass': [norm(w) for w in top[:1]] == ['premiere'],
                 'top5': top,
                 'n_candidates': len(ranked)}
    # C2: tail [82,34,29,40], 4 GT anchors -- the old instrument's zero
    ranked2, anch2 = lookup(words, entries_by_key, inv,
                            ['82', '34', '29', '40'],
                            {'GT', 'PROV-STRONG', 'PROV', 'LEAD'})
    top2 = [w for w, _ in ranked2[:10]]
    res['C2'] = {'pass': 'premiere' in [norm(w) for w in top2],
                 'top10': top2,
                 'n_candidates': len(ranked2)}
    # C3: contradictory GT anchor (82->11='la'): 'premiere' must drop out.
    # (Corrupting to an UNANCHORED group merely removes the anchor -- not a
    # specificity test. A contradictory anchored group is.)
    ranked3, _ = lookup(words, entries_by_key, inv,
                        ['11', '34', '29', '40'],
                        {'GT', 'PROV-STRONG', 'PROV', 'LEAD'})
    top3 = [w for w, _ in ranked3[:10]]
    res['C3'] = {'pass': 'premiere' not in [norm(w) for w in top3],
                 'top10': top3,
                 'n_candidates': len(ranked3)}
    return res


def main():
    meta, words, entries_by_key, inv = load_index()
    print('[index]', meta['n_words'], 'words,', meta['n_keys'], 'keys; ',
          meta['alphabet'], flush=True)

    # ---- controls FIRST ----
    ctl = run_control(words, entries_by_key, inv)
    for c, r in ctl.items():
        print(f'[{c}] pass={r["pass"]} n={r["n_candidates"]} '
              f'top={r.get("top5", r.get("top10"))}', flush=True)
    with open(os.path.join(INVD, 'control.json'), 'w') as f:
        json.dump(ctl, f, ensure_ascii=False, indent=1)
    if not (ctl['C1']['pass'] and ctl['C2']['pass'] and ctl['C3']['pass']):
        print('[CONTROL FAIL] alphabet needs repair; no proposals will be made.')
        return

    print('[CONTROL PASS] proceeding to cipher-word sweep.')


if __name__ == '__main__':
    main()
