# Battery erce-stem-fenceA — word-internal 'erce' stem test at Frame A

Date: 2026-10-09. Worker: 4efb2dbe-8d0e-469e-9273-1e56bd99892b.
Target: `erce-stem-fenceA` (priority 3). Follow-up #3 of battery-frame-29-47.

## Bar (verbatim from battery-queue.json)

> word-internal 'erce' stem test at Frame A once the left groups (43/36/48) resolve; kill the internal reading iff no French '[stem]erce' word fits

Numbered clauses (pre-registered before testing):
- C1: The left groups (43/36/48) resolve (a value is banked for each).
- C2: The word-internal 'erce' reading is killed iff no French '[stem]erce' word fits the Frame A loci.

Adverses (answered below): the internal word is not identified (left groups
unvalued); Frame A is fenced as non-boundary; the '[stem]erce' reading
(exercer/commerce/percer family) survives there unrefuted.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session
(`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`,
parsed per `code/side-keyhunt/repair_parse.py`; 1,847 pairs / 96 types
asserted). `canonical.py` never touched. R5005, sealed gates, red-team
adjudication queue untouched.

Standing values used: 82='m', 29='er', 40='e' (pencil GT); 47='ce' (A4,
granted); 48='e' (promoted, registry ["e","prom"]); 79="tout" (A5, granted);
43 and 36 = noun-class, value open (registry ["noun","cls"]).

## Window evidence (all byte-traced, 0-based)

- Frame A window 1, 0-based @17-26 (row a1_00):
  `17 64 98 82 43 | 29 47 33 | 55 81`
  ("fois qui vient m[43] er ce [33] ..."). Left group = 43 at @21.
- Frame A window 2, 0-based @1225-1234 (row a7_01):
  `57 64 79 82 48 | 29 47 33 | 29 85`
  ("qui tout m e er ce [33] ..."). Left group = 48='e' at @1229.
- "29 47" census: exactly 4x stream-wide (0-based 29-positions
  @22, @422, @1230, @1590). Confirmed in-session.

## Per-clause results

- C1 (left groups resolve): **FAIL**. 48='e' is promoted (resolved); 43 and
  36 remain noun-class with open values (no battery verdict has named a
  value for either; checked all 43/36-target verdicts in
  battery-queue.json). The bar's dependency is unmet, so per the brief the
  battery test is **fenced with stated cause**: the kill clause cannot be
  evaluated frame-wide while 43's value is open (the internal word at @22
  would be "m" + value(43) + "erce"; 43 is noun-class, not letter-tier, so
  no battery-grade enumeration is available).
- C2 (kill iff no French '[stem]erce' word fits): **cannot fire frame-wide**
  (dependency unmet). Locus-level result at the 48-resolved window only
  (see below).

## Substantive finding: internal 'erce' reading DEAD at @1230 (kill grade)

At the 0-based @1230 window the internal reading is testable on resolved
standing values alone, and it dies:

- 82='m' + 48='e' + 29='er' + 47='ce' composes to "meerce". Left of 82 is
  79="tout" (A5, complete word), so no French word extends left past 82;
  the internal word would have to be "meerce"-shaped.
- "meerce" contains "eer". Corpus check (code/side-period/corpus/, 98 files,
  ~59M chars): every "eer" hit is English/Dutch/German ("volunteers",
  "Meyerbeer", "Meer", "mountaineers", "Engineers", "beer") or an OCR
  artifact ("creer"/"suppleer" = unaccented "créer"/"suppléer";
  "Heere"/"Meere"/"Speere"/"leere" verified as German OCR text in context).
  **Zero genuine French words contain "eer."**
- Independently, "me" (82+48) is a complete French word (clitic), forcing 29
  word-initial — the same positional logic battery-erce-1590 used to resolve
  @1590 ("'me' is a complete word, forcing 29 word-initial").
- So the word-internal 'erce' reading is dead at the @1230 window at kill
  grade, on resolved values only, with no ungranted assumptions.

At @22 (0-based) the internal reading **survives unrefuted**: the internal
word would be "m" + value(43) + "erce" and 43's value is open, so no
battery-grade fit test is statable. This is exactly the residual
battery-frame-29-47 left open.

## Adverse disposition

The adverse ("the '[stem]erce' reading survives there unrefuted") is
narrowed with stated cause: it survives only at the @22 locus now; it is
killed at the @1230 locus. No standing or red-team verdict contradicted,
downgraded, or re-litigated; §7 intact.

## Verdict: NULL (fence executed — dependency unmet)

The battery test as specified cannot fire: C1 fails (43/36 unvalued), so the
frame-wide kill clause is fenced with stated cause. The @1230 locus-kill is
recorded as new evidence narrowing the residual to @22.

## Follow-ups (for supervisor queuing; all verified absent from battery-queue.json)

1. `erce-stem-fenceA-rerun` (P3): re-run this bar once 43's value resolves;
   the @22 window is the only surviving locus of the internal reading.
2. `erce-22-stemshape` (P4): enumerate French "m[X]erce" word shapes for
   plausible X classes to bound the @22 internal reading without naming 43.
3. `seg-82-43-22` (P4): test the "82 43" contact at 0-based @20-21 for
   word-internal composition vs boundary; a forced boundary kills the
   internal reading at @22 without 43's value.

Not duplicated: `erce-08-singleton` and `erce-14-singleton` already queued.

## Bookkeeping

- Report: code/crowd17/report_inbox/battery-erce-stem-fenceA.md
- Queue: `erce-stem-fenceA` -> status `verdict`, result `null`, 2026-10-09
  (pre-write assert passed: was queued/verdictless; target-id-unique tmp
  `battery-queue.json.erce-stem-fenceA.tmp` + atomic rename; disk
  re-validated; own entry only; no downgrade; no tmp leftover).
- Lock: created 2026-10-09T21:04:30Z (no stale lock), deleted on completion
  (verified gone).
- R5005, sealed gates, red-team adjudication queue untouched.
