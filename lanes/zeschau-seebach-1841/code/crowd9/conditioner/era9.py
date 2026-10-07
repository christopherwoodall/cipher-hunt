#!/usr/bin/env python3
"""Round-9 conditioner: era-corpus batteries (Nesselrode v8, elision-split)."""
import collections, json, os, re

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
C = os.path.join(LANE, 'code', 'side-period', 'corpus')

def era_words(filepaths):
    words = []
    for fp in filepaths:
        txt = open(fp, encoding='utf-8', errors='replace').read().lower()
        txt = txt.replace('\u2019', "'").replace('\u2018', "'")
        txt = re.sub(r"([a-z\u00e0-\u00ff])'([a-z\u00e0-\u00ff])", r'\1 \2', txt)
        words += re.findall(r'[a-z\u00e0-\u00ff]+', txt)
    return words

def fp(n):
    return os.path.join(C, n)

# French-only pool per ratemodel H-LANG: 97 Nesselrode letters + 746 levant
# French paragraphs. Rebuild: nesselrode-v8.txt is French; for levant use
# French-majority paragraphs. Simpler: use nesselrode-v8 alone (pure French)
# + levant French paragraphs via the ratemodel's own pool if cached.
primary = [fp('nesselrode-v8.txt'), fp('levant-correspondence-1841-p3.txt')]
w = era_words(primary)
N = len(w)
wu = collections.Counter(w)
bi = collections.Counter(zip(w, w[1:]))
tri = collections.Counter(zip(w, w[1:], w[2:]))
OUT = {'N': N}

def P(num, den):
    return num / den if den else 0.0

print('N =', N)
# ---- A. pour / que rates ----
n_pour = wu['pour']
OUT['pour'] = {'n': n_pour, 'P': P(n_pour, N)}
OUT['que_given_pour'] = {'n': bi[('pour', 'que')], 'P': P(bi[('pour', 'que')], n_pour)}
OUT['qu_given_pour'] = {'n': bi[('pour', 'qu')], 'P': P(bi[('pour', 'qu')], n_pour)}
print('P(pour)=%.5f  P(que|pour)=%.4f (n=%d)  P(qu|pour)=%.4f (n=%d)' % (
    P(n_pour, N), P(bi[('pour', 'que')], n_pour), bi[('pour', 'que')],
    P(bi[('pour', 'qu')], n_pour), bi[('pour', 'qu')]))

# ---- D. pour + subject pronoun (should be ~0) ----
prons = ['il', 'elle', 'on', 'nous', 'vous', 'ils', 'elles', 'je', 'tu']
d = {p: bi[('pour', p)] for p in prons}
OUT['pour_pron'] = d
print('pour+pronoun:', d)

# ---- B. «qui le X Y» frame parse ----
# collect all (x, y) after 'qui le'
qly = collections.Counter()
for a, b, c, d_ in zip(w, w[1:], w[2:], w[3:]):
    if a == 'qui' and b == 'le':
        qly[(c, d_)] += 1
OUT['qui_le_n'] = sum(qly.values())
# verb list heuristic: infinitives/participles/3sg forms from corpus
verbs = set(x for x in wu if re.fullmatch(
    r'[a-z\u00e0-\u00ff]*(er|ir|re|oir|dre|tre|ttre|indre|oudre|soudre)\b', x)
    and len(x) > 3)
# common conjugated forms list (3sg present indicative frequent after 'qui le')
conj3sg = set()
for x in ['rend', 'fait', 'veut', 'peut', 'doit', 'sait', 'voit', 'croit',
          'prend', 'met', 'dit', 'concerne', 'croirait', 'composent',
          'demande', 'regarde', 'oblige', 'touche', 'porte', 'donne',
          're\u00e7oit', 'exige', 'prouve', 'montre', 'trouve', 'laisse',
          'rendit', 'fit', 'voulut', 'put', 'dut', 'sut', 'vit', 'crut']:
    conj3sg.add(x)
n_verb_xy = 0   # x+y concatenated is a known verb form (bisyllabic verb)
n_y_est = 0     # y == 'est' (noun + est frame)
n_x_verb = 0    # x alone is a verb form (monosyllabic verb)
examples_verb, examples_est = [], []
for (x, y), n in qly.most_common(60):
    xy = x + y
    if y == 'est':
        n_y_est += n
        if len(examples_est) < 8:
            examples_est.append(((x, y), n))
    elif xy in verbs or xy in conj3sg or x in conj3sg or x in verbs:
        if xy in verbs or xy in conj3sg:
            n_verb_xy += n
            if len(examples_verb) < 8:
                examples_verb.append(((x, y), n))
        else:
            n_x_verb += n
OUT['qui_le_frame'] = {'n_total': sum(qly.values()), 'n_y_est': n_y_est,
                       'n_xy_verb': n_verb_xy, 'n_x_verb': n_x_verb,
                       'ex_verb': examples_verb, 'ex_est': examples_est,
                       'top': [[list(k), v] for k, v in qly.most_common(25)]}
print('«qui le X Y»: n=%d  y=est: %d  xy=verb: %d  x=verb: %d' % (
    sum(qly.values()), n_y_est, n_verb_xy, n_x_verb))
print('  top:', qly.most_common(12))

# ---- «ce qui le X Y» specifically ----
cqly = collections.Counter()
for a, b, c, d_, e in zip(w, w[1:], w[2:], w[3:], w[4:]):
    if a == 'ce' and b == 'qui' and c == 'le':
        cqly[(d_, e)] += 1
OUT['ce_qui_le'] = {'n': sum(cqly.values()),
                    'top': [[list(k), v] for k, v in cqly.most_common(15)]}
print('«ce qui le X Y»: n=%d top=%s' % (sum(cqly.values()), cqly.most_common(10)))

# ---- C. «qui [V] me» rate ----
# verb = any infinitive-form or common 3sg; check «qui V me» with V in verb set
qvme = sum(1 for a, b, c in zip(w, w[1:], w[2:])
           if a == 'qui' and c == 'me' and (b in verbs or b in conj3sg))
OUT['qui_V_me'] = qvme
print('«qui [V] me» n =', qvme)
# and «qui V X» for X in {me, que, ...}: what follows qui+V?
qvx = collections.Counter()
for a, b, c in zip(w, w[1:], w[2:]):
    if a == 'qui' and (b in verbs or b in conj3sg):
        qvx[c] += 1
OUT['qui_V_follower_top'] = qvx.most_common(15)
print('followers of «qui [V]»:', qvx.most_common(12))

# ---- F. -este family verbs in diplomatic era ----
este = {x: wu[x] for x in
        ['conteste', 'contestent', 'd\u00e9teste', 'manifeste',
         'manifestent', 'proteste', 'protestent', 'reste', 'restent',
         'atteste', 'attestent'] if x in wu}
OUT['este_verbs'] = este
print('-este verbs:', este)

# ---- E. «que [N] en [V]» frames: count «que X en Y» with Y a verb ----
qnen = collections.Counter()
for a, b, c, d_ in zip(w, w[1:], w[2:], w[3:]):
    if a == 'que' and c == 'en' and (d_ in verbs or d_ in conj3sg):
        qnen[b] += 1
OUT['que_X_en_V'] = {'n': sum(qnen.values()), 'topX': qnen.most_common(12)}
print('«que X en [V]»: n=%d topX=%s' % (sum(qnen.values()), qnen.most_common(10)))

# ---- 86 L2: P(qu|pour) already; also «pour qu X» successors ----
pqx = collections.Counter()
for a, b, c in zip(w, w[1:], w[2:]):
    if a == 'pour' and b == 'qu':
        pqx[c] += 1
OUT['pour_qu_suc'] = pqx.most_common(15)
print('«pour qu X» successors:', pqx.most_common(12))

json.dump(OUT, open(os.path.join(os.path.dirname(__file__), 'era9_results.json'), 'w'),
          indent=1)
print('wrote era9_results.json')
