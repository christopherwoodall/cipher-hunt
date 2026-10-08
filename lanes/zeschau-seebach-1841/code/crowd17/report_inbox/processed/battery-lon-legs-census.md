# Battery report: lon-legs-census — 7 'l'on' legs re-derived; @146 fenced R3

- Target: `lon-legs-census`
- Claim: re-derive all 7 'l'on' legs under post-collision unconditioned 84='on'; @146 fenced as residual R3 alongside R1/R2
- Verdict: **promote** (claim confirmed; no value promoted; no standing verdict changed)
- Date: 2026-10-08
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed like code/side-keyhunt/repair_parse.py).
  canonical.py never used. R5005 untouched.
- Lock: locks/lon-legs-census.lock (created on start, deleted on completion).

## 1. Pre-registered bar (verbatim)

> re-derive all 7 legs on the repaired stream; record @146 as fenced R3 alongside R1/R2

Numbered pass/fail clauses (frozen before testing; not modified after seeing data):

1. **C1 — re-derive all 7 'l'on' legs** (@145/259/1057/1446/1484/1763/1802) on
   the repaired stream with 84='on' unconditioned.
2. **C2 — grade each leg's dependence** on provisional 77='le' (A15-C1 inheritance).
3. **C3 — record @146 as fenced R3** alongside fenced R1 (@1619) and R2 (@1664).

## 2. Method

Re-parsed in this run from repaired_offsets.json + upstream-ct_R5005.txt
(byte-exact rule from repair_parse.py). n=1,847 pairs; n(84)=25; n(77)=44.
Enumerated every 77-84 bigram stream-wide. No numbers inherited from prior
reports; all counts below are this run's.

## 3. Window-level evidence

- **77-84 bigrams stream-wide: exactly 7**, at @145/259/1057/1446/1484/1763/1802.
  Offsets match the A15 red-team re-derivation byte-for-byte. No other 77-84
  bigram exists.

Leg table (leg @ = 77 position; 84 follows at @+1):

- **@145** (row a1_04): pre-77=64 ('qui'); 84->29. Read: "qui l'on [29]".
  Holds the R3 anomaly (see §4).
- **@259** (row a2_02): pre-77=43; 84->74. Read: "[43] l'on [74]".
- **@1057** (row a6_04): pre-77=23; 84->09. Read: "[23] l'on [09]".
- **@1446** (row a7_09): '64 77 84 59 36' = "qui l'on est [36]".
- **@1484** (row a7_10): '46 77 84 24 87' = "que l'on [24] ce [87]"
  (A15's en-arm leg, byte-identical).
- **@1763** (row a8_08): pre-77=06; 84->09. Read: "[06] l'on [09]".
- **@1802** (row a8_10): '87 64 77 84 59 35' = "ce qui l'on est [35]".

- **Twin legs**: @1446 and @1802 are the same '64 77 84 59' frame
  ("qui l'on est"), differing only in the tail cell (36 vs 35). The same frame
  shape takes the same 84 reading in two windows. This strengthens the census.
- **84 successor census** (re-derived, sums to n(84)=25): 59 x4, 24 x3, 02 x2,
  92 x2, 09 x2, 29 x1, 26 x1, 53 x1, 74 x1, 91 x1, 73 x1, 51 x1, 06 x1, 79 x1,
  33 x1, 78 x1, 64 x1. Matches the A15 "84→59 ×4, 84→24 ×3". The two 84->59
  legs are 2 of the 4 "on est" windows. Every successor is 'on'-compatible
  except 29 (the R3 anomaly, unique x1).
- **Dependence grade (A15-C1)**: every leg's "l'on" reading needs 77='le'
  (provisional) for the elided 'l'. If 77 falls, the legs fall. The value is
  carried by 77-independent legs ("qu'on en" x2, "mon"@166, 82-84 @166) —
  the 84='on' grant does not rest on this census.

## 4. R3 fence record (joins fenced R1/R2)

- **R1** (A15-C3, confirmed): @1619=11, @1620=84 = "la on [78]" (row a8_03).
  11-84 unique x1 stream-wide. Stays fenced.
- **R2** (A15-C3, confirmed): @1664=94, @1665=84 = "ne on [64]" (row a8_04).
  94-84 unique x1 stream-wide. Stays fenced. The "non"=94+84 rescue stays
  forbidden (67 is the sole polyvalence; registry holds).
- **R3** (new, from the battery-lon-29-146 null, 2026-10-08): @146=84, @147=29.
  84-29 unique x1 of n(84)=25. Stated cause: 29='er' can neither attach left
  to 'on' ("oner" is not a French word) nor open a word before 'ce'
  (29 word-initial is unattested stream-wide); no parse covers 77-84-29-87
  with zero contradiction. Fenced. The frame-qui-77-84 promotion, the 84='on'
  grant, and the 6 clean 'l'on' legs are untouched.

## 5. Per-clause verdict

- **C1 — PASS**: all 7 legs re-derived at the exact offsets; 84 reads 'on'
  cleanly on 6 legs; the 7th holds the fenced R3.
- **C2 — PASS**: each leg's "l'on" reading inherits provisional 77='le'
  (A15-C1). No 77 promotion made — dependence only.
- **C3 — PASS**: @146 recorded as fenced R3; R1 (@1619) and R2 (@1664)
  confirmed still fenced per A15-C3.

Adverses:

- **"77='le' provisional — dependence grading, not a 77 promotion" —
  ANSWERED**: graded per leg in §3; this report makes no 77 verdict and changes
  nothing about 77's provisional status.

## 6. Verdict: promote — claim confirmed

All clauses pass; the adverse is answered. No value promoted. No standing
verdict changed. No contradiction with any red-team ruling: 84='on'
unconditioned stands (collision-62-84 killed 62="on" unconditioned; A15-C2
resolved); R1/R2 stay fenced per A15-C3; R3 is fenced as the third genuine
1/25 residual of n(84)=25.
