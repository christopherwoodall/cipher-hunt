# Battery verdict: ne-follower-verbless-sweep

## Bar (verbatim from battery-queue.json)

"if @509 is the sole verb-less 'ne', the residual stands alone; if a verb-less
family exists, re-frame the @508 window inside it"

Claim: "classify all 37 94-windows by verb presence; @509's verb-less status is
or isn't unique"
Adverses: none.
Evidence: lon-94-64-rightedge null (2026-10-08): full 94-follower census
(82 x4, 74 x3, 59 x3, 52 x3, 92/24/76/79 x2, 16 singletons incl. 64).

## Numbered clauses

1. C1: Classify all 37 94-windows by verb presence on the repaired stream.
2. C2: Decide whether @509 is the SOLE verb-less 'ne'.
   - If sole: the residual stands alone (report as isolate).
   - If a verb-less family exists: re-frame the @508 window inside it.

## Method

- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
  `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`).
  `canonical.py` never touched. R5005, sealed gates, red-team queue untouched.
- 94 windows re-derived: 37, at
  @65 @101 @161 @250 @318 @349 @494 @509 @558 @570 @578 @651 @688 @699 @762 @771
  @774 @785 @841 @1102 @1169 @1182 @1293 @1330 @1353 @1363 @1549 @1576 @1664
  @1687 @1701 @1705 @1713 @1742 @1773 @1795 @1806. Matches the ne-ce-1169 census.
- Verb-class set V = {24, 31, 32, 33, 86, 88}, registry-grounded
  (`code/table-grid/table-registry.json`: 24=verb, 31=VERBAL, 32=verb, 33=INF,
  86=INF, 88=gov). 85 has no registry cell (A3 frame grant only) — excluded from
  primary, sensitivity-checked.
- Three definitions of "verb presence" (sensitivity ladder):
  - D1 (distributional, clitic span): verb-class group in forward +1..+5.
  - D2 (tight): verb-class group in forward +1..+2.
  - D3 (grammatical, attachable): nearest forward verb-class group within +1..+8
    with no granted non-clitic intervener. Blocker set =
    {87,47,46,64,96,17,79,00,84,59} (granted/promoted word-level groups that can
    never be preverbal clitics in 1841 French). 11='la' and 77='le'(prov)
    deliberately EXCLUDED from blockers — both can be preverbal object clitics
    ("ne la voit"). Sensitivity: re-running with 11/77 as blockers changes no
    window's assignment (neither is ever the sole intervener before a verb).
- 94='ne' STRONG LEAD (R17-001) is the assumed particle; the test is whether
  each window can host it.

## Window-level evidence

### D1 census (verb in +1..+5): 14 verb-present / 23 verb-less

Verb-present: @65 @161 @494 @509 @651 @762 @771 @774 @841 @1330 @1576 @1701
@1705 @1773. Verb-less: the other 23. @509 IS verb-present under D1 (88 at +4).

### D2 census (verb in +1..+2): 4 verb-present / 33 verb-less

Verb-present only at @161 (24@+1), @774 (33@+2), @1705 (88@+1), @1773 (24@+1).
@509 verb-less under D2 — but one of 33, not unique.

### D3 census (attachable verb, +1..+8, no non-clitic intervener): 9 / 28

Attachable (particle-'ne' viable):
- @65  verb 24@+4 [92 69 13]
- @161 verb 24@+1 []
- @651 verb 24@+3 [76 49]
- @771 verb 33@+5 [07 06 94 15]  (caveat: second 94 intervenes at +3)
- @774 verb 33@+2 [15]
- @1330 verb 86@+5 [70 52 39 83]
- @1701 verb 88@+5 [30 20 62 94]  (caveat: second 94 intervenes at +4)
- @1705 verb 88@+1 []
- @1773 verb 24@+1 []

Un-attachable: 28, INCLUDING @509. @509's interveners: 64 98 65; 64='qui'
(granted) blocks — 'qui' can never intervene between "ne" and its verb.

### Span-robustness

Verb-less counts by forward span: +2: 33 | +5: 23 | +8: 21 | +12: 16.
The family is not a span artifact: 16/37 windows have NO verb-class group
within +12 forward positions (@101 @318 @349 @570 @578 @688 @699 @785 @1102
@1182 @1293 @1353 @1549 @1664 @1713 @1742 @1795 @1806).

### The @508 window (re-frame target)

@508 [a3_00] 62; @509 [a3_00] 94. Window ±6:
"39 68 21 67 77 62 94 64 98 65 88 56 87".
- Left profile: 62-94. The 62-94 bigram is x9 on the stream
  (@101 @509 @762 @841 @1330 @1363 @1687 @1705 @1773); 62 is the modal preceder
  of verb-less 94s. @509's left context MATCHES the family profile.
- Right profile: 94-64 is a stream-unique bigram (64 follows 94 only here).
  64='qui' granted → particle-'ne' attachment fails at kill grade for this
  window: no 1841 construction places "ne" directly before "qui".
- Family precedents for non-particle 94: 70-12-94 "prenne" word-internal
  (@348, fenced); 61-94 word-final "ne" candidate (@578 verb-less, @1169 —
  cf. ne-ce-1169 rescue-(1)); 12-94 x3 (@65 @349 @1549, R17-018 duality).

## Per-clause pass/fail

- C1 (classify all 37): PASS — full census under three definitions, all
  @-offsets re-derived on the repaired stream.
- C2-sole (is @509 the sole verb-less 'ne'?): FAIL — refuted under every
  definition. D1: @509 not verb-less (14 verb-present). D2: @509 verb-less
  but one of 33. D3: @509 un-attachable, one of 28. Span ladder: 33/23/21/16.
  The "sole" branch is dead; the residual does NOT stand alone.
- C2-family (verb-less family exists → re-frame @508): PASS — family
  demonstrated at battery grade (28/37 un-attachable; robust to span and to
  blocker-set choice). Re-frame performed:
  the @508 window is re-framed as a member of the 28-member un-attachable
  94-family. Particle-'ne' fails at this window (64='qui' blocker at +1; nearest
  verb-class 88@+4 un-attachable). Its left profile (62-94) is the family's
  modal pattern. The 94 here is re-segmented as a NON-PARTICLE candidate —
  62-94 word-final "ne" syllable, or a distinct 94 value per the R17-018
  duality — consistent with the family's profile and with ne-ce-1169's
  rescue-(1) (61-94 word-final "ne"). No second 94 value is DECLARED here
  (§7: red-team declaration required); the re-frame is a segmentation
  hypothesis, not a value claim.

## Standing verdicts

- R17-001 (94='ne' STRONG LEAD): UNTOUCHED. 9/37 windows host attachable
  particle-'ne', including clean "94 24" frames (@161 @1773) and "94 88"
  (@1705). The lead stands; its DOMAIN is narrowed, not its value.
- No standing verdict contradicted or downgraded. No red-team fence crossed.

## Verdict: PROMOTE

The bar's conditional is decided at battery grade: the verb-less family exists
(28/37 un-attachable under the grammatical definition; 23/37 verb-less at
clitic span; robust across span ladder and blocker-set sensitivity), @509 is
not the sole verb-less 'ne' under any registry-grounded definition, and the
@508 window is re-framed inside the family as a non-particle re-segmentation
candidate with the specific blocker (64='qui') and family precedents named.
No adverses were listed; none ignored.

## Optional next steps (not required for this verdict)

- `seg-62-94-wordfinal` (P2): test 62-94 x9 as word-final "ne" syllable
  (paradigm: 70-12-94 "prenne", 61-94 candidate).
- `ne-attachable-paradigm` (P3): the 9 attachable windows as the clean
  particle-'ne' paradigm — use as positive controls for future 94 batteries.
- Note for red team: if the un-attachable family's 94s resolve as syllabic,
  R17-018 (12/94 duality) may need widening to a 94 positional split; NOT
  declared here.
