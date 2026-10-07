"""Red-team round 4: quantified lane position on homophony/polyvalence (work order 9/10).

Method:
 1. Load the 1,846 aligned pairs (upstream offsets tokenization).
 2. Encode the adjudicated reading ledger (grades from round-3/3b red-team JSONs + STATE).
 3. Count groups with >=2 LIVE readings (live = grade >= LEAD, or provisional+, not killed).
 4. Null A (kill-rate): graded-hypothesis kill rate from red-team ledgers -> expected
    spurious surviving doubles (binomial).
 5. Null B (exemplar/direction): from the personne/prend/erre exemplars, measure the
    encipherer's respell signature (group-follows-sound vs group-takes-new-sound);
    test whether observed doubles match the ear-cutting noise direction (allophony)
    or the polyvalence direction (same group, different sounds).
 6. Conditioning audit: verify each established double's conditioning rule in the pair stream.
 7. Information bound: token coverage of identified groups; era-corpus syllable
    inventory vs ~72 syllable slots (96 groups - ~24 letter slots).
"""
import json, re, math
from collections import Counter

LANE = '/home/hatch/workspace/cipher-hunt/lanes/zeschau-seebach-1841'

def load_pairs():
    off = json.load(open(LANE + '/data/upstream-offsets.json'))
    lines = [l.strip() for l in open(LANE + '/data/upstream-ct_R5005.txt') if l.strip()]
    key_of = {}
    for i, line in enumerate(lines):
        k, s = line.split()
        key_of[k] = s
    toks = []
    for k in sorted(key_of, key=lambda k: (int(k.split('_')[0][1:]), int(k.split('_')[1]))):
        s = key_of[k]
        o = off[k]
        toks += [s[i:i + 2] for i in range(o, len(s) - 1, 2)]
    return toks

pairs = load_pairs()
N = len(pairs)
freq = Counter(pairs)
print(f'pairs={N} distinct_groups={len(freq)}')

# ---- adjudicated reading ledger: (group, reading, grade, conditioning_note) ----
# grades: GT > CONF > PROV > PROVs > SLEAD > LEAD > MED > PLAUS ; killed/disfavored excluded
LEDGER = [
    # ground truth pencil cribs
    ('11','la','GT','-'),('70','pre','GT','-'),('82','m','GT','-'),('34','i','GT','-'),
    ('29','er','GT','-'),('40','e','GT','-'),('46','que','GT','-'),
    ('87','ce','PROVs','cela-leg register-dependent; 4/5 then 3/4 era'),
    ('64','qui','PROV','re-promotion BLOCKED; rival meme live'),
    ('64','meme','LEAD','stem-hunter rival; round-4 order 7 to adjudicate'),
    ('96','par','PROV','CONFIRMED 4/4, inherits 87=ce status'),
    ('94','ne','PROVs','on-ne-prend-pas lock @1331; ne-pas-inf x2'),
    ('94','re','LEAD','morphologist rival: -rement 1.28x vs -nement 0.66x (F24)'),
    ('94','en','LEAD','islets @1168 en-ce-83, @1575 m-en-76; LEAD-grade conditioned'),
    ('62','on','SLEAD','on-ne-[verbe] x5+; pers|on|ne @508 same reading'),
    ('67','veut','PROV','-'),
    ('78','me','LEAD','promote rejected; chunk tension pending'),
    ('06','verb-stem-class','PROV','F21 worker convergence'),
    ('06','ent','PLAUS','restricted to 3 trigrams @578/@1181/@1350; K1 killed general only'),
    ('77','le','LEADW','3b: LEAD-weak accepted, 1 check; pas DISFAVORED strong; three-way -> round-4 order 2'),
    ('52','pas','SLEAD','on-ne-prend-pas @1331; ne-pas-inf x2 @1293/@1806; K5-bounded'),
    ('52','se','LEAD','closer rival L1 1.191 + qui->52 r=1.32; live under polyvalence'),
    ('52','so','LEAD','K5-forced: per|so|nne @160 (93 52 94) coherent parse'),
    ('24','en','SLEAD','formula-locked en-ce-qui x2, en-plus @73; collision noted'),
    ('56','plus','MED','en-plus @73; K7 rejected -> tension only'),
    ('43','me','MED','scoped outside x2 formula'),
    ('37','le','MED','le-gouvernement @1178; qui-le-[v] x3'),
    ('37','me','LEADW','closer rival LEAD-weak L1 1.001; unadjudicated'),
    ('21','le/les','LEAD','stem-hunter lead'),
    ('00','de','LEAD','stem-hunter lead'),
    ('01','est','MED','@295; c-est=87+01 in x2 formula'),
]
GRADE_RANK = {'GT':7,'CONF':6,'PROV':5,'PROVs':5,'SLEAD':4,'LEAD':3,'LEADW':2.5,'MED':2,'PLAUS':1,'WEAK':0.5}
LIVE_MIN = 3  # LEAD and up (PLAUS counts only if it survived a kill: 06=ent did via K1)

LIVE_MIN = 3  # LEAD and up; 06=ent PLAUS kept: survived K1 kill of the general reading
live = [r for r in LEDGER if GRADE_RANK[r[2]] >= LIVE_MIN or (r[0]=='06' and r[1]=='ent')]
identified = [r for r in LEDGER if r[2] in GRADE_RANK]  # any surviving grade incl MED/PLAUS
identified += [('17','fois','WEAK','single window @1033')]  # below bar, still an identified group
D_groups = {g for g,_,_,_ in identified}
by_group = {}
for g, rd, gr, note in live:
    by_group.setdefault(g, []).append((rd, gr, note))
M = len(by_group)
R = len(live)
doubles = {g: v for g, v in by_group.items() if len(v) >= 2}
print(f'\nM (groups with >=1 live reading) = {M}')
print(f'R (live readings) = {R}')
print(f'groups with >=2 live readings = {len(doubles)}')
for g, v in sorted(doubles.items()):
    print(f'  {g}: ' + '; '.join(f'{rd}[{gr}]' for rd, gr, _ in v))

# established = every reading >= LEAD and (>=1 kill-forced or naked observation or >=2 legs)
ESTABLISHED = {'06', '94', '52'}
print(f'\nestablished conditioned-polyvalent (>=LEAD all readings): {sorted(ESTABLISHED)}')
print(f'  -> {len(ESTABLISHED)}/{M} = {len(ESTABLISHED)/M:.3f}')
print(f'inclusive (rivalries 64, 37): {len(doubles)}/{M} = {len(doubles)/M:.3f}')
print(f'identified groups (any surviving grade, incl 17=fois WEAK): {len(D_groups)}')
print(f'strict polyvalence rate: {len(ESTABLISHED)}/{len(D_groups)} = {len(ESTABLISHED)/len(D_groups):.3f}')
print(f'inclusive polyvalence rate: {len(doubles)}/{len(D_groups)} = {len(doubles)/len(D_groups):.3f}')

# ---- token coverage of identified groups ----
cov_tokens = sum(freq[g] for g in by_group)
print(f'\ntoken coverage of live-reading groups: {cov_tokens}/{N} = {cov_tokens/N:.3f}')
poly_tokens = sum(freq[g] for g in doubles)
print(f'token share in polyvalent groups: {poly_tokens}/{N} = {poly_tokens/N:.3f}')

# ---- conditioning audit: verify each established double's rule in the pair stream ----
print('\n--- conditioning audit (pair indices) ---')
idx = {g: [i for i, p in enumerate(pairs) if p == g] for g in doubles}
# 06: trigram-internal 06 = the 06 in 77 78 94 82 06 windows @578/@1181/@1350 ; elsewhere verb-stem
for g in sorted(doubles):
    print(f'{g}: n={len(idx[g])} idx={idx[g][:12]}{"..." if len(idx[g])>12 else ""}')
# verify the three 06 trigram windows byte-identical 77 78 94 82 06
for t in (578, 1181, 1350):
    print(f'  @ {t}: {" ".join(pairs[t:t+5])}')
# 94 islets
for t in (1168, 1575):
    print(f'  94-islet @ {t}: {" ".join(pairs[t-2:t+4])}')
# 52: negation frames vs @160
for t in (1331, 1293, 1806, 160):
    print(f'  52-frame @ {t}: {" ".join(pairs[t-2:t+4])}')

# ---- Null A: kill-rate from red-team ledgers ----
rt3 = json.load(open(LANE + '/code/crowd3/red_team_results.json'))
rt3b = json.load(open(LANE + '/code/crowd3/red_team_round3b_results.json'))
led = rt3b['ledger_round3_combined']
def aslist(v): return v if isinstance(v, list) else []
killed_group_readings = [
    "06=/mɑ̃/ (N17 crib contradiction)",
    "24=est (N10 refuted)",
    "01=ci (K4 killed provisional)",
    "06=ent general (K1/N19 refuted; restricted survives)",
    "77=que (N18 disfavored)",
    "52=pas single-reading (K5 scoped; reading survives)",
    "24=de in en-ce-qui formula (K2 scoped)",
    "43=mi/parmi in x2 formula (K3 conditional)",
    "56=plus single-reading (K7 rejected)",
    "H5 J-ai-l-honneur-de composite (N11; 82=neur DOA vs GT)",
    "96=de (N14 refuted)",
    "16=a (N13 not promoted)",
]
K = len(killed_group_readings)
G = len(live) + K  # graded group-reading hypotheses
kappa = K / G
E = len(live) - len(by_group)  # extra readings beyond first per group
p_all_survive = (1 - kappa) ** E
print('--- Null A: kill-rate ---')
print(f'killed group-readings={K} graded={G} kappa={kappa:.3f}')
print(f'extra live readings E={E}; under M1(monovalent) P(all {E} survive)=(1-kappa)^{E}={p_all_survive:.3f}')
print(f'expected surviving spurious doubles = {E*(1-kappa):.2f} vs observed {E}')
print()
print('ledger:', {k: led[k] for k in ('kills_hard','kills_provisional','kills_scoped','kills_rejected','refuted_downgraded','demotions','promotions','upheld')})

print('=== conditioning audit: 94 (36 occurrences) ===')
for i in idx['94']:
    ctx = ' '.join(pairs[max(0,i-2):i+3])
    tag = []
    if i > 0 and pairs[i-1] == '62': tag.append('62_94:on-ne?')
    if i+1 < N and pairs[i+1] in ('52','70'): tag.append('94_52/70:ne-pas/pre')
    if i in (1168, 1575): tag.append('ISLET:en')
    print(f'{i:5d} {ctx:22s} {" ".join(tag)}')

print()
print('=== conditioning audit: 06 trigram-internal vs elsewhere ===')
tri_internal = set()
for t in (578, 1181):
    w = pairs[t:t+3]
    assert w == ['94','82','06'], (t, w)
    tri_internal.add(t+2)
# third trigram: find 77 78 94 82 06
for i in range(N-4):
    if pairs[i:i+5] == ['77','78','94','82','06']:
        tri_internal.add(i+4)
        print('trigram 77 78 94 82 06 @', i)
print('trigram-internal 06 positions:', sorted(tri_internal))
print('06 total n =', len(idx['06']), '-> verb-stem-class positions =', len(idx['06']) - len(tri_internal))


print()
print('=== conditioning audit: 52 (27 occurrences) ===')
for i in idx['52']:
    ctx = ' '.join(pairs[max(0,i-2):i+3])
    tag = []
    if i > 0 and pairs[i-1] in ('94','70'): tag.append('neg-frame:pas')
    if i == 160: tag.append('K5 word-internal:so')
    print(f'{i:5d} {ctx:22s} {" ".join(tag)}')

print('=== repeat byte-identity (exemplar null) ===')
def win(i, k=5): return ' '.join(pairs[i:i+k])
# gouvernement trigrams: 94-positions
gou = [i for i in range(N-2) if pairs[i:i+3] == ['94','82','06']]
print('94-82-06 trigrams @', gou)
for i in gou: print('  ', i, win(i-2, 7))
# erre 29 40 @290/@684
for t in (290, 684): print('erre @', t, win(t-2, 6))
# en ce qui: 24 87 64
ecq = [i for i in range(N-2) if pairs[i:i+3] == ['24','87','64']]
print('24-87-64 @', ecq)
for i in ecq: print('  ', i, win(i-2, 7))
# ne pas: 94 52
np_ = [i for i in range(N-1) if pairs[i:i+2] == ['94','52']]
print('94-52 bigrams @', np_)
# parce que: 96 87 46 ?
pcq = [i for i in range(N-2) if pairs[i:i+3] == ['96','87','46']]
print('96-87-46 @', pcq)
# personne windows
print('personne @160:', win(158, 6), '| @508:', win(506, 6))
