# Battery report: qui37-rival-values

- Worker: subagent 4e5deadd-2375-4991-b746-752232625f67
- Lock created: 2026-10-09T00:57:19Z (no prior lock present; no stale lock)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py).
  canonical.py was NOT used. R5005 NOT touched. No data invented.

## Bar (verbatim, pre-registered)

"rank rival values for 37 in the three 'qui 37' verb frames against the
A8/A3 verb-frame grammar; state consequences for the value race without
deciding the A1 grant"

## Bar restated as numbered pass/fail clauses (fixed before testing)

- Clause 1: The three 'qui 37' frames (@676, @939, @1633) are re-derived on
  the repaired 1,847-pair stream with full local windows.
- Clause 2: The A8/A3 verb-frame diagnostics are stated from the standing
  grants and applied to 37, calibrated against the finite-verb control 67.
- Clause 3: Each rival value {finite verb, verb-stem, adjective, 'le', noun}
  is tested per-frame for grammaticality and globally against the
  diagnostics, producing one ranking.
- Clause 4: Consequences for the value race are stated without deciding the
  A1 grant and without declaring polyvalence (protocol §7).
- Clause 5: Adverses fenced — A1 predicative-frame grant untouched
  (red-team's); A12 37-01 unit untouched; R5005, sealed gates, and the
  red-team adjudication queue untouched.

## Method

1. Reparsed the repaired stream byte-exactly per repair_parse.py (1,847
   pairs). Located all 64-37 bigrams: exactly 3, at 0-based 675/938/1632
   (= 1-based @676/@939/@1633), matching the queue evidence.
2. Stated the A8/A3 verb-frame grammar from the standing red-team grants:
   - A8 (80/89 verb-frames): 29→X high (80: 4/17, 89: 5/14, the "er [verb]"
     infinitive context), 24→X (80: 2/17, 89: 3/14), 87-77→X (1 each,
     "ce le [verb]"), 79→X (80: 3/17, "tout [verb]").
   - A3 (85 verb-stem): 24→X ×5 ("en [stem]"), "que [stem]er" ×2; stem
     class {33,86}: X→29 = 9/57 ("[stem]er").
3. Computed 37's contact profile (n=28) on the same diagnostics and ran
   Fisher depletion tests vs the granted classes, with 67 ("veut"/"et",
   the sole true polyvalence, a finite verb) as the finite-verb control.
4. Tested each rival value for grammaticality in each of the three frames
   using only banked/promoted/provisional anchors (64=qui promoted;
   77='le' provisional; 84='on', 96='par' promoted).

## Window-level evidence

### The three frames (re-derived, 1-based @ = 0-based + 1)

- F1 @676: `... 86 24 80 03 [64 37] 77 45 23 09 07 00 ...`
  = "[03] qui 37 le(77, prov) 45 23 ..."
- F2 @939: `... 00 33 21 [64 37] 01 07 50 40 08 62 ...`
  = "33-21 qui 37-01 07 ..." (A12 37-01 unit; "21-64-37-01" 4-gram)
- F3 @1633: `... 00 33 21 [64 37] 01 74 87 74 74 35 ...`
  = "33-21 qui 37-01 74 ..." (byte-identical 4-gram to F2)

### 37's profile against the A8/A3 diagnostics

| token | n | X→29 (stem) | 29→X (frame) | 24→X ("en") | 87-77→X | 64→X |
|---|---|---|---|---|---|---|
| 37 | 28 | 0 | 1 | 2 | 0 | 3 |
| 33 | 25 | 5 | 0 | 0 | 0 | 0 |
| 86 | 32 | 4 | 0 | 0 | 0 | 0 |
| 80 | 17 | 0 | 4 | 2 | 1 | 0 |
| 89 | 14 | 0 | 5 | 3 | 1 | 0 |
| 85 | 15 | 0 | 3 | 5 | 0 | 0 |
| 67 (finite-verb control) | 38 | 0 | 2 | 0 | 0 | 0 |

- Stem diagnostic (X→29): 37 = 0/28 vs {33,86} = 9/57. Fisher depletion
  p = 0.0219 — 37 is NOT a verb-stem at the lane's distributional standard.
  Calibration: finite-verb 67 shows the same depletion (0/38, p = 0.0077).
  The diagnostic kills stem-hood, not verb-hood.
- Frame diagnostic (29→X): 37 = 1/28 vs {80,89} = 9/31. Fisher depletion
  p = 0.0097 — 37 is not a verb-frame token of the 80/89 class either.
- "en [X]" (24→X): 37 = 2/28 (@312, @475, both "84-24-37-78" = "on [24]
  [37] 78", 84='on' granted) — not enriched vs 85 (5/15); weak.
- "ce le [X]" (87-77→37): 0. "tout [37]" (79→37): 1 (@51).
- Net: the A8/A3 grammar operationalizes stem/infinitive verb-hood. 37
  fails both diagnostics exactly the way the finite-verb control 67 does.
  The grammar is the wrong instrument for "qui 37" — it can exclude the
  stem reading but cannot confirm or kill finite-verb-hood.

### Per-frame grammatical tests

F1 @676 "03 qui 37 le(77, prov) 45":
- Finite verb: "…[03]. Qui [V] le [45-N]" — grammatical (relative clause,
  transitive verb + article-noun object). Only grammatical reading under
  standing values. Conditional on 45 nominal (45 open: 'ce' HOLD / 'dict'
  rival) and 03 closing the prior clause (03 open, stem-03 queued).
- 'le': "qui le le 45" — ungrammatical (provisional-77-dependent).
- Adjective: "qui [adj] le 45" — ungrammatical (no 'est').
- Noun: "qui [noun] le 45" — ungrammatical.
- Order: verb > 'le' (contradicted) > adjective/noun (ungrammatical).

F2 @939 / F3 @1633 "33-21 qui 37-01 X" (byte-identical 4-gram ×2):
- Finite verb: "qui [V] [01]" — grammatical CONDITIONAL on 01 taking a
  post-verbal value. 01's value is open ('ci'/'faisant' KILLED by
  ci-01-value). Not contradicted; unresolved.
- 'le': 37 is sub-unit of the A12-granted 37-01 collocation; standalone
  'le' unavailable here.
- Adjective: "qui [adj]-01" — ungrammatical.
- A12-unit interaction (fenced, not decided): if 37-01's value were
  "certain" (adjective — A12 notes compatibility only, never proof),
  "qui certain" is ungrammatical. So either 37 is verb-shaped with 01
  separate, or the 37-01 unit is verb-shaped. The 'certain' compatibility
  is in TENSION with the qui frames — stated as consequence C2, A12
  untouched.
- Order: verb (conditional) > 'le' (blocked) > adjective/noun
  (ungrammatical).

### Conditional pro-verb leg outside the qui frames

24-37 ×2, both "84-24-37-78" (@312, @475): 84='on' granted. IF 24='en',
the frame reads "on en [V] 78" — 'en' selects a verb, so 37 would be
verb-shaped here too. Conditional on 24's open value; stated as such, not
as proof.

## Ranking (global, against the A8/A3 verb-frame grammar)

1. **Finite verb** — the only rival that parses grammatically in all three
   qui frames; profile matches the finite-verb control 67 on both A8/A3
   diagnostics (depleted exactly like 67, not like stems/frames).
2. **Adjective** — ungrammatical in the qui frames (no 'est'), but live
   elsewhere: A1's predicative frame (under red-team re-adjudication per
   frame-37-reexam) and la-finder's "la 52-37-43" ×2. The live rival; the
   polyvalence pressure point (see C1).
3. **'le' (S5)** — contradicted in F1 ("qui le le", provisional-dependent),
   blocked in F2/F3 by the A12 unit; s5-foundation's five clean
   banked/promoted-anchored contradictions stand. The S5 fence itself is
   red-team's; this battery does not overturn it.
4. **Verb-stem** — distributionally excluded: 37→29 = 0/28 vs {33,86} =
   9/57, Fisher depletion p = 0.0219 (kill grade at the lane's standard).
5. **Noun** — no legs; ungrammatical after 'qui' in all three frames.

## Consequences for the value race (A1 NOT decided)

- C1 (polyvalence pressure): if A1's predicative value for 37 survives
  red-team re-adjudication AND 37 is verb-shaped in the qui frames, that
  is two values for 37 — a second polyvalence, which only the red team
  can declare (§7: 67 is the sole true polyvalence; battery never declares
  a second). This battery states the pressure; it does not resolve it.
- C2 (A12 tension): F2/F3 put the A12 37-01 unit's 'certain' compatibility
  in tension with grammatical French ("qui certain" is ungrammatical).
  Either 37 is a verb with 01 separate (01's value open), or the 37-01
  unit is verb-shaped. A12 (unit, not value) stands untouched; the value
  question is flagged, not decided.
- C3 (instrument limit): the A8/A3 grammar tests stem/infinitive
  verb-hood. It excludes 37-as-stem (p = 0.0219) but is blind to
  finite-verb-hood (67 calibrates: 0/38 post-29). Future verb tests for 37
  need finite-verb diagnostics (complement frames, e.g. F2/F3's 01 slot;
  subject-agreement contexts), not more A8/A3 stem checks.
- C4: the "on [24] [37] 78" ×2 frames (@312/@475) are a conditional
  pro-verb leg, gated on 24's open value.

## Per-clause pass/fail

- Clause 1: PASS — all three frames re-derived on the repaired stream
  (@676/@939/@1633), full windows given.
- Clause 2: PASS — A8/A3 diagnostics stated from standing grants, applied
  to 37 with Fisher tests and the 67 finite-verb control.
- Clause 3: PASS — five rivals tested per-frame and globally; one ranking
  produced (verb > adjective > 'le' > stem > noun).
- Clause 4: PASS — four consequences stated (C1–C4); A1 not decided; no
  polyvalence declared; no value named or granted.
- Clause 5: PASS — A1 untouched (red-team escalation stands);
  A12 37-01 unit untouched (tension flagged only); R5005, sealed gates,
  red-team queue untouched.

## Verdict: promote

**The ranking is promoted as battery-decided.** This promotes the RANKING
only — no value for 37 is named, granted, or promoted; the A1
predicative-frame grant is not decided (red-team re-adjudication stands);
no second polyvalence is declared (§7). All bar clauses pass and both
adverses are fenced with stated cause (A1 deferred to red team; A12 unit
grant untouched).
