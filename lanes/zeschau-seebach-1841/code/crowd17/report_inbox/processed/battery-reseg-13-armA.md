# Battery report: reseg-13-armA

Target: `reseg-13-armA`. Claim: "arm A dissolves without polyvalence -
13 closes the preceding nominal leftward and the verb-class successor
starts a new clause".
Date: 2026-10-09. Worker: subagent (battery worker).
Lock `locks/reseg-13-armA.lock` created 2026-10-09T06:13:40Z (no
pre-existing lock for this id); deleted on completion.

Offset convention: @n = 0-based pair index in the repaired 1,847-pair
stream (1-based in parens).

## Bar (verbatim, pre-registered)

"(a) state the clause boundary per window
(@68/@822/@1381/@1554/@1684) with standing values; (b) if any arm-A
window admits no boundary, the arm stands"

## Bar restated (numbered pass/fail clauses; frozen before testing)

1. For each of the 5 arm-A windows, the clause boundary is stated:
   where 13 closes the preceding nominal leftward, and where the
   verb-class successor starts the new clause — supported only by
   standing values (protocol section 7 + ratified promotes; battery
   leads marked as leads, class-open values marked, nothing invented).
2. Falsifier: if ANY one of the five windows admits no such boundary
   (a standing value forces the re-segmentation false), the arm stands
   and the claim is killed.

## Method

Read BATTERY-PROTOCOL.md first. Re-derived the repaired 1,847-pair
stream independently from `data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json`, parsed per
`code/side-keyhunt/repair_parse.py` (asserted 1,847 pairs / 96 types
before testing). `canonical.py` never used. R5005, sealed gates,
red-team queue untouched. Every number traces to the stream.

Standing values used: banked GT 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e,
46=que; granted 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour
(A9, leg-1 class-level), 84=on (A15), 47=ce (A4 allophone tier);
provisional 59=est, 77=le; promoted 24=finite verb class
(ne-24-profile), 93=verb class (verb-93), 65=noun class,
92=verb class; leads 94=ne (R17-001), 78=ver (R16-005), 30=pas,
06=ent; holds 45=ce (A11). Battery-grade (unratified, marked):
W1 subjectless-clause precedent ("ne mentent", every subject slot
closed); 69 noun reading live (§7 split candidate: noun 10-11/12 vs
verbal @1115); "62 94" leftward composition ("[62]ne", conditional on
77=le).

## Window-level evidence (re-derived, all 5)

Legend: `||` = the proposed clause boundary (13 closes nominal
leftward; verb-class successor starts new clause).

### @68 (69, a1_01, rowpos 33) — ADMITS
`08 34 29 40 12 94 92 69 [13] || 24 56 87 14 24 87 11 00 11 29 42`
- Left: 94=ne (lead) + 92=verb class + nominal "[69]-13". 69's noun
  reading is live (battery §7 split candidate; verbal only @1115).
  Left clause reads as [ne] [verb-92] [nominal-69-closed-by-13].
  (34/29/40 = "i er e" letter-level here — sub-lexical composition is
  normal on this row, supporting 13 as sub-lexical.)
- Right: 24=finite verb class starts new clause
  ("24 56 ce 14 ce la pour"); subject elided per W1 subjectless-clause
  precedent (fenced, not invented).
- Nothing in standing values forces another parse. ADMITS.

### @822 (823, a5_05, rowpos 22) — ADMITS (softest left leg)
`74 47 78 40 95 [13] || 24 87 59 38 82 01 24 87 11 77 76 59`
- Left: 47=ce (granted) + 78=ver (lead) + 40=e + nominal "[95]-13".
  95 is class-open; no standing value forces non-nominal. Exact role
  of "78 40" left of 95 is unresolved at battery grade (78=ver is a
  lead, not granted) — but the boundary's left leg needs only
  "[95]-13" to close a nominal, which no standing value forbids.
- Right: 24=finite verb class starts new clause ("24 ce est 38 m 01
  ... 24 ce la le ..."); subject elided (W1 precedent).
- ADMITS. Flagged: left-clause verb identification is lead-grade;
  the nominal-closing itself is unblocked.

### @1381 (1382, a7_06, rowpos 22) — ADMITS (cleanest)
`89 84 92 69 [13] || 24 65 68 52 82 16 06 29 67 86 29 89`
- Left: 84=on (granted A15) + 92=verb class + "[69]-13" — full SVO,
  "on [verb-92] [nominal-69-closed-by-13". Cleanest arm-A left leg.
- Right: 24=finite verb class starts new clause
  ("24 65-noun 68 52 m 16 06 29"); 65=noun class follows; subject
  elided or postposed (fenced, not decided).
- ADMITS.

### @1554 (1555, a8_01, rowpos 1) — ADMITS
`92 45 23 99 [13] || 93 61 40 17 11 26 30 06 60 71 50`
(preceded by `46 70 12 94 92` = "que pre 12 ne")
- Left: 92=verb class + NP "45=ce (hold A11) 23 [99]-13" — 45 is the
  determiner closing over "23 [99]-13"; 13 closes the nominal
  leftward. 99 class-open, unblocked.
- Right: 93=verb class starts new clause
  ("93 61 e fois la 26 pas 06"; 26=finite verb, 30=pas lead follow).
- ADMITS.

### @1684 (1685, a8_05, rowpos 18) — ADMITS (strongest left leg)
`44 00 46 79 65 [13] || 93 62 94 79 14 60 27 46 24 85 58`
- Left: 00=pour (granted) + 46=que (GT) + 79=tout (granted) +
  "[65]-13" — 65 is PROMOTED noun class; 13 closes the nominal
  leftward. Class-known predecessor: exactly what the claim needs.
- Right: 93=verb class starts new clause
  ("93 62 94 79=tout 14 60 27 46=que"); "62 94" composes leftward
  per the @508 battery finding ("[62]ne", conditional on 77=le);
  subject elided (W1 precedent).
- ADMITS.

## Per-clause pass/fail

1. **PASS.** Clause boundary stated per window with standing values:
   @68: after 13 (`69-13 || 24`); @822: after 13 (`95-13 || 24`);
   @1381: after 13 (`69-13 || 24`); @1554: after 13 (`99-13 || 93`);
   @1684: after 13 (`65-13 || 93`). Left legs use standing verbs /
   determiners (92 x3, 84=on, 45=ce, 46=que, 79=tout, 00=pour) and
   nominal-compatible predecessors; right legs use promoted
   verb-classes 24 (x3) / 93 (x2).
2. **PASS (falsifier not triggered).** No window admits no boundary.
   Stress tests run per window: no standing value forces any
   predecessor non-nominal (65 class-known noun; 69 noun reading live;
   95/99 class-open and unblocked); no standing value forces 24/93
   non-verbal (24=finite verb class, 93=verb class promoted). The arm
   does not stand — it dissolves.

## Adverses answered

- **n=5: ANSWERED BY EXHAUSTION.** Arm A is exactly these five
  windows; each was tested individually above. There is no sixth
  arm-A window to miss.
- **predecessor classes open: ANSWERED.** @1684's predecessor is
  class-KNOWN: 65=promoted noun class — the claim's strongest leg.
  @68/@1381's 69 has a live battery-grade noun reading (§7 split
  candidate; verbal only at @1115). @822's 95 and @1554's 99 are
  class-open, and no standing value forces them non-nominal. The
  bar's standard is admissibility ("admits no boundary" is the
  falsifier), and open classes admit the nominal reading.

## Caveats (battery-grade limits, for the red-team package)

1. **24's unadjudicated conflict.** 24-en-verb-conflict is queued but
   unadjudicated: 24=finite verb class (ne-24-profile, standing) vs
   24='en' (en85-gerund-reaudit). Three of five right legs
   (@68/@822/@1381) use 24 as the clause-starting verb. If the red
   team resolves 24='en', those three legs fail and this promote
   falls. The two 93-windows (@1554/@1684) are unaffected.
2. **New-clause subjects fenced, not identified.** The mechanism
   rests on the W1 battery-grade subjectless-clause precedent
   ("ne mentent"; every subject slot closed). Subject identities are
   not invented; elision vs postposing is open.
3. **Predecessor nominal readings are compatible-not-proven** for
   69/95/99 (only 65 is class-known). The bar tests admissibility,
   not proof of the suffix value.
4. **Arm-B uniformity untested.** If 13 is uniformly a leftward
   nominal-closing suffix, arm-B windows must re-segment too
   ("00=pour [13] 52" -> "pour-13"?; "45=ce [13] 55" -> "ce-13"?).
   That is a separate bar, recommended below — this promote covers
   arm A only.
5. No contradiction with standing red-team verdicts: dissolving arm A
   SUPPORTS §7's sole-polyvalence standing (67 et/veut untouched).

## Verdict: PROMOTE

All five arm-A windows admit the re-segmentation: 13 closes the
preceding nominal leftward (strongest at @1684 with promoted
65=noun class; cleanest clause at @1381 with 84=on + 92=verb;
complete NP at @1554 under 45=ce) and the verb-class successor
(24 x3, 93 x2) starts a new clause. The falsifier (bar b) found no
purchase — no window admits no boundary. The determiner/pronoun
polyvalence pressure on arm A dissolves without declaring a second
polyvalence: 13 is not a word here at all, it is a nominal-closing
suffix, and 24/93 belongs to the next clause. 13's value remains
sub-lexical (third arm); this promote establishes the segmentation,
not the suffix's gloss.

## Recommended follow-ups (for supervisor; verdict is promote)

1. **reseg-13-armB** (priority 3). Claim: the same leftward
   nominal-closing 13 re-segments all 7 arm-B windows
   (@139/@456/@481/@567/@575/@1166/@1360). Bars: (a) state the
   nominal closed leftward per window with standing values —
   hard cases "00=pour [13] 52" (@481) and "45=ce [13] 55"
   (@575/@1166); (b) any window forcing a word-level 13 kills the
   uniform-suffix account. Adverses: 66/52/92 class-open; 13's
   gloss still open.
2. **Escalate 24-en-verb-conflict to the red-team round** — this
   promote's three 24-legs are conditional on its resolution (see
   caveat 1). If 24='en' wins, reseg-13-armA must be re-opened.

## Reproducibility

All counts re-derived in-session from the repaired stream (1,847
pairs / 96 types asserted before testing); analysis ran session-local.
No writes outside this report, the queue edit, and the lockfile
(deleted).
