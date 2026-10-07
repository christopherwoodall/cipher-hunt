#!/usr/bin/env python3
"""Round-10 59COND battery: full 59 census on the repaired canonical stream."""
import collections, json, os, sys

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd6', 'redteam'))
from verify_baseline import load_stream

pairs = load_stream()
N = len(pairs)
assert N == 1847, N

def ctx(i, w=3):
    lo, hi = max(0, i - w), min(N, i + w + 1)
    return '-'.join('[%02d]' % pairs[j] if j == i else '%02d' % pairs[j]
                    for j in range(lo, hi))

w59 = [i for i, v in enumerate(pairs) if v == 59]
pre = collections.Counter(pairs[i-1] for i in w59)
suc = collections.Counter(pairs[i+1] for i in w59 if i + 1 < N)
pre_suc = collections.Counter((pairs[i-1], pairs[i+1]) for i in w59 if i + 1 < N)

OUT = {
    'n59': len(w59),
    'windows': [{'pos': i,
                 'pre': pairs[i-1] if i > 0 else None,
                 'suc': pairs[i+1] if i + 1 < N else None,
                 'pre2': pairs[i-2] if i > 1 else None,
                 'suc2': pairs[i+2] if i + 2 < N else None,
                 'ctx3': ctx(i)} for i in w59],
    'pre_counts': sorted(pre.items(), key=lambda kv: -kv[1]),
    'suc_counts': sorted(suc.items(), key=lambda kv: -kv[1]),
    'pre_suc_counts': sorted(pre_suc.items(), key=lambda kv: -kv[1]),
    'n64': sum(1 for v in pairs if v == 64),
    'n94': sum(1 for v in pairs if v == 94),
    'n84': sum(1 for v in pairs if v == 84),
}
OUT['p_59_given_64'] = pre.get(64, 0) / OUT['n64']
OUT['p_59_given_94'] = pre.get(94, 0) / OUT['n94']

# byte-identical ±3 7-mer dedup for n_eff
seen = {}
for w in OUT['windows']:
    key = tuple(pairs[max(0,w['pos']-3):w['pos']+4])
    seen.setdefault(key, []).append(w['pos'])
OUT['dup_7mers'] = {str(k): v for k, v in seen.items() if len(v) > 1}

with open(os.path.join(LANE, 'code', 'crowd10', 'conditioner59',
                       'census_results.json'), 'w') as f:
    json.dump(OUT, f, indent=2)

print('n59 =', len(w59))
print('pre:', OUT['pre_counts'])
print('suc:', OUT['suc_counts'])
print('P(59|64)=%.4f  P(59|94)=%.4f' % (OUT['p_59_given_64'], OUT['p_59_given_94']))
print('dup 7-mers:', OUT['dup_7mers'])
for w in OUT['windows']:
    print(w['pos'], 'pre=%02d' % w['pre'], 'suc=%02d' % w['suc'], w['ctx3'])
