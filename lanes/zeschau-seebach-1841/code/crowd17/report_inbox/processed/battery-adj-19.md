# Battery verdict: adj-19

## Bar (verbatim from queue)
"promote iff >=2 independent predicative frames"

Restated as numbered clauses:
- C1: >=2 independent predicative frames for 19 exist on the repaired stream.
- C2: every listed adverse answered (answered = re-parsed cleanly, fenced with
  stated cause, or shown to be a misread — not ignored).

## Method
Read BATTERY-PROTOCOL.md first. Created `locks/adj-19.lock` on start with
agent id + UTC timestamp. Re-derived the repaired 1,847-pair / 96-type stream
in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`
(parsed per `repair_parse.py`); verified 1,847 pairs, 96 groups.
`canonical.py` never used; R5005, sealed gates, red-team queue untouched.
All offsets below are 1-based stream indices of the 19 token unless stated.

## 19 census (re-derived, byte-exact)
n(19)=9. Predecessor set: {01, 09, 10, 41, 59, 88, 90, 98}.
Successor set: {00, 18, 24, 41, 48, 58, 64, 74}.

| @ | window (pre 19 suc) | row |
|---|---|---|
| 91 | 98 19 41 | a1_02 |
| 122 | 90 19 58 | a1_03 |
| 212 | 88 19 74 | a2_00 |
| 329 | 01 19 00 | a2_05 |
| 486 | 01 19 64 | a2_11 |
| 585 | 10 19 18 | a3_02 |
| 966 | 41 19 24 | a6_00 |
| 1779 | 59 19 48 | a8_09 |
| 1822 | 09 19 00 | a8_10/11 (row boundary) |

## The single established leg
@1774-1783 = `94 24 | 87 64 59 19 48 74 65 23`:
- @1776 = 87 = "ce" (promoted)
- @1777 = 64 = "qui" (banked GT)
- @1778 = 59 = "est" (provisional)
- @1779 = 19
- @1780 = 48 = "e" (R17 letter-tier)
= "ce qui est 19[e]". The single predicative leg holds: "est 19" is the
copular frame, with 48 as a plausible feminine '-e' inflection on the
adjective (mirrors fem-32e's "est 32e"). Matches the protocol hold "19 (1 leg)"
and the target evidence note (finders' "@1777" = the 'qui' token).

## Clause results
- **C1 — FAIL (epistemic).** The "59 19" bigram occurs exactly once
  stream-wide (@1778-1779). No other predecessor is a copula candidate:
  59="est" is the only copula candidate and 37/32/42 (A1 predicative frames)
  never precede 19 (37/32/42 before 19: none). The other eight windows are not
  predicative frames under standing values:
  - @91 "98 19 41": 98 is a finite verb ("vient [19]") — not a copula.
  - @966 "41 19 24": 24 = "faire" (battery-promoted) — not a copula.
  - @486 "01 19 64": relative "…[01] 19 qui…" — adjective/noun head of a
    relative, not a predicative frame (see follow-ups).
  - @122/@212/@329/@585/@1822: 90/88/01/10/09 before 19 — open values, no
    copular shape statable; "01 19 00" x2 (00="pour" A9) is prepositional, not
    copular. Nothing in any window forces 19 non-adjectival, but no second
    independent predicative frame can be named.
- **C2 — adverses answered.** "single leg": confirmed byte-exactly (9 windows,
  exactly one copular frame). "adjective battery keyhole": acknowledged — the
  adjective class for 19 would rest on one window, so a promote is blocked at
  battery grade; the single leg is unrefuted (no window forces a rival reading).

## Verdict: NULL
Only one independent predicative frame exists; the bar requires >=2. This is
not kill-grade: the "est 19[e]" leg parses cleanly under standing values
(provisional 59="est", R17 letter-tier 48="e") and nothing on the stream
forces 19 non-adjectival. No standing verdict contradicted or downgraded; §7
intact; the protocol hold "19 (1 leg)" stands as confirmed, not re-litigated.

## Follow-ups proposed (for supervisor queuing)
1. `inflect-19e-48` (P3) — test @1778-1780 "19 48" as feminine '-e' inflection
   under the R17 letter-tier, parallel to fem-32e's "est 32e" (§3/4 windows).
   If 19 inflects like 32, the adjective-class lead gains a second independent
   leg; if 48 is not 'e'-inflectional at @1780, the single leg dissolves.
2. `noun-19-486-relative` (P3) — adjudicate @486 "01 19 64=qui": is 19 an
   adjective or a noun as the head of the relative clause? Deciding it either
   kills the relative-clause rival or fences it, sharpening the predicative
   account.

## Bookkeeping
- `battery-queue.json` `adj-19` → status `verdict`, result `null`, date
  2026-10-09 (temp-file + rename, own entry only; pre-write assert confirmed
  queued/verdictless; JSON re-validated post-write).
- Lock created on start with agent id + UTC timestamp, deleted on completion.
- No standing verdict contradicted or downgraded. R5005, sealed gates,
  red-team queue untouched; `canonical.py` never used.
- 1841 diplomatic French only; every number re-derived on the repaired stream.
