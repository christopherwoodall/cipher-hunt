# Battery report: antec-08-91-39

**Target:** `antec-08-91-39` — "Name the antecedent NP 08 91 39 at @35-37 (antecedent of the sole 'qui [41]' frame @38-39)."
**Worker:** battery-worker-antec-08-91-39 (4d0cb551-bff3-4979-8d09-710e6bbf4fac).
**Date:** 2026-10-09. **Verdict: NULL** (unrecoverable at battery grade; adverse-confirmed).

## Bar (verbatim, from battery-queue.json)

"Name the value/class of the 08 91 39 NP via its 39/91/08 windows (39 n=13, 91 n=21, 08 n=18); report 41's implied agreement number; a landed agreement number re-opens the fin-41-le docket."

## Bar restated as numbered clauses (fixed before testing)

- **C1:** 08, 91, or 39 can be named (value) or classed from their window censuses (39 n=13, 91 n=21, 08 n=18), composing a nameable "08 91 39" NP.
- **C2:** 41's implied agreement number (3sg/3pl via qui's antecedent) lands on the named NP.
- **C3:** The landed agreement number discriminates within the fin-41-le docket.

## Method

Read `BATTERY-PROTOCOL.md` first; created `locks/antec-08-91-39.lock` on start
(UTC timestamp inside). Stream re-derived in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`,
parsed per `code/side-keyhunt/repair_parse.py`: 1,847 pairs / 96 types
asserted. `canonical.py` never used. R5005, sealed gate instances, and the
red-team adjudication queue untouched. Offsets below are 0-based; lane @ = +1.
All standing premises adopted from §7 (none re-litigated).

## Window-level evidence (@-offsets, repaired stream)

**Locus.** 0b @34–40 = `01 08 91 39 64 41 01` (row a1_01), i.e. lane @35–41.
The claim's antecedent is 0b @35–37 = `08 91 39`; the frame is 0b @38–39 =
`64 41` = "qui 41" (64='qui' granted).

**Hapax status (re-derived).** The trigram `08 91 39` occurs exactly once
stream-wide (0b @35); both bigrams `08 91` and `91 39` are also hapax.
`64 41` occurs exactly once (0b @38–39); 41 n=19 total but no other window
touches the relative frame.

**08 census (n=18 confirmed).** Followers: 31×3, 65×2, 62×2, then singletons
91, 34, 21, 67, 24, 52, 29, 01, 43, 81, 55. Predecessors: 60×2, 67×2, 37×2,
40×2, then singletons 01, 41, 85, 16, 17, 45, 80, 87, 47, 23. Contact with
GT letters: exactly one window (1b @61: `41 08 34 29 40` — 34='i', 29='er'
pencil GT; the lone letter-adjacent contact). 08='on' homophony is
kill-grade dead (on-08-homophony, battery KILL: uniformity holds but the
lane-standard cycling/frame discriminators reject the merge with granted
84="on"). No window names or classes 08.

**91 census (n=21 confirmed).** Followers: 53, 39, 65×2, 32×3, 37, 18, 36,
77, 12, 84, 67, 11×2 (1b @1006, @1669), 61, 78, 85, 79. The two "91 11"
('la') contacts do not license a nominal class — 11='la' as right neighbor
is a separate-word contact with no battery-grade noun frame behind it.
No window names or classes 91.

**39 census (n=13 confirmed).** All windows: locus + 1b @504 (`29 40 56 39
68 21 67`), @601 (`29 40 03 39 26 96 45`), @608 (`93 54 64 39 64 02 58`),
@693, @765, @1069, @1334, @1492, @1513, @1606, @1677, @1727. No GT-letter
contact anywhere; no window names or classes 39. (Note: this battery's
census found 13 windows; fin-41-lexicon listed 12 — it missed 1b @1727;
no conclusion changes.)

**41's agreement number.** 41's class is the three-arm split (red-team
docket item, venue red-team, unadjudicated) — so even a named NP could not
force a finite-verb agreement reading at battery grade. With the NP
unnameable, no number (3sg/3pl) lands. Clause C2's input is missing, and
C3's discrimination cannot run.

## Per-clause results

- **C1 — FAIL (epistemic, not kill grade).** 08/91/39 carry no banked,
  promoted, granted, provisional, or live value; the component trigram and
  both bigrams are hapax; the sole letter contact (08 @61) belongs to the
  gated seg-08-ier-61 re-segmentation. The NP is unrecoverable at battery
  grade.
- **C2 — FAIL (input missing).** 41's implied agreement number cannot land:
  no NP value/class + 41's three-arm class split pending red-team.
- **C3 — does not fire.** No agreement number landed; fin-41-le stays closed.

## Adverses answered

- "the NP may be genuinely unrecoverable at battery grade" — **confirmed,
  not ignored.** Three independent censuses (13+21+18 windows) plus the
  kill-grade closure of the 08='on' rescue (on-08-homophony) leave no live
  naming route. This is the honest NULL the target anticipated.
- "single-window roles don't carry" — **respected.** The locus's nominal
  reading of "08 91 39" as qui's antecedent is single-window and is not
  promoted into a class claim.

## Verdict: NULL

No standing or red-team verdict contradicted or downgraded; §7 intact.
Canonical-stream caveat stands (row a1_01 offset unvalidated per protocol).

## Follow-ups proposed (all verified absent from battery-queue.json)

1. `stem-08-letter-probe` (P3) — test whether 08 is word-internal at 1b @60
   (`41 08 34 29 40`, the sole GT-letter contact of 08): promote
   word-internal iff 08's letter contacts are all segmentally licensed;
   kill iff 08 must be a standalone word. A landed word-internal 08 kills
   "08 91 39" as a three-word NP and re-frames the antecedent.
2. `det-91-11-frame` (P3) — test 91's class via the two "91 11" windows
   (1b @1006, @1669): promote 91 nominal iff 'la' licenses a following-NP
   frame with stated byte cause; else fence. Coordinate with adj-91-nulls;
   do not duplicate.
3. `antec-08-91-39-rerun-gated` (P4) — gated re-run of this bar once 01's
   class lands (det-01-slot / 01-verbclass adjudication): with 01 resolved,
   the "01 08 91 39" antecedent boundary and the NP's head become testable.

## Bookkeeping

- Report: this file (`code/crowd17/report_inbox/battery-antec-08-91-39.md`).
- Lock: `code/crowd17/next-token/locks/antec-08-91-39.lock` created on start,
  deleted on completion.
- Queue entry `antec-08-91-39` updated via temp-file + rename (pre-write
  assert: status `queued`, verdict null — passed; post-write JSON re-validated;
  own entry only; 958 targets intact).
