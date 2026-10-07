#!/usr/bin/env python3
"""ROUND-10 FRENCHMAN — era/register gates for the round-10 live questions.

Era standard: Nesselrode v8 strict (nesselrode-v8.txt), elision-split
tokenizer per F53 (shared corpus9 loader from round 9). Dispersion:
primary (v8 + levant-correspondence-1841-p3), diplomatic set
(ness8 + guizot-memoires-t5-t6), diplomatic_all (whole corpus dir, 4.2M).

Questions:
 Q1 @1351 triple collision: 06-islet "ne ment pas" vs gouv "gouvernement pas"
    vs 77="le" — confirm/revise era grades with corpus counts (+ H1c/H1d).
 Q2 59 conditioned frames: era-grade each licensed frame.
 Q3 48 syllable candidates: era frame battery (V1 missing-ne, V2 clitic order,
    H1e L1-collocate) + German-thought by-ear licensing rule (F68).
 Q4 @1248 arms: Gate 4 compliance — "pour X que" inventory, non-finite only.
 Q5 standing vetoes; no new executor proposals landed as of this writing.
"""
import json, sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)).replace('crowd10', 'crowd9'))
import corpus9
sys.path.insert(0, str(corpus9.LANE / 'code/crowd8/frenchman'))
from util import PAIRS, N, positions, window

OUT = {}
v8t = corpus9.tokenize_elision(open(corpus9.CORP / 'nesselrode-v8.txt', encoding='utf-8', errors='replace').read())
V8N = len(v8t)
prim = corpus9.load('primary')
allt = corpus9.load('all')
ALLN = len(allt)
guiz = corpus9.tokenize_elision(open(corpus9.CORP / 'guizot-memoires-t5-t6.txt', encoding='utf-8', errors='replace').read())
diplo = v8t + guiz
DIPN = len(diplo)
OUT['corpus_sizes'] = {'v8': V8N, 'primary': len(prim), 'diplo_ness8_guizot': DIPN, 'all': ALLN}

def ngram(t, *w):
    n = len(w)
    return sum(1 for i in range(len(t) - n + 1) if tuple(t[i:i+n]) == tuple(w))

def frames(t, mid, left=None, right=None):
    """count frames left+mid+right with optional wildcards"""
    n = 3 if right else (2 if left else 1)
    c = 0
    for i in range(len(t) - n + 1):
        ok = True
        if left is not None and t[i] != left: ok = False
        if t[i + (1 if left else 0)] != mid: ok = False
        if right is not None and t[i + (2 if left else 1)] != right: ok = False
        if ok: c += 1
    return c

# ================= Q1: @1351 triple collision =================
q1 = {}
# window anchor (repaired parse)
q1['window_1348_1359'] = {'groups': PAIRS[1348:1360], 'labels': window(1353, 6)}
# "ne ment pas" exact + variants
for corpus_name, t in [('v8', v8t), ('primary', prim), ('all', allt)]:
    q1[f'ne_ment_pas_{corpus_name}'] = ngram(t, 'ne', 'ment', 'pas')
    q1[f'ne_mentent_pas_{corpus_name}'] = ngram(t, 'ne', 'mentent', 'pas')
    q1[f'ne_ment_{corpus_name}'] = ngram(t, 'ne', 'ment')
    q1[f'ment_pas_bare_{corpus_name}'] = sum(
        1 for i in range(1, len(t)) if t[i-1] == 'ment' and t[i] == 'pas'
        and not any(t[j] in ('ne', "n'") for j in range(max(0, i-4), i)))
# frame productivity: "ne <V> pas" trigrams in v8
q1['ne_V_pas_trigrams_v8'] = sum(1 for i in range(V8N - 2) if v8t[i] == 'ne' and v8t[i+2] == 'pas')
# "gouvernement" + "pas"
gouv_idx = [i for i, w in enumerate(diplo) if w == 'gouvernement']
q1['n_gouvernement_diplo'] = len(gouv_idx)
q1['gouvernement_pas_adjacent_diplo'] = sum(1 for i in gouv_idx if i + 1 < DIPN and diplo[i+1] == 'pas')
q1['gouvernement_pas_within3_diplo'] = sum(1 for i in gouv_idx if any(diplo[j] == 'pas' for j in range(i+1, min(i+4, DIPN))))
# H1c: "on" in L1..L2 of "gouvernement"
q1['on_L1L2_gouvernement_diplo'] = sum(
    1 for i in gouv_idx if (i > 0 and diplo[i-1] == 'on') or (i > 1 and diplo[i-2] == 'on'))
q1['on_L1L2_gouvernement_v8'] = sum(
    1 for i, w in enumerate(v8t) if w == 'gouvernement' and
    ((i > 0 and v8t[i-1] == 'on') or (i > 1 and v8t[i-2] == 'on')))
# H1d: "le qui"
q1['le_qui_diplo'] = ngram(diplo, 'le', 'qui')
q1['le_qui_v8'] = ngram(v8t, 'le', 'qui')
q1['pas_le_qui_diplo'] = ngram(diplo, 'pas', 'le', 'qui')
# 77="le" + 78: "le ver*" (noun) for the (a2) fork; "le"+"er" structural zero
q1['le_ver_v8'] = ngram(v8t, 'le', 'ver')
q1['le_ver_diplo'] = ngram(diplo, 'le', 'ver')
q1['le_ver_all'] = ngram(allt, 'le', 'ver')
# "le" + ver-initial words in v8 (what could 78="ver" start?)
ver_words = collections.Counter(w for w in v8t if w.startswith('ver') and len(w) > 3)
q1['ver_initial_words_v8_top'] = ver_words.most_common(12)
OUT['Q1_1351'] = q1

# ================= Q2: 59 conditioned frames =================
q2 = {}
q2['n59'] = len(positions(59))
q2['windows_59'] = {p: {'pre': PAIRS[p-1], 'suc': PAIRS[p+1]} for p in positions(59)}
# F-A: 59="est"-as-word after 84 in «qui le 84 59»: «qui le [V] est» for ALL verbs, all-corpus
q2['qui_le_V_est_all'] = sum(1 for i in range(ALLN - 3)
                             if allt[i] == 'qui' and allt[i+1] == 'le' and allt[i+3] == 'est')
q2['qui_le_V_est_diplo'] = sum(1 for i in range(DIPN - 3)
                               if diplo[i] == 'qui' and diplo[i+1] == 'le' and diplo[i+3] == 'est')
q2['qui_le_X_est_v8'] = sum(1 for i in range(V8N - 3)
                            if v8t[i] == 'qui' and v8t[i+1] == 'le' and v8t[i+3] == 'est')
# F-B: -este verbs (conditioner list, re-verify on v8)
este_verbs = ['déteste', 'conteste', 'atteste', 'proteste', 'manifeste', 'reste',
              'teste', 'déneste', 'infeste', 'peste']
ev = {}
for vb in este_verbs:
    ev[vb] = {'v8': v8t.count(vb),
              'qui_le_vb_v8': ngram(v8t, 'qui', 'le', vb),
              'qui_le_vb_diplo': ngram(diplo, 'qui', 'le', vb),
              'qui_le_vb_all': ngram(allt, 'qui', 'le', vb)}
q2['este_verbs'] = ev
# F-C: 59="est"-word banked contexts by predecessor class
# 94="ne"prov -> "n'est" (elision-split: "n'" "est"); 64="qui"prov -> "qui est";
# 87="ce"prov -> "c'est"; {93,8}="l'"lead -> "l'est"; 11="la"GT -> "la est"/"l'est"
q2['n_prime_est_v8'] = ngram(v8t, "n'", 'est')
q2['qui_est_v8'] = ngram(v8t, 'qui', 'est')
q2['c_prime_est_v8'] = ngram(v8t, "c'", 'est')
q2['l_prime_est_v8'] = ngram(v8t, "l'", 'est')
q2['la_est_bare_v8'] = ngram(v8t, 'la', 'est')   # unelided (by-ear "la"+"est")
q2['ne_est_bare_v8'] = ngram(v8t, 'ne', 'est')   # unelided "ne est"
# 59="est"-word at @1190/@1291 (pre=84): frame «84-59-46/35» — era «[V] est que»?
q2['est_que_v8'] = ngram(v8t, 'est', 'que')
OUT['Q2_59frames'] = q2

# ================= Q3: 48 syllable battery =================
q3 = {}
q3['n48'] = len(positions(48))
w48 = {p: {'pre': PAIRS[p-1], 'suc': PAIRS[p+1]} for p in positions(48)}
q3['windows_48'] = w48
q3['pos_48_pas'] = [p for p in positions(48) if PAIRS[p+1] == 52]   # V1 windows
q3['pos_62_48'] = [p for p in positions(48) if PAIRS[p-1] == 62]   # "on 48"
q3['pos_48_le'] = [p for p in positions(48) if PAIRS[p+1] == 77]   # V2 windows (@1350 etc.)
# V1: era "X pas" with no ne/n' in 6-back — generalized over candidate X
def bare_X_pas(t, x):
    c = 0
    for i in range(1, len(t)):
        if t[i-1] == x and t[i] == 'pas':
            if not any(t[j] in ('ne', "n'") for j in range(max(0, i-7), i-1)):
                c += 1
    return c
candidates = ['en', 'de', 'le', 'les', 'dans', 'son', 'sur', 'tout', 'bien', 'fort',
              'grand', 'con', 'com', 'ter', 'ser', 'ver', 'des', 're', 'te', 'se',
              'dont', 'sans', 'nous', 'vous', 'ment', 'plus', 'tant', 'point']
batt = {}
for x in candidates:
    batt[x] = {
        'on_X_v8': ngram(v8t, 'on', x),
        'X_pas_bare_v8': bare_X_pas(v8t, x),
        'X_pas_bare_diplo': bare_X_pas(diplo, x),
        'X_le_v8': ngram(v8t, x, 'le'),
        'n_v8': v8t.count(x),
    }
q3['battery'] = batt
# H1e: top-L1 collocates of "gouvernement" in diplo (for successor48 IF gouv@1351 stands)
l1 = collections.Counter(diplo[i-1] for i in gouv_idx if i > 0)
q3['gouvernement_L1_top_diplo'] = l1.most_common(15)
OUT['Q3_48'] = q3

# ================= Q4: @1248 Gate 4 =================
q4 = {}
q4['window_1248'] = {'groups': PAIRS[1242:1255]}
def pour_X_que(t):
    c = collections.Counter()
    for i in range(len(t) - 2):
        if t[i] == 'pour' and t[i+2] == 'que':
            c[t[i+1]] += 1
    return c
for nm, t in [('v8', v8t), ('primary', prim), ('diplo', diplo), ('all', allt)]:
    pxq = pour_X_que(t)
    q4[f'pour_X_que_{nm}'] = pxq.most_common(25)
    q4[f'pour_X_que_total_{nm}'] = sum(pxq.values())
# non-finite inventory on all-corpus
pxq_all = pour_X_que(allt)
nonfinite = {x: n for x, n in pxq_all.items()}
q4['pour_X_que_all_full'] = sorted(nonfinite.items(), key=lambda kv: -kv[1])
# cela / peu word lengths (R1 cell = 1-4 letters)
q4['cela_letters'] = len('cela')
q4['peu_letters'] = len('peu')
OUT['Q4_1248'] = q4

json.dump(OUT, open('era_gates10_out.json', 'w'), ensure_ascii=False, indent=1)
print(json.dumps({k: v for k, v in OUT.items() if k != 'Q2_59frames' and k != 'Q3_48'}, ensure_ascii=False, indent=1)[:4000])
