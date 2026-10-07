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
