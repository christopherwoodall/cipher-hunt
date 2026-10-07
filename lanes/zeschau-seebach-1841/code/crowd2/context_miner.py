#!/usr/bin/env python3
"""
Crowd round 2 — THE CONTEXT MINER.
Work Order 3: exploit 64=qui (provisional, F9) + 87=ce (provisional).

(a) All FIVE 87->64 ("ce qui") contexts, +/-6 groups each:
    what precedes "ce", what follows "qui".
(b) Joint 87/64 windows (both present within +/-4 groups):
    other groups co-occurring >=2x => function-word candidates.
(c) 82->16 (11x total, 29% of 82's followers) vs qui-anchored windows:
    counts within +/-3 and +/-5 of 64 (and of 87 for comparison).
Era rates from data/gutenberg-30513/30514-tocqueville-t*.txt (Tocqueville
1835/1840, 214,861 words) -- NOT Les Mis (per F10 register ruling).

Deterministic. No invented ciphertext. Results ->
code/crowd2/context_miner_results.{md,json}
"""
import json, re, collections, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.join(HERE, '..', '..')
DATA = os.path.join(LANE, 'data')
sys.path.insert(0, os.path.join(LANE, 'code'))
from crib_attack import load_pairs

ANCHORS = {'11': 'la', '70': 'pre', '82': 'm', '34': 'i', '29': 'er',
           '40': 'e', '46': 'que', '87': 'ce', '64': 'qui'}


def load_tocqueville():
    words = []
    for fn in ('gutenberg-30513-tocqueville-t1.txt',
               'gutenberg-30514-tocqueville-t2.txt'):
        text = open(os.path.join(DATA, fn), encoding='utf-8').read().lower()
        words.extend(re.findall(r"[a-z\u00e0\u00e2\u00e4\u00e9\u00e8\u00ea\u00eb\u00ee\u00ef\u00f4\u00f6\u00f9\u00fb\u00fc\u00e7\u0153\u00e6]+", text))
    return words


def main():
    pairs, odd_lines, off1 = load_pairs()
    n = len(pairs)
    res = {'n_pairs': n}

    # ============ (a) the five 87->64 contexts ============
    cequi = [i for i in range(n - 1) if pairs[i] == '87' and pairs[i + 1] == '64']
    res['a_n_87_64'] = len(cequi)
    res['a_positions'] = cequi
    print(f"(a) 87->64 occurrences: {len(cequi)} (expect 5)")
    contexts = []
    fol64_in_ctx = collections.Counter()
    pre87_in_ctx = collections.Counter()
    for k, i in enumerate(cequi):
        lo, hi = max(0, i - 6), min(n, i + 8)
        win = pairs[lo:hi]
        annotated = [f"{g}={ANCHORS[g]}" if g in ANCHORS else g for g in win]
        ctx = {'occurrence': k + 1, 'pos': i,
               'window': ' '.join(win),
               'annotated': ' '.join(annotated)}
        # predecessor of 87 and up to 5 before
        pre = [pairs[j] for j in range(i - 1, i - 6, -1) if j >= 0]
        # followers of 64: up to 5 after
        fol = [pairs[j] for j in range(i + 2, i + 7) if j < n]
        ctx['pre_87'] = pre
        ctx['fol_64'] = fol
        contexts.append(ctx)
        if pre:
            pre87_in_ctx[pre[0]] += 1
        for f in fol:
            fol64_in_ctx[f] += 1
        print(f"  [{k+1}] pos {i}:")
        print(f"      {' '.join(win)}")
        print(f"      {' '.join(annotated)}")
    res['a_contexts'] = contexts
    res['a_pre87_immediate'] = dict(pre87_in_ctx)
    res['a_fol64_next5'] = dict(fol64_in_ctx)

    # followers of 64 globally vs in "ce qui" windows (for reference)
    fol64_all = collections.Counter(pairs[i + 1] for i in range(n - 1) if pairs[i] == '64')
    res['a_fol64_all'] = dict(fol64_all.most_common(12))

    # "24 ce qui" trigram: how often does 24 precede 87 overall?
    bigram_24_87 = sum(1 for i in range(n - 1)
                       if pairs[i] == '24' and pairs[i + 1] == '87')
    trigram_24_87_64 = sum(1 for i in range(n - 2)
                           if pairs[i] == '24' and pairs[i + 1] == '87'
                           and pairs[i + 2] == '64')
    freq = collections.Counter(pairs)
    ranked = sorted(freq.items(), key=lambda kv: -kv[1])
    rank24 = next(i for i, (g, _) in enumerate(ranked) if g == '24')
    res['a_bigram_24_87'] = bigram_24_87
    res['a_trigram_24_87_64'] = trigram_24_87_64
    res['a_freq_24'] = freq['24']
    res['a_rank_24'] = rank24
    # immediate follower of 64 within the five ce-qui contexts
    res['a_immediate_fol64_in_cequi'] = [pairs[i + 2] for i in cequi if i + 2 < n]
    print(f"  bigram 24->87: {bigram_24_87}, trigram 24->87->64: {trigram_24_87_64}, "
          f"freq(24)={freq['24']} rank(24)={rank24}")
    print(f"  immediate followers of 64 in the 5 ce-qui contexts: "
          f"{res['a_immediate_fol64_in_cequi']}")
    # predecessors of 87 globally
    pre87_all = collections.Counter(pairs[i - 1] for i in range(1, n) if pairs[i] == '87')
    res['a_pre87_all'] = dict(pre87_all.most_common(8))
    print(f"  predecessors of 87 globally: {pre87_all.most_common(8)}")

    # ============ (b) joint 87/64 windows ============
    # find index lists
    i87 = [i for i, g in enumerate(pairs) if g == '87']
    i64 = [i for i, g in enumerate(pairs) if g == '64']
    # joint events: an 87 and a 64 with |j-k| <= 4
    joint_events = []  # (j87, k64)
    for j in i87:
        for k in i64:
            if abs(j - k) <= 4 and j != k:
                joint_events.append((j, k))
    # dedupe: group into windows (a single window may contain several 87/64 pairs)
    joint_windows = []
    seen = set()
    for j, k in joint_events:
        lo, hi = max(0, min(j, k) - 4), min(n, max(j, k) + 5)
        key = (lo, hi)
        if key not in seen:
            seen.add(key)
            joint_windows.append((lo, hi, j, k))
    res['b_n_joint_events'] = len(joint_events)
    res['b_n_joint_windows'] = len(joint_windows)
    print(f"(b) joint 87/64 events (|d|<=4): {len(joint_events)}, "
          f"distinct windows: {len(joint_windows)}")
    co = collections.Counter()
    win_list = []
    for lo, hi, j, k in joint_windows:
        win = pairs[lo:hi]
        win_list.append({'lo': lo, 'hi': hi, 'i87': j, 'i64': k,
                         'window': ' '.join(win)})
        for idx in range(lo, hi):
            g = pairs[idx]
            if g not in ('87', '64'):
                co[g] += 1
        print(f"      [{lo}..{hi}] 87@{j} 64@{k}: {' '.join(win)}")
    res['b_joint_windows'] = win_list
    res['b_cooccur_ge2'] = {g: c for g, c in co.most_common() if c >= 2}
    print(f"  co-occurring groups >=2x: {res['b_cooccur_ge2']}")

    # ============ (c) 82->16 vs ce/qui windows ============
    bigrams_82_16 = [i for i in range(n - 1)
                     if pairs[i] == '82' and pairs[i + 1] == '16']
    res['c_total_82_16'] = len(bigrams_82_16)
    fol82_all = collections.Counter(pairs[i + 1] for i in range(n - 1) if pairs[i] == '82')
    res['c_fol82_all'] = dict(fol82_all.most_common(8))

    def dist_to_nearest(idx, targets):
        return min((abs(idx - t) for t in targets), default=None)

    def dist_to_nearest_strict(idx, targets):
        # distance measured in groups between the bigram's 82 slot and the target slot
        return min((abs(idx - t) for t in targets), default=None)

    c = {}
    for name, targets in (('87', i87), ('64', i64)):
        within3 = sum(1 for i in bigrams_82_16
                      if dist_to_nearest_strict(i, targets) is not None
                      and dist_to_nearest_strict(i, targets) <= 3)
        within5 = sum(1 for i in bigrams_82_16
                      if dist_to_nearest_strict(i, targets) is not None
                      and dist_to_nearest_strict(i, targets) <= 5)
        c[name] = {'within_3': within3, 'within_5': within5}
        # also distances distribution
        ds = sorted(d for d in
                    (dist_to_nearest_strict(i, targets) for i in bigrams_82_16)
                    if d is not None)
        c[name]['min_dists'] = ds
        print(f"(c) 82->16 within +/-3 of {name}: {within3}, +/-5: {within5}, "
              f"min dists: {ds[:6]}")
    res['c_near'] = c
    res['c_bigram_positions'] = bigrams_82_16
    # windows around the 82->16 bigrams nearest to a 64 (dist<=5)
    near64 = [i for i in bigrams_82_16
              if dist_to_nearest_strict(i, i64) is not None
              and dist_to_nearest_strict(i, i64) <= 5]
    res['c_windows_near64'] = [
        {'pos': i, 'window': ' '.join(pairs[max(0, i - 4):i + 6]),
         'annotated': ' '.join(
             f"{g}={ANCHORS[g]}" if g in ANCHORS else g
             for g in pairs[max(0, i - 4):i + 6])}
        for i in near64]
    for w in res['c_windows_near64']:
        print(f"  82->16 near 64 @ {w['pos']}: {w['annotated']}")
    # profile of 16 itself
    fol16 = collections.Counter(pairs[i + 1] for i in range(n - 1) if pairs[i] == '16')
    pre16 = collections.Counter(pairs[i - 1] for i in range(1, n) if pairs[i] == '16')
    res['c_fol16'] = dict(fol16.most_common(8))
    res['c_pre16'] = dict(pre16.most_common(8))
    res['c_freq_16'] = freq['16']
    print(f"  followers of 16: {fol16.most_common(8)}")
    print(f"  predecessors of 16: {pre16.most_common(8)}")

    # ============ era reference: what follows "ce qui" / "qui" in Tocqueville ============
    words = load_tocqueville()
    res['era_words'] = len(words)
    fol_ce_qui = collections.Counter()
    fol_qui = collections.Counter()
    pre_ce = collections.Counter()
    for i in range(len(words) - 2):
        if words[i] == 'ce' and words[i + 1] == 'qui':
            fol_ce_qui[words[i + 2]] += 1
    for i in range(len(words) - 1):
        if words[i] == 'qui':
            fol_qui[words[i + 1]] += 1
    for i in range(1, len(words)):
        if words[i] == 'ce':
            pre_ce[words[i - 1]] += 1
    res['era_fol_ce_qui'] = dict(fol_ce_qui.most_common(15))
    res['era_fol_qui'] = dict(fol_qui.most_common(15))
    res['era_pre_ce'] = dict(pre_ce.most_common(15))
    print(f"era corpus words: {len(words)}")
    print(f"era 'ce qui' -> top followers: {fol_ce_qui.most_common(12)}")
    print(f"era 'qui' -> top followers: {fol_qui.most_common(12)}")
    print(f"era '<w> ce' -> top predecessors: {pre_ce.most_common(12)}")

    # era: "qui erreur"? (does 29=er after 64 make sense?)
    qui_erreur = sum(1 for i in range(len(words) - 1)
                     if words[i] == 'qui' and words[i + 1].startswith('err'))
    ce_qui_erreur = sum(1 for i in range(len(words) - 2)
                        if words[i] == 'ce' and words[i + 1] == 'qui'
                        and words[i + 2].startswith('err'))
    res['era_qui_er_star'] = qui_erreur
    res['era_ce_qui_er_star'] = ce_qui_erreur
    print(f"era 'qui err*': {qui_erreur}, 'ce qui err*': {ce_qui_erreur}")

    # era: which words precede "ce", and "X ce qui" phrase rates
    n_ce = sum(1 for w in words if w == 'ce')
    phrase = {}
    for a, b, cc in (('tout', 'ce', 'qui'), ('de', 'ce', 'qui'),
                     ('est', 'ce', 'qui'), ('pour', 'ce', 'qui'),
                     ('sur', 'ce', 'qui'), ('par', 'ce', 'qui')):
        cnt = sum(1 for i in range(len(words) - 2)
                  if words[i] == a and words[i + 1] == b and words[i + 2] == cc)
        n_a_ce = sum(1 for i in range(len(words) - 1)
                     if words[i] == a and words[i + 1] == b)
        phrase[f"{a}_{b}_{cc}"] = {'count': cnt, 'n_a_b': n_a_ce,
                                   'p_qui_given_a_ce': round(cnt / n_a_ce, 4)
                                   if n_a_ce else None}
    res['era_X_ce_qui'] = phrase
    print(f"era X-ce-qui phrases: {phrase}")
    # era: "ce qui <w1> <w2> que" — does a que follow ce-qui within 2 words?
    n_ce_qui = sum(1 for i in range(len(words) - 1)
                   if words[i] == 'ce' and words[i + 1] == 'qui')
    ce_qui_q = sum(1 for i in range(len(words) - 3)
                   if words[i] == 'ce' and words[i + 1] == 'qui'
                   and words[i + 3] == 'que')
    ce_qui_v1q = sum(1 for i in range(len(words) - 4)
                     if words[i] == 'ce' and words[i + 1] == 'qui'
                     and words[i + 4] == 'que')
    res['era_ce_qui_que_within2'] = {'n_ce_qui': n_ce_qui,
                                     'que_at_+2': ce_qui_q,
                                     'que_at_+3': ce_qui_v1q}
    print(f"era ce-qui: n={n_ce_qui}, que 2 words later: {ce_qui_q}, "
          f"3 words later: {ce_qui_v1q}")

    # era unigram ranks + P(ce|X) for 24-candidate checks ("tout","est","de","a")
    uni = collections.Counter(words)
    era_rank = {}
    for i, (w, _) in enumerate(uni.most_common()):
        if w not in era_rank:
            era_rank[w] = i
    cand = {}
    for w in ('tout', 'est', 'de', 'a', 'ce', 'qui', 'que'):
        n_w = uni[w]
        n_w_ce = sum(1 for i in range(len(words) - 1)
                     if words[i] == w and words[i + 1] == 'ce')
        cand[w] = {'n': n_w, 'rank': era_rank.get(w),
                   'n_w_ce': n_w_ce,
                   'p_ce_given_w': round(n_w_ce / n_w, 4) if n_w else None}
    res['era_unigram_candidates'] = cand
    print(f"era candidates: {cand}")
    # era: what follows elided "m'" (tokenized as 'm' + next word)
    fol_m = collections.Counter()
    for i in range(len(words) - 1):
        if words[i] == 'm':
            fol_m[words[i + 1]] += 1
    res['era_fol_m'] = dict(fol_m.most_common(10))
    res['era_n_m'] = sum(fol_m.values())
    print(f"era m' -> : {fol_m.most_common(10)} (n={sum(fol_m.values())})")

    # anchors-only full decode of the five ce-qui windows for the md table
    json.dump(res, open(os.path.join(HERE, 'context_miner_results.json'), 'w'),
              indent=1, ensure_ascii=False)
    print("[done] wrote code/crowd2/context_miner_results.json")
    return res


if __name__ == '__main__':
    main()
