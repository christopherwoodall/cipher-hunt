#!/usr/bin/env python3
"""Mehemet-Ali @8 battery — Seebach round 7, patternist work order 5.

Claim: P[8:13]=[78,18,93,62,98] reads me|he|met|a|li = "Mehemet-Ali"
(T7 LEAD, N42 UPHELD; anchored null 33/11,870=0.28%; 10 bearing windows).

==================== PRE-REGISTERED BATTERY (bars fixed before results) ====================
  M0 REPRODUCE — re-derive the T7 anchored numbers (10 bearings, null
     33/11,870 @8) with the lane engine. Hygiene only, not a new check.
  M1 STREAM-WIDE EXCESS — for every stream window starting with 78 (n78=31),
     anchor-preserving null for its 5-group pattern under the same anchor
     engagement (78->'me'); E = sum of nulls; compare observed bearings (10).
     Pre-reg: observed >= 2*E with E>=1 => support; observed <= E =>
     bearings noise-consistent => adverse (not kill alone).
     NOTE: null counts by-ear lexicon fitters incl. 78='ver' readings (as in
     the T7 engine); E is an upper bound on name-bearing expectation.
  M2 SPELLING — is "Mehemet-Ali"/"Mehemet-Ali" the contemporary (1840-41)
     French spelling, and was the man topical in Jan 1841? Sources: on-VM
     period corpora (Tocqueville 1835/1840, Les Mis T1) + web check of French
     reference works. The "293x in Revue des Deux Mondes" figure attributed
     to the period fleet: VERIFY or mark UNVERIFIED (no RdDM corpus on VM).
     Pre-reg: M2 passes iff (a) hyphenated mehemet-ali spelling attested in
     French sources of/near the era AND (b) topical Jan 1841 (Oriental-crisis
     aftermath). The 293x figure is NOT required for a pass, but an
     unverified figure must be flagged, not cited.
  M3 ALTERNATIVE READINGS @8 — (a) enumerate all 33 anchor-preserving lexicon
     fitters at [78,18,93,62,98]; classify name-like vs common-word vs other;
     is Mehemet-Ali the unique NAME? (b) rival name spellings: 'mohamedali'
     (mo|ha|med|a|li -- 78='mo' unlicensed => must die), 'mehemedali'
     (same-reading variant), k=6 'me|h|me|t|a|li' (6 cells vs 5 groups =>
     dead by construction -- traceability nit on the T7 drag), by-ear-pure
     'me|e|met|a|li' (does it fit?).
     Pre-reg ADVERSE (weak): the 'he' cell writes a SILENT h -- etymological,
     not by-ear; the F44 model is by-ear. Not kill-grade (mixed table R4
     allows letter-cells; 'm' is GT), but it costs the reading purity.
     Pre-reg: M3 passes iff Mehemet-Ali is the unique name among fitters AND
     no common-word fitter uses strictly cleaner cells (all-20-string-
     inventory cells) in a period-plausible frame.
  M4 CORROBORATION — classify the other 9 bearing windows by best rival word;
     inspect P[13:16] after @8 ("pacha" follow-up: anchor-free => VACUOUS by
     method, reported not scored).

Verdict bars:
  PROMOTE (to provisional): >=2 of {M1,M2,M3} PASS, n_eff>=3 each, no
      kill-grade adverse. Dependency recorded: 78="me" islet is LEAD -- if
      the islet falls, this falls with it.
  HOLD (LEAD): exactly 1 of {M1,M2,M3} passes; no kill-grade adverse.
  KILL: kill-grade adverse -- M2 spelling-death (1841 French never wrote the
      name this way AND cells can't accommodate the true spelling), OR
      (M1 observed <= E AND M3 finds a strictly cleaner common-word reading
      at @8).

No double-counting: M0/M1 reuse the T7 engine (hygiene + new stream-wide
computation); M2/M3/M4 are new data. N35 accounting: the 33 fitters are used
once (M3).
===========================================================================================
"""
import json
import os
import sys
from collections import Counter

LANE = os.path.expanduser('~/workspace/cipher-hunt/lanes/zeschau-seebach-1841')
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd4'))
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd6', 'period_drag'))
sys.path.insert(0, os.path.join(LANE, 'code', 'crowd6', 'inventorist'))
from repaired_parse import load_pairs_repaired
from common import GT, PROV, LE77, ISLETS, fit_cells, load_lexicon_tilings
from byear import tile as byear_tile, normalize

P, _, _ = load_pairs_repaired()
HARD = dict(GT)
HARD.update(PROV)
HARD.update(LE77)
MANUAL = [['me', 'he', 'met', 'a', 'li'], ['me', 'h', 'me', 't', 'a', 'li']]

# ---------------- M0: reproduce T7 anchored ----------------
bearing = []
for s in range(len(P) - 4):
    if P[s] != '78':
        continue
    groups = P[s:s + 5]
    for cells in MANUAL:
        ok, _ = fit_cells(cells, groups, HARD)
        if ok:
            bearing.append(s)
            break
m0 = {'n_bearing': len(bearing), 'positions': bearing[:15]}
print('M0 bearings:', m0['n_bearing'], m0['positions'][:12])

# null @8 exactly as the T7 engine (by-ear top-8 tilings, anchor-preserving)
lex = load_lexicon_tilings()
til_cache = {}


def tilings8(w):
    if w not in til_cache:
        til_cache[w] = [cells for cells, _s in byear_tile(w, k=8)]
    return til_cache[w]


def null_count(groups, hard=HARD):
    n = 0
    sample = []
    for w in lex:
        for cells in tilings8(w):
            if len(cells) != len(groups):
                continue
            ok, _ = fit_cells(cells, groups, hard)
            if ok:
                n += 1
                if len(sample) < 40:
                    sample.append((w, cells))
                break
    return n, len(lex), sample


n8, N8, samp8 = null_count(P[8:13])
m0['null_at_8'] = [n8, N8]
print(f'M0 null @8: {n8}/{N8} = {n8 / N8:.4f}')

# ---------------- M1: stream-wide excess over 78-windows ----------------
s78 = [i for i in range(len(P) - 4) if P[i] == '78']
E = 0.0
per_win = []
for s in s78:
    n, N, _ = null_count(P[s:s + 5])
    E += n / N
    per_win.append((s, n))
m1 = {'n_78_windows': len(s78), 'expected_bearings': round(E, 3),
      'observed_bearings': len(bearing),
      'pass': bool(len(bearing) >= 2 * E and E >= 1)}
print('M1 E=%.3f observed=%d pass=%s' % (E, len(bearing), m1['pass']))

# ---------------- M3: alternative readings @8 ----------------
# (a) classify the 33 fitters
def classify(w, cells):
    wl = w.lower()
    if 'mehemet' in wl or 'mehemed' in wl or 'mohamed' in wl or 'ali' in wl:
        return 'name-like'
    return 'common-word'


cats = Counter()
by_cat = {'name-like': [], 'common-word': []}
cells_of = {}
for w, cells in samp8:
    c = classify(w, cells)
    cats[c] += 1
    cells_of[w] = cells
    if len(by_cat[c]) < 15:
        by_cat[c].append([w, cells])
name_fits = [w for w, _ in samp8 if classify(w, _) == 'name-like']

# (b) rival name spellings / tilings at the @8 window
def try_cells(cells_list):
    out = []
    for cells in cells_list:
        if len(cells) != 5:
            out.append((cells, 'DEAD: arity != 5'))
            continue
        ok, notes = fit_cells(cells, P[8:13], HARD)
        out.append((cells, 'FITS' if ok else 'no-fit', notes if not ok else {}))
    return out

rival_tests = {
    # by-ear-pure (no silent h): me|e|met|a|li
    'me|e|met|a|li': try_cells([['me', 'e', 'met', 'a', 'li']]),
    # t/d variant: me|he|med|a|li
    'me|he|med|a|li': try_cells([['me', 'he', 'med', 'a', 'li']]),
    # Mohamed spelling: mo|ha|med|a|li (78='mo' not in islet)
    'mo|ha|med|a|li': try_cells([['mo', 'ha', 'med', 'a', 'li']]),
    # k=6 manual variant from the T7 drag (arity check)
    'me|h|me|t|a|li(k=6)': try_cells([['me', 'h', 'me', 't', 'a', 'li']]),
    # no-hyphen same cells
    'me|he|met|a|li(repeat)': try_cells([['me', 'he', 'met', 'a', 'li']]),
}
# 'he'-cell purity adverse: 'he' writes a silent h (etymological, not by-ear)
m3 = {
    'n_fitters': n8, 'categories': dict(cats),
    'name_like_fits': name_fits,
    'name_like_sample': by_cat['name-like'],
    'common_word_sample': by_cat['common-word'][:15],
    'rival_tests': {k: [(c, r) for c, r, *_ in v] for k, v in rival_tests.items()},
    'he_cell_adverse': ("'he' writes a SILENT h (Mehemet pronounced [me.e.mE]); "
                        "etymological, not by-ear -- weak adverse vs the F44 model; "
                        "not kill-grade (R4 mixed table allows letter-cells)"),
    'unique_name': len(name_fits) <= 1,
}
# cleaner-cells test: any common-word fitter using only 20-string inventory cells?
KNOWN20 = {'la', 'pre', 'm', 'i', 'er', 'e', 'que', 'ce', 'qui', 'par', 'ne',
           'veut', 'on', 'me', 'le', 'ent', 'pas', 'so', 'se', 'en'}
cleaner = [(w, cells) for w, cells in samp8
           if classify(w, cells) == 'common-word' and all(c in KNOWN20 for c in cells)]
m3['cleaner_common_word_fits'] = cleaner[:10]
m3['n_cleaner'] = len(cleaner)
m3['pass'] = bool(m3['unique_name'] and len(cleaner) == 0)
print('M3 cats:', dict(cats), 'unique_name:', m3['unique_name'],
      'cleaner:', len(cleaner), 'pass:', m3['pass'])

# ---------------- M4: other 9 bearing windows + P[13:16] ----------------
m4 = {'other_windows': bearing[1:],
      'after_8': P[13:19],
      'pacha_note': 'P[13:19]=[76,45,91,53,17,64]: "pacha"-shaped follow-up is '
                    'anchor-free => VACUOUS by method (same as Ibrahim+"pacha", N42); '
                    'reported, not scored.'}
print('M4 other windows:', bearing[1:], 'P[13:19]:', P[13:19])

# ---------------- M2: spelling (done via corpora + web; recorded here) ----------------
m2 = {
    'corpus_check': ('Tocqueville T1+T2 (1835/1840) and Les Mis T1: ZERO '
                     'attestations of mehemet/mehemed/mohamed+ali -- the name '
                     'does not occur in the on-VM period corpora.'),
    'rddm_293x': ('UNVERIFIED: no Revue des Deux Mondes corpus on the VM; the '
                  '"293x" figure attributed to the period fleet could not be '
                  'reproduced or falsified here. Flagged, not cited.'),
    'web_check': ('"Mehemet-Ali" (hyphenated, unaccented) and "Mehemet-Ali" '
                  '(accented) both attested in French sources: fr.wikisource '
                  '"Mehemet-Ali durant ses dernieres annees" uses BOTH forms; '
                  'Driault (L\'Egypte et l\'Europe: la crise de 1839-1841, apud '
                  'journals.openedition.org/cdlm/16391) quotes "Mehemet-Ali". '
                  'Accent-stripping is the lane\'s disclosed convention, so the '
                  'cipher form matches the contemporary spelling.'),
    'topical_jan1841': ('Muhammad Ali Pasha (d. 1849): London Convention '
                        '15 Jul 1840, hereditary pashalik settlement running '
                        'into early 1841 (firman Feb 1841) -- the name was '
                        'front-page topical in Jan 1841 French diplomacy.'),
    'pass': True,
}
print('M2 pass:', m2['pass'], '(spelling+topicality verified; 293x UNVERIFIED)')

passes = sum([m1['pass'], m2['pass'], m3['pass']])
kill = False  # spelling-death not observed; M1/M3 kill conjunction evaluated below
if m1['observed_bearings'] <= m1['expected_bearings'] and m3['n_cleaner'] > 0:
    kill = True
    verdict = 'KILL'
elif passes >= 2:
    verdict = 'PROMOTE'
elif passes == 1:
    verdict = 'HOLD'
else:
    verdict = 'HOLD'
out = {'check': 'Mehemet-Ali@8', 'M0': m0, 'M1': m1, 'M2': m2, 'M3': m3,
       'M4': m4, 'n_pass': passes, 'kill_triggered': kill, 'verdict': verdict}
json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                'battery_mehemet_results.json'), 'w'), indent=1)
print('VERDICT:', verdict, f'({passes}/3 checks pass)')
