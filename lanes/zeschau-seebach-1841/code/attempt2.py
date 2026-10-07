#!/usr/bin/env python3
"""
Attempt 2 — test the two bigram leads from attempt 1 as anchor hypotheses.

H1: 82=m -> 16 (11/38, 29%). Candidate readings: 16 = vowel letter (a? -> "ma"),
    or a frequent syllable. Independent checks:
    (a) frequency rank of 16 vs French vowel-letter expectations
        (attempt 1: 34=i rank 70, 40=e rank 36; French letter order e > a > i),
    (b) predecessor distribution of 16 (is 82 dominant?),
    (c) 82->34 ("mi") and 82->40 ("me") control counts — if the syllabary
        spells ma/mi/me with letters, all three should be elevated,
    (d) Les Mis reference: P(next-letter | m) in real French.
H2: 87 -> 11=la (7/44, 15.9%). Candidate readings: 87 = de / a` / ce ("cela").
    Independent checks:
    (a) frequency rank of 87 (de should be top-5),
    (b) 87->46 count (de/à never precede "que"),
    (c) Les Mis reference: P("la" | "de") and P("la" | "a`") vs 15.9%,
    (d) predecessor distribution of 87.

Verdict rule (transparent, rule-based):
    CONFIRMED  = >=2 independent checks pass  -> may join the drag as a
                 *provisional* anchor (still labeled hypothesis).
    PLAUSIBLE  = exactly 1 check passes.
    otherwise  = INCONCLUSIVE (or REFUTED if a check actively contradicts).
If CONFIRMED, re-run the Phase-C function-word drag with the denser anchor
set and report whether it is still degenerate.

Deterministic. No invented ciphertext. Results -> ../data/attempt2_results.json
"""
import json, math, re, collections, os, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, '..', 'data')
import sys
sys.path.insert(0, HERE)
from crib_attack import load_pairs, ANCHORS, load_quadgrams, qscore, decode_window

LES_MIS_SRC = os.path.expanduser(
    '~/workspace/cipher-hunt/lanes/catherine-medici-1567/data/gutenberg-17489-miserables1.txt')
LES_MIS_LOCAL = os.path.join(DATA, 'gutenberg-17489-miserables1.txt')


def ensure_les_mis():
    """Lane-local copy of the French reference text, with provenance."""
    if not os.path.exists(LES_MIS_LOCAL):
        shutil.copyfile(LES_MIS_SRC, LES_MIS_LOCAL)
    return LES_MIS_LOCAL


def french_reference():
    """Word and letter statistics from Les Miserables Tome 1 (French prose)."""
    path = ensure_les_mis()
    text = open(path, encoding='utf-8', errors='replace').read().lower()
    m = re.search(r'\*\*\* start of.*?\*\*\*', text)
    if m:
        text = text[m.end():]
    m = re.search(r'\*\*\* end of.*', text)
    if m:
        text = text[:m.start()]
    words = re.findall(r"[a-zàâäéèêëîïôöùûüÿç]+", text)
    n_de = sum(1 for w in words if w == 'de')
    n_de_la = sum(1 for a, b in zip(words, words[1:]) if a == 'de' and b == 'la')
    n_a = sum(1 for w in words if w in ('à', 'a'))
    n_a_la = sum(1 for a, b in zip(words, words[1:]) if a in ('à', 'a') and b == 'la')
    n_ce = sum(1 for w in words if w == 'ce')
    n_cela = sum(1 for w in words if w == 'cela')
    n_ce_que = sum(1 for a, b in zip(words, words[1:]) if a == 'ce' and b == 'que')
    # letter-level: what follows 'm' inside words
    after_m = collections.Counter()
    n_m = 0
    for w in words:
        for i, ch in enumerate(w):
            if ch == 'm':
                n_m += 1
                after_m[w[i + 1] if i + 1 < len(w) else '#'] += 1
    letters = collections.Counter(''.join(words))
    return {
        'words': len(words),
        'p_la_given_de': n_de_la / n_de if n_de else None,
        'n_de': n_de, 'n_de_la': n_de_la,
        'p_la_given_a': n_a_la / n_a if n_a else None,
        'n_a': n_a, 'n_a_la': n_a_la,
        'p_cela_given_ce': n_cela / n_ce if n_ce else None,
        'n_ce': n_ce, 'n_cela': n_cela,
        'p_que_given_ce': n_ce_que / n_ce if n_ce else None,
        'n_ce_que': n_ce_que,
        'p_next_given_m': {k: round(v / n_m, 4) for k, v in after_m.most_common(12)},
        'n_m': n_m,
        'top_letters': letters.most_common(10),
    }


def rank_of(g, ranked):
    return next((i for i, (gg, _) in enumerate(ranked) if gg == g), None)


def neighbours(pairs, anchor, direction=+1):
    c = collections.Counter()
    for i, g in enumerate(pairs):
        if g == anchor:
            j = i + direction
            if 0 <= j < len(pairs):
                c[pairs[j]] += 1
    return c


def contexts(pairs, seq, width=3):
    out = []
    L = len(seq)
    for i in range(len(pairs) - L + 1):
        if pairs[i:i + L] == seq:
            out.append(' '.join(pairs[max(0, i - width):i + L + width]))
    return out


def main():
    pairs, _, _ = load_pairs()
    freq = collections.Counter(pairs)
    ranked = sorted(freq.items(), key=lambda kv: -kv[1])
    res = {'anchors': ANCHORS}

    # ---------------- H1: 82=m -> 16 ----------------
    h1 = {}
    n82 = freq['82']
    fol82 = neighbours(pairs, '82', +1)
    h1['n_82'] = n82
    h1['followers_82_top12'] = fol82.most_common(12)
    h1['p_16_given_82'] = round(fol82['16'] / n82, 4)
    h1['count_82_34_mi'] = fol82['34']
    h1['count_82_40_me'] = fol82['40']
    h1['count_82_06'] = fol82['06']
    h1['rank_16'] = rank_of('16', ranked)
    h1['freq_16'] = freq['16']
    pre16 = neighbours(pairs, '16', -1)
    fol16 = neighbours(pairs, '16', +1)
    h1['predecessors_16_top12'] = pre16.most_common(12)
    h1['followers_16_top12'] = fol16.most_common(12)
    h1['p_82_given_16'] = round(pre16['82'] / freq['16'], 4)
    h1['contexts_82_16'] = contexts(pairs, ['82', '16'])
    res['H1_82_to_16'] = h1
    print("[H1] 82=m occurs %dx; followers: %s" % (n82, fol82.most_common(8)))
    print("[H1] 16: freq=%d rank=%d (0-based); P(82|16)=%.3f"
          % (freq['16'], h1['rank_16'], h1['p_82_given_16']))
    print("[H1] 82->34 (mi)=%d  82->40 (me)=%d  82->06=%d"
          % (h1['count_82_34_mi'], h1['count_82_40_me'], h1['count_82_06']))
    print("[H1] predecessors of 16: %s" % pre16.most_common(8))

    # ---------------- H2: 87 -> 11=la ----------------
    h2 = {}
    n87 = freq['87']
    fol87 = neighbours(pairs, '87', +1)
    pre87 = neighbours(pairs, '87', -1)
    h2['n_87'] = n87
    h2['rank_87'] = rank_of('87', ranked)
    h2['freq_87'] = n87
    h2['followers_87_top15'] = fol87.most_common(15)
    h2['p_11_given_87'] = round(fol87['11'] / n87, 4)
    h2['count_87_46_que'] = fol87['46']
    h2['count_87_29_er'] = fol87['29']
    h2['count_87_34_i'] = fol87['34']
    h2['count_87_70_pre'] = fol87['70']
    h2['count_87_40_e'] = fol87['40']
    h2['predecessors_87_top12'] = pre87.most_common(12)
    h2['contexts_87_11'] = contexts(pairs, ['87', '11'], width=4)
    # what follows 11 in the 87->11 cases
    after = []
    for i in range(len(pairs) - 2):
        if pairs[i] == '87' and pairs[i + 1] == '11':
            after.append(pairs[i + 2] if i + 2 < len(pairs) else None)
    h2['group_after_11_in_87_11_cases'] = collections.Counter(after).most_common()
    res['H2_87_to_11'] = h2
    print("[H2] 87: freq=%d rank=%d (0-based); P(11|87)=%.3f"
          % (n87, h2['rank_87'], h2['p_11_given_87']))
    print("[H2] followers of 87: %s" % fol87.most_common(10))
    print("[H2] 87->46(que)=%d  87->29(er)=%d  87->34(i)=%d  87->70(pre)=%d  87->40(e)=%d"
          % (h2['count_87_46_que'], h2['count_87_29_er'], h2['count_87_34_i'],
             h2['count_87_70_pre'], h2['count_87_40_e']))

    # ---------------- French reference ----------------
    ref = french_reference()
    res['french_reference'] = ref
    print("[FR] words=%d  P(la|de)=%.4f (%d/%d)  P(la|a`)=%.4f (%d/%d)"
          % (ref['words'], ref['p_la_given_de'], ref['n_de_la'], ref['n_de'],
             ref['p_la_given_a'], ref['n_a_la'], ref['n_a']))
    print("[FR] P(next|m) in French words: %s" % ref['p_next_given_m'])
    print("[FR] top letters: %s" % ref['top_letters'])

    # ---------------- verdicts (rule-based, transparent) ----------------
    v1, why1 = [], []
    # H1 check (a): rank of 16 vs vowel expectations (e rank 36, i rank 70)
    r16 = h1['rank_16']
    if r16 is not None and r16 <= 70:
        v1.append(True); why1.append("rank(16)=%d in vowel-letter band (e:36, i:70)" % r16)
    else:
        v1.append(False); why1.append("rank(16)=%s outside vowel band" % r16)
    # H1 check (b): 82 dominates predecessors of 16
    if h1['p_82_given_16'] >= 0.5:
        v1.append(True); why1.append("P(82|16)=%.2f >= 0.5, 16 bound to m" % h1['p_82_given_16'])
    else:
        v1.append(False); why1.append("P(82|16)=%.2f < 0.5, 16 not bound to m" % h1['p_82_given_16'])
    # H1 check (c): mi/me controls elevated like ma
    mi_me = h1['count_82_34_mi'] + h1['count_82_40_me']
    if mi_me >= 4:
        v1.append(True); why1.append("82->34/40 (mi/me) total %d, letter-spelling pattern" % mi_me)
    else:
        v1.append(False); why1.append("82->34/40 (mi/me) total %d, no letter-spelling pattern" % mi_me)
    # H1 check (d): Les Mis P(a|m) dominant
    pm = ref['p_next_given_m']
    if pm.get('a', 0) >= 0.20:
        v1.append(True); why1.append("Les Mis P(a|m)=%.2f dominant" % pm.get('a', 0))
    else:
        v1.append(False); why1.append("Les Mis P(a|m)=%.2f not dominant" % pm.get('a', 0))
    s1 = sum(v1)
    verdict1 = 'CONFIRMED' if s1 >= 2 else ('PLAUSIBLE' if s1 == 1 else 'INCONCLUSIVE')
    res['verdict_H1'] = {'verdict': verdict1, 'checks_passed': s1, 'of': 4, 'reasons': why1}
    print("[V1] H1 (82->16): %s (%d/4): %s" % (verdict1, s1, '; '.join(why1)))

    v2, why2 = [], []
    # H2 check (a): rank of 87 in top-8 (de-calibre)
    r87 = h2['rank_87']
    if r87 is not None and r87 < 8:
        v2.append(True); why2.append("rank(87)=%d, de-calibre frequency" % r87)
    else:
        v2.append(False); why2.append("rank(87)=%s, below de-calibre" % r87)
    # H2 check (b): 87->46(que) ~ 0
    if h2['count_87_46_que'] == 0:
        v2.append(True); why2.append("87->que = 0, consistent with de/a`")
    else:
        v2.append(False); why2.append("87->que = %d, against de/a`" % h2['count_87_46_que'])
    # H2 check (c): observed P(11|87) within factor 2 of Les Mis P(la|de) or P(la|a`)
    obs = h2['p_11_given_87']
    ok_c = any(p and 0.5 * p <= obs <= 2.0 * p
               for p in (ref['p_la_given_de'], ref['p_la_given_a']))
    if ok_c:
        v2.append(True); why2.append("P(11|87)=%.3f matches Les Mis de-la/a`-la rate" % obs)
    else:
        v2.append(False); why2.append("P(11|87)=%.3f vs Les Mis de:%.3f a`:%.3f"
                                     % (obs, ref['p_la_given_de'], ref['p_la_given_a']))
    # H2 check (d): predecessors of 87 diverse (function word, not bound stem)
    n_pre = len(pre87)
    if n_pre >= 8:
        v2.append(True); why2.append("%d distinct predecessors, free function word" % n_pre)
    else:
        v2.append(False); why2.append("only %d distinct predecessors" % n_pre)
    s2 = sum(v2)
    verdict2 = 'CONFIRMED' if s2 >= 2 else ('PLAUSIBLE' if s2 == 1 else 'INCONCLUSIVE')
    # check (b) is not just a miss: 87->que=3 actively contradicts de/a`
    # ("de que" / "a` que" are ungrammatical in French), so de/a` is REFUTED
    # even though two weaker checks passed.
    if h2['count_87_46_que'] >= 2:
        verdict2 = 'REFUTED'
        why2.append("OVERRIDE: 87->que=%d contradicts de/a` -> REFUTED"
                    % h2['count_87_46_que'])
    res['verdict_H2'] = {'verdict': verdict2, 'checks_passed': s2, 'of': 4, 'reasons': why2}
    print("[V2] H2 (87->11 as de/a`): %s (%d/4): %s" % (verdict2, s2, '; '.join(why2)))

    # ---------------- H2b: 87 = ce ("cela", "ce que") ----------------
    # The 87->que hits that refute de/a` are exactly what "ce" predicts.
    h2b = {}
    tri_24_87_46 = sum(1 for i in range(len(pairs) - 2)
                       if pairs[i] == '24' and pairs[i + 1] == '87'
                       and pairs[i + 2] == '46')
    h2b['trigram_24_87_46_count'] = tri_24_87_46  # "est-ce que" if 24=est, 87=ce
    v2b, why2b = [], []
    if r87 is not None and r87 < 25:
        v2b.append(True); why2b.append("rank(87)=%d, common-word band" % r87)
    else:
        v2b.append(False); why2b.append("rank(87)=%s too rare for ce" % r87)
    obs_cela = h2['p_11_given_87']
    p_cela = ref['p_cela_given_ce']
    if p_cela and 0.5 * p_cela <= obs_cela <= 2.0 * p_cela:
        v2b.append(True); why2b.append("P(11|87)=%.3f ~= Les Mis P(cela|ce)=%.3f"
                                       % (obs_cela, p_cela))
    else:
        v2b.append(False); why2b.append("P(11|87)=%.3f vs Les Mis P(cela|ce)=%.3f"
                                        % (obs_cela, p_cela))
    obs_que = h2['count_87_46_que'] / n87
    p_que = ref['p_que_given_ce']
    if p_que and 0.5 * p_que <= obs_que <= 2.0 * p_que:
        v2b.append(True); why2b.append("P(que|87)=%.3f ~= Les Mis P(que|ce)=%.3f"
                                       % (obs_que, p_que))
    else:
        v2b.append(False); why2b.append("P(que|87)=%.3f vs Les Mis P(que|ce)=%.3f"
                                        % (obs_que, p_que))
    if tri_24_87_46 >= 2:
        v2b.append(True); why2b.append("24-87-46 trigram x%d ('est-ce que' shape)"
                                       % tri_24_87_46)
    else:
        v2b.append(False); why2b.append("24-87-46 trigram x%d" % tri_24_87_46)
    if len(pre87) >= 8:
        v2b.append(True); why2b.append("%d distinct predecessors" % len(pre87))
    else:
        v2b.append(False); why2b.append("only %d distinct predecessors" % len(pre87))
    s2b = sum(v2b)
    verdict2b = 'CONFIRMED' if s2b >= 2 else ('PLAUSIBLE' if s2b == 1 else 'INCONCLUSIVE')
    res['verdict_H2b_ce'] = {'verdict': verdict2b, 'checks_passed': s2b, 'of': 5,
                             'reasons': why2b, 'trigram_24_87_46': tri_24_87_46}
    print("[V2b] H2b (87=ce): %s (%d/5): %s" % (verdict2b, s2b, '; '.join(why2b)))

    # ---------------- conditional drag re-run ----------------
    res['drag_rerun'] = None
    prov = {}
    if verdict1 == 'CONFIRMED':
        # provisional reading for 16: most defensible single-letter value is 'a'
        prov['16'] = 'a'
    if verdict2b == 'CONFIRMED':
        # provisional reading for 87: 'ce' ("cela" and "ce que" both attested)
        prov['87'] = 'ce'
    if prov:
        q, floor = load_quadgrams()
        table = dict(ANCHORS)
        table.update(prov)
        cand = [g for g, _ in ranked[:40] if g not in table]
        occ = {g: [i for i, gg in enumerate(pairs) if gg == g] for g in cand}
        cands_words = ['le', 'les', 'de', 'des', 'du', 'un', 'une', 'et', 'est',
                        'ne', 'ce', 'ces', 'se', 'il', 'ils', 'elle', 'nous',
                        'vous', 'je', 'on', 'en', 'au', 'aux', 'dans', 'pour',
                        'par', 'sur', 'pas', 'plus', 'tout', 'tous', 'toute',
                        'qui', 'dont', 'comme', 'avec', 'sans', 'mais', 'ou',
                        'mon', 'ma', 'mes', 'son', 'sa', 'ses', 'notre',
                        'votre', 'leur', 'cette']
        out = []
        for g in cand:
            for w in cands_words:
                if w in table.values():
                    continue
                t2 = dict(table)
                t2[g] = w
                tot, cnt, bw, bs = 0.0, 0, '', float('-inf')
                for p in occ[g][:400]:
                    win = pairs[max(0, p - 6):p + 7]
                    dec = decode_window(win, t2)
                    sc = qscore(dec, q, floor)
                    if sc == float('-inf'):
                        continue
                    tot += sc
                    cnt += 1
                    if sc > bs:
                        bs, bw = sc, dec
                if cnt:
                    out.append((tot / cnt, g, w, cnt, bw, round(bs, 3)))
        out.sort(reverse=True)
        # anchors-only baseline with the provisional table
        base = []
        for g in cand[:10]:
            tot, cnt = 0.0, 0
            for p in occ[g][:200]:
                win = pairs[max(0, p - 6):p + 7]
                sc = qscore(decode_window(win, table), q, floor)
                if sc != float('-inf'):
                    tot += sc
                    cnt += 1
            base.append(round(tot / cnt, 3) if cnt else None)
        still_floor = all((b is None or abs(b - floor) < 1e-9) for b in base)
        res['drag_rerun'] = {
            'provisional_anchors': prov,
            'n_anchors': len(table),
            'top10': [{'group': g, 'word': w, 'windows': c, 'mean': round(ms, 3),
                       'best_window': bw, 'best_score': bs}
                      for ms, g, w, c, bw, bs in out[:10]],
            'baseline_still_at_floor': still_floor,
            'baseline': base,
        }
        print("[D] drag re-run with %d anchors (provisional: %s)" % (len(table), prov))
        print("[D] baseline still at floor: %s" % still_floor)
        for r_ in res['drag_rerun']['top10'][:8]:
            print("     %s -> %-8s mean=%.3f best='%s'"
                  % (r_['group'], r_['word'], r_['mean'], r_['best_window']))
    else:
        print("[D] no hypothesis CONFIRMED; drag not re-run (per work order)")

    with open(os.path.join(DATA, 'attempt2_results.json'), 'w') as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
    print("[done] wrote ../data/attempt2_results.json")


if __name__ == '__main__':
    main()
