# Battery report: faire-complement-field

- Target id: `faire-complement-field`
- Claim: census 'faire' complements stream-wide ('faire [03]er' x1, 'faire [80]' x2, 'faire [85]' x5, 'faire ce' x10): build the semantic field of 24's infinitive objects to narrow 03's stem
- Date: 2026-10-09
- Worker: battery worker (subagent 4c23e675)
- Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` +
  `code/side-keyhunt/repaired_offsets.json`, parsed like
  `code/side-keyhunt/repair_parse.py`; n=1847 asserted, 96 groups asserted).
  All @-offsets are 0-based repaired-stream indices. `canonical.py` never used.
  R5005, sealed gates, red-team adjudication queue untouched.
- Lock: `code/crowd17/next-token/locks/faire-complement-field.lock`
  (created at start, deleted on completion).

## Bar (verbatim, pre-registered BEFORE testing)

"census 'faire' complements stream-wide ('faire [03]er' x1, 'faire [80]' x2,
'faire [85]' x5, 'faire ce' x10): build the semantic field of 24's infinitive
objects to narrow 03's stem."

Numbered pass/fail clauses (restated before testing, not modified after):

1. The census of 24's complement windows confirms the brief's counts
   ('faire [03]er' x1, 'faire [80]' x2, 'faire [85]' x5, 'faire ce' x10)
   and extends them to a full 24-successor census.
2. The semantic field of 24's infinitive objects is built from the census:
   complement classes named with their windows.
3. 03's stem is tested against the field: the field either narrows 03's
   stem to a named class or is recorded as a non-narrowing with the
   limitation stated.
4. Adverses answered: causation compatibility with every -er verb above;
   no monovalent candidate covers 03's full profile (imp-80-set).

## Method

1. Re-derived the repaired stream in-session (1,847 pairs, 96 types).
2. Enumerated all n(24)=52 windows with ±8 context; full successor census.
3. Classified complements against standing values/grants (protocol §7):
   24 = finite verb, modal-shaped, infinitive-taking (ne-24-profile,
   battery-PROMOTE, class-level — value 'faire' NOT banked); 87='ce'
   granted; 30='pas' battery-promote; 29='er' banked GT; 80/89
   verb-frames (A8, value open); 85 verb-stem (A3, value open).
4. Phase-checked the @1319 '24 03 29' trigram under a7_04's rival offset.

## Census: n(24) = 52, successors byte-exact

| follower | n | windows (0-based @) |
|---|---|---|
| 87 ('ce') | 10 | 73, 162, 179, 190, 643, 823, 829, 1486, 1766, 1774 |
| 85 (verb stem, A3) | 5 | 732, 955, 1438, 1693, 1754 |
| 82 ('m' banked letter) | 4 | 165, 535, 1193, 1830 |
| 30 ('pas') | 3 | 29, 1268, 1728 |
| 89 (A8 verb-frame) | 3 | 221, 985, 1497 |
| 37 (predicative frame) | 2 | 311, 474 |
| 80 (A8 verb-frame) | 2 | 564, 672 |
| 26 | 2 | 654, 991 |
| 41 | 2 | 807, 1015 |
| 65 | 2 | 811, 1382 |
| 49 | 2 | 859, 917 |
| 48 (-e inflection) | 2 | 1220, 1657 |
| 03 | 1 | 1319 |
| 88 | 1 | 41 |
| 56 | 1 | 69 |
| 47 | 1 | 547 |
| 42 | 1 | 783 |
| 24 | 1 | 806 |
| 06 | 1 | 966 |
| 02 | 1 | 1083 |
| 77 | 1 | 1132 |
| 11 | 1 | 1522 |
| 74 | 1 | 1567 |
| 53 | 1 | 1580 |
| 00 | 1 | 1492 |

The brief's counts are confirmed exactly: 'faire [03]er' x1 (@1319),
'faire [80]' x2 (@564, @672), 'faire [85]' x5 (@732/@955/@1438/@1693/
@1754), 'faire ce' x10 (@73–@1774 list).

## The semantic field of 24's infinitive objects

**Infinitival class (24 as causative-modal governor):**
- 24→85 x5 (verb stem, A3): the dominant infinitival complement —
  "faire [85]" ×5 with 85's value open.
- 24→89 x3 (A8 infinitive-verb-frame): "24 89 48" @985 pairs with 48;
  @221/@1497 bare.
- 24→80 x2 (A8 verb-frame): @564 "24 80 97", @672 "24 80 03".
- 24→03+29 x1 (@1319): the ONLY 29-explicit infinitive in the set —
  "…vient(98) [15] [24] [03]er [80]…" (a7_04). Lane precedent: this
  window is the gapping-kill for 24's governor candidates
  (stem48-65-governor), and it is the sole locus of the imp-80-set's
  infinitive arm for 03.
- 24→88 x1 (@41), 24→56 x1 (@69): 88 verb class, 56 whole-word
  (noun/verb alternation) — verb-frame-compatible, open values.

**Non-infinitival classes:**
- 24→87='ce' x10: the largest complement class — "faire ce…"
  (ce-que relatives etc.).
- 24→30 x3: "24 pas" — bare-pas negation (ne-drop precedent).
- 24→82 x4: "24 m'…".
- 24→48 x2 (@1220 "24 48 30", @1657 "24 48 47"): 48 = inflectional -e;
  no clean infinitive-object parse — fenced, not infinitival.
- Residue (open classes): 24→{37×2, 26×2, 41×2, 65×2, 49×2, 42, 24,
  06, 02, 77, 11, 74, 53, 47, 00}.

## Per-clause pass/fail

1. PASS — brief's counts confirmed byte-exact on the re-derived stream;
   extended to the full 52-window census.
2. PASS — field built above: infinitival (85×5, 89×3, 80×2, 03er×1,
   88/56 frame-compatible) vs ce-object ×10 vs pas ×3 vs clitic ×4
   vs fenced 48×2 vs open residue.
3. PASS as a graded narrowing (see result below): 03's infinitive is
   the unique 29-explicit complement in the set; the field narrows
   03's stem to "causative-complement -er infinitive" and no further.
4. PASS — adverses answered (see below).

## Result: graded narrowing, honestly thin

- The field **confirms** 03's membership in 24's governed-infinitive
  class: @1319 is the only window in the stream where an explicit
  29-marked infinitive sits as 24's complement, and it carries 03.
- The field **cannot discriminate among -er verbs**: every sibling
  infinitival complement (85×5, 89×3, 80×2) is value-open at every
  tier. Causation is compatible with every -er verb above, exactly as
  the adverse states. No monovalent candidate covers 03's full profile
  (imp-80-set); the complement field adds the causative-governor slot
  as one more constraint, not a value.
- The one distinctive signal: 03+29 is the sole 29-explicit infinitive
  in the set. If the sibling stems (85/80/89) ever name values, the
  "bare-stem vs 29-explicit" distinction becomes a discriminator for
  03's stem value. Until then the field is a confirmed-membership
  census, not a value test.

## Adverses answered

(a) "Causation is compatible with every -er verb above" — CONFIRMED
by the census: the 24-governed infinitival class has four occupants
(03er, 85, 80, 89), three of them value-open stems/frames, and nothing
in the field excludes any -er verb from the 03 slot. (b) "no
monovalent candidate covers 03's full profile (imp-80-set)" —
CONFIRMED: this target narrows via the complement field only; the
imp-80-set arms (noun loci, stem loci, infinitive loci) are owned by
stem-03-nounfamily and val-03-noun, not re-litigated here.

## Load-bearing caveats (stated, not hidden)

1. The entire field is **conditional on 24 = modal/verb-class**
   (ne-24-profile). The 24-en-verb-conflict adjudication is queued;
   if the red team resolves 24='en', this complement reading
   dissolves with it.
2. @1319's '24 03 29' trigram is **phase-fragile**: row a7_04 is
   55 digits; under its rival offset-1 the trigram dissolves (verified
   in-session). The census holds on the canonical stream per protocol.
3. 24='faire' is NOT a promoted value — the governor is read as the
   causative-modal class; the 'faire' label is the brief's shorthand.

## Verdict: PROMOTE (census/record grade)

The census bar is complete (counts confirmed, field built, narrowing
graded per the adverse's own terms). No standing or red-team verdict
contradicted or downgraded; §7 intact. No follow-ups required — this
is a completed census, not a null; the value question stays with the
already-queued 03 threads (stem-03-nounfamily, val-03-noun,
val-21-reopen).
