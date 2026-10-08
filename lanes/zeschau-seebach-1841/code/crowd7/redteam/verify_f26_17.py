#!/usr/bin/env python3
"""Round-7 red-team extension: F26-17 adjudication checks (2026-10-07).

Extends code/crowd6/redteam/verify_baseline.py (49/49 PASS, untouched) with
every stream-derived number behind the coordinator-applied "curator: ..."
marks in N39-N44 and F45-F51, plus the T4 either/or windows.

Position convention: bigram/trigram START indices (0-based, repaired
1,847-pair parse). This corrects three successor-index slips found in
round-6 memos (F46 «le 84» list, closer87_00 94->84/11->84, closer6 F50
quad, frenchman 77->62) -- counts were right, cited indices were +1.

Run with no args; exits nonzero on any mismatch.

R7BANK (2026-10-07): round-8 red-team extension appending the round-7 banked
facts F52-F59 / N45-N48 (cipher-side stream numbers; corpus-side legs are
banked with provenance in the verify_round7.py STATUS-LINE extension).
Existing checks untouched.

R9BANK (2026-10-07): round-9 red-team extension appending the round-8
adjudicated facts (code/crowd8/adjudicator/RULINGS-FINAL.md), cipher-side
stream numbers only; corpus-side legs are banked with provenance in the
verify_round7.py ROUND8-LEDGER extension. Existing checks untouched.

R10BANK (2026-10-07): round-10 red-team finalizer extension appending the
round-10 adjudicated facts (code/crowd10/redteam/RULINGS-ROUND10.md,
finalized R1-R8), cipher-side stream numbers only; the round-10 status
deltas are banked in the verify_round7.py ROUND10-LEDGER extension.
Existing checks untouched.

R11BANK (2026-10-07): round-11 red-team final extension appending the
round-11 adjudicated facts (code/crowd11/redteam/RULINGS-ROUND11.md,
finalized R1-R7), cipher-side stream numbers only; the round-11 status
deltas are banked in the verify_round7.py ROUND11-LEDGER extension.
Existing checks untouched.

R14BANK (2026-10-07): round-14 red-team pre-registration extension appending
the round-14 standing inputs (round-13 adjudicated facts F100-F113 / N60:
ISLET-3 census, 76 ver-tine windows, le-prince x2, la-52 x3, @825 frame,
@1355 window, W-est1 singleton, n67/n81, KE2 87-follower ranks, F42 A2 bound,
96-87-46 frames, 76->94 zero), cipher-side stream numbers only; bars live in
code/crowd14/redteam/PREREG14.md (locked before any round-14 executor output
was read). Existing checks untouched.

R14BANK-close (2026-10-07): round-14 red-team adjudication extension appending
the cipher-side stream numbers behind the round-14 rulings R-001..R-009
(code/crowd14/redteam/RULINGS-ROUND14.md): 74-74 bigrams, @862-866 frame,
[1228]=82, 62->48 starts, la-52 5-gram x2, Vstem-arm 52s, 11->59 @463,
11->78 x2, 87->59 sole window, @460 tout-cela-est. All re-derived by the red
team. Existing checks untouched.

R16BANK (2026-10-07): round-16 red-team adjudication extension appending the
cipher-side stream numbers behind the round-16 red-team rulings R16-001..
R16-032 (code/crowd16/report_inbox/next-token-redteam.md), all re-derived by
the red team on the repaired 1,847-pair stream. Existing checks untouched.
"""
import json, sys
from collections import Counter
from pathlib import Path

LANE = Path(__file__).resolve().parents[3]  # .../zeschau-seebach-1841
sys.path.insert(0, str(LANE / 'code' / 'crowd6' / 'redteam'))
from verify_baseline import load_stream  # noqa: E402  (49/49 apparatus, reused)

def main():
    pairs = load_stream()
    groups = Counter(pairs)
    big = Counter(zip(pairs[:-1], pairs[1:]))
    def pos2(a, b):
        return [i for i in range(len(pairs) - 1) if (pairs[i], pairs[i + 1]) == (a, b)]

    checks = []
    def chk(name, got, want):
        checks.append((name, got, want, got == want))

    # ---- N44 headline numbers (coordinator re-derived; all confirmed) ----
    for k, want in [(62,35),(94,37),(6,44),(78,31),(59,27),(84,25),(0,55),
                    (47,28),(45,22),(16,28),(24,52),(52,27)]:
        chk(f'n{k:02d}', groups[k], want)
    for (a,b), want in [((62,94),9),((78,45),4),((0,86),12),((0,6),0),
                        ((46,62),0),((47,46),3),((47,64),0),((94,82),4),
                        ((77,78),7),((77,86),5)]:
        chk(f'{a:02d}->{b:02d}', big[(a,b)], want)

    # ---- N39 (frenchman62): non-ear battery for 62="on" ----
    chk('n46', groups[46], 29)
    chk('46->62 absent', big[(46,62)], 0)
    chk('46->34 absent (voids N35 il-differential premise)', big[(46,34)], 0)
    chk('46->29 H-split calibration', pos2(46,29), [95,217])
    chk('21->62 x5', big[(21,62)], 5)
    chk('77->62 start (memo cited successor @508)', pos2(77,62), [507])
    # E=29*0.2475=7.1775 ; p=(1-0.2475)^29
    import math
    chk('N39 E[46->62|on,H-split]', round(29*0.2475,4), 7.1775)
    p0 = (1-0.2475)**29
    chk('N39 p(X=0) ~2.6e-4 (worker)', f'{p0:.1e}', '2.6e-04')

    # ---- F45 (59="est" closer battery) ----
    chk('64->59 S2', pos2(64,59), [315,1209,1776])
    chk('94->59 S3', pos2(94,59), [558,762,1795])
    chk('59->46 S4 positions', pos2(59,46), [216,1190])
    chk('S1 ratio', round((27/1847)/0.01054,2), 1.39)
    chk('S4 ratio ~5.4x adverse (worker: 5.40x)', abs((2/27)/0.0137 - 5.40) < 0.02, True)
    chk('59->37 S5', big[(59,37)], 6)

    # ---- F46 (84 conflict): «le 84» x7 CORRECTED positions ----
    chk('77->84 starts (NOTES F46 listed +1)', pos2(77,84),
        [145,259,1057,1446,1484,1763,1802])
    chk('11->84 start (memo cited successor @1620)', pos2(11,84), [1619])
    chk('94->84 start (memo cited successor @1665)', pos2(94,84), [1664])
    chk('82->84', pos2(82,84), [166])
    chk('46->84', pos2(46,84), [309,472])
    chk('84->59', pos2(84,59), [1189,1290,1447,1803])
    chk('E2 P(84|46)=2/29', round(2/29,4), 0.0690)

    # ---- F47 (00 conflict) ----
    chk('96->00 "par le"', pos2(96,0), [47,465,960])
    chk('00->46 "pour que"', pos2(0,46), [106,545,1545,1680])
    chk('06->00 "[V] pour"', pos2(6,0), [184,544,666,738])
    chk('00->11 "pour la"', big[(0,11)], 4)
    chk('B2b P(86|00)=12/55', round(12/55,3), 0.218)

    # ---- F48 (inventorist) ----
    chk('parmi span', pairs[1196:1199], [96,82,16])
    chk('cela @269', pairs[269:271], [47,11])
    chk('cela @357', pairs[357:359], [47,11])

    # ---- F50/F51 (bigram closer) ----
    chk('le-meme-qui quad start (memos cited @313)', pairs[312:316], [37,78,45,64])
    chk('78->45 @313', pairs[313:315], [78,45])
    chk('78->45 positions', pos2(78,45), [313,573,982,1164])
    chk('77->78 positions', pos2(77,78), [7,213,647,1077,1180,1351,1542])
    chk('P(78|77)', round(big[(77,78)]/groups[77],4), 0.1591)
    chk('P(78|47)', round(big[(47,78)]/groups[47],4), 0.1786)
    chk('F38 ver-islet windows 78->94', pos2(78,94), [1181,1352])

    # ---- N42 T4 windows ----
    chk('T4 @1180', pairs[1180:1185], [77,78,94,82,6])
    chk('T4 @1351', pairs[1351:1356], [77,78,94,82,6])
    chk('94-82-06 @578 (F39: 94=ne there)', pairs[578:581], [94,82,6])

    # ---- R7BANK (2026-10-07, round-8 red-team extension) ----
    # Round-7 banked facts F52-F59 / N45-N48, cipher-side only (corpus-side
    # legs live in the verify_round7.py STATUS-LINE extension, provenance-noted).
    # N45 curator headline items not covered above:
    chk('62->98 (N45)', big[(62,98)], 5)
    chk('n64 bedrock-corrected', groups[64], 47)
    # F52: 59="est" PROVISIONAL — cipher-side leg rates
    chk('P(59|64)=3/47', round(big[(64,59)]/groups[64],4), round(3/47,4))
    chk('P(59|94)=3/37', round(big[(94,59)]/groups[94],4), round(3/37,4))
    chk('P(59)=27/1847', round(groups[59]/len(pairs),5), round(27/1847,5))
    # F56: M6 {37,77}="le" sole exception — cipher-side contacts
    chk('n77/n37', (groups[77], groups[37]), (44,28))
    chk('37->77', big[(37,77)], 2)
    # F58/N46: 48="ne"-allophone is FLAGGED, not a status — battery baseline
    chk('n48', groups[48], 38)
    chk('62->48 (top predecessor)', big[(62,48)], 6)
    chk('48->46 (no "ne que")', big[(48,46)], 0)
    chk('48<->94 (no "ne" contact)', (big[(48,94)], big[(94,48)]), (0,0))
    succ48 = Counter(pairs[i+1] for i in range(len(pairs)-1) if pairs[i] == 48)
    chk('48 successor ceiling (flat profile)', max(succ48.values()), 2)
    # N46: 93="l'" — cipher side (E=32.0 corpus-side, banked in STATUS-LINE)
    chk('n93', groups[93], 14)
    # F59: Mehemet-Ali @8 window + archived M0 (drift guard on the archive)
    chk('Mehemet-Ali P[8:13]', pairs[8:13], [78,18,93,62,98])
    m0 = json.loads((LANE / 'code/crowd7/patternist/battery_mehemet_results.json')
                    .read_text())
    chk('M0 null 33/11870 (archived)', m0['M0']['null_at_8'], [33,11870])
    chk('M0 bearing windows (archived)', m0['M0']['positions'],
        [8,443,476,573,879,982,1105,1164,1670,1758])

    # ---- R9BANK (2026-10-07, round-9 red-team extension) ----
    # Round-8 adjudicated facts (code/crowd8/adjudicator/RULINGS-FINAL.md),
    # cipher-side stream numbers only; corpus-side legs are banked with
    # provenance in the verify_round7.py ROUND8-LEDGER extension.
    # R1: 48="ne"-allophone REFUTED (F60 kill) — H5/H6 adverses cipher-side
    chk('48-47-46 H5 adverse @863', pairs[863:866], [48,47,46])
    chk('24-48-47-98 H5 adverse @1657', pairs[1657:1661], [24,48,47,98])
    # H2 kill leg: 75/1847=0.04061 vs diplomatic P("ne")=0.00850 (corpus-side, banked)
    chk('H2 kill 4.78x (cipher part)', round((75/1847)/0.00850, 2), 4.78)
    # R4: 84 en-islet re-scope — «qu'en» legs WITHDRAWN (46-84-24-37-78 x2)
    chk('46-84-24-37-78 x2', [i for i in range(1843)
                              if pairs[i:i+5] == [46,84,24,37,78]], [309,472])
    # conditional extensions (on 66/89 noun-class readings — leads, not provisional)
    chk('66-84 84-indices', sorted(i for i, p in enumerate(pairs)
                                   if p == 84 and i > 0 and pairs[i-1] == 66),
        [154,1151])
    chk('89-84 84-indices', sorted(i for i, p in enumerate(pairs)
                                   if p == 84 and i > 0 and pairs[i-1] == 89),
        [276,1378])
    chk('66-84 n_eff=2', len({(pairs[i-1], pairs[i], pairs[i+1])
                              for i in (154,1151)}), 2)
    chk('89-84 n_eff=2', len({(pairs[i-1], pairs[i], pairs[i+1])
                              for i in (276,1378)}), 2)
    chk('82-84 GT-anchored frame', [(pairs[i-1], pairs[i], pairs[i+1])
                                    for i in (167,)], [(82,84,53)])
    # R4c: noun identity NULL — «qui le [verb=84-59]» x2 REFERRED to round 9
    chk('64-77-84-59 x2', [i for i in range(1844)
                           if pairs[i:i+4] == [64,77,84,59]], [1445,1801])
    chk('06-84-59-46 S4#2 (pre(84)=06, unclassified)',
        [i for i in range(1844) if pairs[i:i+4] == [6,84,59,46]], [1188])
    # R7a: {93,8}="l'" LEAD — homophony legs cipher-side
    chk('n93/n8', (groups[93], groups[8]), (14,18))
    chk('(93|8)->62 starts', (pos2(93,62), pos2(8,62)), ([10,1685],[944,1323]))
    chk('93/8 shared predecessors',
        sorted({pairs[i-1] for i in range(1,1847) if pairs[i] == 93} &
               {pairs[i-1] for i in range(1,1847) if pairs[i] == 8}),
        [45,67,85])
    chk('93/8 shared followers',
        sorted({pairs[i+1] for i in range(1846) if pairs[i] == 93} &
               {pairs[i+1] for i in range(1846) if pairs[i] == 8}),
        [29,52,62])
    chk('94-93-59 "ne l\'est" @101', pairs[101:104], [94,93,59])
    chk('93->52 / 87->8 (fenced costs)', (big[(93,52)], big[(87,8)]), (2,1))
    # R7e: 06="ent"-iff-pre=82 LEAD (conditioned; falsifier frozen verbatim)
    chk('06 pre==82 06-indices', sorted(i for i, p in enumerate(pairs)
                                        if p == 6 and i > 0 and pairs[i-1] == 82),
        [580,738,1184,1355])
    chk('06-islet n_eff=3', len({(pairs[i-1], pairs[i], pairs[i+1])
                                 for i in (580,738,1184,1355)}), 3)
    chk('GT core 94-82-06-06 starts', [i for i in range(1844)
                                        if pairs[i:i+4] == [94,82,6,6]],
        [578,1182])
    # R6: @1248 fork counterdatum fenced n=1 (67 at 1248; window starts 1246)
    chk('@1246 window [16,00,67,46,26]', pairs[1246:1251], [16,0,67,46,26])

    # ---- R9BANK2 (2026-10-07, round-9 final pass: R8/R9 cipher-side facts) ----
    # Conditioner 86 battery (que-family REFUTED)
    chk('n86', groups[86], 32)
    chk('86->70 / 86->52 / 86->56', (big[(86,70)], big[(86,52)], big[(86,56)]),
        (1,2,4))
    chk('77->86 starts', pos2(77,86), [430,798,877,950,1133])
    # Conditioner 66/89 classes (CONFIRMED)
    chk('00->66 x7', pos2(0,66), [188,245,253,714,1108,1493,1532])
    chk('n89', groups[89], 14)
    chk('77->89 / 29->89 / 89->48', (big[(77,89)], big[(29,89)], big[(89,48)]),
        (2,5,3))
    # Conditioner formulas (HOLD / refined, no promotion)
    chk('64-96-43 @341/@1025', [i for i in range(1845)
                                if pairs[i:i+3] == [64,96,43]], [341,1025])
    chk('45-64-96-43-87-01 6-mer', [i for i in range(1842)
                                    if pairs[i:i+6] == [45,64,96,43,87,1]],
        [340,1024])
    # Successor48 (H_verb dead; datum correction)
    chk('48->52 @283/@1737', pos2(48,52), [283,1737])
    chk('48 distinct successors = 29 (not 19)',
        len({pairs[i+1] for i in range(1846) if pairs[i] == 48}), 29)
    chk('n52/n96', (groups[52], groups[96]), (27,21))
    # Resolver62 (HOLD; C1-C4 tested-NULL)
    chk('62->59 / 59->62', (big[(62,59)], big[(59,62)]), (0,0))
    chk('62->(93|8) @1539', [i for i in range(1846)
                             if pairs[i] == 62 and pairs[i+1] in (93,8)],
        [1539])
    chk('PAIRS[100:104] 62-94-93-59', pairs[100:104], [62,94,93,59])
    # Finisher67 windows
    chk('@199 ctx', pairs[197:202], [60,8,67,76,87])
    chk('@630 ctx', pairs[629:633], [78,67,8,52])

    # ---- R10BANK (2026-10-07, round-10 red-team extension) ----
    # Round-10 adjudicated facts (code/crowd10/redteam/RULINGS-ROUND10.md),
    # cipher-side stream numbers only. Existing checks untouched.
    # R7 conditioner59 — ISLET 10 (granted with F33 narrowing)
    chk('59 est-arm windows (pre in {64,94,93}, excl S5-fenced @1796)',
        sorted(i for i in range(1847)
               if pairs[i] == 59 and pairs[i-1] in (64,94,93) and i != 1796),
        [103,316,559,763,1210,1777])
    chk('59 pre=94 @1796 is S5-fenced (suc=37)', pairs[1797], 37)
    chk('59 este-arm pre=84 windows', sorted(i for i in range(1847)
                                             if pairs[i] == 59 and pairs[i-1] == 84),
        [1190,1291,1448,1804])
    chk('59->46 (S4, both re-read verb+que)', pos2(59,46), [216,1190])
    chk('@463 pre=11 (anti-unconditioned datum)', (pairs[462],pairs[464]), (11,42))
    chk('@103 ctx', pairs[100:105], [62,94,93,59,45])
    # R7: pre=06/61/44/86 windows are F33-fenced OBSERVATIONS per R7
    # (post-hoc condition expansions — NOT islet legs; @216's verb re-read
    # granted only as F52-caveat-3 dissolution). Positions banked as drift guards.
    chk('59 pre=06 windows (F33-fenced observations, not islet legs)',
        sorted(i for i in range(1847) if pairs[i]==59 and pairs[i-1]==6),
        [216,1186])
    chk('59 pre in {61,44} windows (@448/@1715 frame-forced observations;'
        ' @528 S5-fenced, @1511 leftover)', sorted(i for i in range(1847)
                                                  if pairs[i]==59 and pairs[i-1] in (61,44)),
        [448,528,1511,1715])
    chk('59 pre=86 window (F33-fenced lean observation)', [i for i in range(1847)
                                       if pairs[i]==59 and pairs[i-1]==86], [554])
    # R5 resolver1351 — @1351-1356 window
    chk('@1351-1356', pairs[1351:1357], [77,78,94,82,6,52])
    chk('other 94 in 1340-1370', [i for i in range(1340,1371) if pairs[i]==94],
        [1353,1363])
    # R4 arm1248
    chk('67->46 positions', [i for i in range(1846)
                             if pairs[i]==67 and pairs[i+1]==46], [471,1248])
    chk('00->67 singleton', [i for i in range(1846)
                             if pairs[i]==0 and pairs[i+1]==67], [1247])
    chk('no 62 in @1242-1255', [i for i in range(1242,1255) if pairs[i]==62], [])
    # R3 finisher67 round-10 L2 contacts
    chk('11->31 / 11->98 / 11->33', (big[(11,31)],big[(11,98)],big[(11,33)]),
        (1,0,0))
    chk('64->31 adverse', big[(64,31)], 2)
    # R2 watch06 — H4g frame positions (REFUTED per pre-registered bar)
    chk('94-82-06-06 starts', [i for i in range(1844)
                               if pairs[i:i+4]==[94,82,6,6]], [578,1182])
    def _p_comb_fn():
        import math as _m
        def _plit(k):
            return _m.comb(4,k)/_m.comb(44,k) if k <= 4 else 0.0
        _p_suc = 1 - (1-_plit(2))**6*(1-_plit(4))**3*(1-_plit(3))*(1-_plit(6))
        _p_pre2 = 1 - (1-_plit(2))**2*(1-_plit(3))**3*(1-_plit(4))**2
        return 1 - (1-_p_suc)*(1-_p_pre2)
    chk('H4g p_comb literal (PREREG "same p_k form")',
        round((_p_comb_fn()),6), 0.050810)

    # ---- R11BANK (2026-10-07, round-11 red-team extension) ----
    # Round-11 adjudicated facts (code/crowd11/redteam/RULINGS-ROUND11.md,
    # finalized R1-R7), cipher-side stream numbers only; corpus-side legs are
    # banked with provenance in the verify_round7.py ROUND11-LEDGER extension.
    # Existing checks untouched.
    # R3 census33 — 33 = infinitive-class (C1); fork @1450/@1623 lean-veut LEAN
    chk('n33', groups[33], 25)
    chk('00->33 x8', big[(0,33)], 8)
    chk('33->29 x5', big[(33,29)], 5)
    # R5 arm1248 — peu STRENGTHENED 4/8; empêcher-class WEAK-FENCED 3/7
    # (label corrected: the 11-token frame spans 1244-1254; the R5 ruling's
    # "@1244-1256" label is +2 — values byte-exact)
    chk('@1244-1254 pour 33 16 pour 67 que frame', pairs[1244:1255],
        [0,33,16,0,67,46,26,30,6,65,46])
    chk('@470-473', pairs[470:474], [6,67,46,84])
    # R6 finisher67 — @633 -> et-CONDITIONAL(C1^C2); fork SUPPORTED, fenced n=2
    chk('@631-635', pairs[631:636], [8,52,67,63,74])
    chk('11->52 / 08->52', (big[(11,52)], big[(8,52)]), (3,1))
    chk('11->31 / 64->31 / 08->31', (big[(11,31)], big[(64,31)], big[(8,31)]),
        (1,2,3))
    chk('@1421-1426 veut-arm window', pairs[1421:1427], [33,21,67,33,29,87])
    chk('n92 / 00->92 / 46->92 / 11->92', (groups[92], big[(0,92)],
                                          big[(46,92)], big[(11,92)]),
        (22,6,1,3))
    chk('11->98 / n98 / 46->16 / 11->16', (big[(11,98)], groups[98],
                                           big[(46,16)], big[(11,16)]),
        (0,40,0,0))
    # R7 anchorer48 — 3 fences (A, B-premise, D-conditional); cipher-side windows
    chk('62->48 48-positions (on-frames)', sorted(i for i in range(1,1847)
        if pairs[i] == 48 and pairs[i-1] == 62), [361,426,1316,1350,1465,1570])
    chk('82->48 48-positions (m-frames)', sorted(i for i in range(1,1847)
        if pairs[i] == 48 and pairs[i-1] == 82), [126,377,398,1229])
    chk('48->(77|11) pronoun-cell windows',
        sorted(i for i in range(1846) if pairs[i] == 48 and pairs[i+1] in (77,11)),
        [126,1076,1350])
    chk('@1076 frame pre=12', pairs[1075:1080], [12,48,77,78,64])
    chk('48->47 window starts (@863, @1658)',
        sorted(i for i in range(1846) if pairs[i] == 48 and pairs[i+1] == 47),
        [863,1658])

    # ---- R12BANK (2026-10-07, round-12 red-team extension) ----
    # Round-12 adjudicated facts (code/crowd12/redteam/RULINGS-ROUND12.md,
    # finalized R1-R7), cipher-side stream numbers only; corpus-side legs are
    # banked with provenance in the verify_round7.py ROUND12-LEDGER extension.
    # Existing checks untouched.
    # R1 identifier33 — 33-value paradox recorded; 8 "pour 33" cluster tails
    chk('R1 F-A tails @186/@1245', (pairs[186:190], pairs[1245:1249]),
        ([33,16,0,66],[33,16,0,67]))
    chk('R1 F-B tail @408', pairs[408:411], [33,1,2])
    chk('R1 F-C tails @467/@1088', (pairs[467:470], pairs[1088:1091]),
        ([33,79,80],[33,79,80]))
    chk('R1 F-D tail @846', pairs[846:849], [33,96,40])
    chk('R1 F-E tails @936/@1630', (pairs[936:939], pairs[1630:1633]),
        ([33,21,64],[33,21,64]))
    # R2 veutleg — second leg NULL (clean null); census positions
    chk('R2 n36 / n66', (groups[36], groups[66]), (9,19))
    chk('R2 36 positions excl decider @1449',
        sorted(i for i,p in enumerate(pairs) if p==36 and i!=1449),
        [388,421,740,1174,1215,1313,1585,1834])
    chk('R2 66 positions excl decider @1622',
        sorted(i for i,p in enumerate(pairs) if p==66 and i!=1622),
        [88,123,140,153,189,246,254,457,705,715,766,1018,1109,1150,
         1346,1459,1494,1533])
    chk('R2 00->66 x7 (lead L1)', (big[(0,66)],
        sorted(i for i in range(1846) if pairs[i]==0 and pairs[i+1]==66)),
        (7,[188,245,253,714,1108,1493,1532]))
    chk('R2 36 suc=29', [i for i in range(1846)
        if pairs[i]==36 and pairs[i+1]==29], [421])
    chk('R2 66 pre=77', [i for i in range(1847) if pairs[i]==66
        and pairs[i-1]==77], [88])
    chk('R2 33->46 only decider pair', [i for i in range(1846)
        if pairs[i]==33 and pairs[i+1]==46], [1451,1624])
    # R3 class3192 — 31=VERBAL prov-cond; 92 H-pre REFUTED / H-presuc FENCED
    chk('R3 n31', groups[31], 8)
    chk('R3 64->31 (qui-relative windows @338/@1647)',
        [i for i in range(1846) if pairs[i]==64 and pairs[i+1]==31],
        [337,1646])
    chk('R3 @1486-1489 D-ce window (est-ce confound killed)',
        pairs[1486:1490], [24,87,8,31])
    chk('R3 @683 POUR-arm cross-signature (H-pre falsifier)',
        pairs[681:687], [7,0,92,64,29,40])
    chk('R3 @1154 INF-islet', pairs[1152:1158], [2,0,92,29,80,17])
    chk('R3 64->29 (T1/T2 -quiere tension)', [i for i in range(1846)
        if pairs[i]==64 and pairs[i+1]==29], [290,684,1199])
    chk('R3 92 VERB-arm pre in {94,46}',
        sorted((pairs[i-1],i) for i,p in enumerate(pairs)
               if p==92 and pairs[i-1] in (94,46)),
        [(46,1453),(94,66),(94,1550)])
    # R4 followup48 — ML-1 OPEN; ML-2 scope-corrected; @863 POINTER-ONLY;
    # @1077->@1078 prose correction byte-exact
    chk('R4 @1075-1081 (ML-1 frame; 77@1077, 78@1078)',
        pairs[1075:1081], [12,48,77,78,64,6])
    chk('R4 n12', groups[12], 23)
    chk('R4 12->48', [i for i in range(1846)
        if pairs[i]==12 and pairs[i+1]==48], [169,709,809,1075,1736])
    chk('R4 78->29 absent (0/31)', [i for i in range(1846)
        if pairs[i]==78 and pairs[i+1]==29], [])
    chk('R4 @862-865 (48-47-46 de-ce frame)', pairs[862:866], [74,48,47,46])
    chk('R4 64->6', [i for i in range(1846)
        if pairs[i]==64 and pairs[i+1]==6], [1079,1666])
    chk('R4 77->78 x7', [i for i in range(1846)
        if pairs[i]==77 and pairs[i+1]==78], [7,213,647,1077,1180,1351,1542])
    # R5 rerun1248 — PC-1 leg (peu 4/8->5/9); DP-1 explicit fence;
    # pre(06@470)=80: ISLET-3 does not cover @471
    chk('R5 @469-473 (pre(06@470)=80)', pairs[469:474], [80,6,67,46,84])
    # R6 estetie — H0 holds; T5 clean negative; 06="pro" compat-unconfirmed
    chk('R6 64-77-84-59 starts (T5 clean negative, exactly 2x)',
        [i for i in range(1844) if pairs[i:i+4]==[64,77,84,59]], [1445,1801])
    chk('R6 @1291 window', pairs[1288:1296], [11,17,84,59,35,94,52,80])
    chk('R6 @1188-1190 (pre(06@1188)=42, ISLET-3 off)',
        (pairs[1188:1191], pairs[1187]), ([6,84,59],42))
    # R8 french-blitz — Mehemet-Ali discriminator (adjudicated; see RULINGS-ROUND12 R8)
    chk('R8 @8 window', pairs[8:13], [78,18,93,62,98])
    # R9 french-blitz — gouvernement re-reader (adjudicated; see RULINGS-ROUND12 R9)
    # 77="gouv" DEMOTED->disfavored; "gouvernement"/"gouvernent" readings KILLED
    chk('R9 5-mer @1180', pairs[1180:1185], [77,78,94,82,6])
    chk('R9 5-mer @1351', pairs[1351:1356], [77,78,94,82,6])
    # R10 french-blitz — premiere-noun hunter (adjudicated; see RULINGS-ROUND12 R10)
    # "la premiere fois" @1034 LEAD; e-initial-noun theory RETIRED permanently
    chk('R10 @754 la-premiere window', pairs[754:762], [11,70,82,34,29,40,20,62])
    chk('R10 @1034 la-premiere window', pairs[1034:1042], [11,70,82,34,29,40,17,77])
    # R11 french-blitz — 59-frame mapper (adjudicated; see RULINGS-ROUND12 R11)
    # ISLET-10 HOLDS (no widening); 59 provisional HOLDS; canonical.py bug contained
    chk('R11 n59', groups[59], 27)
    chk('R11 est-arm 6/6 (pre-59-suc frames)',
        [pairs[w-1:w+2] for w in (103,316,559,763,1210,1777)],
        [[93,59,45],[64,59,32],[94,59,30],[94,59,39],[64,59,32],[64,59,19]])
    chk('R11 este-arm 3/3 (pre=84 verb-final)',
        [pairs[w-1:w+2] for w in (1190,1448,1804)],
        [[84,59,46],[84,59,36],[84,59,35]])
    chk('R11 @463 F1-WATCH frame', pairs[462:465], [11,59,42])
    chk('R11 @825 candidate frame', pairs[824:827], [87,59,38])
    chk('R11 S5-fenced @528/@1443/@1796',
        [pairs[w-1:w+2] for w in (528,1443,1796)],
        [[44,59,37],[68,59,37],[94,59,37]])
    # R12 french-blitz — formulae miner (adjudicated; see RULINGS-ROUND12 R12)
    # "par ce que"x3 corroboration-grade (NOT a new leg); "par le"x3 corroboration
    chk('R12 par-ce-que @224/@952/@1526',
        [pairs[w:w+3] for w in (224,952,1526)],
        [[96,87,46]]*3)
    chk('R12 par-le @47/@465/@960',
        [pairs[w:w+2] for w in (47,465,960)],
        [[96,0]]*3)
    chk('R12 head @0 (null recorded)', pairs[0:6], [9,0,97,51,47,41])
    chk('R12 @998 (conditioner WO)', pairs[997:1000], [11,96,82])
    chk('R12 96->11 absent', [i for i in range(1846)
        if pairs[i]==96 and pairs[i+1]==11], [])
    # R13 french-blitz — 48 syntax battery (adjudicated; see RULINGS-ROUND12 R13)
    # unconditioned-48="de" KILLED (11 windows, kill-grade); 48 UNIDENTIFIED
    chk('R13 n48', groups[48], 38)
    chk('R13 48 positions (38)',
        [i for i,p in enumerate(pairs) if p==48],
        [126,170,283,361,365,377,398,426,450,542,641,710,729,810,856,863,
         872,928,972,987,1076,1177,1212,1221,1229,1276,1279,1316,1350,
         1398,1465,1525,1570,1589,1614,1658,1737,1779])
    chk('R13 kill: 48->0 @377', pairs[377:379], [48,0])
    chk('R13 kill: 48->24 @810', pairs[810:812], [48,24])
    chk('R13 kill: 48->59 @1177', pairs[1177:1179], [48,59])
    chk('R13 kill: 48->96 @1212', pairs[1212:1214], [48,96])
    chk('R13 kill: 11->48 @1525', pairs[1524:1526], [11,48])
    chk('R13 kill: 62->48 x6 (on-de 0 genuine)',
        [i for i in range(1846) if pairs[i]==62 and pairs[i+1]==48],
        [360,425,1315,1349,1464,1569])
    chk('R13 S1: 82->48 x4 (m-48 vowel-initial conditional)',
        [i for i in range(1846) if pairs[i]==82 and pairs[i+1]==48],
        [125,376,397,1228])

    # ---- R13BANK (2026-10-07, round-13 red-team extension) ----
    # Round-13 adjudicated facts (code/crowd13/adjudicator/RULINGS-ROUND13.md,
    # finalized R-DRAG, R-CD1, R-CD2, R-IA1..R-IA7, R-CC92, R-AB1, R-AB2,
    # R-CC31, R-CC33, R-CR48, R-CR1248, R-CRESTE, R-MM1, R-MM2), cipher-side
    # stream numbers only; corpus-side legs are banked with provenance in the
    # verify_round7.py ROUND13-LEDGER extension. Existing checks untouched.
    # R-DRAG: 6 new hit trigrams (null verdict; FDR=12.7/9=1.41)
    chk('R13 drag: le-prince x2', (pairs[1240:1243], pairs[1401:1404]),
        ([77,81,87],[77,81,87]))
    chk('R13 drag: tout-ce-qui x4',
        (pairs[179:182], pairs[1766:1769], pairs[1774:1777], pairs[1799:1802]),
        ([24,87,64],[24,87,64],[24,87,64],[79,87,64]))
    # R-CD1: {52,59} SPLIT — frame-table windows (index = 52 position)
    chk('R13 CD1: 52 frame trigrams',
        (pairs[1341:1344], pairs[1293:1296], pairs[1806:1809],
         pairs[1434:1437], pairs[159:162], pairs[263:266], pairs[570:573]),
        ([64,52,38],[94,52,80],[94,52,80],[64,52,82],[93,52,94],
         [93,52,33],[94,52,87]))
    chk('R13 CD1: pre(59)=84 x4 (este-arm exclusivity)',
        [i for i in range(1846) if pairs[i]==84 and pairs[i+1]==59],
        [1189,1290,1447,1803])
    # R-CD2: {76,78} SPLIT
    chk('R13 CD2: 76->94 = 0',
        [i for i in range(1846) if pairs[i]==76 and pairs[i+1]==94], [])
    chk('R13 CD2: 78->94 x2',
        [i for i in range(1846) if pairs[i]==78 and pairs[i+1]==94],
        [1181,1352])
    chk('R13 CD2: le-76 x3', (pairs[832:835], pairs[891:894], pairs[968:971]),
        ([77,76,59],[77,76,1],[77,76,1]))
    chk('R13 CD2: 94->76 x2',
        [i for i in range(1846) if pairs[i]==94 and pairs[i+1]==76],
        [651,1576])
    # R-IA1: ISLET-10 dissolved — word-rule frame anchors
    chk('R13 IA1: 93-59 / 94-59 / 84-59 frame anchors',
        (sorted(i for i in range(1846) if pairs[i]==93 and pairs[i+1]==59),
         sorted(i for i in range(1846) if pairs[i]==94 and pairs[i+1]==59)),
        ([102],[558,762,1795]))
    chk('R13 IA1: 84-59 firm windows', pairs[1447:1450], [84,59,36])
    # R-IA2: ISLET-8 frames (corrected frame starts @1444/@1800)
    chk('R13 IA2: qui-le-este frames',
        (pairs[1444:1451], pairs[1800:1807]),
        ([37,64,77,84,59,36,67],[87,64,77,84,59,35,94]))
    # R-IA3: ISLET-1 arms
    chk('R13 IA3: 82-84 @166', pairs[166:168], [82,84])
    chk('R13 IA3: 66-84 @153/@1150',
        (pairs[153:156], pairs[1150:1153]), ([66,84,26],[66,84,2]))
    chk('R13 IA3: 89-84 @275/@1377',
        (pairs[275:278], pairs[1377:1380]), ([89,84,91],[89,84,92]))
    chk('R13 IA3: n84', groups[84], 25)
    # R-IA4: ISLET-2/3 word rules (96-00 start @960 corrected)
    chk('R13 IA4: 96-00 x3',
        [i for i in range(1846) if pairs[i]==96 and pairs[i+1]==0],
        [47,465,960])
    chk('R13 IA4: W06 06-positions subset',
        all(p in [i for i,pp in enumerate(pairs) if pp==6]
            for p in [580,738,1184,1355]), True)
    # R-IA6: ISLET-4 true polyvalence — @1248 NEITHER-fence window
    chk('R13 IA6: @1248 window', pairs[1248:1251], [67,46,26])
    # R-IA7: ISLET-5 singleton
    chk('R13 IA7: 64-96-47 @150', pairs[149:153], [64,96,47,46])
    # R-CC92: 92 POUR-arm windows (pre=00)
    chk('R13 CC92: 92 POUR-arm x6',
        (pairs[49:52], pairs[330:333], pairs[593:596],
         pairs[683:686], pairs[978:981], pairs[1154:1157]),
        ([92,79,37],[92,50,45],[92,79,85],[92,64,29],[92,7,76],[92,29,80]))
    chk('R13 CC92: pre(92)=00 x6', [pairs[i-1] for i in
        [49,330,593,683,978,1154]], [0,0,0,0,0,0])
    # R-AB1: {33,86} SPLIT — disjoint pour-successors
    chk('R13 AB1: 33 pour-successors',
        sorted((pairs[i],pairs[i+1],pairs[i+2])
               for i in range(1845) if pairs[i]==0 and pairs[i+1]==33),
        sorted([(0,33,16),(0,33,16),(0,33,1),(0,33,79),(0,33,79),
                (0,33,96),(0,33,21),(0,33,21)]))
    chk('R13 AB1: 86 pour-successor count', sum(
        1 for i in range(1845) if pairs[i]==0 and pairs[i+1]==86), 12)
    chk('R13 AB1: 77->33 = 0',
        [i for i in range(1846) if pairs[i]==77 and pairs[i+1]==33], [])
    chk('R13 AB1: 77->86 x5',
        [i for i in range(1846) if pairs[i]==77 and pairs[i+1]==86],
        [430,798,877,950,1133])
    # R-AB2: {48,94} SPLIT
    chk('R13 AB2: n48/n94', (groups[48], groups[94]), (38,37))
    # R-CC31: 31=VERBAL CONFIRM — byte-identical re-derivation
    chk('R13 CC31: D-ce @1488', pairs[1488:1492], [8,31,92,39])
    chk('R13 CC31: qui-relative @338/@1647',
        (pairs[338:341], pairs[1647:1650]), ([31,14,45],[31,10,3]))
    # R-CC33: 8 "pour 33" frames
    chk('R13 CC33: pour-33 x8',
        (pairs[186:189], pairs[408:411], pairs[467:470], pairs[846:849],
         pairs[936:939], pairs[1088:1091], pairs[1245:1248], pairs[1630:1633]),
        ([33,16,0],[33,1,2],[33,79,80],[33,96,40],[33,21,64],
         [33,79,80],[33,16,0],[33,21,64]))
    # R-CR48: 48 follow-ups
    chk('R13 CR48: 74->77 x2 (verb-adverse)',
        [i for i in range(1846) if pairs[i]==74 and pairs[i+1]==77],
        [212,1677])
    chk('R13 CR48: 48-47 starts',
        [i for i in range(1846) if pairs[i]==48 and pairs[i+1]==47],
        [863,1658])
    chk('R13 CR48: 48->29 x2 / 48->40 x1 (H_stem windows)',
        ([i for i in range(1846) if pairs[i]==48 and pairs[i+1]==29],
         [i for i in range(1846) if pairs[i]==48 and pairs[i+1]==40]),
        ([1229,1589],[1398]))
    # R-CR1248: double-pour stack bytes pairs[1244:1255]
    chk('R13 CR1248: double-pour stack',
        pairs[1244:1256], [0,33,16,0,67,46,26,30,6,65,46,1])
    # R-MM1: deficit arithmetic anchors (n48/n94/n52/n59/n76/n78)
    chk('R13 MM1: n52/n59/n76/n78',
        (groups[52], groups[59], groups[76], groups[78]), (27,27,21,31))

    # ---- R14BANK (2026-10-07, round-14 red-team pre-registration extension) ----
    # Appends the round-14 standing inputs (round-13 adjudicated facts, F100-F113
    # / N60) that the round-14 work orders build on, as cipher-side stream
    # checks. Bars live in code/crowd14/redteam/PREREG14.md (locked before any
    # round-14 executor output was read). Existing checks untouched.
    # R14: ISLET-3 census — 82->06 (predecessor positions; the cited
    # [580,738,1184,1355] are the 06/successor positions)
    chk('R14: 82->06 census (ISLET-3, F77)',
        [i for i in range(1846) if pairs[i]==82 and pairs[i+1]==6],
        [579,737,1183,1354])
    # R14: 76 ver-tine windows (F103 — 76 fits ONLY ver-initial)
    chk('R14: 76 windows @833/@892/@969',
        (pairs[833:835], pairs[892:894], pairs[969:971]),
        ([76,59],[76,1],[76,1]))
    # R14: "le prince" x2 byte-identical (F108 — 81="prin" battery venue, WO3)
    chk('R14: le-prince x2 byte-identical',
        (pairs[1240:1244], pairs[1401:1405]),
        ([77,81,87,11],[77,81,87,11]))
    # R14: "la 52" x3 (F103 residual — 52's non-est battery venue, WO5)
    chk('R14: la-52 x3',
        [i for i in range(1846) if pairs[i]==11 and pairs[i+1]==52],
        [1006,1123,1721])
    # R14: @825 "en ce"+noun frame (WO7 — 59's third-value venue;
    # word-"est" ruled out there per F71)
    chk('R14: @825 en-ce frame',
        pairs[823:830], [24,87,59,38,82,1,24])
    # R14: @1355 "ne ment pas" window (F70 resolution, F77 gloss rare-but-real)
    chk('R14: @1349-1361 window',
        pairs[1349:1362], [62,48,77,78,94,82,6,52,37,64,35,13,92])
    # R14: W-est1 93-59="l'est" singleton (ISLET-10 dissolution, F100)
    chk('R14: W-est1 93->59 @102',
        [i for i in range(1846) if pairs[i]==93 and pairs[i+1]==59],
        [102])
    # R14: n67 (fork tally venue) / n81 (prin battery venue)
    chk('R14: n67/n81', (groups[67], groups[81]), (38,14))
    # R14: KE2 — 87 follower ranks, 64 above 46 (F104 R1)
    chk('R14: KE2 87->11 x7 / 87->64 x5 / 87->46 x3',
        (big[(87,11)], big[(87,64)], big[(87,46)]), (7,5,3))
    # R14: F42 A2 bound — 47 is NOT the same "ce" as 87 (47->64 zero)
    chk('R14: 47->64 zero', pos2(47,64), [])
    # R14: 96-87-46 frame starts (F19 "parce que")
    chk('R14: 96->87 frame starts', pos2(96,87), [224,952,1526])
    # R14: 76->94 zero (ver-islet exclusion; 78->94=2 banked at F38)
    chk('R14: 76->94 zero', big[(76,94)], 0)

    # ---- R14BANK-close (2026-10-07, round-14 red-team adjudication) ----
    # Cipher-side stream numbers behind the round-14 rulings R-001..R-009
    # (code/crowd14/redteam/RULINGS-ROUND14.md). All re-derived by the red
    # team against the repaired 1,847-pair stream. Existing checks untouched.
    # R-004: 74-74 self-bigrams (74=syllable-class leg)
    chk('R14b: 74-74 x6',
        [i for i in range(1846) if pairs[i]==74 and pairs[i+1]==74],
        [417,816,861,919,1053,1637])
    # R-004: @862-866 "de ce que" frame (48="de" islet venue)
    chk('R14b: @862-866 frame', pairs[862:867], [74,48,47,46,0])
    # R-004: B3a 82="m" GT elision licensor @1228
    chk('R14b: [1228]=82 (m-GT)', pairs[1228], 82)
    # R-005: 62->48 window starts (polyvalence battery)
    chk('R14b: 62->48 starts',
        [i for i in range(1846) if pairs[i]==62 and pairs[i+1]==48],
        [360,425,1315,1349,1464,1569])
    # R-006: la-52 5-gram x2 (formulaic la-arm, n_eff=2)
    chk('R14b: 6-11-52-37-43 x2',
        (pairs[1122:1127], pairs[1720:1725]),
        ([6,11,52,37,43],[6,11,52,37,43]))
    # R-006: Vstem-arm 52s (pre in {6,86}; referral, not run)
    chk('R14b: Vstem-arm 52s',
        [(i, pairs[i-1]) for i in range(1847)
         if pairs[i]==52 and pairs[i-1] in (6,86)],
        [(1081,6),(1100,86),(1129,86),(1356,6)])
    # R-006: 11->59 @463 (same-pre/different-suc allophone datum)
    chk('R14b: 11->59 @463', pairs[462:464], [11,59])
    # R-007: "la 78" x2 (H0-er kill, GT-anchored)
    chk('R14b: 11->78 x2',
        [i for i in range(1846) if pairs[i]==11 and pairs[i+1]==78],
        [296,1669])
    # R-008: 87->59 sole window (@825 = 59 cell)
    chk('R14b: 87->59 sole',
        [i for i in range(1846) if pairs[i]==87 and pairs[i+1]==59],
        [824])
    # R-002: @460 "tout cela est" (second tout-frame datum)
    chk('R14b: @460 tout-cela-est', pairs[460:464], [79,87,11,59])

    # ---- R15BANK (2026-10-07, round-15 red-team adjudication) ----
    # Cipher-side stream numbers behind the next-token battery rulings
    # (code/crowd15/report_inbox/next-token-redteam.md, A1-A16 + P1).
    # All re-derived by the red team against the repaired 1,847-pair stream.
    # Existing checks untouched. Position convention: bigram/trigram START
    # indices (0-based); batteries sometimes cite the key cell (+1/+2) --
    # the physical cells are identical.
    # A1: est->X frames (37/32/42 PROMOTE, 19 HOLD)
    chk('R15: 59->37 x6', pos2(59,37), [528,624,912,1178,1443,1796])
    chk('R15: 59->32 x3', pos2(59,32), [316,448,1210])
    chk('R15: 59->42 x2', pos2(59,42), [463,1186])
    chk('R15: 59->19 x1', pos2(59,19), [1777])
    # F71 correction: est-arm = 7 (64-59 x3 + 94-59 x3 + 93-59 x1), not 6
    chk('R15: F71 94->59 x3', pos2(94,59), [558,762,1795])
    chk('R15: F71 64->59 x3', pos2(64,59), [315,1209,1776])
    chk('R15: F71 93->59 x1', pos2(93,59), [102])
    # A2: 23/26 SPLIT (suc-class {12,30,00}: 23 0/8 vs 26 11/17)
    chk('R15: A2 23 never takes {12,30,00}',
        [b for a,b in big if a==23 and b in (12,30,0)], [])
    chk('R15: A2 26 takes {12,30,00} x11',
        sum(big[(26,b)] for b in (12,30,0)), 11)
    # A3: "parce qu'en" @952 (24-tail only at @952)
    chk('R15: A3 96-87-46 x3', pos2(96,87) and
        [i for i in range(1845) if (pairs[i],pairs[i+1],pairs[i+2])==(96,87,46)],
        [224,952,1526])
    chk('R15: A3 tails 98/24/21',
        [pairs[i+3] for i in (224,952,1526)], [98,24,21])
    chk('R15: A3 85 pre=24 x5',
        sum(1 for i in range(1,1847) if pairs[i]==85 and pairs[i-1]==24), 5)
    # A4: 47="ce" allophone (87<-24 x10 vs 47<-24 x1)
    chk('R15: A4 87 pre=24 x10',
        sum(1 for i in range(1,1847) if pairs[i]==87 and pairs[i-1]==24), 10)
    chk('R15: A4 47 pre=24 x1',
        sum(1 for i in range(1,1847) if pairs[i]==47 and pairs[i-1]==24), 1)
    chk('R15: A4 47->46 x3', pos2(47,46), [151,548,864])
    chk('R15: A4 87->46 x3', pos2(87,46), [225,953,1527])
    chk('R15: A4 tail parity 3/1',
        (sum(1 for i in pos2(87,46) if pairs[i-1]==96),
         sum(1 for i in pos2(47,46) if pairs[i-1]==96)), (3,1))
    # A5: 79="tout" (3 compositional legs)
    chk('R15: A5 79-17 x2', pos2(79,17), [451,1460])
    chk('R15: A5 79-87-11 @460',
        [i for i in range(1845) if (pairs[i],pairs[i+1],pairs[i+2])==(79,87,11)],
        [460])
    chk('R15: A5 79-87-64 @1799',
        [i for i in range(1845) if (pairs[i],pairs[i+1],pairs[i+2])==(79,87,64)],
        [1799])
    chk('R15: A5 79-80 x3', pos2(79,80), [468,1010,1089])
    # A6: [09/92]-qui-er-e-65 anchors (direction correction)
    chk('R15: A6 anchor09 @289', pairs[289:294], [9,64,29,40,65])
    chk('R15: A6 anchor92 @683', pairs[683:688], [92,64,29,40,65])
    chk('R15: A6 92 pre=00 x6 vs 09 x0',
        (sum(1 for i in range(1,1847) if pairs[i]==92 and pairs[i-1]==0),
         sum(1 for i in range(1,1847) if pairs[i]==9 and pairs[i-1]==0)), (6,0))
    # A7: trigram (48="est" killed: 0/38 vs 59's 12/27 predicative)
    chk('R15: A7 79-82-48 x2',
        [i for i in range(1845)
         if (pairs[i],pairs[i+1],pairs[i+2])==(79,82,48)], [396,1227])
    chk('R15: A7 82-48 x4', pos2(82,48), [125,376,397,1228])
    chk('R15: A7 48->{37,32,35} x0',
        sum(big[(48,x)] for x in (37,32,35)), 0)
    chk('R15: A7 59->{37,32,35} x12',
        sum(big[(59,x)] for x in (37,32,35)), 12)
    # A8: 80/89 verb-frames, DISTINCT (zero shared suc classes)
    chk('R15: A8 87-77-80 @515', pairs[515:518], [87,77,80])
    chk('R15: A8 87-77-89 @869', pairs[869:872], [87,77,89])
    chk('R15: A8 80/89 shared sucs empty',
        sorted(set(b for a,b in big if a==80) &
               set(b for a,b in big if a==89)), [])
    # A9: 00="pour" (00->INF-class x20/55; "pour que" x4)
    chk('R15: A9 00->86 x12 + 00->33 x8', (big[(0,86)],big[(0,33)]), (12,8))
    chk('R15: A9 00-46 x4', pos2(0,46), [106,545,1545,1680])
    # A10: 33 que-valency (33-46 x2) + 33-29 x5
    chk('R15: A10 33-46 x2', pos2(33,46), [1451,1624])
    chk('R15: A10 33-29 x5', pos2(33,29), [273,626,1232,1424,1477])
    # A11: 45="ce" HOLD (0/22 pre=24; 45-64 x3)
    chk('R15: A11 45 pre=24 x0',
        sum(1 for i in range(1,1847) if pairs[i]==45 and pairs[i-1]==24), 0)
    chk('R15: A11 45-64 x3', pos2(45,64), [314,340,1024])
    # A12: 37-01 unit x3
    chk('R15: A12 37-01 x3', pos2(37,1), [939,1633,1817])
    # A13/A15: 84="on" (77-84 x7; qu'on en x2; mon @166; R1/R2 fenced)
    chk('R15: A15 77-84 x7', pos2(77,84),
        [145,259,1057,1446,1484,1763,1802])
    chk('R15: A15 qu-on-en x2',
        [i for i in range(1843)
         if tuple(pairs[i:i+5])==(46,84,24,37,78)], [309,472])
    chk('R15: A15 46-77-84-24-87 @1483',
        pairs[1483:1488], [46,77,84,24,87])
    chk('R15: A15 82-84 @166', pos2(82,84), [166])
    chk('R15: A15 R1 11-84 @1619 / R2 94-84 @1664',
        (pos2(11,84),pos2(94,84)), ([1619],[1664]))
    chk('R15: A15 84->59 x4 + 84->24 x3', (big[(84,59)],big[(84,24)]), (4,3))
    # A14: par-le-X frames
    chk('R15: A14 96-00-92/33/86',
        ([i for i in range(1845) if (pairs[i],pairs[i+1],pairs[i+2])==(96,0,92)],
         [i for i in range(1845) if (pairs[i],pairs[i+1],pairs[i+2])==(96,0,33)],
         [i for i in range(1845) if (pairs[i],pairs[i+1],pairs[i+2])==(96,0,86)]),
        ([47],[465],[960]))
    # P1: cela = 87+11 x7 (mutual top-attraction banked in LEDGER)
    chk('R15: P1 87-11 x7', pos2(87,11),
        [74,163,201,461,830,1242,1403])

    # ---- R16BANK (2026-10-07, round-16 red-team adjudication extension) ----
    # Appends the cipher-side stream numbers behind the round-16 red-team
    # rulings (code/crowd16/report_inbox/next-token-redteam.md), re-derived
    # by the red team on the repaired 1,847-pair stream. Existing checks
    # untouched.
    #
    # R16-001: 77="le" PROMOTION DEMOTED (bar L1(b) failed: the three legs
    # are conditional on unbanked values; 80/89 verb-frames are conditional
    # on 77="le" per the round-15 ledger -> circular). Adverse dissolved;
    # 77 stays PROVISIONAL.
    chk('R16: n77', groups[77], 44)
    chk('R16: 87-77 "ce le" x2', pos2(87,77), [515,869])
    chk('R16: 77-76 x3', pos2(77,76), [832,891,968])
    chk('R16: @832 cela-boundary', pairs[828:838],
        [1,24,87,11,77,76,59,35,56,17])
    chk('R16: @516 "ce le [80]"', pairs[514:521], [56,87,77,80,9,70,91])
    chk('R16: @870 "ce le [89]"', pairs[868:875], [70,87,77,89,48,20,74])
    chk('R16: @1031 fenced adverse', pairs[1029:1036], [1,3,29,80,77,11,70])
    chk('R16: 77 follower top', groups[77] and
        Counter(pairs[i+1] for i in range(len(pairs)-1)
                if pairs[i]==77).most_common(5),
        [(78,7),(84,7),(86,5),(81,4),(76,3)])
    # R16-002: 84="on" WEAKENED (on-est x4 VOID per ISLET-10 classification;
    # 59-independent legs intact)
    _cls16 = json.load(open(LANE / 'code/crowd10/conditioner59'
                            / 'classification.json'))
    chk('R16: 84->59 x4 positions', pos2(84,59), [1189,1290,1447,1803])
    chk('R16: class 59@1190/1291/1448/1804',
        tuple(_cls16[str(k)]['class'] for k in (1190,1291,1448,1804)),
        ('ESTE','FENCED','ESTE','ESTE'))
    chk('R16: class 59@834 LEFTOVER (@832 leg reduced)',
        _cls16['834']['class'], 'LEFTOVER')
    chk('R16: 84 l-on x7 intact', pos2(77,84),
        [145,259,1057,1446,1484,1763,1802])
    chk('R16: 84->24 x3 intact', pos2(84,24), [310,473,1485])
    chk('R16: 82-84 "mon" @166 intact', pos2(82,84), [166])
    chk('R16: qu-on-en x2 intact',
        [i for i in range(len(pairs)-4)
         if tuple(pairs[i:i+5])==(46,84,24,37,78)], [309,472])
    # R16-003: 37/42 predicative frames DEMOTED -> HOLD (ISLET-10)
    chk('R16: 59->37 x6 all LEFTOVER',
        tuple(_cls16[str(k)]['class'] for k in (528,624,912,1178,1443,1796)),
        ('LEFTOVER',)*6)
    chk('R16: 59->42 void (LEFTOVER+ESTE)',
        tuple(_cls16[str(k)]['class'] for k in (463,1186)),
        ('LEFTOVER','ESTE'))
    chk('R16: 32 keeps 2 EST legs',
        tuple(_cls16[str(k)]['class'] for k in (316,1210)), ('EST','EST'))
    chk('R16: 59->30 @559 EST / @1715 ESTE (30="pas" lead)',
        tuple(_cls16[str(k)]['class'] for k in (559,1715)), ('EST','ESTE'))
    # R16-004: 45="ce" PROMOTE->HOLD ("ce verdict" x2 forces 45="dict";
    # "par ce" x2 forces 45="ce"; complementary distribution)
    chk('R16: 78-45 "verdict" x4', pos2(78,45), [313,573,982,1164])
    chk('R16: @573 "ce verdict" (87 banked)', pairs[571:575], [52,87,78,45])
    chk('R16: @982 "ce verdict" (47 granted)', pairs[980:984], [76,47,78,45])
    chk('R16: 96-45 "par ce" x2', pos2(96,45), [602,1213])
    chk('R16: 45-64 x3', pos2(45,64), [314,340,1024])
    chk('R16: @314 contested', pairs[311:320],
        [24,37,78,45,64,59,32,94,6])
    # R16-005: 78 "er" KILLED distributionally (OR=22.9); "ce 78" x7 frames;
    # @296 "l'ere" fenced residual for 78="ver" LEAD
    _det = {11,77,47,87}
    _d78 = sum(1 for i in range(1,len(pairs))
               if pairs[i]==78 and pairs[i-1] in _det)
    _d29 = sum(1 for i in range(1,len(pairs))
               if pairs[i]==29 and pairs[i-1] in _det)
    chk('R16: 78 det-pre 16/31', (_d78, groups[78]), (16,31))
    chk('R16: 29 det-pre 2/45', (_d29, groups[29]), (2,45))
    chk('R16: OR 22.93',
        round((_d78/(groups[78]-_d78))/(_d29/(groups[29]-_d29)),2), 22.93)
    chk('R16: 78 after 33 = 0; 29 after 33 = 5',
        (sum(1 for i in range(1,len(pairs)) if pairs[i]==78 and pairs[i-1]==33),
         sum(1 for i in range(1,len(pairs)) if pairs[i]==29 and pairs[i-1]==33)),
        (0,5))
    chk('R16: "ce 78" x7 (er ungrammatical)',
        sorted(i-1 for i in range(1,len(pairs))
               if pairs[i]==78 and pairs[i-1] in (47,87)),
        [363,572,628,818,981,1104,1396])
    chk('R16: @296 l-ere residual', pairs[294:302],
        [16,1,11,78,40,97,86,91])
    # R16-006: 94="ne" PROMOTE declined -> STRONG LEAD (conditional legs)
    chk('R16: 94-59 "n-est" x3', pos2(94,59), [558,762,1795])
    chk('R16: 94-82 "ne m" x4', pos2(94,82), [578,1182,1353,1742])
    chk('R16: 62-94 x9 / 62-48 x6', (big[(62,94)],big[(62,48)]), (9,6))
    # R16-007: record corrections to prior findings
    chk('R16: 67-33 x6 (was x1)', pos2(67,33),
        [272,1148,1423,1450,1476,1623])
    chk('R16: 12-48 x5 (was x7)', pos2(12,48), [169,709,809,1075,1736])
    chk('R16: 26-30 x4 (was x3)', pos2(26,30), [655,992,1250,1560])
    chk('R16: 26-12 x4', pos2(26,12), [240,842,1470,1707])
    chk('R16: 46-85-29 x0 (finder claim killed)',
        sum(1 for i in range(len(pairs)-2)
            if tuple(pairs[i:i+3])==(46,85,29)), 0)
    chk('R16: @95 is 46-29-85', pairs[93:100], [81,97,46,29,85,8,21])
    # R16-008: confirmed batteries (cipher-side)
    chk('R16: 31 followers 8/8 distinct',
        len(set(pairs[i+1] for i in range(len(pairs)-1) if pairs[i]==31)), 8)
    chk('R16: n79=18', groups[79], 18)
    chk('R16: 00 follower census',
        Counter(pairs[i+1] for i in range(len(pairs)-1)
                if pairs[i]==0).most_common(8),
        [(86,12),(33,8),(66,7),(92,6),(97,4),(11,4),(46,4),(36,3)])
    chk('R16: 65-94 exclusive x2', pos2(65,94), [687,1712])
    chk('R16: 20-62-94 x3', [i for i in range(len(pairs)-2)
        if tuple(pairs[i:i+3])==(20,62,94)], [760,839,1703])
    chk('R16: 67-77-81 x4 (fork-conditional)', pos2(67,77) and
        [i for i in range(len(pairs)-2)
         if tuple(pairs[i:i+3])==(67,77,81)], [743,1239,1400,1597])
    chk('R16: 17-11-26 x2 absolute', pos2(17,11) and
        [i for i in range(len(pairs)-2)
         if tuple(pairs[i:i+3])==(17,11,26)], [238,1558])
    chk('R16: 17-77-82 x2 absolute', [i for i in range(len(pairs)-2)
        if tuple(pairs[i:i+3])==(17,77,82)], [1040,1157])
    chk('R16: 73-34 "lui" x2', pos2(73,34), [392,1347])
    chk('R16: 70-17 @369 sole anomaly', pos2(70,17), [368])
    chk('R16: 11-84 R1 / 94-84 R2 residuals stand',
        (pos2(11,84),pos2(94,84)), ([1619],[1664]))
    chk('R16: @146 R3 new 84 residual', pairs[144:151],
        [64,77,84,29,87,64,96])

    print(f'F26-17 adjudication stream: {len(pairs)} pairs')
    allok = True
    for name, got, want, ok in checks:
        print(f'  [{"OK " if ok else "FAIL"}] {name:52s} got={got} want={want}')
        allok = allok and ok
    print(f'F26-17 EXTENSION: {sum(1 for *_, ok in checks if ok)}/{len(checks)} PASS'
          if allok else 'MISMATCH -- adjudication blocked')
    sys.exit(0 if allok else 1)

if __name__ == '__main__':
    main()
