#!/usr/bin/env python3
"""
Attempt 3 — era-matched reference corpus + test 64="qui" as the 9th anchor.

NEW vs attempt 2: the French rate reference is no longer Les Miserables Tome 1
(novel, 1862 — era mismatch AND register mismatch vs an 1841 diplomatic
despatch). It is now Tocqueville, "De la democratie en Amerique", Tomes 1+2
(1835/1840, formal political prose): era-correct and the closest available
register to diplomatic correspondence at scale.

Work:
  (1) Build era reference stats; report where they agree/disagree with the
      Les Mis rates attempt 2 used.
  (2) Re-validate 87=ce (attempt 2's 4/5 CONFIRMED anchor) against era rates.
  (3) Test H3: 64="qui". Evidence: 87->64 x5 ("ce qui" the natural reading);
      64 is rank 4 at 46x. Same bar: >=2 independent checks to promote;
      a grammatical contradiction REFUTES (attempt-2 rule).
  (4) Bonus (STATE.md next): re-examine 82->16 in ce-anchored windows.

Deterministic. No invented ciphertext. Results -> ../data/attempt3_results.json
"""
import json, re, collections, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, '..', 'data')
sys.path.insert(0, HERE)
from crib_attack import load_pairs, ANCHORS

T1 = os.path.join(DATA, 'gutenberg-30513-tocqueville-t1.txt')
T2 = os.path.join(DATA, 'gutenberg-30514-tocqueville-t2.txt')
LES_MIS_LOCAL = os.path.join(DATA, 'gutenberg-17489-miserables1.txt')


def load_words(path):
    text = open(path, encoding='utf-8', errors='replace').read().lower()
    m = re.search(r'\*\*\* start of.*?\*\*\*', text)
    if m:
        text = text[m.end():]
    m = re.search(r'\*\*\* end of.*', text)
    if m:
        text = text[:m.start()]
    return re.findall(r"[a-zàâäéèêëîïôöùûüÿç]+", text)


def ref_stats(words, label):
    n = len(words)
    def cnt(w):
        return sum(1 for x in words if x == w)
    def bicnt(a, b):
        return sum(1 for x, y in zip(words, words[1:]) if x == a and y == b)
    n_ce = cnt('ce')
    n_cela_uni = cnt('cela')
    fol_ce = collections.Counter(y for x, y in zip(words, words[1:]) if x == 'ce')
    wc = collections.Counter(words)
    ranked_words = [w for w, _ in wc.most_common()]
    def word_rank(w):
        return ranked_words.index(w) if w in ranked_words else None
    # letter-level: what follows 'm' inside words (attempt-2 check d analogue)
    after_m = collections.Counter()
    n_m = 0
    for w in words:
        for i, ch in enumerate(w):
            if ch == 'm':
                n_m += 1
                after_m[w[i + 1] if i + 1 < len(w) else '#'] += 1
    return {
        'label': label,
        'words': n,
        'n_ce': n_ce,
        # NOTE: "cela" is one orthographic word, so the bigram-conditional
        # P(word after "ce" == "cela") is ~0 in any corpus. Attempt 2 compared
        # the cipher bigram rate P(11|87) against the UNIGRAM ratio
        # n("cela")/n("ce") (every "cela" word = one ce+la spelling in the
        # syllabary). We keep that comparison for continuity and report the
        # era-vs-LesMis gap explicitly. Both quantities are stored.
        'p_cela_bigram_given_ce': bicnt('ce', 'cela') / n_ce if n_ce else None,
        'unigram_ratio_cela_over_ce': n_cela_uni / n_ce if n_ce else None,
        'n_cela': n_cela_uni,
        'n_ce_cela': bicnt('ce', 'cela'),
        'p_que_given_ce': bicnt('ce', 'que') / n_ce if n_ce else None,
        'n_ce_que': bicnt('ce', 'que'),
        'p_qui_given_ce': bicnt('ce', 'qui') / n_ce if n_ce else None,
        'n_ce_qui': bicnt('ce', 'qui'),
        'p_la_given_de': (lambda nd: bicnt('de', 'la') / nd if nd else None)(cnt('de')),
        'n_de_la': bicnt('de', 'la'), 'n_de': cnt('de'),
        'p_la_given_a': (lambda na: sum(1 for x, y in zip(words, words[1:]) if x in ('à', 'a') and y == 'la') / na if na else None)(sum(1 for x in words if x in ('à', 'a'))),
        'top_followers_of_ce': fol_ce.most_common(10),
        'rank_qui': word_rank('qui'),
        'rank_ce': word_rank('ce'),
        'rank_que': word_rank('que'),
        'rank_cela': word_rank('cela'),
        'p_next_given_m': {k: round(v / n_m, 4) for k, v in after_m.most_common(8)},
    }


def neighbours(pairs, anchor, direction=+1):
    c = collections.Counter()
    for i, g in enumerate(pairs):
        if g == anchor:
            j = i + direction
            if 0 <= j < len(pairs):
                c[pairs[j]] += 1
    return c


def within_factor(obs, ref, lo=0.5, hi=2.0):
    return ref is not None and ref > 0 and lo * ref <= obs <= hi * ref


def main():
    pairs, _, _ = load_pairs()
    freq = collections.Counter(pairs)
    ranked = sorted(freq.items(), key=lambda kv: -kv[1])
    res = {'anchors': ANCHORS}

    # ---------------- era reference ----------------
    era = ref_stats(load_words(T1) + load_words(T2), 'tocqueville-1835-1840')
    les = ref_stats(load_words(LES_MIS_LOCAL), 'les-miserables-1862')
    res['era_reference'] = era
    res['lesmis_reference_recomputed'] = les
    print("[ERA] %s: %d words" % (era['label'], era['words']))
    print("[ERA] n(cela)/n(ce)=%.4f (%d/%d)  P(que|ce)=%.4f (%d/%d)  P(qui|ce)=%.4f (%d/%d)"
          % (era['unigram_ratio_cela_over_ce'], era['n_cela'], era['n_ce'],
             era['p_que_given_ce'], era['n_ce_que'], era['n_ce'],
             era['p_qui_given_ce'], era['n_ce_qui'], era['n_ce']))
    print("[ERA] top followers of 'ce': %s" % era['top_followers_of_ce'])
    print("[ERA] word ranks: qui=%s ce=%s que=%s cela=%s"
          % (era['rank_qui'], era['rank_ce'], era['rank_que'], era['rank_cela']))
    print("[LESMIS] n(cela)/n(ce)=%.4f  P(que|ce)=%.4f  P(qui|ce)=%.4f  P(la|de)=%.4f  P(la|a)=%.4f"
          % (les['unigram_ratio_cela_over_ce'], les['p_que_given_ce'], les['p_qui_given_ce'],
             les['p_la_given_de'], les['p_la_given_a']))
    print("[COMPARE] cela-rate: era %.4f vs lesmis %.4f | que|ce: era %.4f vs lesmis %.4f | "
          "qui|ce: era %.4f vs lesmis %.4f"
          % (era['unigram_ratio_cela_over_ce'], les['unigram_ratio_cela_over_ce'],
             era['p_que_given_ce'], les['p_que_given_ce'],
             era['p_qui_given_ce'], les['p_qui_given_ce']))

    # ---------------- cipher stats for 87 and 64 ----------------
    n87 = freq['87']
    fol87 = neighbours(pairs, '87', +1)
    pre87 = neighbours(pairs, '87', -1)
    n64 = freq['64']
    fol64 = neighbours(pairs, '64', +1)
    pre64 = neighbours(pairs, '64', -1)
    rank64 = next((i for i, (g, _) in enumerate(ranked) if g == '64'), None)
    rank87 = next((i for i, (g, _) in enumerate(ranked) if g == '87'), None)
    c_87_64 = fol87['64']
    c_46_64 = neighbours(pairs, '46', +1)['64']   # "que qui" negative control
    c_64_87 = fol64['87']
    p_64_given_87 = c_87_64 / n87
    obs_cela = fol87['11'] / n87
    obs_que = fol87['46'] / n87
    res['cipher'] = {
        'n_87': n87, 'rank_87': rank87, 'n_64': n64, 'rank_64': rank64,
        'count_87_64': c_87_64, 'p_64_given_87': round(p_64_given_87, 4),
        'count_46_64_que_qui': c_46_64,
        'count_64_87': c_64_87,
        'p_87_given_64': round(pre64['87'] / n64, 4) if n64 else None,
        'followers_64_top12': fol64.most_common(12),
        'predecessors_64_top12': pre64.most_common(12),
        'followers_87_top12': fol87.most_common(12),
        'p_11_given_87': round(obs_cela, 4),
        'p_que_given_87': round(obs_que, 4),
    }
    print("[C] 87: n=%d rank=%d | 64: n=%d rank=%d" % (n87, rank87, n64, rank64))
    print("[C] 87->64 = %d (P=%.4f) | 46=que -> 64 = %d | 64->87 = %d | P(87|64)=%.4f"
          % (c_87_64, p_64_given_87, c_46_64, c_64_87, res['cipher']['p_87_given_64']))
    print("[C] followers of 64: %s" % fol64.most_common(10))
    print("[C] predecessors of 64: %s" % pre64.most_common(10))

    # ---------------- re-validate 87=ce against ERA rates ----------------
    v, why = [], []
    if rank87 is not None and rank87 < 25:
        v.append(True); why.append("rank(87)=%d, common-word band (era-independent)" % rank87)
    else:
        v.append(False); why.append("rank(87)=%s too rare" % rank87)
    if within_factor(obs_cela, era['unigram_ratio_cela_over_ce']):
        v.append(True); why.append("P(11|87)=%.3f ~= era n(cela)/n(ce)=%.3f" % (obs_cela, era['unigram_ratio_cela_over_ce']))
    else:
        v.append(False); why.append("P(11|87)=%.3f vs era n(cela)/n(ce)=%.3f (lesmis %.3f) -- REGISTER GAP"
                                    % (obs_cela, era['unigram_ratio_cela_over_ce'], les['unigram_ratio_cela_over_ce']))
    if within_factor(obs_que, era['p_que_given_ce']):
        v.append(True); why.append("P(que|87)=%.3f ~= era P(que|ce)=%.3f" % (obs_que, era['p_que_given_ce']))
    else:
        v.append(False); why.append("P(que|87)=%.3f vs era P(que|ce)=%.3f (lesmis was %.3f)"
                                    % (obs_que, era['p_que_given_ce'], les['p_que_given_ce']))
    if len(pre87) >= 8:
        v.append(True); why.append("%d distinct predecessors (era-independent)" % len(pre87))
    else:
        v.append(False); why.append("only %d distinct predecessors" % len(pre87))
    s = sum(v)
    verdict_ce = 'CONFIRMED' if s >= 2 else ('PLAUSIBLE' if s == 1 else 'INCONCLUSIVE')
    res['revalidate_87_ce_era'] = {'verdict': verdict_ce, 'checks_passed': s, 'of': 4,
                                   'reasons': why}
    print("[R] 87=ce re-validated vs era: %s (%d/4): %s" % (verdict_ce, s, '; '.join(why)))

    # ---------------- H3: 64 = "qui" ----------------
    h, whyh = [], []
    # (a) frequency band: 64 is rank 4 of 96 groups; "qui" should be a top word
    rq = era['rank_qui']
    if rank64 is not None and rank64 <= 8 and rq is not None and rq < 30:
        h.append(True); whyh.append("rank(64)=%d of 96 groups; era rank('qui')=%d (top word)" % (rank64, rq))
    else:
        h.append(False); whyh.append("rank(64)=%s vs era rank('qui')=%s" % (rank64, rq))
    # (b) P(64|87) vs era P(qui|ce), factor-2 band
    if within_factor(p_64_given_87, era['p_qui_given_ce']):
        h.append(True); whyh.append("P(64|87)=%.4f ~= era P(qui|ce)=%.4f" % (p_64_given_87, era['p_qui_given_ce']))
    else:
        h.append(False); whyh.append("P(64|87)=%.4f vs era P(qui|ce)=%.4f (lesmis %.4f)"
                                     % (p_64_given_87, era['p_qui_given_ce'], les['p_qui_given_ce']))
    # (c) negative control: 46=que -> 64 ("que qui" ungrammatical) must be ~0
    if c_46_64 == 0:
        h.append(True); whyh.append("46=que -> 64 = 0, consistent with 'qui'")
    else:
        h.append(False); whyh.append("46=que -> 64 = %d, against 'qui'" % c_46_64)
    # (d) 64 is a free function word: diverse followers and predecessors
    nfol, npre = len(fol64), len(pre64)
    top_share = fol64.most_common(1)[0][1] / n64 if n64 else 1
    if nfol >= 8 and npre >= 8 and top_share < 0.5:
        h.append(True); whyh.append("%d followers/%d predecessors, top share %.2f: free function word"
                                    % (nfol, npre, top_share))
    else:
        h.append(False); whyh.append("followers=%d predecessors=%d top share=%.2f"
                                    % (nfol, npre, top_share))
    sh = sum(h)
    verdict_h3 = 'CONFIRMED' if sh >= 2 else ('PLAUSIBLE' if sh == 1 else 'INCONCLUSIVE')
    if c_46_64 >= 2:
        verdict_h3 = 'REFUTED'
        whyh.append("OVERRIDE: 46=que -> 64 = %d contradicts 'qui' -> REFUTED" % c_46_64)
    res['verdict_H3_64_qui'] = {'verdict': verdict_h3, 'checks_passed': sh, 'of': 4,
                                'reasons': whyh}
    print("[V3] H3 (64=qui): %s (%d/4): %s" % (verdict_h3, sh, '; '.join(whyh)))

    # rival note: 64 as "ci" (ceci = 87+64)? P(87|64) measures ceci-binding.
    print("[V3] rival 'ci': P(87|64)=%.4f — %s" %
          (res['cipher']['p_87_given_64'],
           "64 not ceci-bound; favours 'qui' (diverse contexts)" if res['cipher']['p_87_given_64'] < 0.25
           else "64 mostly follows 87; 'ci' (ceci) stays live"))

    # ---------------- bonus: 82->16 in ce-anchored windows ----------------
    near_ce = 0
    total_82_16 = 0
    for i in range(len(pairs) - 1):
        if pairs[i] == '82' and pairs[i + 1] == '16':
            total_82_16 += 1
            window = pairs[max(0, i - 3):i + 5]
            if '87' in window:
                near_ce += 1
    res['bonus_82_16_near_ce'] = {'total_82_16': total_82_16, 'with_87_within_3': near_ce}
    print("[B] 82->16 total=%d, with 87=ce within +-3 groups: %d" % (total_82_16, near_ce))

    # ---------------- conditional drag re-run (only if H3 confirmed) ----------------
    res['drag_rerun'] = None
    if verdict_h3 == 'CONFIRMED':
        from crib_attack import load_quadgrams, qscore, decode_window
        q, floor = load_quadgrams()
        table = dict(ANCHORS); table['87'] = 'ce'; table['64'] = 'qui'
        cand = [g for g, _ in ranked[:40] if g not in table]
        occ = {g: [i for i, gg in enumerate(pairs) if gg == g] for g in cand}
        cands_words = ['le', 'les', 'de', 'des', 'du', 'un', 'une', 'et', 'est',
                        'ne', 'ces', 'se', 'il', 'ils', 'elle', 'nous', 'vous',
                        'je', 'on', 'en', 'au', 'aux', 'dans', 'pour', 'par',
                        'sur', 'pas', 'plus', 'tout', 'tous', 'toute', 'dont',
                        'comme', 'avec', 'sans', 'mais', 'ou', 'mon', 'ma',
                        'mes', 'son', 'sa', 'ses', 'notre', 'votre', 'leur', 'cette']
        out = []
        for g in cand:
            for w in cands_words:
                if w in table.values():
                    continue
                t2 = dict(table); t2[g] = w
                tot, cnt, bw, bs = 0.0, 0, '', float('-inf')
                for p in occ[g][:400]:
                    win = pairs[max(0, p - 6):p + 7]
                    dec = decode_window(win, t2)
                    sc = qscore(dec, q, floor)
                    if sc == float('-inf'):
                        continue
                    tot += sc; cnt += 1
                    if sc > bs:
                        bs, bw = sc, dec
                if cnt:
                    out.append((tot / cnt, g, w, cnt, bw, round(bs, 3)))
        out.sort(reverse=True)
        base = []
        for g in cand[:10]:
            tot, cnt = 0.0, 0
            for p in occ[g][:200]:
                win = pairs[max(0, p - 6):p + 7]
                sc = qscore(decode_window(win, table), q, floor)
                if sc != float('-inf'):
                    tot += sc; cnt += 1
            base.append(round(tot / cnt, 3) if cnt else None)
        still_floor = all((b is None or abs(b - floor) < 1e-9) for b in base)
        res['drag_rerun'] = {'n_anchors': len(table), 'still_at_floor': still_floor,
                             'top5': [{'group': g, 'word': w, 'mean': round(ms, 3)}
                                      for ms, g, w, c, bw, bs in out[:5]]}
        print("[D] drag re-run with %d anchors: still at floor = %s" % (len(table), still_floor))
    else:
        print("[D] H3 not CONFIRMED; drag not re-run")

    with open(os.path.join(DATA, 'attempt3_results.json'), 'w') as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
    print("[done] wrote ../data/attempt3_results.json")


if __name__ == '__main__':
    main()
