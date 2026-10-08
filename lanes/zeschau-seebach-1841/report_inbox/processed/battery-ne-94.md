# Battery report — ne-94 (94="ne")

Worker: d6cab360-c0d0-4532-aecd-b6679585910e. Date: 2026-10-07.
Lock: predecessor `locks/ne-94.lock` (battery-worker-ne94, 2026-10-08T04:22:04Z)
was stale — the worker died in the agent-daemon restart at ~2026-10-08 04:26 UTC
with no partial report on disk. Lock refreshed per protocol §6 and proceeded
with a clean restart; nothing is inherited from the dead run.

## Bar (verbatim, from battery-queue.json)

`promote iff >=2 independent 'ne'-frames parse cleanly + zero board contradictions + 'n\'' elision frames hold`

Numbered clauses (pre-registered BEFORE testing):

1. C1 — >=2 INDEPENDENT 'ne'-frames parse cleanly.
2. C2 — ZERO board contradictions for 94="ne".
3. C3 — the 'n'' elision frames hold (94 before vowel-initial cell reads "n'").

## Method

Parsed only the repaired 1,847-pair stream:
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`,
tokenized like `code/side-keyhunt/repair_parse.py`
(`[s[i:i+2] for i in range(o, len(s)-1, 2)]` per row offset). 1,847 pairs,
96 distinct cells, 37 occurrences of 94. Every @-offset below is a 0-based
index into that stream. `code/side-keyhunt/canonical.py` not used. R5005 not
touched. Standing constraints per BATTERY-PROTOCOL.md §7 apply (GT:
11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que; promoted: 87=ce, 64=qui,
96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce; kills hold).

## Window-level evidence

All 94 frame counts re-derived from the stream (independent of the pre-finder):

- F-A 'n'est' x3: 94-59 @558 ("...86 94 59 30..." = "[86] n'est pas"),
  @762 ("62 94 59 39" = "[62] n'est [39]"), @1795 ("42 94 59 37" =
  "[42] n'est [37-predicative]"). 59=est provisional; round-15 review
  already classified these three as "n'est [30/39/37]". All three parse
  cleanly. INDEPENDENT of F-B/F-C/F-D (different neighbour cells).
- F-B 'ne me/m'' x4: 94-82 @578 ("61 94 82 06 06"), @1182 ("78 94 82 06"),
  @1353 ("78 94 82 06", byte-repeat of @1182), @1742 ("34 94 82 46" =
  "i ne me que", 34=i, 46=que GT). 82=m GT. All four parse cleanly.
- F-C 62-94 x9: 94@101, @509, @762, @841, @1330, @1363, @1687, @1705, @1773
  with 62 immediately before. Under either live 62 reading (62="il" rival
  or 62="on" strong lead per A15-C2) the frame is "[il/on] ne ..." — clean
  French either way; 94="ne" is not the forked cell.
- F-D 'prenne' x2: 70-12-94 @347-349 ("70 12 94" = pre+n+ne, 70=pre GT)
  and @1547-1549 ("46 70 12 94 ..." = "que pre-n-ne ..."). The
  analytic/syllabic duality with the letter battery (12="n", 48="e"):
  "prenne" spelled 70-12-94 analytically, while 94 carries "ne" as a
  syllable. Both parse cleanly.
- Bonus (not needed for the bar): 94-52 x3 = "ne pas" @570-571, @1293-1294,
  @1806-1807 (52="pas" iff negation-frame); 35-94-52-80-04 byte-identical
  @1292/@1805 = "ne pas [inf]"; 82-94-76 x2 @651, @1576 ("m(e)-ne" shape).

Full 94 window scan (37 windows, ±3 context each) for contradictions:
predecessors {62x9, 12x3, 42x3, 82x3, 35x2, 65x2, 78x2, 61x2, 22x2, 52x1,
06x1, 28x1, 32x1, 33x1, 34x1, 44x1, 45x1, 86x1}; followers {82x4, 74x3,
59x3, 52x3, 24x2, 76x2, 79x2, 92x2, 02x1, 06x1, 07x1, 15x1, 26x1, 29x1,
30x1, 44x1, 60x1, 64x1, 65x1, 70x1, 84x1, 87x1, 88x1, 93x1}.
Notable reads: @509 "62 94 64" = "[62] ne qui" (64=qui); @1169 "61 94 87"
= "61 ne ce"; @1701 "33 94 30" = "[33] ne [30]" (ne...pas shape);
@688 "65 94 29" = "65 ne er" (29=er; "n-er" morphology); @65 "40 12 94 92"
= "e n ne 92" ("enne"-shaped, analytic duality). No window forces 94 != "ne".

## Per-clause pass/fail

- C1 — PASS: four independent 'ne'-frame types parse cleanly (94-59 x3,
  94-82 x4, 62-94 x9, 70-12-94 x2), each re-derived from the stream.
- C2 — PASS: 37-window scan, zero hard contradictions. The one tension
  (@1664 "22 94 84" = "...ne on") is fenced with stated cause per A15-C3
  (see adverses), not a contradiction.
- C3 — PASS: all three 94-59 windows REQUIRE the "ne"→"n'" elision before
  vowel-initial 59="est" and read cleanly as "n'est". The registry forbids
  only the "non"=94+84 rescue (94 cannot be letter-"n", A15-C3) — an
  elision constraint, not a failure; no frame where "n'" elision is
  required fails to hold.

## Adverses disposition

- A1 "pre-beat kills were of OTHER 48 hypotheses, not 94='ne'" — ANSWERED.
  The crowd8 homophone battery (`code/crowd8/report_inbox/homophonist-48-ne.md`)
  KILLed only 48's membership in a {94,48}="ne" homophone set, explicitly
  taking "94='ne' provisional-strong" as its ANCHOR. The 48="est"/"de"
  kills are of 48-value hypotheses; the live 48="e" letter battery is
  compatible (analytic/syllabic duality with 94="ne", not a rival).
- A2 "R1/R2 'ne on' windows fenced per A15-C3" — ANSWERED. R2 = @1664
  ("22 94 84 64") is the lane's single 94-84 window, fenced per A15-C3
  with stated cause ("ne on" = genuine 1/25 residual; "non"=94+84 rescue
  forbidden). R1 (@1619 "11-84") does not involve 94. Fenced, not ignored.
- No standing red-team verdict contradicts 94="ne": REPORT.md round-4
  re-battery on the repaired parse says 94="ne" HOLDS (provisional-strong,
  F21); this verdict upgrades provisional → promoted, which is the
  battery's purpose. §7 kill list ("{48,94} homophone-set") is not this
  claim and is unaffected.

## Verdict

**promote**
