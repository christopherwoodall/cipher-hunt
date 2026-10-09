# Battery report: verb-41-value

**Target:** `verb-41-value` — name 41's verb value at @40.
**Date:** 2026-10-09. Verdict: **NULL**.

## Bar (verbatim from battery-queue.json)

"test verb values (infinitive vs finite) at @40 with 01's value; name 41's verb value iff forced"

Numbered clauses (restated before testing, not modified after):
- C1: Test infinitive-41 vs finite-41 at @40 ("qui [41] [01]"), using 01's value where it bears.
- C2: Name 41's verb value iff forced by the window.

## Method

Read BATTERY-PROTOCOL.md first; lock created on start. Re-derived the repaired
1,847-pair / 96-type stream in-session from `code/side-keyhunt/repaired_offsets.json`
+ `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`
(1,847 pairs confirmed). `canonical.py` never used. R5005, sealed gate instances,
and the red-team adjudication queue untouched.

Window byte-confirmed: 0-based @38–42, row a1_01 mid-row = `64 41 01 24 88`
= "qui [41] [01] [24-faire] [88-verb]". @-offsets below are 0-based; the target's
"@40" is the 41 token (1-based @40).

## Standing premises (adopted, not re-litigated)

- 64 = 'qui' banked ground truth (relative pronoun).
- 41 is verb-forced at this window (class-41-contact: noun-41 and
  determiner-41 both die at @40; "qui [verb]" relative clause parses).
- 01's value open: R17-015 KILL CONFIRMED killed 01="ci" and 01="faisant" as
  general values; live candidates are 'en' and 'tain' (the bar's adverse).
- 24 = finite-verb class (ne-24-profile; §7 tension with 'en' is red-team venue,
  not engaged here).

## Per-clause results

### C1: infinitive vs finite — DISCRIMINATED, infinitive dead at kill grade

- **Infinitive-41: FAIL at kill grade.** Relative "qui" introduces a finite
  clause in 1841 French; "qui" + bare infinitive is ungrammatical
  (no elliptical-interrogative license exists in this window). This is
  independent of 01's value.
- **Finite-41: SURVIVES.** "qui [41-fin]" is a clean relative-clause head.
  Class discriminated (finite, not infinitive), but C1 does not name a value.

### C2: name 41's verb value iff forced — FAIL, not forced

Tested whether 01 can be 41's complement under each live 01 value,
since a complement would constrain 41's value:

- 01 = 'en': French clitic order is preverbal — "qui en [41-fin]" is the
  grammatical shape; postverbal "qui [41-fin] en" is ungrammatical.
  01 cannot be 41's complement here.
- 01 = 'tain': an interjection (and no 1841-diplomatic complement role);
  cannot be a finite verb's complement.
- 01 = 'ci': R17-015 kill-grade dead globally; not a live option.
- A word-internal composition "[41]en"/"[41]tain" would name 41's word but
  is unforced at battery grade (no composition evidence; 01 as letter
  cluster conflicts with its independent grouphood).

Since 01 cannot be 41's complement under any live value, 41's finite verb
value is fully unconstrained by this window: any finite verb fits.
No value is forced. C2 fails.

## Adverse answered

"01's value open ('en'/'ci'/'tain')" — answered, not ignored: R17-015 removes
'ci'; the remaining open values ('en', 'tain') are exactly what blocks the
naming bar, because neither can license "qui [41-fin] [01]" as a
verb-complement frame. The adverse is the fence's stated cause.

## Verdict: NULL

Infinitive is dead, finite survives, but no verb value is forced.
No standing verdict contradicted or downgraded; §7 intact.

## Follow-ups proposed (all verified absent from battery-queue.json)

1. `val-01-census` (P3) — census and name 01's value across its windows; a
   landed 01 value re-opens whether "[41]en"-style composition or a
   41|01 boundary constrains 41's verb value.
2. `qui-41-01-boundary` (P3) — byte-level word-boundary test between 41 and
   01; a forced boundary proves 41's verb value 01-independent.
3. `fin-41-lexicon` (P3) — test finite-verb value candidates for 41 against
   the "qui [41]" relative frame's subject/agreement shape.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-verb-41-value.md` (this file).
- Lock: `code/crowd17/next-token/locks/verb-41-value.lock` created on start,
  deleted on completion.
- Queue entry `verb-41-value` updated via temp-file + rename (status verdict,
  result null); no other entry touched.
