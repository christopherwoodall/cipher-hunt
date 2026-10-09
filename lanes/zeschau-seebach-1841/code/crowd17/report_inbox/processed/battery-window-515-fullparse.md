# Battery report: window-515-fullparse

- Target id: `window-515-fullparse`
- Claim: full-context parse of @507-522 independent of the re-segmentation; decide whether '87 77 80' must attach left or right
- Date: 2026-10-09
- Worker: battery worker (subagent e00815c5-38af-4839-b85c-4c371ef7586e)
- Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; asserts held: 1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed gate instances, red-team adjudication queue untouched.

Terms (ASD-STE100): "full-window parse" = one grammatical French reading that covers every group from @507 to @522. "Ungranted assumption" = a value for a group that is not in the standing list in BATTERY-PROTOCOL.md section 7. "Attach left" = the group belongs to the clause before it. "Attach right" = the group opens or joins the clause after it. "Residual" = a window that cannot be parsed cleanly and is set aside with a stated cause.

## Bar (verbatim from the brief)

"one full-window parse of @507-522 with <=1 ungranted assumption; fence as residual if no clean parse"

Numbered pass/fail clauses (restated before testing, not modified after):

1. C1: produce one full-window parse of @507-522 that uses zero or one ungranted assumption.
2. C2: decide whether "87 77 80" (@515-517) must attach left or right.
3. C3: if no clean parse exists under C1, fence the window as a residual with a stated cause.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/window-515-fullparse.lock` on start (agent id + 2026-10-09T11:16Z); deleted on completion. Note: no pre-existing lock was checked before creation (minor worker gap; no evidence of a prior lock).
2. Re-derived the repaired stream in-session. Window @507-522 (0-based), all row a3_00:
   - @507=77 @508=62 @509=94 @510=64 @511=98 @512=65 @513=88 @514=56
   - @515=87 @516=77 @517=80 @518=09 @519=70 @520=91 @521=77 @522=06
   - Left context @500-506: 29 40 56 39 68 21 67. Right context @523-529: 55 81 97 47 44 59 37.
3. Held section 7 fixed: 87=ce, 64=qui, 70=pre, 29=er, 40=e, 77=le (provisional), 80/89 verb-frame (A8, value open), 59=est (provisional), 47=ce, 37 predicative frame (A1). 62='on' unconditioned is KILLED (collision-62-84); 62='il' is a demonstrated rival, not promoted. 94='ne', 30='pas', 39='a', 06='ent/ment', 81=noun are battery-promoted but pending ratification, so they count as ungranted under the bar.

## C1: full-window parse attempt (FAIL)

Three segments, three independent breaks.

Break 1 — left half @507-511 = "le [62] ne qui [98]":
- 77=le (provisional, standing). 62 has no standing value. Spending the one assumption on 62='il' gives "le il ne qui" — ungrammatical ("le" and "il" cannot co-occur). 62='on' is killed unconditioned and gives "le on ne qui" — equally broken. 94='ne' is itself ungranted (pending ratification), and "ne qui" has no licensed frame: 64=qui is a relative, and no verb stands between them for "ne" to modify.
- Adopted, not re-litigated: @508 was already fenced as residual in collision-62-84 ("anomalous under both rivals").

Break 2 — core @515-517 = "87 77 80" = "ce le [80]":
- Finite-verb 80 (A8 frame): "ce le [verb]" is ungrammatical ("ce" cannot head a finite clause with an object clitic; it needs "est" or "c'est").
- Imperative 80 (imp-80-set): "ce le [imperative]" is ungrammatical (imperative objects are enclitic: "fais-le", not "le fais").
- Infinitive 80: red-team venue (poly-80-docket; inf-80-89-ratify returned NULL) — a new assumption, and even granted, "ce le [inf]" is unlicensed at this locus (no governor; inf-7780-reseg failed its C2 here).
- "87 77" = "celle" fusion: dead at this locus (it needs a relative 64/46 after; the follower is 80) — adopted from inf-7780-reseg.

Break 3 — right half @518-522 = "[09] pre [91] le [06]":
- Every bigram is a hapax (80-09, 09-70, 70-91, 91-77, 77-06 each n=1 stream-wide). No formulaic anchor. 70=pre is banked; 06='ent/ment' is pending ratification (ungranted), so "le [06]" cannot be licensed without spending the assumption.

Cheapest attempt: spend the one assumption on 94='ne'. The parse still breaks at 62 ("le"+"il"/"on" impossible) and at the "ce le [80]" core. No single ungranted assumption closes all three breaks. C1 FAILS. Per the bar, the window is fenced as a residual (see C3).

## C2: attachment of "87 77 80" (LEAN LEFT, undecided at battery grade)

- Left-attachment evidence: "56 87" occurs 2x stream-wide — @70 ("24 56 87 14 24 87 11") and @514. At @70, 87 follows 56 and is followed by 14, so 87='ce' naturally closes a left clause there. This is the only standing collocation evidence for 87's attachment, and it points left.
- Right-attachment evidence: none. "87 77 80" is a hapax trigram, and the "ce le [80]" core is ungrammatical under every standing reading (see Break 2).
- Lean: 87 attaches LEFT ("...[56], ce ..."), with "77 80" as the unparsed residue. Because no full clean parse exists, this is a lean, not a battery-grade decision. C2 PARTIAL.

## C3: fence (EXECUTED — stated cause)

Window @507-522 is fenced as a genuine residual. Cause: three independent breaks — (a) the left half needs a value for 62 that section 7 does not grant, and every candidate yields an ungrammatical "le [62]" sequence; (b) the "ce le [80]" core is ungrammatical under all standing readings of 80 (finite A8, imperative imp-80-set, infinitive red-team venue and unlicensed here); (c) the right half is locally unique (five hapax bigrams) with no formulaic anchor. No single ungranted assumption closes all three breaks. No standing or red-team verdict was contradicted or downgraded; section 7 intact.

## Verdict: NULL

Not promote: C1 fails (no full-window parse within the assumption budget). Not kill: the claim is procedural, and no window forces a positive claim false — the window resists parsing, which the bar routes to a residual fence, not a kill. Adverses: none listed.

## Follow-ups proposed (nulls regenerate work; all verified absent from battery-queue.json)

1. `87-left-attach-census` (P3) — census all "X 87" left-collocations and 87's full predecessor set; test whether 87='ce' systematically closes left clauses, with follower-class profiles (demonstrative-closing vs clause-opening). Discriminates the C2 left lean.
2. `ne-qui-94-64-census` (P4) — "94 64" is a hapax bigram (@509); census "94 [relative]" frames (94-64, 94-46) to test whether 94='ne' can ever precede a relative pronoun; locates whether the left-half break sits at 94 or at 62.
3. `syllabic-7780-word` (P4) — test the syllabic alternative: "87 77 80" as one word ("ce-le-[80]"-shaped), constrained by 80's syllable inventory from A8 verb frames and the banked "la premiere" syllable map; the clitic readings are exhausted, so a word-internal reading is the remaining structural rival.

## Bookkeeping

- Queue: `window-515-fullparse` -> `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock created on start, deleted on completion (verified gone).
