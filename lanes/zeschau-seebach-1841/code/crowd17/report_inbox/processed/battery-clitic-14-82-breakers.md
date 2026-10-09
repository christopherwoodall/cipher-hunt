# Battery verdict: clitic-14-82-breakers — the '82 14' x2 windows do NOT break the tie

- Target: `clitic-14-82-breakers`
- Claim: the '82 14' x2 windows break the clitic-vs-determiner tie
- Worker: battery-worker clitic-14-82-breakers (72c4a2e0-43d9-4fd5-b9eb-438aab589160)
- Date: 2026-10-09
- Verdict: **NULL** (fence as tie, per the bar's else-branch)

## Pre-registered bar (verbatim)

"name 14's class iff '82 14' @623 ('82 14 59') and @896 ('82 14 98') both parse under one class with 82='m' banked (clitic cluster vs determiner after elided 'm''), <=1 stated assumption; else fence as tie"

## Bar as numbered clauses (fixed before testing)

- C1: W1 (1-based @623, row a4_01: `76 82 14 59 37 33`) parses as a full grammatical window under one class for 14 (clitic or determiner), with 82='m' banked, <=1 stated assumption.
- C2: W2 (1-based @896, row a5_08: `98 82 14 98 83 86`) parses as a full grammatical window under the SAME class for 14, with 82='m' banked, <=1 stated assumption.
- C3 (adverse): 59='est' is provisional at W1 — answered, not ignored.
- C4 (adverse): 98's value is open at W2 — answered, not ignored.
- Else-branch: if C1 and C2 do not both pass under one class, fence as tie.

## Method

- Stream: repaired 1,847-pair parse from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, tokenized per `code/side-keyhunt/repair_parse.py`. `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
- @-offsets below are 1-based pair indices on the repaired stream, re-derived by script in this run. Both '82 14' bigrams are the only two stream-wide (byte-count verified: 2).
- W1: 0-based @622 = 1-based @623, row a4_01: `29 88 37 [76 82 14 59 37 33] 29 87 78 67 08` — core trigram row-internal.
- W2: 0-based @895 = 1-based @896, row a5_08: `01 [98 82 14 98 83 86] 16` — core trigram row-internal (row boundary falls after @900, outside the window).
- Standing premises used as given (not re-litigated, zero stated assumptions consumed): 82='m' (GT, letter); 59='est' (provisional); 29='er' (GT); 87='ce' (prom); 76=noun (lead, battery-promoted); 33=INF (cls); 86=INF (cls); 88=gov (cls); 98=finite-verb class (prof-98, promoted); 83='de' (lead); 14's verb class fenced lane-wide (stem-14-84-retest, NULL); 14='le' killed as a window-independent (global) value at kill grade (le-14-kill-1121, KILL).
- 1841 diplomatic French is the grammaticality standard throughout.

## Window evidence

### Letter-strictness correction (applies to both windows)

82='m' is a banked letter (gloss "la pre m i er e"). The lane's own A7-L2 frame shows "me" spelled 82+48 ('e'). Therefore "82 14" CANNOT be "me le" (tout-slot-14's C3 note was loose): "me" requires 82+48, and "82 14" reads "m"+"le" = "mle", not a word. The only letter-strict clitic-cluster readings of "82 14" are elided "m'" + vowel-initial clitic: "m'en", "m'y". This correction tightens tout-slot-14 (already a fence); it overturns nothing.

### H-DETERMINER (14 = determiner)

- W1: "14 59" = "[det] est". 59='est' (provisional) is a finite verb. A determiner requires a following nominal head; the followers are 59 (verb), 37 (predicative, A1), 33 (infinitive) — no nominal head anywhere downstream in the window. "le est" is ungrammatical for every determiner value. Independently, the only determiner value ever named for 14 ('le') is now killed globally at kill grade (le-14-kill-1121) — no live determiner value remains. DEAD at W1 (kill grade, conditional on 59='est').
- W2: "14 98" = "[det] [98]". 98 is finite-verb class (promoted). "le vient" is ungrammatical for every determiner value, independent of 98's value. DEAD at W2 (kill grade, value-independent).
- Determiner arm: dead at both windows.

### H-CLITIC (14 = clitic pronoun; letter-strict: "m'" + vowel-initial 14)

- W1: "[76-noun] m'en est [37-pred] [33-inf]er". The core "[76] m'en est [37-predicative]" is literary-grammatical on the "il m'en est resté / garant" pattern (76=noun lead supplies the subject; 59='est' provisional). But the full window blocks at "37 33": a predicative (A1) followed by a bare infinitive (33=INF cls) is ungrammatical in the same clause, and placing a boundary after 37 leaves "[33]er ce [78-ver]" ("*partir ce") unparseable. 14='y' is worse: "m'y est" — "être" takes no "y". Best achievable: a fenced partial core-parse, NOT a full-window parse.
- W2: "[01] [98] m'en [98] de [86-inf]". Two finite verbs in sequence ("[V] m'en [V]" dies for any finite V), and "vient m'en" violates clitic order — French clitics precede the finite verb outside imperatives/interrogatives ("je m'en viens", "j'en viens"; never "vient m'en"). No row-internal boundary exists between 14 and the second 98 (all row a5_08), and one would not save "vient m'en" regardless. DEAD at W2 (value-independent).
- Clitic arm: no full-window parse at either window (partial core at W1 only).

## Per-clause pass/fail

- C1: FAIL. Neither class yields a full grammatical parse of W1 (determiner kill-grade dead; clitic best case is a fenced partial core blocked at "37 33").
- C2: FAIL. Neither class parses W2 (determiner: "le [V-fin]"; clitic: "[V-fin] m'en [V-fin]" / clitic-order violation).
- C3 (59='est' provisional): ANSWERED. The W1 determiner kill and the W1 clitic core-parse are both conditional on 59='est'; if the provisional falls, W1 needs re-audit. W2 results do not depend on 59.
- C4 (98's value open): ANSWERED. Both W2 kills are value-independent — 98's promoted verb class suffices ("le [V-fin]" and "[V-fin] m'en [V-fin]" die for any finite verb). 98='vient' (battery-promoted, pending ratification) was used illustratively only.
- Else-branch: FIRES. Neither class parses both windows → fence as tie.

## Verdict: NULL (fence as tie)

The '82 14' x2 windows do not break the clitic-vs-determiner tie. Recorded asymmetry for the red team (not a naming — the bar's criterion is unmet): the determiner arm is doubly dead (structural kill at both windows AND its only named value 'le' killed globally by le-14-kill-1121), while the clitic arm retains a grammatical core at W1 ("[76] m'en est [37]", literary). The tie is lopsided, but the bar requires both windows to parse under one class, which no class achieves.

## Notes for the red team (escalations, not adjudications)

1. Battery-vs-battery tension: vient-98-name's @894 aside parses "[01] vient m'[14]" CONDITIONAL on "14 vowel-initial infinitive" — that condition is now fenced lane-wide by stem-14-84-retest (NULL). vient-98-name's bar clause 1(b) (@897 '[14] vient de [86-inf]') does not depend on @894, but its clause 7 (zero board contradictions) may need re-audit. Proposed follow-up `vient-98-894-reaudit` below; red-team adjudication if the re-audit fails.
2. The "37 33" adjacency (predicative + bare infinitive) is the load-bearing blocker for W1's clitic core-parse. Any future 14-clitic case at W1 must dissolve it (boundary, 37 re-class, or 33 re-parse).
3. tout-slot-14's C3 "me le" compatibility note is corrected above (letter-strictness); its fence verdict is unaffected.

## Proposed follow-up targets (null regeneration)

1. `vient-98-894-reaudit` (priority 2). Claim: vient-98-name's promote survives stem-14-84-retest's lane-wide 14-verb fence. Bars: "promote stands iff vient-98-name's bar clauses 1–6 pass without the @894 'vient m'[14-inf]' conditional parse and no new contradiction is introduced by the fence; else escalate to red team as a battery-vs-battery contradiction."
2. `clitic-14-623-steelman` (priority 3). Claim: W1 admits a full-window clitic parse. Bars: "produce a complete grammatical parse of 1-based @619–631 (row a4_01) under 14='en' (clitic) with <=1 stated assumption, resolving the '37 33' continuation (boundary placement, 37 re-class, or 33 re-parse); else record the exact blocking adjacency."
3. `en14-three-window` (priority 3). Claim: 14='en' (the only letter-strict "m'"+clitic value) is viable. Bars: "test 14='en' at 1-based @623, @896, and @178 ('[69] en [24-verb]', the clitic reading's best leg per tout-slot-14); keep the 'en' arm iff >=1 window yields a grammatical local parse under standing values; else kill 14='en' at battery grade."
