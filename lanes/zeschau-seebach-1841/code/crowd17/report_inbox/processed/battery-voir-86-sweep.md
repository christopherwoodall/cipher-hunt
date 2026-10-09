# Battery verdict: voir-86-sweep — global test of 86 = "voi" (stem of "voir")

Date: 2026-10-09. Worker: 4a790e73-d7d1-4a5c-b3a7-ccddbe8fa3f4 (battery worker).
Lock: code/crowd17/next-token/locks/voir-86-sweep.lock (created 2026-10-09T02:49:00Z; no prior lock; deleted on completion).
Target id: voir-86-sweep. Queue status at take: queued, priority 2.
Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt, parsed like code/side-keyhunt/repair_parse.py).
canonical.py never used. R5005, sealed gate instances, red-team adjudication
queue untouched. No data invented; every number re-derived below. @-offsets
are 0-based stream indices.

## Bar (pre-registered verbatim from battery-queue.json, BEFORE testing)

"promote 86='voi' iff all 32 windows parse with 'voi'/'voir'/'pourvoir'-family compositions and zero hard contradictions; kill iff any window forces otherwise. Predicts: 'pour voir' x2 (@1375, @1825), 'veut voir' (@1391), 'le voir' (@431), 'la voir' (@671), 'pourvoient' (@889)"

### Numbered clauses (operative, pre-registered)

1. PROMOTE iff all 32 windows of 86 parse with "voi"/"voir"/"pourvoir"-family
   compositions AND zero hard contradictions.
2. KILL iff any window forces otherwise (86 cannot be "voi" there at kill grade).
3. Otherwise NULL.

## Method

1. Re-parsed the repaired stream per repair_parse.py; extracted all 32
   windows of group 86 with ±3 context, row ids, and byte-exact neighbors.
2. Follower census re-derived: 29:4, 56:4, 01:2, 24:2, 52:2, 66:2, and
   singletons {06,12,16,20,21,44,48,50,59,67,70,71,78,91,94,96} — matches
   battery-split-86-amended-rule exactly (32/32). Predecessor census:
   00:12, 77:5, 67:3, 83:2, rest singletons.
3. Adopted the sibling battery's partition as the test frame (coordinate,
   not duplicate): V-life = followers {29,59,06} (n=6: @431, @553, @889,
   @1375, @1391, @1825); D-life = all other followers (n=26).
4. For each window, attempted a "voi"-family composition (voir, pourvoir,
   pourvoient, voie/voix/voisin/revoir/prévoir/entrevoir-family) requiring:
   (a) real 1841 French word, (b) every group in the word assigned, no
   residue, (c) grammatical clause. Banked values used per protocol §7
   (pencil + granted; battery-promoted values cited as caveated where used).
5. Tested the bar's five predictions individually on bytes.

## Window-level evidence

### V-life windows (n=6) — the "voi" compositions

- @431 (a2_09): "77 [86] 29 82" = "le voi er" → **"le voir"** (substantivized
  infinitive). Parses cleanly. Prediction "le voir" CONFIRMED.
- @1375 (a7_06): "00 [86] 29 89" = "pour voi er" → **"pourvoir"** (one word,
  "to provide") or "pour voir" (two words, "in order to see") — both
  grammatical, both "voi"-family. Prediction "pour voir" CONFIRMED (tighter
  parse: "pourvoir").
- @1391 (a7_07): "67 [86] 29 89" = "veut voi er" → **"veut voir"** ("wants to
  see"; 67="veut" by the positional rule, follower infinitive-shaped).
  Prediction CONFIRMED.
- @1825 (a8_11): "00 [86] 29 82" — same as @1375 → "pourvoir"/"pour voir".
  Prediction CONFIRMED.
- @889 (a5_08): "00 [86] 06 77" = "pour voi ent" → **"pourvoient"** (3pl
  present of pourvoir), demonstrated byte-exact by battery-reseg-86-553-889
  (00="pour" + 86="voi" + 06="ent", no residue, grammatical clause).
  Prediction CONFIRMED at battery level — **BUT this parse contradicts the
  standing red-team clause-boundary fence** ("00 86 | 06 77", rulings.md /
  morph47_06.md), flagged per protocol §5.2 and already escalated via
  queued P1 `redteam-889-pourvoient`. Adopting it here inherits the
  contradiction; it cannot serve as a promote leg until adjudicated.
- @553 (a3_01): "00 [86] 59 34 17" = "pour voi est-i fois" — **genuine
  residual**. 86 is followed by 59 ("est", provisional), not 29, so no
  "voir"/"pourvoir" composition exists; "pourvoi" (noun, "appeal") + "est-i"
  dies on "59 34" ("est-i" admits no grammatical continuation, per reseg
  battery's five failed re-segmentation families). The defect localizes to
  "59 34", orthogonal to 86's value — but the window does NOT parse as a
  "voi"-family composition. Soft residual, not kill-grade.

V-life score: 5/6 compose (4 clean + 1 contradicted-by-red-team-fence);
1 residual (@553).

### D-life windows (n=26) — no demonstrable "voi" composition

For each D-window, the "voi"-family parse was attempted and fails or is
undemonstrable on current bytes. Strongest cases:

- @728 (a5_02): "00 [86] 48 88" = "pour voi [48]". 48="e" is battery-level
  only (pending ratification); even granting it, "pourvoie" (subjunctive of
  pourvoir) requires a "que"-clause — left context is "64 11" ("qui la"),
  no "que". "pour voie" (two words) is ungrammatical. No composition
  demonstrable.
- @175 (a1_05): "87 [86] 21 69" = "ce voi [21]…" — dead under "voi"; also
  dead under a determiner reading ("ce" + determiner ungrammatical). Open,
  not forcing.
- @671 (a5_00): "11 [86] 24 80" = "la voi [24]" — **the bar's predicted
  "la voir" FAILS on bytes**: the follower is 24 (verb-class, value open),
  not 29. "la voir" is not what this window shows. Not kill-grade (24's
  value unknown), but the prediction is falsified as stated.
- @557 (a3_01): "17 [86] 94 59" = "fois voi ne est" — no composition.
- @878 (a5_08): "77 [86] 78 17" = "le voi ver…" (78="ver" battery lead) —
  no "voi"-family word ("voiver" is not French).
- @899 (a5_08): "83 [86] 16 92" — neighbors unvalued; open.
- @948 (a6_00): "96 [86] 01 77" = "par voi [01]…" — "par voix" is not
  idiomatic French; open.
- @951 (a6_00): "77 [86] 96 87" = "le voi par ce" — no composition.
- @962/@1002/@1506/@1792: "00 [86] 56" ×4 = "pour voi [56]" — "pourvoir"
  needs 29; 56's value is open. "pourvoi" (noun) + unknown 56 is
  speculative, not demonstrable. Neutral ×4.
- @661 (a4_02): "00 [86] 50 80" = "pour voi [50]" — same, neutral.
- @867 (a5_07): "00 [86] 70 87" = "pour voi pre ce" — "pourvoi" + "pre…"
  continues nowhere demonstrable. Neutral.
- @1128 (a6_07): "00 [86] 52 37" = "pour voi [52]" — neutral.
- @1131 (a6_07): "37 [86] 24 77" — neutral/open.
- @1134 (a6_08): "77 [86] 20 62" = "le voi [20]" — no composition.
- @1099 (a6_06): "67 [86] 52 82" = "et/veut voi [52]" — "veut voir" needs
  29; absent. Neutral.
- @1458 (a7_09): "67 [86] 66 79" — neutral.
- @1147 (a6_08): "98 [86] 67 33" = "vient voi et/veut" — no composition.
- @1335 (a7_05): "83 [86] 71 64" — open.
- @1345 (a7_05): "47 [86] 66 73" = "ce voi [66]" — no composition.
- @1739 (a8_07): "52 [86] 12 34" — "voi n…" ("voin" not French); open.
- @1792 counted above; @716 (a5_01): "66 [86] 01 02" — open.
- @300 (a2_04): "97 [86] 91 18" — open.
- @799 (a5_04): "77 [86] 44 74" = "le voi [44]" — no composition.

D-life score: 0/26 demonstrably parse as "voi"-family compositions; none
forces 86≠"voi" at kill grade (unknown neighbors keep most windows open
rather than contradictory).

## Per-clause pass/fail

1. **PROMOTE: FAIL.** At most 5/32 windows parse as "voi"-family
   compositions (4 clean + @889 which is red-team-contradicted); @553 is a
   genuine residual; 0/26 D-windows compose on current bytes; the bar's
   "la voir" prediction at @671 is falsified as stated (follower is 24,
   not 29).
2. **KILL: FAIL.** No window forces 86≠"voi" at kill grade. The D-windows
   are open/neutral (unvalued neighbors), not contradictory; the promoted
   amended rule assigns D-life positionally but names no rival value.
3. **NULL** (both bars fail; §4).

## §5.2 headline contradiction (blocks any future promote on this line)

Adopting the @889 "pourvoient" parse (required for the "voi" value's
strongest leg) contradicts the standing red-team clause-boundary fence
("00 86 | 06 77"). Flagged, not overwritten. Already escalated via queued
P1 `redteam-889-pourvoient` — no duplicate created. Per §7, a global "voi"
value coexisting with 26 determiner-life windows would imply a second
polyvalence (67 et/veut is the sole true polyvalence); declaring any split
remains the red team's act.

## Adverses

- "coordinates with split-86-amended-rule; does not duplicate it":
  ANSWERED. split-86-amended-rule returned battery-level promote; this sweep
  used its 26/6 partition as the test frame and tested the VALUE "voi"
  across it. Result: "voi" composes only inside the V-partition (5/6, one
  contradicted); it does not explain the D-partition (0/26). The rule and
  the value are complementary findings, not duplicates; split declaration
  stays with the red team.

## Verdict: NULL

86="voi" is strongly supported inside the verb-adjacent partition
("voir" ×4, "pourvoir" ×2, "pourvoient" ×1) but the global claim fails:
@553 is a genuine residual, no D-life window composes a "voi"-family word
on current bytes, and @889's strongest leg contradicts a standing red-team
fence. Not kill-grade: no window forces a non-"voi" value.

## Follow-up targets (null regenerates work)

1. `voi-86-dwindow-composition` (P2): for each of the 26 D-life windows,
   test word-internal "voi"-family compositions (voix/voie/voisin/revoir/
   prévoir/entrevoir/apercevoir-family) using only ratified neighbor
   values. Bar: kill the global-"voi" hypothesis iff any D-window forces a
   determiner-exclusive parse; else promote window-local "voi" readings.
   Notes the dependency on red-team adjudication of the 86 split.
2. `det-86-dlife-value` (P3): name 86's determiner-life value over the 26
   D-windows (le/la/les/un/une/son/sa/ce candidates) with stated byte
   evidence per window. Bar: promote iff one value parses all 26 with zero
   hard contradictions. Complement to this sweep; does not declare the
   split (red-team act).
3. Already queued — referenced, not duplicated: `redteam-889-pourvoient`
   (P1, must adjudicate before any "voi"-family promotion); `reseg-553-retry`
   (P3, owns the @553 "59 34" residual).

## Constraints compliance

- Tested only on the repaired 1,847-pair stream; canonical.py never
  touched; R5005, sealed gates, red-team queue untouched.
- No standing verdict downgraded or overwritten; the @889 contradiction is
  flagged per §5.2 (this null, not an overwrite).
- 86 polyvalence NOT declared; no new polyvalence implied at battery level.
- Sibling split-86-amended-rule's promote stands uncontradicted (rule ≠ value).
