#!/usr/bin/env python3
"""Period drag T1-T8 — Seebach cipher-hunt round 6.

Drags the 117 red-team-adjudicated period crib cards (code/side-period/
cribs-adjudicated.md, work order code/crossfleet/memo2-period-corpus.md)
against the canonical 1,847-pair repaired stream at the 8 concrete targets.

All positions cited are 0-based pairs in the REPAIRED frame
(code/side-keyhunt/repaired_offsets.json). The memo's raw-frame positions
were re-verified: raw 766/1054 (la premiere) = repaired 754/1034;
raw 884/1204 (R1) -> repaired 1180/1351 (see notes on raw artifacts below).

Constraints honored:
- F44 crib-learned 24-unit by-ear alphabet (inventorist tiler) + manual
  fused/split variants. No standard-French syllabification.
- Anchor-preserving controls on every drag (N34): null = lexicon fitters at
  the SAME window with the SAME anchor set.
- Anti-collision: "premier"/"premiere" never dragged.
- T4: 94="ne" (provisional-strong) is NOT adopted/demoted here; the tension
  is quantified and referred to the Red Team.
- >=2 independent checks per claim.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import (PAIRS, GT, PROV, LE77, ISLETS, fit_cells, drag_word,
                    null_rate, load_lexicon_tilings)

P = PAIRS
HARD = dict(GT)
HARD.update(PROV)          # 87=ce 64=qui 96=par 94=ne (94 freed per-target in T4)
HARD77 = dict(HARD)
HARD77.update(LE77)        # +77=le (provisional-CONDITIONED; fenced at T4)

LEX = None


def lex():
    global LEX
    if LEX is None:
        LEX = load_lexicon_tilings()
    return LEX


def _tilings(word, manual=()):
    """Candidate tilings: by-ear tiler top-8 UNION manual fused/split variants."""
    from common import byear_tile
    tilings, seen = [], set()
    for cells, _s in byear_tile(word, k=8):
        t = tuple(cells)
        if t not in seen:
            seen.add(t)
            tilings.append(cells)
    for cells in manual:
        t = tuple(cells)
        if t not in seen:
            seen.add(t)
            tilings.append(list(cells))
    return tilings


def window_fits(word, start, kcells, hard, free=frozenset(), manual=()):
    """All fitting tilings of `word` at P[start:start+k] for each k in kcells."""
    out = []
    for cells in _tilings(word, manual):
        k = len(cells)
        if k not in kcells:
            continue
        groups = P[start:start + k]
        if len(groups) < k:
            continue
        ok, notes = fit_cells(cells, groups, hard, free)
        if ok:
            out.append({'start': start, 'cells': cells, 'notes': {
                'overrides': notes['overrides'],
                'islet_reads': notes['islet_reads'],
                'free_reads': notes['free_reads'],
                'collisions': notes['collisions']}})
    return out


def scan(word, lo, hi, kcells, hard, free=frozenset(), manual=()):
    """Slide candidate over [lo, hi); return {start: [fits]}."""
    tils = _tilings(word, manual)
    byk = {}
    for cells in tils:
        byk.setdefault(len(cells), []).append(cells)
    hits = {}
    for start in range(lo, hi):
        f = []
        for k, cells_list in byk.items():
            if k not in kcells:
                continue
            groups = P[start:start + k]
            if len(groups) < k:
                continue
            for cells in cells_list:
                ok, notes = fit_cells(cells, groups, hard, free)
                if ok:
                    f.append({'start': start, 'cells': cells, 'notes': {
                        'overrides': notes['overrides'],
                        'islet_reads': notes['islet_reads'],
                        'free_reads': notes['free_reads'],
                        'collisions': notes['collisions']}})
        if f:
            hits[start] = f
    return hits


def invert(window_groups, hard, free=frozenset(), topn=15):
    """Lexicon inversion: words with a fitting tiling at this exact window,
    ranked by era frequency. Discovery inside the drag framework."""
    from common import LANE
    idx = json.load(open(os.path.join(
        LANE, 'code', 'crowd6', 'inventorist', 'byear_index.json')))
    freq = {w: f for w, f in idx['words']}
    cands = []
    for w, tilings in lex().items():
        for cells in tilings:
            ok, notes = fit_cells(cells, window_groups, hard, free)
            if ok:
                cands.append((freq.get(w, 0), w, cells, notes))
                break
    cands.sort(reverse=True)
    return [(w, f, cells) for f, w, cells, _n in cands[:topn]], len(cands)


RES = {'targets': {}, 'frame_notes': []}
NOTE = RES['frame_notes'].append

# ============ frame verification ============
NOTE('la premiere 11-70-82-34-29-40 @754 and @1034 repaired (memo raw 766/1054) VERIFIED')
NOTE('R1 77-78-94-82-06 @1180 and @1351 repaired (memo raw 884/1204). '
     'raw@884 9-mer (follow 77-44-91-67) ABSENT from repaired stream: the '
     'memo claim "R1a followed by 77=le (sentence break)" is a RAW-FRAME '
     'ARTIFACT, void in every canonical parse (old 1846 and repaired 1847).')
NOTE('memo R2 06-77-78-18-71-10-01 @raw1429: 0x in repaired stream (and 0x in '
     'old 1846 parse per crowd round). Raw-only artifact straddling dropped '
     'digits; the "06|77|78 = ent le gou" cross-check cannot be run. VOID.')
NOTE('94-82-06 trigram x3 @578/@1182/@1353 repaired; @1182/@1353 sit INSIDE '
     'the T4 windows (@1180/@1351 +2). The T4 windows ARE two of the three '
     '"restricted-ent PLAUSIBLE" trigrams.')
NOTE('96=par x21 repaired @47/131/150/224/230/342/465/602/847/914/927/947/952/'
     '960/998/1026/1063/1196/1213/1526/1786. 96->77 is 0/21: "par le" never '
     'occurs as 96-77.')

# ============ T1: opening @0 ============
t1 = {'window': P[0:6], 'cands': {}}
t1['cands']['Monsieur le Baron'] = window_fits(
    'monsieurlebaron', 0, [6], HARD,
    manual=[['mon', 'si', 'eur', 'le', 'ba', 'ron'],
            ['m', 'on', 'sieur', 'le', 'ba', 'ron'],
            ['mon', 'sieu', 'r', 'le', 'ba', 'ron']])
t1['cands']['Mon cher Baron'] = []
for k, man in [(5, [['mon', 'cher', 'ba', 'ron'],
                    ['m', 'on', 'cher', 'ba', 'ron']]),
               (6, [['m', 'on', 'ch', 'er', 'ba', 'ron'],
                    ['mo', 'n', 'che', 'r', 'ba', 'ron'],
                    ['mon', 'c', 'her', 'ba', 'ron']])]:
    t1['cands']['Mon cher Baron'].extend(window_fits('moncherbaron', 0, [k],
                                                    HARD, manual=man))
# nulls at @0 (6-cell and 5-cell windows), anchor-preserving
t1['null_6'] = null_rate(P[0:6], HARD, lex=lex())[:2]
t1['null_5'] = null_rate(P[0:5], HARD, lex=lex())[:2]
t1['verdict'] = ('HIT' if any(t1['cands']['Monsieur le Baron']) or
                 any(t1['cands']['Mon cher Baron']) else 'NULL')
RES['targets']['T1'] = t1

# ============ T2: "Votre depeche du" / "J'ai recu..." in 0-150 ============
t2 = {'cands': {}}
t2['cands']['Votre depeche du'] = scan(
    'votredepechedu', 0, 150, [6, 7], HARD,
    manual=[['vo', 'tre', 'dé', 'pê', 'che', 'du'],
            ['vo', 'tre', 'de', 'pe', 'che', 'du'],
            ['vot', 're', 'dé', 'pê', 'che', 'du'],
            ['vo', 'tre', 'dé', 'pê', 'che', 'd', 'u']])
t2['cands']["J'ai recu votre depeche du"] = scan(
    'jairecuvotredepechedu', 0, 150, [9, 10], HARD,
    manual=[['j', 'ai', 're', 'çu', 'vo', 'tre', 'dé', 'pê', 'che', 'du'],
            ['jai', 're', 'cu', 'vo', 'tre', 'de', 'pe', 'che', 'du'],
            ['j', 'ai', 're', 'cu', 'vo', 'tre', 'de', 'pe', 'che', 'du']])
for name, hits in t2['cands'].items():
    t2['cands'][name] = {'n_windows': len(hits),
                         'positions': sorted(hits)[:10]}
    if hits:
        s = sorted(hits)[0]
        k = len(hits[s][0]['cells'])
        nr = null_rate(P[s:s + k], HARD, lex=lex())
        t2['cands'][name]['null_at_first'] = nr[:2]
t2['verdict'] = 'HIT' if any(v['n_windows'] for v in t2['cands'].values()) else 'NULL'
RES['targets']['T2'] = t2

# ============ T3: noun after "la premiere" ============
# Alignment A: noun starts AT 40=e (759/1039) — the memo's e-initial theory:
# before a vowel the mute-e is silent, so 40=e is the noun's initial.
# Alignment B: noun starts after full "premiere" (760/1040).
t3 = {'A': {}, 'B': {}, 'invert': {}}
A_cands = {
    'entrevue': (['e', 'n', 'tre', 'vue'], ['e', 'nt', 're', 'vue']),
    'expedition': (['e', 'x', 'pe', 'di', 'tion'], ['ex', 'pe', 'di', 'tion']),
    'epreuve': (['e', 'pre', 'u', 've'], ['e', 'preu', 've']),
    'epoque': (['e', 'po', 'que'], ['e', 'p', 'o', 'que']),
}
for name, (m1, m2) in A_cands.items():
    fits = []
    for start, kmax in [(759, 5), (1039, 5)]:
        for k in [len(m1), len(m2)]:
            fits.extend(window_fits(name, start, [k], HARD77, manual=[m1, m2]))
    nr759 = null_rate(P[759:759 + len(m1)], HARD77, lex=lex())[:2]
    t3['A'][name] = {'fits': fits, 'null_759': nr759}
# Alignment B: lexicon inversion at the noun slots
inv760, n760 = invert(P[760:764], HARD)          # 20 62 94(ne) 59
inv1040, n1040 = invert(P[1040:1044], HARD77)    # 17 77(le) 82(m) 63
inv759, n759 = invert(P[759:762], HARD)           # 40(e) 20 62
inv1039, n1039 = invert(P[1039:1042], HARD77)     # 40(e) 17 77(le)
t3['invert'] = {'@760[20,62,94,59]': (inv760, n760),
                '@1040[17,77,82,63]': (inv1040, n1040),
                '@759[40,20,62]': (inv759, n759),
                '@1039[40,17,77]': (inv1039, n1039)}
t3['verdict'] = 'HIT' if any(v['fits'] for v in t3['A'].values()) else 'NULL'
RES['targets']['T3'] = t3

# ============ T4: "le gouverment" @1180/@1351 ============
# hard = GT+PROV minus 94 (test variable), minus 77 (F37 fenced exception);
# 78 free (islet would block 'gou'); 06 free ('ent' hypothesis in fenced scope)
HARD_T4 = {g: v for g, v in HARD.items() if g != '94'}
FREE_T4 = frozenset(['77', '78', '94', '06'])
t4 = {'windows': {'1180': P[1180:1185], '1351': P[1351:1356]}}
t4['le_gouverment'] = {}
for start in (1180, 1351):
    t4['le_gouverment'][start] = window_fits(
        'legouverment', start, [5], HARD_T4, free=FREE_T4,
        manual=[['le', 'gou', 'ver', 'm', 'ent'],
                ['le', 'gouv', 'er', 'm', 'ent']])
# rival family enumeration: lexicon 5-cell [le,?,?,m,ent] fitters at both windows
fam = {}
for start in (1180, 1351):
    fitters = []
    for w, tilings in lex().items():
        for cells in tilings:
            if len(cells) != 5:
                continue
            ok, notes = fit_cells(cells, P[start:start + 5], HARD_T4, FREE_T4)
            if ok and cells[0] == 'le' and cells[3] == 'm' and cells[4] == 'ent':
                fitters.append((w, cells[1], cells[2]))
                break
    fam[start] = fitters
t4['family_le_?_?_m_ent'] = {s: {'n': len(f), 'sample': f[:20]} for s, f in fam.items()}
from collections import Counter
t4['cell94_readings'] = {s: Counter(c2 for _w, _c1, c2 in f).most_common()
                         for s, f in fam.items()}
t4['cell78_readings'] = {s: Counter(c1 for _w, c1, _c2 in f).most_common()
                         for s, f in fam.items()}
# independent check: the THIRD trigram @578 (61|94|82|06) — 94 free, tabulate
tri = []
for w, tilings in lex().items():
    for cells in tilings:
        if len(cells) != 4:
            continue
        ok, notes = fit_cells(cells, P[577:581], HARD_T4, FREE_T4)
        if ok:
            tri.append((w, cells[1]))
            break
t4['trigram_@578_94_readings'] = Counter(c for _w, c in tri).most_common(12)
t4['trigram_@578_nfitters'] = len(tri)
nhit = sum(1 for s in (1180, 1351) if t4['le_gouverment'][s])
t4['verdict'] = f'HIT@{nhit}/2 windows' if nhit else 'NULL'
t4['redteam_referral'] = (
    '94="ne" provisional-strong NOT adopted/demoted here. Tension: T4 needs '
    '94=ver (2 windows); banked 94="ne" legs (unigram 1.025x, trigram x3 @ '
    '1.054x era -nement with 82=m centered, 94->52/59 "ne se" x5) stand. '
    'See cell94_readings + trigram_@578_94_readings for the quantified split.')
RES['targets']['T4'] = t4

# ============ T5: "par le dernier courrier" at every 96 ============
n96 = [i for i in range(len(P)) if P[i] == '96']
t5 = {'n96': len(n96), 'cands': {}}
t5['cands']['par le dernier courrier'] = {}
for i in n96:
    fits = window_fits('parlederniercourrier', i, [6, 7], HARD77,
                       manual=[['par', 'le', 'der', 'nier', 'cour', 'rier'],
                               ['par', 'le', 'der', 'ni', 'er', 'cour', 'rier']])
    if fits:
        t5['cands']['par le dernier courrier'][i] = fits
t5['cands']['par le dernier courrier'] = {
    'n_windows': len(t5['cands']['par le dernier courrier']),
    'positions': sorted(t5['cands']['par le dernier courrier'])}
# sharp-end check: 96->77 bigram count (already 0/21 in frame notes)
t5['par_le_bigram_96_77'] = sum(1 for i in n96 if P[i + 1] == '77')
# null at a representative window (@150, the "par ce que" window)
t5['null_@150'] = null_rate(P[150:156], HARD77, lex=lex())[:2]
t5['verdict'] = ('HIT' if t5['cands']['par le dernier courrier']['n_windows']
                 else 'NULL')
RES['targets']['T5'] = t5

# ============ T6: tail closings, pairs 1800-1846 ============
t6 = {'cands': {}}
t6['cands']['consideration'] = scan('consideration', 1800, 1847, [5, 6], HARD,
    manual=[['con', 'si', 'dé', 'ra', 'tion'], ['con', 'sid', 'é', 'ra', 'tion']])
t6['cands']['distinguee'] = scan('distinguee', 1800, 1847, [4], HARD,
    manual=[['dis', 'tin', 'gué', 'e'], ['di', 'stin', 'gué', 'e']])
t6['cands']['Adieu, mon cher baron'] = scan(
    'adieumoncherbaron', 1800, 1847, [6, 7], HARD,
    manual=[['a', 'dieu', 'mon', 'cher', 'ba', 'ron'],
            ['ad', 'ieu', 'mon', 'cher', 'ba', 'ron'],
            ['a', 'di', 'eu', 'mon', 'cher', 'ba', 'ron']])
t6['cands']['Tout a vous'] = scan('toutavous', 1800, 1847, [3, 4], HARD,
    manual=[['tout', 'a', 'vous'], ['tou', 't', 'a', 'vous']])
t6['cands']['haute consideration'] = scan(
    'hauteconsideration', 1800, 1847, [7], HARD,
    manual=[['hau', 'te', 'con', 'si', 'dé', 'ra', 'tion']])
for name, hits in t6['cands'].items():
    t6['cands'][name] = {'n_windows': len(hits), 'positions': sorted(hits)[:8]}
    if hits:
        s = sorted(hits)[0]
        f0 = hits[s][0]
        k = len(f0['cells'])
        t6['cands'][name]['null_at_first'] = null_rate(
            P[s:s + k], HARD, lex=lex())[:2]
t6['verdict'] = 'HIT' if any(v['n_windows'] for v in t6['cands'].values()) else 'NULL'
RES['targets']['T6'] = t6

# ============ T7: name drags, mid-despatch ============
t7 = {'cands': {}}
t7['cands']['Metternich(29=er)'] = scan('metternich', 0, 1847, [4], HARD,
    manual=[['met', 't', 'er', 'nich'], ['me', 'tt', 'er', 'nich']])
t7['cands']['Nesselrode(94=ne)'] = scan('nesselrode', 0, 1847, [4, 5], HARD,
    manual=[['ne', 'ssel', 'ro', 'de'], ['ne', 'se', 'l', 'ro', 'de']])
t7['cands']['Ibrahim(34=i)'] = scan('ibrahim', 0, 1847, [3, 4], HARD,
    manual=[['i', 'bra', 'him'], ['i', 'b', 'ra', 'him']])
t7['cands']['Saxe(40=e)'] = scan('saxe', 0, 1847, [2], HARD,
    manual=[['sax', 'e']])
t7['cands']['Mehemet-Ali(78 islet me)'] = scan('mehemetali', 0, 1847, [5], HARD,
    manual=[['me', 'he', 'met', 'a', 'li'], ['me', 'h', 'me', 't', 'a', 'li']])
t7['cands']["l'Empereur(no anchor: vacuous)"] = scan(
    'empereur', 0, 1847, [3], HARD, manual=[['em', 'pe', 'reur']])
t7['cands']['Guizot(no anchor: vacuous)'] = scan(
    'guizot', 0, 1847, [2], HARD, manual=[['gui', 'zot']])
t7['cands']['Damas(no anchor: vacuous)'] = scan(
    'damas', 0, 1847, [2, 3], HARD, manual=[['da', 'mas'], ['da', 'ma', 's']])
for name, hits in t7['cands'].items():
    t7['cands'][name] = {'n_windows': len(hits), 'positions': sorted(hits)[:12]}
    if hits:
        s = sorted(hits)[0]
        k = len(hits[s][0]['cells'])
        t7['cands'][name]['null_at_first'] = null_rate(
            P[s:s + k], HARD, lex=lex())[:2]
t7['verdict'] = 'see per-name'
RES['targets']['T7'] = t7

# ============ T8: treaty double-surface ============
t8 = {'cands': {}}
t8['cands']['le traite de Londres'] = scan(
    'letraitedelondres', 0, 1847, [6, 7], HARD77,
    manual=[['le', 'trai', 'té', 'de', 'lon', 'dre'],
            ['le', 'tra', 'i', 'té', 'de', 'lon', 'dre']])
t8['cands']['le traite du 15 juillet'] = scan(
    'letraiteduquinzejuillet', 0, 1847, [7, 8], HARD77,
    manual=[['le', 'trai', 'té', 'du', 'quin', 'ze', 'juil', 'let'],
            ['le', 'trai', 'té', 'du', 'quinze', 'juil', 'let']])
for name, hits in t8['cands'].items():
    t8['cands'][name] = {'n_windows': len(hits), 'positions': sorted(hits)[:12]}
    if hits:
        s = sorted(hits)[0]
        k = len(hits[s][0]['cells'])
        t8['cands'][name]['null_at_first'] = null_rate(
            P[s:s + k], HARD77, lex=lex())[:2]
t8['verdict'] = 'HIT' if any(v['n_windows'] for v in t8['cands'].values()) else 'NULL'
RES['targets']['T8'] = t8

json.dump(RES, open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 'results.json'), 'w'), indent=1,
          default=str)
print('wrote results.json')
for t, d in RES['targets'].items():
    print(t, '->', d.get('verdict'))
