#!/usr/bin/env python3
"""RED TEAM audit of the Frenchman's 62="on" leg-3 case (round 5).

Independently re-derives every load-bearing number in
code/crowd5/frenchman62_leg3.{py,json,md} and stress-tests the two
claimed non-ear legs:
  A+E: subject-battery rival kill + "il"-differential on the 46->62 null
  C:   mappable-cell follower profile chi-square
Plus the differential the Frenchman did NOT run: 62's follower profile
vs era P(.|il) (does "on" actually beat its closest rival?).
"""
import json, math, re, collections
from pathlib import Path

LANE = Path(__file__).resolve().parents[3]
DATA = LANE / 'data'

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

pairs = load_repaired(); n = len(pairs)
assert n == 1847
big = collections.Counter(zip(pairs[:-1], pairs[1:]))
n62 = pairs.count(62)

# era tokenizer (same word-space recipe as the claimant, independent re-implementation)
def words(path):
    t = open(path, encoding='utf-8', errors='replace').read().lower()
    t = re.sub(r"[']", "'", t)
    t = re.sub(r"\b([a-zàâäéèêëîïôöùûüç]+)'([a-zàâäéèêëîïôöùûüç]+)", r"\1' \2", t)
    return re.findall(r"[a-zàâäéèêëîïôöùûüç]+(?:'[a-zàâäéèêëîïôöùûüç]+)?", t)

toks = words(DATA/'gutenberg-30513-tocqueville-t1.txt') + words(DATA/'gutenberg-30514-tocqueville-t2.txt')
N = len(toks); uni = collections.Counter(toks)
print(f'era tokens: {N} (claimant: 221027)')

def cond(a, b):  # P(b|a) word-space
    na = uni[a]; nab = sum(1 for x, y in zip(toks, toks[1:]) if x == a and y == b)
    return na, nab, nab/na if na else float('nan')

def cond_pred(a, b):  # P(a|b) word-space
    nb = uni[b]; nab = sum(1 for x, y in zip(toks, toks[1:]) if x == a and y == b)
    return nb, nab, nab/nb if nb else float('nan')

print('--- era marginals: redteam vs claimant ---')
for label, a, b, mode, claim in [
    ('P(on)        ', 'on', None, 'uni', 0.007311),
    ('P(ne|on)     ', 'on', ('ne','n'), 'condset', 0.1584),
    ('P(on|que)    ', 'que', 'on', 'condpredset', 0.0798),
    ('P(ne|il)     ', 'il', ('ne','n'), 'condset', 0.1896),
    ('P(il|que)    ', 'que', 'il', 'condpredset', 0.1045),
    ('P(me|on)     ', 'on', 'me', 'cond', 0.0050),
]:
    if mode == 'uni':
        got = uni[a]/N
    elif mode == 'cond':
        got = cond(a, b)[2]
    elif mode == 'condset':
        nab = sum(1 for x, y in zip(toks, toks[1:]) if x == a and y in b)
        got = nab/uni[a]
    elif mode == 'condpredset':
        nb = uni[b]; nab = sum(1 for x, y in zip(toks, toks[1:]) if x in ('que','qu') and y == b)
        got = nab/nb
    print(f'  {label} redteam={got:.6f} claim={claim:.6f} ratio={got/claim:.4f} {"OK" if abs(got/claim-1)<0.02 else "MISMATCH"}')

# --- binomial checks B and E ---
n46nf = sum(1 for i in range(n-1) if pairs[i] == 46)
nb = uni['on']; nab = sum(1 for x, y in zip(toks, toks[1:]) if x in ('que','qu') and y == 'on')
p_on_q = nab/uni['que']
p_il_q = sum(1 for x, y in zip(toks, toks[1:]) if x in ('que','qu') and y == 'il')/uni['que']
p0_on = (1-p_on_q)**n46nf
p0_il = (1-p_il_q)**n46nf
print(f'--- binomials ---')
print(f'  trials n46_nonfinal={n46nf}; obs 46->62={big[(46,62)]}')
print(f'  Check B: E={n46nf*p_on_q:.2f} (claim 2.31), p0={p0_on:.4f} (claim 0.0896)')
print(f'  Check E: E_if_il={n46nf*p_il_q:.2f} (claim 3.03), p0_if_il={p0_il:.4f} (claim 0.0407)')

# --- Check C chi-square exact recompute ---
fol_on = collections.Counter(y for x, y in zip(toks, toks[1:]) if x == 'on')
fol_il = collections.Counter(y for x, y in zip(toks, toks[1:]) if x == 'il')
n_on = uni['on']; n_il = uni['il']
obs62_fol = collections.Counter(pairs[i+1] for i in range(n-1) if pairs[i] == 62)
cells = [('ne', 94, (fol_on['ne']+fol_on['n'])/n_on),
         ('me', 21, fol_on['me']/n_on),
         ('la', 11, fol_on['la']/n_on),
         ('que', 46, (fol_on['que']+fol_on['qu'])/n_on)]
p_cells = [c[2] for c in cells]; p_other = 1-sum(p_cells)
obs = [obs62_fol[c[1]] for c in cells] + [n62 - sum(obs62_fol[c[1]] for c in cells)]
exp = [n62*p for p in p_cells] + [n62*p_other]
chi2 = sum((o-e)**2/e for o, e in zip(obs, exp))
print(f'--- Check C: obs={obs} exp={[round(e,3) for e in exp]} chi2={chi2:.2f} (claim 11.24)')
print(f'  low expected cells (<5): {sum(1 for e in exp[:-1] if e<5)}/4 named cells -> chi2 approx INVALID')
# exact multinomial p via Monte Carlo (fixed n=35, cell probs as above)
import random
random.seed(7)
probs = p_cells + [p_other]
def draw():
    cs = [0]*5
    for _ in range(n62):
        r = random.random(); s = 0
        for k, p in enumerate(probs):
            s += p
            if r < s: cs[k] += 1; break
    return cs
def stat(cs):
    return sum((cs[k]-n62*probs[k])**2/(n62*probs[k]) for k in range(5))
obs_stat = stat(obs)
M = 200000; ge = sum(1 for _ in range(M) if stat(draw()) >= obs_stat)
print(f'  exact multinomial p (MC {M}): {ge/M:.4f} (chi2 approx claimed 0.024)')

# --- the differential NOT run: same profile vs era P(.|il) ---
cells_il = [('ne', 94, (fol_il['ne']+fol_il['n'])/n_il),
            ('me', 21, fol_il['me']/n_il),
            ('la', 11, fol_il['la']/n_il),
            ('que', 46, (fol_il['que']+fol_il['qu'])/n_il)]
p_il = [c[2] for c in cells_il]; p_il_o = 1-sum(p_il)
exp_il = [n62*p for p in p_il] + [n62*p_il_o]
probs_il = p_il + [p_il_o]
def stat_il(cs):
    return sum((cs[k]-n62*probs_il[k])**2/(n62*probs_il[k]) for k in range(5))
obs_stat_il = stat_il(obs)
ge_il = sum(1 for _ in range(M) if stat_il(draw()) >= obs_stat_il)
# MC draws must use il probs for the il test
def draw_il():
    cs = [0]*5
    for _ in range(n62):
        r = random.random(); s = 0
        for k, p in enumerate(probs_il):
            s += p
            if r < s: cs[k] += 1; break
    return cs
ge_il = sum(1 for _ in range(M) if stat_il(draw_il()) >= obs_stat_il)
print(f'--- same profile vs era P(.|il): chi2-like={obs_stat_il:.2f} exact p={ge_il/M:.4f}')
print(f'  era P(ne|il)={(fol_il["ne"]+fol_il["n"])/n_il:.4f} era P(me|il)={fol_il["me"]/n_il:.4f}')
# log-likelihood ratio: profile fit under on vs under il
ll = lambda ps: sum(o*math.log(p) for o, p in zip(obs, ps) if p > 0)
print(f'  logL(profile|on)={ll(probs):.2f}  logL(profile|il)={ll(probs_il):.2f}  delta={ll(probs)-ll(probs_il):.2f}')
