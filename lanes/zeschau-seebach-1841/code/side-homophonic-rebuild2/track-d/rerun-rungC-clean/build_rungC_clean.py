#!/usr/bin/env python3
"""Clean re-run of rung-C package build (isolated: rerun-rungC-clean/).

- 6 truth x 6 salad = 36 binding pairs; 6 diagnostic bouts truth_i vs paraphrase_i BY SEED.
- 84 fresh 8-hex blind labels, zero hits vs all 138 previously used blind labels
  (pilot 18 + v3A 18 + v3B 18 + voided-v3C 84, from void-v3c-labels-collected.json).
- Prompt pin: sha256 d907c592... (v3C), asserted before anything.
- Schedules: 3 passes per pair, per-pass order + position randomized, fresh RNG
  (seed 20261008, logged); each label presented-first at least once per pair.
- Packages -> rungC-clean-pkg-{1,2,3}.json ; schedules -> rungC-clean-schedules.json ;
  key -> _KEY_V3C_CLEAN_DO_NOT_OPEN.json (sealed; label -> eternal_id, class, seed).
"""
import json, os, random, secrets, hashlib, re

HERE = os.path.dirname(os.path.abspath(__file__))
TRACKD = os.path.dirname(HERE)
PROMPT_SHA = 'd907c59202c9d38e5dfe10bf8048c869bcba2fb547631c02ceb34f93b5b2615e'
RNG_SEED = 20261008
LOG = open(os.path.join(HERE, 'build.log'), 'a')
def say(m):
    LOG.write(m + '\n'); print(m)

# --- assert prompt pin ---
h = hashlib.sha256(open(os.path.join(TRACKD, 'prompt-v3C.txt'), 'rb').read()).hexdigest()
assert h == PROMPT_SHA, f'PROMPT CHANGED: {h}'
say(f'prompt-v3C.txt sha256 OK: {h}')

# --- class the 18 candidates from the pilot key's expected_median (as build_rungC.py) ---
pk = json.load(open(os.path.join(TRACKD, 'instrument-acceptance', '_KEY_DO_NOT_OPEN.json')))
old_to_class = {}
for new, v in pk.items():
    m = v['expected_median']
    old_to_class[v['old_label']] = 'salad' if m <= 30 else ('truth' if m <= 75 else 'paraphrase')
cands = json.load(open(os.path.join(TRACKD, 'candidates.json')))['candidates']
lmap = json.load(open(os.path.join(TRACKD, 'label_map.json')))
# cross-check class against label_map (seed carrier)
for lab, cls in old_to_class.items():
    assert lmap[lab]['class'] == cls, (lab, cls, lmap[lab]['class'])
say('class derivation matches label_map for all 18 eternal IDs')
truth = sorted(l for l, c in old_to_class.items() if c == 'truth')
salad = sorted(l for l, c in old_to_class.items() if c == 'salad')
para = sorted(l for l, c in old_to_class.items() if c == 'paraphrase')
assert len(truth) == 6 and len(salad) == 6 and len(para) == 6
seed_of = {lab: lmap[lab]['seed'] for lab in truth + salad + para}
truth_by_seed = {seed_of[l]: l for l in truth}
para_by_seed = {seed_of[l]: l for l in para}
assert sorted(truth_by_seed) == sorted(para_by_seed) == [f'18410{i}' for i in range(1, 7)]
texts = {l: cands[l]['text'] for l in truth + salad + para}
say(f'candidates: truth={len(truth)} salad={len(salad)} paraphrase={len(para)}')

# --- all previously used blind labels (must avoid) ---
old_blind = set()
for rel in ['instrument-acceptance/_KEY_DO_NOT_OPEN.json',
            'instrument-acceptance-v3a/_KEY_V3A_DO_NOT_OPEN.json',
            'instrument-acceptance-v3b/_KEY_V3B_DO_NOT_OPEN.json']:
    old_blind |= set(json.load(open(os.path.join(TRACKD, rel))).keys())
old_blind |= set(json.load(open(os.path.join(HERE, 'void-v3c-labels-collected.json'))))
say(f'previously used blind labels: {len(old_blind)}')
assert len(old_blind) == 138, len(old_blind)

# --- 84 fresh labels ---
fresh = set()
while len(fresh) < 84:
    lab = secrets.token_hex(4)
    if lab not in old_blind and lab not in fresh:
        fresh.add(lab)
fresh = list(fresh)
assert len(set(fresh) & old_blind) == 0
say(f'fresh labels generated: {len(fresh)}, zero overlap with the 138')

# --- pairs ---
pairs = []
key = {}
li = 0
def take_pair(pid, a_old, b_old, bout):
    global li
    la, lb = fresh[li], fresh[li + 1]; li += 2
    pairs.append({'pair_id': pid, 'label_a': la, 'label_b': lb, 'bout': bout})
    for lab, old in ((la, a_old), (lb, b_old)):
        key[lab] = {'eternal_id': old, 'class': old_to_class[old],
                    'seed': seed_of[old], 'pair_id': pid, 'bout': bout}

pi = 0
for i, t in enumerate(truth):
    for j, s in enumerate(salad):
        pi += 1
        take_pair(f'P{pi:02d}', t, s, 'binding')
assert pi == 36
for i, seed in enumerate([f'18410{k}' for k in range(1, 7)]):
    take_pair(f'D{i+1:02d}', truth_by_seed[seed], para_by_seed[seed], 'diagnostic')
say(f'pairs: {len(pairs)} binding={sum(1 for p in pairs if p["bout"]=="binding")} '
    f'diagnostic={sum(1 for p in pairs if p["bout"]=="diagnostic")}')
say('diagnostic bouts paired BY SEED: ' +
    ', '.join(f'D{i+1}={s}' for i, s in enumerate([f'18410{k}' for k in range(1,7)])))

# --- assignment: 12 binding + 2 diagnostic per judge ---
binding = [p for p in pairs if p['bout'] == 'binding']
diag = [p for p in pairs if p['bout'] == 'diagnostic']
assign = {1: binding[0:12] + diag[0:2], 2: binding[12:24] + diag[2:4], 3: binding[24:36] + diag[4:6]}
assert all(len(v) == 14 for v in assign.values())

# --- schedules ---
rng = random.Random(RNG_SEED)
schedules = {}
for j, plist in assign.items():
    passes = []
    for pno in (1, 2, 3):
        order = list(range(len(plist))); rng.shuffle(order)
        seq = []
        for pos, idx in enumerate(order):
            pr = plist[idx]
            first = pr['label_a'] if (pno + idx) % 2 == 0 else pr['label_b']
            seq.append({'pair_id': pr['pair_id'], 'presented_first': first})
        passes.append(seq)
    schedules[str(j)] = passes
say(f'schedules: rng seed={RNG_SEED}, 3 passes/judge, position randomized per pass')

# --- write packages ---
for j, plist in assign.items():
    pkg = {'judge': j, 'prompt_sha256': PROMPT_SHA,
           'pairs': [{'pair_id': p['pair_id'], 'bout': p['bout'],
                      'label_a': p['label_a'], 'text_a': texts[key[p['label_a']]['eternal_id']],
                      'label_b': p['label_b'], 'text_b': texts[key[p['label_b']]['eternal_id']]}
                     for p in plist]}
    json.dump(pkg, open(os.path.join(HERE, f'rungC-clean-pkg-{j}.json'), 'w'))
json.dump(schedules, open(os.path.join(HERE, 'rungC-clean-schedules.json'), 'w'), indent=1)
json.dump(key, open(os.path.join(HERE, '_KEY_V3C_CLEAN_DO_NOT_OPEN.json'), 'w'))
say(f'key written: {len(key)} labels (SEALED)')

# --- sanity ---
for j, plist in assign.items():
    labs = [p['label_a'] for p in plist] + [p['label_b'] for p in plist]
    assert len(set(labs)) == 28, j
for j, passes in schedules.items():
    plist = assign[int(j)]
    byid = {p['pair_id']: (p['label_a'], p['label_b']) for p in plist}
    firsts = {}
    for seq in passes:
        for e in seq:
            firsts.setdefault(e['pair_id'], set()).add(e['presented_first'])
    for pid, (la, lb) in byid.items():
        assert firsts[pid] == {la, lb}, (j, pid)
say('sanity checks PASS (28 unique labels/judge; each label first >=1 time per pair)')

# --- tripwire grep on packages BEFORE any judge runs ---
gate = ['184201', '184202', '184203', '184204', '184206', '184207']
r5005 = re.compile(r'(?i)r5005|ct_r5005')
hits = []
for j in (1, 2, 3):
    blob = open(os.path.join(HERE, f'rungC-clean-pkg-{j}.json')).read()
    for g in gate:
        if g in blob: hits.append((j, 'gate-id', g))
    for m in r5005.finditer(blob): hits.append((j, 'r5005', m.group(0)))
blob = open(os.path.join(HERE, 'rungC-clean-schedules.json')).read()
for g in gate:
    if g in blob: hits.append(('sched', 'gate-id', g))
say(f'tripwire PRE-judge: {len(hits)} hits -> {hits}')
assert len(hits) == 0, hits
say('TRIPWIRE PRE-JUDGE CLEAR')
LOG.close()
