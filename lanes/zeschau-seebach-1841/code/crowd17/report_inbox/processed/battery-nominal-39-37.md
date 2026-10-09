# Battery nominal-39-37 — verdict: PROMOTE (locus-level)

- Target: `nominal-39-37` (battery-queue.json, priority 3, status queued → verdict).
- Claim: test nominal 39 at @37 (`[91] [39] qui [41]`) — 39 as the nominal antecedent of relative qui.
- Worker: 4d3ec1e4-6f9f-462a-8464-16c52b25374a. Date: 2026-10-09.
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`; asserts held: 1,847 pairs, 96 types). `canonical.py` NOT used. R5005, sealed gates, red-team adjudication queue untouched.
- All @-offsets are 0-based pair indices in the repaired stream.
- Lock: `code/crowd17/next-token/locks/nominal-39-37.lock` created on start (2026-10-09T15:47:28Z, no stale lock present); deleted on completion.

## Bar (verbatim, pre-registered)

"name nominal-39 iff it parses with standing values and zero kill-grade contradictions; else fence"

**Restated as numbered pass/fail clauses (frozen before testing):**
1. **C1:** @37 parses as `[91] [39-N] qui [41]…` with standing values only (39 nominal, the antecedent of relative "qui").
2. **C2:** zero kill-grade contradictions with standing values.
3. **C3:** the listed adverse (R17-005 /a/ allophone LEAD, confirmed R20-010) is answered (compatible with nominal).

Standing values used (per protocol §7): pencil ground truth (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que); promoted/granted (87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce); provisional (59=est, 77="le"); 67 et/veut polyvalence; splits 20~17, 23~26.

## Method

1. Read BATTERY-PROTOCOL.md in full before testing.
2. Re-derived the repaired stream in-session; byte-confirmed the @37 window.
3. Tested the nominal parse against standing values; checked every standing constraint for forced non-nominal 39 at @37; checked the R17-005 adverse.

## Window-level evidence

Locus byte-confirmed (row a1_01):

| @ | pair | standing |
|---|------|----------|
| 35 | 08 | open |
| 36 | 91 | open (R19-164 grants 91=past-participle at the 16-91 windows @538/@1371 — locus-scoped, does not touch @37) |
| 37 | **39** | **nominal (this battery)** |
| 38 | 64 | "qui" granted (relative pronoun) |
| 39 | 41 | open (inside the relative clause) |
| 40 | 01 | open |
| 41 | 24 | 24-class finite/modal |
| 42 | 88 | A8 verb frame |

Parse: `…[08] [91] [39-N] qui [41] [01] [24-V] [88]…`. The granted relative pronoun "qui" (@38) requires a nominal antecedent; the NP ending at @37 is `[91] [39]`, so 39 must be nominal — this is forced by French grammar itself, not by any ungranted assumption. 91's class need not be named: the parse works with 91 as any determiner/adjective-like element preceding a noun.

## Clause results

- **C1: PASS.** `[91] [39-N] qui [41] [01] [24-V] [88]…` parses with standing values only; zero new assumptions.
- **C2: PASS.** Zero kill-grade contradictions:
  - verb-39 is KILLED at kill grade (`val-39-class-census`, 2026-10-09) — nominal is the surviving route, not a contradiction.
  - No standing verdict forces 39 non-nominal at @37.
  - 41's openness (§7 split candidate) is inside the relative clause and does not touch 39's class.
  - 91's openness is immaterial (no 91 value needed for the parse).
  - Canonicality caveat noted: row a1_01 offset unvalidated (68/70 rows unvalidated); the locus parse is conditional on the repaired phase.
- **C3: PASS.** R17-005 (39="/a/" GRANT LEAD, allophone tier; confirmed R20-010, not upgraded to full promote) is compatible: its three /a/ frames include precisely "91 [39] 64" @37. Nominal-39 at @37 is the class-level instantiation of that granted frame — a nominal bearing the /a/ phoneme (e.g. word-final 'a' or 'a'-containing noun). No contradiction.

## Verdict: PROMOTE (locus-level)

39 is named **nominal at @37** at battery grade. This is consistent with (not an upgrade beyond) `val-39-class-census`'s finding that @37 forces 39 as the nominal antecedent; it names the class explicitly under the target's bar.

## Scope

Locus-level only. 39's class elsewhere stays open: syllable/stem tier in "pre[39]" @1068/@1605; indeterminate at the other 10 windows. No global 39 value named; no registry change requested; R17-005 stays at allophone-tier LEAD (not upgraded). No standing/red-team verdict contradicted or downgraded; §7 intact. Per §4 (promote), no follow-ups required.

## Bookkeeping

- `battery-queue.json`: `nominal-39-37` queued → verdict/promote (temp-file + rename, own entry only; pre-write assert confirmed no prior verdict; JSON re-validated; no downgrade; 1,393 targets total).
- Lock `locks/nominal-39-37.lock`: created on start, deleted on completion.
- R5005, sealed gates, red-team adjudication queue untouched.
