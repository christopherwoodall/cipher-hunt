# Battery contre-00-three-windows — verdict: NULL (escalated to red team)

## Bar (verbatim, pre-registered)

`test 00="contre" at @47/@465/@960; promote iff all three parse with zero contradiction on banked neighbors`

## Bar restated as numbered clauses

- C1: 00="contre" parses at @47 with zero contradiction on banked neighbors.
- C2: 00="contre" parses at @465 with zero contradiction on banked neighbors.
- C3: 00="contre" parses at @960 with zero contradiction on banked neighbors.
- C4 (from brief adverse): if positive, escalate to red team — 00="pour" is A9
  class-level granted, so a battery-level promote would contradict a standing
  red-team grading (protocol §5.2).

## Method

Read BATTERY-PROTOCOL.md first. Created
`locks/contre-00-three-windows.lock` on start (agent id + UTC timestamp).
Re-derived the full repaired stream from `data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json` (1,847 pairs, 96 types verified).
`canonical.py` never used. R5005, sealed gates, red-team queue untouched.
All @-offsets 0-based.

## Window evidence

"96 00" bigram census (byte-exact): exactly 3 occurrences, @47/@465/@960.
Wide windows (10 groups each side):

- @47: `39 64 41 01 24 88 43 81 30 62 | 96 00 | 92 79 37 11 79 85 58 35`
  Banked neighbors: 79="tout" (x2), 11="la". Under 00="contre":
  "[62] par contre [92] tout [37] la tout [85]". "par contre" as adversative
  adverbial is grammatical; no banked value contradicted. C1 PASS.
- @465: `65 13 66 14 02 79 87 11 59 42 | 96 00 | 33 79 80 06 67 46 84 24`
  Banked neighbors: 79="tout", 46="que". "[42] par contre [33] tout
  [80]...[67] que". Adverbial "par contre" sits cleanly. C2 PASS.
- @960: `77 86 96 87 46 24 85 04 20 67 | 96 00 | 86 56 41 19 24 06 77 76`
  "[20] [67] par contre [86]..." — "et par contre" is textbook French. C3 PASS.

Period evidence for the claim: Littré, art. "contre" (1873): "Par contre est
une locution dont plusieurs se servent, pour dire en compensation, en
revanche" — grammatically justifiable, in use in 19th-c. French. The claim's
period premise holds.

## Distributional check (for the escalation, not the bar)

00 n=55. The other 52 non-"96 00" windows under 00="contre":

- Followers: 86 x12, 33 x8, 66 x7, 92 x6, 97 x4, 11 x4, 46 x4, 36 x3,
  plus singletons (34, 64, 98, 67, 44, 13, 20).
- SUPPORT: "contre la" x4 (11="la" banked) — "contre la [porte]" is natural.
- STRIKE: "contre que" x4 (46="que" banked) — ungrammatical. Under 00="pour"
  these are "pour que" (subjunctive), perfectly grammatical.
- STRAIN: "contre [33]" x8 — 33 is verbal-class; "contre"+infinitive is
  ungrammatical unless word-internal (33 has the penser/pens- segmentation
  duality). Neutral at battery level, red-team's call.

A global 00="contre" promote faces real resistance at "contre que" x4. The
bar's three windows are clean, but the global picture is mixed — exactly the
kind of trade-off red-team adjudication exists to weigh. A positional
alternative (00="contre" only after 96="par") would be a second polyvalence;
declaring one is red-team's act (§7: 67 et/veut is the sole true polyvalence).

## Adverse answered

00="pour" is A9 class-level granted (standing constraint §7). No battery-level
contradiction exists — the three windows parse — so per the brief's adverse
("escalate to red team if positive") and protocol §5.2, the positive finding
is escalated, not promoted. No standing verdict contradicted or downgraded.

## Verdict: NULL — headline: 00="contre" parses all three "par pour" windows
cleanly but contradicts the A9 00="pour" grant; escalated to red team.

C1/C2/C3 PASS; C4 FIRES (escalation taken). The claim survives its windows;
the decision is above battery pay-grade.

## Follow-ups proposed (for supervisor queuing)

1. `contre-00-global-census` (P2) — full 55-window census under 00="contre";
   "contre que" x4 and "contre [33]" x8 as the kill legs; promote global iff
   zero hard contradictions, else fence to the "96 00" positional reading.
2. `redteam-contre-00` (P1) — red-team adjudication of the A9 conflict: three
   clean "par contre" windows + "contre la" x4 support vs "contre que" x4
   strike vs A9 00="pour" class-level grant; rule on the positional
   (post-96) alternative as a conditioned reading.

## Bookkeeping

Report: `code/crowd17/report_inbox/battery-contre-00-three-windows.md`.
Queue: `contre-00-three-windows` → status `verdict`, result `null`, own entry
only, temp-file + rename, pre-write assert passed. Lock deleted on completion.
