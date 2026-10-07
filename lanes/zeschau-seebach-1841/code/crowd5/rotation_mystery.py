#!/usr/bin/env python3
"""rotation_mystery.py — SEGMENTER executor, round 5: WHAT IS THE ROTATION?

Implements the pre-registered battery in code/crowd5/rotation_mystery.md.
All inputs: code/side-keyhunt/repaired_offsets.json (1,847 pairs), banked
code/crowd4/phase_map_repaired.json (re-derived independently here, T0).

Cipher-internal only (F30-legal). No era legs. No invented values.
Chance baselines are stated per test in rotation_mystery.md.
"""
import json, os, sys, math, collections, itertools, random

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd4'))
from repaired_parse import load_pairs_repaired

random.seed(20261007)
OUT = {}


def derive_phases(stream, k_cut=12):
    """Jaccard-k12 agglomerative (contactor's method), reimplemented here."""
    groups = sorted(set(stream))
    foll = collections.defaultdict(collections.Counter)
    pred = collections.defaultdict(collections.Counter)
    for a, b in zip(stream, stream[1:]):
        foll[a][b] += 1
        pred[b][a] += 1
    K = 10
    TOP = {g: (set(h for h, _ in foll[g].most_common(K)) |
               set(h for h, _ in pred[g].most_common(K))) for g in groups}

    def jac(a, b):
        sa, sb = TOP[a], TOP[b]
        u = sa | sb
        return len(sa & sb) / len(u) if u else 0.0

    clusters = [{g} for g in groups]
    merges = []
    while len(clusters) > 1:
        best, bi, bj = -1.0, None, None
        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                c1, c2 = clusters[i], clusters[j]
                s = sum(jac(a, b) for a in c1 for b in c2) / (len(c1) * len(c2))
                if s > best:
                    best, bi, bj = s, i, j
        merges.append((sorted(clusters[bi]), sorted(clusters[bj])))
        new = clusters[bi] | clusters[bj]
        clusters = [c for k, c in enumerate(clusters)
                    if k not in (bi, bj)] + [new]
    cs = [{g} for g in groups]
    for c1l, c2l in merges:
        if len(cs) <= k_cut:
            break
        c1, c2 = set(c1l), set(c2l)
        cs = [c for c in cs if c != c1 and c != c2] + [c1 | c2]
    cs = sorted(cs, key=len, reverse=True)
    block = {}
    for x, lbl in ((cs[0], 'A'), (cs[1], 'B'), (cs[2], 'C')):
        for g in x:
            block[g] = lbl
    for c in cs[3:]:
        for g in c:
            block[g] = 'R'
    return block


def chi2_3x3(stream, block):
    trans = [(a, b) for a, b in zip(stream, stream[1:])]
    return chi2_3x3_trans(trans, block)


def chi2_3x3_trans(trans, block):
    obs = [[0] * 3 for _ in range(3)]
    for a, b in trans:
        pa, pb = block[a], block[b]
        if pa in 'ABC' and pb in 'ABC':
            obs['ABC'.index(pa)]['ABC'.index(pb)] += 1
    rs = [sum(r) for r in obs]
    cs = [sum(obs[r][c] for r in range(3)) for c in range(3)]
    T = sum(rs)
    chi2 = sum((obs[r][c] - rs[r] * cs[c] / T) ** 2 / (rs[r] * cs[c] / T)
               for r in range(3) for c in range(3) if rs[r] * cs[c])
    return chi2, obs, rs, cs, T


pairs, odd_lines, off1 = load_pairs_repaired()
N = len(pairs)
freq = collections.Counter(pairs)
groups = sorted(set(pairs))

# ---------------- T0: re-derive phases, verify ----------------
block = derive_phases(pairs)
banked = json.load(open(os.path.join(LANE, 'code', 'crowd4',
                                     'phase_map_repaired.json')))
t0_match = (block == banked)
chi2, obs, rs, cs, T = chi2_3x3(pairs, block)
print("T0: rederived==banked:", t0_match, "| chi2=%.1f (banked 366.3)" % chi2)
OUT['T0'] = {'rederived_matches_banked': t0_match,
             'chi2_3x3': round(chi2, 1), 'ABC_transitions': T,
             'phase_sizes': dict(collections.Counter(block.values()))}
if not t0_match:
    print("T0 FAIL: phases not reproduced — STOP")
    json.dump(OUT, open(os.path.join(HERE, 'rotation_mystery.json'), 'w'), indent=1)
    sys.exit(2)

P = block  # group -> phase
CYCLE = {('A', 'C'), ('C', 'B'), ('B', 'A')}

def on_cycle(a, b):
    return (P[a], P[b]) in CYCLE

# global on-cycle rate among ABC transitions
abct = [(a, b) for a, b in zip(pairs, pairs[1:])
        if P[a] in 'ABC' and P[b] in 'ABC']
p_on = sum(1 for a, b in abct if (P[a], P[b]) in CYCLE) / len(abct)
OUT['globals'] = {'p_on_global': round(p_on, 4),
                  'n_abc_transitions': len(abct)}
print("global p_on=%.4f over %d ABC transitions" % (p_on, len(abct)))

# per-phase marginals for chance baselines
pm = collections.Counter(block.values())
pm_n = {k: v / 96 for k, v in pm.items()}
p_same_phase = sum(v * v for v in pm_n.values())
OUT['globals']['p_same_phase_by_chance'] = round(p_same_phase, 4)


def binom_ge(n, k, p):
    return sum(math.comb(n, i) * p ** i * (1 - p) ** (n - i)
               for i in range(k, n + 1))


def binom_le(n, k, p):
    return sum(math.comb(n, i) * p ** i * (1 - p) ** (n - i)
               for i in range(0, k + 1))


def perm_test(labels, values, stat_fn, n_perm=10000, direction='ge'):
    """labels: list of class tags; values: list of phase values; statistic
    computed per class profile. Returns (obs, p)."""
    obs = stat_fn(labels, values)
    ge = 0
    lab = list(labels)
    for _ in range(n_perm):
        random.shuffle(lab)
        s = stat_fn(lab, values)
        if direction == 'ge' and s >= obs:
            ge += 1
        elif direction == 'le' and s <= obs:
            ge += 1
    return obs, (ge + 1) / (n_perm + 1)


# ---------------- T1a: 06 vs 86 mood contrast ----------------
print("T1a: 06 phase=%s, 86 phase=%s (same=%s; chance P(same)=%.3f)"
      % (P['06'], P['86'], P['06'] == P['86'], p_same_phase))
OUT['T1a'] = {'phase_06': P['06'], 'phase_86': P['86'],
              'same_phase': P['06'] == P['86'],
              'p_same_by_chance': round(p_same_phase, 4)}

# ---------------- T1b/T1c: formula-edge on-cycle depletion ----------------
formula_edges = [
    # (a,b,tag)
    ('11', '70', 'w'), ('70', '82', 'w'), ('82', '34', 'w'), ('34', '29', 'w'),
    ('29', '40', 'w'),                       # la premiere (word-internal)
    ('96', '87', 'f'), ('87', '46', 'f'),    # parce que
    ('87', '64', 'f'),                       # ce qui
    ('24', '87', 'f'),                       # 24-87-64 formula
    ('77', '78', 'f'), ('78', '94', 'f'), ('94', '82', 'f'), ('82', '06', 'f'),
    ('64', '96', 'f'), ('96', '43', 'f'), ('43', '87', 'f'), ('87', '01', 'f'),
    ('62', '94', 'f'),                       # on ne
    ('94', '52', 'f'),
    ('06', '29', 'w'),                       # stem|suffix cut
    ('77', '86', 'f'),                       # le + infinitive stem
    ('78', '40', 'f'),
    ('47', '78', 'f'),
    ('37', '78', 'f'),
    ('94', '59', 'f'),
    ('87', '11', 'f'),                       # cela
    ('93', '52', 'w'), ('52', '94', 'w'),    # personne cut @160
    ('77', '62', 'w'), ('62', '94', 'w'),    # personne cut @507
    # 9-mer 56 69 26 00 33 21 64 37 01 x2
    ('56', '69', 'f'), ('69', '26', 'f'), ('26', '00', 'f'), ('00', '33', 'f'),
    ('33', '21', 'f'), ('21', '64', 'f'), ('64', '37', 'f'), ('37', '01', 'f'),
]
fe = [(a, b, t) for a, b, t in formula_edges
      if P[a] in 'ABC' and P[b] in 'ABC']
fe_r = [(a, b, t) for a, b, t in formula_edges
        if not (P[a] in 'ABC' and P[b] in 'ABC')]
obs_on = sum(1 for a, b, _ in fe if (P[a], P[b]) in CYCLE)
n_fe = len(fe)
p_le = binom_le(n_fe, obs_on, p_on)
p_ge = binom_ge(n_fe, obs_on, p_on)
# exclude-formula baseline
abct_x = [(a, b) for a, b in abct if (a, b) not in {(x, y) for x, y, _ in fe}]
p_on_x = sum(1 for a, b in abct_x if (P[a], P[b]) in CYCLE) / len(abct_x)
p_le_x = binom_le(n_fe, obs_on, p_on_x)
print("T1b: %d unique ABC formula edges, %d on-cycle; global p_on=%.3f -> "
      "binom P(<=obs)=%.4f P(>=obs)=%.4f; excl-baseline p_on=%.3f P(<=obs)=%.4f"
      % (n_fe, obs_on, p_on, p_le, p_ge, p_on_x, p_le_x))
OUT['T1b'] = {'n_edges': n_fe, 'n_on_cycle': obs_on,
              'r_touched_excluded': len(fe_r),
              'p_on_global': round(p_on, 4),
              'binom_P_le_obs': round(p_le, 4),
              'binom_P_ge_obs': round(p_ge, 4),
              'p_on_excl_formula': round(p_on_x, 4),
              'binom_P_le_obs_excl': round(p_le_x, 4),
              'off_cycle_edges': [(a, b) for a, b, _ in fe
                                  if (P[a], P[b]) not in CYCLE],
              'on_cycle_edges': [(a, b) for a, b, _ in fe
                                 if (P[a], P[b]) in CYCLE]}
wi = [(a, b) for a, b, t in fe if t == 'w']
cw = [(a, b) for a, b, t in fe if t == 'f']
on_wi = sum(1 for a, b in wi if (P[a], P[b]) in CYCLE)
on_cw = sum(1 for a, b in cw if (P[a], P[b]) in CYCLE)
OUT['T1c'] = {'word_internal': {'n': len(wi), 'on': on_wi,
                                'P_le': round(binom_le(len(wi), on_wi, p_on), 4)},
              'cross_word': {'n': len(cw), 'on': on_cw,
                             'P_le': round(binom_le(len(cw), on_cw, p_on), 4)}}
print("T1c: word-internal %d edges %d on-cycle (P<=%.4f); cross-word %d edges "
      "%d on-cycle (P<=%.4f)" % (len(wi), on_wi, OUT['T1c']['word_internal']['P_le'],
                                 len(cw), on_cw, OUT['T1c']['cross_word']['P_le']))

# T1d: 00->86 frame vs global P(B|C)
foll00 = collections.Counter(b for a, b in zip(pairs, pairs[1:]) if a == '00')
n00 = sum(foll00.values())
obs_86 = foll00['86']
ct = [(a, b) for a, b in abct if P[a] == 'C']
p_BgC = sum(1 for a, b in ct if P[b] == 'B') / len(ct)
OUT['T1d'] = {'00_followers_total': n00, '00_to_86': obs_86,
              'global_P_B_given_C': round(p_BgC, 4),
              'binom_P_ge': round(binom_ge(n00, obs_86, p_BgC), 4)}
print("T1d: 00->86 %d/%d; global P(B|C)=%.4f -> P(>=)=%.4f"
      % (obs_86, n00, p_BgC, OUT['T1d']['binom_P_ge']))

# ---------------- T2a: 06 trigram vs free ----------------
occ06 = [i for i, g in enumerate(pairs) if g == '06']
trigram06 = [i for i in occ06
             if i >= 2 and pairs[i - 1] == '82' and pairs[i - 2] == '94']
free06 = [i for i in occ06 if i not in set(trigram06)]
print("T2a: 06 occurrences=%d, trigram-final=%d at %s, free=%d"
      % (len(occ06), len(trigram06), trigram06, len(free06)))

def next_phase_profile(labels, idxs):
    # labels: 'T'/'F'; idxs: positions; returns chi2-distance of next-phase
    # profiles between the two classes
    prof = {}
    for lab, i in zip(labels, idxs):
        np_ = P[pairs[i + 1]] if i + 1 < N else 'R'
        prof.setdefault(lab, collections.Counter())[np_] += 1
    t, f = prof.get('T', collections.Counter()), prof.get('F', collections.Counter())
    keys = set(t) | set(f)
    nt, nf = sum(t.values()), sum(f.values())
    if nt == 0 or nf == 0:
        return 0.0
    d = 0.0
    for k in keys:
        pt, pf = t.get(k, 0) / nt, f.get(k, 0) / nf
        m = (pt + pf) / 2
        if m:
            d += (pt - pf) ** 2 / m
    return d

labels06 = ['T' if i in set(trigram06) else 'F' for i in occ06]
obs_d, p_d = perm_test(labels06, occ06, next_phase_profile, n_perm=10000)
print("T2a: next-phase chi2-dist T-vs-F = %.3f; permutation p=%.4f"
      % (obs_d, p_d))
OUT['T2a'] = {'n_trigram': len(trigram06), 'trigram_pos': trigram06,
              'n_free': len(free06),
              'chi2_dist_obs': round(obs_d, 4),
              'permutation_p': round(p_d, 4),
              'trigram_next_phases': [P[pairs[i + 1]] for i in trigram06],
              'free_next_phase_dist': dict(collections.Counter(
                  P[pairs[i + 1]] for i in free06))}

# T2c: naked adjacency of 06 readings
near06 = [(a, b) for a in occ06 for b in occ06 if a < b <= a + 3]
t2c_rows = []
for a, b in near06:
    ra = 'T' if a in set(trigram06) else 'F'
    rb = 'T' if b in set(trigram06) else 'F'
    t2c_rows.append({'i1': a, 'r1': ra, 'i2': b, 'r2': rb,
                     'prev_ph': [P[pairs[a - 1]], P[pairs[b - 1]]],
                     'next_ph': [P[pairs[a + 1]], P[pairs[b + 1]]]})
mixed_same_env = [r for r in t2c_rows if r['r1'] != r['r2']
                  and r['prev_ph'][0] == r['prev_ph'][1]
                  and r['next_ph'][0] == r['next_ph'][1]]
print("T2c: %d near-06 pairs; mixed-reading same-phase-env: %d"
      % (len(t2c_rows), len(mixed_same_env)))
OUT['T2c'] = {'n_near_pairs': len(t2c_rows), 'rows': t2c_rows,
              'mixed_same_env': mixed_same_env}

# ---------------- T2d: 94 en-islet vs ne ----------------
occ94 = [i for i, g in enumerate(pairs) if g == '94']
en94 = [i for i in occ94
        if (i > 0 and pairs[i - 1] == '82') or (i + 1 < N and pairs[i + 1] == '87')]
ne94 = [i for i in occ94 if i not in set(en94)]
print("T2d: 94 occurrences=%d, en-islet=%d at %s, ne=%d"
      % (len(occ94), len(en94), en94, len(ne94)))

def prev_phase_profile(labels, idxs):
    prof = {}
    for lab, i in zip(labels, idxs):
        pp = P[pairs[i - 1]] if i > 0 else 'R'
        prof.setdefault(lab, collections.Counter())[pp] += 1
    e = prof.get('E', collections.Counter())
    n_ = prof.get('N', collections.Counter())
    keys = set(e) | set(n_)
    ne_, nn_ = sum(e.values()), sum(n_.values())
    if ne_ == 0 or nn_ == 0:
        return 0.0
    d = 0.0
    for k in keys:
        pe, pn = e.get(k, 0) / ne_, n_.get(k, 0) / nn_
        m = (pe + pn) / 2
        if m:
            d += (pe - pn) ** 2 / m
    return d

labels94 = ['E' if i in set(en94) else 'N' for i in occ94]
obs_d94, p_d94 = perm_test(labels94, occ94, prev_phase_profile, n_perm=10000)
print("T2d: prev-phase chi2-dist E-vs-N = %.3f; permutation p=%.4f"
      % (obs_d94, p_d94))
OUT['T2d'] = {'n_en': len(en94), 'en_pos': en94, 'n_ne': len(ne94),
              'chi2_dist_obs': round(obs_d94, 4),
              'permutation_p': round(p_d94, 4),
              'en_prev_phases': [P[pairs[i - 1]] for i in en94],
              'ne_prev_phase_dist': dict(collections.Counter(
                  P[pairs[i - 1]] for i in ne94))}

# T2e: 52 pas (negation frame) vs other
occ52 = [i for i, g in enumerate(pairs) if g == '52']
pas52 = [i for i in occ52
         if any(pairs[j] == '94' for j in range(max(0, i - 6), i))]
oth52 = [i for i in occ52 if i not in set(pas52)]
labels52 = ['P' if i in set(pas52) else 'O' for i in occ52]
obs_d52, p_d52 = perm_test(labels52, occ52, next_phase_profile, n_perm=10000)
print("T2e: 52 occurrences=%d, neg-frame=%d, other=%d; next-phase chi2-dist=%.3f p=%.4f"
      % (len(occ52), len(pas52), len(oth52), obs_d52, p_d52))
OUT['T2e'] = {'n_pas_frame': len(pas52), 'n_other': len(oth52),
              'chi2_dist_obs': round(obs_d52, 4),
              'permutation_p': round(p_d52, 4),
              'note': 'frame heuristic (94 within -6..-1) is approximate'}

# ---------------- T3: unit-size vs phase (crib-learned cells, R1) ----------------
cells = {'11': ('la', 2, 'GT'), '70': ('pre', 3, 'GT'), '82': ('m', 1, 'GT'),
         '34': ('i', 1, 'GT'), '29': ('er', 2, 'GT'), '40': ('e', 1, 'GT'),
         '46': ('que', 3, 'GT'), '87': ('ce', 2, 'prov'), '64': ('qui', 3, 'prov'),
         '96': ('par', 3, 'prov'), '94': ('ne', 2, 'prov'),
         '62': ('on', 2, 'STRONG-LEAD'), '78': ('me', 2, 'LEAD'),
         '77': ('le', 2, 'LEAD'), '47': ('ce', 2, 'LEAD'),
         '52': ('pas', 3, 'STRONG-bounded'), '67': ('veut', 4, 'prov')}
gs3 = sorted(cells)
lab3 = [P[g] for g in gs3]

def t3a_stat(labels, _):
    lc = [cells[g][1] for g, l in zip(gs3, labels) if l == 'C']
    lo = [cells[g][1] for g, l in zip(gs3, labels) if l != 'C']
    if not lc or not lo:
        return 0.0
    return sum(lc) / len(lc) - sum(lo) / len(lo)

obs3a, p3a = perm_test(lab3, None, t3a_stat, n_perm=10000, direction='le')

def t3b_stat(labels, _):
    means = {}
    for g, l in zip(gs3, labels):
        means.setdefault(l, []).append(cells[g][1])
    ms = [sum(v) / len(v) for v in means.values()]
    m0 = sum(ms) / len(ms)
    return sum((m - m0) ** 2 for m in ms)

obs3b, p3b = perm_test(lab3, None, t3b_stat, n_perm=10000, direction='ge')
mc = [cells[g][1] for g in gs3 if P[g] == 'C']
mo = [cells[g][1] for g in gs3 if P[g] != 'C']
print("T3: n=%d; mean(C)=%.2f mean(not-C)=%.2f diff=%.2f perm-p(one-sided)=%.4f; "
      "3way var=%.3f perm-p=%.4f"
      % (len(gs3), sum(mc) / len(mc), sum(mo) / len(mo), obs3a, p3a, obs3b, p3b))
OUT['T3'] = {'n_cells': len(gs3),
             'mean_len_C': round(sum(mc) / len(mc), 3),
             'mean_len_notC': round(sum(mo) / len(mo), 3),
             'diff_obs': round(obs3a, 4), 'perm_p_directional': round(p3a, 4),
             'var_means_obs': round(obs3b, 4), 'perm_p_3way': round(p3b, 4),
             'cells': {g: {'val': cells[g][0], 'len': cells[g][1],
                           'status': cells[g][2], 'phase': P[g]}
                       for g in gs3}}

# ---------------- T4: syntactic ----------------
F_func = ['11', '46', '87', '64', '96', '94']  # la que ce qui par ne
phF = [P[g] for g in F_func]
kB = sum(1 for x in phF if x == 'B')
pB = pm_n['B']
p4a = binom_ge(6, kB, pB)
F_ext = F_func + ['52', '47']  # + pas (bounded), ce47 (LEAD)
phE = [P[g] for g in F_ext]
kBE = sum(1 for x in phE if x == 'B')
p4a_ext = binom_ge(8, kBE, pB)
print("T4a: function phases=%s -> %d/6 in B (pB=%.3f) P(>=)=%.4f; ext %d/8 in B P(>=)=%.4f"
      % (dict(zip(F_func, phF)), kB, pB, p4a, kBE, p4a_ext))
OUT['T4a'] = {'function_phases': dict(zip(F_func, phF)), 'k_in_B': kB,
              'p_B': round(pB, 4), 'binom_P_ge': round(p4a, 4),
              'ext_phases': dict(zip(F_ext, phE)), 'ext_k_in_B': kBE,
              'ext_binom_P_ge': round(p4a_ext, 4)}
same48 = (P['82'] == P['87'])
print("T4b: 82 phase=%s, 87 phase=%s same=%s (chance P(same)=%.3f)"
      % (P['82'], P['87'], same48, p_same_phase))
OUT['T4b'] = {'phase_82': P['82'], 'phase_87': P['87'], 'same': same48,
              'p_same_by_chance': round(p_same_phase, 4)}
frag = {'70': 'pre', '82': 'm', '34': 'i', '29': 'er', '40': 'e'}
OUT['T4c'] = {'fragment_phases': {g: P[g] for g in frag},
              'distinct_phases': len(set(P[g] for g in frag))}
print("T4c: GT fragment phases: %s (%d distinct of 5)"
      % (OUT['T4c']['fragment_phases'], OUT['T4c']['distinct_phases']))

# ---------------- T5a: hub masking ----------------
by_freq = [g for g, _ in freq.most_common()]
mask_rows = []
for k in range(0, 11):
    topk = by_freq[:k]
    mk = set(topk)
    # drop transitions touching masked groups (no artificial re-zipping)
    rem = [(a, b) for a, b in zip(pairs, pairs[1:])
           if a not in mk and b not in mk]
    c2, o2, _, _, T2 = chi2_3x3_trans(rem, P)
    mask_rows.append({'k': k, 'masked': list(topk), 'chi2': round(c2, 1),
                      'abc_transitions': T2})
    print("T5a: mask top-%d -> chi2=%.1f (n_trans=%d)" % (k, c2, T2))
OUT['T5a'] = {'mask_rows': mask_rows}

# ---------------- T5b: temporal halves ----------------
h1, h2 = pairs[:923], pairs[923:]
c_h1, _, _, _, T_h1 = chi2_3x3(h1, P)
c_h2, _, _, _, T_h2 = chi2_3x3(h2, P)
print("T5b: first half chi2=%.1f (n=%d); second half chi2=%.1f (n=%d)"
      % (c_h1, T_h1, c_h2, T_h2))
OUT['T5b'] = {'half1': {'chi2': round(c_h1, 1), 'abc_transitions': T_h1},
              'half2': {'chi2': round(c_h2, 1), 'abc_transitions': T_h2}}

json.dump(OUT, open(os.path.join(HERE, 'rotation_mystery.json'), 'w'), indent=1)
print("wrote rotation_mystery.json")
