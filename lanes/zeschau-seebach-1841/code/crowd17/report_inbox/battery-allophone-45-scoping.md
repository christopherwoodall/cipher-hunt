# Battery verdict: allophone-45-scoping

## Bar (verbatim, pre-registered)

"(a) enumerate all 22 windows of 45, assign each to 'ce' or 'dict'-syllable (or fenced residual) with per-window parse; (b) the account holds iff the assignment matches the {13,01}-exclusivity partition with <=2 fenced residuals and preserves A11's three mirror legs (@314/@340/@1024); (c) gather only — the positional declaration stays escalated to the red team, no battery-level declaration."

Restated as numbered clauses:
- **C1:** all 22 windows of 45 enumerated on the repaired stream, each assigned 'ce' / 'dict'-syllable / fenced residual with a per-window parse.
- **C2:** the assignment matches the {13,01}-exclusivity partition, has <=2 fenced residuals, and preserves A11's three mirror legs.
- **C3:** gather-only — no battery-level declaration of positional allophony; that stays with the red team.

## Method

Read BATTERY-PROTOCOL.md first. Lock created on start (agent id + UTC timestamp), deleted on completion.
Re-derived the repaired 1,847-pair / 96-type stream in-session from
`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`
(parsed per `repair_parse.py`). n(45) = 22 confirmed. `canonical.py` never used.
R5005, sealed gates, red-team queue untouched.

**Offset convention:** all @-offsets below are 1-based token positions (stream index + 1).
The bar's "@314/@340/@1024" mirror-leg offsets are 0-based; they are my
1-based @315 / @341 / @1025 (byte-identical windows, verified).

## C1: the 22-window census with assignments

Predecessor/successor context is ±4 pairs. Standing values used: 87="ce"
(promoted), 47="ce" (A4 allophone), 46="que" (GT), 96="par" (GT), 11="la" (GT),
64="qui" (promoted), 78="ver" (R16-005 LEAD), 79="tout" (A5), 45="ce" (A11 HOLD),
00="pour" (A9), 84="on" (A15), 40="e"/29="er" (GT), 06="ent" (promoted),
59="est" (provisional), 77="le" (provisional).

Post-78 windows (pre=78): exactly 4 — @315, @575, @984, @1166.

| # | 1-based @ | context (pre .. suc) | assign | parse |
|---|-----------|----------------------|--------|-------|
| 1 | @15 | 76 **45** 91 | ce | "[76-noun] ce [91]" — determiner 'ce' |
| 2 | @105 | 59 **45** 28 | ce | "est(59) ce [28-unknown]" — R16-era est-ce frame |
| 3 | @263 | 74 **45** 93 | ce | "[74] ce [93-verb]" — determiner 'ce' |
| 4 | @315 | 78 **45** 64 | FENCED residual #1 | see below |
| 5 | @333 | 50 **45** 54 | ce | "[50] ce [54]" — determiner 'ce' |
| 6 | @341 | 14 **45** 64 | ce (mirror leg 2) | "[14] ce qui(64)" — "ce qui" mirror |
| 7 | @402 | 11 **45** 88 | ce | "la(11) ce [88-verb]" — determiner 'ce' (window strain is 88-side) |
| 8 | @438 | 63 **45** 46 | ce | "[63] ce que(46)" — 'ce' before que |
| 9 | @479 | 74 **45** 93 | ce | "[74] ce [93-verb]" — determiner 'ce' |
| 10 | @570 | 76 **45** 94 | ce | "[76-noun] ce [94]" — determiner 'ce' |
| 11 | @575 | 78 **45** 13 | dict-syllable | "ce(87) ver-dict(78-45) [13]..." = "ce verdict" — certified sole host (battery-dict-45-host-inventory) |
| 12 | @604 | 96 **45** 93 | ce | "par(96) ce [93-verb]" — 'ce' after par |
| 13 | @679 | 77 **45** 23 | ce | "le(77) ce [23]" — determiner 'ce' |
| 14 | @698 | 50 **45** 28 | ce | "[50] ce [28]" — A11 HOLD honored at @697-698 (donc-28-triangulate) |
| 15 | @975 | 51 **45** 08 | ce | "[51] ce [08]" — determiner 'ce' |
| 16 | @984 | 78 **45** 01 | dict-syllable | "ce(47) ver-dict(78-45) [01]" — positional; reading conditional (ver-78 LEAD + dict-45 lead; ci-demonstrative-census three-way fence noted) |
| 17 | @1025 | 64 **45** 64 | ce (mirror leg 3) | "qui(64) ce qui(64)" — "ce qui" mirror |
| 18 | @1056 | 74 **45** 23 | ce | "[74] ce [23]" — determiner 'ce' |
| 19 | @1166 | 78 **45** 13 | dict-syllable | "[83] [21] [67] ver-dict(78-45) [13] [55-61-94]" — W3 formula "verdict" |
| 20 | @1202 | 29 **45** 58 | ce | "er(29) ce [58]" — 'ce' (58 non-verbal per ant-58-ending kill) |
| 21 | @1215 | 96 **45** 36 | ce | "par(96) ce [36-noun]" — 'ce' after par |
| 22 | @1552 | 92 **45** 23 | ce | "[92] ce [23]" — determiner 'ce' |

**Fenced residual #1 (@315, 1-based; bar's @314):** "84 24 37 78 45 64 59 32 94".
Positionally post-78 (would read 'dict'-syllable under a bare pre-78 rule), but
battery-dict-313-w1-adjudicate resolved this window to A11 'ce' ("ce qui est [32]e"),
and the 'verdict qui' reading lost on assumption count. The A11 'ce' reading is
PRESERVED here as the mirror leg; the residual is fenced against the
positional rule, not against A11. Residuals total: 1 (bar allows <=2).

## C2: partition check

- **{13,01}-exclusivity:** followers of the 4 post-78 45s = {64, 13, 01, 13}.
  Followers of the 18 non-post-78 45s = {91, 28, 93, 54, 64, 88, 46, 93, 94, 93,
  23, 28, 08, 64, 23, 58, 36, 23} — zero 13, zero 01. Exclusivity holds exactly.
- **Mirror legs preserved:** @315 (0b@314) "78 ce qui" — A11 'ce' reading kept
  (residual fence, see above); @341 (0b@340) "[14] ce qui"; @1025 (0b@1024)
  "qui ce qui". All three 'ce' mirror legs intact.
- **Positional rule consistent:** every 'dict'-syllable assignment sits at a
  post-78 window; every 'ce' assignment sits at a non-post-78 window, except the
  one fenced residual. One residual <= 2. C2 PASS.

Note: the boundary-45-exclusivity-sensitivity battery (now verdict/promote)
independently confirmed the {13,01}-exclusivity survives leave-one-out
(p<0.05 all four tables). This battery's partition finding agrees with it.

## C3: gather-only

No positional-allophony declaration is made at battery level. The refined
candidate ("45='dict' iff 78 word-medial", R18-026) stays escalated to the red
team; this battery supplies only the evidence package. C3 PASS.

## Adverses answered

- **boundary-45-exclusivity-sensitivity:** now verdict/promote — coordinated; its
  robustness result agrees with this census.
- **§7 sole-polyvalence:** honored. No polyvalence declared. The fenced residual
  is an evidence-package residual, not a second lexeme; the allophony decision
  itself belongs to the red team.

## Headline

The 22-window positional account is internally consistent: 18 'ce' windows
(including the three "ce qui" mirror legs), 3 'dict'-syllable windows at post-78
positions (the certified 'verdict' host set), and exactly 1 fenced residual
(@315, where A11's 'ce' mirror leg contradicts the bare pre-78 positional rule).
The {13,01}-exclusivity partition is byte-exact. Packaged for the red team;
no battery-level declaration.

## Verdict: PROMOTE (census-finding grade — promotes no value, declares no
allophony; gather-only evidence package)

## Bookkeeping

Report at `code/crowd17/report_inbox/battery-allophone-45-scoping.md`.
`battery-queue.json` updated via temp-file + rename (`allophone-45-scoping`:
queued -> verdict/promote, pre-write assert confirmed no prior verdict, JSON
re-validated). Lock created on start, deleted on completion. No standing
verdict contradicted or downgraded. R5005, sealed gates, red-team queue
untouched; `canonical.py` never used; all numbers re-derived on the repaired
1,847-pair stream.
