# Battery report: elision-77-84

Target: `elision-77-84`
Claim: "77='le' elides to l' exclusively before vowel-initial 84 (A15-C1 support leg)"
Date: 2026-10-08
Worker: e33424b0-3c48-4e0d-b293-19e83231dc41

## Bar (verbatim)

promote-LEG iff the zero-counts re-derive on the repaired stream AND no other 77 follower is shown vowel-initial; else record as provisional-only

## Numbered clauses

1. The zero-counts re-derive on the repaired stream: 77->84 = 7, and
   77->{59,94,46,40,34,47,17} = 0 for each listed follower.
2. No other 77 follower (i.e. any follower other than 84) is shown
   vowel-initial under the standing value assignments.

## Method

Re-parsed the repaired stream exactly like
`code/side-keyhunt/repair_parse.py` (repaired_offsets.json over
`data/upstream-ct_R5005.txt`; `code/side-keyhunt/canonical.py` never used;
R5005 untouched). Stream = 1,847 pairs, 96 distinct groups. Collected every
index i where pairs[i] = "77" and tallied pairs[i+1] (sequential-pair
followers, cross-row allowed; all 44 77-instances have a following pair, so the
scan is the full 44-window census).

## Window-level evidence

77->84 windows (7), all intra-row:

- @145 a1_04: `67/a1_04 64/a1_04 77/a1_04 84/a1_04 29/a1_04 87/a1_04`
- @259 a2_02: `32/a2_02 43/a2_02 77/a2_02 84/a2_02 74/a2_02 45/a2_02`
- @1057 a6_04: `45/a6_04 23/a6_04 77/a6_04 84/a6_04 09/a6_04 98/a6_04`
- @1446 a7_09: `37/a7_09 64/a7_09 77/a7_09 84/a7_09 59/a7_09 36/a7_09`
- @1484 a7_10: `62/a7_10 46/a7_10 77/a7_10 84/a7_10 24/a7_10 87/a7_10`
- @1763 a8_08: `93/a8_08 06/a8_08 77/a8_08 84/a8_08 09/a8_08 24/a8_08`
- @1802 a8_10: `87/a8_10 64/a8_10 77/a8_10 84/a8_10 59/a8_10 35/a8_10`

Zero-counts on the repaired stream:

| follower | count |
|----------|-------|
| 59 | 0 |
| 94 | 0 |
| 46 | 0 |
| 40 | 0 |
| 34 | 0 |
| 47 | 0 |
| 17 | 0 |

Full follower distribution (44 windows, 20 distinct followers):
03x1, 06x1, 11x1, 44x2, 45x1, 60x1, 62x1, 64x1, 66x1, 74x1, 76x3,
78x7, 80x1, 81x4, 82x2, 83x1, 84x7, 86x5, 87x1, 89x2.

Notable: vowel-initial banked/provisional values 59='est' (provisional),
40='e' (banked), 34='i' (banked) never follow 77 — consistent with the elision
reading, and consistent with clause 1.

## Per-clause pass/fail

1. PASS. The repaired stream re-derives the counts exactly: 77->84 = 7 at the
   @-offsets above; 77->{59,94,46,40,34,47,17} = 0 each. No phantom pairs.
2. PASS. Other 77 followers with established values are all
   consonant-initial: 11='la', 45='ce' (A11 hold), 64='qui' (promoted),
   82='m' (banked), 87='ce' (promoted). Followers 86/81/76/44/89, and also 78,
   03, 06, 60, 62, 66, 74, 80, 83, have no established value under the standing
   rules: 81's "prin" claim is a standing kill (value open); 80/89 are
   granted verb-frames with value open. None is *shown* vowel-initial. The
   clause's wording ("shown") is satisfied.

## Adverses answered

- Unknown followers 86/81/76/44/89 could be vowel-initial (open): answered as
  fenced, not resolved — all five, plus 78 (7 occurrences) and the smaller
  unknowns, carry no established value, so none is shown vowel-initial; 81
  specifically sits under the standing 81="prin" kill. Kept open as follow-up
  surface, not ignored.
- 77='le' provisional (le-77 null): acknowledged — this battery promotes only
  the A15-C1 support LEG; the 77='le' value itself is NOT promoted by this
  verdict.

## Verdict

**promote** — the A15-C1 support leg (77='le' elides to l' exclusively before
vowel-initial 84) is ratified by the red team pending their own review. The
77='le' value remains provisional; nothing in this report touches R5005,
sealed gates, or the red-team adjudication queue.
