# Bedrock validation — 70 row offsets, Seebach lane

Date: 2026-10-08. Scope: `code/side-keyhunt/repaired_offsets.json` (70 binary
pair-phase offsets). Method: primary-source evidence only. Read-only: no
stream files rewritten.

## Overall verdict: STANDS WITH CAVEATS

The 1,847-pair stream does NOT require rebuild. Mechanics verified (concur
with `code/bedrock/` fleet: 70 rows, 3,764 digits, 1,847 pairs, 96 groups,
C1 convention forced by (3764−2·1847)=70, carry-over alternative falsified at
1,866 pairs). No offset is definitively falsified. Two offsets flagged for
red-team adjudication (do NOT flip without adjudication).

## The two conditional assumptions — re-graded

1. "Pencil gloss belongs to row a5_03": PROBABLE. The 12-digit crib
   `117082342940` occurs exactly twice raw (1532, 2108); the gloss lands
   exactly on the repaired occurrence (pair 754, row a5_03). Direct check
   needs manuscript images (not in lane). Alternative (mislabeled line +
   ~1e-9 coincidence) rejected per `methodology-ruling.md` R1.
2. "68 of 70 offsets unvalidated": SUPERSEDED. 6 offsets now rest on
   primary/repeat evidence (below). 64 rest on EM statistics with
   leave-one-out robustness grades (table below).

## Offsets confirmed by primary evidence (6)

| Row | Off | Evidence |
|-----|-----|----------|
| a5_03 | 0 | Gloss (i): "la pre m i er e" over 11-70-82-34-29-40. `repair_parse.py` asserts. |
| a8_05 | 1 | Gloss (ii): ends 46="que". Row len 55; off 1 gives last pair digits[53:55]="46". Bedrock verifier B: pair 1692. |
| a6_03 | 0 | Crib repeat: `117082342940` at in-row 28 (even) → pair-aligned under off 0 as second "la première" (pair 1034). Byte-identical to gloss-confirmed occurrence. |
| a2_01 | 1 | Formula repeat: `9883829621` at in-row 21; (21−1)=20 even → 98-83-82-96-21 ("vient de me parvenir" stem + 60-homophone). Off 0 would misalign. Forced. |
| a6_04 | 1 | Same formula at in-row 31; (31−1)=30 even → 98-83-82-96-21 + 62-homophone. Forced. |
| a8_09 | 0 | Same formula at in-row 24; (24−0)=24 even → 98-83-82-96-21 + 68-homophone. Forced. |

The 3-occurrence formula alignment is the strongest independent check: one
10-digit string, three rows, three different offsets (1,1,0), all pair-aligned
as the same five groups. P(chance) ≈ 0.

## Flagged for red-team adjudication (2) — do NOT flip

| Row | Off | Issue |
|-----|-----|-------|
| a4_01 | 1 | Repeat `7778948206` (4×) pair-aligned as 77-78-94-82-06 in a6_10/a7_05 but not here. Two coherent readings exist (one formula 4× → off 0; two formulas 2× each → off 1 stands). LOO supports off 1 (+7.02). Ambiguous. |
| a5_07 | 1 | Same repeat, same ambiguity. LOO supports off 1 (+6.51). Ambiguous. |

## Per-offset grades (64 EM-estimated rows)

Grades: CONFIRMED (above) / PROBABLE (LOO margin >+5 nats) /
PROBABLE-WEAK (LOO +2..+5) / UNRESOLVED (|LOO| ≤2, or LOO-negative, or
repeat-ambiguous). LOO = leave-one-out pair-frequency log-likelihood margin
for the EM choice; positive supports it. No row graded CONTRADICTED:
LOO is proven unreliable for overturning (it contradicts formula-confirmed
a8_09 at −4.21 nats; the gloss overruled EM on a5_03 at −7.17).

Counts: CONFIRMED 6, PROBABLE 24, PROBABLE-WEAK 15, UNRESOLVED 25
(15 weak + 8 LOO-negative + 2 flagged).

| Row | Len | Off | LOO | Grade |
|-----|-----|-----|-----|-------|
| a1_00 | 70 | 0 | +7.89 | PROBABLE |
| a1_01 | 71 | 0 | +6.49 | PROBABLE |
| a1_02 | 65 | 0 | +7.45 | PROBABLE |
| a1_03 | 63 | 0 | +2.19 | PROBABLE-WEAK |
| a1_04 | 58 | 1 | +8.33 | PROBABLE |
| a1_05 | 59 | 1 | +4.36 | PROBABLE-WEAK |
| a2_00 | 55 | 0 | +5.57 | PROBABLE |
| a2_01 | 56 | 1 | +6.36 | CONFIRMED (formula) |
| a2_02 | 54 | 0 | −1.46 | UNRESOLVED |
| a2_03 | 54 | 1 | +8.20 | PROBABLE |
| a2_04 | 54 | 0 | −3.99 | UNRESOLVED (LOO-neg; not overturning) |
| a2_05 | 54 | 0 | −3.35 | UNRESOLVED (LOO-neg; not overturning) |
| a2_06 | 51 | 0 | −0.26 | UNRESOLVED |
| a2_07 | 50 | 1 | +6.03 | PROBABLE |
| a2_08 | 50 | 1 | +7.83 | PROBABLE |
| a2_09 | 54 | 0 | −3.85 | UNRESOLVED (LOO-neg; not overturning) |
| a2_10 | 53 | 0 | +4.38 | PROBABLE-WEAK |
| a2_11 | 51 | 0 | +0.18 | UNRESOLVED |
| a3_00 | 58 | 0 | −0.11 | UNRESOLVED |
| a3_01 | 55 | 0 | +4.72 | PROBABLE-WEAK |
| a3_02 | 64 | 0 | −2.36 | UNRESOLVED (LOO-neg; not overturning) |
| a4_00 | 56 | 0 | −1.69 | UNRESOLVED |
| a4_01 | 52 | 1 | +7.02 | UNRESOLVED-FLAG (repeat ambiguous) |
| a4_02 | 51 | 0 | +5.01 | PROBABLE |
| a5_00 | 53 | 1 | +4.31 | PROBABLE-WEAK |
| a5_01 | 55 | 1 | +3.15 | PROBABLE-WEAK |
| a5_02 | 54 | 0 | −1.63 | UNRESOLVED |
| a5_03 | 52 | 0 | −7.17 | CONFIRMED (gloss i; LOO reproduces known EM error) |
| a5_04 | 52 | 0 | −1.13 | UNRESOLVED |
| a5_05 | 52 | 1 | +6.11 | PROBABLE |
| a5_06 | 52 | 1 | +6.76 | PROBABLE |
| a5_07 | 50 | 1 | +6.51 | UNRESOLVED-FLAG (repeat ambiguous) |
| a5_08 | 53 | 1 | +4.40 | PROBABLE-WEAK |
| a5_09 | 50 | 1 | +12.95 | PROBABLE |
| a5_10 | 49 | 0 | +5.34 | PROBABLE |
| a6_00 | 50 | 1 | +6.26 | PROBABLE |
| a6_01 | 50 | 1 | +4.56 | PROBABLE-WEAK |
| a6_02 | 50 | 1 | +12.05 | PROBABLE |
| a6_03 | 50 | 0 | +6.06 | CONFIRMED (crib repeat) |
| a6_04 | 51 | 1 | +4.11 | CONFIRMED (formula) |
| a6_05 | 46 | 1 | +10.66 | PROBABLE |
| a6_06 | 44 | 1 | +7.66 | PROBABLE |
| a6_07 | 41 | 0 | +5.22 | PROBABLE |
| a6_08 | 40 | 0 | +0.99 | UNRESOLVED |
| a6_09 | 41 | 0 | +2.45 | PROBABLE-WEAK |
| a6_10 | 38 | 1 | +8.44 | PROBABLE |
| a7_00 | 58 | 1 | +8.44 | PROBABLE |
| a7_01 | 60 | 1 | +10.23 | PROBABLE |
| a7_02 | 57 | 0 | +3.18 | PROBABLE-WEAK |
| a7_03 | 60 | 1 | +8.03 | PROBABLE |
| a7_04 | 55 | 0 | +0.07 | UNRESOLVED |
| a7_05 | 55 | 0 | −0.85 | UNRESOLVED |
| a7_06 | 57 | 1 | +2.57 | PROBABLE-WEAK |
| a7_07 | 56 | 0 | −0.50 | UNRESOLVED |
| a7_08 | 56 | 1 | +9.97 | PROBABLE |
| a7_09 | 57 | 1 | +5.15 | PROBABLE |
| a7_10 | 55 | 0 | +4.66 | PROBABLE-WEAK |
| a7_11 | 56 | 0 | −0.21 | UNRESOLVED |
| a8_00 | 58 | 1 | +3.80 | PROBABLE-WEAK |
| a8_01 | 57 | 0 | +2.17 | PROBABLE-WEAK |
| a8_02 | 58 | 0 | −1.48 | UNRESOLVED |
| a8_03 | 57 | 1 | +4.59 | PROBABLE-WEAK |
| a8_04 | 57 | 1 | +1.95 | UNRESOLVED |
| a8_05 | 55 | 1 | +1.97 | CONFIRMED (gloss ii) |
| a8_06 | 52 | 0 | −4.55 | UNRESOLVED (LOO-neg; not overturning) |
| a8_07 | 52 | 0 | +1.22 | UNRESOLVED |
| a8_08 | 52 | 0 | −7.54 | UNRESOLVED (LOO-neg; not overturning) |
| a8_09 | 50 | 0 | −4.21 | CONFIRMED (formula; LOO wrong here) |
| a8_10 | 52 | 0 | −3.03 | UNRESOLVED (LOO-neg; not overturning) |
| a8_11 | 51 | 0 | −0.42 | UNRESOLVED |

## Offsets that must be corrected

NONE definitively. a4_01 and a5_07 are flagged (not falsified) — red-team
adjudication required before any flip. `repaired_offsets.json` left untouched
per task constraints.

## Notes for downstream users

- The 21 even-length rows with offset 1 (each drops 2 digits) are NOT
  transcription errors: the formula repeat forces a2_01=1 and a6_04=1 on
  even-length rows. Even+1 is a real phenomenon in this transcription.
- Within-block phase propagation holds for only 33/62 consecutive line pairs
  (≈ chance). Lines are pair-phase independent; do not assume reading order
  from file order.
- Systematic 10-digit repeat scan: all genuine multi-occurrence formulas
  (3/3, 2/2 cases) are pair-aligned under current offsets except the
  ambiguous `7778948206` (2/4). No other offset is implicated.
- EM error rate: 1 proven error in 70 (a5_03, corrected by gloss). LOO
  cannot reliably find more; do not re-run EM flips without manuscript
  evidence.
