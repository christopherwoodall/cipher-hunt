# Battery npframe-60-454 — class adjudication at @454

Worker: battery. Date: 2026-10-09. Stream: repaired 1,847-pair parse
(`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`,
parsed like `code/side-keyhunt/repair_parse.py`; `canonical.py` never used).
R5005, sealed gates, red-team queue untouched.

## Bar (verbatim from queue)

"if no verbal 60 parses @454 under <=1 unstated assumption, @454 forces
non-verbal 60; combined with @1338 forcing verbal, 60's polyvalence is proven
pending red-team ratification (feed poly-60-redteam)"

## Numbered clauses (fixed before examining @454 in detail)

1. (C1) Enumerate verbal-60 candidates — finite verb, present participle, past
   participle — against "77 60 65" using only banked/granted/promoted/
   provisional values (77="le" provisional, 65=noun-class battery-promoted).
2. (C2) A candidate counts iff the resulting French is grammatical in 1841
   diplomatic French with ≤1 unstated assumption. Unstated assumption =
   any value, boundary, or re-segmentation not in the
   banked/granted/promoted/provisional set (per participle-60's C3
   definition). The 60 value hypothesis itself counts as 1.
3. (C3) If no candidate parses within budget, @454 forces non-verbal 60 and
   the polyvalence proof feeds poly-60-redteam. If any candidate parses,
   the @454-based non-verbal proof fails.

## Window (re-derived, 0-based @-offsets)

@448–461: `59 32 48 79 17 77 60 65 13 66 14 02 79` (row a2_10).
Target trigram @453–455: `77 60 65` = "le[77] [60] [65-noun]".
Left context @451–452: `79 17` = "tout fois" — adverbial ("toutefois",
however, or "toutes les fois"); not a subject. No overt subject for a
finite-verb clause anywhere in @444–453 (`41 10 62 61 59 32 48`).

## Per-candidate results

**(a) 60 = finite verb.** "le" (article) + finite verb is ungrammatical.
Rescue: read 77 as the clitic pronoun ("[subj] le [60-verb] [65-obj]").
The clause would need a subject; none is overt (see left context above),
so the rescue needs a second unstated assumption (pro-drop, ungrammatical
in 1841 French) on top of the value hypothesis. Over budget. FAIL.
(Agrees with participle-60's V2, which found the same rescue STRAINED.)

**(b) 60 = present participle.** "le [participle] [noun]" as pre-nominal
epithet is ungrammatical in 1841 French; participles in epithet position
are post-nominal ("le jour suivant") or lexicalized adjectives.
FAIL with 0 assumptions spent. (Agrees with participle-60's V1.)

**(c) 60 = past participle, dit-class.** "le dit [65]" — "ledit/ladite" +
noun is fully grammatical and highly productive in 1841 diplomatic French
("ledit traité", "ladite somme", "lesdits ministres"; Littré s.v. "dit":
part. passé de dire employé adjectivement). Costs exactly 1 unstated
assumption (the value hypothesis itself); 77="le" and 65=noun-class are
already in the standing set. PARSES within budget.

No re-segmentation, elision, or second value is needed for (c).

## Verdict: NULL

C3's conditional does not fire: a verbal (participial) 60 parses @454
under exactly 1 unstated assumption, so **@454 does not force non-verbal
60**. The @454-based proof of 60's polyvalence fails.

What survives, sharpened: the verbal value that parses @454 (past
participle) is a different verbal form from the one forced at @1338
("64 60 08" = "qui [60] [08]" — "qui" requires a finite verb). So the
polyvalence question stands, now specified as participle-vs-finite rather
than verbal-vs-non-verbal. No polyvalence is declared here (§7: 67 et/veut
remains the sole true polyvalence); this feeds the existing P1
poly-60-redteam docket, no duplicate created.

Note for the red team: 60="dit" (dire — past participle and 3sg present
syncretic, one lexeme) parses BOTH @454 ("le dit [65]") and @1338
("qui dit [08]" = "who says [08]") with the same surface form. That would
be monovalent, not polyvalent. participle-60 tested present participle and
finite -dre stems but never "dit". Pre-registered adverses for the
follow-up: @1644 ("98 60 03" — under 98="vient", "vient [60]" wants an
infinitive, and "dit" is not one) and @690 ("94 29 60 03" — "ne er dit
[03]" looks ungrammatical) are hostile to "dit".

## Follow-ups proposed (for supervisor queuing)

1. `dit-60-syncretic` (P2): test 60="dit" (dire, syncretic pp/3sg-pres)
   across the six windows @454/@690/@1644/@1674/@1338/@700; promote iff all
   parse with ≤1 total unstated assumption; kill iff any window forces
   otherwise. Adverses: @1644 and @690 hostile (above); coordinates with
   (does not duplicate) participle-60's V1/V2.
2. `npframe-60-690` (P2): mirror of this target at @690 ("94 29 60 03" =
   "ne er [60] [03]") — does any verbal 60 parse there within budget?
   Pairs with npframe-60-454 to map which NP frames admit verbal 60.
3. `ledit-60-corrob` (P3): @454 is the only "77 60 [noun]" window
   (full 60 census: 18 occurrences re-derived). Scan 60's other 17 windows
   for a second participial-shaped frame; if none, the @454 participial
   parse stands as a singleton leg (weakens, does not kill).

## Bookkeeping

- Lock `code/crowd17/next-token/locks/npframe-60-454.lock` created on start
  (agent id + UTC), deleted on completion.
- Queue update: temp-file + rename on `battery-queue.json`, own entry only;
  pre-write assert confirmed no prior verdict; JSON re-validated after write.
- No standing verdict contradicted or downgraded.
