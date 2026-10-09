# Battery verdict: ne-census-1248

## Bar (verbatim from battery-queue.json)
"restate census iff x5 re-derived independently + downstream citations corrected"

Numbered clauses:
1. The 12-48 census of exactly 5 windows is re-derived independently on the repaired stream.
2. Downstream citations are checked and corrected where needed.

## Method
Re-derived from the repaired stream per BATTERY-PROTOCOL.md: `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py` (`[s[i:i+2] for i in range(o, len(s)-1, 2)]` per row). `canonical.py` never touched. R5005, sealed gates, and the red-team adjudication queue untouched. Lock `locks/ne-census-1248.lock` created on start.

Stream checks: 1,847 pairs, 96 distinct groups — canonical.

## Window-level evidence (0-based stream @)

All windows where group 12 is immediately followed by group 48:

| @ (0-based) | row | prev | window | successor pairs |
|---|---|---|---|---|
| 169 | a1_05 | 53 | 84 53 **12 48** 21 60 | 48 -> 21 |
| 709 | a5_01 | 53 | 35 53 **12 48** 71 12 | 48 -> 71 |
| 809 | a5_05 | 41 | 24 41 **12 48** 24 65 | 48 -> 24 |
| 1075 | a6_05 | 98 | 98 98 **12 48** 77 78 | 48 -> 77 |
| 1736 | a8_07 | 60 | 06 60 **12 48** 52 86 | 48 -> 52 |

Total: exactly 5 windows. No other 12->48 contact exists in the stream.

## Per-clause pass/fail

1. **C1 (x5 re-derived independently): PASS.** The re-derivation returns exactly 5 windows, matching the census in `report_inbox/processed/battery-stem48-exclusive-legs.md` ("12-48-21" / "12-48-71" / "12-48-24" / "12-48-77" / "12-48-52" — successors 21, 71, 24, 77, 52, all identical). Predecessors also byte-confirmed: 53, 53, 41, 98, 60.
2. **C2 (downstream citations corrected): PASS.** The downstream citations in battery-stem48-exclusive-legs.md (@170/@710/@810/@1076/@1737) use 1-based @-offsets; the 0-based stream indices are @169/@709/@809/@1075/@1736. Both conventions are now on record; the windows are the same byte positions, and no downstream report cites a 12-48 window that does not exist.

Adverses: none listed.

## Verdict: PROMOTE

The 12-48 "ne" census is restated and byte-confirmed: exactly 5 windows, successors 21/71/24/77/52, no downstream citation errors beyond the 1-based vs 0-based offset convention now documented. No standing verdict contradicted or downgraded.
