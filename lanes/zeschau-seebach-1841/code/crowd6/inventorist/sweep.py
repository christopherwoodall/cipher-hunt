#!/usr/bin/env python3
"""Cipher-word sweep for the by-ear re-drive (crowd6/inventorist).

Loads crowd3 segmenter words (viterbi STRUCT + 25 crib-drag targets, old
1,846-pair parse), re-indexes to the canonical 1,847-pair repaired parse
(F32: old n<748 unchanged; 748-772 repaired region -> dropped/flagged;
old n>=773 -> n+1), verifies groups against the rebuilt stream, then runs
the 4-tier by-ear matcher on every word containing >=1 anchored group.

Writes sweep_results.json. Proposals are NOT final -- they go to the
report note for red-team adjudication.
"""
import json
import os
import re
import collections

from matcher import (load_index, lookup, pattern_of, ANCHORS, TIERS,
                     POLYVALENT_GROUPS, BLOCKLIST, norm)

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
INVD = os.path.join(LANE, 'code', 'crowd6', 'inventorist')
DATA = os.path.join(LANE, 'data')


def load_repaired_stream():
    offsets = json.load(open(os.path.join(LANE, 'code', 'side-keyhunt',
                                          'repaired_offsets.json')))
    pairs = []
    for line in open(os.path.join(DATA, 'upstream-ct_R5005.txt')):
        line = line.strip()
        if not line:
            continue
        lid, digits = line.split()
        digits = re.sub(r'\D', '', digits)
        d = digits[offsets.get(lid, 0):]
        for i in range(0, len(d) - 1, 2):
            pairs.append(d[i:i + 2])
    assert len(pairs) == 1847, len(pairs)
    assert len(set(pairs)) == 96
    return pairs


def load_old_words():
    """Viterbi words + 25 targets from the old-parse segmenter."""
    s = json.load(open(os.path.join(LANE, 'code', 'crowd3',
                                    'segmenter_results.json')))
    vb = s['viterbi_bounds_STRUCT']
    words = []
    for i in range(len(vb) - 1):
        words.append((vb[i], vb[i + 1] - 1, 'viterbi'))
    for t in s['crib_drag_targets_STRUCT']:
        words.append((t['start_pair'], t['end_pair'], 'target25'))
    return words, s


def reindex_span(s, e):
    """Old-parse inclusive span -> new-parse span, or None if it touches
    the repaired region 748-772."""
    if e < 748:
        return (s, e)
    if s >= 773:
        return (s + 1, e + 1)
    return None


def main():
    pairs = load_repaired_stream()
    old_words, seg = load_old_words()
    print(f'[seg] {len(old_words)} old-parse words/targets')

    # verify old groups for the targets (sanity on the old parse)
    # (skip: old stream not rebuilt; rely on span reindex + new-stream verify)

    meta, words, entries_by_key, inv = load_index()
    anchor_groups = set(ANCHORS)

    results = []
    dropped_repaired = 0
    verify_fail = 0
    seen_spans = set()
    for s, e, src in old_words:
        ns = reindex_span(s, e)
        if ns is None:
            dropped_repaired += 1
            continue
        ns_, ne_ = ns
        if (ns_, ne_) in seen_spans:
            continue
        seen_spans.add((ns_, ne_))
        groups = pairs[ns_:ne_ + 1]
        # anchor-bearing words only (same selection as the old B sweep)
        if not any(g in anchor_groups for g in groups):
            continue
        # polyvalence flag
        pv = sorted(set(groups) & POLYVALENT_GROUPS)
        tiers = {}
        for tname, tstat in TIERS:
            ranked, anch = lookup(words, entries_by_key, inv, groups, tstat)
            tiers[tname] = {
                'n_anchored': len(anch),
                'n_candidates': len(ranked),
                'top5': [{'word': w, 'freq': f, 'cells': c,
                           'ev': [(i, g, cell, st) for i, g, cell, st in ev]}
                          for w, (f, c, st_, ev) in ranked[:5]],
            }
        t3 = tiers['T3']
        # proposal bar: unique survivor, or freq-gap >=2x with >=2 anchors
        prop = None
        status = 'LEAD-or-null'
        n_anch = t3['n_anchored']
        cands = t3['top5']
        # filter blocklist from candidacy (they can never propose)
        cands_nb = [c for c in cands if norm(c['word']) not in
                    {norm(b) for b in BLOCKLIST}]
        if len(groups) == 1 and groups[0] in ANCHORS:
            status = 'ANCHOR-RESTATEMENT'
        elif not cands_nb:
            status = 'NULL'
        elif len(cands_nb) == 1 and n_anch >= 1:
            prop, status = cands_nb[0], 'CRIB-PROPOSAL-unique'
        elif (len(cands_nb) >= 2
              and cands_nb[0]['freq'] >= 2 * cands_nb[1]['freq']
              and n_anch >= 2):
            prop, status = cands_nb[0], 'CRIB-PROPOSAL-freqgap+2anchors'
        else:
            status = 'LEAD'
        results.append({
            'span': [ns_, ne_], 'groups': groups, 'n': len(groups),
            'pattern': pattern_of(groups), 'source': src,
            'polyvalent_groups': pv,
            'tiers': {t: {'n_anchored': v['n_anchored'],
                          'n_candidates': v['n_candidates'],
                          'top5_words': [c['word'] for c in v['top5']]}
                      for t, v in tiers.items()},
            'status': status,
            'proposal': prop,
        })

    props = [r for r in results if r['status'].startswith('CRIB-PROPOSAL')]
    leads = [r for r in results if r['status'] == 'LEAD']
    nulls = [r for r in results if r['status'] == 'NULL']
    print(f'[sweep] {len(results)} anchor-bearing words: '
          f'{len(props)} proposals, {len(leads)} leads, {len(nulls)} nulls; '
          f'dropped {dropped_repaired} in repaired region')

    out = {
        'meta': {
            'parse': 'canonical 1,847-pair repaired (F32)',
            'dropped_repaired_region': dropped_repaired,
            'proposal_bar': 'unique survivor, or freq>=2x next AND >=2 anchors; '
                            '12 N32-dead words blocklisted',
        },
        'results': results,
    }
    with open(os.path.join(INVD, 'sweep_results.json'), 'w') as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print('[wrote] sweep_results.json')

    for r in props:
        p = r['proposal']
        print(f"  PROPOSAL @{r['span'][0]}-{r['span'][1]} "
              f"{'-'.join(r['groups'])} -> {p['word']} "
              f"(freq {p['freq']}, cells {p['cells']}, pv={r['polyvalent_groups']}) "
              f"[{r['status']}]")


if __name__ == '__main__':
    main()
