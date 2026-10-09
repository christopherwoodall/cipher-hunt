# Battery report: `val-52-630-frame` — verdict: PROMOTE

**Target:** `val-52-630-frame` (Seebach lane next-token pipeline battery worker)
**Date:** 2026-10-09
**Stream:** repaired 1,847-pair / 96-type parse re-derived in-session (asserts held:
1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed gates, and the
red-team adjudication queue untouched.

## Bar (verbatim, pre-registered)

> "class named with >=2 frame-legs at battery grade"

**Numbered clauses:**
- C1: Name 52's class as it bears on the @630 frame ("et 08 52"), supported by
  ≥2 independent frame-legs at battery grade (byte-exact windows parsed under
  standing values only, zero new assumptions).
- C2: Every listed adverse is answered (re-parsed cleanly, fenced with stated
  cause, or shown to be a misread — not ignored).

## Method

Re-derived the repaired stream from `data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json` (same tokenization as
`repair_parse.py`). Full census of 52 (n=27) and 08 (n=18) with ±4 context.
Standing values used: 67="et" (granted; positional rule keeps "et" here since
08 is not infinitive-shaped), 70="pre" (pencil GT), 11="la" (GT), 64="qui"
(granted), 94="ne" (strong lead, cited only as background), 08="t"
(battery-grade PROMOTE, `battery-val-08-letter-census`, stated as conditional
premise with independent corroboration).

## Findings

### The @630 locus (byte-verified)

Row a4_01: `@628=87 @629=78 @630=67 @631=08 @632=52 @633=67 @634=63 @635=74
@636=46`, i.e. `ce [78] et 08 52 et [63] [74] que …`.

The claim's fork: (Arm A) verb-shaped 52 → "et 08 [52-V]" with standalone 08 as
subject; (Arm B) non-verbal 52 → 08–52 composition re-opens.

### Frame-leg 1 — @630: "et t 52 et" forces 52 sub-lexical (PASS)

08="t" is a bound letter, established on 4+ independent windows, all byte-exact:
- "40 08" = "et" at @921–922 (`74 40 08 65`) and @943–944 (`50 40 08 62`);
- "[41]tire" at @59–61 (`12 41 08 34`);
- "[37]tre" at @778–780 (`73 37 08 29`).

A letter "t" cannot stand alone as a clausal subject. Therefore at @631–632 the
"t" cannot be a standalone word, and "t52" is word-internal: 52 occupies the
letter/syllable tier here, composing a "t[52]…" word. A sub-lexical unit cannot
be a finite verb, so **Arm A ("et 08 [52-V]") is impossible at @630**.

The "08 52" bigram is a stream hapax (n=1), and the "et _ 52 et" frame
(`67 _ 52 67`) is likewise unique to @630–633 — the locus is not illuminated by
recurrence, but the letter-tier forcing is direct.

### Frame-leg 2 — @1332: "pre 52" confirms 52's sub-lexical tier independently (PASS)

Row a7_04/a7_05: `@1330=94 @1331=70 @1332=52 @1333=39`, i.e. `[94] pre 52 [39]`.
70="pre" is pencil ground truth and a bound prefix; unaccented "pre" is not a
French word, so "pre 52" must be word-internal ("pre[52]…"). This is a second,
fully independent window forcing 52 into sub-lexical composition — the tier is
live for 52, not an ad-hoc reading of @630.

### Distributional corroboration (independent of 08's value)

In all 18 of 08's windows, 08 is either word-internal (`[41]tire`, `[37]tre`,
`[60]t`, `[37]t`, `[80]t`, `[17]t`, `[ce]t` ×2, `[23]t`, `[85]t`, `[01]t`) or part
of the word "et" (`40 08` ×2). **08 is never a standalone word-sized unit
anywhere.** The "standalone 08" premise required by Arm A therefore has zero
distributional support even setting the "t" value aside.

### Per-clause ruling

- **C1 — PASS.** 52's class at @630 is named **non-verbal, sub-lexical
  (letter/syllable tier)**, with two independent battery-grade frame-legs
  (@630 "t52", @1332 "pre52").
- **C2 — PASS** (adverses answered below).

## Adverses answered

- **A1 — "qui 52" verb legs (@1342 `64 52 38`, @1435 `64 52 82`, n("64 52")=2).**
  Accepted as genuine: "qui" + 52 is most naturally a finite verb in both
  windows. This does NOT contradict the verdict — it shows 52 is **split-shaped
  across loci** (verb-tier in "qui __", sub-lexical at @630/@1332), exactly the
  non-uniformity pattern already established for 88 (`tout-88-frame`). Scope of
  this verdict is locus-level (@630), not global.
- **A2 — "ne 52 [INF]" adverb legs (@1294/@1807 `94 52 80 04`, n("94 52")=3)
  and "la 52" superlative legs (@1006/@1123/@1721 `11 52`, n("11 52")=3).**
  Accepted as genuine ("ne plus/jamais [INF]", "la plus [X]"). Same answer as
  A1: other loci, split-shaped 52, untouched by this verdict. The
  plus/jamais value tie stays fenced per `plus-jamais-tiebreak`.
- **A3 — 08="t" is battery-grade, not red-team ratified.** Stated as a
  conditional premise; the distributional corroboration (08 never standalone in
  18/18 windows) does not depend on the "t" value.
- **A4 — seg-52-80-unit / seg-52-86-unit KILLs.** These fence "52 80"/"52 86"
  as words; they do not touch the "08 52" bigram, which was never under those
  targets. Untouched.
- **A5 — "52 82" ×5 ("52 m").** Examined and set aside: at @1435 ("qui 52 m")
  the "m" most plausibly starts the following word under the verb reading, so
  "52 82" is not a clean sub-lexical leg. Not used.

## Scope

- KILLS the verb-shaped-52 hypothesis **at @630 only**: the "et 08 [52-V]"
  frame is dead (08 cannot be a subject).
- PROMOTES the live parse: **08–52 composition** — "et [t52-word] et [63] …",
  with 52 as the sub-lexical continuation of a "t…" word.
- Does NOT name 52's letter value, does NOT decide the "t52" word's identity,
  does NOT touch 52's verb tier ("qui 52") or adverb tier ("ne 52 [INF]",
  "la plus"), does NOT contradict any standing or red-team verdict. §7 intact
  (no new polyvalence declared; the split is positional, like 88).

## Verdict: PROMOTE

C1 and C2 pass. 52 is non-verbal (sub-lexical) at @630 with two battery-grade
frame-legs; the "et 08 [52-V]" verb frame is killed; 08–52 composition is the
live parse.

## Follow-ups (for supervisor; §4 proposes 1–3 on null — verdict is promote,
so these are optional forward leads, not required regeneration)

1. `word-t52-630-identify` (P3) — identify the "t[52]" word at @630–632 once
   52's letter value or 63's class constrains the "et X et Y" coordination;
   candidate shape "et tout et …" testable against the period corpus.
2. `split-52-redteam-input` (P2, gather-only) — package 52's locus-level tiers
   (verb "qui 52" ×2, adverb "ne 52 [INF]" ×2 + "la plus" ×3, sub-lexical
   "t52"/"pre52") as red-team input for a 52 split/non-uniformity docket item,
   mirroring the 88 treatment.

## Bookkeeping

- Lock: `code/crowd17/next-token/locks/val-52-630-frame.lock` created on start
  (agent a8367872-deb0-42e0-8d0a-4c6133c735c8, 2026-10-09T17:32:02Z), deleted on
  completion. No stale lock was present.
- Report: `code/crowd17/report_inbox/battery-val-52-630-frame.md` (this file).
- Queue: `val-52-630-frame` → `status: verdict`, `verdict.result: promote`,
  pre-write asserted queued/verdictless, temp-file + rename, own entry only,
  no downgrade. Disk re-validated after write.
