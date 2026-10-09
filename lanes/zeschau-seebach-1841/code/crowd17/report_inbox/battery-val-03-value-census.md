# Battery verdict: val-03-value-census

- Target: `val-03-value-census` (battery-queue.json, priority 3, status queued)
- Claim: census all 20 '03' windows for a uniform verb-stem value, lead with the '03 29'=Xer legs (@1030/@1320/@1594).
- Worker: 31b8138b-a2b1-4548-a41d-b3745ed1f10b. Date: 2026-10-09.
- Stream: repaired 1,847-pair / 96-type parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`). `canonical.py` NOT used. R5005, sealed gates, red-team adjudication queue untouched.
- All @-offsets are 0-based pair indices in the repaired stream. Asserts held: 1,847 pairs, 96 types.
- Lock: `code/crowd17/next-token/locks/val-03-value-census.lock` created on start (no stale lock present); deleted on completion.

## Bar (verbatim, pre-registered before testing)

"name 03's verb-stem value iff it holds across windows with zero kill-grade contradictions; else fence uniform-verb-03."

**Restated as numbered pass/fail clauses (frozen before testing):**
1. **C1 (name arm):** a single verb-stem value for 03 parses at all 20 windows with zero kill-grade contradictions — name it.
2. **C2 (fence arm):** otherwise, fence uniform-verb-03 (the claim that one verb-stem value covers all windows).
3. **C3 (adverses):** R20's deferral of the 03/71 §7 split is respected (no split decision); the '77 03' determiner frame at @722 is tested as stated.

## Standing values used (protocol §7)

Pencil GT: 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que. Granted: 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce. Provisional: 59=est, 77=le. Frames: A1 (37/32/42 predicative), A3 (85 verb-stem), A8 (80/89 verb-frames), A9 (00=pour), A15 (84=on).

**Load-bearing red-team standings for 03:**
- **R19-178 (GRANT-WITH-CORRECTIONS):** stem-03 promoted as verb-stem **conditioned to the "03 29" frame ×3** (@1030/@1320/@1594 0b). Registry: ["03","verb-stem","cls"], conditioned scope. Noun arm pending §7 split adjudication; global class = §7 split question, red-team venue.
- **R19-142 / R20-038:** the @1028–1031 window ("Ceci, [03]er!" reading) stays **FENCED** — "do not ratify for banked use"; a battery cannot lift a red-team fence.
- **R20 carry-forward:** 03/71 §7 splits **DEFERRED** — R19-178 stands on its own docket.
- **R20 (ne-W6-pas-verb REJECT):** finite-03 at the W6 "ne…pas" frame (@1367) rejected; W6 C1 does not re-open.

## Method

1. Read BATTERY-PROTOCOL.md in full before testing.
2. Re-derived the repaired stream in-session; byte-confirmed n(03)=20 and all windows with ±4 context.
3. Graded each window against a uniform verb-stem value under standing values only. A bare (uninflected) verb stem is ungrammatical in French; a stem needs inflection or a licensing frame.

## Findings — window-by-window census (n(03)=20)

Notation: K = kill-grade against uniform verb-stem (a window forces the claim false); F = fenced (unlicensable without new assumptions); L = leg.

| @ | row | window (±4) | grade | cause |
|---|---|---|---|---|
| 31 | a1_00 | 00 34 24 **30 03 64** 32 01 08 | **K** | bare 03 before granted "qui" (64); bare stem cannot head a relative |
| 336 | a2_05 | 45 54 88 40 **03 64** 31 14 45 | **K** | "e [03] qui" — bare stem between "e" (40 GT) and "qui" |
| 599 | a4_00 | 85 01 29 40 **03 39** 26 96 45 | F | bare 03, neighbors unvalued (39); no licensed stem parse |
| 657 | a4_02 | 49 24 26 **30 03 62** 16 00 86 | **K** | "pas [03]" — "ne pas" governs an infinitive word, not a bare stem |
| 664 | a4_02 | 00 86 50 **80 03 62** 06 00 20 | **K** | bare 03 adjacent to verb-frame 80 (A8); two verb elements, no license |
| 674 | a5_00 | 11 86 24 **80 03 64** 37 77 45 | **K** | bare 03 between verb-frame 80 and "qui" |
| 691 | a5_00 | 65 94 29 **60 03 39** 74 46 02 | F | bare 03, neighbors unvalued (60/39); no licensed stem parse |
| 722 | a5_02 | 02 21 80 **77 03 91** 65 64 11 | **K** | determiner "le" (77 provisional) + bare 03 — the adverse's frame |
| 886 | a5_08 | 31 79 68 **37 03 02** 00 86 06 | F | bare 03 after predicative 37, before unvalued 02; no license |
| 994 | a6_01 | 49 24 26 **30 03 60** 67 11 96 | **K** | "pas [03]" — same as @657 |
| 1014 | a6_02 | 79 80 78 **47 03 24** 41 15 66 | **K** | "ce [03]" — determiner (47 granted A4) + bare stem |
| 1030 | a6_03 | 96 43 87 01 **03 29** 80 77 11 | L* | "03 29" frame, BUT window FENCED at red-team level (R19-142/R20-038); cannot supply a naming leg |
| 1237 | a7_01 | 29 85 56 **10 03 40** 67 77 81 | F | bare 03 before "e" (40 GT); no standing stem+ending license for 03+40 |
| 1320 | a7_04 | 48 98 15 **24 03 29** 80 08 62 | L | "03 29" frame; 24=finite/modal class (R17-009) takes bare infinitives — genuine infinitive leg (R19-178 F1). Non-discriminating for VALUE: any -er stem fits identically |
| 1367 | a7_06 | 94 79 14 **60 03 30** 82 16 91 | **K** | W6 "ne…pas" frame; finite-03 here REJECTED at R20 — bare 03 as verb killed at red-team level |
| 1594 | a8_02 | 29 47 08 **81 03 29** 80 67 77 | L | "03 29" frame (R19-178 F3, conditional on nounfamily C2 + §7). Non-discriminating for VALUE |
| 1645 | a8_04 | 12 33 98 **60 03 64** 31 10 03 | **K** | bare 03 + "qui" |
| 1649 | a8_04 | **03 64** 31 10 03 38 82 16 01 | **K** | bare 03 + "qui" (second 03 at @1653 also bare) |
| 1675 | a8_05 | 55 81 92 **60 03 39** 74 77 44 | F | bare 03, neighbors unvalued (60/39); no license |
| 1790 | a8_09 | 96 21 68 **47 03 00** 86 56 42 | **K** | "ce [03] pour" — determiner (47) + bare stem |

**Tally: 12 kill-grade (K), 5 fenced (F), 3 "03 29" legs (L/L*).**

### Clause results

- **C1: FAIL.** No value can be named:
  (a) Uniformity is contradicted at kill grade at 12 of 20 windows — bare 03 before granted "qui" (×5: @31/@336/@674/@1645/@1649), after "pas" (×2: @657/@994), after determiners (×3: @722/@1014/@1790), adjacent to verb-frame 80 (×1: @664), and as rejected finite-03 at W6 (@1367).
  (b) Even within R19-178's conditioned "03 29" ×3 scope, no value is nameable: @1030's window is red-team-FENCED (R19-142/R20-038) and cannot supply a banked leg; @1320 and @1594 are genuine infinitive legs but accept any -er stem identically — naming one would be invention (§3 forbids).
  (c) R19-178 itself named no value (class-only grant). No subsequent battery or red-team round has named one.
- **C2: FIRES.** Uniform-verb-03 is fenced: the claim that one verb-stem value covers all 20 windows is dead at kill grade on standing values alone.
- **C3: PASS.** Adverses answered:
  - The 03/71 §7 split is untouched — this battery decides no split; the fence is consistent with R19-178's conditioned scope (verb-stem within "03 29" ×3) plus nounfamily's nominal arms elsewhere, and with R20's deferral.
  - The @722 '77 03' determiner frame was tested as stated and kills the uniform claim at kill grade there.

### Consistency check (protocol §5.2)

No standing red-team verdict is contradicted. R19-178's conditioned verb-stem grant (scope "03 29" ×3) stands untouched — this fence targets only the GLOBAL/UNIFORM claim, which R19-178 already scoped out ("global class = §7 split question, red-team venue"). The sibling batteries `val-03-noun` (NULL, 2026-10-09) and `seg-77-03-722` (NULL, 2026-10-09) are consistent: none names a 03 value; none contradicts this fence. §7 intact. Canonical-stream caveat stands.

## Verdict: NULL (fence executed)

The bar's name arm fails (no value nameable; uniformity kill-grade dead at 12 windows) and the fence arm fires. The fence confirms R19-178's conditioned scope rather than establishing new bankable content, so this is recorded as a null with the fence as the finding — not a promote. No registry change requested. No red-team act requested beyond the docket input below.

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `stem-03-value-discriminator` (P3) — the @1320/@1594 "03 29" legs are genuine but value-nondiscriminating; test whether 24's finite/modal subclass selection at @1320 or a future 81 value at @1594 constrains the stem. Bar: name the stem value iff an independent standing constraint picks exactly one -er stem with zero new assumptions; else fence value-naming at these legs.
2. `noun-03-seven-windows` (P3) — the counterpart of this fence: nounfamily's forced-nominal windows (@336/@674/@1645/@1014/@1790/@722 per val-03-noun). Bar: name 03's noun value iff one lexeme parses all six with zero kill-grade contradictions; else fence uniform-noun-03. (Note: val-03-noun NULL 2026-10-09 killed its singleton candidate; this re-opens with a fresh inventory.)
3. `split-03-redteam-feed` (P2, gather-only) — package this uniform-fence (12 kill-grade windows documented) as red-team input for the deferred 03/71 §7 split docket. Evidence package only; batteries do not decide splits.

## Bookkeeping

- `battery-queue.json`: `val-03-value-census` queued → verdict/null (temp-file + rename, own entry only; pre-write assert confirmed queued/verdictless; JSON re-validated from disk; no downgrade; no existing verdict overwritten).
- Report: `code/crowd17/report_inbox/battery-val-03-value-census.md` (this file).
- Lock `locks/val-03-value-census.lock`: created on start, deleted on completion.
- R5005, sealed gates, red-team adjudication queue untouched.
