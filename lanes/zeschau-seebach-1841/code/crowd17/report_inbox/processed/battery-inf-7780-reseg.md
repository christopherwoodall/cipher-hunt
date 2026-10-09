# Battery report: inf-7780-reseg

- Target id: `inf-7780-reseg`
- Claim: test the re-segmentation "87 | 77 [80/89-inf]" = "ce" + "le [inf]" (infinitive phrase "to V it").
- Date: 2026-10-09
- Worker: battery worker (subagent 55ff292b-a81c-46bd-b81e-d6e6f4979d10)
- Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; asserts held: 1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed gate instances, red-team adjudication queue untouched.

Terms (ASD-STE100): "re-segmentation" = a new word-boundary decision over the same digit groups. "Proclitic" = a short word that attaches to the left of a verb ("le" = "it", the object of the verb).

## Bar (verbatim from the brief)

"(1) test the re-segmentation under standing values; (2) promote iff it parses with zero new assumptions; (3) fence with stated cause if undecidable."

Numbered pass/fail clauses (restated before testing, not modified after):

1. C1: the re-segmentation "87 | 77 [80/89-inf]" is tested at both loci under standing values.
2. C2: PROMOTE iff the re-segmentation parses at both loci with zero new assumptions.
3. C3: else FENCE with stated cause (or KILL if a window forces the claim false at kill grade).

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/inf-7780-reseg.lock` on start (agent id + 2026-10-09T10:53Z); no stale lock; deleted on completion.
2. Re-derived the repaired stream in-session. Census: "87 77" occurs exactly **2x** stream-wide — @515 (row a3_00, follower 80) and @869 (row a5_07, follower 89). Byte-confirmed:
   - @515: `…507=77 508=62 509=94 510=64 511=98 512=65 513=88 514=56 | 515=87 516=77 517=80 | 518=09 519=70 520=91 521=77 522=06`
   - @869: `…861=74 862=74 863=48 864=47 865=46 866=00 867=86 868=70 | 869=87 870=77 871=89 | 872=48 873=20 874=74 875=49 876=16`
3. Standing values held fixed per §7: 87="ce" (granted), 77="le" (provisional), 80/89 = A8 verb-frame (value open, not specifically infinitive), 29="er", 46="que", 00="pour", 47="ce", 11="la".

## C1: window-level test (PASS — tested)

The re-segmentation reads both loci as "ce(87) | le(77) [80/89-inf]" = "ce" + the infinitive phrase "le [infinitive]" ("to V it", with "le" as the infinitive's object clitic).

Window A @515: "…qui(64) vient(98) [65-N] [88] [56] | ce | le [80-inf] | [09] [70]…"
Window B @869: "…ce(47) que(46) pour(00) [86-inf] pre(70) | ce | le [89-inf] | [48] [20]…"

## C2: promote test (FAIL — one load-bearing new assumption required)

The re-segmentation's crux is **80/89 as infinitive**. That reading is NOT a standing value:

- The A8 grant gives 80/89 a verb-frame grant only; the class is value-open.
- `inf-80-89-ratify` (2026-10-09) returned **NULL**: its trigger ("iff 24=modal ratified") is unmet — 24="faire" was REJECTED at R18-008 and demoted to a conditional lead, and 24=finite-verb (R17-009) is a class grant, not a ratified "24=modal" premise. The infinitive-slot legs for 80/89 are therefore unratified at battery grade.
- The only battery-grade 80 reading is imperative via the '80-77' enclitic diagnostic (imp-80-set, n=2: @720, @1032); imp-80-bare-1156-1596 fenced the bare-imperative candidates. `infsub-80-frame` KILLed the infinitive-subject reading at 3/4 windows. No standing verdict licenses 80/89 as infinitive.
- Assuming "80/89 = infinitive" is therefore a **new assumption** — and a contested one, squarely in red-team venue (`poly-80-docket` queued P1, `inf-80-89-ratify-rerun-gated` pending).

Under finite-verb or imperative 80/89, "ce le [80/89]" does not parse: "ce" + "le" + finite verb ("ce le fait"-shaped) is ungrammatical — "ce" cannot head a finite clause without "est"/"c'est". So the re-segmentation parses ONLY under the new infinitive assumption. C2's zero-new-assumption gate fails.

Not kill-grade: since the infinitive reading is open (red-team venue, not dead), no window forces the re-segmentation false. The claim is untestable at battery grade, not refuted.

## C3: fence (EXECUTED — stated cause)

The re-segmentation is **fenced** at battery grade because its crux (80/89 = infinitive) is red-team venue. Supporting facts:

- The "87 77" bigram is exactly 2x stream-wide with divergent followers (80 vs 89) — zero repetition leverage for a uniform reading; 77's successor profile (n=44: 78×7, 84×7, 86×5, 81×4, 76×3, 44×2, 89×2, 82×2, 80×1, …) shows no infinitival-signature dominance.
- The "87 77" = "celle" fusion alternative is dead at both windows: ce-le-verb-frame (battery grade) requires "celle" to be followed by a relative (64/46); here the followers are 80/89. Adopted, not re-litigated.
- Neither locus has a licensed host for a floating "ce le [inf]" phrase: at @515 the left clause "qui vient [65] [88] [56]" does not license a following topic+infinitive; at @869 the "pour [86] pre" governor leaves "ce" unattached. Even with the infinitive assumption, clause integration needs further unstated assumptions.

No standing/red-team verdict contradicted or downgraded; §7 intact; canonical-stream caveat stands (rows a3_00/a5_07 offsets unvalidated).

## Verdict: NULL

## Follow-ups proposed (nulls regenerate work; all verified absent from battery-queue.json)

1. `inf-7780-rerun-gated` (P4) — gated re-run of this bar once the red team adjudicates 80/89's infinitive class (venue: poly-80-docket / inf-80-89-ratify-rerun-gated).
2. `celle-7780-fusion-515-869` (P3) — window-scoped test of the "87 77" = "celle" fusion at @515/@869 against the relative-requirement (expected dead; confirm at these loci).
3. `window-515-fullparse` (P3) — full-context parse of @507–522 independent of the re-segmentation; decide whether "87 77 80" must attach left or right.

## Bookkeeping

- Queue: `inf-7780-reseg` → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock created on start, deleted on completion (verified gone).
