#!/usr/bin/env python3
"""SCORER SMITH round 5 — route (b): SHRINK THE SPACE with F33-style constraints.

F33 (lane position): polyvalence is CONDITIONED, not free; 3/25 groups carry
verified conditioning rules; 35.2% token coverage from identified groups.

Operationalized on the round-4 synthetic control:
  b1 HARD-KNOWN: 5 correct hints -> hard pins; 3 islet (v1,v2) readings
     hard-coded (E-step still per-occurrence); inventory top-300 + known cells.
     Tests: does the CURRENT search now reach truth's basin / pass bars?
  b2 CONDITIONED-POLYVALENCE: v2 allowed only where a conditioning rule verifies
     on data (pre/suc-group chi-square). The control's islets are unconditioned
     coins -> honest expectation is REJECTION (documents the control-vs-F33 gap).
  b3 INVENTORY: coverage of truth primaries in top-300; one 7-pin-only anneal on
     the small inventory (is smaller inventory alone enough?).
"""
import collections, json, math, os, random, sys, time

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
sys.path.insert(0, os.path.join(LANE, 'code'))
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd2'))
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd4'))
from scorer_smith import build_models  # noqa: E402
from joint_engine import (build_letter_ngram, build_inventory, JointModel,
                          PINS)  # noqa: E402

OUTD = os.path.join(LANE, 'code', 'crowd5')
os.makedirs(OUTD, exist_ok=True)
OUTJ = os.path.join(OUTD, 'scorer_identifiability.json')
SPAN = (40000, 41100)
SEED = 1841

def log(*a):
    print('[r5b]', *a, flush=True)

def load_results():
    return json.load(open(OUTJ))

def save_results(R):
    R['meta']['updated'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    json.dump(R, open(OUTJ, 'w'), indent=1, ensure_ascii=False)

log('loading control + models...')
GT = json.load(open(os.path.join(LANE, 'code', 'crowd4', 'control_ground_truth.json')))
GS = GT['stream']; EMITTED = GT['emitted']; GI = GT['group_info']
HINTS = GT['hints']; ISLETS = GT['islets']
M = build_models()
LP, _ = build_letter_ngram(M, n=7, exclude=SPAN)
CELLS, WEIGHTS = build_inventory(M)
CSET = set(CELLS)
BLOCK = {g: v['phase'] for g, v in GI.items()}
R = load_results()
if 'route_b' not in R['stages']:
    R['stages']['route_b'] = {}

# bar groups (same definition as part a)
sfreq = collections.Counter(GS)
cands = [(g, n) for g, n in sfreq.most_common()
         if g not in PINS and GI[g]['primary'] in CSET][:20]

# ---- small inventory: top-300 corpus cells + all known cells ----
known_cells = set(PINS.values()) | set(HINTS.values())
for g, t in ISLETS.items():
    known_cells.add(t['primary']); known_cells.add(t['secondary'])
ranked = sorted(zip(CELLS, WEIGHTS), key=lambda x: -x[1])
small = []
seen = set()
for c, w in ranked:
    if len(small) >= 300: break
    if c not in seen:
        seen.add(c); small.append((c, w))
for c in known_cells:
    if c not in seen:
        seen.add(c); small.append((c, 1))
SCELLS = [c for c, _ in small]; SWEIGHTS = [w for _, w in small]
log('small inventory=%d (top-300 + %d known)' % (len(SCELLS), len(known_cells)))
cov = sum(1 for g, n in cands if GI[g]['primary'] in set(SCELLS))
R['stages']['route_b']['inventory_coverage'] = {
    'small_inventory': len(SCELLS), 'full_inventory': len(CELLS),
    'bar_group_primaries_in_small': '%d/20' % cov}
log('bar-group truth primaries in small inventory: %d/20' % cov)

class ConstrainedModel(JointModel):
    """JointModel with islet (v1,v2) hard-coded and extra hard pins."""
    def __init__(self, *a, islets=None, **k):
        super().__init__(*a, **k)
        self.islet_groups = dict(islets or {})
        # islet groups never move: drop from nonpin
        self.nonpin = [g for g in self.nonpin if g not in self.islet_groups]
    def init_key(self):
        super().init_key()
        for g, (p, s, w) in self.islet_groups.items():
            self.v1[g] = p; self.v2[g] = s; self.w2[g] = w
        for g in self.islet_groups:
            self._rescore_group(g)
        self._refresh_scores()

def eval_bars(m, tag):
    marg = m.marginals(sweeps=150, T=0.3, seed=SEED+5)
    hits = 0; det = []
    for g, n in cands:
        top1 = marg[g][0][0] if marg[g] else None
        ok = (top1 == GI[g]['primary']); hits += ok
        det.append({'g': g, 'true': GI[g]['primary'], 'top1': top1, 'hit': ok,
                    'kind': GI[g]['kind']})
    isl = 0; isld = []
    for g, t in ISLETS.items():
        top3 = [v for v, _ in marg[g][:3]]
        ok = bool(t['primary'] in top3 and t['secondary'] in top3
                  and marg[g] and marg[g][0][0] == t['primary'])
        isl += ok
        isld.append({'g': g, 'pass': ok,
                     'top5': [(v, round(p, 3)) for v, p in marg[g][:5]]})
    agree = sum(1 for a, b in zip(m.pcell, EMITTED) if a == b)/len(GS)
    return {'primary_top1': round(hits/len(cands), 3), 'islets': isl,
            'decode_agreement': round(agree, 3), 'detail': det,
            'islet_detail': isld}

# ---------------------------------------------------------------- b1: hard-known
log('b1: HARD-KNOWN — hints as pins, islet (v1,v2) fixed, small inventory...')
PINS2 = dict(PINS); PINS2.update(HINTS)  # 12 hard pins (all correct)
islet_fix = {g: (t['primary'], t['secondary'], t['w2']) for g, t in ISLETS.items()}
b1 = []
b1_saved = R['stages']['route_b'].get('b1_hard_known', {}).get('restarts', [])
if b1_saved:
    log('  resuming: %d b1 restarts already saved, skipping anneal' % len(b1_saved))
    b1 = b1_saved
else:
    for rs in range(3):
        m = ConstrainedModel(GS, BLOCK, LP, PINS2, {}, SCELLS, SWEIGHTS,
                             0.0, 10.0, 0.0, islets=islet_fix,
                             rng=random.Random(SEED+700+rs))
        res = m.anneal(sweeps=600, T0=2.0, T1=0.02, seed=SEED+700+rs)
        ev = eval_bars(m, 'b1')
        row = {'restart': rs, 'best': round(res['best'], 2),
               'primary_top1': ev['primary_top1'], 'islets': ev['islets'],
               'decode_agreement': ev['decode_agreement']}
        b1.append(row)
        log('  restart %d: best=%.2f top1=%.3f islets=%d/3 decode_agree=%.3f'
            % (rs, res['best'], ev['primary_top1'], ev['islets'], ev['decode_agreement']))
    R['stages']['route_b']['b1_hard_known'] = {
        'pins': len(PINS2), 'islets_fixed': sorted(islet_fix),
        'inventory': len(SCELLS), 'restarts': b1}
    save_results(R)

# b1 ceiling: fully-known key score (everything the constraints allow)
m = ConstrainedModel(GS, BLOCK, LP, PINS2, {}, SCELLS, SWEIGHTS,
                     0.0, 10.0, 0.0, islets=islet_fix, rng=random.Random(1))
m.init_key()
for g in m.groups:
    m.v1[g] = GI[g]['primary']
m.pcell = list(EMITTED); m._refresh_scores()
R['stages']['route_b']['b1_truth_ceiling'] = {
    'total': round(m.total(), 2),
    's_let': round(sum(m.lscore)/max(m.total_letters, 1), 4)}
save_results(R)
log('b1 truth ceiling (all v1 known, islets fixed): total=%.2f' % m.total())

# ---------------------------------------------------------------- b2: conditioned polyvalence
log('b2: CONDITIONED-POLYVALENCE — verify pre/suc conditioning for v2...')
# force-add v2 to candidate groups, E-step, then test conditioning of the choice
m = JointModel(GS, BLOCK, LP, PINS, HINTS, CELLS, WEIGHTS, 0.0, 0.0, 0.0,
               rng=random.Random(SEED))
m.init_key()
# put truth v1 on all groups so the E-step test is about v2 choice, not v1 error
for g in m.groups:
    m.v1[g] = GI[g]['primary']
m._recompute_all(); m._refresh_scores()
test_groups = [g for g, n in cands[:12]] + sorted(ISLETS)
b2rows = []
for g in test_groups:
    # candidate secondary: best local alternative cell
    occ = m.occ[g]
    cands2 = [c for c in random.Random(hash(g) % 9999).sample(CELLS, 40)]
    best_c, best_s = None, float('-inf')
    for c in cands2:
        if c == m.v1[g]: continue
        s = sum(m.F(m.pcell[t-1] if t > 0 else '^', c) for t in occ)
        if s > best_s: best_c, best_s = c, s
    m.v2[g] = best_c; m.w2[g] = 0.5
    m._rescore_group(g)
    choice = [1 if m.pcell[t] == best_c else 0 for t in occ]
    n2 = sum(choice)
    # conditioning test: pre-group identity x choice (top-4 preds + rest)
    preds = collections.Counter(GS[t-1] if t > 0 else '##' for t in occ)
    top_preds = [p for p, _ in preds.most_common(4)]
    # chi-square on 2x5 table (choice x pre-bucket)
    table = [[0]*5 for _ in range(2)]
    for t, ch in zip(occ, choice):
        p = GS[t-1] if t > 0 else '##'
        j = top_preds.index(p) if p in top_preds else 4
        table[ch][j] += 1
    chi2 = 0.0
    rs_ = [sum(r) for r in table]; cs_ = [sum(table[i][j] for i in range(2)) for j in range(5)]
    T_ = sum(rs_)
    for i in range(2):
        for j in range(5):
            e = rs_[i]*cs_[j]/T_ if T_ else 0
            if e > 0: chi2 += (table[i][j]-e)**2/e
    # chi2 df=4; p<0.01 threshold = 13.28
    verified = bool(chi2 > 13.28 and n2 >= 3 and n2 <= len(occ)-3)
    b2rows.append({'group': g, 'v2_candidate': best_c, 'n_v2_chosen': n2,
                   'n_occ': len(occ), 'pre_chi2': round(chi2, 2),
                   'conditioning_verified': verified,
                   'is_true_islet': g in ISLETS})
    m.v2[g] = None; m.w2[g] = 0.0
    m._rescore_group(g)
n_ver = sum(1 for r in b2rows if r['conditioning_verified'])
n_isl_ver = sum(1 for r in b2rows if r['is_true_islet'] and r['conditioning_verified'])
R['stages']['route_b']['b2_conditioned_polyvalence'] = {
    'groups_tested': len(b2rows),
    'verified': n_ver, 'true_islets_verified': n_isl_ver,
    'rows': b2rows,
    'interpretation': 'F33 requires polyvalence to be CONDITIONED. The control plants '
                      'unconditioned islet coins; expectation is rejection.'}
save_results(R)
log('b2: %d/%d groups verify conditioning; true islets verified: %d/3'
    % (n_ver, len(b2rows), n_isl_ver))

# ---------------------------------------------------------------- b3: small inventory, 7 pins only
log('b3: small inventory + 7 pins only (is smaller inventory alone enough?)...')
b3 = []
for rs in range(2):
    m = JointModel(GS, BLOCK, LP, PINS, HINTS, SCELLS, SWEIGHTS,
                   0.0, 10.0, 0.0, rng=random.Random(SEED+800+rs))
    res = m.anneal(sweeps=600, T0=2.0, T1=0.02, seed=SEED+800+rs)
    ev = eval_bars(m, 'b3')
    b3.append({'restart': rs, 'best': round(res['best'], 2),
               'primary_top1': ev['primary_top1'], 'islets': ev['islets']})
    log('  restart %d: best=%.2f top1=%.3f islets=%d/3' % (rs, res['best'], ev['primary_top1'], ev['islets']))
R['stages']['route_b']['b3_small_inventory_only'] = {'restarts': b3}
save_results(R)
log('route (b) complete.')
