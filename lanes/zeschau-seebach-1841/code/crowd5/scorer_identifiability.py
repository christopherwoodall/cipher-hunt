#!/usr/bin/env python3
"""SCORER SMITH round 5 — identifiability attack (lane work order 7).

Two routes on the round-4 synthetic control (code/crowd4/control_ground_truth.json):
  (a) BETTER SEARCH — parallel tempering, smarter proposals, longer runs.
  (b) SHRINK THE SPACE — F33-style hard constraints (known readings, conditioned
      polyvalence, smaller inventory).

Control-first: everything is measured against the sealed synthetic control.
Writes scorer_identifiability.json incrementally (safe to run in background).
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

RESULTS = {'SYNTHETIC': True, 'stages': {}, 'meta': {'seed': SEED, 'span': SPAN}}

def save():
    RESULTS['meta']['updated'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    json.dump(RESULTS, open(OUTJ, 'w'), indent=1, ensure_ascii=False)

def log(*a):
    print('[r5]', *a, flush=True)

# ---------------------------------------------------------------- setup
log('loading control ground truth...')
GT = json.load(open(os.path.join(LANE, 'code', 'crowd4', 'control_ground_truth.json')))
GS = GT['stream']; EMITTED = GT['emitted']; GI = GT['group_info']
HINTS = GT['hints']; ISLETS = GT['islets']
log('stream=%d groups=%d islets=%s' % (len(GS), len(set(GS)), sorted(ISLETS)))
log('building era models (span excluded)...')
M = build_models()
LP, _ = build_letter_ngram(M, n=7, exclude=SPAN)
CELLS, WEIGHTS = build_inventory(M)
CSET = set(CELLS)
BLOCK = {g: v['phase'] for g, v in GI.items()}
log('inventory=%d cells' % len(CELLS))

def make_model(lam_rot=0.0, lam_poly=10.0, lam_hom=0.0, pins=PINS, prov=HINTS,
               cells=CELLS, weights=WEIGHTS, seed=SEED):
    return JointModel(GS, BLOCK, LP, pins, prov, cells, weights,
                      lam_rot, lam_poly, lam_hom, rng=random.Random(seed))

def truth_key(m, with_poly=True):
    for g in m.groups:
        m.v1[g] = GI[g]['primary']
        if with_poly and GI[g]['secondary']:
            m.v2[g] = GI[g]['secondary']; m.w2[g] = GI[g]['w2']
        else:
            m.v2[g] = None; m.w2[g] = 0.0
    m.pcell = list(EMITTED); m._refresh_scores()
    return m

def components(m):
    return {'total': round(m.total(), 3),
            's_let': round(sum(m.lscore)/max(m.total_letters, 1), 4),
            's_pos': round(sum(m.lscore)/len(GS), 4),
            'S_prior': round(m.S_prior, 2), 'n_poly': m.n_poly,
            'S_hom': round(m.S_hom, 2)}

# ---------------------------------------------------------------- stage 1: model-correct check
log('stage 1: model-correct check (truth vs annealed, decomposed)...')
m = make_model(); truth_key(m, with_poly=True)
t_full = components(m)
m0 = make_model(lam_poly=0.0); truth_key(m0, with_poly=True)
t_nopoly = components(m0)
m1 = make_model(lam_poly=0.0); truth_key(m1, with_poly=False)
m1.pcell = [m1.v1[g] for g in GS]; m1._refresh_scores()  # monovalent decode of truth primaries
t_mono = components(m1)
RESULTS['stages']['model_correct'] = {'truth_lam10': t_full, 'truth_lam0': t_nopoly,
                                      'truth_monovalent_decode': t_mono}
save(); log('truth components:', t_full)

# ---------------------------------------------------------------- stage 2: identifiability analysis
log('stage 2: identifiability analysis (emitted distribution vs truth primary)...')
sfreq = collections.Counter(GS)
cands = [(g, n) for g, n in sfreq.most_common()
         if g not in PINS and GI[g]['primary'] in CSET][:20]
rows = []
for g, n in cands:
    dist = collections.Counter(e for gg, e in zip(GS, EMITTED) if gg == g)
    tot = sum(dist.values())
    p_primary = dist.get(GI[g]['primary'], 0)/tot
    modal, modal_n = dist.most_common(1)[0]
    ent = -sum((c/tot)*math.log(c/tot) for c in dist.values())
    rows.append({'group': g, 'n': n, 'kind': GI[g]['kind'],
                 'true_primary': GI[g]['primary'],
                 'p_emitted_is_primary': round(p_primary, 3),
                 'modal_emitted': modal, 'p_modal': round(modal_n/tot, 3),
                 'primary_is_modal': modal == GI[g]['primary'],
                 'n_distinct_emitted': len(dist), 'entropy': round(ent, 2)})
n_unident = sum(1 for r in rows if not r['primary_is_modal'])
RESULTS['stages']['identifiability'] = {
    'bar_groups': rows,
    'n_primary_not_modal': n_unident,
    'max_achievable_top1': round((20-n_unident)/20, 3),
    'note': 'groups whose truth primary is not the modal emitted cell cannot be '
            'recovered by ANY likelihood-based top-1 (the modal cell always wins).'}
save()
log('primary!=modal for %d/20 bar groups -> max achievable top-1 = %.2f'
    % (n_unident, (20-n_unident)/20))

# ---------------------------------------------------------------- contact graph (for pool proposals)
log('building contact graph...')
foll = collections.defaultdict(collections.Counter)
pred = collections.defaultdict(collections.Counter)
for a, b in zip(GS, GS[1:]):
    foll[a][b] += 1; pred[b][a] += 1
TOPC = {g: (set(h for h, _ in foll[g].most_common(10)) |
            set(h for h, _ in pred[g].most_common(10))) for g in set(GS)}
def neighbors(g, k=8):
    sg = TOPC[g]
    sims = []
    for h in TOPC:
        if h == g: continue
        u = sg | TOPC[h]
        j = len(sg & TOPC[h])/len(u) if u else 0.0
        sims.append((j, h))
    sims.sort(reverse=True)
    return [h for _, h in sims[:k]]
NBR = {g: neighbors(g) for g in set(GS)}
RESULTS['meta']['contact_graph'] = 'jaccard-top10, k=8 neighbors'

class SmartModel(JointModel):
    """JointModel + pool-copy and Gibbs-conditional proposals."""
    def __init__(self, *a, gibbs_p=0.10, pool_p=0.10, **k):
        super().__init__(*a, **k)
        self.gibbs_p = gibbs_p; self.pool_p = pool_p
        self._nbr = NBR
    def _local(self, g, c):
        # local fit of candidate cell c in g's contexts (ignores v2/phase)
        s = 0.0
        for t in self.occ[g]:
            ca = self.pcell[t-1] if t > 0 else '^'
            s += self.F(ca, c)
            if t+1 < self.N:
                s += self.F(c, self.pcell[t+1])
        return s
    def propose_move(self, g, rng=None):
        rng = rng or self.rng
        r = rng.random()
        if r < self.pool_p:
            # copy v1 from a contact-similar group (homophone-pool proposal)
            cands = [h for h in self._nbr[g] if h in self.nonpin]
            if not cands: return 'noop', {g}, None
            h = rng.choice(cands); new = self.v1[h]
            if new == self.v1[g]: return 'noop', {g}, None
            snap = self.snapshot({g})
            self._move_v1(g, new)
            self._rescore_group(g)
            return 'pool', {g}, snap
        if r < self.pool_p + self.gibbs_p:
            # Gibbs-conditional: sample cell proportional to local context fit
            short = set()
            while len(short) < 16:
                short.add(self.sample_cell())
            while len(short) < 24:
                short.add(rng.choice(self.cells))
            short.add(self.v1[g]); short.discard(self.v2[g])
            short = list(short)
            T = 1.0
            ws = [math.exp(self._local(g, c)/T) for c in short]
            tot = sum(ws); x = rng.random()*tot; acc = 0.0; new = short[-1]
            for c, w in zip(short, ws):
                acc += w
                if acc >= x: new = c; break
            if new == self.v1[g]: return 'noop', {g}, None
            snap = self.snapshot({g})
            self._move_v1(g, new)
            self._rescore_group(g)
            return 'gibbs', {g}, snap
        return super().propose_move(g, rng)

def marginal_top1(m):
    marg = m.marginals(sweeps=150, T=0.3, seed=SEED+5)
    hits = 0; det = []
    for g, n in cands:
        top1 = marg[g][0][0] if marg[g] else None
        ok = (top1 == GI[g]['primary']); hits += ok
        det.append({'g': g, 'true': GI[g]['primary'], 'top1': top1, 'hit': ok})
    return hits/len(cands), det, marg

def islet_check(marg):
    s = 0; det = []
    for g, t in ISLETS.items():
        top3 = [v for v, _ in marg[g][:3]]
        ok = bool(t['primary'] in top3 and t['secondary'] in top3
                  and marg[g] and marg[g][0][0] == t['primary'])
        s += ok
        det.append({'g': g, 'pass': ok, 'top5': [(v, round(p,3)) for v, p in marg[g][:5]]})
    return s, det

# ---------------------------------------------------------------- stage 3a: baseline (longer runs, current search)
log('stage 3a: BASELINE — current engine, 3 restarts x 600 sweeps...')
base = []
for rs in range(3):
    m = make_model(seed=SEED+rs)
    res = m.anneal(sweeps=600, T0=2.0, T1=0.02, seed=SEED+100+rs)
    acc, det, marg = marginal_top1(m)
    isl, isld = islet_check(marg)
    base.append({'restart': rs, 'best': round(res['best'], 2),
                 'acc_rate': round(res['acc_rate'], 3),
                 'components': components(m),
                 'primary_top1': round(acc, 3), 'islets': isl})
    log('  restart %d: best=%.2f top1=%.3f islets=%d/3' % (rs, res['best'], acc, isl))
    RESULTS['stages']['route_a_baseline'] = base; save()

# ---------------------------------------------------------------- stage 3b: parallel tempering
log('stage 3b: PARALLEL TEMPERING — 6 chains x 600 sweeps, swaps every 10...')
K = 6
temps = [2.0 * (0.02/2.0)**(i/(K-1)) for i in range(K)]
chains = [make_model(seed=SEED+1000+i) for i in range(K)]
for ch in chains:
    ch.init_key()
E = [ch.total() for ch in chains]
best_s, best_state = max(E), None
gbest = float('-inf'); gbest_m = None
t_pt = time.time()
for cyc in range(60):  # 60 cycles x 10 sweeps = 600 sweeps/chain
    for i, ch in enumerate(chains):
        T = temps[i]
        order_rng = random.Random(SEED+5000+cyc*K+i)
        for sw in range(10):
            order = ch.nonpin[:]; order_rng.shuffle(order)
            for g in order:
                mv, touched, snap = ch.propose_move(g, order_rng)
                if mv == 'noop': continue
                new = ch.total(); d = new - E[i]
                if d >= 0 or order_rng.random() < math.exp(d/T):
                    E[i] = new
                else:
                    ch.revert(snap)
        if E[i] > gbest:
            gbest = E[i]
            gbest_m = (dict(ch.v1), dict(ch.v2), dict(ch.w2), list(ch.pcell),
                       components(ch))
    # adjacent swaps
    for i in range(K-1):
        dE = E[i] - E[i+1]
        if dE*(1/temps[i] - 1/temps[i+1]) >= 0 or \
           random.Random(SEED+9000+cyc*K+i).random() < math.exp(dE*(1/temps[i]-1/temps[i+1])):
            chains[i].v1, chains[i+1].v1 = chains[i+1].v1, chains[i].v1
            chains[i].v2, chains[i+1].v2 = chains[i+1].v2, chains[i].v2
            chains[i].w2, chains[i+1].w2 = chains[i+1].w2, chains[i].w2
            chains[i].pcell, chains[i+1].pcell = chains[i+1].pcell, chains[i].pcell
            chains[i]._refresh_scores(); chains[i+1]._refresh_scores()
            E[i], E[i+1] = chains[i].total(), chains[i+1].total()
    if (cyc+1) % 20 == 0:
        log('  PT cycle %d/60 gbest=%.2f elapsed=%.0fs' % (cyc+1, gbest, time.time()-t_pt))
# restore global best into chain 0 for marginals
v1b, v2b, w2b, pcb, compb = gbest_m
chains[0].v1, chains[0].v2, chains[0].w2 = v1b, v2b, w2b
chains[0].pcell = pcb; chains[0]._refresh_scores()
acc, det, marg = marginal_top1(chains[0])
isl, isld = islet_check(marg)
RESULTS['stages']['route_a_PT'] = {'chains': K, 'sweeps_per_chain': 600,
    'temps': [round(t,3) for t in temps], 'gbest': round(gbest,2),
    'components': compb, 'primary_top1': round(acc,3), 'islets': isl,
    'elapsed_s': round(time.time()-t_pt,1)}
save(); log('PT done: gbest=%.2f top1=%.3f islets=%d/3' % (gbest, acc, isl))

# ---------------------------------------------------------------- stage 3c: smarter proposals
log('stage 3c: SMARTER PROPOSALS (pool+gibbs), 3 restarts x 600 sweeps...')
smart = []
for rs in range(3):
    m = SmartModel(GS, BLOCK, LP, PINS, HINTS, CELLS, WEIGHTS, 0.0, 10.0, 0.0,
                   rng=random.Random(SEED+200+rs))
    res = m.anneal(sweeps=600, T0=2.0, T1=0.02, seed=SEED+200+rs)
    acc, det, marg = marginal_top1(m)
    isl, isld = islet_check(marg)
    smart.append({'restart': rs, 'best': round(res['best'],2),
                  'components': components(m),
                  'primary_top1': round(acc,3), 'islets': isl})
    log('  restart %d: best=%.2f top1=%.3f islets=%d/3' % (rs, res['best'], acc, isl))
    RESULTS['stages']['route_a_smart'] = smart; save()

# ---------------------------------------------------------------- stage 3d: basin test
log('stage 3d: BASIN TEST — perturb truth, low-T descent (no re-init), measure recovery...')
def descend(m, sweeps, T0, T1, seed):
    """Greedy-ish low-T descent from the CURRENT key (no init_key reset)."""
    rng = random.Random(seed)
    m._recompute_all()
    for g in m.nonpin:
        if m.v2[g] is not None:
            m._rescore_group(g)
    m._refresh_scores()
    cur = m.total(); best = cur
    cool = (T1/T0)**(1.0/sweeps); T = T0
    for sw in range(sweeps):
        order = m.nonpin[:]; rng.shuffle(order)
        for g in order:
            mv, touched, snap = m.propose_move(g, rng)
            if mv == 'noop': continue
            new = m.total(); d = new - cur
            if d >= 0 or rng.random() < math.exp(d/T):
                cur = new
                if new > best: best = new
            else:
                m.revert(snap)
        T *= cool
    return best

basin = []
for k in (5, 10, 20):
    rec = []
    for rep in range(3):
        m = make_model(seed=SEED+300+rep)
        truth_key(m, with_poly=True)
        rng = random.Random(SEED+400+k*10+rep)
        pert = rng.sample([g for g in m.nonpin if g not in ISLETS], k)
        for g in pert:
            m._move_v1(g, m.sample_cell(exclude=(m.v1[g],)))
        start_state = m.total()  # (pcell still truth; recomputed inside descend)
        end = descend(m, 300, 0.3, 0.01, SEED+500+k*10+rep)
        got = sum(1 for g in pert if m.v1[g] == GI[g]['primary'])
        rec.append({'recovered': got, 'k': k, 'end': round(end, 2)})
        log('  k=%d rep=%d: recovered %d/%d  end=%.2f' % (k, rep, got, k, end))
    basin.append({'k': k, 'mean_recovered': round(sum(r['recovered'] for r in rec)/len(rec), 2),
                  'detail': rec})
RESULTS['stages']['route_a_basin'] = basin; save()

log('route (a) complete. stage 4 next.')
save()
