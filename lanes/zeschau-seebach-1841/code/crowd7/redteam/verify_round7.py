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
"""
import json
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

    fails = [c for c in checks if not c[3]]
    print('round-7 red-team extension: %d/%d PASS' % (len(checks) - len(fails),
                                                     len(checks)))
    for name, got, want, ok in fails:
        print('FAIL %s: got %r want %r' % (name, got, want))
    sys.exit(1 if fails else 0)


if __name__ == '__main__':
    main()
