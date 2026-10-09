# Battery report: imp-80-bare-1156-1596

- Target id: `imp-80-bare-1156-1596`
- Claim: test the two bare-verb imperative candidates @1156 ('[92]er [80] fois') and @1596 ('[03]er [80] et le') with independent clause-boundary evidence; promote either to the imperative set iff the boundary is byte-grounded, else fence.
- Date: 2026-10-09
- Worker: battery worker (subagent 712d01e7-0c6a-41c4-9f91-d1b5c406d83d)
- Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed like `code/side-keyhunt/repair_parse.py`); re-derived in-session: **1,847 pairs, 96 types**. `canonical.py` never used. R5005, sealed gates, red-team queue untouched.

Terms (ASD-STE100): "enclitic diagnostic" = the '80-77' bigram ("[80]-le"), where the object pronoun 77='le' (provisional) attaches after the verb — a shape only an imperative form takes. "Bare-verb candidate" = an 80 window with no enclitic, whose imperative reading depends on a clause boundary before or after it. "Byte-grounded boundary" = a boundary provable from the stream bytes themselves (row break at the locus, gloss anchor, byte-identical bounded formula) — not from an assumed unmarked punctuation point.

## Bar (verbatim, pre-registered before testing)

"test the two bare-verb imperative candidates (@1156 '[92]er [80] fois', @1596 '[03]er [80] et le') with independent clause-boundary evidence; promote either to the imperative set iff the boundary is byte-grounded, else fence"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** @1156 ('[92]er [80] fois') joins the imperative set iff a clause boundary licensing the imperative is byte-grounded; else it is fenced with stated cause.
2. **C2:** @1596 ('[03]er [80] et le') joins the imperative set iff a clause boundary licensing the imperative is byte-grounded; else it is fenced with stated cause.
3. **C3:** the listed adverse is answered: the ungranted clause-boundary assumption (no punctuation survives in the cipher), and the enclitic imperative set stays at n=2 on byte count.

## Parentage

Follow-up of the NULL `imp-80-set` (2026-10-09): its enclitic diagnostic ('80-77' = "[80]-le") returned exactly n=2 (@720/@1032) and it recorded @1156/@1596/@1322 as imperative-consistent only under an ungranted boundary assumption. This battery tests whether either of the two named candidates can clear that assumption on byte evidence.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/imp-80-bare-1156-1596.lock` on start (agent id + 2026-10-09T10:32:22Z); no prior lock existed; deleted on completion.
2. Re-derived the repaired stream byte-exact in-session (1,847 pairs / 96 types confirmed against imp-80-set's census).
3. Enumerated the only byte-level boundary classes available in the cipher: (a) manuscript row breaks, (b) the two pencil-gloss anchors (rows a5_03, a8_05), (c) byte-identical formula twins that could anchor a boundary from a bounded occurrence, (d) row-break-adjacent 80 positions stream-wide.
4. Tested each locus against (a)–(d); adopted imp-80-set's follower inventory and enclitic count as premise (not re-litigated).

## Window-level evidence

### @1156 (row a6_09) — `66 84 02 00 [ROW a6_08→a6_09] 92 29 80 17 77 82 44 83`

- n(92)=22; the 4-group formula '92 29 80 17' occurs exactly **1x stream-wide** — singleton, no twin to anchor a boundary from.
- The one manuscript row break in the ±10 window falls between 00 and 92, i.e. **before the "[92]er" infinitive, not before 80**. It cannot license an imperative at 80 (the break would open a clause starting "[92]er", leaving 80 mid-clause).
- Neither pencil-gloss row is a6_08/a6_09 — no gloss anchor.
- The a6_08/a6_09 row offsets are unvalidated (68 of 70 upstream row offsets unvalidated per §7 canonicality caveat), so even this row break is phase-fragile and cannot ground a clause claim at battery grade.
- Rival readings live but untested here: 80 as finite verb continuing the "pour [92]er …" clause (00='pour' granted A9), or 80 as determiner before temporal "fois" (red-team venue: poly-80-docket).

### @1596 (row a8_02) — `70 64 65 48 29 47 08 81 03 29 80 67 77 81 82 98`

- The 4-group formula '03 29 80 67' occurs exactly **1x stream-wide** — singleton.
- **Zero row breaks** anywhere in the ±10 window (entirely on row a8_02).
- Neither pencil-gloss row is a8_02 — no gloss anchor.
- 67 resolves to 'et' by the positional rule (follower 77='le' is not infinitive-shaped, per §7), so the surface after 80 is "et le [81] …". An imperative reading needs a clause boundary between 80 and "et" — unmarked, ungrounded.
- Note: @1032's enclitic member shares the left shape "[03]er [80]" but has the enclitic diagnostic ('80-77'); @1596's follower is 67, not 77, so the diagnostic does not extend.

### Stream-wide boundary census

- **0 of 17** stream-wide 80s sits immediately after a manuscript row break. There is no row-positional signature of bare-verb imperatives anywhere in the stream.
- Full follower inventory re-verified: {50, 06, 09, 97, 03, 77 x2, 10, 78, 17, 04, 08, 67, 22} — '80-77' x2 only, @720 (`02 21 80 77`) and @1032 (`03 29 80 77`). **The enclitic imperative set stays at n=2** on byte count (adverse confirmed, not extended).

## Per-clause pass/fail

1. **C1 (@1156): FAIL → fence.** The only byte-level boundary in range is the a6_08|a6_09 row break before 92, not before 80; it is on unvalidated rows; no gloss anchor; the formula is a singleton. No byte-grounded boundary licenses the imperative. Fenced with stated cause: imperative-consistent only under the ungranted boundary assumption (adverse, unanswered).
2. **C2 (@1596): FAIL → fence.** No row break, no gloss anchor, singleton formula, and the follower is 67 ('et'), not the enclitic 77. No byte-grounded boundary licenses the imperative. Fenced with stated cause (same).
3. **C3 (adverse): ANSWERED.** The ungranted boundary assumption is not ignored — it is the stated cause of both fences. The enclitic set remains at exactly n=2 (@720, @1032); no third member is byte-licensable. imp-80-set's n=2 ceiling is confirmed, not contradicted.

## Verdict: NULL

Both candidates fenced, neither killed: the windows force nothing false about an imperative 80 (the readings stay imperative-consistent), but nothing in the bytes grounds the required boundary. Per §4 (zero is an absence, not a refutation). No standing or red-team verdict contradicted or downgraded; §7 intact (no polyvalence declared); canonical-stream caveat stated. This verdict does not touch `poly-80-docket` (queued P1) or `infsub-80-frame` — those remain the venues for 80's non-imperative roles.

## Follow-ups proposed (all verified absent from battery-queue.json)

1. `imp-80-finite-rival-1156-1596` (P3) — test the finite-verb rival readings at @1156/@1596 ("…pour [92]er … [80]" / "[03]er … [80]" as finite verbs continuing the prior clause); bar: promote iff subject + agreement license parses with zero ungranted assumptions.
2. `det-80-1156-1011` (P3) — test the determiner/quantifier reading of 80 at @1156 ("[80] fois") and @1011 ("tout [80]"); bar: parse iff "… fois" is a licensed temporal-NP tail; feed to queued `poly-80-docket`.
3. `rowbound-clause-calibration` (P4) — calibrate the base rate at which manuscript row breaks coincide with provable clause boundaries (gloss-anchored rows + pencil cribs); bar: state the coincidence rate with counts, so future boundary claims carry a measured prior instead of an assumed one.
