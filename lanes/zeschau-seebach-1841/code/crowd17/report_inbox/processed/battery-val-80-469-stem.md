# Battery verdict: val-80-469-stem

- Target: `val-80-469-stem` (battery-queue.json, priority 3, status queued)
- Claim: Name 80's value at the "[80]ent" 3pl windows (@469/@1090), where promoted 06='ent' gives the tightest morphological constraint on 80 (3pl stem). A named stem constrains 80's value globally and feeds the @1322 transfer question.

## Bar (verbatim)

"name the stem with <=1 ungranted assumption; a named stem constrains 80's value globally and feeds the @1322 transfer question"

## Bar, numbered

- C1. Name 80's stem at @469/@1090 with ≤1 ungranted assumption.
- C2. The named stem constrains 80's value globally and feeds the @1322 transfer question (moot unless C1 passes).

## Method

1. Read BATTERY-PROTOCOL.md first. Created `locks/val-80-469-stem.lock` on start (agent 50837115-9e76-4fb5-8ab8-ba5b295180c3, 2026-10-09T20:30:00Z); deleted on completion.
2. Re-derived the repaired stream in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt` via `repair_parse.py`: 1,847 pairs, 96 types. `canonical.py` never used.
3. Byte-confirmed the loci: 0-based @469 = "00 33 79 80 06 67 46" (row a2_10) and @1090 = "00 33 79 80 06 43 07" (row a6_05). The "80 06" bigram is exactly 2× stream-wide, both in the frame "00(pour) 33(?) 79(tout) [80] 06(ent)".
4. Rendered 80's full 17-window profile. Standing values used: 00='pour' (A9, leg-1 class-level), 79='tout' (A5), 06='ent' (promoted), 67='et' (sole true polyvalence; positional rule reads 'et' before finite-shaped 46='que'...46=que pencil GT).
5. Tested stem-naming against French 3pl morphology and the val-03-value-census precedent (parsing ≠ naming).

## Findings

### C1 — name the stem: FAIL

Under the bar's frame, "79(tout) [80] 06(ent)" reads as a 3pl finite verb with stem = 80's letter content ("tout [stem]ent"). Candidate French 3pl verbs fitting "[X]ent": sont, font, vont, viennent, disent, prennent, mettent, donnent, veulent, doivent, peuvent, savent, croient, voient, restent, semblent, tiennent, paraissent — twenty-plus lexemes, and the frame supplies **zero selectional pressure** beyond 3pl:

- No agreement controller at either window: @469's left edge is "00 33" ("pour [33]", 33 open); @1090's is identical. Nothing at either window distinguishes one 3pl stem from another.
- No object or complement: @469 continues "67(et) 46(que) 84(on) 24(verb-class)" — a clause restart; @1090 continues "43(open) 07(open) 55(open) 81(open)" — all open values. No selectional leg.
- Tested whether "tout" itself constrains the field: it does not narrow to one lexeme — any 3pl verb accepts a subject.

Every candidate parses identically at both windows. Naming any one would be arbitrary. Per the standing val-03-value-census precedent (parsing ≠ naming), C1 fails at battery grade: **fence value-naming at these legs** (evidentiary fence, not kill — no window forces a specific stem false).

### Adverse / frame tension (recorded, not litigated)

A secondary observation surfaced during testing and is recorded for the red team without battery adjudication: 79='tout' is a singular indefinite pronoun in the standing gloss; a 3pl "-ent" verb after bare "tout" is morphologically tense. This does not select a stem either — it bears on whether the "tout [80]ent" = 3pl frame is itself licensed, a question for `subj-80-469-1090` (proposed below) or the corpus. No §7 declaration, no frame kill: the bar asked only for stem-naming.

### Scope

- Names nothing; fences only value-naming at @469/@1090.
- Untouched: 80's global value (open, absent from registry), A8 verb-frame, poly-80-docket (red-team venue), the @1322 transfer question (`80-inf-transfer-1322` already queued — this result feeds it as a "no transfer source yet" negative), @1032/@1596 sibling windows, §7.
- No standing/red-team verdict contradicted, downgraded, or re-litigated. Canonical-stream caveat stands (a2_10/a6_05 offsets unvalidated).

## Verdict: NULL

C1 fails; the fence arm fires. Not a kill: no window forces any specific stem false, so the value stays open and fenced at these legs.

## Follow-ups (for supervisor queuing; all verified ABSENT from queue)

1. `subj-80-469-1090` (P4) — name the subject of "tout [80]ent" at both windows; if bare "tout" cannot host a 3pl finite verb, the 3pl-stem frame dies at grammaticality grade and the "80 06" contact needs re-segmentation.
2. `stem-80-corpus-3pl` (P4) — corpus census of which 3pl verbs occur with bare "tout" subjects in 1841 French; a zero across all lexemes fences the 3pl frame itself.
3. Not duplicated: `80-inf-transfer-1322` is already queued — it remains the venue for the @1322 transfer question this battery was meant to feed.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-80-469-stem.md`
- Queue: `val-80-469-stem` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.val-80-469-stem.tmp` + atomic rename; disk re-validated; own entry only; no downgrade; no tmp leftover)
- Lock `locks/val-80-469-stem.lock`: created on start, deleted on completion (verified gone). R5005, sealed gates, red-team adjudication queue untouched.
