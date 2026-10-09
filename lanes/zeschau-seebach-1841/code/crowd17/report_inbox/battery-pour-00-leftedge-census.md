# Battery pour-00-leftedge-census — report

**Target:** `pour-00-leftedge-census` (priority 4)
**Claim:** census 00's predecessors stream-wide: does 00 ever open a clause
**Date:** 2026-10-09
**Verdict: PROMOTE (finding grade)**

## Bar (verbatim, pre-registered)

> tests boundary-arm family elsewhere

Restated as numbered clauses before testing:

- **C1:** census all of 00's windows with predecessors stated (n from the stream).
- **C2:** answer whether any window shows a byte-evidenced clause boundary before 00, beyond the known "96 00" case (bound-96-00-clause, NULL/fence, 2026-10-09).

No adverses listed.

## Method

Read BATTERY-PROTOCOL.md first. Created `locks/pour-00-leftedge-census.lock` on start.
Re-derived the repaired stream in-session: 1,847 pairs, 96 types (repaired_offsets.json +
upstream-ct_R5005.txt, parsed per repair_parse.py). `canonical.py` never touched.
R5005, sealed gates, red-team adjudication queue untouched.
Standing values used as premises only, never re-litigated: 46='que' (banked ground
truth), 00='pour' (A9, leg-1 class-level), 11='la' (banked), 17='fois' (promoted).

"Boundary-arm family" = claims that invoke a clause boundary to rescue a stranded
preposition (the bound-96-00-clause case: "par" stranding before "pour"). A clause
boundary counts as byte-evidenced iff it is marked by a standing clause marker
(46='que', 64='qui') or by row-initial position; row breaks are recorded but fenced
as clause edges per the standing canonicality caveat (rows are arbitrary digit wraps;
68 of 70 upstream row offsets unvalidated). The cipher has no punctuation anywhere.

## C1 — full census (PASS)

n(00) = 55, byte-confirmed. Predecessor distribution:

- 11 x4, 06 x4, 16 x4, 63 x4, 81 x3, 96 x3, 43 x3, 44 x3, 26 x3, 98 x3, 28 x3,
  09 x2, 19 x2, 33 x2, 02 x2, 48 x1, 93 x1, 14 x1, 07 x1, 46 x1, 01 x1, 68 x1,
  24 x1, 03 x1, 97 x1

Successor distribution (check sum = 55):

- 86 x12, 33 x8, 66 x7, 92 x6, 97 x4, 11 x4, 46 x4, 36 x3, 34 x1, 13 x1, 20 x1,
  64 x1, 98 x1, 67 x1, 44 x1

"96 00" x3 confirmed at 0-based @48 (a1_01), @466 (a2_10), @961 (a6_00) — matches
bound-96-00-clause's census byte-exact.

## C2 — clause boundaries before 00 (PASS)

Four windows show a byte-evidenced clause opening at 00, via the "pour que"
complementizer (00 46, byte-evidenced by banked 46='que' immediately after 00):

- **@106** (a1_03): "28 00(pour) 46(que) 11(la) 21" — "[28] pour que la [21]..."
- **@545** (a3_01): "06 00(pour) 46(que) 24 47" — "[06] pour que [24] ce..."
- **@1545** (a8_00): "43 00(pour) 46(que) 70(pre) 12(n)" — "[43] pour que pre[nne]..."
- **@1680** (a8_05): "44 00(pour) 46(que) 79(tout) 65" — "[44] pour que tout [65]..."

Under standing 00='pour' (A9), "pour que" + subjunctive is the standard
purpose-consequence complementizer; @1545's "pour que prenne" is textbook.
The clause opens at 00. None of the four follows 96, so the conditioned
00='contre' rival (red-team territory, par-only) does not touch them.

Everything else:

- **"que 00" @866** (a5_07): "47(ce) 46(que) 00(pour) 86 70(pre)" — 00 sits
  INSIDE the que-clause ("ce que ... pour [86] ..."); the boundary precedes 46,
  not 00. Not a clause-opening 00. (The window's strain was already recorded by
  battery-stem-86: "ce que pour [le] pre ce" parses "pour le pre[mier]" but the
  window carries "ce le" downstream; not re-litigated.)
- **Row-initial x3:** @748 (a5_03 rowidx 0, pre=28 crosses row edge),
  @1153 (a6_09 rowidx 0, pre=02 crosses row edge),
  @1822 (a8_11 rowidx 0, pre=19 crosses row edge).
  FENCED: row wraps are not clause edges under the standing canonicality caveat.
- **"96 00" x3** (@48/@466/@961): no boundary (bound-96-00-clause fenced it);
  00 does not open a clause there under any live reading.
- **Remaining 44 windows:** mid-clause complements ("[X] pour [Y]": "26 00 33"
  x3 purpose, "06 00", "16 00", "43 00", "63 00", etc.). No boundary evidence.

## Answer to the claim

Yes — 00 opens a clause in exactly **4 of 55 windows** (the "pour que"
complementizer frames). No other byte-evidenced clause opening exists.
The boundary-arm family (stranded-preposition rescue) has **no live instance
elsewhere**: the sole stranded case remains "par pour" x3, and it has no
boundary (bound-96-00-clause). Nothing here re-opens the fenced "96 00" arm.

## Standing state

No standing verdict contradicted or downgraded. 00='pour' (A9) used as premise;
the four "pour que" windows are consistent with it. §7 intact (no value declared).
The conditioned 00='contre' reading remains red-team territory, untouched.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-pour-00-leftedge-census.md` (this file)
- `battery-queue.json`: `pour-00-leftedge-census` → status `verdict`,
  result `promote`, date 2026-10-09 (temp-file + rename; own entry only)
- Lock `locks/pour-00-leftedge-census.lock` created on start, deleted on completion
- No follow-ups required (promote, not null)
