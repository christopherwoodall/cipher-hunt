#!/usr/bin/env python3
"""Promotion battery v4 (crowd4) — B-78b repair + word-space function-word legs.

Repairs vs crowd3/code/crowd3/battery.py (do NOT edit crowd3 files):

R1 (B-78b, red-team-3b): ePpre divided by the WRONG marginal.
    Old: ePpre(s1, s2) = eb[(s1,s2)] / eu[s2]        -> P(s1|s2), WRONG
    New: ePpre(s1, s2) = eb[(s1,s2)] / eu[s1]        -> P(s2|s1), CORRECT
    Before: 11->78 L2 row: era P = 154/5617 = 0.02742 -> ratio 1.658 in-band.
    After:  11->78 L2 row: era P = 154/7652 = 0.02013 -> ratio 2.260 OUT of band.
    (ePfol was and is correct: P(follower|context).)

R2: L2prov (provisional-anchor legs) now computed in archived code, not by hand.
    Round-3's hand-computed L2prov numbers do not reproduce from archived code;
    every ratio below is machine-computed from the cipher stream + era corpus.

R3: word-space era legs for function-word hypotheses (pas/que/le/me).
    Cipher group-bigram rates vs era WORD-bigram rates (Tocqueville t1+t2).
    Per lane rule F30: no era-syllable-conditional legs on morphological
    fragments; era word-space legs survive (red-team-3b section g).

R4: calibration (N22) enforced in code:
    29/82/34 excluded from ALL legs; 40 excluded from conditional/attestation
    legs (B-78a extension: era 'e' syllable != cipher's word-final mute-e 40).

Band 0.5-2.0 is UNCALIBRATED (M3 standing): rates are context, never promotion
alone. Kills need cipher n>=3 AND era count 0 (grammatical kills additionally
need the construction to be genuinely ungrammatical, not merely unattested).

Anchor sets for word-space legs (monosyllabic word readings only):
  GT:   11=la, 46=que
  PROV: 87=ce, 64=qui, 96=par, 94=ne   (legs tagged provisional)
Excluded: 70=pre (fragment, not a word reading), 40=e (conditional legs),
29/82/34 (all legs).
"""
import sys, os, json, re, collections, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
CODE = os.path.join(HERE, '..')
DATA = os.path.join(CODE, '..', 'data')
sys.path.insert(0, CODE)
from crib_attack import load_pairs

ANCH_GT = {'11': 'la', '46': 'que'}
ANCH_PROV = {'87': 'ce', '64': 'qui', '96': 'par', '94': 'ne'}
EXCLUDED_ALL = {'29', '82', '34'}          # N22: excluded from every leg
EXCLUDED_COND = {'40'}                      # B-78a extension: no conditional/attestation legs

VOWELS = set('aeiouy')
LIQ = {'bl', 'cl', 'fl', 'gl', 'pl', 'br', 'cr', 'dr', 'fr', 'gr', 'pr', 'tr', 'vr'}
DIG = {'ch', 'ph', 'th', 'gn'}

def strip_acc(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

def syllabify(word):
    w = strip_acc(word.lower())
    if not w: return []
    toks = []; i, n = 0, len(w)
    while i < n:
        if w[i] in VOWELS:
            j = i
            while j < n and w[j] in VOWELS: j += 1
            toks.append(('V', w[i:j])); i = j
        else:
            j = i
            while j < n and w[j] not in VOWELS: j += 1
            toks.append(('C', w[i:j])); i = j
    syls, cur, idx = [], '', 0
    if toks and toks[0][0] == 'C': cur, idx = toks[0][1], 1
    while idx < len(toks):
        typ, val = toks[idx]
        if typ != 'V': cur += val; idx += 1; continue
        if idx + 1 < len(toks) and toks[idx+1][0] == 'C':
            cc = toks[idx+1][1]
            if idx + 2 < len(toks) and toks[idx+2][0] == 'V':
                onset = cc[-1]
                if len(cc) >= 2 and (cc[-2:] in LIQ or cc[-2:] in DIG): onset = cc[-2:]
                cur += val + cc[:-len(onset)]
                syls.append(cur); cur = onset; idx += 2
            else: cur += val + cc; idx += 2
        else: cur += val; idx += 1; syls.append(cur); cur = ''
    if cur: syls.append(cur)
    return [s for s in syls if s]

def load_words(path, keep_apos=False):
    text = open(path, encoding='utf-8', errors='replace').read().lower()
    m = re.search(r'\*\*\* start of.*?\*\*\*', text)
    if m: text = text[m.end():]
    m = re.search(r'\*\*\* end of.*', text)
    if m: text = text[:m.start()]
    pat = r"[a-zàâäéèêëîïôöùûüÿç']+" if keep_apos else r"[a-zàâäéèêëîïôöùûüÿç]+"
    return re.findall(pat, text)

class Models:
    def __init__(self):
        self.pairs, _, _ = load_pairs()
        self.N = len(self.pairs)
        self.cf = collections.Counter(self.pairs)
        self.cbi = collections.Counter(zip(self.pairs, self.pairs[1:]))
        # era syllable model (flattened stream; same instrument as battery.py)
        stream = []
        words = []
        for p in (os.path.join(DATA, 'gutenberg-30513-tocqueville-t1.txt'),
                  os.path.join(DATA, 'gutenberg-30514-tocqueville-t2.txt')):
            ws = load_words(p)
            words.extend(ws)
            for w in ws:
                stream.extend(syllabify(w))
        self.eu = collections.Counter(stream)
        self.eb = collections.Counter(zip(stream, stream[1:]))
        self.eN = len(stream)
        # era WORD model (R3: word-space legs for function words)
        self.words = words
        self.wu = collections.Counter(words)
        self.wb = collections.Counter(zip(words, words[1:]))
        self.wN = len(words)

    def cP(self, g): return self.cf[g] / self.N
    def eP(self, s): return self.eu.get(s, 0) / self.eN
    def wP(self, w): return self.wu.get(w, 0) / self.wN
    def cPfol(self, f, g):  # cipher P(f|g)
        return self.cbi.get((g, f), 0) / self.cf[g] if self.cf[g] else 0.0
    def cPpre(self, p, g):  # cipher P(g|p)
        return self.cbi.get((p, g), 0) / self.cf[p] if self.cf[p] else 0.0
    def ePfol(self, s2, s1):  # era syllable P(s2|s1)
        return self.eb.get((s1, s2), 0) / self.eu[s1] if self.eu.get(s1) else 0.0
    def ePpre(self, s1, s2):
        # R1 FIX (B-78b): era syllable P(s2|s1) = eb[(s1,s2)] / eu[s1].
        # The old code divided by eu[s2] (the hypothesis marginal) instead of
        # eu[s1] (the context marginal) -- e.g. P(la|me) instead of P(me|la).
        return self.eb.get((s1, s2), 0) / self.eu[s1] if self.eu.get(s1) else 0.0
    def ePpre_buggy(self, s1, s2):
        # the round-3 bug, kept for before/after display only
        return self.eb.get((s1, s2), 0) / self.eu[s2] if self.eu.get(s2) else 0.0
    def wPfol(self, w2, w1):  # era WORD P(w2|w1)
        return self.wb.get((w1, w2), 0) / self.wu[w1] if self.wu.get(w1) else 0.0
    def wPpre(self, w1, w2):  # era WORD P(w2|w1), called as wPpre(anchor, hyp)
        return self.wb.get((w1, w2), 0) / self.wu[w1] if self.wu.get(w1) else 0.0
    def followers(self, g):
        c = collections.Counter()
        for i, x in enumerate(self.pairs):
            if x == g and i + 1 < self.N: c[self.pairs[i+1]] += 1
        return c
    def predecessors(self, g):
        c = collections.Counter()
        for i, x in enumerate(self.pairs):
            if x == g and i - 1 >= 0: c[self.pairs[i-1]] += 1
        return c
    def e_followers(self, s):
        c = collections.Counter()
        for (a, b), n in self.eb.items():
            if a == s: c[b] = n
        return c

def inband(r): return r is not None and 0.5 <= r <= 2.0

def joint_frame_check(M, g, h, jg, jh):
    """Joint-consistency inventory for g=h jointly with jg=jh.
    jg: joint group number (e.g. '78'), jh: its reading (e.g. 'me').
    FENCED: only valid if the joint reading confirms. Not a promotion leg."""
    out = []
    n_g = M.cf[g]
    for (a, b), n in M.cbi.items():
        if n < 3: continue
        if a == g and b == jg:
            cp = n / n_g
            era = M.wb.get((h, jh), 0) / M.wu[h] if M.wu.get(h) else 0.0
            out.append({'frame': f'{g}={h}->{jg}={jh}', 'n': n,
                        'cipher_P': round(cp, 4), 'era_word_P': round(era, 6),
                        'ratio': round(cp / era, 2) if era else None,
                        'era_zero': era == 0})
        elif a == jg and b == g:
            cp = n / M.cf[a]
            era = M.wb.get((jh, h), 0) / M.wu[jh] if M.wu.get(jh) else 0.0
            out.append({'frame': f'{jg}={jh}->{g}={h}', 'n': n,
                        'cipher_P': round(cp, 4), 'era_word_P': round(era, 6),
                        'ratio': round(cp / era, 2) if era else None,
                        'era_zero': era == 0})
    return out

def run_battery4(M, g, hyps):
    """hyps: list of (reading, tag). reading must be a French word (R3 scope).
    Returns dict of leg results per reading."""
    out = {}
    cg = M.cf[g]
    fol = M.followers(g); pre = M.predecessors(g)
    anchors = [(a, r, 'GT') for a, r in ANCH_GT.items()] + \
              [(a, r, 'PROV') for a, r in ANCH_PROV.items()]
    for h, tag in hyps:
        cr = cg / M.N
        L1w = {'cipher_rate': round(cr, 5), 'era_word_rate': round(M.wP(h), 6),
               'ratio': round(cr / M.wP(h), 3) if M.wP(h) else None}
        L1w['in_band'] = inband(L1w['ratio'])
        L1s = {'era_syll_rate': round(M.eP(h), 6),
               'ratio': round(cr / M.eP(h), 3) if M.eP(h) else None}
        L1s['in_band'] = inband(L1s['ratio'])
        rows = []
        for a, r, astat in anchors:
            n_f = M.cbi.get((g, a), 0)   # anchor follows g
            n_p = M.cbi.get((a, g), 0)   # anchor precedes g
            if n_f >= 2:
                cp = M.cPfol(a, g)
                ep_fix = M.ePfol(r, h)          # syllable P(r|h), marginal correct
                ep_w = M.wPfol(r, h)            # word P(r|h)
                rows.append({
                    'dir': f'{g}->{a}({r})', 'n': n_f, 'anchor_status': astat,
                    'cipher': round(cp, 4),
                    'era_syll': round(ep_fix, 5),
                    'ratio_syll': round(cp / ep_fix, 3) if ep_fix else None,
                    'in_band_syll': inband(cp / ep_fix) if ep_fix else False,
                    'era_word': round(ep_w, 6),
                    'ratio_word': round(cp / ep_w, 3) if ep_w else None,
                    'in_band_word': inband(cp / ep_w) if ep_w else False,
                    'era_zero': ep_fix == 0 and ep_w == 0})
            if n_p >= 2:
                cp = M.cPpre(a, g)
                ep_fix = M.ePpre(r, h)          # syllable P(h|r) -- R1 FIXED marginal
                ep_bug = M.ePpre_buggy(r, h)    # round-3 value, for before/after
                ep_w = M.wPpre(r, h)            # word P(h|r)
                rows.append({
                    'dir': f'{a}({r})->{g}', 'n': n_p, 'anchor_status': astat,
                    'cipher': round(cp, 4),
                    'era_syll': round(ep_fix, 5),
                    'era_syll_buggy': round(ep_bug, 5),
                    'ratio_syll': round(cp / ep_fix, 3) if ep_fix else None,
                    'ratio_syll_buggy': round(cp / ep_bug, 3) if ep_bug else None,
                    'in_band_syll': inband(cp / ep_fix) if ep_fix else False,
                    'era_word': round(ep_w, 6),
                    'ratio_word': round(cp / ep_w, 3) if ep_w else None,
                    'in_band_word': inband(cp / ep_w) if ep_w else False,
                    'era_zero': ep_fix == 0 and ep_w == 0})
        # L3a-word: grammatical attestation kills, cipher n>=3, era word bigram 0
        kills = []
        for a, r, astat in anchors:
            if a in EXCLUDED_ALL or a in EXCLUDED_COND: continue
            if M.cbi.get((g, a), 0) >= 3 and M.wb.get((h, r), 0) == 0:
                kills.append({'frame': f'{g}={h}->{a}={r}', 'n': M.cbi[(g, a)],
                              'anchor_status': astat})
            if M.cbi.get((a, g), 0) >= 3 and M.wb.get((r, h), 0) == 0:
                kills.append({'frame': f'{a}={r}->{g}={h}', 'n': M.cbi[(a, g)],
                              'anchor_status': astat})
        L3a = {'kills': kills, 'pass': not kills}
        # L2b: concentration (structural; era side = syllable followers, unchanged)
        fvals = sorted(fol.values(), reverse=True)
        c_top3 = sum(fvals[:3]) / cg if cg else 0
        ef = M.e_followers(h); evals = sorted(ef.values(), reverse=True)
        e_top3 = sum(evals[:3]) / M.eu[h] if M.eu.get(h) else 0
        L2b = {'cipher_top3_share': round(c_top3, 3), 'era_top3_share': round(e_top3, 3),
               'ratio': round(c_top3 / e_top3, 3) if e_top3 else None}
        L2b['in_band'] = inband(L2b['ratio'])
        # L3b: coherent-frame inventory (era count, grammatical read)
        L3b = {'note': 'hand/ear territory; counts only'}
        out[h] = {'tag': tag, 'L1w': L1w, 'L1s': L1s, 'L2': rows,
                  'L2b': L2b, 'L3aw': L3a, 'L3b': L3b,
                  'top_fol': fol.most_common(6), 'top_pre': pre.most_common(6)}
    return out

def rival_battery78(M):
    """78 rival legs: 'l' (l') via syllable instrument (fixed marginal);
    'e' is a morphological fragment -- word-space N/A, L1 context only."""
    out = {}
    g = '78'
    # rival l': 11->78 x2 as "la l'"
    n_p = M.cbi.get(('11', '78'), 0)
    cp = M.cPpre('11', '78')
    ep = M.eb.get(('la', 'l'), 0) / M.eu['la'] if M.eu.get('la') else 0.0
    out['l'] = {'frame': '11=la->78', 'n': n_p, 'cipher_P': round(cp, 4),
                'era_P_l_given_la': round(ep, 6),
                'ratio': round(cp / ep, 1) if ep else None,
                'grammatical': '"la l\'" ungrammatical'}
    # rival e: fragment, untestable by word-space; L1 context only
    cr = M.cf[g] / M.N
    out['e'] = {'L1_ratio': round(cr / M.eP('e'), 3) if M.eP('e') else None,
                'note': 'fragment hypothesis; B-78a voided the e-e kill; stays live rival'}
    return out

def main():
    M = Models()
    out = {'meta': {
        'worker': 'bigram_closer_round4', 'date': '2026-10-07',
        'cipher': 'R5005 1846 pairs / 96 groups',
        'era': 'Tocqueville t1+t2; syllable stream + word tokens=%d' % M.wN,
        'repairs': ['B-78b: ePpre marginal fixed (divides by eu[s1])',
                    'L2prov in archived code (was hand-computed)',
                    'word-space legs for function-word hypotheses',
                    'N22: 29/82/34 excluded all legs; 40 excluded conditionals'],
        'band': '0.5-2.0 UNCALIBRATED: rates are context, never promotion alone',
        'kill_rule': 'cipher n>=3 AND era count 0'}}
    for g, hyps in [('77', [('pas', 'incumbent'), ('que', 'challenger'), ('le', 'own-best')]),
                    ('78', [('me', 'lead'), ('e', 'rival-fragment')])]:
        out[g] = run_battery4(M, g, hyps)
    out['78']['rival_legs'] = rival_battery78(M)
    # joint-consistency inventory: 77 readings x 78=me (FENCED, not a leg)
    out['joint_77x78me'] = {h: joint_frame_check(M, '77', h, '78', 'me')
                            for h in ('pas', 'que', 'le')}
    with open(os.path.join(HERE, 'battery4_results.json'), 'w') as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
    print('wrote', os.path.join(HERE, 'battery4_results.json'))

if __name__ == '__main__':
    main()
