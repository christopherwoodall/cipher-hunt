# Battery report: seg-55-re-prefix

Target: `seg-55-re-prefix`. Claim: test 55="re" as a verbal prefix independent of the prenne claim.
Date: 2026-10-09. Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`). `canonical.py` never used. R5005, sealed gates, red-team queue untouched. Lock created on start, deleted on completion.

## Bar (verbatim from queue)

"(a) census the corrected 6 x 55-81 bigram windows (@25, @523, @550, @1085, @1094, @1671) plus the 2 x 55-83 and 1 x 55-68 windows; (b) demonstrate 55 as a prefix in ≥2 distinct stems where a \"re-\" reading yields a grammatical French verb and a rival reading breaks; (c) keep 81=\"prin\" kill intact"

## Bar restated as numbered clauses

- C1: census the 6 x 55-81 windows (@25, @523, @550, @1085, @1094, @1671), the 2 x 55-83 windows, and the 1 x 55-68 window — byte-exact on the repaired stream.
- C2: demonstrate 55 as a "re-" prefix in ≥2 distinct stems, each yielding a grammatical French verb where a rival (non-"re") reading breaks.
- C3: the standing 81="prin" kill is not revived or weakened.

## C1 — census (PASS)

Re-derived on the repaired stream. 55 occurs n=12 total. Followers: 81 x6, 61 x3, 83 x2, 68 x1. All brief @-offsets confirmed byte-exact:

55-81 x6:
- @25 [a1_00]: `43 29 47 33 55 81 00 34 24`
- @523 [a3_00]: `70 91 77 06 55 81 97 47 44`
- @550 [a3_01]: `46 24 47 46 55 81 00 86 59`
- @1085 [a6_05]: `52 89 24 02 55 81 00 33 79`
- @1094 [a6_06]: `80 06 43 07 55 81 06 29 67`
- @1671 [a8_05]: `06 91 11 78 55 81 92 60 03`

55-83 x2:
- @906 [a5_09]: `67 16 88 18 55 83 54 49 64`
- @1611 [a8_03]: `92 65 23 08 55 83 71 48 31`

55-68 x1:
- @1285 [a7_03]: `61 56 32 98 55 68 00 11 17`

(55-61 x3 also exists: @576, @1167, @1205 — out of the bar's scope but noted.)

Adverse check: the "55-81-00 x5" misread is corrected — the bigram 55-81 is x6; the trigram 55-81-00 is x3 (@25, @550, @1085), not x5.

## C2 — prefix demonstration (FAIL)

Tested each 55-window for a "re-"+stem reading yielding a grammatical French verb. Known values used: 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que (GT); 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce (granted); 59=est, 77=le (provisional); 06=ent (promoted); 98='vient' (battery); 83='de' conditioned on 98-lead (battery).

- @906 `18 55 83 54 49 64` ("[18] re[83] [54] [49] qui", 64=qui GT): best leg. With 83="gar": "[18] regarder [54] [49] qui" — a grammatical verb frame. But 83="gar" is unstated (1 assumption), [54][49] as a noun phrase is unstated (1 assumption), and the rival (non-"re") reading cannot be shown to break because 83 is unvalued outside the 98-conditioned 'de' windows. Leg-grade only, not demonstration.
- @1611 `08 55 83 71 48 31` ("[08] re[83] [71] e[31]", 48=e GT): same stem candidate (83="gar" → "regarder"), weaker frame. Not a demonstration.
- @1285 `98 55 68 00 11 17` ("vient re[68] pour la fois", 98='vient' battery, 00=pour, 11=la, 17=fois): no "re-" infinitive yields a grammatical window — "vient reprendre/revoir pour la fois" fails on "pour la fois" (needs "pour la première fois" or similar) and on "vient"+bare-infinitive. Strain is in the frame, not kill-grade for "re".
- @25 `43 29 47 33 55 81 00 34 24` ("er ce [33] re[81] pour i [24]"): "re[81] pour" — no candidate stem (pren/ven/met/tour/gard/part) yields "re-X pour" + infinitive grammatically. FAIL.
- @523 `70 91 77 06 55 81 97 47 44` ("le ent re[81] [97] ce [44]"): "le"+"ent" left block unparseable under any "re-" stem. FAIL.
- @550 `46 24 47 46 55 81 00 86 59` ("que [24] ce que re[81] pour [86] est"): "repartir pour [86]" (81="part") is the only near-grammatical candidate but needs 81="part" unstated AND 86 noun-shaped unstated. FAIL.
- @1085 `52 89 24 02 55 81 00 33 79` ("[02] re[81] pour [33] tout"): same "pour" failure. FAIL.
- @1094 `80 06 43 07 55 81 06 29 67` ("[07] re[81] ent er [67]", 06=ent, 29=er GT): 81="gard" → "regardent" is a real word, but the tail "er et/veut" is ungrammatical; 81="pren" → "reprennent" needs the clerk single-consonant spelling AND still fails the tail. FAIL.
- @1671 `06 91 11 78 55 81 92 60 03` ("[78] re[81] [92] [60] [03]"): "recevoir"/"revenir" segmentations (81="cev"/"ven", 92="oir"/"ir") conflict with the 92-29="[92]er" hapax ("oirer"/"irer" not words). FAIL.

Result: at most ONE leg-grade stem (83="gar" → "regarder" @906), and it does not meet the bar's "demonstrate ... and a rival reading breaks" standard. No second stem survives. C2 FAILS.

## C3 — 81="prin" kill intact (PASS)

The kill was never touched: no "prin" reading was proposed for 81 at any window. (Note: 81="pren" as a "reprendre" stem was considered and rejected on window grammar, not promoted; "pren" ≠ killed "prin" and the distinction is preserved.)

## Verdict: NULL

C1 PASS, C2 FAIL, C3 PASS. Failures are epistemic (cannot demonstrate), not falsifications: no window forces 55≠"re", so this is not kill-grade. The "re" reading remains untested as a global value.

## Adverses answered

- "55='re' untested" — still untested at battery grade; this report is the first test and it is inconclusive.
- "55-81-00 x5 misread corrected to bigram x6" — confirmed: bigram x6 exact; trigram 55-81-00 is x3 (@25, @550, @1085).

## Follow-ups for supervisor queuing

1. `re83-gar-test` (P2): test 83="gar" ("regarder" @906/@1611) against the full 83 census (n=15), keeping the 98-conditioned 'de' windows (@228/@898/@931/@1061/@1784) intact or showing a conditioned split; promote 83="gar" iff all non-'de' windows parse with ≤1 unstated assumption, kill iff any window forces otherwise.
2. `re61-son-test` (P2): test 61="son" — "resonnement" @576 (`55 61 94 82 06` = re-son-ne-m-ent, cf. rare noun "resonnement") and "resonne" @1167 (`55 61 94` = "résonne", 3sg of résonner) — against the full 61 census (n=18); decides whether 55-61-94 is a word unit.
3. `re81-stem-elim` (P3): eliminate candidate 81 stems (tour/pas/gard/met/ven/part) across all six 55-81 windows with the 81="prin" kill intact; kill 55="re" iff no stem survives any window, or name the surviving stem for a re-test.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-seg-55-re-prefix.md`
- Queue: `seg-55-re-prefix` → status `verdict`, result `null`, date 2026-10-09 (temp-file + rename; pre-write assert confirmed queued/verdictless).
- Lock deleted on completion.
