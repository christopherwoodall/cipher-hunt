#!/usr/bin/env python3
"""
WO2 — STEM HUNTER (round 3, crowd3). Pursue F21: 06 = verb stem.

Ground-truth anchors: 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que.
Provisional (NOT ground truth): 87=ce, 64=qui, 96=par, 77=pas (rival: 77=que).

Work items:
 (a) Full follower profile of 06 (46 occ) vs verb-stem expectations.
 (b) Companion 67: followers + predecessors; pair pattern with 06?
 (c) Re-test 77="pas" under verb-stem 06.
 (d) Re-test rival 77="que" under verb-stem 06; score both.
 (e) Tension check vs WO1's 06="ent" (word ending) in the 94-82-06 family.

Method notes:
 - All counts recomputed from the pair stream (load_pairs). Nothing invented.
 - Structural checks preferred (per lane methodology warning: the factor-2
   rate band is uncalibrated). Era (Tocqueville 1835/1840) numbers are
   reported as CONTEXT, not verdicts.
 - V29 = {groups g with g->29 >= 2}: groups that take the infinitive ending
   29=er, i.e. verb-stem candidates by purely structural definition.
"""
import json, re, collections, os, sys, math

HERE = os.path.dirname(os.path.abspath(__file__))
CODE = os.path.join(HERE, '..')
DATA = os.path.join(CODE, '..', 'data')
sys.path.insert(0, CODE)
from crib_attack import load_pairs, ANCHORS

PROV = {'87': 'ce', '64': 'qui', '96': 'par', '77': 'pas?'}

T1 = os.path.join(DATA, 'gutenberg-30513-tocqueville-t1.txt')
T2 = os.path.join(DATA, 'gutenberg-30514-tocqueville-t2.txt')


def load_words(path):
    text = open(path, encoding='utf-8', errors='replace').read().lower()
    m = re.search(r'\*\*\* start of.*?\*\*\*', text)
    if m:
        text = text[m.end():]
    m = re.search(r'\*\*\* end of.*', text)
    if m:
        text = text[:m.start()]
    return re.findall(r"[a-zàâäéèêëîïôöùûüÿç]+", text)


def neighbours(pairs, anchor, direction=+1):
    c = collections.Counter()
    for i, g in enumerate(pairs):
        if g == anchor:
            j = i + direction
            if 0 <= j < len(pairs):
                c[pairs[j]] += 1
    return c


def ngram_count(pairs, seq):
    c = 0
    L = len(seq)
    for i in range(len(pairs) - L + 1):
        if pairs[i:i + L] == seq:
            c += 1
    return c


def jaccard_top(a, b, n=10):
    sa = set(g for g, _ in a.most_common(n))
    sb = set(g for g, _ in b.most_common(n))
    return len(sa & sb) / len(sa | sb) if (sa | sb) else 0.0


def cosine(a, b):
    keys = set(a) | set(b)
    dot = sum(a[k] * b[k] for k in keys)
    na = math.sqrt(sum(v * v for v in a.values()))
    nb = math.sqrt(sum(v * v for v in b.values()))
    return dot / (na * nb) if na and nb else 0.0


def main():
    pairs, odd_lines, off1 = load_pairs()
    n = len(pairs)
    freq = collections.Counter(pairs)
    ranked = sorted(freq.items(), key=lambda kv: -kv[1])
    rank_of = {g: i for i, (g, _) in enumerate(ranked)}
    res = {'n_pairs': n}

    # ---------- verify headline numbers ----------
    fol06, pre06 = neighbours(pairs, '06', +1), neighbours(pairs, '06', -1)
    fol67, pre67 = neighbours(pairs, '67', +1), neighbours(pairs, '67', -1)
    fol77, pre77 = neighbours(pairs, '77', +1), neighbours(pairs, '77', -1)
    fol46, pre46 = neighbours(pairs, '46', +1), neighbours(pairs, '46', -1)
    fol29, pre29 = neighbours(pairs, '29', +1), neighbours(pairs, '29', -1)
    fol11, pre11 = neighbours(pairs, '11', +1), neighbours(pairs, '11', -1)
    fol40 = neighbours(pairs, '40', +1)
    fol82 = neighbours(pairs, '82', +1)
    fol78, pre78 = neighbours(pairs, '78', +1), neighbours(pairs, '78', -1)

    res['verify'] = {
        'freq_06': freq['06'], 'rank_06': rank_of['06'],
        'freq_67': freq['67'], 'rank_67': rank_of['67'],
        'freq_77': freq['77'], 'rank_77': rank_of['77'],
        'freq_29': freq['29'], 'rank_29': rank_of['29'],
        '06->77': fol06['77'], '06->29': fol06['29'], '06->11': fol06['11'],
        '06_distinct_predecessors': len(pre06),
        '67->77': fol67['77'], '67->29': fol67['29'], '67->11': fol67['11'],
        '67_distinct_predecessors': len(pre67),
        '77->78': fol77['78'], '78->94': fol78['94'],
        '06->06': fol06['06'],
        '06-67_adjacent': ngram_count(pairs, ['06', '67']),
        '67-06_adjacent': ngram_count(pairs, ['67', '06']),
        '94-82-06_trigram': ngram_count(pairs, ['94', '82', '06']),
        '82->06': fol82['06'],
        '94-82-06-29': ngram_count(pairs, ['94', '82', '06', '29']),
        '06+40+77': ngram_count(pairs, ['06', '40', '77']),
        '06+40_total': fol06['40'], '06+34_total': fol06['34'],
    }

    # ---------- (a) full follower profile of 06 ----------
    res['a_fol06_full'] = fol06.most_common()
    res['a_pre06_full'] = pre06.most_common()
    res['a_fol06_distinct'] = len(fol06)
    top3 = sum(c for _, c in fol06.most_common(3))
    res['a_fol06_top3_share'] = round(top3 / freq['06'], 3)

    # V29: structural verb-stem candidates (take the infinitive ending 29=er >= 2x)
    V29 = {g for g in freq if neighbours(pairs, g, +1)['29'] >= 2}
    res['a_V29_size'] = len(V29)
    res['a_V29_members_top'] = sorted(
        ((g, freq[g]) for g in V29), key=lambda kv: -kv[1])[:20]
    res['a_pre29_distinct'] = len(pre29)  # ending-ness of 29: many stems?

    known_cont = {'29': 'er-infinitive', '40': 'e-ending', '34': 'i-ending',
                  '11': 'la-object', '77': 'pas/que?', '46': 'que-clause',
                  '64': 'qui?(prov)', '96': 'par?(prov)', '87': 'ce?(prov)',
                  '82': 'm', '70': 'pre'}
    compat_known = sum(c for g, c in fol06.items() if g in known_cont)
    compat_v29 = sum(c for g, c in fol06.items()
                     if g not in known_cont and g in V29)
    compat_neither = freq['06'] - compat_known - compat_v29
    res['a_compat'] = {
        'known_verb_continuations': compat_known,
        'v29_modal_infinitive_stem': compat_v29,
        'unexplained': compat_neither,
        'frac_known': round(compat_known / freq['06'], 3),
        'frac_known_plus_v29': round((compat_known + compat_v29) / freq['06'], 3),
    }
    res['a_fol06_v29_followers'] = [(g, c) for g, c in fol06.most_common()
                                    if g not in known_cont and g in V29]
    res['a_fol06_unexplained'] = [(g, c) for g, c in fol06.most_common()
                                  if g not in known_cont and g not in V29]

    # paradigm check: does 06 take the known endings 29/40/34?
    res['a_paradigm'] = {
        '06->29_er': fol06['29'], '06->40_e': fol06['40'],
        '06->34_i': fol06['34'],
        '06->40->77_trigram': ngram_count(pairs, ['06', '40', '77']),
        '06->29->X_sample': None,
    }

    # ---------- predecessor diversity table (S2) ----------
    div = {}
    for g in ['06', '67', '77', '11', '46', '40', '29', '82', '70', '87',
              '64', '00', '24', '94', '78']:
        pre = neighbours(pairs, g, -1)
        div[g] = {'freq': freq[g], 'distinct_pred': len(pre),
                  'diversity': round(len(pre) / freq[g], 3) if freq[g] else None}
    res['a_predecessor_diversity'] = div

    # ---------- (b) 67 profile + pair pattern ----------
    res['b_fol67_full'] = fol67.most_common()
    res['b_pre67_full'] = pre67.most_common()
    res['b_fol67_distinct'] = len(fol67)
    res['b_pair'] = {
        'follower_cosine_06_67': round(cosine(fol06, fol67), 3),
        'follower_jaccard_top10_06_67': round(jaccard_top(fol06, fol67), 3),
        'predecessor_overlap': sorted(set(pre06) & set(pre67)),
        'n_shared_predecessors': len(set(pre06) & set(pre67)),
        'predecessor_jaccard_top10': round(jaccard_top(pre06, pre67), 3),
        'shared_pred_counts': {g: (pre06[g], pre67[g])
                               for g in set(pre06) & set(pre67)},
    }
    # candidate shared "ne"/subject: predecessors hitting BOTH 06 and 67 >= 2x
    res['b_shared_pred_ge2'] = {g: (pre06[g], pre67[g]) for g in
                               set(pre06) & set(pre67)
                               if pre06[g] >= 2 and pre67[g] >= 2}
    # 67's own verb-ness: does 67 take endings?
    res['b_67_paradigm'] = {'67->29': fol67['29'], '67->40': fol67['40'],
                            '67->34': fol67['34'], '67->77': fol67['77'],
                            '67->11': fol67['11']}

    # ---------- (c) 77 = "pas" ----------
    res['c_fol77_full'] = fol77.most_common(20)
    res['c_pre77_full'] = pre77.most_common(20)
    # structural: fraction of 77's predecessors that are verb-stem-like (in V29)
    w_pre_v29 = sum(c for g, c in pre77.items() if g in V29)
    res['c_pred_verbness'] = {
        'pred_in_V29_weighted': w_pre_v29,
        'pred_total': sum(pre77.values()),
        'frac': round(w_pre_v29 / sum(pre77.values()), 3),
        'pred_in_V29_list': [(g, c) for g, c in pre77.most_common() if g in V29],
        'pred_not_in_V29_list': [(g, c) for g, c in pre77.most_common()
                                 if g not in V29],
    }
    # pas + infinitive frame: 77 -> V29-stem -> 29 ?
    n_77_v29_29 = sum(1 for i in range(n - 2)
                      if pairs[i] == '77' and pairs[i + 1] in V29
                      and pairs[i + 2] == '29')
    res['c_77_stem_29_trigram'] = n_77_v29_29
    res['c_77->29_direct'] = fol77['29']

    # ---------- (d) 77 = "pas" vs "que": 77 vs 46 distributional ----------
    res['d_77_vs_46'] = {
        'follower_cosine_77_46': round(cosine(fol77, fol46), 3),
        'follower_jaccard_top10': round(jaccard_top(fol77, fol46), 3),
        '77->29': fol77['29'], '46->29': fol46['29'],
        '77->46': fol77['46'], '46->77': fol46['77'],
        '77->87ce': fol77['87'], '46->87ce': fol46['87'],
        '77->64qui': fol77['64'], '46->64qui': fol46['64'],
        '77->11la': fol77['11'], '46->11la': fol46['11'],
        'pred_overlap_77_46': sorted(set(pre77) & set(pre46)),
        'n_pred_overlap': len(set(pre77) & set(pre46)),
        'pred46_subset_of_pred77_frac':
            round(len(set(pre46) & set(pre77)) / len(set(pre46)), 3)
            if pre46 else None,
        'fol77_top10': fol77.most_common(10),
        'fol46_top10': fol46.most_common(10),
    }

    # ---------- (e) tension: 94-82-06 family vs stem-06 ----------
    # partition 06 occurrences by predecessor == 82 (ending-like) vs rest
    end_like, stem_like = [], []  # indices
    for i, g in enumerate(pairs):
        if g == '06':
            (end_like if i > 0 and pairs[i - 1] == '82' else stem_like).append(i)
    fol_end = collections.Counter(pairs[i + 1] for i in end_like
                                  if i + 1 < n)
    fol_stem = collections.Counter(pairs[i + 1] for i in stem_like
                                   if i + 1 < n)
    pre_end = collections.Counter(pairs[i - 2] for i in end_like if i - 2 >= 0)
    res['e_partition'] = {
        'n_06_pred82': len(end_like), 'n_06_other': len(stem_like),
        'fol_of_06_pred82': fol_end.most_common(),
        'fol_of_06_other': fol_stem.most_common(15),
        'prepre_of_94_82_06': pre_end.most_common(),
        'n_94_82_06': ngram_count(pairs, ['94', '82', '06']),
        '82->06_all_preceded_by_94': None,
    }
    # are all 82->06 preceded by 94?
    n_82_06 = ngram_count(pairs, ['82', '06'])
    res['e_partition']['82->06_total'] = n_82_06
    res['e_partition']['82->06_not_preceded_by_94'] = sum(
        1 for i in range(1, n - 1)
        if pairs[i] == '82' and pairs[i + 1] == '06' and pairs[i - 1] != '94')
    # does an 82-preceded 06 ever take verb continuations 29/11/77?
    res['e_partition']['pred82_06_takes_29_11_77'] = {
        g: fol_end[g] for g in ('29', '11', '77')}
    # 06->06 bigram ("...ment" + "ent..."): positions
    res['e_06_06_positions'] = [i for i in range(n - 1)
                                if pairs[i] == '06' and pairs[i + 1] == '06']
    res['e_06_06_contexts'] = [' '.join(pairs[max(0, i - 3):i + 5])
                               for i in res['e_06_06_positions']]
    # 06 as "ent": stem-role followers that fit entr-/entend-
    res['e_ent_fit'] = {
        '06->29_er_entrer': fol06['29'],
        '06->40_e_entre': fol06['40'],
        '06->34_i': fol06['34'],
        '06->82_m': fol06['82'],
        'note': 'ent syllable: entr-er (06->29), entr-e (06->40), -ment (82->06)',
    }
    # 78 quick profile (for the 77-78 bigram in both repeats)
    res['e_78_profile'] = {'freq': freq['78'], 'rank': rank_of['78'],
                           'fol': fol78.most_common(10),
                           'pre': pre78.most_common(10)}

    # ---------- era corpus context ----------
    words = load_words(T1) + load_words(T2)
    res['era_words'] = len(words)
    wc = collections.Counter(words)
    bigrams = collections.Counter(zip(words, words[1:]))

    def fb(w):
        return collections.Counter(y for x, y in zip(words, words[1:]) if x == w)

    def pb(w):
        return collections.Counter(x for x, y in zip(words, words[1:]) if y == w)

    # E1: predecessors of "pas"
    ppas = pb('pas')
    res['era_pred_pas_top15'] = ppas.most_common(15)
    res['era_n_pas'] = wc['pas']
    res['era_pred_pas_ne'] = ppas['ne']
    # E6: followers of "ne" (kill-check for 06="ne": ne followed by er-initial?)
    fne = fb('ne')
    res['era_fol_ne_top15'] = fne.most_common(15)
    res['era_ne_total'] = wc['ne']
    er_init = sum(c for w, c in fne.items() if w.startswith('er'))
    res['era_ne_followed_by_er_initial'] = er_init

    # E2/E3: P(pas|verb), P(que|verb) for common verb forms
    verb_forms = ['est', 'sont', 'a', 'ont', 'fait', 'font', 'dit', 'disent',
                  'veut', 'veulent', 'peut', 'peuvent', 'doit', 'doivent',
                  'va', 'vont', 'vient', 'viennent', 'faut', 'sait', 'savent',
                  'voit', 'voient', 'prend', 'prennent', 'donne', 'met',
                  'trouve', 'reste', 'devient', 'semble', 'paraît', 'parait']
    rows = []
    for v in verb_forms:
        nv = wc[v]
        if not nv:
            continue
        f = fb(v)
        rows.append({'verb': v, 'n': nv,
                     'p_pas': round(f['pas'] / nv, 4),
                     'p_que': round(f['que'] / nv, 4),
                     'p_la': round((f['la'] + f['le'] + f['les']) / nv, 4)})
    res['era_verb_followers'] = rows
    tot_n = sum(r['n'] for r in rows)
    res['era_verb_mean'] = {
        'p_pas': round(sum(r['p_pas'] * r['n'] for r in rows) / tot_n, 4),
        'p_que': round(sum(r['p_que'] * r['n'] for r in rows) / tot_n, 4),
        'p_la_le_les': round(sum(r['p_la'] * r['n'] for r in rows) / tot_n, 4),
    }
    # E4: modal + infinitive: top followers of modals, eyeball infinitives
    modals = ['veut', 'veulent', 'peut', 'peuvent', 'doit', 'doivent',
              'faut', 'va', 'vont', 'vient', 'fait', 'font']
    res['era_modal_followers'] = {m: fb(m).most_common(12)
                                  for m in modals if wc[m] > 20}

    with open(os.path.join(HERE, 'stem_hunter_results.json'), 'w') as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
    print('[done] wrote stem_hunter_results.json')
    # headline printout
    print('verify:', json.dumps(res['verify'], indent=1, ensure_ascii=False))
    print('compat:', json.dumps(res['a_compat'], indent=1, ensure_ascii=False))
    print('pair:', json.dumps(res['b_pair'], indent=1, ensure_ascii=False))


if __name__ == '__main__':
    main()
