# Battery report: x-er-89-frame

- Target id: `x-er-89-frame` (battery-queue.json, priority 3, status queued)
- Claim: "census the five 'X-er 89' windows (@113, @275, @781, @1377, @1393)"
- Date: 2026-10-09
- Worker: battery worker (subagent 84cf9577-a939-45d2-9b7d-014682049220)
- Stream: repaired 1,847-pair / 96-type parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed like code/side-keyhunt/repair_parse.py;
  n=1847 asserted, 96 types asserted). All @-offsets below are 0-based repaired-stream
  indices; the claim's @113/@275/@781/@1377/@1393 are the 89 positions (= 0-based 29-position + 1).
  `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.
- Evidence cited: val-86-1391 NULL (finding 2).

## Bar (verbatim, pre-registered from battery-queue.json BEFORE testing)

"one licensor frame for 89 parses all five at battery grade, else fence the 89-slot question"

Numbered pass/fail clauses (restated before testing, not modified after):

1. (C1) One licensor frame for 89 parses all five windows (@113, @275, @781, @1377, @1393)
   at battery grade (standing values only, zero ungranted assumptions).
2. (C2) Else: fence the 89-slot question with stated cause (verdict NULL, fence executed).

## Method

1. Read BATTERY-PROTOCOL.md first. Created `locks/x-er-89-frame.lock` on start
   (agent 84cf9577-a939-45d2-9b7d-014682049220, 2026-10-09T20:33:38Z); deleted on completion.
2. Re-derived the repaired stream in-session; asserted 1,847 pairs / 96 types. Never used canonical.py.
3. Confirmed "29 89" occurs exactly 5x stream-wide at 0-based 29-positions [112, 274, 780, 1376, 1392]
   (89 at @113/@275/@781/@1377/@1393) — matches er89-wordinternal-govern's census. No other er-89 windows exist.
4. Adopted as premises (not re-litigated):
   - er89-wordinternal-govern KILL (2026-10-09): "29 89" is a word boundary at all five windows;
     89 is standalone; the word-internal "[G]er89" fork is dead.
   - 89 = noun LEAD, ratified R19-161 (round19 meta: "89 infinitive rival killed, noun lead ratified").
     The infinitive-89 reading is dead at red-team level — this battery uses only noun/adverb frames.
   - noun-89-1377-adjudicate (2026-10-08): at @1377, "pour [86]er [89-noun]" (direct object of the
     infinitive) and "pour [86]er [89-adv]" (manner adverb) are both grammatical under standing
     values; neither could be killed.
   - val-86-1391 NULL finding 2 (2026-10-09): "[86]er" is a spelled -er infinitive (stem 86 + 'er'),
     battery grade.
   - A10: 33+29 composition (33 = stem); A8: 86 INF-class; A9: 00='pour'; 98='vient' LEAD;
     67 et/veut positional rule (sole polyvalence): 67="veut" iff follower infinitive-shaped.
   - de-frame-21-class (processed): "fol 93 (@110): 93-29 mirrors the X-er shape but 93-29 is not
     an attested infinitive. Fenced as ambiguous."
   - class-89-adjudicate (processed): at @275, "= "…[06] veut [33]-er [89], on [91]…".
     Governor 67="veut" by the positional rule" — i.e. "[33]er" treated as infinitive-shaped,
     67=veut applied at exactly this window.
   - 08 = 't' letter-tier (battery-promoted, unratified); "08 29" = "ter" syllable leg.

## Window-level evidence

Candidate single frame F: **89 = noun/adverb complement of the preceding -er infinitive**
("[X]er [89-N/adv]") — the only frame consistent with the 89=noun LEAD adverse.

### @275 (W2): PARSES ✓

Context (0-based 268–280): `73 47 11 06 67 33 29 89 84 91 37 61`
= "[73] ce(47) la(11) ent(06) [67] [33]er(29) [89] on(84) [91] [37] [61]".
- "[33]er": 33 = stem (A10), + 29='er' = -er infinitive, battery grade.
- 67's follower word "[33]er" is infinitive-shaped → 67="veut" (positional rule; applied at
  exactly this window by class-89-adjudicate).
- "veut [33]er [89-N]" = "veut [INF] [noun-object]" — grammatical ("veut prendre [N]").
  "veut [33]er [89-adv]" (manner adverb) likewise grammatical. Zero new assumptions.

### @1377 (W4): PARSES ✓

Context (0-based 1370–1382): `91 67 98 00 86 29 89 84 92 69 13`
= "[91] [67] vient(98) pour(00) [86]er(29) [89] on(84) [92] [69] [13]".
- "[86]er" = spelled -er infinitive (val-86-1391, battery grade).
- "vient pour [86]er [89-N]" = direct object of the infinitive ("pour faire le pain"-shaped);
  "pour [86]er [89-adv]" = manner adverb. Both grammatical and unkilled per
  noun-89-1377-adjudicate. Zero new assumptions.

### @1393 (W5): PARSES ✓

Context (0-based 1386–1398): `16 06 29 67 86 29 89 16 76 47 78`
= "[16] ent(06) er(29) [67] [86]er(29) [89] [16] [76] ce(47) [78]".
- "[86]er" = spelled -er infinitive (val-86-1391, battery grade).
- 67's follower word "[86]er" is infinitive-shaped → 67="veut" (positional rule).
- "veut [86]er [89-N/adv]" — grammatical, same shape as W2. Zero new assumptions.

### @113 (W1): FAILS at battery grade ✗

Context (0-based 106–118): `62 94 93 59 45 28 00 46 11 21 67 93 29 89 68 21 67 14`
= "[62] ne(94) [93] est(59) ce(45) [28] pour(00) que(46) la(11) [21] [67] [93]er(29) [89] [68] …".
- "[93]er" as an infinitive needs 93 = verb stem. 93's standing class is verb (R19-166),
  not stem; 93's value is open. "93 29" is a stream hapax (exactly 1x) — no distributional
  support for a 93+29 composition (contrast A10 for 33+29, val-86-1391 for 86+29).
- Precedent (de-frame-21-class, at this exact window): "93-29 mirrors the X-er shape but
  93-29 is not an attested infinitive. Fenced as ambiguous."
- 67's follower is 93 (verb-class, not infinitive-shaped) → 67="et"; "et [93]er [89]"
  is ungrammatical ("et" + bare infinitive). The 67="veut" rescue is circular (needs
  "[93]er" infinitive-shaped first).
- No other licensor in the window: no finite verb adjacent to 89 on either side
  (left: "pour que la [21] [67]"; right: "[68] [21] [67] [14]", all open cells).
- Frame F fails here at battery grade: licensing "[93]er" as an infinitive is an
  ungranted assumption.

### @781 (W3): FAILS at battery grade ✗

Context (0-based 774–786): `80 10 22 94 07 06 94 15 33 73 37 08 29 89 11 24 42 94`
= "[80] [10] [22] ne(94) [07] ent(06) ne(94) [15] [33] [73] [37] [08]er(29) [89] la(11) [24] [42] ne(94)".
- "[08]er": 08 = 't' letter-tier (battery-promoted, unratified). A letter is not a verb stem;
  "08 29" = "ter" is a syllable leg, not stem+'er'. "08 29" is a stream hapax (exactly 1x).
  "[08]er" cannot be an -er infinitive under standing values — this is stronger than W1's
  fence: the stem reading is not merely unattested, it is tier-incompatible.
- Alternative licensor "[89-N] la(11) [24-fin]" (= "[N] la [V]", subject + object pronoun +
  finite modal) would need an ungranted clause boundary before 89 ("[37] [08]er" is itself
  unparsed) — not battery grade.
- Frame F fails here at battery grade.

## Per-clause pass/fail

1. **C1 FAIL** — Frame F ("89 = noun/adverb complement of the preceding -er infinitive")
   parses 3/5 windows at battery grade (@275, @1377, @1393) but fails at @113
   ("[93]er" not an attested infinitive; fenced as ambiguous by standing precedent) and
   at @781 ("[08]er" tier-incompatible with a stem reading; 08 is letter-tier 't').
   No other single frame parses all five: the infinitive-89 frame is killed at red-team
   level (R19-161) and barred by this target's adverse; finite-clause frames do not
   unify across the windows.
2. **C2 FIRES** — the 89-slot question is FENCED: 89's licensing in the "X-er 89" windows
   cannot be unified under one battery-grade frame. The 3/5 parse (W2/W4/W5) stands as
   established; W1 and W3 are fenced with stated cause (unattested-"[93]er"-infinitive;
   letter-tier-"[08]er").

## Verdict: NULL (fence executed)

No single licensor frame for 89 parses all five "X-er 89" windows at battery grade.
The 89-slot question is fenced, not killed: the @275/@1377/@1393 parses
("veut/vient-pour [X]er [89-N/adv]") remain standing, and the @113/@781 failures are
evidentiary fences re-openable if 93 gains stem evidence or @781's left edge re-parses.

## Adverses

- "89=noun LEAD ratified R19-161: do not overturn without red-team declaration" —
  ANSWERED by compliance: this battery uses only noun/adverb frames for 89 throughout;
  the killed infinitive-89 rival is never invoked; no class is named, no polyvalence
  declared, §7 intact. No standing or red-team verdict contradicted, downgraded, or
  re-litigated.

## Scope

- Fences only the unification question for the five "29 89" windows. Untouched:
  er89-wordinternal-govern's KILL (word boundary stands), the @275/@1377/@1393
  infinitive-complement parses, 89's noun LEAD, 93's verb class, 08's letter tier,
  the 67 positional rule, A8/A10, §7. Canonical-stream caveat stands
  (rows a1_03/a2_03/a5_04/a7_06/a7_07 offsets unvalidated).

## Follow-ups (for supervisor queuing; all verified ABSENT from battery-queue.json)

1. `stem-93-29-test` (P3) — test 93 as a verb stem via independent stem-shaped 93 windows;
   if "[93]er" becomes an attested infinitive, re-test W1's (@113) frame under Frame F.
2. `licensor-89-781` (P4) — find a battery-grade licensor for standalone 89 at @781:
   test the "[89-N] la [24-fin]" subject frame against "[37] [08]er" resegmentation arms.
3. `frame-89-erinf-3of5` (P4, red-team input) — package the 3/5 parse result plus the two
   fenced windows (@113, @781) as input to the 89 docket; the W1/W3 failures may mark
   conditioned splits (§7 venue, red-team adjudication).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-x-er-89-frame.md` (this file).
- Queue: `x-er-89-frame` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed —
  was queued/verdictless; target-id-unique tmp `battery-queue.json.x-er-89-frame.tmp` +
  atomic rename; disk re-validated; own entry only; no downgrade; no tmp leftover).
- Lock `code/crowd17/next-token/locks/x-er-89-frame.lock`: created on start
  (2026-10-09T20:33:38Z, no prior/stale lock), deleted on completion (verified gone).
- R5005, sealed gates, red-team adjudication queue untouched.
