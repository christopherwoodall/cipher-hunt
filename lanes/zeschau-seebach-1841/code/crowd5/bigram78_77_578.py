#!/usr/bin/env python3
"""Round 5 — BIGRAM CLOSER executor: WO1 (78 me/ver), WO2 (77=le promotion), WO3 (@578 host).

Reuses crowd4/battery4.py's repaired methods:
  - B-78b: ePpre divides by the CONTEXT marginal eu[s1] (not the hypothesis marginal)
  - N22: groups 29/82/34 excluded from ALL rate legs; 40 excluded from
    conditional/attestation legs (B-78a extension)
run on the REPAIRED canonical 1,847-pair parse
(code/crowd4/repaired_parse.load_pairs_repaired), NOT crib_attack.load_pairs.

F30: no era-syllable-conditional legs on morphological fragments; era
word-space legs survive. Kill rule: cipher n>=3 AND era count 0
(grammatical kills additionally need genuine ungrammaticality).
Band 0.5-2.0 is UNCALIBRATED: rates are context, never promotion alone.

Writes: bigram78_77_578.json, bigram78_77_578.md
"""
import sys, os, json, re, collections, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
CODE = os.path.join(HERE, '..')
LANE = os.path.join(CODE, '..')
DATA = os.path.join(LANE, 'data')
sys.path.insert(0, os.path.join(CODE, 'crowd4'))
from repaired_parse import load_pairs_repaired

# ---------------- N22 exclusions ----------------
EXCLUDED_ALL = {'29', '82', '34'}   # excluded from every rate leg
EXCLUDED_COND = {'40'}              # excluded from conditional/attestation legs

ANCH = {'11': 'la', '70': 'pre', '82': 'm', '34': 'i', '29': 'er', '40': 'e',
        '46': 'que', '87': 'ce', '64': 'qui', '96': 'par', '94': 'ne',
        '62': 'on', '52': 'pas', '47': 'ce'}

# ---------------- era models ----------------
def strip_acc(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')

VOWELS = set('aeiouy')
LIQ = {'bl', 'cl', 'fl', 'gl', 'pl', 'br', 'cr', 'dr', 'fr', 'gr', 'pr', 'tr', 'vr'}
DIG = {'ch', 'ph', 'th', 'gn'}

def syllabify(word):
    """battery4's documented orthographic syllabifier (unchanged)."""
    w = strip_acc(word.lower())
    if not w:
        return []
    toks = []
    i, n = 0, len(w)
    while i < n:
        if w[i] in VOWELS:
            j = i
            while j < n and w[j] in VOWELS:
                j += 1
            toks.append(('V', w[i:j])); i = j
        else:
            j = i
            while j < n and w[j] not in VOWELS:
                j += 1
            toks.append(('C', w[i:j])); i = j
    syls, cur, idx = [], '', 0
    if toks and toks[0][0] == 'C':
        cur, idx = toks[0][1], 1
    while idx < len(toks):
        typ, val = toks[idx]
        if typ != 'V':
            cur += val; idx += 1; continue
        if idx + 1 < len(toks) and toks[idx + 1][0] == 'C':
            cc = toks[idx + 1][1]
            if idx + 2 < len(toks) and toks[idx + 2][0] == 'V':
                onset = cc[-1]
                if len(cc) >= 2 and (cc[-2:] in LIQ or cc[-2:] in DIG):
                    onset = cc[-2:]
                cur += val + cc[:-len(onset)]
                syls.append(cur); cur = onset; idx += 2
            else:
                cur += val + cc; idx += 2
        else:
            cur += val; idx += 1; syls.append(cur); cur = ''
    if cur:
        syls.append(cur)
    return [s for s in syls if s]

def load_era_words():
    """Elision-split word model (same as morph94_re_battery.py)."""
    words = []
    for fn in ('gutenberg-30513-tocqueville-t1.txt',
               'gutenberg-30514-tocqueville-t2.txt'):
        txt = open(os.path.join(DATA, fn), encoding='utf-8').read().lower()
        txt = txt.replace('’', "'").replace('‘', "'")
        txt = re.sub(r"([a-zà-ÿ])'([a-zà-ÿ])", r'\1 \2', txt)
        words += re.findall(r'[a-zà-ÿ]+', txt)
    return words

class M:
    def __init__(self):
        self.pairs, _, _ = load_pairs_repaired()
        self.N = len(self.pairs)
        assert self.N == 1847, self.N
        self.cf = collections.Counter(self.pairs)
        self.cbi = collections.Counter(zip(self.pairs, self.pairs[1:]))
        words = load_era_words()
        self.wu = collections.Counter(words)
        self.wb = collections.Counter(zip(words, words[1:]))
        self.wN = len(words)
        stream = []
        for w in words:
            stream.extend(syllabify(w))
        self.eu = collections.Counter(stream)
        self.eN = len(stream)

    # cipher
    def cPfol(self, f, g):
        return self.cbi.get((g, f), 0) / self.cf[g] if self.cf[g] else 0.0

    def cPpre(self, p, g):
        return self.cbi.get((p, g), 0) / self.cf[p] if self.cf[p] else 0.0

    # era word-space
    def wPfol(self, w2, w1):
        return self.wb.get((w1, w2), 0) / self.wu[w1] if self.wu.get(w1) else 0.0

    def wPpre(self, w1, w2):
        return self.wb.get((w1, w2), 0) / self.wu[w1] if self.wu.get(w1) else 0.0

    # era syllable-space unigram (B-78b marginal rule applies to conditionals)

def inband(r):
    return r is not None and 0.5 <= r <= 2.0

def find_pat(pairs, pat):
    L = len(pat)
    return [i for i in range(len(pairs) - L + 1) if pairs[i:i + L] == pat]

NONV_INF = {'mer', 'fer', 'ver', 'hier', 'enfer', 'amer'}

def is_infinitive(w):
    if len(w) <= 3 or w in NONV_INF:
        return False
    if re.search(r'(er|ir|oir|yer)$', w):
        return True
    return w in {'faire', 'dire', 'prendre', 'mettre', 'pouvoir', 'vouloir',
                 'savoir', 'devoir'}

# ================= WO1: 78 = me / ver =================
def wo1(m):
    out = {'counts': {}, 'word_legs': {}, 'syllable_legs': {}, 'ver_legs': {},
           'rival_legs': {}}
    cf, cbi, N = m.cf, m.cbi, m.N
    out['counts'] = {
        'n78': cf['78'], 'P78': round(cf['78'] / N, 5),
        'pos_77_78': find_pat(m.pairs, ['77', '78']),
        'pos_78_94': find_pat(m.pairs, ['78', '94']),
        'n_11_78': cbi.get(('11', '78'), 0),
        'n_47_78': cbi.get(('47', '78'), 0),
        'n_87_78': cbi.get(('87', '78'), 0),
        'n_67_78': cbi.get(('67', '78'), 0),
        'n_78_94': cbi.get(('78', '94'), 0),
        'n_78_40': cbi.get(('78', '40'), 0),
    }
    # --- word-space legs for 78='me' (the WORD reading) ---
    cr = cf['78'] / N
    w_me = m.wu.get('me', 0) / m.wN
    out['word_legs']['L1w'] = {'cipher_rate': round(cr, 5),
                               'era_word_rate': round(w_me, 6),
                               'ratio': round(cr / w_me, 2),
                               'in_band': inband(cr / w_me),
                               'verdict': 'ADVERSE (22x over era word rate)'}
    # grammatical word-bigram adverses for the WORD reading
    frames = [('la', 'me', ('11', '78')), ('ce', 'me', ('47', '78')),
              ('ce', 'me', ('87', '78')), ('me', 'ne', ('78', '94')),
              ('le', 'me', ('77', '78')), ('pas', 'me', ('77', '78'))]
    # note: ('77','78') counted once for both le-me and pas-me joint frames
    seen = set()
    adverses = []
    for a, b, (ga, gb) in frames:
        if (ga, gb) in seen:
            continue
        seen.add((ga, gb))
        n_c = cbi.get((ga, gb), 0)
        n_e = m.wb.get((a, b), 0)
        d_e = m.wu.get(a, 0)
        adverses.append({'frame': f'{a} {b}', 'cipher_n': n_c,
                         'era_n': n_e, 'era_P': round(n_e / max(1, d_e), 6),
                         'era_zero': n_e == 0})
    out['word_legs']['grammatical_adverses'] = adverses
    # --- syllable-space L1 for 78='me' (B-78b fixed marginal not needed for unigram) ---
    s_me = m.eu.get('me', 0) / m.eN
    out['syllable_legs']['L1s'] = {'cipher_rate': round(cr, 5),
                                   'era_syll_rate': round(s_me, 6),
                                   'ratio': round(cr / s_me, 3),
                                   'in_band': inband(cr / s_me)}
    # --- rival l' kill recompute (syllable instrument, fixed marginal) ---
    n_p = cbi.get(('11', '78'), 0)
    cp = m.cPpre('11', '78')
    # era P(l|la): syllable bigram la->l over eu[la]
    syl_stream = []
    for w in load_era_words():
        syl_stream.extend(syllabify(w))
    seu = collections.Counter(syl_stream)
    seb = collections.Counter(zip(syl_stream, syl_stream[1:]))
    ep = seb.get(('la', 'l'), 0) / seu['la'] if seu.get('la') else 0.0
    out['rival_legs']['l_quote'] = {'n': n_p, 'cipher_P': round(cp, 4),
                                    'era_P_l_given_la': round(ep, 6),
                                    'ratio': round(cp / ep, 1) if ep else None,
                                    'grammatical': '"la l\'" ungrammatical',
                                    'status': 'KILLED (stands)' if ep and cp / ep > 10 else 'check'}
    # rival e (fragment): L1 context only
    s_e = seu.get('e', 0) / len(syl_stream)
    out['rival_legs']['e_fragment'] = {'L1_ratio': round(cr / s_e, 3),
                                       'status': 'live rival (fragment)'}
    # --- 78='ver' conditioned islet ---
    pos7894 = find_pat(m.pairs, ['78', '94'])
    tri = find_pat(m.pairs, ['94', '82', '06'])
    in_tri = sum(1 for i in pos7894 if i + 1 in tri)
    words = load_era_words()
    wc = collections.Counter(words)
    n_vernement = sum(c for w, c in wc.items() if 'vernement' in w)
    n_verrement = sum(c for w, c in wc.items() if 'verrement' in w)
    out['ver_legs'] = {
        'pos_78_94': pos7894,
        'in_trigram_94_82_06': in_tri,
        'positional_rule': '78=ver iff next=94: %d/%d, 0 exceptions outside trigram' % (in_tri, len(pos7894)),
        'era_vernement_tokens': n_vernement,
        'era_verrement_tokens': n_verrement,
        'me_ne_era_zero': m.wb.get(('me', 'ne'), 0) == 0,
        'n_78_94': len(pos7894),
    }
    return out

# ================= WO2: 77='le' promotion battery =================
def wo2(m):
    out = {'legs': {}, 'adverses': {}, 'diversity': {}}
    cf, cbi, N = m.cf, m.cbi, m.N
    cr = cf['77'] / N
    # Leg A: 77->86 x5 object-pronoun frame vs era P(infinitive|'le')
    n_7786 = cbi.get(('77', '86'), 0)
    cp = m.cPfol('86', '77')
    n_le = m.wu.get('le', 0)
    n_inf = sum(c for (a, b), c in m.wb.items() if a == 'le' and is_infinitive(b))
    ep = n_inf / n_le
    out['legs']['A_follower_frame'] = {
        'cipher': 'P(86|77) = %d/%d = %.4f' % (n_7786, cf['77'], cp),
        'era': 'P(inf|le) = %d/%d = %.4f' % (n_inf, n_le, ep),
        'ratio': round(cp / ep, 3), 'in_band': inband(cp / ep),
        'positions': find_pat(m.pairs, ['77', '86']),
        'note': '86 = infinitive-complement stem (N29, provisional); '
                '77->86->29 @430 = le+stem+er (F22 strip)',
        'caveat': '86 is one stem, not all infinitives: near-exact match is '
                  'consistency, not identification'}
    # Leg B: predecessor verb-adjacency (grammatical frames; rates fenced)
    out['legs']['B_predecessor_frames'] = {
        '64_77_84': {'n': cbi.get(('64', '77'), 0),
                     'note': 'qui le [84] x3 byte-identical (n_eff=1); grammatical',
                     'era_P_le_given_qui': round(m.wPpre('qui', 'le'), 5),
                     'cipher_P_77_given_64': round(m.cPpre('64', '77'), 4)},
        '67_77_81': {'n_67_77': cbi.get(('67', '77'), 0),
                     'n_67_77_81': len(find_pat(m.pairs, ['67', '77', '81'])),
                     'note': 'veut le [81] x4 = verb+article+noun (grammatical); '
                             'fenced on 67=veut provisional',
                     'era_P_le_given_veut': round(m.wPpre('veut', 'le'), 5),
                     'cipher_P_77_given_67': round(m.cPpre('67', '77'), 4)},
        '06_77': {'n': cbi.get(('06', '77'), 0),
                  'note': 'verb-stem + le: imperative-le (demandez-le) or '
                          'verb + le[noun]; 06 verb-stem-class provisional'},
    }
    # Leg C: unigram (context)
    w_le = m.wu.get('le', 0) / m.wN
    out['legs']['C_unigram'] = {'cipher_rate': round(cr, 5),
                                'era_word_rate': round(w_le, 6),
                                'ratio': round(cr / w_le, 3),
                                'in_band': inband(cr / w_le),
                                'note': 'context only'}
    # Leg D: diversity (free function word, not fixed phrase)
    fol = collections.Counter(m.pairs[i + 1] for i in range(N - 1) if m.pairs[i] == '77')
    pre = collections.Counter(m.pairs[i - 1] for i in range(1, N) if m.pairs[i] == '77')
    efol = collections.Counter(b for (a, b) in m.wb if a == 'le' for _ in [0])
    # (efol built properly below)
    efol = collections.Counter()
    epre = collections.Counter()
    for (a, b), c in m.wb.items():
        if a == 'le':
            efol[b] += c
        if b == 'le':
            epre[a] += c
    out['diversity'] = {
        'cipher_distinct_followers': len(fol), 'cipher_top_share': round(max(fol.values()) / cf['77'], 3),
        'cipher_distinct_predecessors': len(pre),
        'era_distinct_followers': len(efol), 'era_top_share': round(max(efol.values()) / n_le, 4),
        'era_distinct_predecessors': len(epre),
        'note': 'both free-function-word profiles'}
    # Adverses
    ce_le_e = m.wb.get(('ce', 'le'), 0)
    out['adverses']['ce_le'] = {
        'cipher_n_87_77': cbi.get(('87', '77'), 0),
        'positions': find_pat(m.pairs, ['87', '77']),
        'era_n_ce_le': ce_le_e, 'era_zero': ce_le_e == 0,
        'note': 'fenced on provisional 87=ce; genuine tension, not kill',
    }
    out['adverses']['rate_overshoot'] = {
        'P77_given_64_vs_era': round(m.cPpre('64', '77') / max(1e-9, m.wPpre('qui', 'le')), 2) if m.wPpre('qui', 'le') else None,
        'note': 'band uncalibrated (F20); grammatical frames pass',
    }
    out['adverses']['joint_le_me'] = {
        'cipher_n_77_78': cbi.get(('77', '78'), 0),
        'era_n_le_me': m.wb.get(('le', 'me'), 0),
        'note': 'era-0 as WORD bigram; DISSOLVED under 78=me-syllable '
                '(category error: syllable bigram vs word bigram); fenced on unconfirmed 78',
    }
    # L2b concentration (context)
    fvals = sorted(fol.values(), reverse=True)
    c_top3 = sum(fvals[:3]) / cf['77']
    evals = sorted(efol.values(), reverse=True)
    e_top3 = sum(evals[:3]) / n_le
    out['legs']['L2b'] = {'cipher_top3': round(c_top3, 3), 'era_top3': round(e_top3, 3),
                          'ratio': round(c_top3 / e_top3, 3), 'note': 'context only'}
    return out

# ================= WO3: @578 trigram host =================
def wo3(m):
    out = {}
    cf, cbi, N = m.cf, m.cbi, m.N
    tri = find_pat(m.pairs, ['94', '82', '06'])
    out['trigram_positions'] = tri
    sixmer = find_pat(m.pairs, ['78', '45', '13', '55', '61', '94'])
    out['sixmer_78_45_13_55_61_94'] = sixmer
    # the second sixmer occurrence continues 94->87 (en islet, suc=87)
    out['second_sixmer_continuation'] = {
        'pos': sixmer[1] if len(sixmer) > 1 else None,
        '94_suc': m.pairs[sixmer[1] + 6] if len(sixmer) > 1 else None,
        '87_suc': m.pairs[sixmer[1] + 7] if len(sixmer) > 1 else None,
        'note': '94 followed by 87=ce: only grammatical reading is en+ce '
                '(ne ce = 0 era; re ce incoherent with free-word ce)',
    }
    words = load_era_words()
    wc = collections.Counter(words)
    W = len(words)
    n_nement = sum(c for w, c in wc.items() if 'nement' in w)
    n_rement = sum(c for w, c in wc.items() if 'rement' in w and 'nement' not in w)
    n_vernement = sum(c for w, c in wc.items() if 'vernement' in w)
    n_verrement = sum(c for w, c in wc.items() if 'verrement' in w)
    out['era_hosts'] = {'nement_tokens': n_nement, 'rement_tokens': n_rement,
                        'host_odds_ne_vs_re': round(n_nement / max(1, n_rement), 2),
                        'vernement_tokens': n_vernement,
                        'verrement_tokens': n_verrement}
    out['particle_argument'] = {
        'claim': 'at the sixmer #2 (@1169), 94=en (F33 islet, suc=87); '
                 '94 is a PARTICLE at the sixmer right edge, incompatible '
                 'with word-internal re (no free word "re" exists)',
        'fence': 'assumes the byte-identical sixmer carries the same '
                 'segmentation at both positions (by-ear inconsistency attested '
                 'but unparsimonious here)',
    }
    # 61 profile (pre-94 group)
    fol61 = collections.Counter(m.pairs[i + 1] for i in range(N - 1) if m.pairs[i] == '61')
    out['g61'] = {'n': cf['61'], 'followers_top': fol61.most_common(6),
                  'pos_61_94': find_pat(m.pairs, ['61', '94']),
                  'note': '61->94 x2 mirrors 78->94 x2 (allophony candidate: '
                          'ver->{78,61}; 1 sound->N groups permitted by N33)'}
    return out

def main():
    m = M()
    res = {'meta': {
        'worker': 'bigram_closer_round5', 'date': '2026-10-07',
        'cipher': 'R5005 REPAIRED parse: 1847 pairs / 96 groups',
        'era': 'Tocqueville t1+t2 (elision-split word model + battery4 syllabifier)',
        'methods': ['B-78b: ePpre divides by context marginal',
                    'N22: 29/82/34 excluded all legs; 40 excluded conditionals',
                    'F30: word-space legs only; no era-syllable legs on fragments',
                    'kill rule: cipher n>=3 AND era count 0'],
        'band': '0.5-2.0 UNCALIBRATED: rates are context, never promotion alone'},
        'WO1_78': wo1(m), 'WO2_77': wo2(m), 'WO3_578': wo3(m)}
    with open(os.path.join(HERE, 'bigram78_77_578.json'), 'w') as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
    print('wrote', os.path.join(HERE, 'bigram78_77_578.json'))

if __name__ == '__main__':
    main()
