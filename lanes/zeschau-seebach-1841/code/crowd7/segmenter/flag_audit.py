#!/usr/bin/env python3
"""flag_audit.py — SEGMENTER round 7, Thread A: apply the N43 noisy-detector
flag to the round-6 package. Re-derives the two load-bearing numbers (gate E1,
P2a momentum) fresh; audits T1/T2/T3/P2b/P2c against the red-team-verified
rotation_r6.json (N41 UPHELD). Writes flag_audit.json. See PREREG7.md."""
import json, os, sys, math
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd4'))
from repaired_parse import load_pairs_repaired

OUT = {}
pairs, _, _ = load_pairs_repaired()
N = len(pairs)
assert N == 1847, N
GROUPS = sorted(set(pairs))
BANKED = json.load(open(os.path.join(LANE, 'code', 'crowd4',
                                     'phase_map_repaired.json')))
LABS4 = ('A', 'B', 'C', 'R')


def apply_labels(stream, lab):
    return [lab[g] for g in stream]


def fit_markov(lseq, states=LABS4, alpha=0.0):
    S = list(states)
    si = {s: i for i, s in enumerate(S)}
    m = len(S)
    C = np.zeros((m, m))
    for a, b in zip(lseq, lseq[1:]):
        C[si[a], si[b]] += 1
    M = (C + alpha) / (C.sum(axis=1, keepdims=True) + alpha * m)
    w, v = np.linalg.eig(M.T)
    pi = np.real(v[:, np.argmin(np.abs(w - 1.0))])
    pi = pi / pi.sum()
    return M, pi, C


def e1_stat(lseq):
    n_all = len(lseq) - 3
    idx = [t for t in range(n_all) if lseq[t] in 'ABC' and lseq[t + 3] in 'ABC']
    n = len(idx)
    obs = sum(1 for t in idx if lseq[t] == lseq[t + 3]) / n
    M, pi, _ = fit_markov(lseq)
    M3 = np.linalg.matrix_power(M, 3)
    num = float(sum(pi[s] * M3[s, s] for s in range(3)))
    den = float(sum(pi[s] * M3[s, :3].sum() for s in range(3)))
    exp = num / den
    se = math.sqrt(exp * (1 - exp) / n)
    return {'n': n, 'obs': round(obs, 4), 'exp': round(exp, 4),
            'z': round((obs - exp) / se, 2)}


def directed_cycle_mass(lseq):
    mf = sum(1 for a, b in zip(lseq, lseq[1:])
             if (a, b) in {('A', 'B'), ('B', 'C'), ('C', 'A')})
    mr = sum(1 for a, b in zip(lseq, lseq[1:])
             if (a, b) in {('A', 'C'), ('C', 'B'), ('B', 'A')})
    return mf, mr


def p2a(lseq):
    mf, mr = directed_cycle_mass(lseq)
    CYC = {'A': 'B', 'B': 'C', 'C': 'A'} if mf > mr else {'A': 'C', 'C': 'B', 'B': 'A'}
    n1 = n0 = c1 = c0 = 0
    for t in range(1, len(lseq) - 1):
        a, b, c_ = lseq[t - 1], lseq[t], lseq[t + 1]
        if not (a in 'ABC' and b in 'ABC' and c_ in 'ABC'):
            continue
        if b == CYC[a]:
            n1 += 1
            c1 += (c_ == CYC[b])
        elif b != a:
            n0 += 1
            c0 += (c_ == CYC[b])
    r1, r0 = c1 / n1, c0 / n0
    p_pool = (c1 + c0) / (n1 + n0)
    se_p = math.sqrt(p_pool * (1 - p_pool) * (1 / n1 + 1 / n0))
    z_p = (r1 - r0) / se_p
    p_one = 1 - 0.5 * (1 + math.erf(z_p / math.sqrt(2)))
    return {'r1': round(r1, 4), 'n1': n1, 'r0': round(r0, 4), 'n0': n0,
            'z': round(z_p, 2), 'p_one_sided': round(p_one, 6)}


lseq_ref = apply_labels(pairs, BANKED)

# A1: re-derive gate E1
e1 = e1_stat(lseq_ref)
OUT['A1_gate_rederived'] = e1
print("A1 gate E1 re-derived: obs=%.4f exp=%.4f z=%.2f n=%d "
      "(round6: 0.4219/0.3505/+5.81)" % (e1['obs'], e1['exp'], e1['z'], e1['n']))
assert abs(e1['obs'] - 0.4219) < 0.002 and abs(e1['z'] - 5.81) < 0.3, "gate mismatch"

# A2: re-derive P2a momentum (full stream)
m_full = p2a(lseq_ref)
OUT['A2_p2a_rederived'] = m_full
print("A2 P2a re-derived: r1=%.4f (n=%d) r0=%.4f (n=%d) z=%.2f p=%.6f "
      "(round6: 0.6327/765/0.4856/383/+4.77)" %
      (m_full['r1'], m_full['n1'], m_full['r0'], m_full['n0'],
       m_full['z'], m_full['p_one_sided']))
assert abs(m_full['r1'] - 0.6327) < 0.002 and abs(m_full['z'] - 4.77) < 0.1

# A3-A7: audit against red-team-verified rotation_r6.json
r6 = json.load(open(os.path.join(LANE, 'code', 'crowd6', 'segmenter',
                                 'rotation_r6.json')))
t1, t2, t3, t4 = r6['thread1'], r6['thread2'], r6['thread3'], r6['thread4']

audit = {}

# T1 labeling robustness
audit['T1_labeling_robustness'] = {
    'round6_verdict': 'FRAGILE (verdict_robust=false); k=16 replicates z=+5.54, 91/96 agree; others degenerate',
    'flag_check': {
        'leans_on_exact_chi2': False,
        'leans_on_per_group_phases': 'partial — 91/96 agreement is instrument-vs-instrument metrology, names no cipher claim',
        'failure_mode': t1['V_cos']['sizes'],
    },
    'verdict': 'SURVIVES*',
    'reason': 'Failure mode is labeling degeneracy (mega-clusters), never excess-death; '
              'the lag-3 excess is not impugned. 91/96 k=16 agreement measures instrument '
              'consistency, not mapping truth (both instruments ~0.5 purity per N43(c)).',
}

# T2 HMM
audit['T2_hmm_vs_bigram'] = {
    'round6_verdict': 'NO (bigram testLL/trans -4.2356 beats HMM -4.2638 by 0.028; BIC favors HMM on parsimony); A cyclic',
    'flag_check': {
        'leans_on_exact_chi2': False,
        'leans_on_per_group_phases': False,
        'labels_in_fit': False,
    },
    'verdict': 'SURVIVES',
    'reason': 'No chi2, no labels in the EM fit. The unsupervised cyclic transition matrix '
              '(S1->S0 1.0, S0->S2 0.705, S2->S1 0.672) is label-free corroboration of cyclic '
              'structure — independent support under N43(c). Viterbi contingency was '
              'not verdict-driving (stays fenced).',
}

# T3 reconciliation
audit['T3_reconciliation'] = {
    'round6_verdict': 'naive 35/96 (N30 61-change) vs best-perm 69/96 (N37) — definitional difference',
    'flag_check': {
        'leans_on_exact_chi2': False,
        'leans_on_per_group_phases': 'metrology only — compares two labelings, asserts nothing about the cipher',
    },
    'verdict': 'SURVIVES*',
    'reason': 'Definitional reconciliation stands. Neither 69 nor 35 measures mapping truth '
              'under N43(c) (~0.5 purity on both sides).',
}

# P2b memory-2
audit['P2b_memory2'] = {
    'round6_verdict': 'FALSIFIED(null): 2nd-order LL/trans -1.2189 < 1st-order -1.2143 held-out',
    'flag_check': {
        'leans_on_exact_chi2': False,
        'leans_on_per_group_phases': 'uses label stream, but verdict is a NULL',
    },
    'verdict': 'SURVIVES',
    'reason': 'Null verdict needs no flag protection. Caveat under N43(c): ~0.5-purity labels '
              'reduce power — absence of FULL memory-2 on the noisy label stream does not '
              'preclude structured second-order effects (P2a is the live alternative).',
}

# P2c fixed column order
p2c = t4['P2c']
audit['P2c_fixed_order'] = {
    'round6_verdict': 'FALSIFIED: halves fwd/fwd but variants flip (cos rev, half1 rev, half2 rev)',
    'flag_check': {
        'leans_on_exact_chi2': False,
        'leans_on_per_group_phases': True,
        'variant_partitions': {v: t1[v]['sizes'] for v in
                               ('V_cos', 'V_k8', 'V_k16', 'V_half1', 'V_half2')},
    },
    'verdict': 'DOWNGRADED to INCONCLUSIVE',
    'reason': 'Direction flips are computed on degenerate partitions (V_cos C=1 group; '
              'V_half1 B=5/C=5; V_half2 B=4/C=4) — under N43(c) (~0.5 purity) these cannot '
              'falsify "one column order"; the instrument is invalid for the question. '
              'Halves-consistency (fwd/fwd) on the reference instrument SURVIVES as an '
              'observation. Bedrock: F11 cycle direction is labeling-relative — direction '
              'was never intrinsic.',
}

# P2a momentum flag audit
audit['P2a_momentum'] = {
    'round6_verdict': 'SUPPORT: r1=0.6327 (n=765) vs r0=0.4856 (n=383), z=+4.77',
    'flag_check': {
        'leans_on_exact_chi2': False,
        'leans_on_per_group_phases': False,
        'note': 'Population-level conditional rate — names no group phase. '
                'Uses banked labels (~0.5 purity); label noise ATTENUATES r1-r0, '
                'so the existence signal is conservative under N43(c). '
                'Circularity caveat: labels fit on the same stream (addressed by Thread B).',
    },
    'verdict': 'SURVIVES* PENDING Thread B',
    'reason': 'Does not lean on chi2 magnitude or any per-group phase claim. '
              'Independent label-free confirmation is the Thread-B test.',
}

# Gate
audit['gate_E1'] = {
    'round6_verdict': 'z=+5.81 (obs 0.4219, exp 0.3505, n=1510)',
    'flag_check': {'leans_on_exact_chi2': False, 'leans_on_per_group_phases': False},
    'verdict': 'SURVIVES',
    'reason': 'Flag N43(a) explicitly confirms: rhythm existence by label-free lag-3, not impugned.',
}

OUT['flag_audit'] = audit
json.dump(OUT, open(os.path.join(HERE, 'flag_audit.json'), 'w'), indent=1)
print("\nFlag audit verdicts:")
for k, v in audit.items():
    print("  %-22s -> %s" % (k, v['verdict']))
print("wrote flag_audit.json")
