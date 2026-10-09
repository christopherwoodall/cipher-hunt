# Battery report: noun-91-det-frames

- Target: `noun-91-det-frames`
- Verdict: **NULL** (naming claim fenced per bar; 91's class stays open)
- Date: 2026-10-09
- Stream: repaired 1,847-pair / 96-type parse (re-derived in-session; asserts held:
  1,847 pairs, 96 types). `canonical.py` never used.

## Bar (verbatim)

"name nominal-91 iff >=2 windows parse with zero kill-grade contradictions, else fence"

Numbered clauses:

- C1: at least 2 of the 3 direct "DET 91" windows parse with 91 as a noun and
  zero kill-grade contradictions → name nominal-91.
- C2 (else): fence the nominal-91 naming claim on the DET windows.

## Method

Byte-exact census of all 21 loci of group 91 on the repaired stream, with ±4
context. Determiner set used: 11="la" (pencil GT), 77="le" (provisional),
87="ce" (granted), 47="ce" (A4 allophone), 45="ce" (A11 hold). Exactly three
direct DET-91 windows exist on the stream: @15 (45 91), @1005 (47 91),
@1518 (11 91). No 77-91 or 87-91 windows.

## Window-level evidence

### @15 (row a1_00): `06 77 78 18 93 62 98 76 [45 91] 53 17 64 98 82 43 29 47 33`

Standing values: 45="ce" (A11), 17="fois" (GT), 64="qui" (granted).
Reads "ce [91] [53] fois qui [98]". A noun-91 parse needs 53 to compose as a
pre-nominal modifier of "fois" in the order DET-N-ADJ-"fois", which has no
French license and no standing value for 53. Not a clean parse. Not a
kill-grade contradiction either (53 is unvalued; no forced non-nominal 91).

### @1005 (row a6_02): `67 11 96 82 33 00 86 56 [47 91] 11 52 35 18 79 80 78 47 03`

Standing values: 00="pour" (A9), 47="ce" (A4), 11="la" (GT), 79="tout" (A5).
Reads "pour [86] [56] ce [91] la [52] [35] [18] tout [80] [78] ce [03]". A
noun-91 parse needs either 52 verb-shaped taking "la" as object ("ce [N] la
[V]") or "la" opening a new NP ("ce [N], la [N]") — no standing license for
either; 52 is unvalued. Not a clean parse; not a kill-grade contradiction.

### @1518 (row a7_11): `12 61 59 39 81 88 11 31 [11 91] 67 08 31 24 11 11 48 96 87`

Standing values: 11="la" (GT), 67="et/veut" (sole polyvalence),
87="ce" (granted). Reads "[81] [88] la [31] la [91] [67] [08] [31] [24] la la
[48] par ce". With 67="et": "la [N] et [08] [31] [24] la..." — grammatical
DET-N coordination under either 67 reading ("la [N] veut [08]..." also
parses if 08 is infinitive-shaped). **Clean leg.** Zero kill-grade
contradictions. (Noted rival: 11 as object pronoun + verb-91, "la [V] et",
also grammatical — does not contradict the noun parse.)

## Per-clause results

- C1: FAIL — only 1 of 3 windows (@1518) parses cleanly as DET + noun; @15
  and @1005 are strained but not kill-grade contradictions.
- C2: FIRES — the nominal-91 naming claim is fenced on the DET windows.

## Verdict: NULL

nominal-91 is not named (bar's ≥2-window threshold not met). The claim is
fenced at the naming level only: no window forces 91 non-nominal, and 91's
class stays open. No standing verdict contradicted: R19-164's locus-level
grant (91 = past participle at the two 16-91 windows @538/@1371, adjective
fenced lane-wide) is untouched — this battery tested only the three DET
windows and names nothing. Consistent with R19-051's note that "91's
≥2-window bar still fails". §7 intact; canonical-stream caveat stands.

## Follow-ups (all verified absent from the queue)

1. `noun-91-nondet-windows` (P3) — test 91's class on the 18 non-DET windows;
   priority hostile loci: @520 ("70 91 77" = "pre [91] le", hostile to noun)
   and @277 ("84 91 37" = "on [91] [37-pred]").
2. `val-53-15-frame` (P4) — name 53's class at the @15 "ce 91 53 fois qui"
   frame; a verb/adjective-shaped 53 discriminates 91's role there.
3. `val-52-1005-frame` (P4) — name 52's class at the @1005 "ce 91 la 52"
   frame; a verb-shaped 52 taking "la" as object would clean up the window.

## Bookkeeping

- Queue: `noun-91-det-frames` → `status: verdict`, `result: null`, 2026-10-09
  (pre-write assert passed — was queued/verdictless; temp-file + rename;
  own entry only; no downgrade).
- Lock created on start (2026-10-09T15:24:06Z), deleted on completion.
- R5005, sealed gates, red-team adjudication queue untouched.
