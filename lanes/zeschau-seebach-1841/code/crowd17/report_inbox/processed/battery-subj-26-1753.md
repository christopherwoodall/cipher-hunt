# Battery report: subj-26-1753

- Target id: `subj-26-1753`
- Claim: "discriminate the single '26 [24]' @1753 window: adverb vs subject reading of 26"
- Date: 2026-10-09
- Worker: battery worker (subagent 80a58ddb-0d00-46d7-9d17-ebe176a3e1e4)
- Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` +
  `code/side-keyhunt/repaired_offsets.json`, parsed byte-exact per
  `code/side-keyhunt/repair_parse.py`; 1,847 pairs / 96 types re-asserted
  in-session). `canonical.py` never used. R5005, sealed gate instances,
  red-team adjudication queue untouched.
- Lock: `code/crowd17/next-token/locks/subj-26-1753.lock` (created at
  start; no prior lock existed; deleted on completion).

## Bar (verbatim, pre-registered BEFORE testing)

"adverb vs subject reading of 26 via 24's subject profile (24 takes
84='on'/46='que'/94='ne' subjects; 26 never precedes 24 elsewhere)
stated; if a subject reading holds, the category-clash arm re-opens;
if not, the kill hardens"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** Parse @1753 with 26 as adverb ("[26-adv] [24-verb]") and as
   subject ("[26-subj] [24-verb]") under standing values, with 24's
   subject profile stated from the stream.
2. **C2:** Kill one arm iff it fails at kill grade.
3. **C3:** If neither arm fails at kill grade, fence with the surviving
   candidates stated.

## Method

1. Re-derived the repaired stream byte-exact per `repair_parse.py`
   (1,847 pairs / 96 types asserted). All @-offsets below are 0-based
   repaired-stream pair indices, matching the prior batteries on this
   window (task's "@1753" = 0-based index of 26).
2. Censused 24's full predecessor profile (n(24)=52) to state its
   subject profile from bytes.
3. Tested the subject arm against every live class hypothesis for 26
   (noun / verb / pronoun) under standing values, without re-running
   the noun-26 umbrella bar and without re-litigating noun26-89-class.
4. Standing inputs (cited, not re-litigated): battery-noun-26 (NULL;
   stated positional rule: 26 = feminine noun iff preceded by 11=la,
   else verb-branch — pending red team); noun26-89-class (PROMOTE,
   conditioned split; @1752's 89 = noun arm conditional on provisional
   77='le'); 26-class-1754 (PROMOTE, conditional; surviving parse at
   @1754 is the gerund "[26-V] en [85] [58]"); pasent-subject-26-56
   (KILL; 3pl-subject hypothesis for 26/56 killed at kill grade);
   A2 23~26 SPLIT; banked pencil values; §7 (67 et/veut sole true
   polyvalence).

## Window-level evidence

Target window (row a8_08, 0-based), byte-confirmed:

| @ | 1751 | 1752 | 1753 | 1754 | 1755 | 1756 | 1757 | 1758 |
|---|------|------|------|------|------|------|------|------|
|   | 28   | 89   | 26   | 24   | 85   | 58   | 17   | 78   |

So the '26 24' bigram is 26@1753–24@1754, left neighbor 89, right
neighbor 85. Byte-identical to the window in pasent-subject-26-56
and 26-class-1754 (those reports index 58 at @1756; consistent).

**24's subject profile (from bytes, n(24)=52):**

| predecessor | count | role |
|-------------|-------|------|
| 11          | 4     | la (det) |
| 01          | 3     | value-open |
| 13          | 3     | value-open |
| 84          | 3     | 'on' — 3sg subject pronoun |
| 46          | 3     | 'que' — relative, subject-bearing clause head |
| 94          | 2     | 'ne' — directly before finite verb (STRONG LEAD) |
| 14/16/49/86/02/88 | 2 each | mixed |
| singletons (19 incl. 26, 09, 83, 98) | 1 each | — |

The stated profile is confirmed: 24's subject-bearing predecessors
are exactly 84='on' (x3), 46='que' (x3), 94='ne' (x2). **26 precedes
24 exactly once stream-wide (@1753).** Confirmed: "26 never precedes
24 elsewhere" is byte-true. Notably, every attested subject-bearing
predecessor is either a licensed subject (84, 46) or a pre-verbal
particle (94) — 26 is in none of those classes.

**26's class evidence at @1753 (n=17 census, re-derived):** the only
nominal legs are "11 26" x2 (1-based @241, @1561) = feminine-singular
"la [26]". Left neighbor at @1753 is 89, not 11 — verb-branch under
the stated positional rule.

## Per-clause pass/fail

**C1: PASS.** Both arms parsed under standing values:

- Arm S (subject): "[26-subj] [24-finite/modal-verb] …" — needs 26
  nominal (finite 24 needs an overt subject; French has no pro-drop;
  26 is the only subject candidate: 89 is left of 26, 85 right of 24).
- Arm A (adverb): "[89-S?] [26-adv] [24-finite/modal-verb] …" — 26
  adverbially modifies 24; the subject slot is 89's (noun arm) or
  stays fenced. This arm is live only under the modal-24 frame; under
  the 24='en' frame 26 is the finite verb (26-class-1754's surviving
  parse), which is untouched here.

**C2: FIRES — the subject arm is killed at kill grade.** The kill is
threefold and independent of the pending positional rule:

1. **Verb-branch category clash.** Under the stated positional rule,
   26 at @1753 (left neighbor 89, not 11) is verb-branch; a verb
   cannot be a subject — kill grade, same instrument as the pasent
   kill.
2. **Bare-noun grammar.** Even setting the positional rule aside, 26's
   only noun evidence is feminine-singular ("la [26]" x2). A bare
   singular count noun cannot head a subject position in 1841 French
   (requires "la [26]"); the left neighbor 89 is not a determiner
   under any live arm (89's noun arm = noun, not determiner; A8's
   verb-frames = verb). No determiner, no subject.
3. **Pronoun rescue §7-barred.** A 3pl/pronominal 26 would be a second
   polyvalence for this battery to declare — barred by §7 (red-team
   act only), as established in pasent-subject-26-56.

No window forces 26-as-subject: the adverb reading remains fully
available (zero byte contradictions), so the discrimination resolves
by kill, not by promotion.

**C3: does not apply.** C2 fired; no fence needed for the subject arm.
Arm A (adverb) is not promoted (no value named; adverb-26 has no
positive evidence beyond compatibility) — it remains the live
compatibility arm under the modal-24 frame, and the 24='en'/26=finite-verb
gerund parse remains the surviving parse of 26-class-1754.

## Adverses answered

- "noun-26 NULL": ANSWERED. The umbrella's NULL is respected: its
  stated positional rule is cited as a stated condition (pending red
  team), its la-only noun legs are cited as evidence, and its bar was
  not re-run. No value for 26 declared.
- "23~26 SPLIT standing": ANSWERED. The A2 split is respected
  throughout; no homophone rescue via 23 was attempted; 23 plays no
  role in any parse.

## Verdict: KILL

The subject reading of 26 at @1753 is **killed at kill grade** on all
three live class hypotheses. The pasent-subject-26-56 category-clash
kill **hardens**: "26 never precedes 24 elsewhere" is byte-confirmed
(1/52 predecessors), and 24's subject-bearing predecessors are
exclusively 84/46/94-class — a profile 26 satisfies at zero windows.
No standing or red-team verdict contradicted or downgraded (§7 intact;
24-en-verb-conflict's modal-24 arm untouched — the kill is of
26-as-subject, not of modal 24).

No follow-ups required for a kill. Note for the red team: if the
24 red-team docket ratifies a new subject profile for 24 that admits
a bare-singular nominal subject, this kill re-opens.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-subj-26-1753.md` (this file).
- Queue: `subj-26-1753` queued → verdict/kill via temp-file + rename,
  own entry only; pre-write assert confirmed no prior verdict (status
  was `queued`, verdict null); JSON re-validated post-write; claim,
  bars, evidence, adverses preserved.
- Lock deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
