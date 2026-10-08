#!/usr/bin/env python3
"""Build rung-C (pairwise forced-choice) packages, schedules, and sealed key.

- 6 truth x 6 salad = 36 binding pairs; 6 truth_i-vs-paraphrase_i diagnostic bouts.
- 84 fresh 8-hex blind labels, zero hits vs all 54 previously used blind labels
  (pilot 18 + v3A 18 + v3B 18). Does NOT check against candidates.json eternal IDs
  (old_label fields) — those are not blind labels.
- Packages: rungC-pkg-{1,2,3}.json ; schedules: rungC-schedules.json ;
  key: _KEY_V3C_DO_NOT_OPEN.json (sealed until all 126 calls logged).
"""
import json, os, random, secrets, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
V3C = os.path.join(HERE, 'instrument-acceptance-v3c')
PROMPT_SHA = 'd907c59202c9d38e5dfe10bf8048c869bcba2fb547631c02ceb34f93b5b2615e'

# --- assert prompt pin ---
h = hashlib.sha256(open(os.path.join(HERE, 'prompt-v3C.txt'), 'rb').read()).hexdigest()
assert h == PROMPT_SHA, f'PROMPT CHANGED: {h}'

# --- class the 18 candidates from the pilot key's expected_median ---
pk = json.load(open(os.path.join(HERE, 'instrument-acceptance', '_KEY_DO_NOT_OPEN.json')))
old_to_class = {}
for new, v in pk.items():
    m = v['expected_median']
    old_to_class[v['old_label']] = 'salad' if m <= 30 else ('truth' if m <= 75 else 'paraphrase')
cands = json.load(open(os.path.join(HERE, 'candidates.json')))['candidates']
truth = sorted(l for l, c in old_to_class.items() if c == 'truth')
salad = sorted(l for l, c in old_to_class.items() if c == 'salad')
para  = sorted(l for l, c in old_to_class.items() if c == 'paraphrase')
assert len(truth) == 6 and len(salad) == 6 and len(para) == 6, (len(truth), len(salad), len(para))
texts = {l: cands[l]['text'] for l in truth + salad + para}

# --- all previously used blind labels (must avoid) ---
old_blind = set()
for rel in ['instrument-acceptance/_KEY_DO_NOT_OPEN.json',
            'instrument-acceptance-v3a/_KEY_V3A_DO_NOT_OPEN.json',
            'instrument-acceptance-v3b/_KEY_V3B_DO_NOT_OPEN.json']:
    k = json.load(open(os.path.join(HERE, rel)))
    old_blind |= set(k.keys())
print('previously used blind labels:', len(old_blind))
assert len(old_blind) == 54, len(old_blind)

# --- 84 fresh labels ---
fresh = set()
while len(fresh) < 84:
    lab = secrets.token_hex(4)
    if lab not in old_blind and lab not in fresh:
        fresh.add(lab)
fresh = list(fresh)
assert len(set(fresh) & old_blind) == 0

# --- pairs: 36 binding (truth_i x salad_j), 6 diagnostic (truth_i vs para_i) ---
pairs = []
key = {}
li = 0
def take_pair(pid, a_old, b_old, bout):
    global li
    la, lb = fresh[li], fresh[li + 1]; li += 2
    pairs.append({'pair_id': pid, 'label_a': la, 'label_b': lb, 'bout': bout})
    for lab, old, cls in ((la, a_old, old_to_class[a_old]), (lb, b_old, old_to_class[b_old])):
        key[lab] = {'old_label': old, 'class': cls, 'pair_id': pid, 'bout': bout}

pi = 0
for i, t in enumerate(truth):
    for j, s in enumerate(salad):
        pi += 1
        take_pair(f'P{pi:02d}', t, s, 'binding')
assert pi == 36
for i in range(6):
    take_pair(f'D{i+1:02d}', truth[i], para[i], 'diagnostic')

# --- assignment: 12 binding + 2 diagnostic per judge ---
binding = [p for p in pairs if p['bout'] == 'binding']
diag = [p for p in pairs if p['bout'] == 'diagnostic']
assign = {1: binding[0:12] + diag[0:2], 2: binding[12:24] + diag[2:4], 3: binding[24:36] + diag[4:6]}
assert all(len(v) == 14 for v in assign.values())

# --- schedules: per judge, 3 passes; fresh order per pass; position randomized ---
# per-pair: across 3 passes each label appears first at least once
rng = random.Random(20261007)
schedules = {}
for j, plist in assign.items():
    passes = []
    for pno in (1, 2, 3):
        order = list(range(len(plist))); rng.shuffle(order)
        seq = []
        for pos, idx in enumerate(order):
            pr = plist[idx]
            # alternate presented-first across passes so each label is first >=1 time
            first = pr['label_a'] if (pno + idx) % 2 == 0 else pr['label_b']
            seq.append({'pair_id': pr['pair_id'], 'presented_first': first})
        passes.append(seq)
    schedules[str(j)] = passes

# --- packages (contain texts; key stays sealed) ---
for j, plist in assign.items():
    pkg = {'judge': j, 'prompt_sha256': PROMPT_SHA,
           'pairs': [{'pair_id': p['pair_id'], 'bout': p['bout'],
                      'label_a': p['label_a'], 'text_a': texts[key[p['label_a']]['old_label']],
                      'label_b': p['label_b'], 'text_b': texts[key[p['label_b']]['old_label']]}
                     for p in plist]}
    json.dump(pkg, open(os.path.join(V3C, f'rungC-pkg-{j}.json'), 'w'))
json.dump(schedules, open(os.path.join(V3C, 'rungC-schedules.json'), 'w'), indent=1)
json.dump(key, open(os.path.join(V3C, '_KEY_V3C_DO_NOT_OPEN.json'), 'w'))
print('pairs:', len(pairs), 'binding:', len(binding), 'diagnostic:', len(diag))
print('labels generated:', len(fresh), '| key entries:', len(key))
# sanity: within each judge, no label repeats
for j, plist in assign.items():
    labs = [p['label_a'] for p in plist] + [p['label_b'] for p in plist]
    assert len(set(labs)) == 28, j
# sanity: position randomization — each label first >=1 time per pair across passes
for j, passes in schedules.items():
    plist = assign[int(j)]
    byid = {p['pair_id']: (p['label_a'], p['label_b']) for p in plist}
    for pno_passes in [passes]:
        firsts = {}
        for seq in pno_passes:
            for e in seq:
                firsts.setdefault(e['pair_id'], set()).add(e['presented_first'])
        for pid, (la, lb) in byid.items():
            assert firsts[pid] == {la, lb}, (j, pid, firsts[pid])
print('sanity checks PASS')
