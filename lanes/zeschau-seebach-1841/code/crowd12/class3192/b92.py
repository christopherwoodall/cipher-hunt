#!/usr/bin/env python3
"""B92 — 92 conditioned-polyvalence battery (H-pre then H-presuc). Runs AFTER PREREG.md."""
import sys, json, collections
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(Path.home() / 'workspace/cipher-hunt/lanes/zeschau-seebach-1841/code/crowd8/frenchman'))
import util
from util import PAIRS, N, UNI, GT
import era

OUT = {}

print('=== gate ===')
assert N == 1847, N
assert UNI[92] == 22, UNI[92]
print('gate PASS: N=1847, n92=22')
OUT['gate'] = 'PASS'

p92 = util.positions(92)
arms = {'POUR': [], 'LA': [], 'VERB': [], 'UNCLASSIFIED': []}
for i in p92:
    pre = PAIRS[i - 1] if i > 0 else None
    suc = PAIRS[i + 1] if i + 1 < N else None
    if pre == 0:
        arms['POUR'].append((i, suc))
    elif pre == 11:
        arms['LA'].append((i, suc))
    elif pre in (94, 46):
        arms['VERB'].append((i, pre, suc))
    else:
        arms['UNCLASSIFIED'].append((i, pre, suc))

print('\n=== arm census ===')
for k, v in arms.items():
    print(f'{k}: n={len(v)}', v)
OUT['arms'] = {k: v for k, v in arms.items()}

# signatures
INF_LEAN = 29   # suc=29: pour [stem]-er (lean: noun-in-er alternative)
NOUN_STRONG = 64  # suc=64: *"pour INF qui" ungrammatical (C1: 64=qui prov)

def sig(suc):
    s = []
    if suc == INF_LEAN:
        s.append('INF-lean')
    if suc == NOUN_STRONG:
        s.append('NOUN-strong')
    return s

print('\n=== H-pre test ===')
pour_sigs = [(i, sig(s)) for i, s in arms['POUR']]
la_sigs = [(i, sig(s)) for i, s in arms['LA']]
print('POUR-arm signatures:', pour_sigs)
print('LA-arm signatures:', la_sigs)
cross_in_pour = [i for i, s in pour_sigs if 'NOUN-strong' in s]   # suc=64 inside INF-arm
cross_in_la = [i for i, s in la_sigs if 'INF-lean' in s]          # suc=29 inside NOUN-arm
inf_in_pour = [i for i, s in pour_sigs if 'INF-lean' in s]
noun_in_la = [i for i, s in la_sigs if 'NOUN-strong' in s]
print(f'INF-lean in POUR: {inf_in_pour} | NOUN-strong in LA: {noun_in_la}')
print(f'CROSS: NOUN-strong in POUR: {cross_in_pour} | INF-lean in LA: {cross_in_la}')
OUT['H_pre'] = {'inf_in_pour': inf_in_pour, 'noun_in_la': noun_in_la,
                'cross_noun_in_pour': cross_in_pour, 'cross_inf_in_la': cross_in_la}

h_pre_grant = (len(inf_in_pour) >= 2 and len(noun_in_la) >= 1
               and not cross_in_pour and not cross_in_la)
h_pre_refuted = bool(cross_in_pour or cross_in_la)
print('H-pre:', 'GRANT' if h_pre_grant else ('REFUTED (falsifier fired)' if h_pre_refuted else 'INCONCLUSIVE'))
OUT['H_pre']['decision'] = 'GRANT' if h_pre_grant else ('REFUTED' if h_pre_refuted else 'INCONCLUSIVE')

# ---- H-presuc (only if H-pre refuted) ----
OUT['H_presuc'] = None
if h_pre_refuted:
    noun_islet = [i for i, s in arms['POUR'] if s == NOUN_STRONG]   # pre=00 & suc=64
    inf_islet = [i for i, s in arms['POUR'] if s == INF_LEAN]       # pre=00 & suc=29
    both = [i for i, s in arms['POUR'] if s == NOUN_STRONG and s == INF_LEAN]
    uncl = [i for i, s in arms['POUR'] if not sig(s)]
    print('\n=== H-presuc ===')
    print(f'NOUN-islet (pre=00 & suc=64): {noun_islet}')
    print(f'INF-islet (pre=00 & suc=29): {inf_islet}')
    print(f'both-signatures (must be []): {both}')
    print(f'unclassified POUR windows (recorded, not forced): {uncl}')
    for i in noun_islet + inf_islet:
        print('  @%d:' % i, ' '.join(str(PAIRS[j]) for j in range(max(0, i - 2), min(N, i + 3))))
    OUT['H_presuc'] = {'noun_islet': noun_islet, 'inf_islet': inf_islet,
                       'both': both, 'unclassified_pour': uncl}
    grant = (noun_islet and inf_islet and not both
             and not set(noun_islet) & set(inf_islet))
    # n_eff bar: below ISLET-3 (n=4/n_eff=3) -> cap at FENCED
    n_eff = min(len(noun_islet), len(inf_islet))
    if grant and n_eff >= 3:
        dec = 'GRANT-WITH-ISLETS (recommendation)'
    elif grant:
        dec = f'FENCED (n_eff={n_eff} < ISLET-3 precedent; hypothesis + replication legs for round 13)'
    else:
        dec = 'NULL'
    print('H-presuc decision:', dec)
    OUT['H_presuc']['decision'] = dec

# ---- VERB-arm (recorded third reading) ----
print('\n=== VERB-arm (pre in {94,46} -> finite verb) ===')
for i, pre, suc in arms['VERB']:
    tag = '94=ne prov-strong (C1)' if pre == 94 else '46=que GT'
    print(f'@{i}: pre={pre} ({tag}) 92 suc={suc}')
OUT['verb_arm_n'] = len(arms['VERB'])

# ---- era legs ----
print('\n=== E92-1: (pour, *, qui) trigrams pool-wide ===')
mid = era.trigram_mid('pour', 'qui')
tot = sum(mid.values())
print(f'total n = {tot}; distinct middles = {len(mid)}')
OUT['E92_1_total'] = tot
OUT['E92_1_middles'] = dict(mid.most_common(40))
# infinitive check: middles ending in -er/-ir/-re are infinitive-lean; report them all
inf_lean = {w: c for w, c in mid.items() if w.endswith(('er', 'ir', 're')) and len(w) > 2}
print(f'infinitive-lean middles (endswith er/ir/re): {inf_lean if inf_lean else "NONE"}')
OUT['E92_1_infinitive_lean_middles'] = inf_lean
# also report any middle that is unambiguously verbal other ways: show full list if small
if tot <= 60:
    print('all middles:', dict(mid))
    OUT['E92_1_all'] = dict(mid)

print('\n=== E92-2: (pour, NOUN, qui) attestation ===')
# constituency note: middles that are clearly nominal/pronominal (non-verbal)
nonverb = {w: c for w, c in mid.items() if w not in inf_lean}
print(f'non-infinitive middles n_types={len(nonverb)}; top:', dict(collections.Counter(nonverb).most_common(10)))
OUT['E92_2_nonverb_top10'] = dict(collections.Counter(nonverb).most_common(10))
OUT['E92_2_nonverb_total'] = sum(nonverb.values())

print('\n=== E92-3: (pour, *-er) attestation ===')
n_pour_er, ex = era.bigram_suc_ending('pour', 'er')
print(f'n((pour, w~er)) = {n_pour_er}; examples: {ex}')
OUT['E92_3_n'] = n_pour_er
OUT['E92_3_examples'] = ex

# ---- overall verdict ----
if h_pre_grant:
    verdict = 'H-pre GRANT (conditioned polyvalence: pre=00->INF, pre=11->NOUN)'
elif h_pre_refuted and OUT['H_presuc'] and OUT['H_presuc']['decision'].startswith('GRANT'):
    verdict = OUT['H_presuc']['decision']
elif h_pre_refuted and OUT['H_presuc']:
    verdict = 'H-pre REFUTED; ' + OUT['H_presuc']['decision']
else:
    verdict = 'NULL (92 contested)'
print('\nB92 VERDICT:', verdict)
OUT['verdict'] = verdict

json.dump(OUT, open(HERE / 'b92_results.json', 'w'), indent=1,
          default=lambda o: list(o) if isinstance(o, tuple) else o)
print('\nwrote b92_results.json')
