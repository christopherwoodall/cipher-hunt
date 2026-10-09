# Battery report: adj-frames-995-637 (adjective-arm frames @995 + @637)

Worker: df123f01-5a52-4531-937e-25f30f767a54. Date: 2026-10-08.
Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt), parsed per code/side-keyhunt/repair_parse.py.
canonical.py never used. R5005 never touched. @i = 0-based pair index.
No red-team verdict on 60 exists (checked
code/crowd15/report_inbox/next-token-redteam.md) — no contradiction, no
escalation of a standing verdict. This is a FRAME battery: 60's value is
not named; verb-60's bar is not re-litigated; adj-60's four bar frames
(@454/@690/@1644/@1674) are not duplicated.
No prior lock on adj-frames-995-637 (no stale lock to note).

## Bar (verbatim, pre-registered before testing)

"promote-frame iff both @995 '03 60 et' and @637 'que 60 et' parse as postnominal/coordinated adjective with 03 nominal (independently supported) + zero contradictions"

Numbered clauses (fixed before data examination):

1. (C1) @995 '03 60 67' parses as "[03-N] [60-adj] et[67]" — postnominal
   adjective, with 03 nominal.
2. (C2) @637 '46 60 67' parses as "que[46] [60-adj] et[67] le[77] [89]" —
   coordinated adjective.
3. (C3) 03 is nominal on independent evidence: 'le [03]' @722,
   'ce [03]' @1014/@1790 via granted 47='ce'.
4. (C4) Zero contradictions.

## Method

Fresh parse per protocol. No prior counts trusted (all numbers below are
re-derived). Standing values used: 11='la', 46='que', 82='m', 29='er',
40='e' (banked); 87='ce', 64='qui', 96='par', 00='pour', 47='ce' (A4),
94='ne' (battery), 12='n'/48='e' letters (battery), 06='ent' (battery),
30='pas' (battery), 39='a' (battery); 77='le' (provisional); 67 positional
rule per §7 (67='veut' iff follower infinitive-shaped, else 67='et').

## Window-level evidence

W1 — @995 '03 60 67' (row a6_01):
@993 30 @994 03 @995 60 @996 67 @997 11 @998 96 @999 82 @1000 33 @1001 00
Reads: "pas[30] [03] [60] et[67] la[11] par[96] me[82] [33] pour[00]..."
Local frame: "[03] [60] et la". Under 03 nominal + 60 adjectival:
"[ne] pas [03-N] [60-adj] et la ..." — postnominal adjective, the normal
French position ("not [03-N] [60-adj] and the ..."). 67='et': follower
@997=11='la' is banked, not infinitive-shaped, so the positional rule
gives 'et' cleanly. Uniqueness on the repaired stream: '03 60 67' x1,
'60 67' x2 (@995 and @637 only), '03 60' x1 (@995 only). PASS as frame.

W2 — @637 '46 60 67' (row a4_01):
@635 74 @636 46 @637 60 @638 67 @639 77 @640 89 @641 48 @642 20
Reads: "[74] que[46] [60] et[67] le[77] [89] e[48] [20]..."
Local frame: "que [60] et le [89]e". 67='et': follower @639=77 is
article-like (provisional 'le'; 77 n=44, article-shaped follower profile,
never infinitive-shaped), so the positional rule gives 'et' cleanly.
Attempted coordinated-adjective parse: "que [60-adj] et le [89-adj]"
(with 89 substantivized). BLOCKED at battery level: 89 is verb-framed
per red-team A8 ("ce le [80/89]" verb frames); '89 48' x3 (@640/@871/@986)
reads "[89]e" with 48='e' letter — verb-3sg-shaped, matching the A8 frame
"ce le [89]e" @869-872; 29='er' precedes 89 x5. An adjective-shaped 89
needs red-team-declared polyvalence (per §7, 67 et/veut is the sole true
polyvalence) — not available at battery level. The window stays strained
(as found in battery-adj-60). Fenced with cause, not ignored.

Anchors — 03 nominal, re-derived, independent of the bar frames:
- 'ce [03]' @1014 (row a6_02): '1013:47 1014:03 1015:24' — 47='ce' is
  A4-granted.
- 'ce [03]' @1790 (row a8_09): '1789:47 1790:03 1791:00' — same.
- 'le [03]' @722 (row a5_02): '721:77 722:03 723:91' — 77='le' is
  provisional (flagged, not load-bearing alone).
- '87 03' x0 on the stream — the 47='ce' attribution is correct.
- '03 64' x4 — relative 'qui' (64 granted) needs a nominal antecedent.
- Bonus: '30 03 64' @30-32 = "pas [03] qui" — nominal under 'pas'.

67-rule corroboration (adverse A1): '67 77' x6 (@506/@638/@743/@1239/
@1400/@1597) and '67 11' x4 (@561/@669/@753/@996) — every instance reads
naturally as 'et' ("et le", "et la" coordinations); no follower is
infinitive-shaped (followers are literally 77/11). Fenced: a 'veut'+NP-
object reading is conceivable at @638 ("veut le [89]") but excluded by
the standing iff-rule; rule revision is red-team-only per §7.

Zero-contradiction scan: adj-60's K1/K2 (@1338/@700 force 60 verbal) are
value-level, at other windows — fenced, not frame contradictions (this
battery promotes frames, not 60's value; the polyvalence question is
queued as poly-60-redteam). No standing verdict contradicts the @995
frame — battery-adj-60 explicitly records @995 as adjective-arm support.
No window forces a non-adjective parse at @995. Note: @995 sits inside
verb-60's V3 window list (queued, undecided) — coordination note, not a
contradiction; this battery does not re-litigate verb-60's bar.

## Per-clause pass/fail

- C1: PASS. @995 parses cleanly as "[03-N] [60-adj] et[67] la[11]"
  postnominal; 67='et' by the positional rule; frame unique on stream.
- C2: FAIL (battery-level block, not kill grade). The coordinated-
  adjective parse needs 89 adjective-shaped; standing A8 frames 89 as
  verb-slot (red-team grant). Only the red team can declare the needed
  polyvalence per §7. No window forces the frame false, and the cleaner
  verb rival ("que [60-V] et le [89-V]e") carries its own subject gap —
  so this is inconclusive, not refuted.
- C3: PASS. 'ce [03]' x2 @1014/@1790 via granted 47='ce' carries the
  independent nominal support; 'le [03]' @722 (provisional 77) and
  '03 64' x4 corroborate; '87 03' x0 keeps attribution clean.
- C4: PASS. Zero contradictions of the frame claims (K1/K2 fenced as
  value-level; A8 tension scored under C2, not double-counted).

Adverses answered:
- A1 (load-bearing on the 67 positional rule): answered — rule applies
  cleanly at both windows (followers 11 banked / 77 article-like, neither
  infinitive-shaped); '67 77' x6 + '67 11' x4 corroborate; 'veut'+NP
  alternative fenced with stated cause (needs red-team rule revision).
- A2 (does not duplicate the four bar frames): answered — @995/@637 are
  disjoint from @454/@690/@1644/@1674; verb-60's bar untouched; 60's
  value unnamed.

## Verdict

**null** — C1, C3, C4 pass: the @995 postnominal-adjective frame holds
with independently supported 03-nominal anchors and zero contradictions.
C2 fails at battery level: @637's coordinated-adjective parse is blocked
by standing A8 (89 verb-framed) and needs a red-team ruling on 89's
class/polyvalence. Not kill: no window forces the @637 frame false; the
frame is unpromotable now, not refuted. Work regenerates below.

## Follow-ups (work regenerates)

1. **adj-frame-995-solo** (priority 2): narrow re-bar on @995 alone.
   Bar: "promote-frame iff '03 60 67' @995 parses as '[03-N] [60-adj]
   et[67] la[11]' postnominal with 03 nominal independently supported
   ('ce [03]' x2 @1014/@1790 via granted 47='ce'; 'le [03]' @722;
   '03 64' x4; 'pas [03] qui' @30) + zero contradictions."
   Adverses: none beyond the 67 rule (follower 11='la' banked).
   Evidence: C1/C3/C4 pass in this report; '03 60 67' unique on the
   repaired stream; feeds poly-60-redteam.
2. **coord-637-89gate** (priority 2): gated re-test of @637's
   coordinated-adjective parse, gated on a red-team ruling on 89.
   Bar: "resolve iff red team declares 89 adjective-compatible (or
   adjective/verb polyvalence with a positional rule); then re-parse
   'que [60-adj] et le [89-adj]' @637 with zero contradictions."
   Adverses: A8 verb-frame stands until red team moves; do not
   re-litigate A8 at battery level.
   Evidence: A8 "ce le [89]" verb frames vs '89 48' x3 "[89]e";
   29='er' before 89 x5; parse fully specified in this report, blocked
   only on 89's class.
3. **verb-coord-637** (priority 3): test @637 as verb coordination.
   Bar: "resolve iff 'que [60-V] et le [89-V]e' @637 parses with 74's
   class stated and both verbs' subjects identified + zero
   contradictions; else fence with cause."
   Adverses: subject gap unresolved; coordinate with verb-60 (queued).
   Evidence: '89 48' x3 verb-3sg-shaped; A8 verb-frame; discriminates
   60's class at this window; feeds the verb arm of poly-60-redteam.
