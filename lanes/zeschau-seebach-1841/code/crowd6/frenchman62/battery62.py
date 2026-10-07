#!/usr/bin/env python3
"""Round 6 frenchman: non-ear on-vs-il discrimination battery for 62.

Three legs, disjoint data, ZERO ear content, all era legs in word space (F30):
  Leg 1: 46->62 elision-habit calibration (cipher-internal, GT-anchored) ->
         adjudicates N35's "il"-differential AND N28's merger corroboration.
  Leg 2: three-way (on/il/qui) likelihood on disjoint clean pieces:
         (a) 62->94 ne-rate [cond. 94="ne" prov-strong],
         (b) 62->46 que-follower [GT 46],
         (d) 96->62 par-frame [prov 96].  (46->62 EXCLUDED: recycled in N35.)
  Leg 3: the 59 follow (F42 order): 59's structural profile; on/il discrimination?
Unbridgeability proof: tabulate mappable vs discriminative cells for profiles.
"""
import json, re, math, collections
from pathlib import Path
LANE = Path.home() / 'workspace/cipher-hunt/lanes/zeschau-seebach-1841'
DATA = LANE / 'data'
OUT = Path(__file__).parent

def load_repaired():
    rows = []
    for line in open(DATA / 'upstream-ct_R5005.txt'):
        line = line.strip()
        if not line: continue
        lid, digits = line.split()
        rows.append((lid, re.sub(r'\D', '', digits)))
    off = json.loads((LANE / 'code/side-keyhunt/repaired_offsets.json').read_text())
    pairs = []
    for lid, digits in rows:
        o = off[lid]
        pairs += [digits[i:i+2] for i in range(o, len(digits)-1, 2)]
    return [int(g) for g in pairs]

pairs = load_repaired(); n = len(pairs); assert n == 1847
big = collections.Counter(zip(pairs[:-1], pairs[1:]))
uni = collections.Counter(pairs)
res = {'n_pairs': n}

# ---------- re-derived baselines ----------
n62 = uni[62]; n46 = uni[46]
n46nf = sum(1 for i in range(n-1) if pairs[i] == 46)
res['baselines'] = {
    'n62': n62, 'rank62': sorted(uni.values(), reverse=True).index(n62)+1,
    'f62_94': [big[(62,94)], n62], 'f46_62': [big[(46,62)], n46nf],
    'n24': uni[24], 'n52': uni[52], 'n59': uni[59], 'n64': uni[64],
    'n87': uni[87], 'n96': uni[96], 'n94': uni[94],
}
fol62 = collections.Counter(pairs[i+1] for i in range(n-1) if pairs[i] == 62)
pre62 = collections.Counter(pairs[i-1] for i in range(1, n) if pairs[i] == 62)
res['fol62'] = dict(sorted(fol62.items())); res['pre62'] = dict(sorted(pre62.items()))

# ---------- era word-space (audit tokenizer) ----------
def words(path):
    t = open(path, encoding='utf-8', errors='replace').read().lower()
    t = re.sub(r"[']", "'", t)
    t = re.sub(r"\b([a-zàâäéèêëîïôöùûüç]+)'([a-zàâäéèêëîïôöùûüç]+)", r"\1' \2", t)
    return re.findall(r"[a-zàâäéèêëîïôöùûüç]+(?:'[a-zàâäéèêëîïôöùûüç]+)?", t)
toks = words(DATA/'gutenberg-30513-tocqueville-t1.txt') + words(DATA/'gutenberg-30514-tocqueville-t2.txt')
N = len(toks); eu = collections.Counter(toks); eb = collections.Counter(zip(toks, toks[1:]))
def Pfol(fset, w):
    nw = eu[w]; c = sum(eb[(w,f)] for f in fset); return c/nw
def Ppreis(pset, w):
    nw = eu[w]; c = sum(eb[(p,w)] for p in pset); return c/nw
NE = {'ne','n'}; QU = {'qu'}; QUE = {'que','qu'}
era = {}
for w in ['on','il','qui']:
    era[w] = {
        'P': eu[w]/N,
        'Pne_fol': Pfol(NE, w),
        'Pqu_pre': Ppreis(QU, w),
        'Pque_fol': Pfol(QUE, w),
        'Pl_pre': Ppreis({'l'}, w),
        'Pssi_pre': Ppreis({'s','si'}, w),
        'Pme_fol': Pfol({'me'}, w),
        'Pqui_par': sum(eb[('par',x)] for x in ['on','il','qui'])/eu['par'] if False else None,
    }
era['P_qui_given_par'] = eb[('par','qui')]/eu['par']
era['tokens'] = N
res['era'] = era

def binom_logL(k, nn, p):
    if p <= 0: return float('-inf') if k > 0 else 0.0
    if p >= 1: return float('-inf') if k < nn else 0.0
    return k*math.log(p) + (nn-k)*math.log(1-p)
def binom_p_ge(k, nn, p):
    # exact upper-tail P(X>=k)
    from math import comb
    return sum(comb(nn, j)*(p**j)*((1-p)**(nn-j)) for j in range(k, nn+1))

# ---------- Leg 1: elision-habit calibration ----------
fol46 = collections.Counter(pairs[i+1] for i in range(n-1) if pairs[i] == 46)
fol94 = collections.Counter(pairs[i+1] for i in range(n-1) if pairs[i] == 94)
leg1 = {
    'f46_34_i': fol46[34], 'f46_40_e': fol46[40], 'f46_29_er': fol46[29],
    'f46_11_la': fol46[11], 'f46_70_pre': fol46[70], 'f46_82_m': fol46[82],
    'f94_34_i': fol94[34], 'f94_40_e': fol94[40], 'f94_29_er': fol94[29],
    'n46_nonfinal': n46nf,
    'note': '46 writes /k/ before vowel-initial 29=er x2 (qu-er), never before /i/(34),/e/(40); 94 same shape (0,0,1).',
}
# H-split adverse under 62="on": E=29*P(qu|on), obs 0
p_qu_on = era['on']['Pqu_pre']; p_qu_il = era['il']['Pqu_pre']
leg1['Hsplit_adverse_on'] = {'E': 29*p_qu_on, 'P0': (1-p_qu_on)**29, 'Pqu_on': p_qu_on}
leg1['Hsplit_adverse_il'] = {'E': 29*p_qu_il, 'P0': (1-p_qu_il)**29, 'Pqu_il': p_qu_il}
leg1['verdict'] = ('VOID both N28 merger-corroboration and N35 il-kill as licensed inferences; '
    'under best-calibrated habit (split /k/+V, 4 instances: 46-29 x2 GT + 87-01 x2 prov-cond) '
    '46->62=0 is ADVERSE to "on" (p~3e-4, caveated) and INERT re "il" (/k/+/i/ split uncalibrated: 46->34=0).')
res['leg1_calibration'] = leg1

# ---------- Leg 2: three-way ----------
a = {}  # 62->94 = 9/35 vs P(ne|w) [cond. 94="ne" prov-strong]
for w in ['on','il','qui']:
    p = era[w]['Pne_fol']
    a[w] = {'p': p, 'logL': binom_logL(9, 35, p), 'p_ge9': binom_p_ge(9, 35, p)}
b = {}  # 62->46 = 1/35 vs P(que|w) [GT 46]
for w in ['on','il','qui']:
    p = era[w]['Pque_fol']
    if p == 0: p = 1/(eu[w]+2)  # Laplace floor for the zero
    b[w] = {'p_raw': era[w]['Pque_fol'], 'p_used': p, 'logL': binom_logL(1, 35, p)}
d = {}  # 96->62 = 0/21 vs P(w|par) [prov 96]
for w in ['on','il','qui']:
    pw_par = eb[('par',w)]/eu['par']
    d[w] = {'p': pw_par, 'logL': binom_logL(0, 21, pw_par)}
joint = {w: a[w]['logL'] + b[w]['logL'] + d[w]['logL'] for w in ['on','il','qui']}
# unigram (hedged: groups != words; reported separately, not in joint)
c = {}
for w in ['on','il','qui']:
    c[w] = {'ratio_group': (n62/n) / era[w]['P'], 'logL_group': binom_logL(n62, n, era[w]['P'])}
res['leg2_threeway'] = {
    'a_ne_rate_9_35_cond_94ne_prov': a,
    'b_que_fol_1_35_GT46': b,
    'd_par_pre_0_21_prov96': d,
    'joint_a_b_d': joint,
    'delta_on_il': joint['on']-joint['il'],
    'delta_on_qui': joint['on']-joint['qui'],
    'c_unigram_hedged': c,
    'verdict': 'on≈il TIE (Δ=+0.27 nats for on on clean pieces); qui weakly disfavored (-6.2 nats, driven by 62->46=1 and ne-rate). Unigram favors il (+9.4 nats) but granularity-hedged.',
}

# ---------- Leg 3: the 59 follow ----------
fol59 = collections.Counter(pairs[i+1] for i in range(n-1) if pairs[i] == 59)
pre59 = collections.Counter(pairs[i-1] for i in range(1, n) if pairs[i] == 59)
xframes = collections.Counter(pairs[i+2] for i in range(n-2) if pairs[i] == 62 and pairs[i+1] == 94)
res['leg3_59'] = {
    'n59': uni[59], 'fol59': dict(sorted(fol59.items())), 'pre59': dict(sorted(pre59.items())),
    'f59_46': big[(59,46)], 'f94_59': big[(94,59)], 'f59_29': big[(59,29)], 'f59_52': big[(59,52)],
    'f11_59': big[(11,59)], 'f87_59': big[(87,59)], 'f64_59': big[(64,59)],
    'subjects_via_94': sorted(set(pairs[i-1] for i in range(1,n-1) if pairs[i]==94 and pairs[i+1]==59)),
    'xframes_62_94_X': dict(xframes),
    'f62_X_46_trigrams': sum(1 for i in range(n-2) if pairs[i]==62 and pairs[i+2]==46),
    'verdict': '59=verb established structurally (11=la GT -> 59: object-pronoun+verb). Subject-selection does not discriminate on/il with available instruments; impersonal-only not established (needs own >=2-check battery). NULL on on-vs-il.',
}

# ---------- unbridgeability proof tables ----------
res['unbridgeability'] = {
    'followers': {
        'mappable': {
            '94=[ne]prov-strong n=9': 'both in band (1.62x/1.36x); RECYCLED (N35)',
            '96=[par]prov n=1': 'P(par|on)=P(par|il)=0 both; non-discriminating',
            '21=[me]LEAD n=1': 'P(me|on)=0.0050 P(me|il)=0.0097; both small; non-discriminating',
            '46=que GT n=1': 'P(que|on)=0.0050 P(que|il)=0.0018; weak, n=1',
        },
        'discriminative_but_unidentified': {
            'impersonal verbs (faut/y-a/semble/suffit/convient)': 'il-only followers; no identified cell',
            '48 x6, 98 x5, 16 x4, 61 x2, 6 x2, 91/18/38/93 x1': 'unidentified; cannot map to era',
        },
    },
    'predecessors': {
        'mappable': {
            '40=e GT n=1, 34=i GT n=1': 'bare letters; unmappable in word space',
            '77=[le]prov n=1': '"le on"/"le il" both 0; non-discriminating',
            '78=proclitic n=2': '"l\'"-word killed (58x N20); euphonic l\' unidentified',
            '21=[me]LEAD n=5': '"me on"/"me il" both ~0; shared puzzle, non-discriminating',
        },
        'discriminative_but_unidentified': {
            '"l\'" (l\'on, P=0.0619 on-only)': 'l\'-cell unidentified',
            '"s"/"si" (s\'il/si-on asymmetry, P=0.0369/0.0080)': 'cells unidentified',
            '20 x4, 74 x3, 93/3/8/92 x2, singles': 'unidentified; cannot map to era',
        },
    },
    'conclusion': 'No follower/predecessor cell is BOTH mappable AND discriminative with n>>2. The red-team-named profile route is structurally unachievable with the current value inventory.',
}

# ---------- 62/64 overlap (qui-rival) ----------
fol64 = collections.Counter(pairs[i+1] for i in range(n-1) if pairs[i] == 64)
pre64 = collections.Counter(pairs[i-1] for i in range(1, n) if pairs[i] == 64)
res['overlap_62_64'] = {
    'jaccard_fol': len(set(fol62)&set(fol64))/len(set(fol62)|set(fol64)),
    'jaccard_pre': len(set(pre62)&set(pre64))/len(set(pre62)|set(pre64)),
    'f87_62': big[(87,62)], 'f87_64': big[(87,64)],
    'f62_64': big[(62,64)], 'f64_62': big[(64,62)],
    'note': 'Low overlap consistent with conditioned polyvalence OR distinct values; 87->62=0 vs 87->64=5 needs a conditioning rule for a 62="qui" allophone claim (none identified).',
}

with open(OUT/'battery62_results.json','w') as f:
    json.dump(res, f, indent=1)
print(json.dumps({
    'baselines': res['baselines'],
    'leg1_Hsplit_adverse_on': leg1['Hsplit_adverse_on'],
    'leg1_Hsplit_adverse_il': leg1['Hsplit_adverse_il'],
    'leg2_joint': joint, 'delta_on_il': joint['on']-joint['il'], 'delta_on_qui': joint['on']-joint['qui'],
    'leg2_a': {w: {'p': round(a[w]['p'],4), 'logL': round(a[w]['logL'],2), 'p_ge9': round(a[w]['p_ge9'],4)} for w in a},
    'leg2_b': {w: {'logL': round(b[w]['logL'],2)} for w in b},
    'leg2_c_ratios': {w: round(c[w]['ratio_group'],2) for w in c},
}, indent=1))
