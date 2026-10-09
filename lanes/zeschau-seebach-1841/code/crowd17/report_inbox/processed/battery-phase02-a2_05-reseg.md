# Battery report: phase02-a2_05-reseg

- Target id: `phase02-a2_05-reseg`
- Claim: "constraint sweep of row a2_05 under offset-1; hardens the @345 fence or dissolves it"
- Date: 2026-10-09
- Worker: battery worker (subagent 0befa484-880f-4a59-81aa-82828b816fe2)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py).
  1,847 pairs / 96 types re-derived in-session. All @-offsets 1-based.
  `canonical.py` never used. R5005, sealed gates, red-team adjudication
  queue untouched.
- Lock: code/crowd17/next-token/locks/phase02-a2_05-reseg.lock (created at start,
  deleted at end; no prior lock existed).

## Bar (verbatim, pre-registered before testing)

"constraint sweep under offset-1"

Numbered pass/fail clauses (restated before testing, not modified after):

1. C1: reparse row a2_05 under offset-1, byte-exact, and map the @345 fence's
   digit span onto the re-phase.
2. C2: test each leg of the @345 fence (stemless-'ent' 06 complex, "pre"+"n"+"ne"
   70-12-94 complex, 87="ce", no-que-governor, dead "ce qui par" left edge)
   for survival in any recognizable form under offset-1.
3. C3 (outcome): if no fence leg survives in any form, the @345 fence DISSOLVES
   under offset-1; if a parallel residual survives, the fence HARDENS
   (the re-phase does not rescue it).

## Method

1. Re-derived the repaired stream in-session (1,847 pairs verified).
2. Extracted row a2_05 raw digits (54 digits, canonical offset 0) and reparsed
   with offset 1: pairs = [s[i:i+2] for i in range(1, len(s)-1, 2)].
3. Mapped the canonical fence window (@345–@351) to raw digits and located the
   same digit span in the off-1 parse.
4. Censused the full off-1 row for the fence's material cells and checked the
   re-phased span for any parallel residual or new battery-grade anomaly.
5. Adopted (not re-litigated): residual-345-06's canonical-stream fence
   (@345 = 06-driven residual, value-independent of 01); edge-340-31-14's
   kill-grade "ce qui par" left-edge kill; standing values (§7:
   11=la, 70=pre, 29=er, 64=qui, 47=ce, 96=par, 94=ne, 06='ent' PROMOTE,
   67 et/veut positional rule).

## Window-level evidence

Row a2_05 raw: `637110011900925045548840036431144564964387010670129474`
(54 digits; canonical offset 0; upstream base offset 0).

Canonical (offset-0): 27 pairs, global 1-based @325–351 =
`63 71 10 01 19 00 92 50 45 54 88 40 03 64 31 14 45 64 96 43 87 01 06 70 12 94 74`

Offset-1: 26 pairs (drops leading digit `6`, trailing digit `4`) =
`37 11 00 11 90 09 25 04 55 48 84 00 36 43 11 44 56 49 64 38 70 10 67 01 29 47`

**Fence span:** canonical @345–@351 = `87 01 06 70 12 94 74` = raw digits
s[40:54] = `87010670129474` (byte-exact).

**Same span under offset-1:** in-row j=19–25 = `38 70 10 67 01 29 47`
(j=19 straddles s[40]; j=20–25 cover s[41:53] exactly).

**Full off-1 row census of fence material:**
- `06`: 0 (canonical row: 1). The stemless-'ent' leg has no carrier at all.
- `94`: 0. `87`: 0. `12`: 0. `74`: 0. `46`: 0.
- `70`="pre" (GT) persists at j=20, but its context is `38 70 10 67 01 29 47`
  — no 06/12/94 neighbors, no subjunctive structure, no bare-'ent'.
  No residual analog exists.
- `67` at j=22 with follower j=23=`01` (open): per the exceptionless
  positional rule, 67='et' default. No battery-grade anomaly in the span.

**Left-edge kill material (edge-340-31-14):** canonical in-row k=17–19 =
`45 64 96` = "ce qui par" (@342–344; residual-345-06's prose says @341–343,
a ±1 slip — the `45 64 96` trigram itself is byte-exact). Under offset-1,
the same digit span s[30:40] = `1445649643` becomes j=15–19 =
`44 56 49 64 38`. The "ce qui par" trigram does not exist anywhere in the
off-1 row. The kill dissolves, as the parent claim predicted.

## Per-clause pass/fail

1. C1 (byte-exact off-1 reparse + span mapping): PASS — 26 pairs, span
   mapped to s[40:54].
2. C2 (fence-leg survival): FAIL for every leg — `06`/`94`/`87`/`12`/`74`/`46`
   are all row-wide absent under off-1; the one persisting GT cell (`70`) has
   no residual context. The left-edge `45 64 96` trigram is likewise absent.
3. C3 (outcome): DISSOLVE fires — under offset-1 the @345 fence has no
   subject matter; the stemless-'ent' complex, the "pre-n-ne" complex, and
   the dead left edge all vanish. Same mechanism class as the
   seg-81-30-offset1 finding on row a1_01.

## Verdict: PROMOTE (conditional dissolution verified at battery grade)

**Scope (explicit):** promotes only the conditional finding — under offset-1,
the @345 fence and the edge-340-31-14 kill both dissolve. This battery does
NOT adopt offset-1 for row a2_05 and does NOT overturn residual-345-06's
canonical-stream fence (which stands on offset-0 per protocol). Row a2_05's
phase is red-team venue (canonicality caveat: 68 of 70 upstream row offsets
unvalidated). No standing/red-team verdict contradicted or downgraded; §7
intact. No follow-ups required per §4 (promote).
