#!/usr/bin/env python3
"""hunter7778: H1 (collocation frames), H2 (06 cross-check), H4 (intersection).
Pre-registered in PREREG.md BEFORE running. Cipher = repaired 1,847-pair parse."""
import json, re, glob, os, collections, math
from pathlib import Path

LANE = Path.home() / 'workspace/cipher-hunt/lanes/zeschau-seebach-1841'
CORP = LANE / 'code/side-period/corpus'

# ---------- cipher ----------
def load_pairs():
    rows = []
    for line in open(LANE / 'data/upstream-ct_R5005.txt'):
        line = line.strip()
        if not line:
            continue
        lid, digits = line.split()
        rows.append((lid, re.sub(r'\D', '', digits)))
    off = json.loads((LANE / 'code/side-keyhunt/repaired_offsets.json').read_text())
    pairs = []
    for lid, digits in rows:
        o = off[lid]
        pairs += [digits[i:i+2] for i in range(o, len(digits)-1, 2)]
    assert len(pairs) == 1847, len(pairs)
    return [int(g) for g in pairs]

P = load_pairs(); N = len(P)

# ---------- corpus ----------
def tokenize_elision(text):
    text = text.replace('-\n', '').replace('-\r\n', '')
    text = text.lower()
    text = re.sub(r"[’‘`]", "'", text)
    text = re.sub(r"\b([a-zàâäéèêëîïôöùûüçœæ]+)'([a-zàâäéèêëîïôöùûüçœæ]+)", r"\1' \2", text)
    return re.findall(r"[a-zàâäéèêëîïôöùûüçœæ]+'?|[a-zàâäéèêëîïôöùûüçœæ]+", text)

def load_slice(files):
    toks = []
    for f in files:
        toks.extend(tokenize_elision(open(f, encoding='utf-8', errors='replace').read()))
    return toks

ness8 = load_slice([CORP / 'nesselrode-v8.txt'])
guiz = load_slice([CORP / 'guizot-memoires-t5-t6.txt'])
print(f'nesselrode-v8: {len(ness8)} toks; guizot t5-t6: {len(guiz)} toks')

def gouv_profile(toks, name):
    n = len(toks)
    idx = [i for i, t in enumerate(toks) if t == 'gouvernement']
    pl = sum(1 for t in toks if t in ('gouvernements', 'gouvernemental', 'gouvernementaux'))
    L1 = collections.Counter(toks[i-1] for i in idx if i > 0)
    R1 = collections.Counter(toks[i+1] for i in idx if i+1 < n)
    tot = len(idx)
    print(f'\n=== {name}: n(gouvernement)={tot} (+{pl} plural/adj forms, excluded)')
    print('  top L1:', [(w, c, f'{c/tot:.3f}') for w, c in L1.most_common(10)])
    print('  top R1:', [(w, c, f'{c/tot:.3f}') for w, c in R1.most_common(10)])
    return toks, idx, L1, R1, tot

tn, idxn, L1n, R1n, totn = gouv_profile(ness8, 'NESSELRODE v8')
tg, idxg, L1g, R1g, totg = gouv_profile(guiz, 'GUIZOT t5-t6')

# H1b: "est le gouvernement" trigram vs independence
for toks, name in ((tn, 'ness8'), (tg, 'guizot')):
    n = len(toks)
    tri = sum(1 for i in range(n-2) if toks[i] == 'est' and toks[i+1] == 'le' and toks[i+2] == 'gouvernement')
    pe, pl, pg = toks.count('est')/n, toks.count('le')/n, toks.count('gouvernement')/n
    E = pe*pl*pg*n
    print(f'H1b {name}: n("est le gouvernement")={tri} vs independence E={E:.2f} ratio={tri/E if E else float("nan"):.2f}')

# H1c: P("on" within L1..L2 of gouvernement)
for toks, idx, name in ((tn, idxn, 'ness8'), (tg, idxg, 'guizot')):
    hit = sum(1 for i in idx if (i > 0 and toks[i-1] == 'on') or (i > 1 and toks[i-2] == 'on'))
    print(f'H1c {name}: P(on in L1..L2 | gouvernement) = {hit}/{len(idx)} = {hit/len(idx) if idx else 0:.3f}')

# H1d: "le qui" bigram rate; modal R1 already printed
for toks, name in ((tn, 'ness8'), (tg, 'guizot')):
    n = len(toks)
    lq = sum(1 for i in range(n-1) if toks[i] == 'le' and toks[i+1] == 'qui')
    print(f'H1d {name}: n("le qui")={lq} / {n} = {lq/n:.2e}; n("le")={toks.count("le")}')

# ---------- H2: enumerate 77-78-06 and 77-78-X-06 ----------
print('\n=== H2: 77-78 bigram windows ===')
bigrams = [(i) for i in range(N-1) if P[i] == 77 and P[i+1] == 78]
print('77-78 bigrams @', bigrams, 'n =', len(bigrams))
fivemers = [i for i in range(N-4) if P[i:i+5] == [77, 78, 94, 82, 6]]
print('77-78-94-82-06 5-mers @', fivemers, '(assert exactly 2)')
assert fivemers == [1180, 1351], fivemers
print('exact windows:')
for i in bigrams:
    print(f'  @{i}:', P[max(0,i-2):i+6])
print('\n77-78-06 trigrams / 77-78-X-06:')
for i in bigrams:
    if i+2 < N and P[i+2] == 6:
        print(f'  @{i}: 77 78 06 — 06@{i+2} pre={P[i+1]} F61->', 'ent' if P[i+1]==82 else 'NOT ent')
    elif i+3 < N and P[i+3] == 6:
        print(f'  @{i}: 77 78 {P[i+2]} 06 — 06@{i+3} pre={P[i+2]} F61->', 'ent' if P[i+2]==82 else 'NOT ent')
# F61 windows: 06 with pre=82
f61 = [i for i in range(1, N) if P[i] == 6 and P[i-1] == 82]
print('06-with-pre=82 windows @', f61, '(F61: n=4, n_eff=3)')
# 78-94 bigrams (for H3c scan)
b7894 = [i for i in range(N-1) if P[i] == 78 and P[i+1] == 94]
print('78-94 bigrams @', b7894)
# 29-94 bigrams (GT er + ne)
b2994 = [i for i in range(N-1) if P[i] == 29 and P[i+1] == 94]
print('29-94 bigrams @', b2994)

# ---------- H4: intersection with anchored regions ----------
print('\n=== H4: anchored-region intersection ===')
crib = [i for i in range(N-5) if P[i:i+6] == [11, 70, 82, 34, 29, 40]]
print('crib 11-70-82-34-29-40 @', crib)
thread_idx = set()
for i in bigrams:
    thread_idx.update(range(i-3, i+5))
anchored = set()
for i in crib:
    anchored.update(range(i-3, i+9))
q46 = [i for i in range(N) if P[i] == 46]
for i in q46:
    anchored.update(range(i-3, i+4))
inter = sorted(thread_idx & anchored)
print('thread-window indices ∩ anchored-region indices:', inter if inter else 'EMPTY — no overlap')
# 78="me"@8 domain vs T4 domain
print('@8 window:', P[5:13], ' T4 windows @1180-1184, @1351-1355 — domains disjoint:', not ({8} & {1180,1181,1182,1183,1184,1351,1352,1353,1354,1355}))
# exact @1351-1359 and @1180-1189 frames for the record
print('@1180-1189:', P[1180:1190])
print('@1351-1359:', P[1351:1360])
print('@1177-1179 (48 59 37):', P[1177:1180])
print('@1348-1350 (34 62 48):', P[1348:1351])
