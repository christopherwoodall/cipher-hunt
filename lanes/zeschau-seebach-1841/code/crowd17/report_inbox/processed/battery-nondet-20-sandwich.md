# Battery verdict: nondet-20-sandwich

**Verdict: NULL** (all three non-det/adj arms fenced with stated cause).

## Target

- id: `nondet-20-sandwich` (priority 3)
- claim: "A non-determiner/adjective role for 20 — conjunction/preposition
  candidate or the one-word '61-20-61' re-segmentation with 20 word-internal —
  parses the @279-281 sandwich."
- evidence: battery-61-20-61-frame.md null follow-up #2
- adverses: (a) the one-word re-segmentation needs phonotactic evidence;
  (b) the near-miss 'chaque premier [noun]' reading would need 2+ ungranted
  assumptions (clause boundary inside the sandwich plus bare-determiner clause
  start); (c) do not duplicate the queued poly-20-docket (the 20 paradox venue).

## Bar (verbatim from battery-queue.json)

"Test non-det/adj roles for 20 at @279-281 — conjunction/preposition
candidates and the one-word '61-20-61' re-segmentation (20 word-internal)
against French phonotactics. Coordinate with queued poly-20-docket; do not
duplicate it."

## Numbered pass/fail clauses (pre-registered before testing — bar not modified after data)

1. **C1 (conjunction):** PASS iff a French conjunction value for 20 yields a
   grammatical parse of the sandwich under standing values plus the adopted
   parent premises (61 = "premier" at window level on both flanks).
2. **C2 (preposition):** PASS iff a French preposition value for 20 yields a
   grammatical parse under the same premises.
3. **C3 (one-word):** PASS iff "61-20-61" re-segmented as one word with 20
   word-internal survives French phonotactics with named spellings for 61
   and 20.

Verdict rule: **promote** iff >=1 clause passes with all adverses answered;
**kill** iff all three fail at kill grade; **null** otherwise, with 1–3
follow-ups.

## Method

Read BATTERY-PROTOCOL.md first. Created
`code/crowd17/next-token/locks/nondet-20-sandwich.lock` on start (agent id +
2026-10-09T10:46:00Z); no stale lock present. Re-derived the repaired
1,847-pair / 96-type stream in-session from
`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`
(byte-exact tokenization, asserts held). `canonical.py` never used. R5005,
sealed gates, and the red-team adjudication queue untouched. Standing values
held fixed per §7.

Adopted from the parent battery `61-20-61-frame` (NULL, not re-litigated):
61 = "premier" at window level on both flanks ("le premier" left via
37 = 'le' S5 MEDIUM; "premier [noun]" right via 42 = noun-class); det/adj
is structurally excluded at the sandwich. poly-20-docket (queued P1)
remains the 20-paradox venue — no ruling on 20's global class/value here.

## Window-level evidence (all byte-verified on the repaired stream)

### Locus

1-based @280–282 = `61 20 61`, row a2_03 (offset 1), mid-row. The
"61-20-61" trigram occurs exactly **1×** stream-wide; "61 20" and "20 61"
bigrams 1× each (this window only). Flanks:

`... @278=91 @279=37('le' S5 MEDIUM) | @280=61 @281=20 @282=61 |
@283=42(noun-class) @284=48('e' letter) @285=52 ...`

i.e. "[91] le premier | [20] | premier [noun] e ...".

## Per-clause results

### C1 — conjunction: FAIL (fence, stated cause)

- Under the adopted premise, the geometry is "le premier [20-CONJ]
  premier [noun]". Left conjunct is a complete NP ("le premier"); the right
  conjunct ("premier [noun]") lacks the parallel determiner. Coordinated
  NPs in French require parallel determiners — "le premier et premier
  [noun]" is ungrammatical for every coordinator (et, ou, ni, mais, car,
  or, donc). No French subordinator composes an NP-antecedent + bare-NP
  clause here either.
- Fence, not kill: the whole argument is conditional on the window-level
  61 = "premier" extension, which the parent battery left flank-supported
  but unproven at @280/@282. If 61 takes another value at the flanks, the
  conjunction geometry changes with it.

### C2 — preposition: FAIL (fence, stated cause)

- Under the same premise: "le premier [20-PREP] premier [noun]". The
  putative complement "premier [noun]" is a bare ordinal-headed NP; no
  French preposition takes such a complement in this position ("le
  premier de la classe" / "des [noun]" require the article). No
  preposition value yields a grammatical parse, and no licensed host
  exists for the PP.
- Fence, not kill: same window-level 61 caveat as C1. 20's value is open,
  so each candidate is hypothetical rather than forced-false.

### C3 — one-word "61-20-61" (20 word-internal): FAIL (untestable; fence)

- Phonotactics needs spellings. 61's only spelling is the locus-level
  "premier" at @1556 (val-61-premier PROMOTE); the global 61-value KILL
  (val-61-contact) stands, so no global 61 spelling exists. 20 has no
  letter value at any grade (20 = "fois" is kill-grade dead; no other
  spelling stands).
- The adverse's demand for phonotactic evidence therefore cannot be met
  at standing grade — the arm is untestable, not refuted. Fence.

**Verdict: NULL.** No standing verdict contradicted or downgraded; §7
intact. The sandwich stays fenced as a 20-value residual; the det/adj
exclusion (parent) and the non-det/adj exclusion (this battery) jointly
leave the slot value-open pending the red-team paradox venue.

## Adverses answered

- (a) Phonotactic evidence: demanded and searched — none available at
  standing grade (no 61/20 global spellings); stated as the C3 fence
  cause, not ignored.
- (b) "chaque premier [noun]" near-miss: belongs to the parent's det/adj
  route, not this bar; acknowledged as fenced (2+ ungranted assumptions),
  not re-tested here.
- (c) poly-20-docket: coordinated, not duplicated — this battery tests
  only the three named arms at the sandwich and makes no ruling on 20's
  global class or value.

## Follow-ups proposed (all verified ABSENT from battery-queue.json;
premier-61-flank-census already queued — noted, not re-proposed)

1. `conj-prep-20-wide` (P3) — test conjunction/preposition roles for 20
   across its full 15-window profile (@281/@308/@491/@643/@669/@704/
   @742/@761/@840/@874/@959/@1136/@1225/@1271/@1704). A role forced at
   >=2 independent windows revives the sandwich arms.
2. `val-20-lettertier` (P3) — name 20's letter value (candidate lead: @761
   "34 29 40 20" = "iere[20]" adjacency); unblocks the one-word
   phonotactic test permanently.
3. `sandwich-61premier-rerun-gated` (P4) — re-run this bar once 61 =
   "premier" is window-confirmed at @280/@282 (e.g. via
   premier-61-flank-census); a proven "premier" converts the C1/C2
   fences into kills.

## Bookkeeping

- `battery-queue.json`: `nondet-20-sandwich` queued → verdict/null
  (temp-file + rename, own entry only, pre-write assert confirmed no
  prior verdict, JSON re-validated).
- Lock created on start, deleted on completion. No standing/red-team
  verdict contradicted or downgraded. R5005, sealed gates, red-team queue
  untouched.
