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
