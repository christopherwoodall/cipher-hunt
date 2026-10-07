#!/usr/bin/env python3
"""Track A step 3 (runs ONLY after red-team PREREG sign-off): rescore the
frozen 184101 truth decode vs the frozen pilot-salad decode under
(a) the Tocqueville reference (sanity: reproduce the verifier's 2,601-nat
    salad-wins margin to <=1 nat), and
(b) the register-matched diplomatic reference built by build_ref.py.

Uses the INDEPENDENT verifier rescorer (verifier/rescore.py) with a single
documented deviation: the lm.json path is overridable. All scoring code,
E-step, phonetics, phase analysis, and config are the verifier's, untouched.
Read-only wrt every other lane dir; writes only track-a/results/.

Outputs: track-a/results/rescore.json (full part tables) + console tables.
"""
import collections
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REBUILD = os.path.abspath(os.path.join(HERE, '..', '..', 'side-homophonic-rebuild'))
sys.path.insert(0, os.path.join(REBUILD, 'verifier'))
import rescore as V  # noqa: E402  (independent verifier rescorer)

SEED = '184101'
LM_TOCQ = os.path.join(REBUILD, 'solver', 'lm_ref', 'lm.json')
LM_DIPLO = os.path.join(HERE, 'lm_ref_diplo', 'lm.json')


class RescorerReg(V.Rescorer):
    """The verifier's Rescorer with ONLY the lm.json path swapped.

    All scoring machinery (CharLM, E-step, phonetics, phase, _cover_sum,
    score()) is inherited byte-for-byte; the only deviation from
    verifier/rescore.py is which reference file is loaded.
    """
    def __init__(self, pairs, cfg, lm_path):
        self.pairs = pairs
        self.cfg = cfg
        self.groups = sorted(set(pairs))
        self.occ = collections.defaultdict(list)
        for t, g in enumerate(pairs):
            self.occ[g].append(t)
        lm_data = json.load(open(lm_path))
        self.lm = V.CharLM(lm_data)
        self.lex = [(e['w'], e['wt']) for e in lm_data['lexicon']]
        self.lex_wt = {e['w']: e['wt'] for e in lm_data['lexicon']}
        self.phase = V.analyze_stream(pairs)
        self.beta = cfg['beta0'] * self.phase['gate']
        self.lm_label = os.path.basename(os.path.dirname(lm_path))


def load_keys(r):
    """Truth and salad key construction, mirroring verifier/verify.py exactly."""
    anchors = V.load_anchors(SEED)
    truth = V.load_truth(SEED)
    v1t, v2t, w2t = {}, {}, {}
    for g in r.groups:
        if g in anchors:
            v1t[g] = anchors[g]
            v2t[g] = None
        else:
            v1t[g] = truth[g]['primary']
            sec = truth[g].get('secondaries') or []
            v2t[g] = sec[0] if sec else None
            w2t[g] = 0.5 if sec else 0.0
    pilot = json.load(open(os.path.join(
        REBUILD, 'pilot', 'rebuild-pilot-final', 'result.json')))
    bw = pilot['best']
    v1s = {g: bw['assignment'][g]['v1'] for g in r.groups}
    v2s = {g: bw['assignment'][g]['v2'] for g in r.groups}
    return (v1t, v2t, w2t), (v1s, v2s, {})


PARTS = ['S_char', 'S_cov', 'S_single', 'S_word', 'S_potts',
         'S_conc', 'n_poly', 'total']


def table(rows):
    hdr = f'{"decode":>22}' + ''.join(f'{p:>11}' for p in PARTS)
    print(hdr)
    for label, d in rows:
        print(f'{label:>22}' + ''.join(
            f'{d[p]:>11.1f}' for p in PARTS))


def main():
    cfg = json.load(open(os.path.join(REBUILD, 'solver', 'config.json')))
    print(f'[track-a] cfg: word_minlen={cfg["word_minlen"]} '
          f'lambda_poly={cfg["lambda_poly"]} lambda_conc={cfg["lambda_conc"]} '
          f'conc_cap={cfg["conc_cap"]} lambda_word={cfg["lambda_word"]} '
          f'beta0={cfg["beta0"]}', flush=True)
    pairs = V.load_pairs(SEED)
    out = {}
    for tag, lm_path in (('tocqueville', LM_TOCQ), ('diplomatic', LM_DIPLO)):
        r = RescorerReg(pairs, cfg, lm_path)
        (v1t, v2t, w2t), (v1s, v2s, w2s) = load_keys(r)
        pt = r.score(v1t, v2t, w2t, label='TRUTH (planted)')
        ps = r.score(v1s, v2s, w2s, label='SALAD (pilot winner 199939)')
        out[tag] = {'truth': {k: pt[k] for k in PARTS},
                    'salad': {k: ps[k] for k in PARTS}}
        print(f'\n=== [{tag}] lm={r.lm_label} '
              f'phase chi2={r.phase["chi2"]} gate={r.phase["gate"]} ===',
              flush=True)
        table([('truth', pt), ('salad', ps)])
        margin = ps['total'] - pt['total']  # >0 means salad wins
        print(f'[verdict] margin (salad - truth) = {margin:+.1f} nats '
              f'(salad wins)' if margin > 0 else
              f'[verdict] margin (salad - truth) = {margin:+.1f} nats '
              f'(TRUTH wins)', flush=True)
    # sanity: (a) must reproduce the verifier's 2,601-nat margin to <=1 nat
    m_a = out['tocqueville']['salad']['total'] - out['tocqueville']['truth']['total']
    san = abs(m_a - 2601.0) <= 1.0
    print(f'\n[sanity] tocqueville margin={m_a:+.1f} vs verifier 2601.0: '
          f'{"REPRODUCED (<=1 nat)" if san else "MISMATCH -- STOP"}',
          flush=True)
    m_b = out['diplomatic']['salad']['total'] - out['diplomatic']['truth']['total']
    print(f'[diagnostic] diplomatic margin={m_b:+.1f} nats', flush=True)
    if m_b <= -500:
        print('[verdict] H0 SUPPORTED: truth beats salad by >=500 nats under '
              'register-matched reference', flush=True)
    elif m_b >= 500:
        print('[verdict] H1 SUPPORTED: salad still beats truth by >=500 nats '
              'under register-matched reference', flush=True)
    else:
        print('[verdict] INCONCLUSIVE: margin inside (-500,+500); '
              'no pilot anneal without re-registration', flush=True)
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    json.dump(out, open(os.path.join(HERE, 'results', 'rescore.json'), 'w'),
              indent=1)
    print('[track-a] wrote track-a/results/rescore.json')


if __name__ == '__main__':
    main()
