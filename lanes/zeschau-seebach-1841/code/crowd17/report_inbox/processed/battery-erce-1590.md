# Battery verdict: erce-1590

Target: `erce-1590` (priority 3). Follow-up #3 of battery-profile-29-left.
Date: 2026-10-09. Worker: 729b9405-8a3c-4ac1-af64-f1dbc1e9c23f.

## Bar (verbatim from battery-queue.json)

> produce one grammatical segmentation of @1590 honoring 29's syllabic profile

Numbered clauses (pre-registered before testing):
1. One segmentation of the "48 29 47" region at @1589-1591 (0-based; @1590 is
   the 29 position, queue convention) is produced.
2. The segmentation is grammatical in 1841 diplomatic French.
3. It honors 29's syllabic profile: 29 = 'er' (pencil GT); word-initial 29
   reads "erre" (3sg of *errer*) per the profile-29-left PROMOTE finding;
   word-internal 29 reads "-er-" (infinitive "-er", "-iere" suffix, "enterre").

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session
(`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`,
parsed per `code/side-keyhunt/repair_parse.py`; 1,847 pairs / 96 types
verified). `canonical.py` never touched. R5005, sealed gates, red-team
adjudication queue untouched.

Standing values used: 65 = noun class (R18 ratified); 48 = 'e' letter-tier
(R17-003; fem-e-48 battery PROMOTE: 48 serves as feminine/inflectional -e in
the 32-48 x4 and 19-48 x1 frames); 29 = 'er' (pencil GT; profile-29-left
PROMOTE: 29 occurs word-initially as "erre"); 47 = "ce" (A4, allophone tier
with 87). 08's value/class is open (n=18, heterogeneous contacts, no class).

## Window evidence (all byte-traced)

- Target span @1586-1595, all mid-row a8_02:
  `70 64 65 48 29 47 08 81 03 29`
  ("pre" "qui" [65-noun] "e" "er" "ce" [08] [81-noun] [03-stem]"er").
- "29 47" bigram occurs exactly 4x stream-wide (29-position, 0-based):
  @22 ("43 29 47", 43 open - fenced in profile-29-left),
  @422 ("36 29 47", 36 open - fenced),
  @1230 ("48 29 47" after "82 48" = "me" - POSITIVE positional: "me" is a
  complete word, forcing 29 word-initial, "me"+"er[re]"),
  @1590 (this target).
- "47 08" occurs exactly 1x stream-wide (@1591-1592); 08 undecided.
- "65 48" occurs exactly 1x stream-wide (@1588-1589).

## Segmentation: "65 48 | 29 | 47" = "[65]e" | "erre" | "ce"

- **"[65]e"**: 65 (noun class) + 48 ('e' as feminine/inflectional -e) forms one
  complete feminine-noun word. This extends fem-e-48's promoted -e function
  (32-48, 19-48) to the 65 noun. Stated assumption (1): 48 is the
  inflectional -e on the 65 noun. 48 cannot stand alone ('e' is not a word),
  so it must attach left; 65 is its only neighbor.
- **Boundary before 29 is forced**: "[65]e" is a complete word, so 29 is
  word-initial - the same positional logic as @1230 ("me" + word-initial 29).
- **"erre"**: 29 word-initial = 3sg of *errer* ("wanders"), the established
  word-initial-29 lexicon from profile-29-left's PROMOTE ("qui erre" @291/@685,
  "l'on erre" @147, "cela erre" @500, "n'erre" @689). Subject "[65]e" (3sg
  noun) agrees with 3sg "erre". *Errer* is intransitive, so the clause
  "[65]e erre" is complete at "erre".
- **"ce"**: 47 = "ce" opens the next clause as demonstrative. Exact parallel:
  @147 reads "29 87" = "erre, ce qui" (profile-29-left strong positive); here
  "29 47" = "erre ce" with 47 the A4-allophone of 87. The complement
  ("ce [08]...") is left open - 08's value is a separate undecided question
  and outside this bar's scope.

## Rival placements (exhaustive, all dead)

- "65 | 48 29 | 47": "48 29" = "eer" - no French word contains "eer". DEAD.
- "65 48 29 | 47": "[65]eer" - same "eer" impossibility. DEAD.
- "65 | 48 | 29 47": 48 = 'e' standing alone is not a French word. DEAD.
- 29 word-internal with 47 ("erce"): no French word contains "erce" - this
  was the original "erce problem" statement. DEAD.

Word-initial "erre" is therefore not just one grammatical reading but the
unique surviving reading of the trigram.

## Per-clause verdicts

1. Segmentation produced ("[65]e" | "erre" | "ce"): **PASS**.
2. Grammatical: subject-verb "[65]e erre" (3sg agreement) + clause-initial
   "ce", with the intransitive boundary exactly as at @147: **PASS**.
3. Honors 29's syllabic profile (word-initial "erre" per profile-29-left
   PROMOTE; "eer"/"erce" word-internal readings excluded): **PASS**.

Adverses: none listed. No standing verdict contradicted or downgraded; no
polyvalence declared (§7 intact); no values named for 65 or 08 (locus-level
finding only).

## Verdict: PROMOTE (finding grade, locus-level)

The "erce" residual from profile-29-left is resolved at @1590: the trigram
parses as feminine noun "[65]e" + "erre" (3sg) + clause-initial "ce", under
one stated assumption (48 = inflectional -e on the 65 noun, parallel to the
promoted 32-48/19-48 frames). Residual for the lane: the "ce [08]" clause
completion waits on 08's class/value.
