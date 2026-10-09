# Battery `seg-88er-1049` — verdict: PROMOTE

## Bar (verbatim, pre-registered)

"Segmentation resolved with byte evidence at battery grade; else fence."

Numbered clauses:
- C1: The segmentation at @1049 ('[88]er' + 'e...' vs '[88]ere'-one-word) is resolved with byte evidence at battery grade.
- C2 (else): Fence.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`
(parsed like `repair_parse.py`; asserts held: 1,847 pairs, 96 types).
`canonical.py` never used. Locus byte-confirmed (0-based, row a6_04):

`[1044]11 [1045]67 [1046]76 [1047]85 [1048]41 [1049]88 [1050]29 [1051]40 [1052]29 [1053]74 [1054]74`

Banked pencil GT (§7, inviolable): 29="er", 40="e".

Ran the two bar-mandated censuses:
1. 40's word-final-'e' profile (n(40)=21, follower distribution).
2. The 29-40 collocation census (9 bigrams stream-wide).
Plus a period-corpus check (`code/side-period/corpus`, ~34.5M chars) for
"eer"-initial vs "er"-initial French words.

## Findings

### 1. 29-40 collocation census

Nine "29 40" bigrams at @62, @291, @500, @597, @685, @758, @1038, @1050, @1710.
Preceders: 34×3, 64×2, 11, 01, 88, 06. Followers: 65×3, 12, 56, 03, 20, 17, 29×1.

- "34 29 40" = "ière" ×3: @758 and @1038 are the byte-exact crib
  "11 70 82 34 29 40" = "la premiere" (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e);
  @62 is "12 41 08 34 29 40 12", same "ière" shape. In all three, 29-40 is the
  word-final "ere" unit.
- In 8 of 9 windows, 29-40 is followed by a non-29 cell. The single exception
  is our window @1050 (follower 29). "40 29" occurs exactly once in the stream
  (n(40)=21); "29 40 29" is a hapax (1/1847).

### 2. 40's word-final-'e' profile

In both crib windows 40 is definitively word-final "e" ("première" ends in "e";
followers 20 and 17="fois" are word-initial cells). Across n(40)=21, the only
follower that is a letter cell is 29, and only at @1051 (our window). 40's
profile is word-final-"e"-capable and never word-initial-"e" under banked
values in any resolved window.

### 3. The trigram forces the boundary (byte proof)

Pairs @1050-1052 are 29 40 29 = "er" + "e" + "er" (banked). Enumerating
boundary placements inside the trigram:

- Boundary @1050|@1051 → next word = "e"+"er"+[74]+[74] = "eer…".
  Period corpus (~34.5M chars): zero genuine French common words begin "eer".
  All 26 "eer*"-initial tokens are "Eernani"/"EERNANI" (proper noun, Verdi),
  "eerie" (English), "Eerwick" (proper noun), or Dutch/OCR fragments
  ("eeren", "eerbe", "eeregmad", "eerfd", "eertaines", "eere"). DEAD.
- No boundary → word contains "ereer" → no French license (§3). DEAD.
- Boundary @1051|@1052 → word1 ends "…e" (40 word-final, matching its
  profile and the "première" pattern), word2 = "er"+[74]+[74] = "er…".
  Corpus: "erreur" ×314, "erreurs" ×165, "errer" ×23 — genuine "er"-initial
  French words are common. VIABLE.

The boundary is therefore FORCED at @1051|@1052. This is Option B:
**[88 29 40] is one word ("[88]ere"); [29 74 74 …] begins a new word ("er…").**
Option A ('[88]er' + 'e…') is killed at kill grade — it forces an
"eer"-initial word, unattested in 34.5M characters of period French.

### Per-clause

- C1: PASS at battery grade. Segmentation resolved: [88 29 40] | [29 74 74].
  Option A killed (kill grade); Option B is the sole survivor, forced by the
  banked letter values and the trigram geometry. No new assumptions.
- C2 (fence arm): does not fire.

### Adverses

None listed on the target. Answered anyway: the "40 29" bigram's uniqueness
(1/21 forty-followers) is explained — it is the forced word-boundary locus,
not a 40-profile violation.

## Scope

- Segmentation only. 88's value is NOT named; 74's value is NOT named.
- Consistency note (not a claim): 88 is forced finite (verb class) by the
  @729–735 battery; "[88]ere" is consistent with finite present-tense shapes
  such as "préfère"/"adhère"/"suggère" (stem + "ère"). The "88-infinitive"
  naming the parent anticipated is constrained AGAINST at this window: 88
  cannot be "[88]er"-infinitive here; it is "[88]ere".
- The follower word "er"+[74]+[74] ("erreur"-family shape, "erreur" ×314 in
  corpus) is a candidate for future 74-value work; not named here.
- No standing or red-team verdict contradicted or downgraded; §7 intact;
  canonical-stream caveat stands. Per §4 (promote), no follow-ups required.

## Bookkeeping

- Stream: repaired 1,847-pair parse, re-derived in-session; asserts held.
- Report: `code/crowd17/report_inbox/battery-seg-88er-1049.md`
- Queue: `seg-88er-1049` → `status: verdict`, `result: promote`, 2026-10-09
  (pre-write assert passed — was queued/verdictless; temp-file + rename;
  disk re-read confirms verdict/promote; own entry only; no downgrade).
- Lock created on start, deleted on completion. R5005, sealed gates, red-team
  adjudication queue untouched.
