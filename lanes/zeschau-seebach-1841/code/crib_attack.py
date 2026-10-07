#!/usr/bin/env python3
"""
Attempt 1 — crib-anchored attack on the Zeschau/Seebach two-digit syllabary (R5005).

Anchors (from the erased pencil decipherment, Bourdeau 2026-09-21):
    11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que
Language of R5005: French.

Phase A: verify transcription (counts, crib presence, long repeats), profile groups.
Phase B: anchor-context profiling (what follows/precedes 46=que and 11=la).
Phase C: crib-anchored function-word drag — for each frequent unassigned group g and
         each candidate French function word w, decode +/-6-group windows with
         anchors+{g:w} and score with the French quadgram model. Rank by mean window
         score. A real assignment should produce windows that read as French.

Deterministic. No invented ciphertext. Results -> ../data/attempt1_results.json
"""
import json, math, re, collections, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, '..', 'data')

ANCHORS = {'11': 'la', '70': 'pre', '82': 'm', '34': 'i',
           '29': 'er', '40': 'e', '46': 'que'}

# French function words likely to appear as one or two syllable-groups.
CANDIDATES = ['le', 'les', 'de', 'des', 'du', 'un', 'une', 'et', 'est', 'ne',
              'ce', 'ces', 'se', 'il', 'ils', 'elle', 'nous', 'vous', 'je',
              'on', 'en', 'au', 'aux', 'dans', 'pour', 'par', 'sur', 'pas',
              'plus', 'tout', 'tous', 'toute', 'qui', 'que', 'dont', 'comme',
              'avec', 'sans', 'sous', 'entre', 'vers', 'chez', 'mais', 'ou',
              'donc', 'car', 'ni', 'mon', 'ma', 'mes', 'son', 'sa', 'ses',
              'notre', 'votre', 'leur', 'leurs', 'cette', 'ces', 'auxdits']


def load_pairs():
    """Load grouped transcription, applying upstream per-line offsets."""
    offsets = json.load(open(os.path.join(DATA, 'upstream-offsets.json')))
    pairs, odd_lines, off1 = [], 0, 0
    for line in open(os.path.join(DATA, 'upstream-ct_R5005.txt')):
        line = line.strip()
        if not line:
            continue
        lid, digits = line.split()
        digits = re.sub(r'\D', '', digits)
        if len(digits) % 2 == 1:
            odd_lines += 1
        off = offsets.get(lid, 0)
        if off == 1:
            off1 += 1
        d = digits[off:]
        for i in range(0, len(d) - 1, 2):
            pairs.append(d[i:i + 2])
    return pairs, odd_lines, off1


def load_quadgrams():
    q = json.load(open(os.path.join(DATA, 'french-quadgrams.json')))
    floor = q.pop('floor')
    q.pop('meta', None)
    return q, floor


def qscore(s, q, floor):
    s = re.sub(r'[^A-Z]', '', s.upper())
    if len(s) < 4:
        return float('-inf')
    tot, n = 0.0, 0
    for i in range(len(s) - 3):
        tot += q.get(s[i:i + 4], floor)
        n += 1
    return tot / n if n else float('-inf')


def decode_window(seq, table):
    return ''.join(table.get(g, '') for g in seq)


def main():
    pairs, odd_lines, off1 = load_pairs()
    q, floor = load_quadgrams()
    res = {}

    # ---- Phase A: verification & profiling ----
    n_digits = sum(1 for _ in pairs) * 2
    freq = collections.Counter(pairs)
    distinct = len(freq)
    res['phaseA'] = {
        'pairs': len(pairs),
        'digits_implied': n_digits,
        'distinct_groups': distinct,
        'odd_digit_lines': odd_lines,
        'lines_with_offset1': off1,
    }
    print(f"[A] pairs={len(pairs)} distinct_groups={distinct} "
          f"odd_digit_lines={odd_lines} offset1_lines={off1}")
    crib_freq = {g: freq.get(g, 0) for g in ANCHORS}
    ranked = sorted(freq.items(), key=lambda kv: -kv[1])
    crib_rank = {g: next((i for i, (gg, _) in enumerate(ranked) if gg == g), None)
                 for g in ANCHORS}
    res['phaseA']['crib_freq'] = crib_freq
    res['phaseA']['crib_rank'] = crib_rank
    print(f"[A] crib frequencies: {crib_freq}")
    print(f"[A] crib frequency ranks (0=top): {crib_rank}")
    print(f"[A] top-15 groups: {ranked[:15]}")
    res['phaseA']['top15'] = ranked[:15]

    # long repeats at pair level
    s_pairs = ' '.join(pairs)
    r1 = ['77', '78', '94', '82', '06']
    r2 = ['06', '77', '78', '18', '71', '10', '01']
    def count_seq(seq):
        c = 0
        for i in range(len(pairs) - len(seq) + 1):
            if pairs[i:i + len(seq)] == seq:
                c += 1
        return c
    c1, c2 = count_seq(r1), count_seq(r2)
    res['phaseA']['repeat_7778948206_count'] = c1
    res['phaseA']['repeat_06777818711001_count'] = c2
    print(f"[A] repeat 77 78 94 82 06 (7778948206): {c1} occurrences")
    print(f"[A] repeat 06 77 78 18 71 10 01 (06777818711001): {c2} occurrences")

    # index of coincidence of the group stream
    n = len(pairs)
    ic = sum(f * (f - 1) for f in freq.values()) / (n * (n - 1))
    res['phaseA']['group_IC'] = ic
    print(f"[A] group-stream IC = {ic:.4f} (flat random over 96 groups would be ~0.0104)")

    # ---- Phase B: anchor-context profiling ----
    def neighbours(anchor, direction=+1, top=10):
        c = collections.Counter()
        for i, g in enumerate(pairs):
            if g == anchor:
                j = i + direction
                if 0 <= j < len(pairs):
                    c[pairs[j]] += 1
        return c.most_common(top)

    res['phaseB'] = {
        'after_que_46': neighbours('46', +1),
        'after_la_11': neighbours('11', +1),
        'before_la_11': neighbours('11', -1),
        'after_m_82': neighbours('82', +1),
    }
    for k, v in res['phaseB'].items():
        print(f"[B] {k}: {v}")

    # contexts of the x5 repeat (does the surrounding text vary?)
    ctxs = []
    for i in range(len(pairs) - 5):
        if pairs[i:i + 5] == r1:
            ctxs.append(pairs[max(0, i - 4):i + 9])
    res['phaseB']['repeat1_contexts'] = [' '.join(c) for c in ctxs]
    print(f"[B] x5-repeat contexts ({len(ctxs)}):")
    for c in ctxs:
        print(f"     {' '.join(c)}")

    # ---- Phase C: crib-anchored function-word drag ----
    # candidate groups: top-40 frequent, excluding anchors
    cand_groups = [g for g, _ in ranked[:40] if g not in ANCHORS]
    occ = {g: [i for i, gg in enumerate(pairs) if gg == g] for g in cand_groups}
    results = []
    for g in cand_groups:
        idxs = occ[g][:400]  # cap occurrences for speed
        for w in CANDIDATES:
            if w in ANCHORS.values():
                continue
            table = dict(ANCHORS)
            table[g] = w
            tot, cnt = 0.0, 0
            best_win, best_sc = '', float('-inf')
            for p in idxs:
                win = pairs[max(0, p - 6):p + 7]
                dec = decode_window(win, table)
                sc = qscore(dec, q, floor)
                if sc == float('-inf'):
                    continue
                tot += sc
                cnt += 1
                if sc > best_sc:
                    best_sc, best_win = sc, dec
            if cnt:
                results.append((tot / cnt, g, w, freq[g], cnt, best_win, best_sc))
    results.sort(reverse=True)
    res['phaseC'] = [
        {'group': g, 'word': w, 'group_freq': f, 'windows': c,
         'mean_score': round(ms, 3), 'best_window': bw, 'best_window_score': round(bs, 3)}
        for ms, g, w, f, c, bw, bs in results[:25]
    ]
    print("[C] top-25 (group -> word) by mean window quadgram score:")
    for r in res['phaseC'][:15]:
        print(f"     {r['group']}({r['group_freq']}x) -> {r['word']:<8} "
              f"mean={r['mean_score']} best='{r['best_window']}'")

    # baseline: anchors-only windows (no candidate) for comparison
    base = []
    for g in cand_groups[:10]:
        idxs = occ[g][:200]
        tot, cnt = 0.0, 0
        for p in idxs:
            win = pairs[max(0, p - 6):p + 7]
            dec = decode_window(win, ANCHORS)
            sc = qscore(dec, q, floor)
            if sc != float('-inf'):
                tot += sc
                cnt += 1
        base.append(round(tot / cnt, 3) if cnt else None)
    res['phaseC_baseline_anchors_only'] = base
    print(f"[C] anchors-only baseline mean window scores (10 groups): {base}")

    with open(os.path.join(DATA, 'attempt1_results.json'), 'w') as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
    print("[done] wrote ../data/attempt1_results.json")


if __name__ == '__main__':
    main()
