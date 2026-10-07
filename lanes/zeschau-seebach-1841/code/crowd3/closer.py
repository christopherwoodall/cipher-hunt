#!/usr/bin/env python3
"""
WO4 (round 3) — THE CLOSER: resolve 87="ce"'s provisional status.

Deterministic. All numbers recomputed from the pair stream (crib_attack.load_pairs)
and from the two local corpora with the attempt-3 tokenizer. No invented
ciphertext. Results -> code/crowd3/closer_results.{md,json}.

Parts:
  (a) STEELMAN 87=ce from scratch (cipher profile + era syllabary-aware model).
  (b) RIVAL battery: se, ne, le, je, on, en (de/a already dead) vs same checks.
  (c) REDO the 24-inversion intersection under a documented mixed-register model.
  (d) 96-licenses-que reframing -> what sits in "par _ que" frames?
  (e) NEW: 87-inversion sweep (which era words fit 87's triple profile?).
"""
import json, re, collections, math, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CODE = os.path.dirname(HERE)
DATA = os.path.join(CODE, '..', 'data')
sys.path.insert(0, CODE)
from crib_attack import load_pairs

ANCHORS = {'11': 'la', '70': 'pre', '82': 'm', '34': 'i',
           '29': 'er', '40': 'e', '46': 'que'}

RIVALS = ['se', 'ne', 'le', 'je', 'on', 'en']


def load_words(path):
    text = open(path, encoding='utf-8', errors='replace').read().lower()
    m = re.search(r'\*\*\* start of.*?\*\*\*', text)
    if m:
        text = text[m.end():]
    m = re.search(r'\*\*\* end of.*', text)
    if m:
        text = text[:m.start()]
    return re.findall(r"[a-zàâäéèêëîïôöùûüÿç]+", text)


class Corp:
    """Word-level corpus stats with the attempt-3 tokenizer."""
    def __init__(self, words, label):
        self.label = label
        self.words = words
        self.n = len(words)
        self.uni = collections.Counter(words)
        self.bi = collections.Counter(zip(words, words[1:]))
        self.tri = collections.Counter(zip(words, words[1:], words[2:]))
        self.fol = collections.defaultdict(collections.Counter)
        self.pre = collections.defaultdict(collections.Counter)
        for a, b in zip(words, words[1:]):
            self.fol[a][b] += 1
            self.pre[b][a] += 1
        self.ranked = [w for w, _ in self.uni.most_common()]

    def p_fol(self, a, b):
        na = self.uni.get(a, 0)
        return (self.bi.get((a, b), 0) / na) if na else None

    def p_pre(self, b, a):
        nb = self.uni.get(b, 0)
        return (self.bi.get((a, b), 0) / nb) if nb else None

    def share(self, w):
        return self.uni.get(w, 0) / self.n

    def rank(self, w):
        return self.ranked.index(w) + 1 if w in self.uni else None

    def distinct_preds(self, w):
        return len(self.pre.get(w, {}))


def wilson(p, n, z=1.96):
    if n == 0:
        return (0.0, 1.0)
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return ((c - h) / d, (c + h) / d)


def within2(obs, ref):
    if obs is None or ref is None:
        return None
    if ref == 0:
        return None
    if obs == 0:
        return False  # genuine fail: predicted rate 0 vs observed >0
    return max(obs, ref) / min(obs, ref) <= 2.0


def main():
    pairs, odd_lines, off1 = load_pairs()
    N = len(pairs)
    f87 = pairs.count('87')
    uni = collections.Counter(pairs)
    fol87 = collections.Counter(pairs[i + 1] for i, g in enumerate(pairs[:-1]) if g == '87')
    pre87 = collections.Counter(pairs[i - 1] for i, g in enumerate(pairs[1:], 1) if g == '87')
    pre11 = collections.Counter(pairs[i - 1] for i, g in enumerate(pairs[1:], 1) if g == '11')
    fol46 = collections.Counter(pairs[i + 1] for i, g in enumerate(pairs[:-1]) if g == '46')
    # all 87->46 bigrams with their predecessors (96-licenses-que reframing)
    bg87_46 = [(pairs[i - 1], i) for i, g in enumerate(pairs[1:], 1)
               if g == '87' and pairs[i + 1] == '46'] if False else None
    bg87_46 = []
    for i in range(1, N - 1):
        if pairs[i] == '87' and pairs[i + 1] == '46':
            bg87_46.append((pairs[i - 1], i))
    f96 = uni.get('96', 0)
    n96_87 = sum(1 for i, g in enumerate(pairs[:-1]) if g == '96' and pairs[i + 1] == '87')
    # cipher profile of 87
    p11_87 = fol87.get('11', 0) / f87
    p46_87 = fol87.get('46', 0) / f87
    p64_87 = fol87.get('64', 0) / f87
    share87 = f87 / N
    rank87 = sorted(uni, key=lambda g: -uni[g]).index('87') + 1

    cipher87 = {
        'n_pairs': N, 'n_87': f87, 'rank_87': rank87, 'share_87': round(share87, 6),
        'followers_87': dict(fol87.most_common()),
        'P_11_given_87': round(p11_87, 4), 'n_87_11': fol87.get('11', 0),
        'P_46_given_87': round(p46_87, 4), 'n_87_46': fol87.get('46', 0),
        'P_64_given_87': round(p64_87, 4), 'n_87_64': fol87.get('64', 0),
        'n_distinct_predecessors_87': len(pre87),
        'predecessors_87': dict(pre87.most_common()),
        'top_predecessors_of_11': dict(pre11.most_common(6)),
        'n_distinct_followers_87': len(fol87),
        'n_96': f96, 'n_96_87': n96_87, 'P_87_given_96': round(n96_87 / f96, 4) if f96 else None,
        'bigrams_87_46': [{'predecessor': p, 'pair_index': i} for p, i in bg87_46],
        'odd_lines': odd_lines, 'off1_lines': off1,
    }

    # corpora
    era = Corp(load_words(os.path.join(DATA, 'gutenberg-30513-tocqueville-t1.txt')) +
                         load_words(os.path.join(DATA, 'gutenberg-30514-tocqueville-t2.txt')),
               'tocqueville-1835-1840')
    mis = Corp(load_words(os.path.join(DATA, 'gutenberg-17489-miserables1.txt')),
               'les-miserables-1862')

    # ---- syllabary-aware "ce" model: which corpus tokens syllabify with first syllable "ce"
    # standalone "ce" (follower = next word); compounds: cela->la, ceci->ci, cet/cette->t/te,
    # ceux->x, celui/celle(s)->lui/lle(s)
    ce_compounds = {'cela': 'la', 'ceci': 'ci', 'cet': 't', 'cette': 'te',
                    'ceux': 'x', 'celui': 'lui', 'celle': 'lle', 'celles': 'lles'}

    def ce_model(c):
        denom = c.uni.get('ce', 0) + sum(c.uni.get(w, 0) for w in ce_compounds)
        pred = {}
        for w, syl in ce_compounds.items():
            pred['P_' + syl + '_given_87model'] = round(c.uni.get(w, 0) / denom, 4) if denom else None
        for w in ('qui', 'que', 'qu', 'n', 'sont', 'point'):
            pred['P_' + w + '_given_87model'] = round(c.bi.get(('ce', w), 0) / denom, 4) if denom else None
        pred['denom'] = denom
        pred['n_ce'] = c.uni.get('ce', 0)
        return pred

    steel = {}
    for c in (era, mis):
        m = ce_model(c)
        steel[c.label] = {
            'model': m,
            'cipher_P_11_given_87': round(p11_87, 4),
            'cipher_P_64_given_87': round(p64_87, 4),
            'cipher_P_46_given_87': round(p46_87, 4),
            'within2_la': within2(p11_87, m['P_la_given_87model']),
            'within2_qui': within2(p64_87, m['P_qui_given_87model']),
            'within2_que': within2(p46_87, m['P_que_given_87model']),
        }

    # ---- (b) RIVAL battery, same checks, era corpus
    battery = {}
    for R in RIVALS + ['ce']:
        nR = era.uni.get(R, 0)
        row = {
            'n': nR, 'rank': era.rank(R), 'share': round(era.share(R), 6),
            'share_within2_of_87': within2(era.share(R), share87),
            'P_la': round(era.p_fol(R, 'la') or 0.0, 4), 'n_R_la': era.bi.get((R, 'la'), 0),
            'P_la_within2': within2(era.p_fol(R, 'la'), p11_87),
            'P_que': round(era.p_fol(R, 'que') or 0.0, 4), 'n_R_que': era.bi.get((R, 'que'), 0),
            'P_que_within2': within2(era.p_fol(R, 'que'), p46_87),
            'P_qui': round(era.p_fol(R, 'qui') or 0.0, 4), 'n_R_qui': era.bi.get((R, 'qui'), 0),
            'P_qui_within2': within2(era.p_fol(R, 'qui'), p64_87),
            'distinct_predecessors': era.distinct_preds(R),
            'n_par_R_que_trigrams': sum(era.tri.get(('par', R, 'que'), 0) for _ in [0]),
        }
        row['n_par_R_que_trigrams'] = era.tri.get(('par', R, 'que'), 0)
        battery[R] = row

    # grammar judgements for the triple {R+la, R+que, R+qui} and par+R+que frame
    grammar = {
        'se':  {'R_la': 'rare (se+la: "se la rappellent" marginal)', 'R_que': 'UNGRAMMATICAL',
                'R_qui': 'UNGRAMMATICAL', 'par_frame': 'UNGRAMMATICAL'},
        'ne':  {'R_la': 'marginal ("ne la regarda pas" possible, low)',
                'R_que': 'UNGRAMMATICAL as bigram (ne...que needs verb between)',
                'R_qui': 'UNGRAMMATICAL', 'par_frame': 'UNGRAMMATICAL'},
        'le':  {'R_la': 'UNGRAMMATICAL (article+article)', 'R_que': 'UNGRAMMATICAL',
                'R_qui': 'UNGRAMMATICAL', 'par_frame': 'UNGRAMMATICAL'},
        'je':  {'R_la': 'grammatical ("je la vois")', 'R_que': 'UNGRAMMATICAL',
                'R_qui': 'UNGRAMMATICAL', 'par_frame': 'UNGRAMMATICAL'},
        'on':  {'R_la': 'grammatical ("on la nomme")', 'R_que': 'UNGRAMMATICAL',
                'R_qui': 'UNGRAMMATICAL', 'par_frame': 'UNGRAMMATICAL'},
        'en':  {'R_la': 'marginal/rare', 'R_que': 'UNGRAMMATICAL',
                'R_qui': 'UNGRAMMATICAL', 'par_frame': 'UNGRAMMATICAL'},
        'ce':  {'R_la': 'grammatical ("cela" = ce+la)', 'R_que': 'grammatical ("ce que")',
                'R_qui': 'grammatical ("ce qui")', 'par_frame': 'grammatical ("parce que" = par+ce+que)'},
    }

    # ---- (e) 87-inversion sweep: which words fit {P(que|W)~0.0938, P(qui|W)~0.1562}?
    def invert87(c):
        out = []
        for w, nw in c.uni.most_common(4000):
            if nw < 20:
                break
            pq = (c.bi.get((w, 'que'), 0) / nw)
            pi = (c.bi.get((w, 'qui'), 0) / nw)
            sh = nw / c.n
            lq = within2(pq, p46_87)
            li = within2(pi, p64_87)
            ls = within2(sh, share87)
            # distance: max log2 ratio over the two bigram legs
            d = max(abs(math.log2(max(pq, 1e-9) / p46_87)),
                    abs(math.log2(max(pi, 1e-9) / p64_87)))
            out.append({'w': w, 'n': nw, 'share': round(sh, 6),
                        'P_que': round(pq, 4), 'P_qui': round(pi, 4),
                        'legs_bigram': (1 if lq else 0) + (1 if li else 0),
                        'share_band': bool(ls), 'dist': round(d, 3)})
        out.sort(key=lambda r: (-r['legs_bigram'], r['dist']))
        return out

    inv87_era = invert87(era)
    inv87_mis = invert87(mis)
    ce_pos_era = next(i for i, r in enumerate(inv87_era) if r['w'] == 'ce')
    ce_pos_mis = next(i for i, r in enumerate(inv87_mis) if r['w'] == 'ce')

    # ---- (c) 24-inversion redo under mixed-register model
    # legs: B* = P(ce|W) ~ P(87|24)=10/52=0.1923 ; C* = P(W|que,qu pooled) ~ P(24|46)=3/29=0.1034
    f24 = uni.get('24', 0)
    n24_87 = sum(1 for i, g in enumerate(pairs[:-1]) if g == '24' and pairs[i + 1] == '87')
    p87_24 = n24_87 / f24
    p24_46 = fol46.get('24', 0) / uni.get('46', 0)

    def invert24(c):
        nque = c.uni.get('que', 0) + c.uni.get('qu', 0)
        out = []
        for w, nw in c.uni.most_common(4000):
            if nw < 20:
                break
            pb = c.bi.get((w, 'ce'), 0) / nw                      # P(ce|W)
            pc = (c.bi.get(('que', w), 0) + c.bi.get(('qu', w), 0)) / nque  # P(W|que,qu)
            lb = within2(pb, p87_24)
            lc = within2(pc, p24_46)
            out.append({'w': w, 'n': nw, 'P_ce_given_W': round(pb, 4),
                        'P_W_given_quequ': round(pc, 4),
                        'legB': bool(lb), 'legC': bool(lc)})
        both = [r for r in out if r['legB'] and r['legC']]
        topB = sorted([r for r in out if r['legB']],
                      key=lambda r: abs(math.log2(max(r['P_ce_given_W'], 1e-9) / p87_24)))[:8]
        topC = sorted([r for r in out if r['legC']],
                      key=lambda r: abs(math.log2(max(r['P_W_given_quequ'], 1e-9) / p24_46)))[:8]
        return {'both': both, 'topB': topB, 'topC': topC}

    inv24_era = invert24(era)
    inv24_mis = invert24(mis)
    mixed_both_words = sorted({r['w'] for r in inv24_era['both']} |
                              {r['w'] for r in inv24_mis['both']})

    # ---- (d) 96-licenses-que / "par _ que" frames
    par_frames = collections.Counter()
    for (a, b, c_), n_ in era.tri.items():
        if a == 'par' and c_ == 'que':
            par_frames[b] += n_
    parce = era.uni.get('parce', 0)
    parce_que = era.bi.get(('parce', 'que'), 0)
    par_ce = era.bi.get(('par', 'ce'), 0)
    npar = era.uni.get('par', 0)

    frame96 = {
        'era_trigrams_par_W_que_top10': dict(par_frames.most_common(10)),
        'era_n_parce': parce, 'era_P_que_given_parce': round(parce_que / parce, 4) if parce else None,
        'era_n_par': npar, 'era_P_ce_given_par': round(par_ce / npar, 4) if npar else None,
        'cipher_P_87_given_96': round(n96_87 / f96, 4) if f96 else None,
        'cipher_P_46_given_87_pre96': '3/3',
        'cipher_P_46_given_87_pre24': '0/10',
        'cipher_87_46_predecessors': [p for p, _ in bg87_46],
        'rival_par_frame_counts': {R: era.tri.get(('par', R, 'que'), 0) for R in RIVALS + ['ce']},
    }

    results = {
        'meta': {'worker': 'closer (crowd3, WO4)', 'question': '87="ce" provisional resolution',
                 'ground_truth_anchors': ANCHORS},
        'cipher_87_profile': cipher87,
        'steelman_syllabary_aware': steel,
        'rival_battery_era': battery,
        'rival_grammar': grammar,
        'inversion_87': {
            'era_top15': inv87_era[:15], 'lesmis_top15': inv87_mis[:15],
            'ce_position_era': ce_pos_era, 'ce_position_lesmis': ce_pos_mis,
            'n_words_scored_era': len(inv87_era), 'n_words_scored_lesmis': len(inv87_mis),
            'era_pass_both_bigram_legs': [r['w'] for r in inv87_era if r['legs_bigram'] == 2][:20],
            'lesmis_pass_both_bigram_legs': [r['w'] for r in inv87_mis if r['legs_bigram'] == 2][:20],
        },
        'inversion_24_redo_mixed_register': {
            'cipher_legs': {'P_87_given_24': round(p87_24, 4), 'n24': f24,
                            'P_24_given_46': round(p24_46, 4)},
            'era_both': inv24_era['both'], 'era_topB': inv24_era['topB'], 'era_topC': inv24_era['topC'],
            'lesmis_both': inv24_mis['both'], 'lesmis_topB': inv24_mis['topB'], 'lesmis_topC': inv24_mis['topC'],
            'mixed_model_union_both': mixed_both_words,
            'mixed_model_definition': 'word fits if it passes legs under EITHER corpus (union)',
        },
        'frame96_par_que': frame96,
        'wilson_3_of_32': [round(x, 4) for x in wilson(3 / 32, 32)],
        'wilson_7_of_32': [round(x, 4) for x in wilson(7 / 32, 32)],
        'wilson_5_of_32': [round(x, 4) for x in wilson(5 / 32, 32)],
    }
    return results


if __name__ == '__main__':
    res = main()
    outdir = os.path.join(HERE, '')
    with open(os.path.join(HERE, 'closer_results.json'), 'w') as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
    print(json.dumps({
        'n_pairs': res['cipher_87_profile']['n_pairs'],
        'n_87': res['cipher_87_profile']['n_87'],
        'rank_87': res['cipher_87_profile']['rank_87'],
        'top_predecessors_of_11': res['cipher_87_profile']['top_predecessors_of_11'],
        'steelman': {k: {kk: v[kk] for kk in ('within2_la', 'within2_qui', 'within2_que')} for k, v in res['steelman_syllabary_aware'].items()},
        'ce_pos_87inv_era': res['inversion_87']['ce_position_era'],
        'ce_pos_87inv_lesmis': res['inversion_87']['ce_position_lesmis'],
        'era_both_bigram_pass': res['inversion_87']['era_pass_both_bigram_legs'],
        'mis_both_bigram_pass': res['inversion_87']['lesmis_pass_both_bigram_legs'],
        'inv24_era_both': [r['w'] for r in res['inversion_24_redo_mixed_register']['era_both']],
        'inv24_mis_both': [r['w'] for r in res['inversion_24_redo_mixed_register']['lesmis_both']],
        'mixed_union': res['inversion_24_redo_mixed_register']['mixed_model_union_both'],
        'par_frames': res['frame96_par_que']['era_trigrams_par_W_que_top10'],
        'parce': (res['frame96_par_que']['era_n_parce'], res['frame96_par_que']['era_P_que_given_parce']),
        'P_ce_given_par': res['frame96_par_que']['era_P_ce_given_par'],
    }, indent=1, ensure_ascii=False))
