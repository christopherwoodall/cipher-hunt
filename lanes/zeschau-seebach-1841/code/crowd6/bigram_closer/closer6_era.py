#!/usr/bin/env python3
"""Round 6 closer, part 2: era inversions for (a) 84=noun and (c) 78-45=meme.

Word-space only (F30-legal). Two tokenizers:
 - SPLIT: elision-split (bigram78_77_578 style) — for "me"-morpheme counts
 - PLAIN: closer87_angles style (no elision split) — for article frames
"""
import os, re, json, collections

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
DATA = os.path.join(LANE, 'data')
HERE = os.path.dirname(os.path.abspath(__file__))

def load_plain():
    W = []
    for fn in ('gutenberg-30513-tocqueville-t1.txt',
               'gutenberg-30514-tocqueville-t2.txt'):
        text = open(os.path.join(DATA, fn), encoding='utf-8').read().lower()
        m = re.search(r'\*\*\* start of.*?\*\*\*', text)
        if m: text = text[m.end():]
        m = re.search(r'\*\*\* end of.*', text)
        if m: text = text[:m.start()]
        W += re.findall(r"[a-zàâäéèêëîïôöùûüÿç]+", text)
    return W

def load_split():
    W = []
    for fn in ('gutenberg-30513-tocqueville-t1.txt',
               'gutenberg-30514-tocqueville-t2.txt'):
        txt = open(os.path.join(DATA, fn), encoding='utf-8').read().lower()
        txt = txt.replace('\u2019', "'").replace('\u2018', "'")
        txt = re.sub(r"([a-z\u00e0-\u00ff])'([a-z\u00e0-\u00ff])", r'\1 \2', txt)
        W += re.findall(r'[a-z\u00e0-\u00ff]+', txt)
    return W

P = load_plain(); S = load_split()
PBI = list(zip(P, P[1:])); SBI = list(zip(S, S[1:]))
PU = collections.Counter(P); PB = collections.Counter(PBI); PN = len(P)
SU = collections.Counter(S); SB = collections.Counter(SBI); SN = len(S)

def inband(r): return r is not None and 0.5 <= r <= 2.0

out = {}
p84 = 25 / 1847  # cipher P(84)

# ---- (a) 84 = noun: era article frames -------------------------------------
le_fol = collections.Counter(w2 for (w1, w2) in PBI if w1 == 'le')
la_fol = collections.Counter(w2 for (w1, w2) in PBI if w1 == 'la')
# candidate nouns: top followers of both articles
cands = {}
for w, n in le_fol.most_common(40):
    if la_fol[w] >= 3:  # attested after both articles
        cands[w] = (n, la_fol[w])
inv = out['a_noun_inversion'] = []
for w, (nle, nla) in sorted(cands.items(), key=lambda kv: -(kv[1][0] + kv[1][1])):
    pw = PU[w] / PN
    r = p84 / pw
    inv.append({'w': w, 'n_le': nle, 'n_la': nla, 'era_n': PU[w],
                'ratio': round(r, 3), 'inband': inband(r)})
out['a_n_le_total'] = sum(le_fol.values())
out['a_n_la_total'] = sum(la_fol.values())
# re-verify 84="fait" kill
pfait = PU['fait'] / PN
out['a_fait_kill'] = {'era_n_fait': PU['fait'], 'era_p': pfait,
                      'ratio': round(p84 / pfait, 3)}
# era P(verb | "qui le") is sparse (n=12) — record the Les Mis check too
LM = []
lm_path = os.path.join(DATA, 'gutenberg-17489-miserables1.txt')
if os.path.exists(lm_path):
    text = open(lm_path, encoding='utf-8').read().lower()
    LM = re.findall(r"[a-zàâäéèêëîïôöùûüÿç]+", text)
LMU = collections.Counter(LM); LMB = collections.Counter(zip(LM, LM[1:]))
lm_qle = collections.Counter(w2 for (w1, w2) in LMB if w1 == 'qui' and False)
# trigram qui le W in les mis
lm_tri = collections.Counter()
for i in range(len(LM) - 2):
    if LM[i] == 'qui' and LM[i+1] == 'le':
        lm_tri[LM[i+2]] += 1
out['a_lesmis_qui_le'] = {'n': sum(lm_tri.values()), 'top': lm_tri.most_common(10)}
tq_tri = collections.Counter()
for i in range(len(P) - 2):
    if P[i] == 'qui' and P[i+1] == 'le':
        tq_tri[P[i+2]] += 1
out['a_tocq_qui_le'] = {'n': sum(tq_tri.values()), 'top': tq_tri.most_common(12)}

# ---- (c) 45="me" word vs 78-45="meme" ----------------------------------------
# me-morpheme in split model: "m" (elided) + "me"
n_me_morph = SU['m'] + SU['me']
p_me_morph = n_me_morph / SN
p45 = 22 / 1847
c45 = out['c_45'] = {}
c45['me_morpheme'] = {'n_m': SU['m'], 'n_me': SU['me'], 'n': n_me_morph,
                      'p': p_me_morph,
                      'ratio_cipher_over_era': round(p45 / p_me_morph, 3),
                      'inband': inband(p45 / p_me_morph)}
c45['par_me'] = SB.get(('par', 'me'), 0)          # 96->45 x2 adverse
c45['me_qui'] = SB.get(('me', 'qui'), 0)          # 45->64 x3 adverse
c45['m_qui'] = SB.get(('m', 'qui'), 0)
c45['par_m'] = SB.get(('par', 'm'), 0)
# "meme" hypothesis: 78-45 = me|me
n_meme = SU['m\u00eame'] + PU['m\u00eame']
c45['meme'] = {'era_n_split': SU['m\u00eame'], 'era_n_plain': PU['m\u00eame'],
               'era_p_plain': PU['m\u00eame'] / PN,
               'cipher_P78_45': 4 / 1847,
               'ratio': round((4 / 1847) / (PU['m\u00eame'] / PN), 3)
                       if PU['m\u00eame'] else None}
c45['le_meme'] = PB.get(('le', 'm\u00eame'), 0)    # @313 lock
c45['meme_qui'] = PB.get(('m\u00eame', 'qui'), 0)  # @313 lock
c45['ce_meme'] = PB.get(('ce', 'm\u00eame'), 0)    # @982
c45['meme_era_n_le'] = PU['le']
# sanity: era ("le","me") re-derived on plain model
c45['le_me_plain'] = PB.get(('le', 'me'), 0)

json.dump(out, open(os.path.join(HERE, 'closer6_era.json'), 'w'),
          indent=1, ensure_ascii=False)
print('wrote closer6_era.json')
print('== (a) noun inversion (top 20) ==')
for r in inv[:20]:
    print('  %(w)-14s le=%(n_le)-4d la=%(n_la)-3d era_n=%(era_n)-5d ratio=%(ratio).2f %(s)s' %
          dict(r, **{'s': 'IN' if r['inband'] else '--'}))
print('fait kill ratio:', out['a_fait_kill']['ratio'])
print('tocq qui le:', out['a_tocq_qui_le'])
print('lesmis qui le:', out['a_lesmis_qui_le'])
print('== (c) ==')
print(json.dumps(c45, indent=1, ensure_ascii=False))
