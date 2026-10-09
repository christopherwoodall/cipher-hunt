# Battery report: 08-leftattach-944-1323 — test 08 as word-final letter attaching leftward

Worker: battery-worker-08-leftattach-944-1323 (e8eb6c7c-ec9e-47b1-9685-72516a66f3e3), 2026-10-09.
Lock: created fresh at 2026-10-09T13:29:50Z (no pre-existing/stale lock present).
Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt), parsed per code/side-keyhunt/repair_parse.py
(replicated inline; asserts held: 1,847 pairs, 96 types). canonical.py never
touched. R5005, sealed gate instances, and the red-team adjudication queue
never touched. All numbers trace to the stream.

Provenance: follow-up #3 of order-control-08-62 NULL (2026-10-09). '08 62'
bigram exactly x2 stream-wide (@944, @1323), re-verified byte-exact below.

## Bar (verbatim, pre-registered)

"name the host word with <=1 ungranted assumption at both windows, else fence the left-attachment route."

## Bar restated as numbered clauses (fixed before testing)

- C1: at W1 (@944, row a5_10, '40 08' window), name the host word — the word
  08 would be the final letter of — with <=1 ungranted assumption.
- C2: at W2 (@1323, row a7_04, '80 08' window), name the host word with <=1
  ungranted assumption.
- C3 (else-arm): if C1 or C2 fails, fence the left-attachment route with
  stated cause.

Adverses: none listed.

Standing premises adopted (§7; battery promotes, never re-litigated):
08 is letter-tier, letter-value set = single letters only, value OPEN
(stem-08-letter-probe PROMOTE; 08-letter-geometry PROMOTE; val-08-31-letter
still queued — 08's letter value is ungranted). 40='e' pencil GT. 64='qui',
96='par', 17='fois', 87='ce' promoted free words — a word boundary is forced
after/before a free word (adopted 08-position-profile rule). 37-01 is a
granted unit (A12). 80/89 are granted verb-frames (A8) with value OPEN.
29='er' pencil. 98 = verb class (R19). 62 unvalued (62='il' killed at kill
grade; class is red-team venue). 08-position-profile PROMOTE: @944 is
"boundary-dependent: initial iff 40|08 boundary, else internal" (word-final
NOT a licensed reading there); @1323 is "undetermined".

## Method

Re-derived the repaired stream in-session byte-exact per repair_parse.py.
Byte-exact bigram census for '08 62', '40 08', '80 08'. ±8 context at both
loci with row-boundary check. For each window, traced the cheapest
standing-licensed left boundary of the host word, then counted ungranted
assumptions (values for unvalued cells; unlicensed boundaries) needed to
name the host word. Cross-checked 07/50/80/08 against all queue verdicts:
zero promoted values for any of them (1276-target scan).

## Window-level evidence (@-offsets, 0-based, repaired stream)

Bigram census: '08 62' exactly x2 — 08@944->62@945 and 08@1323->62@1324.
'40 08' @921 (40@921->08@922) and @943 (40@943->08@944). '80 08' @1322
(80@1322->08@1323). No row joins within ±8 of either locus.

- W1 @944 (a5_10) [936..952]:
  `33 21 64 37 01 07 50 40 | 08 62 98 | 96 86 01 77 86 96`
- W2 @1323 (a7_04) [1315..1331]:
  `62 48 98 15 24 03 29 80 | 08 62 98 | 56 30 06 62 94 70`

### W1 host-word audit (@944)

Cheapest standing-licensed left boundary: 64='qui' is a promoted free word,
so a word boundary is forced after 64; 37-01 is the granted A12 unit, so the
next word — the host — starts at 07. Host word = `07 50 40` + final-letter 08.
Values needed to name it: 07 (open — zero promoted values queue-wide),
50 (open — zero promoted values queue-wide), 08 (letter value open,
val-08-31-letter still queued). **= 3 ungranted assumptions > 1.**

Cheaper hosts all cost unlicensed boundaries:
- `50 40 08`: boundary 07|50 (ungranted) + values for 50, 08 = 3.
- `40 08` alone: boundary 50|40 (ungranted) + 08's letter value = 2, and the
  naming still fails cleanly: "e"+[08] as a French word forces 'n' ("en"),
  't' ("et" — collides with 67=et/veut, §7 sole polyvalence), 'r' ("er" —
  collides with 29='er' pencil GT), or 's' ("es" — not a word). The "en"
  via 08 has no standing anchor: the only 40-12='en' word-frame
  (enne-word-64) was KILLED, and '40 12' occurs exactly x1 stream-wide (@63),
  so no promoted spelling licenses it. Every naming path invents values §3
  bars at battery grade.

Additionally, the word-final reading presupposes a boundary AFTER 08
(08|62): zero standing basis — 62 is unvalued, no free word licenses it —
and the adopted position profile does not list word-final among @944's
licensed readings (boundary-dependent initial-or-internal only).

### W2 host-word audit (@1323)

No standing boundary marker left of 80 in [1315..1322] (62 unvalued,
48 values killed, 98 verb class is not a boundary licensor, 24/15/03 open).
Minimal host = `80 08`: 80's value is OPEN (A8 frame granted, value open —
zero promoted values queue-wide) + 08's letter value open.
**= 2 ungranted assumptions > 1.** Extending left with granted 29='er'
(`29 80 08`) does not help: still needs 80's value + 08's letter value = 2.
(Note the order: 29 precedes 80, so no infinitive-shaped stem+"er" reading
is available either.)

The word-final reading again presupposes an unlicensed 08|62 boundary
(adopted profile: @1323 "undetermined" — final is not a licensed reading).

## Per-clause pass/fail

- C1 (W1 @944): FAIL. Cheapest standing-licensed host (`07 50 40`+08) needs
  3 ungranted assumptions (07, 50, 08 values); every shorter host adds an
  unlicensed boundary and still needs >=2, with no clean French naming.
- C2 (W2 @1323): FAIL. Minimal host (`80 08`) needs 2 ungranted assumptions
  (80's value, 08's letter value); no standing boundary shortens the bill.
- C3: FENCE EXECUTED with stated cause:
  1. Neither window's host word is nameable within the bar's budget: W1
     needs >=3 ungranted assumptions, W2 needs >=2, against a bar of <=1.
     The deficit sits in unvalued cells (07, 50, 80, 08), not in the method.
  2. The word-final geometry itself is unlicensed at both windows: it
     presupposes an 08|62 boundary with zero standing basis, and the adopted
     08-position-profile licenses no word-final reading at @944
     (boundary-dependent initial-or-internal) or @1323 (undetermined).
     The only promoted word-final 08 window remains @198 ([60 08] before
     free 67) — a different frame, untouched by this fence.
  3. Naming shortcuts are closed: the candidate French readings of a
     `40 08` host ("en"/"et"/"er"/"es") each collide with a standing value
     (29='er', 67=et/veut) or a killed frame (enne-word-64), or are not
     words; '40 12' x1 stream-wide gives 08-as-'n' no distributional leg.

Not kill grade: both failures rest on unvalued cells — a future naming of
08's letter value (val-08-31-letter / syllable-08-letter-value) or of
80/07/50 could reopen the count. No standing or red-team verdict is
contradicted or downgraded; the @198 word-final promote stands untouched.

## Verdict

**null** — fence executed. 08-as-word-final-letter attaching leftward is
fenced at both windows: no host word is nameable within <=1 ungranted
assumption (W1: 3, W2: 2), and the required 08|62 boundary has no standing
basis at either window.

## Follow-ups (nulls regenerate work; all verified ABSENT from battery-queue.json)

1. **08-final-rerun-gated** (P3) — GATED re-fire of this target's C1/C2 iff a
   letter value for 08 is named (val-08-31-letter or syllable-08-letter-value
   promotes) or values for 80/07/50 land. Bar: name the host word with <=1
   ungranted assumption at both windows (@944/@1323); else re-fence.
   Evidence: this report (battery-08-leftattach-944-1323.md, null
   2026-10-09); deficit is purely in unvalued cells. Adverses: none.
2. **80-value-host-w2** (P3) — name 80's value at the W2 host (`29 80 08` /
   `80 08` @1322-1323) under the A8 verb-frame grant. Bar: 80's value named
   with <=1 ungranted assumption; a grant would drop W2's host-naming bill to
   08's letter value alone (1 <= 1), reopening C2. Evidence: a7_04 window
   [1315..1331] above; 80 value-open queue-wide. Adverses: none.
3. **08-62-boundary-adjudication** (P2) — adjudicate the 08|62 boundary
   directly, the presupposition of every 08-word-final claim at @944/@1323:
   byte-exact census of 08's right-neighbor boundary evidence across all 18
   windows. Bar: state 08|62 as boundary or no-boundary on
   standing-licensed grounds at both windows; else fence the boundary claim
   with stated cause. Evidence: '08 62' x2 @944/@1323; 62 unvalued;
   order-control-08-62's '08 | 62 98' parse. Adverses: none.

## Bookkeeping

- Lock `locks/08-leftattach-944-1323.lock` created on start (fresh, no stale
  lock), deleted on completion (verified below).
- Queue: `08-leftattach-944-1323` -> `status: verdict`, `result: null`,
  `2026-10-09` (pre-write assert: was `queued`/verdictless; temp-file +
  rename; JSON re-validated; own entry only; no downgrade).
- R5005, sealed gates, red-team adjudication queue untouched.
