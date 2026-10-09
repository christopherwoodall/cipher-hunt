# Battery report: fin88-646-rerun

- Target id: `fin88-646-rerun`
- Claim: re-run @646 finiteness for 88 without the now-dead @1541 parallel leg.
- Date: 2026-10-09
- Worker: battery worker (subagent fc9f6351-619b-446a-a172-c8564f77bce1)
- Stream: repaired 1,847-pair / 96-type parse re-derived in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` (asserts held: 1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed gate instances, and the red-team adjudication queue untouched.

## Bar (verbatim, from battery-queue.json)

"finite-88 forced at @646 with zero ungranted assumptions; kill iff forced non-finite; else fence"

Numbered pass/fail clauses (pre-registered before testing, not modified after):

1. **C1:** finite-88 is FORCED at @646 — no licensed alternative reading under standing values.
2. **C2:** the forcing argument uses ZERO ungranted assumptions.
3. **Kill check:** the window forces 88 non-finite at battery grade.
4. **Verdict rule:** promote iff C1 and C2 both pass; kill iff the kill check holds; else NULL (fence).

Terms (ASD-STE100): "finite" = a verb form that agrees with a subject ("il crée"). "Forced" = the reading is the only one the grammar allows at this window. "Ungranted assumption" = a premise the lane has not approved. The "parallel leg" is the now-dead @1541 window.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/fin88-646-rerun.lock` on start (2026-10-09T11:34:44Z); deleted on completion.
2. Re-derived the repaired stream byte-exact per `code/side-keyhunt/repair_parse.py`. All @-offsets below are 0-based pair indices.
3. Adopted, never re-litigated: 87=determiner at @644 (det-87-644-function PROMOTE, zero-assumption, this window only), 77="le" (provisional), 29="er" (banked GT), 88=VERB class (battery PROMOTE, pending red-team ratification), 24=finite-verb modal-shaped (R17-009, class-level; 24="faire" rejected at R18-008), val-61-premier (PROMOTE, locus-level @1556 only), val-61-contact (KILL of any global 61 value, stands), fin-88-645 NULL (not re-litigated, never downgraded).

## Window-level evidence

### The locus — 0b@643–648 (row a4_02, mid-row), byte-confirmed

`[643]24 [644]87 [645]61 [646]88 [647]77 [648]78` = "…[24] ce [61] [88] le [78]…"

### What changed since the parent NULL (fin-88-645)

Four new verdicts land after the parent's NULL:

1. **fin-88-1541-parallel → KILL.** The @1541 "62 93 88 le 78" window forces 88 non-finite ("Il [93-fin] [88-inf] le [78]"). The "[88] le [78]" transitive frame's only other attestation (the locus is the other) is now infinitive-shaped. The parallel leg that kept @646's finite reading "live" is dead: the frame now supports 88-as-INFINITIVE, not finite-88.
2. **det-87-644-function → PROMOTE (window-level).** 87 is a determiner at @644 with zero ungranted assumptions — all four "ce"-pronominal frames fail at grammar level (bare "ce" is never a direct-object pronoun in any period; 0 instances of finite-verb + bare "ce" + clause punctuation in 31.7M chars of 1841 French). "ce [61]" is therefore an NP, not a pronominal subject. This removes the pronominal-87 rival but does NOT name 61's value or resolve 24's form.
3. **form-24-643 → NULL.** 24's form at @643 (finite vs "en" residual) stays undecided.
4. **val-61-646-locus → NULL.** 61="premier" at @645 stays unproven by the locus method.

### C1/C2 test — is finite-88 forced with zero assumptions?

The finite-88 reading is: "…[24-fin] [ce 61=premier] [88-fin] le [78]" — the NP "ce premier" as subject of finite 88. It fails the forcing bar on two independent counts, each still an ungranted assumption after the four new verdicts:

1. **61="premier" at @645 is unstated.** val-61-premier is locus-level (@1556 only); val-61-contact's global-61 KILL stands; val-61-646-locus came back NULL. det-87-644 licenses the adjectival/nominal 61 arm but does not name it.
2. **The 24/88 collision is unresolved.** R17-009 grants 24 class-level finiteness. A finite 24 at @643 beside a finite 88 at @646 needs a clause boundary between them (juxtaposition without punctuation — unattested license) or 24 as the "en" residual (form-24-643 NULL). Either resolution is an ungranted assumption.

**C1 FAIL, C2 FAIL.** With zero assumptions the window is unparseable at battery grade; the finite reading is not the only licensed reading because no reading is fully licensed.

### Kill check — is 88 forced non-finite?

No. Nothing in standing values forces 88 non-finite at @646:

- The modal-NP-infinitive parse ("…[24-modal] ce [61] [88-inf] le [78]") is ungrammatical in French: a modal takes its infinitive complement directly ("il veut laisser"), never across an NP object ("*il veut ce premier laisser").
- A bare governed infinitive has no governor here and is 1841-zero in print register (gov-excl-inf drama/prose batteries).
- A8 is verb-frame only; it does not force the infinitive shape.
- The @1541 kill does not touch @646.

**Kill check does not hold.** Neither reading is forced. → **not kill-grade.**

## Verdict: NULL (fence executed)

Finite-88 at @646 is neither forced nor forced false without the @1541 parallel leg. The @1541 kill removes the frame-level support but does not supply a local forcing argument either way; det-87-644 narrows the NP frame ("ce [61]" is an object/subject NP, not a pronoun) without naming 61 or deciding 24. The window stays a 61/88 residual: resolution is downstream of (a) 61's value at @645 and (b) 24's form at @643. No standing or red-team verdict contradicted or downgraded; §7 intact; canonical-stream caveat stands (row a4_02 offset unvalidated).

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `boundary-24-87-643` (P3) — test for a licensed clause boundary between 24@643 and 87@644 (subject-position evidence, pause-mark precedent in the lane corpus); a licensed boundary dissolves the 24/88 collision at battery grade, removing ungranted assumption (2).
2. `np-inf-modal-corpus` (P3) — corpus verdict in 1841 diplomatic French: does any modal verb license "modal + NP + infinitive"? Confirmed zero kills the non-finite-88 arm here permanently; any attestation revives it.
3. `val-61-645-det` (P3) — name 61's class at @645 under the now-promoted determiner-87 (zero-assumption NP frame: "ce [61]"); adjectival-61 advances the "ce premier" subject arm one full assumption.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-fin88-646-rerun.md` (this file).
- Queue: `fin88-646-rerun` queued → verdict/null, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `locks/fin88-646-rerun.lock`: created on start, deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
