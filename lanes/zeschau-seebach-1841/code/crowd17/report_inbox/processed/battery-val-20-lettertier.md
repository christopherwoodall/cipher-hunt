# Battery verdict: val-20-lettertier

**Verdict: NULL** (fence executed per the bar's else-arm — letter-tier naming under-powered, not refuted).

## Target

- id: `val-20-lettertier` (priority 3)
- claim: "name 20 letter value (candidate lead: @761 '34 29 40 20' = 'iere[20]' adjacency); unblocks the one-word phonotactic test permanently"
- evidence: battery-nondet-20-sandwich.md NULL 2026-10-09, follow-up 2
- adverses: none listed.

## Bar (verbatim from battery-queue.json, pre-registered before testing)

"name iff >=2 independent letter-tier legs; else fence"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1 (name):** PASS iff >=2 independent windows license 20 as a letter composing word-internally with letter-valued neighbors into a licensed French spelling, converging on ONE named letter value.
2. **C2 (else-arm):** if C1 fails → fence the letter-tier naming question with stated cause.

## Method

Read BATTERY-PROTOCOL.md first. Created
`code/crowd17/next-token/locks/val-20-lettertier.lock` on start (agent id +
2026-10-09T18:51:23Z); no stale lock present. Re-derived the repaired stream
in-session from `data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json`, parsed per
`code/side-keyhunt/repair_parse.py`: **1,847 pairs / 96 types**, asserts held;
20 census n=15 (0-based @280 @307 @490 @642 @668 @703 @741 @760 @839 @873
@958 @1135 @1224 @1270 @1703). `canonical.py` never used. R5005, sealed gate
instances, red-team adjudication queue untouched.

Adopted, never re-litigated: banked pencil (11=la, 70=pre, 82=m, 34=i,
29=er, 40=e, 46=que); granted 17=fois, 79=tout, 00=pour, 84=on; provisional
59=est, 77=le; letter-tier grants 12="n", 48="e" (R20-008), 08="t" battery;
kills 20="fois"; split 20~17; gloss (i) "la premiere" over 11 70 82 34 29 40
(R5005 repair; 40 = word-final 'e', gloss-anchored); 20 = post-nominal
adjective @642 (subj-20-642 PROMOTE); 48 = word-internal 'e' of "[89]e" @641
(conj-20-642-subordinator C1); 20 heads the right clause @760 under two
battery-grade clause-initial roles (boundary-760-20role KILL); 20 = relative
adverb 'où' @1703 (reladv-20-1703 precedent); particle face 'mais' @839
(particle-20-760-839); poly-20-docket FENCED (R20-126, confirm R19-036);
§7 intact (no polyvalence declared).

Terms (ASD-STE100): "letter tier" = a cipher number that writes one letter
inside a word. "letter-tier leg" = a window where 20 composes word-internally
with letter-valued neighbors into a licensed French spelling. "fence" = the
route is suspended with a stated cause, not killed. "battery grade" = the
evidence standard of this pipeline.

## Window-level evidence (exhaustive letter-tier adjacency inventory)

All 15 windows tested against standing letter-tier neighbors
(12="n", 48="e", 40="e", 34="i", 82="m"). Letter-tier adjacency exists at
exactly 4 loci:

### Lead leg: @760 — "34 29 40 | 20" = "iere[20]" — DEAD (two independent kills)

- Byte-verified: `... 11 70 82 34 29 40 | 20 62 94 59 ...` (row a5_03).
- Kill 1: gloss (i) anchors 40 as the word-final 'e' of "premiere"; no
  French word continues "premiere"+letter ("premieres" would break the
  gloss's singular "la"; "ierez"/"ieret"/"ierex" are not French words).
- Kill 2: boundary-760-20role KILL (battery grade) — 20 heads the right
  clause here under the particle face and the relative-adverb face; a
  letter-tier 20 contradicts that standing verdict and is not re-litigated.
- The lead that motivated this target is dead.

### @703 — "98 20 12" = "vient [20]n" — LIVE but weak (the sole surviving leg)

- Byte-verified: `60 12 98 | 20 12 66 21` (row a5_01).
- 12="n" granted letter tier (R20-008). Composition "20 12" = [20]+'n'
  yields licensed French words only for 20='u' ("un") or 20='e' ("en"):
  "vient un [66]" (66 noun-class confirmed) or "vient en [place]"
  (66 value open). All other letters ("an"/"on"/"in") are ungrammatical here.
- **Non-unique:** the window does not discriminate 'u' from 'e'; 66's value
  is open, so both parses survive. One leg, no name.

### "48 20" ×2 (@642, @873) — DEAD (standing-verdict contradiction)

- "48 20" = 'e'+[20]: "en" (20='n') / "es" / "et" / "ex" all re-parseable in
  principle, but @642 carries two standing battery verdicts: 20 =
  post-nominal adjective (subj-20-642 PROMOTE) and 48 = word-internal 'e'
  of the closed NP "[89]e" (conj-20-642-subordinator C1). A letter-tier 20
  contradicts both; @873 is the fenced twin. Per §5 these cannot count as
  clean legs. "et" would additionally collide with 67="et" under §7.

### "40 20" ×1 — identical to the @760 lead leg. DEAD (see above).

### All other windows — no letter-tier adjacency at all

- @280 "61 20 61": no spellings for 61/20 (already fenced by
  nondet-20-sandwich C3 — the phonotactic test this target was meant to unblock).
- @307 "88 20 17": 17="fois" word-level; 20 cannot supply a letter to a group.
- @490/@668/@741/@958/@1135/@1224/@1270: 20 sits between word-level groups
  (67=et/veut, 00=pour, 30=pas, 64=qui) or unvalued groups — letter-tier
  composition is geometrically impossible (a single letter cannot stand alone
  as a word, and no French word is letter+word-boundary here).
- @839: particle face 'mais' stands (battery grade). @1703: relative-adverb
  'où' precedent stands. Letter-tier contradicts both.

## Per-clause results

- **C1 — FAIL.** Exactly one live letter-tier leg (@703 "20 12" = "un"/"en"),
  and it does not uniquely name a letter ('u' vs 'e' both parse). The bar
  needs ≥2 independent legs converging on one value.
- **C2 — FIRES (fence).** The letter-tier naming question is fenced with
  stated cause: (a) the motivating lead (@760 "iere[20]") is dead on two
  independent grounds; (b) the sole surviving leg (@703) is weak and
  non-discriminating; (c) 11 of 15 windows admit no letter-tier geometry at
  all; (d) the two "48 20" loci are blocked by standing battery verdicts.
  Fence, not kill: if 66's value lands (place vs count noun), @703's leg
  upgrades to a discriminator; if 61's value lands, @280 re-opens as a
  second leg. Consequence: the one-word phonotactic test for "61-20-61"
  (nondet-20-sandwich C3) stays blocked — 20 has no spelling at any grade.

## Scope

Fences only the letter-tier VALUE-naming question. Untouched: 20's word-level
faces (particle 'mais' @760/@839, relative adverb 'où' @1703/@760,
post-nominal adjective @642), the 20~17 split, the 20="fois" kill,
poly-20-docket's FENCE (R20-126), and §7 (no polyvalence declared — a
letter-tier 20 alongside word-level 20 faces would be a class split and is
red-team venue, not declared here). No standing or red-team verdict
contradicted or downgraded. Canonical-stream caveat stands (row a5_01/a5_03
offsets unvalidated).

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `val-20-703-66` (P3) — name 66's value at @705; a place licenses
   20='e' ("vient en [place]"), a count noun licenses 20='u'
   ("vient un [noun]"). Arms the sole surviving leg toward a discriminator.
2. `letter-20-sandwich-revisit` (P4) — re-test the letter-tier question once
   61's value lands; a 61 spelling unblocks @280 as the second independent leg.
3. `un-20-12-census` (P4) — census all "X 12" bigrams stream-wide to test
   whether "20 12" patterns with word-level "un"/"en" behavior or is a
   letter-tier coincidence.

## Bookkeeping

- Queue: `val-20-lettertier` queued → `verdict`/`null`, 2026-10-09
  (pre-write assert passed — was queued/verdictless; temp-file + rename;
  JSON re-validated; own entry only; no downgrade).
- Lock `code/crowd17/next-token/locks/val-20-lettertier.lock` created on start,
  deleted on completion (verified gone).
- R5005, sealed gates, red-team adjudication queue untouched.
