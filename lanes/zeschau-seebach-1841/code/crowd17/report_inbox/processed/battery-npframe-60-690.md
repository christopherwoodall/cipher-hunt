# Battery npframe-60-690 — mirror class adjudication at @690

Worker: battery. Date: 2026-10-09. Stream: repaired 1,847-pair parse
(`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`,
parsed like `code/side-keyhunt/repair_parse.py`; `canonical.py` never used).
R5005, sealed gates, red-team queue untouched.

## Bar (verbatim from queue)

"pairs with npframe-60-454 to map which NP frames admit verbal 60; any
verbal 60 parsing within budget is a positive"

## Numbered clauses (fixed before examining @690 in detail)

1. (C1) Enumerate verbal-60 candidates — finite verb, infinitive, past
   participle, present participle — against "94 29 60 03" using only
   banked/granted/promoted/provisional values (94="ne" STRONG LEAD per
   R17-001, 29="er" pencil ground truth).
2. (C2) A candidate counts iff the resulting French is grammatical in 1841
   diplomatic French with ≤1 unstated assumption. Unstated assumption =
   any value, boundary, or re-segmentation not in the
   banked/granted/promoted/provisional set (per npframe-60-454's C2).
   The 60 value hypothesis itself counts as 1.
3. (C3) If any candidate parses within budget, record the positive (which
   verbal class @690 admits). If none parses, @690 is a non-verbal-60
   frame within budget; the 454/690 pair maps one admitting frame
   (@454, participial) against one refusing frame (@690) for the
   red-team polyvalence docket. No polyvalence is declared here (§7:
   67 et/veut remains the sole true polyvalence).

## Window (re-derived, 0-based @-offsets)

@678–700: `45 23 09 07 00 92 64 29 40 65 94 29 60 03 39 74 46 02 50 45 28 94 60`
(row a5_00).
Target span @688–691: `94 29 60 03` = "ne[94] er[29] [60] [03]".
Left context @684–687: `64 29 40 65` = "qui[64] er[29] e[40] [65-noun]".
Right context @692–694: `39 74 46` ("[39] [74] que[46]").

Standing values spent: 94="ne" (STRONG LEAD, 0 assumptions — leads count
as standing per npframe-60-454 method), 29="er" (pencil GT, 0 assumptions).
Total unstated assumptions available: 1 (the 60 hypothesis itself).

## Per-candidate results

**(a) 60 = finite verb.** "ne er [V-finite] [03]" — banked 29="er" is
neither pronoun, adverb, nor clitic; 1841 French has no clause shape
"ne er V". Re-segmentation audit (coordinated with, not duplicating,
dit-60-syncretic's exhaustive W2 audit): 94 leftward ("[65]ne er [V]")
strands "er [V]"; 94-29 fused ("ner[V]") is not a French word; 29-60
fused ("er[V]") is not a French word for any verbal 60 ("redit" would
require 29="re", contradicting banked 29="er"). FAIL with 0 assumptions
spent. The argument is form-independent: it kills finite-verb 60
generally, not just "dit"-as-3sg.

**(b) 60 = infinitive.** "ne" cannot negate an infinitive in 1841 French
(cf. ce-inf-1841 kill: the substantivized infinitive takes "le", never
"ce"; "ne"+infinitive is ungrammatical outside fixed "ne savoir
que"-type constructions, which are unavailable here). Banked "er"
intervenes regardless. FAIL with 0 assumptions spent.

**(c) 60 = past participle.** "ne" cannot negate a bare participle; no
auxiliary is present; banked "er" is stranded between "ne" and the
participle. This is the same structural block as dit-60-syncretic's
past-participle arm, which failed at kill grade at this exact window
("ne er dit [03]" ungrammatical under every available segmentation).
FAIL with 0 assumptions spent.

**(d) 60 = present participle.** "ne" + participle is ungrammatical
(participle-60's @700 finding); banked "er" intervenes on top of that.
FAIL with 0 assumptions spent.

**Robustness note.** The failure is independent of 94's value:
dit-60-syncretic's audit showed "NO rescue exists under any 94 value"
because banked pencil GT 29="er" directly abuts 60 — so 94's
particle/syllabic duality (the 94-duality docket) does not reopen @690
within budget. The one route that audit did not exhaust is leftward
fusion of 94 into 65 (@687-688, "[65]94" as one word), which would
dissolve "ne" but still strand "er [60]"; proposed as follow-up #2
below with honest negative expectation.

## Verdict: NULL

No verbal 60 parses "94 29 60 03" at @690 within budget — no positive
under C3. The bar carries no promote clause and no kill clause, and no
standing verdict is contradicted (this agrees with participle-60's V1/V2
fails and dit-60-syncretic's kill at this window; no red-team value
verdict on 60 exists).

**Mapping result (the deliverable):** @454 admits verbal 60
(participial "ledit [65]", npframe-60-454 (c), 1 assumption) while @690
admits no verbal 60 within budget. The 454/690 pair is now mapped:
one admitting NP frame, one refusing NP frame. This feeds the existing
P1 poly-60-redteam docket — no duplicate created, no polyvalence
declared (§7).

## Follow-ups proposed (for supervisor queuing)

1. `npframe-60-1674` (P2): mirror class adjudication at @1674
   ("92 60 03", row a8_04: `78 55 81 92 60 03 39 74 77`) — does any verbal
   60 parse within budget? Completes the NP-frame map (454: yes,
   participial; 690: no). Adverses: 92's class open (dit-60-syncretic
   W4: neutral/open); coordinate with (do not duplicate)
   participle-60's W3.
2. `reseg-690-leftedge` (P3): test leftward fusions @687–689
   ("[65]94" one word; "94 29" = "ner"-shaped) as the only segmentation
   routes dit-60-syncretic's audit did not exhaust; kill iff every
   fusion strands "er" or contradicts banked 29="er". Expected outcome:
   negative (closes the segmentation space at @690).

## Bookkeeping

- Lock `code/crowd17/next-token/locks/npframe-60-690.lock` created on start
  (agent id + UTC), deleted on completion.
- Queue update: temp-file + rename on `battery-queue.json`, own entry only;
  pre-write assert confirmed no prior verdict; JSON re-validated after write.
- No standing verdict contradicted or downgraded.
