#!/usr/bin/env python3
"""Red-team verification apparatus for Seebach round 5.

Builds the canonical repaired 1,847-pair stream (repair_parse.load_rows +
parse with repaired_offsets.json) and re-derives every load-bearing number
round-5 promotion claims will be judged against. Run with no args; prints a
baseline table and exits nonzero on any mismatch.
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

    checks = []
    def chk(name, got, want):
        checks.append((name, got, want, got == want))

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
    chk('06->00', big[(6, 0)], 4)
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

    print(f'canonical stream: {len(pairs)} pairs, {len(groups)} distinct groups')
    print(f'"la premiere" @ {lp}')
    allok = True
    for name, got, want, ok in checks:
        mark = 'OK ' if ok else 'FAIL'
        print(f'  [{mark}] {name:32s} got={got} want={want}')
        allok = allok and ok
    print('BASELINE PASS' if allok else 'BASELINE MISMATCH')
    sys.exit(0 if allok else 1)

if __name__ == '__main__':
    main()
