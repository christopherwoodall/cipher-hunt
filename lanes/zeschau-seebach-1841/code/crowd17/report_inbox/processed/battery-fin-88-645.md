# Battery report: fin-88-645

- Target id: `fin-88-645`
- Claim: test 88's finiteness at @645 ("ce premier [88-V]").
- Date: 2026-10-09
- Worker: battery worker (subagent b495157d-23a5-4e39-be56-edf65a7173dc)
- Stream: repaired 1,847-pair / 96-type parse re-derived in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` (asserts held: 1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed gate instances, and the red-team adjudication queue untouched.

## Bar (verbatim, from battery-queue.json)

"promote iff finite-88 forced at @645 with zero ungranted assumptions"

Numbered pass/fail clauses (pre-registered before testing, not modified after):

1. **C1:** finite-88 is FORCED at the locus — no licensed alternative reading under standing values.
2. **C2:** the forcing argument uses ZERO ungranted assumptions.
3. **Verdict rule:** promote iff C1 and C2 both pass; kill iff the window forces 88 non-finite; else NULL (fence) with 1–3 follow-ups.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/fin-88-645.lock` on start (2026-10-09T10:52:45Z); deleted on completion.
2. Re-derived the repaired stream byte-exact per `code/side-keyhunt/repair_parse.py`. All @-offsets below are 0-based pair indices.
3. Adopted, never re-litigated: 87='ce' (granted), 77='le' (provisional), 29='er' (banked GT), 88=VERB class (battery PROMOTE, 2026-10-09, pending red-team ratification), 24=finite-verb modal-shaped (R17-009, class-level; the 24="faire" value was REJECTED at R18-008, demoted to conditional lead; the 24="en" residual is live), val-61-premier (PROMOTE, locus-level @1556 only), val-61-contact (KILL of any global 61 value, stands).

## Window-level evidence

### The locus — 0b@644–648 (row a4_02, mid-row)

`…[643]24 [644]87(ce) [645]61 [646]88 [647]77(le) [648]78…` = "…[24] ce [61] [88] le [78]…"

Wider clause (0b@636–656): "…que(46) [60] et(67) le(77) [89] e(48) [20] [24] ce [61] [88] le [78] [52] m(82) ne(94) [76] [49] [24] [26] pas(30)…"

### Census facts (byte-exact)

- **"88 77 78" trigram: exactly 2× stream-wide** — 0b@646 (the locus) and 0b@1541 ("[62] [93] [88] le [78]", 62='il' battery-promoted). The transitive-governor frame "[88] le [78]" is real at @1541; its subject there is 62='il'.
- **"87 61" bigram: 1× stream-wide** (the locus only). "ce [61]" has zero repetition leverage.
- n(88)=23 confirmed.

### C1/C2 test — is finite-88 forced?

The finite-88 reading is: "ce [61=premier] [88-V-fin] le [78]" with "ce premier" as pronominal subject. It fails the forcing bar on three independent counts, each requiring an ungranted assumption:

1. **61="premier" at @645 is unstated.** val-61-premier is locus-level (@1556 "61 40 17" only); val-61-contact's KILL of any global 61 value stands. The parent flank census (premier-61-flank-census) itself graded @645 "flank-supported," not proven.
2. **"ce premier" as pronominal subject is unlicensed.** No standing frame licenses "ce"+"premier" as a pronominal subject phrase; it is a compositional assumption, not a standing value.
3. **24's class-level finiteness collides in the same clause.** R17-009 grants 24 = finite verb (class-level). If 24 is finite at @643, a finite 88 gives two finite verbs with no subordinate boundary (no qui/que) — ungrammatical. Dissolving the collision requires assuming 24 is the "en"-residual here — a live but unproven arm, i.e. another ungranted assumption.

That is ≥2 ungranted assumptions plus a standing tension. **C1 FAIL, C2 FAIL.**

### Kill check — is finite-88 forced false?

No. The finite reading stays live: the "[88] le [78]" transitive-governor frame is byte-real at @1541 with 62='il' as subject, and 88's battery verb-class legs include a finite-subject arm. 24's finiteness at @643 is itself unforced (the 24="en" residual is live). The window does not force the claim false → **not kill-grade.**

## Verdict: NULL (fence executed)

Finite-88 at @646 is neither forced nor forced false. The "ce [61] [88] le [78]" window stays a 61/88 residual: its resolution is downstream of (a) 61's value at @645 and (b) 24's form at @643. No standing or red-team verdict contradicted or downgraded; §7 intact; canonical-stream caveat stands (row a4_02 offset unvalidated).

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `val-61-646-locus` (P3) — test 61="premier" at @645 by the val-61-premier locus method; removes assumption (1).
2. `fin-88-1541-parallel` (P3) — force 88's finiteness at the parallel @1541 "[62] [93] [88] le [78]" window (62='il' battery-promoted subject); a forced-finite @1541 makes the @646 finite reading frame-consistent.
3. `form-24-643` (P3) — decide 24's form at @643 (finite vs "en" residual); finite-24 kills the finite-88 reading here, "en"-24 re-opens it.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-fin-88-645.md` (this file).
- Queue: `fin-88-645` queued → verdict/null, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `locks/fin-88-645.lock`: created on start, deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
