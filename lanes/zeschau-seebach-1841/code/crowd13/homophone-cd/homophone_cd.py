#!/usr/bin/env python3
"""Round 13 WO2 — homophone-set frame batteries for {52,59} and {76,78}.

Pre-registered: code/crowd13/homophone-cd/PREREG.md.
All counts from the repaired 1,847-pair stream; era rates on the
clean-diplo pool (lane tokenizer verbatim); v8 VOID for phrases.
"""
import json, math, re, unicodedata, sys
from collections import Counter
from pathlib import Path

LANE = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(LANE / 'code' / 'crowd6' / 'redteam'))
from verify_baseline import load_stream  # noqa: E402

s = load_stream()
assert len(s) == 1847

GLOSS = {11: 'la', 70: 'pre', 82: 'm', 34: 'i', 29: 'er', 40: 'e', 46: 'que',
         87: 'ce?', 64: 'qui?', 96: 'par?', 59: 'est/-este?', 77: 'le?',
         94: 'ne?', 52: 'pas~', 6: 'Vstem?', 62: 'on?', 78: 'ver/er?',
         84: 'en/stem?', 0: 'pour/le?', 24: '?', 48: '?', 33: 'inf?',
         47: 'ce~', 76: '?', 35: '?', 36: '?', 37: '?', 43: '?', 45: '?',
         42: '?', 44: '?', 67: 'et/veut?', 61: '?', 86: 'Vstem2?', 15: '?',
         17: 'fois~', 83: '?', 93: '?', 79: '?', 91: '?', 27: '?', 28: '?',
         30: '?', 31: '?', 32: '?', 38: '?', 39: '?', 53: '?', 58: '?',
         66: '?', 68: '?', 74: '?', 89: '?', 90: '?', 16: '?', 18: '?',
         19: '?', 26: '?', 41: '?', 49: '?', 50: '?', 56: '?', 57: '?',
         63: '?', 65: '?', 69: '?', 71: '?', 72: '?', 73: '?', 75: '?',
         80: '?', 81: '?', 85: '?', 88: '?', 92: '?', 95: '?'}

def g(i):
    v = s[i]
    return '%d%s' % (v, '=%s' % GLOSS.get(v, '?') if v in GLOSS else '?')

def win(i, r=3):
    return ' '.join(g(j) for j in range(max(0, i - r), min(len(s), i + r + 1)))

OUT = {}

# ---------------- era corpus (clean-diplo, lane tokenizer verbatim) ----------------
CORP = LANE / 'code' / 'side-period' / 'corpus'
FRENCH_CLEAN = ['guizot-memoires-t1-gutenberg.txt', 'guizot-memoires-t2-gutenberg.txt',
                'guizot-memoires-t3-gutenberg.txt', 'guizot-memoires-t5-t6.txt',
                'metternich-papiere-v4.txt', 'metternich-papiere-v6.txt',
                'pozzo-di-borgo-correspondance-v1.txt',
                'levant-correspondence-1841-p3.txt', 'talleyrand-memoires-v1.txt',
                'revue-deux-mondes-1841-q1.txt', 'revue-deux-mondes-1841-q2.txt',
                'revue-deux-mondes-1841-q3.txt', 'revue-deux-mondes-1841-q4.txt']
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

ctoks = []
for f in FRENCH_CLEAN:
    ctoks += tokenize((CORP / f).read_text(encoding='utf-8', errors='replace'))
N_ERA = len(ctoks)
cbi = Counter(zip(ctoks[:-1], ctoks[1:]))
ctri = Counter(zip(ctoks[:-1], ctoks[1:], ctoks[2:]))
OUT['era'] = {'pool': 'clean-diplo (v8 VOID for phrases)', 'N': N_ERA}

def era2(a, b):
    return cbi.get((a, b), 0)

def era3(a, b, c):
    return ctri.get((a, b, c), 0)

# ---------------- cipher-side helpers ----------------
def positions(gr):
    return [i for i, v in enumerate(s) if v == gr]

def pre(i):
    return s[i - 1] if i > 0 else None

def suc(i):
    return s[i + 1] if i + 1 < len(s) else None

def chi2_uniform(counts):
    n = sum(counts)
    k = len(counts)
    e = n / k
    chi2 = sum((c - e) ** 2 / e for c in counts)
    return chi2, chi2_p(chi2, k - 1)

def chi2_p(x, df):
    # upper-tail via incomplete gamma (df small, x moderate)
    if df == 1:
        return math.erfc(math.sqrt(x / 2))
    # generic: use series for lower incomplete gamma
    a = df / 2
    xx = x / 2
    if xx < a + 1:
        # series
        ap = a; total = 1.0 / a; term = 1.0 / a
        for _ in range(200):
            ap += 1; term *= xx / ap; total += term
            if abs(term) < abs(total) * 1e-12:
                break
        lower = total * math.exp(-xx + a * math.log(xx))
        return 1 - lower / math.gamma(a)
    else:
        # continued fraction for upper
        b = xx + 1 - a; c = 1e300; d = 1.0 / b; h = d
        for i in range(1, 200):
            an = -i * (i - a); b += 2
            d = an * d + b
            if abs(d) < 1e-300: d = 1e-300
            c = b + an / c
            if abs(c) < 1e-300: c = 1e-300
            d = 1.0 / d; delta = d * c; h *= delta
            if abs(delta - 1.0) < 1e-12: break
        return h * math.exp(-xx + a * math.log(xx)) / math.gamma(a)

def runs_test(seq):
    # Wald-Wolfowitz on a binary list of 0/1 in stream order
    n1 = sum(1 for x in seq if x == 0)
    n2 = sum(1 for x in seq if x == 1)
    runs = 1
    for a, b in zip(seq, seq[1:]):
        if a != b:
            runs += 1
    mu = 2 * n1 * n2 / (n1 + n2) + 1
    var = (2 * n1 * n2 * (2 * n1 * n2 - n1 - n2)) / ((n1 + n2) ** 2 * (n1 + n2 - 1))
    z = (runs - mu) / math.sqrt(var)
    return {'n1': n1, 'n2': n2, 'runs': runs, 'mu': round(mu, 2),
            'z': round(z, 3), 'p_two_sided': round(chi2_p(z * z, 1), 4)}

def pre_homogeneity(pos_a, pos_b, topk=6):
    # chi2 test of homogeneity of predecessor distributions; lump tail
    ca, cb = Counter(pre(i) for i in pos_a), Counter(pre(i) for i in pos_b)
    allp = Counter()
    for p in set(ca) | set(cb):
        allp[p] = ca.get(p, 0) + cb.get(p, 0)
    top = [p for p, _ in allp.most_common(topk)]
    ta = [ca.get(p, 0) for p in top] + [sum(v for p, v in ca.items() if p not in top)]
    tb = [cb.get(p, 0) for p in top] + [sum(v for p, v in cb.items() if p not in top)]
    na, nb = sum(ta), sum(tb)
    chi2 = 0.0
    for ra, rb in zip(ta, tb):
        ea = na * (ra + rb) / (na + nb)
        eb = nb * (ra + rb) / (na + nb)
        if ea > 0: chi2 += (ra - ea) ** 2 / ea
        if eb > 0: chi2 += (rb - eb) ** 2 / eb
    df = len(ta) - 1
    return {'cats': top + ['OTHER'], 'a': ta, 'b': tb, 'chi2': round(chi2, 3),
            'df': df, 'p': round(chi2_p(chi2, df), 4)}

# ================= SET {52,59} =================
p52, p59 = positions(52), positions(59)
assert len(p52) == 27 and len(p59) == 27

est_pre = {64, 94, 93}
win52 = []
for i in p52:
    p, q = pre(i), suc(i)
    arm = 'EST-LICENSED' if p in est_pre else ('ESTE-ARM?' if p == 84 else 'OTHER')
    win52.append({'pos': i, 'pre': p, 'suc': q, 'arm': arm, 'window': win(i)})

# era frame rates for the three licensed frames (banked-clean, re-stated on same pool)
era_frames = {
    'qui_est': era2('qui', 'est'),
    'n_est': era2("n'", 'est'),
    'ne_l_est': era3('ne', "l'", 'est'),
    'qui_le_est': era3('qui', 'le', 'est'),
    'ce_qui_le_est': 0,  # placeholder; computed below as 4-gram-ish
}
# «ce qui est» frame rate for 1777-type window
ce_qui_est = sum(1 for a, b, c in zip(ctoks[:-2], ctoks[1:-1], ctoks[2:])
                 if (a, b, c) == ('ce', 'qui', 'est'))

# successor diagnostics for word-est: what follows 59 in est-arm vs 52
suc59_est = Counter(suc(i) for i in p59 if pre(i) in est_pre)
suc52_lic = Counter(suc(i) for i in p52 if pre(i) in est_pre)

set52 = {}
set52['n52'] = len(p52); set52['n59'] = len(p59)
chi2u, pu = chi2_uniform([len(p52), len(p59)])
set52['uniformity'] = {'counts': [len(p52), len(p59)], 'chi2': round(chi2u, 3),
                       'p': round(pu, 4), 'ratio': 1.0}
seq = [0 if s[i] == 52 else 1 for i in sorted(p52 + p59)]
set52['runs'] = runs_test(seq)
set52['pre_homogeneity'] = pre_homogeneity(p52, p59)
set52['windows52'] = win52
set52['era_frames'] = {k: v for k, v in era_frames.items()}
set52['ce_qui_est'] = ce_qui_est
set52['suc59_estarm'] = dict(suc59_est)
set52['suc52_licensed'] = dict(suc52_lic)
set52['pre52_dist'] = dict(Counter(pre(i) for i in p52))
set52['pre59_dist'] = dict(Counter(pre(i) for i in p59))
# negative control: 59 windows whose pre is outside est-arms, for comparison
set52['windows59_other'] = [{'pos': i, 'pre': pre(i), 'suc': suc(i), 'window': win(i)}
                            for i in p59 if pre(i) not in est_pre and pre(i) != 84]
set52['n59_pre84'] = sum(1 for i in p59 if pre(i) == 84)
set52['n52_pre84'] = sum(1 for i in p52 if pre(i) == 84)
OUT['set_52_59'] = set52

# ================= SET {76,78} =================
p76, p78 = positions(76), positions(78)
assert len(p76) == 21 and len(p78) == 31

win76 = [{'pos': i, 'pre': pre(i), 'suc': suc(i), 'window': win(i)} for i in p76]
win78 = [{'pos': i, 'pre': pre(i), 'suc': suc(i), 'window': win(i)} for i in p78]

# frenchman-style er|ne diagnostic on the CIPHER side:
# 78->94 and 76->94 bigrams; era: count word-types where 'Xer ne' boundary occurs
# era: for tokens ending in 'er' followed by 'ne'
er_ne_types = set()
er_ne_toks = 0
for a, b in zip(ctoks[:-1], ctoks[1:]):
    if a.endswith('er') and len(a) > 2 and b == 'ne':
        er_ne_toks += 1; er_ne_types.add(a)
# 'ver'+'ne' impossible at word level by construction; do verX-ne at word level:
# words ending in 'ver' followed by 'ne'
ver_ne = [(a, b) for a, b in zip(ctoks[:-1], ctoks[1:]) if a.endswith('ver') and b == 'ne']

big76_94 = sum(1 for i in p76 if suc(i) == 94)
big78_94 = sum(1 for i in p78 if suc(i) == 94)
# pre=94 (ne) windows for both: «ne [76/78]» 
pre94_76 = [i for i in p76 if pre(i) == 94]
pre94_78 = [i for i in p78 if pre(i) == 94]

# 77-adjacency (the «le [78]» frame family)
pre77_76 = [i for i in p76 if pre(i) == 77]
pre77_78 = [i for i in p78 if pre(i) == 77]

set76 = {}
set76['n76'] = len(p76); set76['n78'] = len(p78)
chi2u, pu = chi2_uniform([len(p76), len(p78)])
set76['uniformity'] = {'counts': [len(p76), len(p78)], 'chi2': round(chi2u, 3),
                       'p': round(pu, 4), 'ratio': round(31 / 21, 3)}
seq = [0 if s[i] == 76 else 1 for i in sorted(p76 + p78)]
set76['runs'] = runs_test(seq)
set76['pre_homogeneity'] = pre_homogeneity(p76, p78)
set76['windows76'] = win76
set76['windows78'] = win78
set76['cipher_76_94'] = big76_94
set76['cipher_78_94'] = big78_94
set76['pre94_76'] = pre94_76
set76['pre94_78'] = pre94_78
set76['pre77_76'] = pre77_76
set76['pre77_78'] = pre77_78
set76['pre76_dist'] = dict(Counter(pre(i) for i in p76))
set76['pre78_dist'] = dict(Counter(pre(i) for i in p78))
set76['era_er_ne'] = {'tokens': er_ne_toks, 'types': len(er_ne_types)}
set76['era_ver_ne_words'] = ver_ne[:10]
set76['era_ver_ne_n'] = len(ver_ne)
# era «le VER/er» sanity: count 'le' + word ending in er / ver
le_er = sum(1 for a, b in zip(ctoks[:-1], ctoks[1:])
            if a == 'le' and b.endswith('er') and len(b) > 2)
set76['era_le_Xer'] = le_er
OUT['set_76_78'] = set76

outp = LANE / 'code' / 'crowd13' / 'homophone-cd' / 'homophone_cd_results.json'
outp.write_text(json.dumps(OUT, indent=1, ensure_ascii=False))
print('wrote', outp)
print('52/59 uniformity chi2=%.3f p=%.4f' % (chi2u, pu) if False else '')
print('n52=%d n59=%d n76=%d n78=%d' % (len(p52), len(p59), len(p76), len(p78)))
print('52 pre-dist:', dict(Counter(pre(i) for i in p52)))
print('59 pre-dist:', dict(Counter(pre(i) for i in p59)))
print('76 pre-dist:', dict(Counter(pre(i) for i in p76)))
print('78 pre-dist:', dict(Counter(pre(i) for i in p78)))
