#!/usr/bin/env python3
"""Round-8 59-consolidation battery (pre-registered in PRE-REGISTER.md).

G1: S5 dependency (59->37 x6 fenced on 37="le" MEDIUM) — A1..A4.
G2: S4 frame-level test (06-59-46-29 @216; 84-59-46-07 @1190) — L0, B1..B4.
"""
import json, re, unicodedata
from pathlib import Path
from collections import Counter

LANE = Path(__file__).resolve().parents[3]
import sys
sys.path.insert(0, str(LANE / 'code' / 'side-keyhunt'))
sys.path.insert(0, str(LANE / 'code' / 'crowd5' / 'redteam'))
from repair_parse import load_rows, parse  # noqa: E402

CORP = LANE / 'code' / 'side-period' / 'corpus'
OUT = Path(__file__).parent
res = {}

# ---------- cipher stream ----------
rows = load_rows()
off = json.loads((LANE / 'code/side-keyhunt/repaired_offsets.json').read_text())
pairs = [int(g) for g, _ in parse(rows, off)]
assert len(pairs) == 1847
big = Counter(zip(pairs[:-1], pairs[1:]))
n59, n37, n46 = pairs.count(59), pairs.count(37), pairs.count(46)

# ---------- A1: S5 census ----------
p5937 = [i for i in range(len(pairs) - 1) if (pairs[i], pairs[i+1]) == (59, 37)]
a1 = []
for i in p5937:
    a1.append({'at': i, 'ctx': pairs[max(0,i-2):i+4], 'pre59': pairs[i-1] if i > 0 else None})
res['A1_S5_windows'] = a1
res['A1_n'] = len(p5937)
res['A1_any_pre87'] = any(w['pre59'] == 87 for w in a1)
res['P37_given_59'] = round(big[(59,37)]/n59, 4)

# 46 successor profile (B3 support + general)
suc46 = sorted([(b, big[(46,b)]) for b in set(pairs) if big[(46,b)]], key=lambda x: -x[1])
res['succ_46'] = suc46[:15]
res['B3_46_to_vowel'] = {str(k): big[(46,k)] for k in (29,34,40)}  # er/i/e known vowel-initial

# 37 profile (A3)
pre37 = sorted([(a, big[(a,37)]) for a in set(pairs) if big[(a,37)]], key=lambda x: -x[1])
suc37 = sorted([(b, big[(37,b)]) for b in set(pairs) if big[(37,b)]], key=lambda x: -x[1])
res['A3_n37'] = n37
res['A3_pre37'] = pre37[:12]
res['A3_suc37'] = suc37[:12]

# 59->46 positions (S4) + windows
p5946 = [i for i in range(len(pairs)-1) if (pairs[i],pairs[i+1])==(59,46)]
res['S4_positions'] = p5946
res['S4_w1_ctx'] = pairs[210:224]   # @216 window + margin
res['S4_w2_ctx'] = pairs[1184:1200] # @1190 window + margin
w1 = p5946[0]; w2 = p5946[1]
res['S4_w1_4win'] = pairs[w1-1:w1+3]  # 06-59-46-29
res['S4_w2_4win'] = pairs[w2-1:w2+3]  # 84-59-46-07
res['B4_pre84_w2'] = pairs[w2-2]      # predecessor of 84

# ---------- corpus ----------
WORD = re.compile(r"[a-zàâäéèêëîïôöùûüÿçœæ]+(?:'[a-zàâäéèêëîïôöùûüÿçœæ]+)*")
def tokenize(text):
    text = unicodedata.normalize('NFC', text.lower().replace('’', "'").replace('‘', "'"))
    toks = []
    for m in WORD.finditer(text):
        w = m.group(0)
        parts = w.split("'")
        for i, p in enumerate(parts):
            if not p:
                continue
            toks.append(p + "'" if i < len(parts) - 1 else p)
    return toks

def load_corpus(fn):
    return tokenize((CORP/fn).read_text(encoding='utf-8', errors='replace'))

ness8 = load_corpus('nesselrode-v8.txt')
guiz = load_corpus('guizot-memoires-t5-t6.txt')
raw8 = (CORP/'nesselrode-v8.txt').read_text(encoding='utf-8', errors='replace').lower()

def cond_rate(toks, num, den, den_pre_excl=None):
    """P(num|den); optionally restrict den to tokens whose predecessor not in excl set."""
    n_den = 0; n_num = 0
    for i in range(len(toks)-1):
        if toks[i] == den:
            if den_pre_excl is not None:
                pre = toks[i-1] if i > 0 else None
                if pre in den_pre_excl:
                    continue
            n_den += 1
            if toks[i+1] == num:
                n_num += 1
    return (n_num/n_den if n_den else None), n_num, n_den

# A2: P(le|est) and bare-est version
for name, toks in [('nesselrode_v8', ness8), ('guizot_t5t6', guiz)]:
    p_all, k, n = cond_rate(toks, 'le', 'est')
    p_bare, kb, nb = cond_rate(toks, 'le', 'est', den_pre_excl={"c'", 'ce'})
    res[f'A2_{name}'] = {
        'P_le_given_est': round(p_all,5) if p_all else None, 'k': k, 'n': n,
        'P_le_given_bare_est': round(p_bare,5) if p_bare else None, 'kb': kb, 'nb': nb,
        'cipher_P37_given_59': round(big[(59,37)]/n59,4),
        'ratio_all': round((big[(59,37)]/n59)/p_all,2) if p_all else None,
        'ratio_bare': round((big[(59,37)]/n59)/p_bare,2) if p_bare else None,
    }
    # "n'est le" trigram (for @1796 94-59-37 under 94=ne, 37=le)
    tri = sum(1 for i in range(len(toks)-2)
              if toks[i] in ("n'", 'ne') and toks[i+1]=='est' and toks[i+2]=='le')
    res[f'A2_{name}_nest_le_trigram'] = tri

# L0: letter-level "estqu" check (no single-word "est"+"que" parse)
estqu = re.findall(r'estqu\w*', raw8)
res['L0_estqu_hits'] = len(estqu)
res['L0_estqu_examples'] = sorted(set(estqu))[:10]

# B1: "est que" frame inventory (Nesselrode v8)
CLOSED_PRE = {"c'", 'ce', "n'", 'ne', 'se', 'il', 'elle', 'ils', 'elles', 'on',
              'nous', 'vous', 'je', 'tu', 'qui', 'que', "s'", "d'", "l'", "qu'",
              'le', 'la', 'les', 'un', 'une', 'des', 'du', 'de', 'ceci', 'cela', 'ça'}
frames = []  # (pre, suc)
frames_elided = []  # "est qu'" + vowel-initial
for i in range(len(ness8)-1):
    if ness8[i] == 'est' and ness8[i+1] == 'que':
        pre = ness8[i-1] if i > 0 else None
        suc = ness8[i+2] if i+2 < len(ness8) else None
        frames.append((pre, suc))
    if ness8[i] == 'est' and ness8[i+1] == "qu'":
        pre = ness8[i-1] if i > 0 else None
        suc = ness8[i+2] if i+2 < len(ness8) else None
        frames_elided.append((pre, suc))
res['B1_n_est_que'] = len(frames)
res['B1_n_est_qu_elided'] = len(frames_elided)
pre_counter = Counter(p for p, s in frames)
res['B1_pre_counter'] = pre_counter.most_common(25)
res['B1_open_pre'] = sorted([(p, c) for p, c in pre_counter.items() if p not in CLOSED_PRE],
                            key=lambda x: -x[1])[:20]

def er_initial(w):
    return bool(w) and (w.startswith('er') or w.startswith('err'))

def an_final(w):
    return bool(w) and re.search(r'(ent|ant|an|en|em|am)$', w) is not None

# B2: compatibility counts
compat_strict = [(p,s) for p,s in frames if p not in {"c'",'ce',"n'",'ne'} and an_final(p) and er_initial(s)]
compat_loose  = [(p,s) for p,s in frames if p not in {"c'",'ce',"n'",'ne'} and er_initial(s)]
compat_elided = [(p,s) for p,s in frames_elided if p not in {"c'",'ce',"n'",'ne'} and er_initial(s)]
res['B2_compat_strict_anfinal_and_erinital'] = compat_strict
res['B2_compat_loose_notcene_and_erinitial'] = compat_loose
res['B2_compat_elided'] = compat_elided
res['B2_N'] = len(frames)
# closest misses: er-initial suc regardless of pre
res['B2_er_suc_any_pre'] = [(p,s) for p,s in frames if er_initial(s)][:15]
res['B2_er_suc_elided_any_pre'] = [(p,s) for p,s in frames_elided if er_initial(s)][:15]

# Guizot check for B2
frames_g = []
for i in range(len(guiz)-1):
    if guiz[i]=='est' and guiz[i+1]=='que':
        frames_g.append((guiz[i-1] if i>0 else None, guiz[i+2] if i+2<len(guiz) else None))
res['B2_guiz_N'] = len(frames_g)
res['B2_guiz_compat_loose'] = [(p,s) for p,s in frames_g
                               if p not in {"c'",'ce',"n'",'ne'} and er_initial(s)][:15]

json.dump(res, open(OUT/'battery_results.json','w'), indent=1,
          default=str, ensure_ascii=False)
print(json.dumps({k: v for k, v in res.items()
                  if not k.startswith(('A1_S5','B1_pre','B1_open'))}, indent=1, ensure_ascii=False)[:4000])
print('...')
print('A1 windows:', json.dumps(res['A1_S5_windows'], ensure_ascii=False))
print('B1 top pre:', res['B1_pre_counter'][:12])
print('B1 open pre:', res['B1_open_pre'][:12])
