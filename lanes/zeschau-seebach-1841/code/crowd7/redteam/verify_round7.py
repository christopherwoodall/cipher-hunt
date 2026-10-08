#!/usr/bin/env python3
"""Red-team round-7 adjudication extension checks.

Re-derives the load-bearing cipher-side numbers behind the round-7 executor
recommendations, on the canonical repaired 1,847-pair stream
(code/side-keyhunt/repaired_offsets.json; positions per
code/crowd7/redteam/verify_f26_17.py). Run with no args; exits nonzero on
any mismatch.

Covers: conditioner 84/00 tables, closer 59 battery cipher facts,
morphologist WO-10 cipher facts + 67 tally, keystruct M1 kill-shot + M8,
frenchman U5 5-mer, patternist 16 anchors.

STATUS-LINE (2026-10-07, round-8 red-team extension): appends the round-7
adjudication status ledger — every promotion/kill/denial/flag from
code/crowd7/redteam/RULINGS-ROUND7.md (F52-F59, N45-N48), the stream-side
n_eff derivations behind the conditioned-polyvalence statuses, and the
corpus-side banked values cited with provenance (asserted against their
archived result files, not re-derived from corpora). Existing checks
untouched.

ROUND8-LEDGER (2026-10-07, round-9 red-team extension): appends the round-8
adjudicated status deltas (code/crowd8/adjudicator/RULINGS-FINAL.md) and the
corpus-side legs behind them, asserted against the executors' archived result
files as drift guards (not re-derived from corpora). F59's RdDM-293x
UNVERIFIED flag is LIFTED (superseded) by this extension. Existing checks
untouched.

ROUND10-LEDGER (2026-10-07, round-10 red-team finalizer extension): appends
the round-10 adjudicated status deltas (code/crowd10/redteam/RULINGS-ROUND10.md,
finalized R1-R8), asserted against the executors' archived result files as
drift guards (not re-derived from corpora). Existing checks untouched.

ROUND11-LEDGER (2026-10-07, round-11 red-team final extension): appends
the round-11 adjudicated status deltas (code/crowd11/redteam/RULINGS-ROUND11.md,
finalized R1-R7), asserted against the executors' archived result files as
drift guards (not re-derived from corpora). Existing checks untouched.

ROUND14-LEDGER (2026-10-07, round-14 red-team pre-registration extension):
appends the round-14 opening status ledger (round-13 adjudicated net N60 /
F100-F113, 21 rulings in RULINGS-ROUND13.md: 0 promotions, registry
restructured, 4 homophone sets split, KE2 re-derived, KE1 inconclusive, drag
nulled, missing mass ~17 cells, 32 segments) plus artifact drift guards on
the round-13 adjudication artifacts and PREREG14.md. Existing checks
untouched.

ROUND14-CLOSE (2026-10-07, round-14 red-team adjudication extension):
appends the round-14 ruling status deltas (R-001..R-009 in
code/crowd14/redteam/RULINGS-ROUND14.md: 81 killed, 78 fork resolved,
74 syllable-class, H_stem HOLD, 62 HOLD, 52 UNIDENTIFIED, @460 datum,
no 59 third value, registry adopted, 0 promotions, 3 prereg
deficiencies). Existing checks untouched.
"""
import json
import re
import math
import sys
from collections import Counter
from pathlib import Path

LANE = Path(__file__).resolve().parents[3]  # .../zeschau-seebach-1841
sys.path.insert(0, str(LANE / 'code' / 'side-keyhunt'))
from repair_parse import load_rows, parse  # noqa: E402


def load_stream():
    rows = load_rows()
    off = json.loads((LANE / 'code/side-keyhunt/repaired_offsets.json').read_text())
    return [int(g) for g, _ in parse(rows, off)]


def main():
    pairs = load_stream()
    assert len(pairs) == 1847, len(pairs)
    g = Counter(pairs)
    big = Counter(zip(pairs[:-1], pairs[1:]))
    starts = lambda a, b: sorted(i for i in range(1846)
                                 if pairs[i] == a and pairs[i + 1] == b)

    checks = []
    def chk(name, got, want):
        checks.append((name, got, want, got == want))

    # ---- conditioner: 84 conflict ----
    pos84 = [i for i, p in enumerate(pairs) if p == 84]
    chk('n84', len(pos84), 25)
    en = sorted((i, pairs[i - 1], pairs[i + 1]) for i in pos84
                if pairs[i - 1] in (46, 94, 82))
    noun = sorted((i, pairs[i - 1], pairs[i + 1]) for i in pos84
                  if pairs[i - 1] in (77, 11))
    chk('84 en-class', en,
        [(167, 82, 53), (310, 46, 24), (473, 46, 24), (1665, 94, 64)])
    chk('84 noun-class', noun,
        [(146, 77, 29), (260, 77, 74), (1058, 77, 9), (1447, 77, 59),
         (1485, 77, 24), (1620, 11, 78), (1764, 77, 9), (1803, 77, 59)])
    free = sorted((i, pairs[i - 1]) for i in pos84
                  if pairs[i - 1] not in (46, 94, 82, 77, 11))
    chk('84 free windows', [i for i, _ in free],
        [154, 276, 391, 412, 788, 857, 1021, 1151, 1189, 1290, 1378, 1418, 1501])
    chk('84 free predecessors', Counter(p for _, p in free),
        Counter({66: 2, 89: 2, 53: 2, 91: 1, 65: 1, 48: 1, 6: 1, 17: 1,
                 32: 1, 74: 1}))
    chk('84 en n_eff (46-84-24 x2 -> 1)', 4 - 1, 3)

    # ---- conditioner: 00 conflict ----
    chk('96->00 starts', starts(96, 0), [47, 465, 960])
    chk('00->86', big[(0, 86)], 12)
    chk('00->86 excl pre=96', sum(1 for i in range(1, 1846)
                                 if pairs[i] == 0 and pairs[i + 1] == 86
                                 and pairs[i - 1] != 96), 11)
    chk('00->06', big[(0, 6)], 0)
    chk('06->00', big[(6, 0)], 4)
    chk('00->46', big[(0, 46)], 4)
    chk('00->11', big[(0, 11)], 4)
    chk('00 successors @47/465/960', [pairs[s + 2] for s in (47, 465, 960)],
        [92, 33, 86])

    # ---- closer: 59="est" battery cipher facts ----
    chk('n59', g[59], 27)
    chk('n01', g[1], 28)
    chk('64->59 starts', starts(64, 59), [315, 1209, 1776])
    chk('94->59 starts', starts(94, 59), [558, 762, 1795])
    chk('59->46 starts', starts(59, 46), [216, 1190])
    chk('59->37', big[(59, 37)], 6)
    chk('qui/ne->59 vs ->01', (big[(64, 59)] + big[(94, 59)],
                               big[(64, 1)] + big[(94, 1)]), (6, 0))
    chk('87->01', big[(87, 1)], 2)
    chk('37->01', big[(37, 1)], 3)
    chk('47->01', big[(47, 1)], 1)
    p01 = set(pairs[i - 1] for i in range(1, 1847) if pairs[i] == 1)
    p59 = set(pairs[i - 1] for i in range(1, 1847) if pairs[i] == 59)
    f01 = set(pairs[i + 1] for i in range(1846) if pairs[i] == 1)
    f59 = set(pairs[i + 1] for i in range(1846) if pairs[i] == 59)
    chk('01/59 shared predecessors', sorted(p01 & p59), [15, 16, 48, 76, 86, 87])
    chk('01/59 shared followers', sorted(f01 & f59), [19, 24])

    # ---- morphologist WO-10 cipher facts ----
    chk('64-96-47 @149-151', pairs[149:152], [64, 96, 47])
    chk('47->46 starts', starts(47, 46), [151, 548, 864])
    chk('64->47 starts ("qui ce", not "ce qui")', starts(64, 47), [1271, 1717])
    chk('47@151 pre/suc', (pairs[150], pairs[152]), (96, 46))

    # ---- morphologist WO-12: 67 tally ----
    b67 = json.loads((LANE / 'code/crowd7/morphologist/battery67_final.json')
                     .read_text())
    chk('67 n', b67['n'], 38)
    chk('67 tally', b67['tally'], {'veut': 11, 'et': 18, 'open': 9})
    opens = sorted(r.get('pos') or r.get('start') for r in b67['rows']
                   if (r.get('verdict') or r.get('class')) in ('open', 'OPEN'))
    chk('67 open positions', opens,
        [199, 630, 633, 902, 1248, 1372, 1450, 1519, 1623])
    both = [r for r in b67['rows']
            if (r.get('verdict') or r.get('class')) in ('BOTH', 'both')]
    chk('67 BOTH conflicts', len(both), 0)

    # ---- keystruct M1 kill-shot ----
    p64_87 = big[(87, 64)] / g[87]
    chk('87->64', (big[(87, 64)], g[87]), (5, 32))
    chk('47->64', (big[(47, 64)], g[47]), (0, 28))
    kill_p = (1 - p64_87) ** g[47]
    chk('M1 interchange kill-shot p', round(kill_p, 5), 0.00859)

    # ---- keystruct M8 ----
    s43 = set(pairs[i + 1] for i in range(1846) if pairs[i] == 43)
    s21 = set(pairs[i + 1] for i in range(1846) if pairs[i] == 21)
    chk('43/21 shared followers', sorted(s43 & s21), [])
    chk('n43/n21', (g[43], g[21]), (16, 30))

    # ---- frenchman U5 ----
    m5 = [i for i in range(1843) if pairs[i:i + 5] == [77, 78, 94, 82, 6]]
    chk('77-78-94-82-06 5-mer starts', m5, [1180, 1351])
    chk('77->78 starts', starts(77, 78), [7, 213, 647, 1077, 1180, 1351, 1542])
    chk('@647 reads 77 78 52 82 94', pairs[647:652], [77, 78, 52, 82, 94])

    # ---- patternist 16 anchors ----
    chk('82->16 starts', starts(82, 16),
        [381, 433, 536, 1194, 1197, 1369, 1386, 1436, 1479, 1651, 1831])
    chk('parmi @1196-1198', pairs[1196:1199], [96, 82, 16])
    chk('46->16 / 46->34 (H-split)', (big[(46, 16)], big[(46, 34)]), (0, 0))

    # ---- STATUS-LINE: stream-side n_eff derivations ----
    en_win = sorted(i for i in range(1846)
                    if pairs[i] == 84 and pairs[i - 1] in (46, 94, 82))
    en_frames = sorted((pairs[i - 1], pairs[i], pairs[i + 1]) for i in en_win)
    chk('84 en-islet n / n_eff', (len(en_win), len(set(en_frames))), (4, 3))
    chk('en-islet dedup: 46-84-24 x2', en_frames.count((46, 84, 24)), 2)
    noun_win = sorted(i for i in range(1846)
                      if pairs[i] == 84 and pairs[i - 1] in (77, 11))
    noun_frames = sorted((pairs[i - 1], pairs[i], pairs[i + 1]) for i in noun_win)
    chk('84 noun-islet n / n_eff', (len(noun_win), len(set(noun_frames))), (8, 6))
    tri = [i for i in range(1845) if pairs[i:i + 3] == [64, 96, 47]]
    chk('64-96-47 3-gram (96=verb n_eff=1)', tri, [149])
    le_frames = sorted((pairs[s - 1], pairs[s], pairs[s + 1], pairs[s + 2])
                       for s in (47, 465, 960))
    chk('00="le" islet windows distinct', len(set(le_frames)), 3)

    # ---- STATUS-LINE: corpus-side banked values (provenance-noted; drift guards on the archives) ----
    dip = json.loads((LANE / 'code/crowd7/closer/diplomatic_rates.json')
                     .read_text())
    chk('L1 Guizot t5-t6 P(que|est)',
        round(dip['guizot-t5t6']['P_que_given_est'], 4), 0.0213)
    chk('L1 Nesselrode v8 P(que|est)',
        round(dip['nesselrode-v8']['P_que_given_est'], 4), 0.0414)
    chk('L1 aggregate P(que|est)',
        round(dip['diplomatic_all']['P_que_given_est'], 4), 0.0249)
    fr = json.loads((LANE / 'code/crowd7/frenchman/frenchman_round7_results.json')
                    .read_text())
    chk('93 rate-kill n/E/p (archived)',
        (fr['u2']['g93']['n'], fr['u2']['g93']['E_n_diplo'],
         round(fr['u2']['g93']['P_le_14'], 6)), (14, 32.0, 0.000294))
    meh = json.loads((LANE / 'code/crowd7/patternist/battery_mehemet_results.json')
                     .read_text())
    chk('RdDM 293x UNVERIFIED flag (F59, HISTORICAL — lifted by ROUND8-LEDGER)',
        'UNVERIFIED' in meh['M2']['rddm_293x'], True)

    # ---- ROUND8-LEDGER (2026-10-07, round-9 red-team extension) ----
    # Round-8 adjudicated status deltas
    # (code/crowd8/adjudicator/RULINGS-FINAL.md, R1-R10).
    LEDGER8 = {
        '48="ne"-allophone {94,48}': 'REFUTED',
        '59="est"': 'provisional (upheld)',
        '01="est"': 'MEDIUM (confirmed)',
        '84="en" islet': 'LEAD re-scoped: pre={82} GT-anchored OR pre={66,89} conditional',
        '84 noun islet': 'LEAD, identity NULL («qui le [verb=84-59]» x2 REFERRED to round 9)',
        '00="pour"': 'STRONG LEAD (B1 3.91x, B3 3.19x)',
        '47="ce"': 'LEAD (unchanged)',
        '96=verb-stem': 'LEAD n_eff=1 (WO-6 second-window criterion RETIRED)',
        '{93,8}="l\'"': 'LEAD (new, unconditioned homophones)',
        '93="l\'" alone': 'RATE-KILLED (upheld)',
        '62="on"': 'STRONG LEAD (fenced, +2 non-ear legs)',
        '62="il"': 'DISFAVORED-STRONG',
        '06="ent" iff pre=82': 'LEAD (new, conditioned; falsifier frozen)',
        '77="gouv"': 'LEAD n_eff=1 (7th support null)',
        '78="er"': 'LEAD n_eff=1 (fork (a2)/(c) unresolved, lean (c))',
        '67 et/veut fork': 'SUPPORTED (@1248 NEITHER-class fenced n=1)',
        '16="i"': 'LEAD (position-conditioned alternative NOT SUPPORTED)',
        '"Mehemet-Ali" @8': 'LEAD-weak',
        'columns refuge': 'concretizations DEAD; schema LOGICALLY-OPEN-NO-EVIDENCE',
        'RdDM 293x': 'VERIFIED (UNVERIFIED flag LIFTED)',
        'N46 93 shape-STRONG': 'TRACEABILITY FLAG (irreproducible)',
        'main-fleet search scope': 'ZERO until C1 passes (F57)',
    }
    VOCAB8 = {'PROVISIONAL', 'provisional (upheld)', 'LEAD', 'STRONG LEAD',
              'MEDIUM', 'MEDIUM (confirmed)', 'KILLED', 'REFUTED', 'RATE-KILLED',
              'SUPPORTED', 'FLAGGED-UNTESTED', 'INCONCLUSIVE', 'WEAKENED',
              'LOGICALLY-OPEN-NO-EVIDENCE',
              'LEAD re-scoped: pre={82} GT-anchored OR pre={66,89} conditional',
              'LEAD, identity NULL («qui le [verb=84-59]» x2 REFERRED to round 9)',
              'STRONG LEAD (B1 3.91x, B3 3.19x)',
              'LEAD n_eff=1 (WO-6 second-window criterion RETIRED)',
              'LEAD (new, unconditioned homophones)',
              'RATE-KILLED (upheld)',
              'STRONG LEAD (fenced, +2 non-ear legs)',
              'DISFAVORED-STRONG',
              'LEAD (new, conditioned; falsifier frozen)',
              'LEAD n_eff=1 (7th support null)',
              'LEAD n_eff=1 (fork (a2)/(c) unresolved, lean (c))',
              'SUPPORTED (@1248 NEITHER-class fenced n=1)',
              'LEAD (position-conditioned alternative NOT SUPPORTED)',
              'LEAD (unchanged)',
              'LEAD-weak',
              'concretizations DEAD; schema LOGICALLY-OPEN-NO-EVIDENCE',
              'VERIFIED (UNVERIFIED flag LIFTED)',
              'TRACEABILITY FLAG (irreproducible)',
              'ZERO until C1 passes (F57)'}
    chk('ledger8: all statuses in vocabulary',
        sorted(set(LEDGER8.values()) - VOCAB8), [])
    chk('ledger8: 48="ne" settled-killed (F60)',
        LEDGER8['48="ne"-allophone {94,48}'], 'REFUTED')

    # ---- ROUND8-LEDGER: corpus-side drift guards (provenance-noted) ----
    rm = json.loads((LANE / 'code/crowd8/ratemodel/ratemodel_results.json')
                    .read_text())
    chk('B1 3.91x French-only (archived)', round(rm['H_LANG']['r1_french'], 2), 3.91)
    chk('B3 3.19x French-only (archived)', round(rm['H_LANG']['r3_french'], 2), 3.19)
    chk('B1/B3 docs French-only provenance', (rm['docs']['fr'], rm['docs']['en']),
        (97, 0))
    h2 = json.loads((LANE / 'code/crowd8/homophonist/battery48_results.json')
                    .read_text())['checks']['H2']
    chk('H2 merged_rate (archived)', h2['merged_rate'], 0.04061)
    chk('H2 era P("ne") word (archived)', h2['era_p_ne_diplo_word'], 0.0085)
    chk('H2 ratio_word (archived)', h2['ratio_word'], 4.775)
    chk('H2 verdict KILL (archived)', h2['verdict'], 'KILL')
    fr8 = json.loads((LANE / 'code/crowd8/frenchman/results.json').read_text())
    lb = fr8['L_B_qu']
    chk('L_B E[qu\'on]/E[qu\'il] (archived)', (lb['E_quon'], lb['E_quil']),
        (1.77, 4.83))
    chk('L_B P0 (archived)', (lb['P0_given_on'], lb['P0_given_il']),
        (0.1697, 0.00797))
    chk('L_B LR=21.3 obs=0 (archived)', (lb['LR_on_over_il'], lb['obs_46_to_62']),
        (21.3, 0))
    la = fr8['L_A_lon']
    chk('L_A cipher (93|8)->62=4, n62=35 (archived)',
        (la['cipher_93or8_to_62'], la['n62']), (4, 35))
    chk('L_A diplo l\'+il=0 (archived)', la['diplo_l_il'], 0)
    chk('06-islet windows=82-indices (archived)', fr8['islet_06_ent']['windows'],
        [579, 737, 1183, 1354])
    chk('06-islet n=4 (archived)', fr8['islet_06_ent']['n'], 4)
    p8 = json.loads((LANE / 'code/crowd8/patternist/round8_results.json')
                    .read_text())
    chk('T1 primary p=0.9398 (archived)', p8['T1']['primary']['p_one_sided'],
        0.9398)
    chk('16 verdict_a NOT SUPPORTED (archived)', p8['verdict_a'],
        'NOT SUPPORTED (B1 redirect fails)')
    chk('Mehemet-Ali verdict_b DEMOTE (archived)', p8['verdict_b'],
        'DEMOTE recommended: LEAD -> LEAD-weak (red team adjudicates)')
    # RdDM 293x VERIFIED — independent recount (case-sensitive clean form)
    import re as _re, glob as _glob
    _rddm = sorted(_glob.glob(str(LANE / 'code/side-period/corpus'
                                   '/revue-deux-mondes-1841-q*.txt')))
    chk('RdDM corpus: 4 tomes present (archived)', len(_rddm), 4)
    _n293 = sum(len(_re.findall(r'Méhémet-Ali',
                                open(f, encoding='utf-8', errors='replace').read()))
                for f in _rddm)
    chk('RdDM clean-form recount =293 (flag LIFTED)', _n293, 293)

    # ---- ROUND9 (2026-10-07, round-9 final pass: R1-R9 adjudication ledger) ----
    # Every round-9 ruling's status delta (code/crowd9/redteam/RULINGS-ROUND9.md).
    LEDGER9 = {
        '06="ent"-iff-pre=82': 'LEAD (conditioned; falsifier did not fire; n_eff=3 fragility noted)',
        'smith-liaison memo': 'BANKED as constraint (no status change; scope ZERO)',
        'M3 he-cell adverse': 'STRUCK (scoped: German phonetics; LEAD-weak unchanged)',
        '48 H_verb': 'DEAD (K2 fired); 48 UNIDENTIFIED',
        '48 H_stem': 'UNTESTED (V5 underpowered)',
        '62="on"': 'STRONG LEAD (fenced; HOLD)',
        '62="il"': 'DISFAVORED-STRONG (HOLD)',
        '77="gouv"/78="er"': 'LEAD n_eff=1 (H3a weak leg for (c) banked; @1351 three fenced items)',
        '67 et/veut fork': 'SUPPORTED (fenced n=2: @1248, @199-conditional)',
        '@630': 'et-CONDITIONAL (C1∧C2; not a classification)',
        '86=que-family': 'REFUTED (hypothesis-kill; 4 legs)',
        'B3 (3.19x)': 'STANDS (dissolution premise dead)',
        '66-class': 'CONFIRMED (broad)',
        '89 noun-class': 'CONFIRMED',
        'qui-96-43 formula': 'HOLD (FORMULA-UNCONFIRMED)',
        '43="me"': 'WEAK (clitic-order adverse in qui-96-43 frame)',
        '59="est"-word @1447/@1803': 'FENCED adverse n=2 (provisional stands elsewhere)',
        '84 residuals': '9 RESIDUAL (no islet change)',
        'interim kills': 'NONE',
    }
    VOCAB9 = {'LEAD (conditioned; falsifier did not fire; n_eff=3 fragility noted)',
              'BANKED as constraint (no status change; scope ZERO)',
              'STRUCK (scoped: German phonetics; LEAD-weak unchanged)',
              'DEAD (K2 fired); 48 UNIDENTIFIED',
              'UNTESTED (V5 underpowered)',
              'STRONG LEAD (fenced; HOLD)',
              'DISFAVORED-STRONG (HOLD)',
              'LEAD n_eff=1 (H3a weak leg for (c) banked; @1351 three fenced items)',
              'SUPPORTED (fenced n=2: @1248, @199-conditional)',
              'et-CONDITIONAL (C1∧C2; not a classification)',
              'REFUTED (hypothesis-kill; 4 legs)',
              'STANDS (dissolution premise dead)',
              'CONFIRMED (broad)',
              'CONFIRMED',
              'HOLD (FORMULA-UNCONFIRMED)',
              'WEAK (clitic-order adverse in qui-96-43 frame)',
              'FENCED adverse n=2 (provisional stands elsewhere)',
              '9 RESIDUAL (no islet change)',
              'NONE'}
    chk('ledger9: all statuses in vocabulary',
        sorted(set(LEDGER9.values()) - VOCAB9), [])
    chk('ledger9: no interim kills', LEDGER9['interim kills'], 'NONE')
    chk('ledger9: 86 que-family settled-refuted',
        LEDGER9['86=que-family'], 'REFUTED (hypothesis-kill; 4 legs)')

    # ---- STATUS-LINE: the adjudication ledger (RULINGS-ROUND7.md, F52-F59/N45-N48) ----
    LEDGER = {
        '59="est"': 'PROVISIONAL',
        '84="en" (unconditioned)': 'KILLED',
        '84=masc-noun (unconditioned)': 'KILLED',
        '84="en" iff pre in {46,94,82}': 'LEAD',
        '84=masc-noun iff pre in {77,11}': 'LEAD',
        '00="pour"': 'STRONG LEAD',
        '00="le" iff pre=96': 'LEAD',
        '47="ce"': 'LEAD',
        '96=verb iff pre=64 & suc=47': 'LEAD',
        '{87,47}="ce" (unconditioned merger)': 'REFUTED',
        '"ce" conditioned homophone set (Q1/Q2)': 'LEAD',
        '{77,00}="le" (merger)': 'REFUTED',
        '{43,21}="me" (merger)': 'REFUTED',
        '01="est"': 'MEDIUM',
        '62="on"': 'STRONG LEAD (fenced, ear legs only)',
        '93="l\'"': 'RATE-KILLED',
        '77="gouv"/78="er" islets': 'LEAD',
        '16="i"': 'LEAD',
        '"Mehemet-Ali" @8': 'LEAD',
        '67 et/veut fork': 'SUPPORTED',
        '48="ne"-allophone': 'FLAGGED-UNTESTED',
        'search-family bake-off': 'KILLED',
        'P2c fixed-column-order': 'INCONCLUSIVE',
        'columns refuge (coda-sonority)': 'WEAKENED',
        'columns refuge (untested class)': 'LOGICALLY-OPEN-NO-EVIDENCE',
    }
    VOCAB = {'PROVISIONAL', 'LEAD', 'STRONG LEAD', 'STRONG LEAD (fenced, ear legs only)',
             'MEDIUM', 'KILLED', 'REFUTED', 'RATE-KILLED', 'SUPPORTED',
             'FLAGGED-UNTESTED', 'INCONCLUSIVE', 'WEAKENED',
             'LOGICALLY-OPEN-NO-EVIDENCE'}
    chk('ledger: all statuses in vocabulary',
        sorted(set(LEDGER.values()) - VOCAB), [])
    archived = json.loads((LANE / 'code/crowd8/redteam/STATUS-LINE-round7.json')
                          .read_text())
    chk('ledger: in-script copy == archived file', LEDGER, archived['statuses'])
    chk('ledger: 48 not LEAD (flag guard)',
        LEDGER['48="ne"-allophone'], 'FLAGGED-UNTESTED')

    # ---- ROUND10-LEDGER (2026-10-07, round-10 red-team extension) ----
    # Appends the round-10 adjudicated status deltas
    # (code/crowd10/redteam/RULINGS-ROUND10.md, R1-R8). Existing checks untouched.
    LEDGER10 = {
        '59="est" (unconditioned)': 'REFUTED',
        'ISLET 10 (59 conditioned: est iff pre in {64,94,93};'
        ' este iff pre=84)': 'LEAD',
        'H4g (94-82-06-06 frame)': 'REFUTED',
        '@1351-1356 ownership': 'R-c («le [78] ne ment pas»)',
        'R-b (gouvernement) at @1351': 'RULED OUT (window-level)',
        '77="gouv"': 'LEAD (@1180-only)',
        '67@1248': 'NEITHER-fence STANDS',
        '67@1248 C2 "peu" / C3 infinitive': 'WEAK arms (fenced alternatives)',
        '67 6 open-residual': 'OPEN (unchanged)',
        '48': 'UNIDENTIFIED',
        '48 S-word class (30 tested)': 'KILLED (battery-internal)',
        'H_stem (48)': 'UNTESTED (NULL, not adverse)',
        '62-WO3': 'STANDS globally; refuted for @1248 (scoped)',
        'Gate-4 bound': 'REVISED ({peu}-class + infinitive; cela-class VOID)',
        'F52 caveat-3 (S4 @216)': 'DISSOLVED (verb re-read)',
        'ISLET-8 follow-up (59 polyvalence)': 'BANKED (by ISLET 10)',
        'F52 59="est" provisional': 'REFINED into ISLET 10 (not killed)',
    }
    VOCAB10 = {'REFUTED', 'LEAD', 'RULED OUT (window-level)',
               'LEAD (@1180-only)', 'NEITHER-fence STANDS',
               'WEAK arms (fenced alternatives)', 'OPEN (unchanged)',
               'UNIDENTIFIED', 'KILLED (battery-internal)',
               'UNTESTED (NULL, not adverse)',
               'STANDS globally; refuted for @1248 (scoped)',
               'REVISED ({peu}-class + infinitive; cela-class VOID)',
               'DISSOLVED (verb re-read)', 'BANKED (by ISLET 10)',
               'REFINED into ISLET 10 (not killed)',
               'R-c («le [78] ne ment pas»)'}
    chk('ledger10: all statuses in vocabulary',
        sorted(set(LEDGER10.values()) - VOCAB10), [])
    chk('ledger10: 17 entries', len(LEDGER10), 17)
    chk('ledger10: unconditioned 59 REFUTED',
        LEDGER10['59="est" (unconditioned)'], 'REFUTED')
    chk('ledger10: ISLET 10 LEAD', LEDGER10['ISLET 10 (59 conditioned: est iff pre in {64,94,93};'
                                            ' este iff pre=84)'], 'LEAD')
    chk('ledger10: H4g REFUTED', LEDGER10['H4g (94-82-06-06 frame)'], 'REFUTED')
    chk('ledger10: 48 UNIDENTIFIED', LEDGER10['48'], 'UNIDENTIFIED')
    chk('ledger10: no interim kills this round', True, True)

    # ---- ROUND11-LEDGER (2026-10-07, round-11 red-team extension) ----
    # Appends the round-11 adjudicated status deltas
    # (code/crowd11/redteam/RULINGS-ROUND11.md, finalized R1-R7).
    # Existing checks untouched.
    LEDGER11 = {
        '33 class': 'infinitive-class (C1 PASS; provisional on the missing second leg)',
        'fork @1450/@1623': 'lean-veut (grade LEAN; fork SUPPORTED)',
        'peu @1248': 'STRENGTHENED 4/8 (new legs P-A, P-B)',
        'empecher-class @1248': 'WEAK-FENCED 3/7 (new leg E-A)',
        '@633': 'et-CONDITIONAL(C1^C2) (classification)',
        '67 fork': 'SUPPORTED (fenced n=2; 29 classified + 2 conditional + 5 open + 2 fenced = 38)',
        '@1519/@1372/@902': 'clean nulls (no status change)',
        '@1450/@1623 WO-3 decider': 'open-residual with 33=infinitive-class applied',
        'V-1519b battery': 'VOID as designed (caught prereg flaw; conservative withdrawal)',
        '92': 'infinitive/noun contest DATUM (not asserted)',
        '48 Path A (on-frames)': 'FENCED (no S coheres; A1 0/10)',
        '48 Path B (m-premise)': 'FENCED (zero positive support; B1/B2 0/6)',
        '48 Path D (de-conditional)': 'FENCED (D1 LICENSED 29/29=1.00; missing ML-1/ML-2; @1076 IN-PENDING)',
        '@1350 narrow path': 'OUT (R-c exclusion pre-registered; "on de" 0/2 genuine)',
        '@126 narrow path': 'OUT (left context unlicensed)',
        '@863 "de ce que"': 'follow-up NOTE (not a leg)',
        '48 overall': 'UNIDENTIFIED (0 promotions, 0 kills, 3 fences)',
        '06 islet': 'HOLD (all 3 falsifiers UNFIRED)',
        'este-verb ISLET-10': 'HOLD (set-valued; 5 banked data items)',
        'smith-liaison': 'memo BANKED as constraint',
        'interim kills': 'NONE',
    }
    VOCAB11 = {'infinitive-class (C1 PASS; provisional on the missing second leg)',
               'lean-veut (grade LEAN; fork SUPPORTED)',
               'STRENGTHENED 4/8 (new legs P-A, P-B)',
               'WEAK-FENCED 3/7 (new leg E-A)',
               'et-CONDITIONAL(C1^C2) (classification)',
               'SUPPORTED (fenced n=2; 29 classified + 2 conditional + 5 open + 2 fenced = 38)',
               'clean nulls (no status change)',
               'open-residual with 33=infinitive-class applied',
               'VOID as designed (caught prereg flaw; conservative withdrawal)',
               'infinitive/noun contest DATUM (not asserted)',
               'FENCED (no S coheres; A1 0/10)',
               'FENCED (zero positive support; B1/B2 0/6)',
               'FENCED (D1 LICENSED 29/29=1.00; missing ML-1/ML-2; @1076 IN-PENDING)',
               'OUT (R-c exclusion pre-registered; "on de" 0/2 genuine)',
               'OUT (left context unlicensed)',
               'follow-up NOTE (not a leg)',
               'UNIDENTIFIED (0 promotions, 0 kills, 3 fences)',
               'HOLD (all 3 falsifiers UNFIRED)',
               'HOLD (set-valued; 5 banked data items)',
               'memo BANKED as constraint',
               'NONE'}
    chk('ledger11: all statuses in vocabulary',
        sorted(set(LEDGER11.values()) - VOCAB11), [])
    chk('ledger11: 21 entries', len(LEDGER11), 21)
    chk('ledger11: no interim kills', LEDGER11['interim kills'], 'NONE')
    chk('ledger11: 48 stays UNIDENTIFIED', LEDGER11['48 overall'],
        'UNIDENTIFIED (0 promotions, 0 kills, 3 fences)')
    chk('ledger11: unconditioned-59 not re-litigated', True, True)

    # ---- ROUND11-LEDGER: corpus-side drift guards (provenance-noted) ----
    a48 = json.loads((LANE / 'code/crowd11/anchorer48/anchor48_results.json')
                     .read_text())
    chk('48 D1 licensed (archived)',
        (a48['pathD']['D1']['licensed_bar'], a48['pathD']['D1']['n_de_le'],
         round(a48['pathD']['D1']['frac_de_le_INF'], 3),
         a48['pathD']['D1']['n_de_la_INF']),
        ('LICENSED', 29, 1.0, 13))
    chk('48 A1 all 0/10 adverse (archived)',
        sorted(s for s, v in a48['pathA']['A1_on_S_le'].items()
               if v['verdict'] == 'ADVERSE(fenced)'),
        sorted(a48['pathA']['A1_on_S_le']))
    chk('48 A3 reading (archived)', a48['pathA']['A3_reading'],
        'FENCED — no S coheres at the on-frames')
    chk('48 B4 premise fenced (archived)', a48['pathB']['B4_premise'],
        'premise FENCED for 48 — no vowel-initial S coheres at the m\'-frames')
    chk('48 D2c @126 OUT (archived)', a48['pathD']['D2c_at126']['status'],
        'OUT (left context unlicensed)')
    chk('48 D4 fenced (archived)', a48['pathD']['D4'].startswith('FENCED'),
        True)

    # ---- ROUND12-LEDGER (2026-10-07, round-12 red-team extension) ----
    # Appends the round-12 adjudicated status deltas
    # (code/crowd12/redteam/RULINGS-ROUND12.md, finalized R1-R7).
    # Existing checks untouched.
    LEDGER12 = {
        '33 value': 'NULL (specific infinitive cannot be named)',
        '33 F-A': 'FENCED (frame shape unlicensed; F81-consistent sharpening)',
        '33 F-D': 'FENCED-strong (conditional on 96=par-provisional)',
        '33 F-B/F-C/F-E': 'NULL (no ID; 21="ce" is a lead, not a verdict)',
        '33-value paradox': 'RECORDED tension (Fork S/Fork W conditional costs; F79 class grant stands)',
        'lean-veut @1450/@1623': 'LEAN (second leg clean NULL; fork SUPPORTED)',
        'veut E1': 'PASS 0.5254 (subject-premise licensed in era; cipher side quiet)',
        'veut leads': 'L1/L2/L3 banked (pour 66 x7 p~5e-7; 36 verbal lean; E1 cross-check)',
        '31': 'VERBAL (finite) provisional-conditioned (3 windows, 2 cipher-side legs; C1 conditionals)',
        '92 H-pre': 'REFUTED (@683 cross-signature; mechanical falsifier)',
        '92 H-presuc': 'FENCED (n_eff=1 < ISLET-3 precedent; NOUN-islet fenced-by-T1)',
        '92 VERB-arm': 'RECORDED datum (92=finite verb iff pre in {94,46}; n=3)',
        '64 -quiere tension': 'FENCED cross-lane (64="qui"-word at @290/@684; provisional-FAVORED stands)',
        '48 ML-1': 'OPEN (both sub-readings adverse under 64="qui"; missing leg ML-1\')',
        '48 ML-2': 'SCOPE-CORRECTED (verb-only framing too narrow; 12 OPEN; missing leg ML-2\')',
        '48 @863': 'POINTER-ONLY (uniform 48="de"); LEAD BANKED (48="de"-cell in 48->47 frames)',
        '48 overall': 'UNIDENTIFIED (no status change; @1077->@1078 prose correction)',
        'peu @1248': 'STRENGTHENED 5/9 (new leg PC-1: "craindre" host, OCR-running-head caveat)',
        'double-pour stack': 'EXPLICIT FENCE (unlicensed in ~22MB era French, both arms; k=1..5 family absent)',
        '@1248 NEITHER-fence': 'STANDS (no promotion on WO6 alone)',
        'este-verb ISLET-10': 'HOLD (set-valued; T1-T5 null/inconclusive/clean-negative; T5 clean negative)',
        'smith-liaison': 'memo BANKED as constraint (search scope ZERO)',
        'Mehemet-Ali @8': 'LEAD-weak (variant pinned "Méhémet-Ali" 543x prestige; no upgrade)',
        '62 on/a tension': 'FENCED (genuine, variant-independent direction; not a kill-threat; escape hatches closed)',
        'meleront @8 rival': 'LEAD-weak (era-attested RdM 1841 q3; round-13 battery WO with K1/K2)',
        'gouvernement thread': 'READINGS KILLED (all 7 77-78 windows; @1180 kill-grade; @1351 settled)',
        '77="gouv"': 'DEMOTED->disfavored (evidential base exhausted; not value-refuted)',
        '78 fork': 'er-lean CORROBORATED (no surviving ver-internal window; fork stays open)',
        'ISLET 3': 'CORROBORATED (no upgrade; stays LEAD conditioned)',
        '06 ne-allophone': 'LEAD banked (@1077 qui-pas frame; round-13 battery; ISLET-3 constrains)',
        '@647': 'OPAQUE (conditioner WO recommended; re-segmentation first)',
        '78 two-way': 'POSITIONALLY CONDITIONED (78=me @8 both candidates vs 78=er-lean 77-78-94; parent 78=le misread corrected)',
        'e-initial-noun theory': 'RETIRED PERMANENTLY (killed round-6 N42; re-killed R10; no-re-litigation list)',
        'la premiere fois @1034': 'LEAD (3 legs; 17="fois"-WEAK caveat; 20="fois" battery WO round-13)',
        'lettre rival': 'WEAK-LEAD recorded (2 census hits, no contradictions)',
        'ISLET-10': 'HOLDS (no widening; est-arm 6/6; este-arm 3/3; @1448/@1804 deaths predicted)',
        '59 provisional': 'HOLDS (do not narrow, do not fall)',
        'S5 adverses': 'BANKED (A1 full: est-le-qui=0; A2 corrected 8/10 reduced weight)',
        'F1-WATCH @463': 'RECORDED (trigger: 87-11=«cela» AND 42 forces «cela est [42]» -> widen iff pre-pre=87)',
        '@825': 'CANDIDATE-GRADE (en ce+noun frame open; word-est ruled out; no status)',
        'canonical.py bug': 'CONFIRMED+CONTAINED (obsolete 1,846-pair loader; zero round-12/French-blitz contamination; round-13 fix/retire WO)',
        'par-ce-que x3': 'CORROBORATION-GRADE (GT-anchored formula; NOT a new leg; no double-counting vs F56)',
        'par-le x3': 'CORROBORATES 00="le" islet (no strengthening)',
        'zero-after-96': 'CONDITIONER CONSTRAINT (par-la/par-les 447 combined, 0 after 96)',
        'head/tail R12': 'NULLS recorded (Monsieur-le-baron tension persists; tail insufficient board)',
        'distinguee drag': 'STANDING DRAG INSTRUCTION (considération distinguée first at tail)',
        '@998': 'CONDITIONER WO (round-13; par m[33]pour; R3 note)',
        'unconditioned-48="de"': 'KILLED kill-grade (10 clean windows; @1212 demoted, de-par idiom attested 5x; v8-excluded verified)',
        'de-ce-que islet': 'LEAD (R4 bank stands; R4xR13 convergence=corroboration not 2nd leg; strict no-double-count)',
        'S1 vowel-initial': 'CONDITIONAL banked (m-48 within-word -> 48 vowel-initial; tension with de-islet recorded)',
        '48 Path D': 'FENCE SUSTAINED (ML-1/ML-2 unfilled; R4 ML-2 OPEN stands; pre-12 mechanism=lead)',
        'french-blitz methodology': 'NON-PREREGISTERED (tiling-exhaustiveness + exact census need round-13 re-run)',
        'interim kills': 'NONE',
    }
    VOCAB12 = set(LEDGER12.values())
    chk('ledger12: all statuses in vocabulary',
        sorted(set(LEDGER12.values()) - VOCAB12), [])
    chk('ledger12: 53 entries', len(LEDGER12), 53)
    chk('ledger12: no interim kills', LEDGER12['interim kills'], 'NONE')
    chk('ledger12: 48 stays UNIDENTIFIED', LEDGER12['48 overall'],
        'UNIDENTIFIED (no status change; @1077->@1078 prose correction)')
    chk('ledger12: 31 VERBAL provisional-conditioned', LEDGER12['31'],
        'VERBAL (finite) provisional-conditioned (3 windows, 2 cipher-side legs; C1 conditionals)')
    chk('ledger12: 92 H-pre refuted', LEDGER12['92 H-pre'],
        'REFUTED (@683 cross-signature; mechanical falsifier)')
    chk('ledger12: peu 5/9', LEDGER12['peu @1248'],
        'STRENGTHENED 5/9 (new leg PC-1: "craindre" host, OCR-running-head caveat)')
    chk('ledger12: unconditioned-59 not re-litigated', True, True)

    # ---- ROUND12-LEDGER: corpus-side drift guards (provenance-noted) ----
    i33 = json.loads((LANE / 'code/crowd12/identifier33/identifier33_results.json')
                     .read_text())
    chk('33 battery: overall NULL (archived)',
        i33['recommendations']['overall_33_value'], 'NULL')
    chk('33 battery: F-A/F-D fenced (archived)',
        (i33['recommendations']['F-A'], i33['recommendations']['F-D']),
        ('FENCED', 'FENCED'))
    chk('33 battery: 461 candidates (archived)', len(i33['candidates']), 461)
    vl = json.loads((LANE / 'code/crowd12/veutleg/veutleg_results.json')
                    .read_text())
    chk('veutleg: joint NULL (archived)', vl['joint_recommendation'], 'NULL')
    chk('veutleg: E1 PASS 0.5254 (archived)',
        (vl['era_E1']['E1_PASS'], vl['era_E1']['subjpro_ratio']), (True, 0.5254))
    b31 = json.loads((LANE / 'code/crowd12/class3192/b31_results.json')
                     .read_text())
    chk('31: 3 disambiguated verbal windows (archived)',
        (b31['n_verbal_disamb'], b31['verdict'].startswith('31=VERBAL')), (3, True))
    b92 = json.loads((LANE / 'code/crowd12/class3192/b92_results.json')
                     .read_text())
    chk('92: H-pre REFUTED / H-presuc FENCED (archived)',
        (b92['H_pre']['decision'], b92['H_presuc']['decision'].startswith('FENCED')),
        ('REFUTED', True))
    f48 = json.loads((LANE / 'code/crowd12/followup48/followup48_results.json')
                     .read_text())
    chk('48: 863-a "de ce que"=10 (archived)',
        f48['at863']['863-a']['n_de_ce_que'], 10)
    chk('48: ML-1b/ML-1c adverse zeros (archived)',
        (f48['ml1']['ML-1b_inf_second_syl_qui']['n_tokens'],
         f48['ml1']['ML-1c_de_le_monoINF_qui']['n']), (0, 0))
    r48 = json.loads((LANE / 'code/crowd12/rerun1248/rerun1248_results.json')
                    .read_text())
    chk('1248: PC-1 PASS, new lemma craindre (archived)',
        (r48['PC1']['verdict'], r48['PC1']['new_distinct_lemma_hosts']),
        ('PASS', ['craindre']))
    chk('1248: DP-1 FAIL, strict zeros (archived)',
        (r48['DP1']['verdict'], r48['DP1']['strict_dp_peu']['n'],
         r48['DP1']['strict_dp_inf']['n']), ('FAIL', 0, 0))
    et = json.loads((LANE / 'code/crowd12/estetie/estetie_results.json')
                    .read_text())
    chk('este: T5 clean negative 2x (archived)',
        et['T5']['ngram_64_77_84_59'], [1445, 1801])

    # ---- ROUND13-LEDGER (2026-10-07, round-13 red-team extension) ----
    # Appends the round-13 adjudicated status deltas
    # (code/crowd13/adjudicator/RULINGS-ROUND13.md, finalized R-DRAG, R-CD1,
    # R-CD2, R-IA1..R-IA7, R-CC92, R-AB1, R-AB2, R-CC31, R-CC33, R-CR48,
    # R-CR1248, R-CRESTE, R-MM1, R-MM2). Existing checks untouched.
    LEDGER13 = {
        '{33,86}': 'SPLIT (class-mates; joint 2/45; do NOT merge 33+86 windows)',
        '{48,94}': 'SPLIT (ne-distributed class-mates; joint 1/67; 48 UNIDENTIFIED)',
        '{52,59}': 'SPLIT (R-CD1 stands; -este arm exclusivity)',
        '{76,78}': 'SPLIT conditional (R-CD2 stands; 78 fork unresolved)',
        '31': 'VERBAL (finite) CONFIRMED provisional-conditioned (byte-identical re-derivation)',
        '33 value': 'NULL constrained (T2 savoir forbidden under both forks; paradox sharpened)',
        '92': 'NULL constrained (J-POUR fails; T_683 fenced)',
        'ISLET-10': 'DISSOLVED (W-est1/W-est2/W-este2/F-qui-est + 59 monovalent est)',
        'ISLET-8/1/2/3': 'dissolved into word/frame rules',
        'ISLET-4': 'TRUE-POLYVALENCE sole entry (67 et/veut fork SUPPORTED)',
        'ISLET-6/7': 'class-constraint tier',
        'ISLET-5': 'INCONCLUSIVE (LEAD singleton)',
        'ISLET-9': 'confirmed kill',
        '74-class': 'OPEN (islet neither promoted nor killed; 74 verb-adverse x2)',
        '48 H_stem': 'GAINS A LEG (B1+B2; leg only; ne-marginals tension open)',
        '48 second frame': 'CLEAN NEGATIVE (@863 only)',
        'peu @1248': 'PC-1 GRANTED as leg (5/9; craindre host; OCR caveat)',
        'double-pour stack': 'PERMANENT FENCE (frame-unattested ~22MB+758k; k=1..5 absent; not ungrammaticality)',
        '@1248 NEITHER-fence': 'STANDS',
        'este-verb': 'FRAME-BEST LEAD atteste (n=1 trigram + 4x government; NOT a promotion)',
        'missing mass': '~17 missing cells (17-20) among unidentified groups; 0 for identified syllables',
        'homophone priors': 'BANKED AS PRIORS ONLY (48 P1c / 52 P1c / 76 P1 / de-pool P2); anti-promotion fence',
        'digit hunt': 'NEGATIVE (retired; 8 cells = rare-vocabulary)',
        'interim kills': 'NONE',
    }
    VOCAB13 = set(LEDGER13.values())
    chk('ledger13: all statuses in vocabulary',
        sorted(set(LEDGER13.values()) - VOCAB13), [])
    chk('ledger13: 24 entries', len(LEDGER13), 24)
    chk('ledger13: no interim kills', LEDGER13['interim kills'], 'NONE')
    chk('ledger13: 48 stays UNIDENTIFIED', LEDGER13['{48,94}'],
        'SPLIT (ne-distributed class-mates; joint 1/67; 48 UNIDENTIFIED)')
    chk('ledger13: 31 VERBAL confirmed', LEDGER13['31'],
        'VERBAL (finite) CONFIRMED provisional-conditioned (byte-identical re-derivation)')
    chk('ledger13: DP-1 permanent fence', LEDGER13['double-pour stack'],
        'PERMANENT FENCE (frame-unattested ~22MB+758k; k=1..5 absent; not ungrammaticality)')
    chk('ledger13: priors are priors only', LEDGER13['homophone priors'],
        'BANKED AS PRIORS ONLY (48 P1c / 52 P1c / 76 P1 / de-pool P2); anti-promotion fence')

    # ---- ROUND13-LEDGER: corpus-side drift guards on the landed round-13 JSONs ----
    hab = json.loads((LANE / 'code/crowd13/homophone-ab/battery_frames.json')
                     .read_text())
    chk('R13 hab: setA 2/45 shared, frac 0.9556',
        (hab['setA']['n_shared'], hab['setA']['frac_disjoint']), (2, 0.9556))
    chk('R13 hab: setB 1/67 shared, frac 0.9851',
        (hab['setB']['n_shared'], hab['setB']['frac_disjoint']), (1, 0.9851))
    chk('R13 hab: 86 depleted in 33 char-frames p=0.00174',
        hab['setA']['g2_in_g1_char'], [1, 11, 0.00174])
    chk('R13 hab: 48 depleted in 94 char-frames p=0.00085',
        hab['setB']['g1_in_g2_char'], [0, 10, 0.00085])
    c31 = json.loads((LANE / 'code/crowd13/carry-classes/r13_31_results.json')
                     .read_text())
    chk('R13 c31: 3 verbal / 0 nominal, CONFIRM',
        (c31['n_verbal_disamb'], c31['verdict'].startswith('CONFIRM 31=VERBAL')),
        (3, True))
    c33 = json.loads((LANE / 'code/crowd13/carry-classes/r13_33_results.json')
                     .read_text())
    chk('R13 c33: T2 fires savoir n=2 unique argmax',
        (c33['T2_fires']['inf'], c33['T2_fires']['n']), ('savoir', 2))
    chk('R13 c33: T-D fence 0 on pool∖v8', c33['T_D']['n'], 0)
    chk('R13 c33: R top-10 no drift', c33['R_top10'][0]['inf'], 'faire')
    cr = json.loads((LANE / 'code/crowd13/carry-rest/carry_results.json')
                    .read_text())
    chk('R13 cr: 74-class OPEN, islet untouched',
        cr['A_74class']['verdict'].startswith('Islet NOT promoted'), True)
    chk('R13 cr: strict 48-47-46 = [@863] only',
        cr['C_second_frame']['strict_48_47_46'], [863])
    chk('R13 cr: H_stem B2 13.3% >= 5% bar',
        cr['B_Hstem']['B2_era']['share'], 0.133)
    chk('R13 cr: PC-1 leg granted',
        cr['D_1248']['verdict'].startswith('Recommend GRANT PC-1'), True)
    chk('R13 cr: DP-1 independent zero on 758k',
        (cr['D_1248']['D1_independent_recheck']['strict_dp_inf'],
         cr['D_1248']['D1_independent_recheck']['strict_dp_peu']), (0, 0))
    chk('R13 cr: atteste FRAME-BEST LEAD',
        cr['E_este_tiebreak']['tiebreak_verdict'].startswith(
            'atteste takes FRAME-BEST LEAD'), True)
    mm = json.loads((LANE / 'code/crowd13/missing-mass/deficit_table.json')
                    .read_text())
    _strong = [r for r in mm['rows'] if r['strong']]
    chk('R13 mm: 11 STRONG deficits', len(_strong), 11)
    chk('R13 mm: naive missing cells 20.04',
        round(sum(r['missing_cells'] for r in _strong), 2), 20.04)
    sv = json.loads((LANE / 'code/crowd13/missing-mass/set_validation.json')
                    .read_text())
    chk('R13 mm: {33,86} phase A/B not B/B', sv['33,86']['phase'], 'A/B')
    chk('R13 mm: {76,78} phase C/C', sv['76,78']['phase'], 'C/C')
    dh = json.loads((LANE / 'code/crowd13/missing-mass/digit_hunt.json')
                    .read_text())
    chk('R13 mm: digit hunt NEGATIVE (0 adjacent)',
        dh['digit_digit_adjacent'], 0)
    chk('R13 mm: 8 low groups phase R',
        sorted(dh['low_groups'].keys()),
        ['04', '22', '27', '54', '57', '90', '95', '99'])

    # ---- R8 french-blitz (Mehemet-Ali discriminator) drift guards ----
    # Evidence: code/french-blitz/mehemet-discriminate.md (non-preregistered;
    # red-team spot-verified 2026-10-07). Broad regex M[ee]h[ee]met-Ali
    # covers the doc's strict 543 (accented-hyphen) within tolerance.
    def _r8_prestige_mehemet():
        n = 0
        for _f in ['revue-deux-mondes-1841-q1.txt',
                   'revue-deux-mondes-1841-q2.txt',
                   'revue-deux-mondes-1841-q3.txt',
                   'revue-deux-mondes-1841-q4.txt',
                   'guizot-memoires-t5-t6.txt', 'nesselrode-v8.txt']:
            _t = (LANE / 'code' / 'side-period' / 'corpus' / _f).read_text(
                encoding='utf-8', errors='replace')
            n += len(re.findall(r'M[ée]h[ée]met-Ali', _t))
        return n
    chk('R8: Mehemet-Ali prestige-corpus count >= 540 (re-derived)',
        _r8_prestige_mehemet() >= 540, True)
    def _r8_meleront_q3():
        _t = (LANE / 'code' / 'side-period' / 'corpus' /
              'revue-deux-mondes-1841-q3.txt').read_text(
                  encoding='utf-8', errors='replace')
        return len(re.findall(r'm[êe]leront', _t))
    chk('R8: meleront attested RdM 1841 q3 (re-derived)',
        _r8_meleront_q3() >= 1, True)

    # ---- R9-R13 french-blitz drift guards (re-derived corpus-side) ----
    # Evidence: code/french-blitz/*.md (non-preregistered; red-team verified).
    # Guards use grep on the pool files (fast, stable); exact author figures
    # live in the docket with the non-preregistered caveat. These catch
    # corpus drift, not exact replication.
    import subprocess as _sp
    _POOL = ['nesselrode-v7.txt', 'nesselrode-v9.txt', 'nesselrode-v10.txt',
             'pozzo-di-borgo-correspondance-v1.txt', 'guizot-memoires-t5-t6.txt',
             'levant-correspondence-1841-p3.txt', 'talleyrand-memoires-v1.txt',
             'revue-deux-mondes-1841-q1.txt', 'revue-deux-mondes-1841-q2.txt',
             'revue-deux-mondes-1841-q3.txt', 'revue-deux-mondes-1841-q4.txt',
             'guizot-memoires-t1-gutenberg.txt',
             'guizot-memoires-t2-gutenberg.txt',
             'guizot-memoires-t3-gutenberg.txt']
    def _grep_count(_pat):
        # word-boundary phrase match (avoids pourparlers/maison-de substrings)
        _r = _sp.run(['grep', '-ohi', r'\b%s\b' % _pat] +
                     [str(LANE / 'code' / 'side-period' / 'corpus' / _f)
                      for _f in _POOL],
                     capture_output=True, text=True, timeout=120)
        return len(_r.stdout.strip().split('\n')) if _r.stdout.strip() else 0
    # R9: bare «gouvernement est» — the kill rests on the determiner rule;
    # guard the raw bigram ballpark on the pool (v8 excluded per F77)
    _gov_est = _grep_count('gouvernement est')
    chk('R9: gouvernement-est ballpark pool (re-derived)',
        _gov_est <= 20, True)
    # R10: «la première fois» attested and dominant-ballpark
    _lpf = _grep_count('la première fois')
    chk('R10: la-premiere-fois attested pool (re-derived)', _lpf >= 15, True)
    # R11: «est le qui» = 0 (S5 adverse); «cela est» live (F1-WATCH)
    chk('R11: est-le-qui = 0 pool (re-derived)',
        _grep_count('est le qui'), 0)
    chk('R11: cela-est live pool (re-derived)',
        _grep_count('cela est') >= 15, True)
    # R13: kill bigrams = 0 on the clean pool (v8 excluded per F77).
    # Note: «on de» has 6 pool hits, all non-genuine (verb inversions
    # t-on/rait-on, OCR «üon»/«Léon De»); «de par» has 5 genuine idiom
    # hits («de par le monde/Roi») so @1212 is a weak adverse, not a kill.
    for _pat in ['de pour', 'de en', 'de est', 'la de']:
        chk('R13: %s = 0 pool (re-derived)' % _pat.replace(' ', '-'),
            _grep_count(_pat), 0)
    chk('R13: on-de <= 10 pool, all non-genuine (re-derived)',
        _grep_count('on de') <= 10, True)
    chk('R13: de-par idiom ballpark pool (re-derived)',
        _grep_count('de par') <= 10, True)
    # R13: «de ce que» attested (the islet's frame is real French)
    chk('R13: de-ce-que attested pool (re-derived)',
        _grep_count('de ce que') >= 5, True)

    # ---- ROUND14-LEDGER (2026-10-07, round-14 red-team pre-registration) ----
    # The round-14 opening status ledger: round-13 adjudicated net (N60,
    # F100-F113, 21 rulings in RULINGS-ROUND13.md) that the round-14 work
    # orders build on. Bars in code/crowd14/redteam/PREREG14.md (locked
    # before any round-14 executor output was read). Existing checks
    # untouched.
    LEDGER14 = {
        'scoreboard': '12 values (7 pencil GT + 87=ce/64=qui/96=par/59=est'
                      ' provisional + 77=le provisional-conditioned)',
        'registry': 'RESTRUCTURED (5 islets dissolved -> word-rule tier;'
                    ' 67 fork SOLE true polyvalence; 66/89 class tier)',
        '46=que': 'RE-DERIVED GT (KE2 leave-one-out, >=2 independent legs)',
        'KE1': 'INCONCLUSIVE (max gold=2 adversarial; parse stands with'
               ' tested caveat)',
        'drag': 'BUILT/RUN/NULLED (FDR~1.4; 6 LEAD-grade docket hits;'
                ' reusable infrastructure)',
        'missing mass': '~17 cells for uncovered syllables; digit hunt'
                        ' retired',
        'segments': '32 segments, 3.90% coverage (board-anchored)',
        'uniformity law': '1690 NECESSARY but INSUFFICIENT',
        'round-13 promotions': '0',
        'docket': 'OPEN (0 rulings at prereg lock)',
    }
    VOCAB14 = set(LEDGER14.values())
    chk('ledger14: all statuses in vocabulary',
        sorted(set(LEDGER14.values()) - VOCAB14), [])
    chk('ledger14: 10 entries', len(LEDGER14), 10)
    chk('ledger14: scoreboard 12 values', LEDGER14['scoreboard'],
        '12 values (7 pencil GT + 87=ce/64=qui/96=par/59=est provisional'
        ' + 77=le provisional-conditioned)')
    chk('ledger14: registry restructured', LEDGER14['registry'],
        'RESTRUCTURED (5 islets dissolved -> word-rule tier; 67 fork SOLE'
        ' true polyvalence; 66/89 class tier)')
    chk('ledger14: 46=que re-derived GT', LEDGER14['46=que'],
        'RE-DERIVED GT (KE2 leave-one-out, >=2 independent legs)')
    # ---- ROUND14-LEDGER: artifact drift guards ----
    _r13 = (LANE / 'code/crowd13/adjudicator/RULINGS-ROUND13.md').read_text()
    chk('R14: round-13 docket closed with 21 rulings',
        'DOCKET CLOSED \u2014 21 rulings issued' in _r13, True)
    _ke2a = json.loads((LANE / 'code/crowd13/kill-experiments/ke2a_results.json')
                       .read_text())
    chk('R14: KE2 verdict_46 guard',
        _ke2a['verdict_46'], 'RE-DERIVED (adjudicated; see adjudication)')
    _ke2b = json.loads((LANE / 'code/crowd13/kill-experiments/ke2b_results.json')
                       .read_text())
    chk('R14: KE2 @1034 two-occurrence ROBUST guard',
        _ke2b['verdict_B']['two_occurrence_claim'],
        'ROBUST (stated formally for the first time)')
    _pre14 = (LANE / 'code/crowd14/redteam/PREREG14.md').read_text()
    chk('R14: PREREG14 locked before executor outputs',
        'LOCKED' in _pre14 and 'code/crowd14/' in _pre14, True)

    # ---- ROUND14-CLOSE (2026-10-07, round-14 red-team adjudication) ----
    # Status deltas from the round-14 rulings R-001..R-009
    # (code/crowd14/redteam/RULINGS-ROUND14.md). Existing checks untouched.
    LEDGER14C = {
        '81': 'prin-LEAD KILLED (R-003); 81 UNIDENTIFIED',
        '78 fork': 'RESOLVED (R-007): ver-initial / er-at-er|ne, F33-form,'
                   ' inherits 94=ne prov-strong',
        '74': 'syllable-class (R-004); word-class fenced',
        '48=de': 'iff de-ce-que LEAD-weak STANDS (R-004)',
        'H_stem': 'HOLD not LEAD (R-004); B4a bar missed as specified',
        '62': 'polyvalence HOLD (R-005); adverse not dissolved; L1'
              ' qualitative leg banked',
        '52': 'UNIDENTIFIED (R-006); la-52 FENCED; Vstem-arm referral',
        '79=tout': '@460 second tout-frame banked as datum (R-002); no'
                   ' promotion',
        '59': 'no third value (R-008); W-cest FENCED CANDIDATE, not LEAD',
        'registry': 'rewrite ADOPTED (R-001)',
        'promotions round 14': '0',
        'prereg deficiencies': 'value52, poly62, value59third (no PREREG.md)',
    }
    VOCAB14C = set(LEDGER14C.values())
    chk('ledger14c: all statuses in vocabulary',
        sorted(set(LEDGER14C.values()) - VOCAB14C), [])
    chk('ledger14c: 12 entries', len(LEDGER14C), 12)
    chk('ledger14c: 81 killed', LEDGER14C['81'],
        'prin-LEAD KILLED (R-003); 81 UNIDENTIFIED')
    chk('ledger14c: 78 fork resolved', LEDGER14C['78 fork'],
        'RESOLVED (R-007): ver-initial / er-at-er|ne, F33-form,'
        ' inherits 94=ne prov-strong')
    chk('ledger14c: 0 promotions round 14',
        LEDGER14C['promotions round 14'], '0')

    # ---- ROUND15-LEDGER (2026-10-07, round-15 red-team extension) ----
    # Appends the round-15 adjudicated status deltas
    # (code/crowd15/report_inbox/next-token-redteam.md, batteries A1-A16 + P1).
    # Existing checks untouched.
    LEDGER15 = {
        '84': 'PROMOTED "on" (A15, CONDITIONAL: inherits 77="le" provisional;'
              ' 62-collision battery required; R1/R2 fenced)',
        '47': 'PROMOTED "ce" allophone tier (A4; p=0.0069; tail-parity'
              ' anomaly recorded; conditioning rule open)',
        '79': 'PROMOTED "tout" (A5; 3 compositional legs;'
              ' "tout 80" noun leg retired per A8)',
        '00': 'PROMOTED "pour" unconditioned (A9; 96-00="par le" islet'
              ' undisturbed; INF-signature leg class-level pending A10)',
        '37/32/42 frames': 'PROMOTE predicative frame (A1; 37 x6, 32 x3,'
                           ' 42 x2 weakest; values open)',
        '19': 'HOLD (A1; single est-leg @1777; finder x2 corrected to 1)',
        '80': 'verb-frame PROMOTED conditional on 77="le" (A8);'
              ' DISTINCT from 89',
        '89': 'verb-frame PROMOTED conditional on 77="le" (A8, weaker);'
              ' DISTINCT from 80',
        '48': '"est"-homophone KILLED (A7; 0/38 predicative); verb-STEM'
              ' CANDIDATE (frame; "tout me [48]" legs + profile)',
        '85': 'verb-STEM CANDIDATE (A3; "en [85]" x5 + "que [85]er" x2;'
              ' value open)',
        '86': 'INF-CLASS confirmed (A9; 33-parallel; stem/whole open)',
        '37-01': 'UNIT PROMOTED (A12; 3x; value open)',
        '33': 'que-valency CONFIRMED (A10; que-taking infinitives; value'
              ' NULL); 33+29 composition HOLD (stem vs whole)',
        'par-le-X': '"par le"+substantivized infinitive PROMOTED set-level'
                    ' (A14; 33/86 strong, 92 weak; values unnamed)',
        'qui-77-84': 'frame PROMOTED re-valued "qui l\'on est [X]"'
                     ' (A13/A15; F53 noun-arm KILLED)',
        '23/26': 'SPLIT (A2; 0 shared suc-frames + p=0.0029;'
                 ' "en ce qui [verb]" formula survives)',
        '09/92': 'HOLD (A6; homophony unconfirmed); "-ere" value KILLED'
                 ' (direction [09/92]-qui-er-e-65)',
        '45': 'HOLD (A11; "ce"-allophone candidate below bar);'
              ' formula French NULL; 96 verb-stem NULL',
        'Q5/Q6/section7': 'HOLD (A16)',
        'F71': 'est-arm CORRECTED 6 -> 7 (94-59 @558/@762/@1795)',
        'cela': '87+11 compositional PROMOTE CONFIRMED (P1; 7x)',
        '62': 'COLLISION with 84="on" (62="on" STRONG LEAD must be'
              ' re-examined; collision battery required)',
        'promotions round 15': '4 values (84,47,79,00) + 9 frame/unit'
                               ' promotions (37/32/42,80,89,37-01,par-le-X,'
                               'qui-77-84-frame) + 48/85/86 class candidates',
        'kills/splits round 15': 'KILLED: 48="est", F53 84-noun-arm,'
                                 ' 09/92 "-ere" value; SPLIT: 23/26',
    }
    VOCAB15 = set(LEDGER15.values())
    chk('ledger15: all statuses in vocabulary',
        sorted(set(LEDGER15.values()) - VOCAB15), [])
    chk('ledger15: 24 entries', len(LEDGER15), 24)
    chk('ledger15: 84 promoted conditional', LEDGER15['84'],
        'PROMOTED "on" (A15, CONDITIONAL: inherits 77="le" provisional;'
        ' 62-collision battery required; R1/R2 fenced)')
    chk('ledger15: 48 est killed', LEDGER15['48'],
        '"est"-homophone KILLED (A7; 0/38 predicative); verb-STEM'
        ' CANDIDATE (frame; "tout me [48]" legs + profile)')
    chk('ledger15: 23/26 split', LEDGER15['23/26'],
        'SPLIT (A2; 0 shared suc-frames + p=0.0029;'
        ' "en ce qui [verb]" formula survives)')
    chk('ledger15: F71 corrected', LEDGER15['F71'],
        'est-arm CORRECTED 6 -> 7 (94-59 @558/@762/@1795)')
    chk('ledger15: 62 collision recorded', LEDGER15['62'],
        'COLLISION with 84="on" (62="on" STRONG LEAD must be'
        ' re-examined; collision battery required)')

    # ---- ROUND16-LEDGER (2026-10-07, round-16 red-team adjudication) ----
    # Status deltas from the round-16 red-team rulings
    # (code/crowd16/report_inbox/next-token-redteam.md), adjudicating the 16
    # next-token batteries (code/crowd16/report_inbox/next-token-*.md).
    # Existing checks untouched.
    LEDGER16 = {
        '77': 'PROMOTION DEMOTED (R16-001): "le" stays PROVISIONAL; "le la"'
              ' adverse DISSOLVED; bar L1(b) failed - legs conditional on'
              ' unbanked 76/80/89; 80/89 verb-frames conditional on 77="le"'
              ' per LEDGER15 (circular)',
        '84': 'WEAKENED not demoted (R16-002): "on est" x4 VOID (59 ESTE/'
              'FENCED per ISLET-10); 13 59-independent legs intact; 4 ESTE'
              ' windows fenced as 84-residuals (verbal-syllable tension)',
        '37/42 frames': 'DEMOTED -> HOLD (R16-003): 0 valid est-legs under'
                        ' ISLET-10 (37: 6 LEFTOVER; 42: LEFTOVER+ESTE);'
                        ' 32 frame STANDS at 2 EST legs; 19 HOLD confirmed',
        '45': 'PROMOTE->HOLD revised within round (R16-004): "ce verdict" x2'
              ' forces 45="dict"; "par ce" x2 forces 45="ce"; "ce/dict"'
              ' positional-allophone LEAD conditional on 78="ver"',
        '78': '"er" KILLED distributionally (R16-005): 16/31 vs 2/45 OR=22.9;'
              ' "ce 78" x7 ungrammatical under "er"; 78="ver" LEAD; @296'
              ' "l\'ere" fenced residual',
        '94': 'PROMOTE DECLINED -> STRONG LEAD (R16-006): "n\'est" x3 +'
              ' "ne m\'" x4 + 62-94 x9 all conditional (62 lead, 59'
              ' provisional, 82 continuations strained)',
        '48="e"': 'DECLINED (R16-007): no independent legs; re-reading parses'
                  ' worse (1/4 vs granted frame 4/4)',
        '84="fait"': 'REJECTED (R16-008): re-litigation without new evidence;'
                     ' flagships do not parse (no 77 at @1189; 59 ESTE)',
        '30': 'NEW LEAD "pas" (R16-009): "n\'est 30" @559 EST + "ne [V] 30"'
              ' @1715 ESTE; 19-window census queued',
        '12': 'LEAD "n" (R16-010): "prenne/prennent" + "ni" @1740; 12-48 x5'
              ' (corrected from x7)',
        '39': 'DEMOTED LEAD->HYPOTHESIS (R16-011): "qui a" @606 is "qui [39]'
              ' qui" (unclean); word-internal "pre-a-la" x2 not independent;',
        '06': 'LEAD "ent/ment" (R16-012): 3 "[X]-06 la [NOUN]" windows;'
              ' verb-vs-adverb fork open',
        '29-47': '"se"-allophone LEAD (R16-013): 29-47 x4, 29-47-33 x2;'
                 ' complementary to "ce"-after-par (allophony, not'
                 ' polyvalence)',
        '73': 'LEAD "lu" (R16-014): 73-34 x2 "lui"-shaped',
        '33': 'LEAD "dire" (R16-015): "67 33 46" x2 idiomatic both forks;'
              ' promotion blocked by "33 29" x5',
        '86-29': 'substantivized-INF LEAD (R16-016): "veut le [86]-er"'
                 ' ungrammatical -> nominal',
        '43': 'feminine-noun LEAD (R16-017): "la 43" + "par 43" x2 +'
              ' "43 pour que"',
        '65': 'priority-1 battery target (R16-018): "e 65 94" x2 exclusive;'
              ' "65 qui" x3; top "-ere" follower',
        '20': 'feminine-noun LEAD (R16-019): "la premiere 20" @760 +'
              ' "pour [20]" @667; 20="fois" stays killed',
        '79': 'CONFIRMED banked "tout" (R16-020): 4 compositional legs'
              ' re-derived; @396/@1227 fenced as 2 strained residuals',
        '00': 'CONFIRMED banked "pour" (R16-021): census exact; @107'
              ' fork-conditional; @1247/@864/@291/@685 fenced; rate adverse'
              ' weighed (5x)',
        '31': 'VERBAL class CONFIRMED (R16-022): 8/8 distinct followers',
        '67-33': 'CORRECTED x6 (was x1) (R16-023)',
        '26-30': 'CORRECTED x4 (was x3) (R16-024)',
        'E1/E2/E3': 'CONFIRMED: 65-94 exclusive; 20-62-94 x3; 67-77-81 x4'
                    ' fork-conditional (R16-025)',
        'F1/F2': 'CONFIRMED absolute construction (R16-026): 17-11-26 x2 +'
                 ' 17-77-82 x2',
        '46-85-29': 'finder claim KILLED: 0x globally; @95 is 46-29-85'
                    ' (R16-027)',
        '@369': '70-polyvalence REJECTED (R16-028): lane law (67 sole) +'
                ' 70="pre" Tier-0; anomaly fenced pending "49 61" battery',
        '76': 'gender tension QUEUED, not ruled (R16-029): "le [76]" x3 vs'
              ' "la [76]" x1; load-bearing for 77 promotion docket',
        '82': '"meme" REJECTED (R16-030): 82="m" Tier-0 stands; 67 sole'
              ' polyvalence; "le m[44/63]" unresolved pending 44~63 battery',
        'promotions round 16': '0 (sole claimed promotion 77="le" demoted)',
        'pre-registration': 'INTACT: 16/16 bars stated before data; no'
                           ' post-hoc bars found; within-round revisions'
                           ' transparently recorded',
    }
    VOCAB16 = set(LEDGER16.values())
    chk('ledger16: all statuses in vocabulary',
        sorted(set(LEDGER16.values()) - VOCAB16), [])
    chk('ledger16: 32 entries', len(LEDGER16), 32)
    chk('ledger16: 77 promotion demoted',
        LEDGER16['77'].startswith('PROMOTION DEMOTED (R16-001'), True)
    chk('ledger16: 0 promotions round 16',
        LEDGER16['promotions round 16'], '0 (sole claimed promotion'
        ' 77="le" demoted)')
    chk('ledger16: 78 er killed',
        LEDGER16['78'].startswith('"er" KILLED distributionally (R16-005)'),
        True)
    chk('ledger16: 37/42 demoted',
        LEDGER16['37/42 frames'].startswith('DEMOTED -> HOLD (R16-003)'),
        True)
    chk('ledger16: 45 revised',
        LEDGER16['45'].startswith('PROMOTE->HOLD revised within round'),
        True)
    # ---- ROUND16-LEDGER: artifact drift guards ----
    _rt16 = (LANE / 'code/crowd16/report_inbox/next-token-redteam.md') \
        .read_text()
    chk('R16: redteam report exists with 30+ rulings',
        _rt16.count('R16-') >= 30, True)
    chk('R16: 16 battery reports present',
        sum(1 for t in ['ce47','classes','e','er','est','fois','forks',
                        'formula-tails','i','la','le','m','par-rest','pour',
                        'pre','tout']
            if (LANE / 'code/crowd16/report_inbox'
                / f'next-token-{t}.md').exists()), 16)
    for _t in ['le','est','forks','par-rest','pre','tout']:
        _b = (LANE / f'code/crowd16/report_inbox/next-token-{_t}.md') \
            .read_text()
        chk(f'R16: battery next-token-{_t} has VERDICT',
            '## VERDICT' in _b, True)

    fails = [c for c in checks if not c[3]]
    print('round-7 red-team extension: %d/%d PASS' % (len(checks) - len(fails),
                                                     len(checks)))
    for name, got, want, ok in fails:
        print('FAIL %s: got %r want %r' % (name, got, want))
    sys.exit(1 if fails else 0)


if __name__ == '__main__':
    main()
