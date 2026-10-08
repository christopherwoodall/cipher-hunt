# Next-token findings: est-reexam (beat est-reexam, 2026-10-08)

Beat: est-reexam. Why: the crowd16 est-finder challenged the round-15 A1
grant. A1 granted "59->37" x6 as predicative frames. The est-finder says
all six are fenced leftovers (VOID). The related battery frame-37-reexam
must not decide this at battery level. This report is evidence for the
red team. It does not decide 37's value. It does not re-litigate the A1
grant. It does not promote.

## (a) Method

1. Parse the repaired 1,847-pair stream the lane way: data/
upstream-ct_R5005.txt with code/side-keyhunt/repaired_offsets.json, per
code/side-keyhunt/repair_parse.py. Never use code/side-keyhunt/
canonical.py (obsolete 1,846-pair parse).
2. Extract all 59 windows (+/-4 groups) from the repaired stream.
3. Re-derive each of the six 59->37 windows with @-offsets (the 59-cell's
0-based stream index). Same for the controls: "qui est 32" x2, 59->32 x3,
59->42 x2, "qui 37" x3 verb frames.
4. Check each 59-cell against code/crowd10/conditioner59/
classification.json (ISLET-10, round-10 R7 ruling). A window is a VALID
"est X" leg only if class(59)=EST: pre(59) in {64,94,93} and not fenced.
5. Verify every count the est-finder claimed. Note corrections.
6. Present both sides' evidence window by window. Give per-window
pass/fail on the ISLET-10 fencing claim. The red team decides.

Terms: ISLET-10 = round-10 law. 59 = word-"est" iff pre(59) is in
{64,94,93} ("qui est", "n'est", "l'est"). Unconditioned 59="est" is
REFUTED (kill-grade, round-10 R7(a)). ISLET-10's est-arm stands at LEAD
(round-10 R7(b)). S5 = the round-7 fence: the six 59->37 windows are
fenced on 37="le" MEDIUM (round-7 RULINGS-ROUND7; kept by round-10 R7(b)).
S5 was never re-litigated.

## (b) Per-window fencing analysis

All six 59->37 positions re-derived exact on the repaired stream:
@528, @624, @912, @1178, @1443, @1796. No other 59->37 window exists.
All six 7-mers are distinct (no formula double-count).

### Window 1: 59@528 (pre=44). Fencing claim: PASS (VOID).

Window: 81 97 47 44 [59] 37 64 26 32 (rows a3_00/a3_01).
Classification: LEFTOVER. Pre=44 is not in {64,94,93}. ISLET-10 gives 59
no licensed "est" reading here. Unconditioned 59="est" is kill-grade
refuted. The A1 "est [37]" reading has no standing law behind it at this
window. Note from classification.json: "'ce [44] [59] le qui' resists
both" — the fence was never re-litigated.

### Window 2: 59@624 (pre=14). Fencing claim: PASS (VOID).

Window: 37 76 82 14 [59] 37 33 29 87 (row a4_01).
Classification: LEFTOVER. Pre=14 not in {64,94,93}. Same as window 1:
no licensed est frame; unconditioned "est" refuted.

### Window 3: 59@912 (pre=83). Fencing claim: PASS (VOID).

Window: 54 49 64 83 [59] 37 96 09 02 (row a5_09).
Classification: LEFTOVER. Pre=83 not in {64,94,93}. No licensed est
frame. This window also carries the est-finder's anti-37="le" datum:
37@913 is followed by 96="par" (promoted), giving "37-96" = "le par" —
ungrammatical as article + "par". Single window. It strains 37="le"
(S5's foundation) but does not kill it alone (neighbors 83, 09 are
unresolved).

### Window 4: 59@1178 (pre=48). Fencing claim: PASS (VOID).

Window: 36 74 32 48 [59] 37 77 78 94 (row a6_10).
Classification: LEFTOVER. Pre=48 not in {64,94,93}. No licensed est
frame. Extra strain on the A1 side: round-15 A7 KILLED 48="est"
(distributional), so the predecessor here cannot be "est" either way.

### Window 5: 59@1443 (pre=68). Fencing claim: PASS (VOID).

Window: 85 01 52 68 [59] 37 64 77 84 (rows a7_08/a7_09).
Classification: LEFTOVER. Pre=68 not in {64,94,93}. No licensed est
frame.

### Window 6: 59@1796 (pre=94). Fencing claim: CONDITIONAL.

Window: 86 56 42 [94] [59] 37 91 79 87 (rows a8_09/a8_10). Stream
[1794:1798] = [42,94,59,37].
Classification: LEFTOVER, note: "S5-fenced (59->37): 'n'est le' era
10/3.96M (rare, not absent) - fence stands, NOT re-litigated".
This is the 7th pre-in-{64,94,93} window (round-10 R7(b) verified).
ISLET-10's conditioning LICENSES "n'est" here. The ONLY fence is S5,
which rests on 37="le" MEDIUM (round-7). The fencing claim holds IFF S5
stands. If the red team finds S5's foundation dead, this window becomes
the one valid "n'est [37]" leg.
Count note: @1795 is the 94-cell of THIS window, not a separate window.
A1's "+1 negated leg @1795" is a double-count. A1's own bar demanded
"independent = non-overlapping positions, not the same window viewed
twice". Verified: 6 unique windows, not 7.

Per-window fencing score: 5 PASS (VOID), 1 CONDITIONAL (@1796, turns on
S5).

### Controls

"qui est 32" x2 — both sides agree these are valid legs:
- 59@316 (pre=64): 78 45 64 [59] 32 94 06. Class EST. "qui est 32
[94] [06]". Verified.
- 59@1210 (pre=64): 61 21 65 64 [59] 32 48 96. Class EST. "qui est 32
[48] par" (96="par" promoted, favors past participle). Verified.

59->32 x3: @316 EST, @448 ESTE (pre=61, "on [61-59] [32]" frame-forced),
@1210 EST. A1 counted all three as legs. Under round-10 R7(b) F33
narrowing, pre=61 is EXCLUDED from the islet rule (fenced LEAD tier, not
an islet member). Valid est-legs for 32 under standing law: 2 (@316,
@1210). The 32 frame still stands on 2 legs.

59->42 x2:
- 59@463 (pre=11): 02 79 87 11 [59] 42 96 00 33. Class LEFTOVER.
"la/cela [59]": "la est" is era-0/3.96M, so 59 is not "est" here.
- 59@1186 (pre=06): 94 82 06 06 [59] 42 06 84 59. Class ESTE
("ne me [06-59] [42]"). Pre=06 is EXCLUDED from the islet rule per F33
(LEAD tier only).
Valid est-legs for 42 under standing law: 0. Both A1 legs are void.

59->19: single window @1777 (pre=64): 24 87 64 [59] 19 48 74. Class
EST. Both sides agree: 1 valid leg, HOLD. The round-15 "x2" was one
physical window (red team confirmed).

"qui 37" x3 verb frames (est-finder TIER-2, unfenced 37 evidence):
- 37@676: 24 80 03 64 [37] 77 45 23 09 — "qui 37 [77]..."
- 37@939: 00 33 21 64 [37] 01 07 50 40 — "qui 37-01" (A12 unit, 3x
@939/@1633/@1817, granted)
- 37@1633: 00 33 21 64 [37] 01 74 87 74 — "qui 37-01" again
37 sits in verb position after "qui" three times, twice feeding the
granted 37-01 unit. This is the est-finder's positive evidence that 37
is verb-class, independent of the est fight.

## (c) Verified counts vs the est-finder's claims

| Claim (est-finder) | Re-derived | Result |
|---|---|---|
| 59->37 = 6, @528/624/912/1178/1443/1796, no other | exact 6, same positions | CONFIRMED |
| class = LEFTOVER x6 | classification.json: LEFTOVER x6 | CONFIRMED |
| @1795/@1796 = one physical window [42,94,59,37] | stream[1794:1798] = [42,94,59,37] | CONFIRMED (A1 double-count corrected) |
| 59->32 = 3 @316/448/1210; valid EST = @316/@1210 | exact | CONFIRMED |
| 59->42 = 2 @463/1186; valid = 0 | exact | CONFIRMED |
| 59->19 = 1 @1777 (EST) | exact | CONFIRMED |
| 59->30 = 2 @559(EST)/@1715(ESTE) | exact | CONFIRMED |
| 59->39 = 2 (@763 EST, @1511 LEFTOVER); valid single | exact, both windows found | CONFIRMED (no error; "single" = valid legs) |
| 59->45 = 1 @103 (EST) | exact | CONFIRMED |
| 59->35 = 3: @834 LEFTOVER, @1291 FENCED, @1804 ESTE | exact | CONFIRMED |
| EST-class keys exactly {103,316,559,763,1210,1777} | classification.json has exactly these 6 | CONFIRMED |
| n59 = 27; 27 classification keys | 27 pairs; 27 keys | CONFIRMED |
| 37-01 x3 @939/@1633/@1817 (not x2) | exact x3 | CONFIRMED (finder's own correction holds) |
| 37-78 x4 @312/@414/@475/@1770 (not x2) | exact x4 | CONFIRMED (finder's own correction holds) |
| "qui 37" x3 @676/@939/@1633 | 64->37 starts @675/@938/@1632 | CONFIRMED |
| 64->32 direct x2 @32/@854 | exact | CONFIRMED |
| 26->32 x2, 56->32 x2, 91->32 x2, 32->48 x4 | @129/@531, @1282/@1571, @247/@256, @449/@855/@1176/@1211 | CONFIRMED |
| "52-37" x3 | stream shows x4 (@1124/@1129/@1356/@1722), all distinct | CORRECTION: x4, not x3 (minor; no verdict effect) |

No other count errors found. The est-finder's arithmetic is clean.

## (d) Evidence for red-team adjudication

The conflict, stated plainly:

SIDE A (round-15 A1, red-team confirmed): six 59->37 windows are
predicative frames "est [37]". Bar: (a) >=2 independent "est X" windows
(est=59 conditioned frame); (b) adjective-compatible successors; (c)
zero windows forcing a non-adjective reading. A1's red team re-derived
all six positions and granted the frame, with 42 named weakest.

SIDE B (crowd16 est-finder + est battery): ISLET-10 (standing law since
round 10) licenses word-"est" only for pre(59) in {64,94,93}. Five of the
six windows have pre in {44,14,83,48,68} — no licensed est frame, and
unconditioned 59="est" is kill-grade refuted (round-10 R7(a)). The sixth
(@1796, pre=94) is licensed but S5-fenced. Result: 37 has ZERO valid
"est" legs; the frame should be DEMOTED to HOLD (not killed — A1's
clause (b) successor evidence survives as unanchored distributional
evidence).

What this re-exam establishes on the repaired stream:
1. Both sides' WINDOW counts are correct (6 windows, same positions).
2. The ISLET-10 partition applies as the est-finder says: 5 windows are
unlicensed-pre LEFTOVER; only @1796 is a licensed-pre window.
3. The round-15 A1 battery and its red team never checked the six legs
against classification.json. The standing registry already partitioned
est=6 (@103/@316/@559/@763/@1210/@1777) + @1796 S5-fenced + S5-fenced x6
before A1 ran. This is a scope gap of the same kind the round-15 red
team flagged in A15 (the 62="on" collision). The red team must decide
whether the gap voids A1's clause (a).
4. A1's "+1 negated leg @1795" violates A1's own independence clause
(non-overlapping positions). 6 unique windows, not 7. Verified.
5. A1's 32-count (3) includes @448 (pre=61), which round-10 R7(b) F33
excludes from the islet rule. Valid 32 legs under standing law: 2
(@316, @1210). The 32 frame survives on 2 legs.
6. A1's 42-count (2) includes @463 (LEFTOVER) and @1186 (pre=06,
F33-excluded). Valid 42 legs under standing law: 0. The 42 demotion to
HOLD follows from standing law alone, no new evidence needed.
7. @1796 is the ONLY window where the disagreement turns on a live
fence (S5), not on arithmetic. S5 rests on 37="le" MEDIUM (round-7).
The sole datum against 37="le" on record is the @913 "le par" window
(37-96 adjacent, 96="par" promoted) — real tension, single window,
neighbors unresolved. Not kill-grade on its own.
8. Independent positive evidence for 37's class exists outside the est
fight: "qui 37" x3 verb frames (@676/@939/@1633), the granted 37-01
unit x3, 37-78 x4. The est-finder's verb-stem/syllable lead is real
evidence; it is not adjudicated here.

The red team's decision points:
- D1: Does the ISLET-10 scope gap void A1's clause (a) for 37 (6 -> 0
valid legs: DEMOTE to HOLD) and 42 (2 -> 0: DEMOTE to HOLD)?
- D2: Does S5 stand on @1796? If S5 falls, @1796 is the 7th est-arm leg
("n'est [37]") and 37 holds 1 valid leg (still HOLD under A1's bar,
which needs >=2).
- D3: 32's frame stands on 2 valid legs either way; the adjective/verb
tension (64/26/56/91->32) goes to the class battery.

## (e) Follow-up batteries for the supervisor queue

1. **s5-foundation (37="le" MEDIUM under test)**. Claim: 37 is not
article-"le". Bars: (a) >=2 of 37's 28 windows where a "le" reading
forces ungrammatical French, with named parses; (b) the @913 "le par"
window re-derived with neighbor analysis (83, 09); (c) ZERO windows
requiring 37="le". Priority: 1 (gates @1796 and the S5 fence).
Evidence: @913 (37-96="le par"), "qui 37" x3 verb frames,
37-78 x4, 37-01 x3. Adverses: S5 standing fence (37="le" MEDIUM,
round-7); A12 37-01 unit grant ("certain" cer-tain compatibility, not
proof).

2. **1796-conditional (7th est-arm leg)**. Claim: @1796 is a valid
"n'est [37]" est-arm leg. Bars: (a) red team lifts S5 (this battery is
BLOCKED until D2 is decided — do not run before); (b) successor-91
profile compatible with the predicative class (@316/@1210 successors);
(c) no window contradicts. Priority: 2 (gated). Evidence: window
@1792-1800 "42-94-[59]-37-91-79"; ISLET-10 licensing (pre=94).
Adverses: classification.json "n'est le era 10/3.96M" rarity note;
round-10 R7(b) exclusion.

3. **classification-sweep (independent re-derive)**. Claim: the 27-window
classification.json partition re-derives from the repaired stream
without trusting the file. Bars: (a) all 27 59-cells classified from
pre/successor cells alone, blind to the file; (b) >=26/27 agreement
with classification.json; (c) any disagreement named with window
evidence. Priority: 3. Evidence: n59=27 census; pre census
{64x3, 94x3, 93x1, 84x4, 06x2, 61x2, 44x2, ...}. Adverses: none — this
is a guard battery; a null keeps the current partition.

---

Lock/status: finder beat est-reexam. Report filed. No verdicts changed.
No R5005 touched. No sealed gates touched. No promotions made.
