# Battery report: seg-94-82-06 (NULL — fenced, no uniform parse at <=1 assumption)

**Target:** seg-94-82-06 — the '94-82-06' trigram left edge resolves (ne+ment vs alternatives)
**Worker:** eab0a1e1-f252-4bd9-ab80-d9adafd803e2 | **Date:** 2026-10-08
**Stream:** repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py; 1,847 pairs verified). Never canonical.py. No R5005 touched. No sealed gates touched. No data invented. Every @-offset re-derived from the stream.

## Bar (verbatim from battery-queue.json)

> parse '94-82-06' x4 (@579/@737/@1183/@1356) under standing values; name the segmentation iff one parse covers all four with <=1 ungranted assumption, else fence with stated cause

## Bar as numbered clauses (pre-registered before testing)

1. The repaired stream contains the bar's four frames: 94-82-06 at the stated positions, in the repaired 1,847-pair parse.
2. Under standing values only — 94="ne" (R17-001 STRONG LEAD; value never overturned, re-segmentation only), 82="m" (banked), 06="ent" iff pre=82 (F61 conditioned LEAD) — one segmentation places the trigram's left word-edge uniformly across all four frames with <=1 ungranted assumption. (An "ungranted assumption" = any value, edge rule, or frame reading not granted in protocol §7 or a red-team-adjudicated finding.)
3. The named segmentation is "ne+ment" ([94]|[82-06]) iff it — and no rival — satisfies clause 2; rivals ([94-82]|[06], [94]|[82]|[06], word-internal "…nement", elision "ne m'ent…") are excluded or fenced with stated cause.
4. Adverses answered: 94="ne" is retained in every candidate parse; no standing red-team verdict (F61 06-islet, F72 H4g refutation, F66 per-frame fences, R17-001) is contradicted or downgraded.

## Method

1. Reparsed the repaired stream byte-exactly per repair_parse.py (1,847 pairs; asserts hold: 1,847 pairs, 96 distinct groups).
2. Exact-match census: "94-82-06" trigram x3 at 0-based 578, 1182, 1353; variant "18-82-06" x1 at 0-based 736; "94-82-06-06" 4-gram x2 at 578, 1182; "06-06" doubling stream-wide x2 (at 580, 1184 — exactly the two 4-gram frames); 82→06 census (0-based position of the 06) = [580, 738, 1184, 1355], matching F72's archived census exactly.
3. Tested the uniform left-edge segmentation "[X]|[82-06]" (X∈{94,18}) and all rival edge placements against the four frames under standing values only.

## Window-level evidence (0-based pair indices; bar @-offsets are 1-based/finder convention)

Standing gloss key: 94=ne (R17-001 lead), 82=m (banked), 06=ent* (* = iff pre=82, F61 conditioned LEAD), 64=qui (granted), 00=pour (A9), 59=est? (provisional), 77=le? (provisional).

**Frame A — bar @579 = pair 578 [a3_02]:** `61 [94 82 06] 06 50`
Full: `94 52 87 78 45 13 55 61 [94 82 06] 06 50 10 19 18 14 00 97`
→ "…61 ne m ent ent [50]…" — "ne|ment…" with the word after "ment" unidentified ("mentent [50]" re-uses the F72-REFUTED 4-gram; "ment"+"ent…" needs 50's role = ungranted). F66 by-ear: fenced admissible.

**Frame B — bar @737 = pair 736 [a5_02] (variant, lacks 94 — noted in F2):** `76 [18 82 06] 00 36`
Full: `86 48 88 11 24 85 93 76 [18 82 06] 00 36 20 30 67 77 81`
→ "…76 [18] m ent pour(00) [36]…" — left slot is 18, not 94; 18's value unknown = ungranted. F66 by-ear: fenced. (X variable {94,18} ⇒ X is a separate word ⇒ supports a word edge after X, but does not name the "ne+ment" parse.)

**Frame C — bar @1183 = pair 1182 [a6_10]:** `78 [94 82 06] 06 59`
Full: `36 74 32 48 59 37 77 78 [94 82 06] 06 59 42 06 84 59 46`
→ "…78 ne m ent ent est?(59)…" — "ne mentent/entendent est" is ungrammatical with 59="est"-as-word (F66 ADVERSE fenced). Rescue needs a local 59 re-read (59 is only provisional) = ungranted and ad hoc.

**Frame D — bar @1356 = pair 1353 = the 94 (the 52 sits at 1356) [a7_05]:** `78 [94 82 06] 52 37`
Full: `86 66 73 34 62 48 77 78 [94 82 06] 52 37 64 35 13 92 62 94 79`
→ "…78 ne m ent [52] [37] qui(64)…" — "ne ment pas" parses CLEAN: 52="pas" is bounded to negation frames (F31/F33) and this is a negation frame; 0 ungranted assumptions at trigram level. F66 by-ear: clean. (The "[37] qui" right-frame oddity belongs to the 52-37 unit, owned elsewhere — not this battery.)

## Per-clause pass/fail

1. **Frames exist — PASS WITH NOTE.** All four frames verified; @737 is the 18-variant (no 94, as F2 recorded); @1356 indexes the 52 of frame D (trigram 94 at 1353). 82→06 census [580,738,1184,1355] reproduces F72 exactly.
2. **One parse covers all four with <=1 ungranted assumption — FAIL.** Best candidate "[X]|[82-06]" ("ne|ment…"): D clean (0 ungranted); A needs 50's role (ungranted #1, and the "mentent" word-ID is F72-refuted); C needs a local 59 re-read (ungranted #2); B needs 18's value (ungranted #3). ≥2 ungranted assumptions > 1. No other parse does better (see clause 3).
3. **"ne+ment" named — FENCED, NOT NAMED.** It is the best-supported single segmentation (D clean, A admissible, consistent with the F61 islet and F66's era preference over "gouvernement"), but it fails clause 2's ≤1-assumption bar, so per the bar's own "else" branch it is fenced with stated cause. Rivals: [94-82]|[06] "nem|ent", [94]|[82]|[06] "ne|m|ent", single-word "nement" — EXCLUDED (non-lexical; "m" is not a standalone French word). Word-internal "…ne-ment" ("gouvernement"/"-nement" family) — FENCED by standing red-team adjudication: F66's triple collision put 06-islet "ne ment pas" (era-good) against "gouvernement pas" (era-0 in 40 tokens) and the islet won; naming it here would contradict F66. Elision "ne m'ent…" — FENCED: the doubled-06 frames need "entendent" = en-tend-ent ≠ ent-ent; fails A and C.
4. **Adverses answered — PASS.** 94="ne" retained in every candidate parse (re-segmentation only, never overturned). F61 (06-islet), F72 (H4g refutation), F66 (per-frame fences), R17-001: none contradicted, none downgraded.

## Verdict

**NULL.** No single left-edge segmentation covers all four frames within the ≤1-ungranted-assumption bar. The leading parse "[X]|[82-06]" ("ne|ment…", X∈{94,18}) is clean at frame D ("ne ment pas"), admissible at A, adverse-but-fenced at C (provisional-59 collision), and fenced at B (18 unknown) — that is 2+ ungranted assumptions, so the segmentation is fenced with stated cause, not named. No standing verdict contradicted; R5005, sealed gates, and the red-team queue untouched.

## Follow-up targets for the supervisor queue (null regeneration)

**F1. id: "seg-94-82-06-f1" | priority: 2**
claim: "59 at 0-based 1186 (frame C) reads 'est'-as-word vs a bisyllabic verb-unit; decides whether 'ne mentent/entendent'+59 parses"
bars: "parse '94-82-06-06-59' @1182 under the F61 islet (06='ent' iff pre=82); name 59's local value iff one reading parses the frame grammatically with <=1 ungranted assumption"
evidence: "seg-94-82-06 null (2026-10-08): frame C 'ne mentent/entendent est' ungrammatical under 59='est'-as-word (F66 ADVERSE fenced); 59 is only provisional"
adverses: "F72 H4g refutation stands — do not re-declare the 4-gram a unit; test 59's local value only"

**F2. id: "seg-94-82-06-f2" | priority: 2**
claim: "18 occupies 94's left slot ('18-82-06' vs '94-82-06'); slot-equivalence discriminates word-edge-after-X"
bars: "census 18 (neighbors, rate); 18 fills 94's slot iff its distribution matches 94's left-of-82 slot with <=1 ungranted assumption; name 18's value iff slot-equivalence and a gloss parse both hold"
evidence: "seg-94-82-06 null (2026-10-08): variant frame '18-82-06-00' @736; X variable {94,18} implies X is a separate word, supporting a word edge after X"
adverses: "00='pour' granted (A9) — the 'ment pour' right frame must be honored"

**F3. id: "seg-94-82-06-f3" | priority: 3**
claim: "the second 06 in '06-06' @580/@1184 has a value ('ent ent' vs new word 'ent…'); it sits outside the F61 islet, which covers only 82→06"
bars: "test 'ent ent' (two-word) vs new-word 'ent…' readings of the second 06 at both doublings; decide iff <=1 ungranted assumption"
evidence: "seg-94-82-06 null (2026-10-08): 06-06 doubling occurs only at islet positions (580, 1184); the second 06 is not covered by F61"
adverses: "F72 refuted H4g's p_comb — do not re-run that statistic; the F61 islet itself is unchanged"

---
Lock: locks/seg-94-82-06.lock created 2026-10-09T02:48:38Z, deleted on completion of this report. No R5005 touched. No sealed gates touched. No promotions made. No red-team verdicts modified or downgraded.
