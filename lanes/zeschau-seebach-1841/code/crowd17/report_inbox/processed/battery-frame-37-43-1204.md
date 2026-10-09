# Battery report: frame-37-43-1204

## Target
`frame-37-43-1204` (P3)

## Claim (verbatim from battery-queue.json)
Test the det-adjacent @1204 window ('47 43 55', ce[43]...): if 'ce [43]' parses as a licensed NP it is the only surviving host candidate for an attributive-91 parse; else fence it there too.

## Bar (verbatim, pre-registered)
'ce [43]' parses as a licensed NP under standing values, or the @1204 host is fenced.

Restated as numbered clauses:
- C1: 'ce [43]' parses as a licensed NP under standing values at @1203–1204.
- C2: if C1 fails, the @1204 host is fenced.

## Method
Re-derived the repaired 1,847-pair / 96-type stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`
parsed like `code/side-keyhunt/repair_parse.py`; asserts held (1847 pairs,
96 types). `canonical.py` never used. 1841 diplomatic French only. Adverses:
none listed.

## Window-level evidence
- Locus byte-confirmed: 0-based @1203=47, @1204=43, @1205=55, row a7_00.
  Wider window @1199–1209: `64 29 45 58 47 43 55 61 21 65 64` =
  "qui er ce [58] ce [43] [55] …".
- n(43)=16, byte-exact census: @21(82/29), @43(88/81), @244(56/00),
  @258(32/77), @343(96/87), @386(37/91), @439(46/98), @563(11/24),
  @1027(96/87), @1092(06/07), @1126(37/00), @1204(47/55), @1303(08/21),
  @1305(21/77), @1544(78/00), @1724(37/98).
- Standing values at the window:
  - 47 = 'ce', granted (A4, allophone tier) — determiner-capable; 47 shares
    the 'ce' functional range with 87 (promoted determiner at @644).
  - 43 = [noun, cls], granted R19-045 (Round 19). Scope: all windows EXCEPT
    @21, which is fenced non-nominal (R19-064); @1204 is inside the grant's
    scope. Value open; class tier is sufficient for NP syntax.
  - 58 = [nominal, cls] (R19) at @1202; irrelevant to the NP's internal
    licensing but confirms no fused-unit reading steals 47.

## Per-clause results
- **C1 PASS.** Under standing values alone, "47 43" = 'ce' + noun-class =
  DET + N = the licensed "ce [noun]" NP shape of 1841 French. Zero new
  assumptions: no value named for 43, no polyvalence declared (§7 intact —
  67 remains the sole true polyvalence), no standing verdict contradicted
  or downgraded. The red-team grant is explicit that class-tier noun status
  holds at @1204 (only @21 is excluded).
- **C2 moot** (antecedent false).

## Verdict
**PROMOTE.** The @1204 host is NOT fenced: 'ce [43]' parses as a licensed NP
under standing values with zero ungranted assumptions.

## Scope
NP-level only. This verdict names no value for 43, says nothing about 55's
role or the full clause at @1203–1205, and does not resurrect any 43/91
geometry (per detframe-43-hunt NULL: no 91 within 2 positions of any 43
window except @386). Consistent with (not duplicating) detframe-43-hunt's
finding that @1204 and @563 are the two strict immediate-predecessor-DET
43 windows.

## Follow-ups
None required (promote per §4). Natural continuations already queued or
red-team venue: 55's class/value naming; red-team value-naming of 43.

## Bookkeeping
- Lock `code/crowd17/next-token/locks/frame-37-43-1204.lock` created on start
  (agent 8c4ce5c9-6ebf-4954-8a1b-b6421af5c492, 2026-10-09T12:25:50Z), deleted
  on completion.
- Canonical-stream caveat stands (row a7_00 offsets unvalidated).
- R5005, sealed gates, red-team adjudication queue untouched.
