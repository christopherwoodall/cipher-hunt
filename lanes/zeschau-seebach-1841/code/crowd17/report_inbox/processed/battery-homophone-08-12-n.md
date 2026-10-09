# Battery `homophone-08-12-n` — verdict: NULL (fence executed)

## Bar (verbatim, pre-registered)

"resolve iff 08 profile matches 12 with byte evidence; fence otherwise"

## Numbered clauses

- C1: 08's successor profile matches 12's successor profile with byte evidence → resolve the "n"-sibling hypothesis.
- C2: else-arm — fence the hypothesis with stated cause.

## Target brief

- CLAIM: compare 08 successor profile to granted 12="n" (n=23); "n"-sibling hypothesis survives iff 08 matches 12 better than 94 "ne".
- ADVERSES: none listed.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`
(parsed like `repair_parse.py`); asserts held (1,847 pairs, 96 types).
`canonical.py` never used. Census is byte-exact, 0-based pair offsets.

Standing values adopted, not re-litigated: 12="n" granted (n=23);
94 in the "ne" frame (brief's premise); 48='e' promoted; 87=ce promoted.
No red-team verdict contradicted or downgraded. §7 intact — no new
polyvalence declared or implied.

## Window-level evidence

### Censuses (byte-exact)

- n(08) = 18, positions: 35, 60, 98, 198, 534, 631, 779, 881, 922, 944,
  975, 1302, 1323, 1339, 1488, 1520, 1592, 1610.
- n(12) = 23, positions: 58, 64, 169, 241, 348, 539, 701, 704, 709,
  712, 809, 843, 1075, 1119, 1430, 1471, 1509, 1548, 1582, 1641,
  1708, 1736, 1740.
- n(94) = 37.

### Successor profiles

- 08 successors: 91×1, 34×1, 21×1, 67×1, 24×1, 52×1, 29×1, **31×3**,
  **65×2**, **62×2**, 01×1, 43×1, 81×1, 55×1.
- 12 successors: 41×2, **94×3**, **48×5**, **16×3**, **44×2**, 98×1,
  66×1, 63×1, **06×2**, 61×1, 33×1, 34×1.
- 94 successors: 92×2, 93×1, **24×2**, 65×1, 06×1, **74×3**, 02×1,
  64×1, **59×3**, **52×3**, **82×4**, **76×2**, 29×1, 60×1, 07×1,
  15×1, 26×1, 87×1, 70×1, **79×2**, 84×1, 30×1, 88×1, 44×1.

### Set comparison

- 08 ∩ 12 = {34} — one shared successor; Jaccard 0.04.
- 08 ∩ 94 = {24, 29, 52, 65} — four shared successors; Jaccard 0.118.
- 08's repeat successors (×≥2): {31, 62, 65}. None ever follows 12
  (12+31 = 0, 12+62 = 0, 12+65 = 0).
- 12's repeat successors (×≥2): {06, 16, 41, 44, 48, 94}. None ever
  follows 08 (08+48 = 0, 08+94 = 0, 08+16 = 0, 08+41 = 0, 08+44 = 0,
  08+06 = 0).

The two distinctive "tails" are disjoint: each code's repeated
followers are never followers of the other.

### The decisive discriminator

12="n" is most characteristically followed by 48='e' (×5, "ne" = 12+48).
08 is NEVER followed by 48 (08+48 = 0). Conversely 08's characteristic
follower 31 (×3, the "08 31" windows @881/@1488/@1520, all "… [08][31] …"
word-internal geometry) never follows 12. A true 'n'-allophone would
share the "n"+"e" word-final collocation; 08 lacks it entirely.

### Per-clause verdicts

- **C1: FAIL.** 08's successor profile does not match 12's — it matches
  94's better (4 shared vs 1 shared; 0.118 vs 0.04 Jaccard). The
  "n"-sibling hypothesis does not survive the distributional test.
- **C2: FIRES.** Fence the "n"-sibling hypothesis.

Note: 08 matching 94's profile better is recorded as a distributional
fact only. It does not promote any 08 value (that would need a fresh
target and, for a "ne"-type read, red-team clearance under §7). Per
protocol, 1690-frequency uniformity would be necessary but insufficient;
here even the distributional match fails.

Canonical-stream caveat stands (68 of 70 upstream row offsets
unvalidated); all tested loci are byte-exact on the repaired stream.

## Verdict: NULL (fence)

The "n"-sibling hypothesis for 08 is fenced at battery grade: disjoint
repeat-successor tails and the absent 08+48 collocation.

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `08-vs-94-profile` (P3) — test directly whether 08's successor
   profile matches 94="ne" closely enough to merit a value hypothesis,
   or is an independent letter-class signature.
2. `08-position-profile` (P3) — census 08's word-position signature
   (word-initial vs word-internal) across all 18 windows via
   adjacent-pair geometry, independent of any value claim.
3. `31-08-word-host` (P3) — name the [08][31]… word at @881/@1488/@1520
   once a candidate host class is licensed.
