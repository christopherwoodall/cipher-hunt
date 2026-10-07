#!/usr/bin/env python3
"""Red-team verification apparatus for Seebach round 6.

EXTENDS the round-5 instrument (code/crowd5/redteam/verify_baseline.py, 30/30
PASS, left untouched) with the round-6 work-order load-bearing numbers.

Every check is re-derived from the canonical repaired 1,847-pair stream
(repair_parse.load_rows + repaired_offsets.json). Run with no args; prints a
baseline table and exits nonzero on any mismatch.

Corrections armed (memo 2026-10-07, re-verified on the 1,847-pair stream):
  n62=35 (sidepath's 34 superseded; N28 carries 9/35), n24=52 (unmoved),
  n52=27 (unmoved), n06=44 (repaired; old-parse 46), n78=31, 47->64=0.
"""
import json, sys
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
    groups = Counter(pairs)
    assert len(pairs) == 1847, f'pairs={len(pairs)}, want 1847'
    assert len(groups) == 96, f'distinct={len(groups)}, want 96'
    crib = [11, 70, 82, 34, 29, 40]
    assert all(g in groups for g in crib + [46])
    lp = [i for i in range(len(pairs) - 5) if pairs[i:i + 6] == crib]
    assert lp == [754, 1034], f'la premiere positions={lp}, want [754,1034]'
    big = Counter(zip(pairs[:-1], pairs[1:]))
    tri = Counter(zip(pairs[:-2], pairs[1:-1], pairs[2:]))
    quad = Counter(zip(pairs[:-3], pairs[1:-2], pairs[2:-1], pairs[3:]))

    checks = []
    def chk(name, got, want):
        checks.append((name, got, want, got == want))

    # ================= ROUND-5 BASELINE (inherited, unmodified) =================
    # --- sidepath recounts re-verified on repaired parse (memo 2026-10-07) ---
    chk('n24 (sidepath: 52, unmoved)', groups[24], 52)
    chk('n52 (sidepath: 27, unmoved)', groups[52], 27)
    # --- 62="on" (frenchman; round-5 wants an instrument-independent 3rd leg) ---
    chk('n62', groups[62], 35)
    chk('62->94 "on ne"', big[(62, 94)], 9)
    # --- 47="ce" (morphologist battery) ---
    chk('n47', groups[47], 28)
    chk('47->46 "ce que"', big[(47, 46)], 3)          # 3/28=0.1071 vs era 0.1076
    chk('47->11 "cela"', big[(47, 11)], 3)
    chk('47->64 (absent)', big[(47, 64)], 0)           # "ce qui" goes via 87, never 47
    # --- 06 stem (morphologist/stem-hunter) ---
    chk('n06', groups[6], 44)                        # repaired (old-parse 46)
    chk('06->77', big[(6, 77)], 6)
    chk('06->29 infinitive frames', big[(6, 29)], 4)  # repaired: 4 (old 5th off-phase)
    chk('06->11', big[(6, 11)], 4)
    chk('06->00', big[(6, 00)], 4)
    chk('00->86', big[(0, 86)], 12)                   # 06/86 complementary dist.
    chk('00->06', big[(0, 6)], 0)
    # --- 77="le" (bigram closer) ---
    chk('77->86', big[(77, 86)], 5)
    p7786 = [i for i in range(len(pairs) - 1) if (pairs[i], pairs[i + 1]) == (77, 86)]
    chk('77->86 positions', p7786, [430, 798, 877, 950, 1133])
    # --- 78="me"/"ver" (bigram closer) ---
    chk('77->78 adverse frames', big[(77, 78)], 7)    # "pas me" era-0 under 78=me
    chk('n78', groups[78], 31)
    # --- 87=ce (closer) ---
    chk('n87', groups[87], 32)
    chk('24->87->64', tri[(24, 87, 64)], 3)
    chk('96->87->46', tri[(96, 87, 46)], 3)
    chk('87->64', big[(87, 64)], 5)
    p8778 = [i for i in range(len(pairs) - 3) if pairs[i:i + 4] == [87, 64, 77, 84]]
    chk('87-64-77-84 @', p8778, [1800])               # <<ce qui [verbe] 84>>
    chk('24->87->46 (absent)', tri[(24, 87, 46)], 0)  # que licensed by 96, never 24
    # --- 64="qui" / 96="par" anchors ---
    chk('64->77', big[(64, 77)], 3)                   # one byte-identical trigram
    chk('n24', groups[24], 52)
    chk('24->87', big[(24, 87)], 10)
    # --- 94="ne" (morphologist) ---
    chk('94->82', big[(94, 82)], 4)
    p9482 = [i for i in range(len(pairs) - 1) if (pairs[i], pairs[i + 1]) == (94, 82)]
    chk('94->82 positions', p9482, [578, 1182, 1353, 1742])  # REINDEX rule: old 1181/1352/1741 -> +1

    # ================= ROUND-6 EXTENSION =================
    # WO1: 62="on" non-ear discrimination — follow-59 lead (F42), double-duty
    # datum armed (46->62=0, N35: one datum, cannot serve as the independent leg),
    # full follower/predecessor profiles for the on-vs-il fence (n>>2 cells).
    chk('n59', groups[59], 27)
    p5946 = [i for i in range(len(pairs) - 1) if (pairs[i], pairs[i + 1]) == (59, 46)]
    chk('59->46 positions', p5946, [216, 1190])       # "que" x2 after verb-candidate
    chk('46->62 (absent)', big[(46, 62)], 0)         # double-duty datum, N35
    fol62 = {b: c for (a, b), c in sorted(big.items()) if a == 62}
    pre62 = {a: c for (a, b), c in sorted(big.items()) if b == 62}
    chk('62 followers profile', fol62,
        {6: 2, 16: 4, 18: 1, 21: 1, 38: 1, 46: 1, 48: 6, 61: 2, 91: 1, 93: 1,
         94: 9, 96: 1, 98: 5})
    chk('62 predecessors profile', pre62,
        {2: 1, 3: 2, 4: 1, 6: 1, 8: 2, 10: 1, 14: 1, 20: 4, 21: 5, 30: 1,
         34: 1, 36: 1, 40: 1, 41: 1, 51: 1, 74: 3, 77: 1, 78: 2, 92: 2, 93: 2,
         98: 1})
    # WO2: 96 conditioned-verb battery in "ce qui __ ce que" — F42 A-legs
    p6443 = [i for i in range(len(pairs) - 2) if pairs[i:i + 3] == [64, 77, 84]]
    chk('64-77-84 trigram', p6443, [144, 1445, 1801])  # n_eff=1 byte-identical (N27)
    p4784 = [i for i in range(len(pairs) - 3) if pairs[i:i + 4] == [64, 77, 84, 59]]
    chk('64-77-84-59 quad', p4784, [1445, 1801])      # F42 refinement
    p8701 = [i for i in range(len(pairs) - 1) if (pairs[i], pairs[i + 1]) == (87, 1)]
    chk('87->01 positions', p8701, [344, 1028])       # "c'est" x2 (F42 A1)
    p4701 = [i for i in range(len(pairs) - 1) if (pairs[i], pairs[i + 1]) == (47, 1)]
    chk('47->01 positions', p4701, [194])             # "c'est" joint (F42 A1)
    chk('87->11 "cela"', big[(87, 11)], 7)           # A5 structural (no cela-rate)
    # WO3: 77="le" exploit — 45="me" drag target; WO6: 00="pour" battery
    p7845 = [i for i in range(len(pairs) - 1) if (pairs[i], pairs[i + 1]) == (78, 45)]
    chk('78->45 positions', p7845, [313, 573, 982, 1164])  # 45="me" test x4
    chk('n45', groups[45], 22)
    p0046 = [i for i in range(len(pairs) - 1) if (pairs[i], pairs[i + 1]) == (0, 46)]
    chk('00->46 positions', p0046, [106, 545, 1545, 1680])  # "pour que" (F40)
    # WO7: 67 classification — chiasmus (F42); 43="me" pressure («par 43» x2)
    p6711 = [i for i in range(len(pairs) - 1) if (pairs[i], pairs[i + 1]) == (67, 11)]
    chk('67->11 positions', p6711, [561, 669, 753, 996])
    p1167 = [i for i in range(len(pairs) - 1) if (pairs[i], pairs[i + 1]) == (11, 67)]
    chk('11->67 positions', p1167, [1044])           # "la veut" @1044-1045
    chk('n67', groups[67], 38)
    chk('n84', groups[84], 25)
    chk('n43', groups[43], 16)
    p9643 = [i for i in range(len(pairs) - 1) if (pairs[i], pairs[i + 1]) == (96, 43)]
    chk('96->43 positions', p9643, [342, 1026])      # «par 43» x2 vs era "par me"=0

    print(f'canonical stream: {len(pairs)} pairs, {len(groups)} distinct groups')
    print(f'"la premiere" @ {lp}')
    allok = True
    for name, got, want, ok in checks:
        mark = 'OK ' if ok else 'FAIL'
        print(f'  [{mark}] {name:32s} got={got} want={want}')
        allok = allok and ok
    print(f'ROUND-6 BASELINE: {sum(1 for *_, ok in checks if ok)}/{len(checks)} PASS'
          if allok else 'BASELINE MISMATCH')
    sys.exit(0 if allok else 1)

if __name__ == '__main__':
    main()
