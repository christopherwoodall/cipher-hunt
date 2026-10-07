#!/usr/bin/env python3
"""Build 6 FRESH synthetic control instances (seeds 184201-184206) for the
Round-7 search-family prototype (work order 8).

Same certified design as code/side-homophonic/control/ (CONTROL-DESIGN.md):
Les Mis plaintext, 96 groups, 7 pins, frequency-weighted homophony,
6 polyvalent islets, phase rhythm q_cycle=0.5 (certified), ear noise.
Only the seeds are fresh. Writes to code/crowd7/search/fresh/instances/.

Protocol: the search scripts NEVER read SYNTHETIC-key-*.json (sealed);
scoring happens in score_fresh.py after all solver outputs are in.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
sys.path.insert(0, os.path.join(LANE, 'code', 'side-homophonic', 'control'))

import generator  # noqa: E402  (certified design; seeds only are fresh)

CANDIDATE_SEEDS = [184201, 184202, 184203, 184204, 184206, 184207,
                   184208, 184209, 184210, 184211, 184212]
# Draw in order until 6 land in the certified occurrence-chi2 band [181,320].
# (184205: 329.5 above ceiling; 184206: 172.6 below floor — both rejected,
#  files left in place but NOT part of the scored set.)
OUTD = os.path.join(HERE, 'fresh', 'instances')
generator.OUTD = OUTD  # redirect writes (module-level OUTD is read at call time)

p = dict(generator.PARAMS)
p['seeds'] = list(CANDIDATE_SEEDS)
p['q_cycle'] = 0.5  # certified (CONTROL-DESIGN.md §3); no recalibration
T = 56              # certified inventory knob

tokens = generator.load_lesmis_tokens()
group_labels = generator.real_group_labels()
print('lesmis tokens=%d real groups=%d' % (len(tokens), len(group_labels)),
      flush=True)

summary_path = os.path.join(HERE, 'fresh', 'build_summary.json')
summary = {}
if os.path.exists(summary_path):
    try:
        summary = json.load(open(summary_path)).get('instances', {})
    except Exception:
        summary = {}
lo, hi = p['chi2_band']
FRESH_SEEDS = []
for seed in CANDIDATE_SEEDS:
    if len(FRESH_SEEDS) >= 6:
        break
    ct_path = os.path.join(OUTD, 'SYNTHETIC-ct-%d.pairs.txt' % seed)
    if os.path.exists(ct_path):
        # already built earlier; check the recorded chi2
        prev = summary.get(str(seed), {})
        if prev.get('occurrence_chi2') and 181 <= prev['occurrence_chi2'] <= 320:
            FRESH_SEEDS.append(seed)
            print('seed %d: already built, in-band (chi2=%.1f), accepted'
                  % (seed, prev['occurrence_chi2']), flush=True)
        else:
            print('seed %d: already built, OUT of band, rejected' % seed,
                  flush=True)
        continue
    inst = generator.build_instance(seed, tokens, group_labels, p, T,
                                    verbose=True)
    occ = generator.occurrence_chi2(inst['pclasses'])
    inband = lo <= occ <= hi
    print('seed %d: occurrence_chi2=%.1f in_band[%d,%d]=%s keep=%.3f islets=%d '
          'crib@%d' % (seed, occ, lo, hi, inband, inst['keep_rate'],
                        inst['n_islets'], inst['crib_pair_offset']), flush=True)
    if inband:
        generator.write_instance(inst, p)
        FRESH_SEEDS.append(seed)
    summary[str(seed)] = {
        'occurrence_chi2': round(occ, 1),
        'unsupervised_chi2': round(inst['chi2'], 1),
        'keep_rate': round(inst['keep_rate'], 4),
        'n_islets': inst['n_islets'],
        'crib_pair_offset': inst['crib_pair_offset'],
        'T_eff': inst['T_eff'],
        'in_band': bool(inband),
    }
assert len(FRESH_SEEDS) == 6, 'only %d in-band seeds' % len(FRESH_SEEDS)
print('FRESH_SEEDS =', FRESH_SEEDS, flush=True)
json.dump({'seeds': FRESH_SEEDS, 'q_cycle': 0.5, 'T': T,
           'chi2_band': [lo, hi], 'instances': summary},
          open(os.path.join(HERE, 'fresh', 'build_summary.json'), 'w'), indent=1)
print('wrote %d fresh instances to %s' % (len(summary), OUTD), flush=True)
