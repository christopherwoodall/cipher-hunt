# Battery report: verdict45-value — 'ce verdict' x2 as the positive leg for 78='ver'

- Target id: `verdict45-value` (battery-queue.json, priority 3, status queued)
- Claim: the surviving positive leg for 78='ver' is 'ce verdict' x2 (@573, @982)
- Worker: fa9bf64f-5239-4a51-885f-bb5d55173baa
- Date: 2026-10-09
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
  `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`;
  1,847 pairs / 96 types re-derived in-session).
  `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.
- Lock: code/crowd17/next-token/locks/verdict45-value.lock (created at start, deleted at end).

## Offset convention

All @-offsets in this report are **0-based pair indices in the repaired stream**
(the convention of battery-dict-45-circle-break and the target brief). 1-based
equivalents are given where a cited report used them.

## Bar (verbatim, pre-registered before testing)

"(a) 45's value/frame from the R16-004 lead (coordinate, do not duplicate); (b)
'ce verdict' reads as the French word 'verdict' at both windows under standing
values — or the leg is fenced"

Numbered pass/fail clauses (frozen before testing):

1. (a) 45's value/frame taken from the R16-004 lead, coordinated not duplicated:
   R16-004 = 45="ce" (A11 HOLD arm) / 45="dict" (lead arm); the red-team's
   current refined candidate is "45='dict' iff 78 word-MEDIAL" (R18-026, granted
   as evidence package + §7-docket candidate, no declaration; R18-014 installed
   45="ce" at W1 @313 strengthening A11; R16-004 preserved).
2. (b) 'ce verdict' reads as one French word at @573 (0-based), OR the leg is
   fenced with stated cause.
3. (b) 'ce verdict' reads as one French word at @982 (0-based), OR the leg is
   fenced with stated cause.

Adverse: "45='dict' is a lead, not settled."

## Method

1. Re-derived the repaired stream in-session (1,847 pairs / 96 types).
2. Census: '78 45' occurs exactly 4x stream-wide (0-based 78-positions:
   @313, @573, @982, @1164 — byte-confirms dict-45-host-inventory's inventory).
   Of these, the two with a "ce"-granted predecessor immediately left of 78
   are @573 (87="ce", granted) and @982 (47="ce", A4 allophone tier). Hence
   'ce verdict' x2 = exactly these two windows. Not re-derived from memory.
3. Coordinated (not re-run): R16-004/R16-005 lead structure via
   next-token-redteam-r17/r18 (R17-006: 78="ver" LEAD confirmed, settle
   condition = "45='dict' resolved, or a new positive leg on banked/granted
   values"); dict-45-host-inventory (promote, narrow: 'verdict' the sole host
   of 45="dict" at the four 78-45 windows); verdict-w2-574-gate (promote:
   one-word 78-45 boundary at W2); battery-dict-45-w3-ceci (null: W3 @982
   circularity fence); battery-dict-45-circle-break (null: mutual
   conditionality finding); R18-014/R18-026 (45="ce" at W1; word-medial rule
   candidate escalated).
4. Standing values used: §7 banked (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e,
   46=que) and granted (87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour,
   84=on, 47="ce" allophone-tier); 78="ver" is LEAD (R16-005), not settled;
   A11 45="ce" HOLD stands; 67 et/veut sole true polyvalence.

## Window-level evidence (0-based pair indices, re-derived)

### @573 — "ce(87) verdict" composes (conditional)

Window (row a3_02), 0-based:
`@570:45 @571:94 @572:52 @573:87 | @574(0b573+1):78 @575:45 | @576:13 @577:55 @578:61 @579:94 @580:82 @581:06 @582:06 @583:50`
i.e. 0-based 573 = 87="ce" (granted), 0-based 574 = 78, 0-based 575 = 45.

(Note: the lane's older reports label this window "@573" for the 78 token —
a 0-based slip; byte-identical window. R17-007's re-derivation "61 94 82 06 06
50" @578 1-based = 61 at 1-based @578, which matches this parse exactly.)

Under the lead-augmented standing set:
- 87="ce" granted; 78="ver" (R16-005 LEAD); 78 is followed by 45 (not a word
  boundary) → the refined positional rule "45='dict' iff 78 word-MEDIAL"
  fires toward 45="dict" (R16-004 lead arm).
- One-word 78-45 boundary at this window was PROMOTED by verdict-w2-574-gate.
- "ce verdict" = "this verdict": grammatical French NP (demonstrative +
  noun). Follower 13-55-61 is value-open but the noun needs no completion;
  the clause continues "94 82 06 06" = "ne mentent" (R17-007
  granted-conditional on 94="ne" STRONG LEAD).

No window forces the composition false. The read is available, conditional on
the two unsettled leads (78="ver" + 45="dict") — the same mutual
conditionality the lane has recorded since ver-78. PASS (conditional).

### @982 — fenced under the w3-ceci circularity (coordinated, not re-litigated)

Window (row a6_01), 0-based:
`@979:92 @980:07 @981:76 @982:47 | @983(0b982+1):78 @984:45 | @985:01 @986:24 @987:89 @988:48`
i.e. 0-based 982 = 47="ce" (A4 allophone tier), 0-based 983 = 78,
0-based 984 = 45.

Byte-level the composition "ce verdict" is available here exactly as at
@573 (47="ce" granted; 78 word-medial → "dict" candidate; one-word boundary
not contradicted). But battery-dict-45-w3-ceci established the headline
circularity at THIS window: 78="ver" ↔ 45="dict" are mutually conditional
here — ver-78-rebar already counted this window once, conditionally, as one
of its two positive 'verdict' legs. Re-counting it as a positive leg would
double-count the same conditional. The window was recorded NEUTRAL for the
45="dict" leg (not adverse, not positive).

Per the bar's own alternative ("or the leg is fenced"), the @982 leg is
FENCED with stated cause: w3-ceci circularity, coordinated not re-run.
Clause outcome: fenced, not read.

## Per-clause pass/fail

1. (a) R16-004 coordination: PASS — 45's frame taken as the lead
   (45="dict" iff 78 word-medial; R18-026 evidence package; R18-014's
   45="ce" at W1 respected as the word-final arm). Nothing duplicated.
2. (b) @573 reads: PASS (conditional) — "ce verdict" composes under the
   lead-augmented standing set; no window forces it false.
3. (b) @982 reads: FENCED with stated cause — w3-ceci circularity; the
   window is NEUTRAL for the 45="dict" leg, not a positive leg.

Adverse "45='dict' is a lead, not settled": NOT answered at battery grade —
still a lead; R17-006's settle condition ("45='dict' resolved, or a new
positive leg on banked/granted values") is not met by this battery. It is
fenced as an epistemic condition, not ignored.

## Verdict: NULL

The claim as stated ("the surviving positive leg ... is 'ce verdict' x2")
is not sustained: only x1 (@573) is a conditional positive leg; @982 is
fenced/neutral, so the "x2" does not hold. Promote is blocked because the
adverse (45="dict" ungranted) is not answered. Kill is not available: no
window forces the claim false, and no cleaner rival is demonstrated
("verce"/two-word readings remain the A11 mirror, not a cleaner rival).

## Follow-ups (for supervisor queuing; all verified absent from the queue)

1. `dict-45-w4-adjudicate` (P2): decide 45 at W4 (0-based @1164, "21 67 78 45
   13 55 61") under the word-medial rule with a stated follower parse
   (13-55-61 coordinated from dict-frame-78-45-13-55-61). circle-break left
   W4 fenced as residual ("neither two-token reading parses at battery
   level"); W1–W3 now classified, W4 is the last unclassified 78-45 window.
2. `ver78-non45-positive-leg` (P2): R17-006's settle condition directly —
   test 78="ver" at ≥1 non-45 window on granted/banked values only
   (candidates: @819 0-based 818 "47 78 40" 'verre/verte'-shaped; @364
   0-based 363 "47 78 48"), breaking the 78↔45 mutual conditionality from
   the 78 side.

Coordinated existing item (not a duplicate): `ver78-45-dependency-gate`
(queued) is the venue for the @982 circularity itself; this report does not
re-open it.

## Standing-state check

No standing verdict contradicted or downgraded. R16-004/R16-005 leads
untouched; A11 HOLD untouched; 87="ce" and 47="ce" grants untouched. No new
polyvalence declared (§7 intact). The dict-45-host-inventory promote (narrow)
is consistent with and narrowed by this report (x2 "ce verdict" windows
reduce to x1 conditional positive + x1 fenced).
