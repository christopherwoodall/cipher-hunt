# Battery verdict: homophone-86-split — positional split rule for 86

Date: 2026-10-08. Worker: c87e1d44-8882-4c1b-9a48-7a62abd0ae2a.

## Bar (verbatim from battery-queue.json)

"promote the positional split rule iff no window violates it and 1690-uniformity holds within each life at the lane's standard; include a byte-level homophone-set candidacy check."

Listed adverses: "declaring polyvalence is a red-team act per section 7 (67 sole true polyvalence) - this battery tests a homophone-set/split candidacy, never declares polyvalence; @888 adverse stands; 1690 uniformity necessary-but-insufficient per lane law."

### Numbered clauses (operative)

1. No window violates the positional split rule: every 86-window's follower is
   in the determiner set D = {56,50,01,52,66,70,78,48,44,24,20,67,71,12,21,91,
   94,16,96} (determiner-life) or is 29 (stem-life).
2. 1690-uniformity holds within each life at the lane's standard.
3. Byte-level homophone-set candidacy check included.

## Method

Parsed the repaired 1,847-pair stream exactly per
code/side-keyhunt/repair_parse.py (repaired_offsets.json +
data/upstream-ct_R5005.txt). Never used canonical.py. Never touched R5005,
sealed gate instances, or the red-team adjudication queue. Enumerated all 32
indices i with seq[i]=='86', recorded @-offsets, L3..R3 context, follower
census, and predecessor census — all re-derived on bytes, no prior counts
trusted. French grammaticality judged against 1841 diplomatic French using
banked values only (pencil: 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que;
granted: 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 47=ce, 84=on,
12=n, 48=e, 30=pas, 06=ent; provisional: 59=est, 77=le).

Note on the brief's evidence field: it describes the split as "clean" with
the determiner-life follower set D. Re-derivation shows D omits two observed
followers (59, 06) — the residue is 2 windows, not 0. Corrected below.

## Window-level evidence (all 32, @-offsets on repaired stream)

Notation: L3 L2 L1 [86] R1 R2 R3; known values substituted. Life: S =
stem-life (follower 29), D = determiner-life (follower in D), X = violator
(follower outside D ∪ {29}).

STEM-LIFE (S), n=4:
- #2 @431: 42 63 77 [86] 29 82 16 — 86-29 infinitive-shaped (A9). OK.
- #25 @1375: 67 98 00 [86] 29 89 84 — "pour [86]er" OK.
- #26 @1391: 06 29 67 [86] 29 89 16 — "veut/et [86]er" OK.
- #31 @1825: 00 97 00 [86] 29 82 38 — "pour [86]er" OK.

DETERMINER-LIFE (D), n=26 (followers in D):
- #0 @175: 60 09 87 [86] 21 69 14 — R1=21 ∈ D. ("ce [86]" — 'le' fails here; life assigned, value not.)
- #1 @300: 78 40 97 [86] 91 18 89 — R1=91 ∈ D.
- #4 @557: 59 34 17 [86] 94 59 30 — R1=94 ∈ D.
- #5 @661: 62 16 00 [86] 50 80 03 — R1=50 ∈ D. ("pour le [50]" parses.)
- #6 @671: 20 67 11 [86] 24 80 03 — R1=24 ∈ D. ("la [86]" — 'le' fails.)
- #7 @716: 63 00 66 [86] 01 02 21 — R1=01 ∈ D.
- #8 @728: 64 11 00 [86] 48 88 11 — R1=48 ∈ D. ("pour [86] e" — 'le' fails.)
- #9 @799: 37 44 77 [86] 44 74 62 — R1=44 ∈ D.
- #10 @867: 47 46 00 [86] 70 87 77 — R1=70 ∈ D. ("pour [86] pre" parses.)
- #11 @878: 49 16 77 [86] 78 17 08 — R1=78 ∈ D.
- #13 @899: 14 98 83 [86] 16 92 67 — R1=16 ∈ D.
- #14 @948: 62 98 96 [86] 01 77 86 — R1=01 ∈ D. ("par le [01]" parses.)
- #15 @951: 86 01 77 [86] 96 87 46 — R1=96 ∈ D.
- #16 @962: 67 96 00 [86] 56 41 19 — R1=56 ∈ D. ("pour le [56]" parses.)
- #17 @1002: 82 33 00 [86] 56 47 91 — R1=56 ∈ D. ("pour le [56]" parses.)
- #18 @1099: 06 29 67 [86] 52 82 94 — R1=52 ∈ D. ("et le [52]" parses.)
- #19 @1128: 37 43 00 [86] 52 37 86 — R1=52 ∈ D. ("pour le [52]" parses.)
- #20 @1131: 86 52 37 [86] 24 77 86 — R1=24 ∈ D.
- #21 @1134: 86 24 77 [86] 20 62 98 — R1=20 ∈ D.
- #22 @1147: 42 98 98 [86] 67 33 66 — R1=67 ∈ D.
- #23 @1335: 52 39 83 [86] 71 64 60 — R1=71 ∈ D.
- #24 @1345: 52 38 47 [86] 66 73 34 — R1=66 ∈ D. ("ce [86]" — 'le' fails.)
- #27 @1458: 61 21 67 [86] 66 79 17 — R1=66 ∈ D. ("et le [66]" parses.)
- #28 @1506: 42 33 00 [86] 56 41 12 — R1=56 ∈ D. ("pour le [56]" parses.)
- #29 @1739: 12 48 52 [86] 12 34 94 — R1=12 ∈ D.
- #30 @1792: 47 03 00 [86] 56 42 94 — R1=56 ∈ D. ("pour le [56]" parses.)

VIOLATORS (X), n=2 — follower outside D ∪ {29}, byte-confirmed on raw rows:
- #3 @553 (row a3_01, raw "4655810086593417862", offset 0): 55 81 00 [86] 59 34 17 —
  "pour [86] est i fois", R1=59='est' (provisional). The @552/@553 standing
  adverse ('pour le est' ungrammatical). 59 ∉ D.
- #12 @889 (row a5_08, raw "3703020086067776019882", offset 1): 03 02 00 [86] 06 77 76 —
  "pour [86] ent le [76]", R1=06='ent' (granted). The @888 standing adverse
  ('pour l'ent le' ungrammatical, no elision rescue). 06 ∉ D.

Follower census (re-derived): 01:2, 06:1, 12:1, 16:1, 20:1, 21:1, 24:2, 29:4,
44:1, 48:1, 50:1, 52:2, 56:4, 59:1, 66:2, 67:1, 70:1, 71:1, 78:1, 91:1, 94:1,
96:1 — 22 distinct followers, n=32. Conformers: 30/32.

## Per-clause results

### Clause 1 (no window violates the positional rule): FAIL

Two windows violate the rule as stated, both byte-confirmed:
- #3 @553: follower 59 ∉ D ∪ {29}.
- #12 @889: follower 06 ∉ D ∪ {29}.

Both violators coincide exactly with the two standing adverses for 86
(@552/@553 'pour le est'; @888/@889 'pour l'ent le'). The remaining 30/32
windows conform with perfect mutual exclusivity: follower 29 ⟺ stem-life
(4/4), follower ∈ D ⟹ determiner-life (26/26), and no determiner-life window
has follower 29. The segregation signal is genuine; the exceptionless "iff"
is not established.

### Clause 2 (1690-uniformity within each life at the lane's standard): NOT VIOLATED

- Stem-life (n=4): all four followers are 29 — uniform by construction. n is
  too small for a runs test; recorded, not inferred from.
- Determiner-life (n=26, 19 distinct followers): 56 x4, five followers x2
  (01, 24, 52, 66, 94), thirteen x1. The 56-x4 cluster is the fixed formula
  '00 86 56' (@962, @1002, @1506, @1792) — a formulaic repeat, not a
  uniformity break. No pathological concentration inconsistent with a single
  underlying value; the long tail is expected for 'le' (many nominal heads).
- Runs test on the 32-window life sequence (@-order): 6 runs vs 8.0 expected,
  z = -1.72 — mild clumping of the stem-life windows, BELOW the lane's |z|>2
  significance bar. Not a rejection.
- Third-life check (predecessor conditioning within determiner-life): the
  00-predecessor windows (n=8) take followers {50,48,70,56,52} and the
  77-predecessor windows (n=4) take {44,78,96,20} — zero overlap observed, but
  a 20,000-trial permutation test gives P(no overlap | random) ≈ 0.384. Not
  significant. No third life; recorded as an open question, not a finding.
- Stem-life predecessors (77, 00, 67, 00) are mixed — no predecessor
  conditioning on the stem side either.
- LIMIT (per the adverse): 1690 uniformity is necessary but insufficient per
  lane law — these uniformity results cannot promote on their own.

### Clause 3 (byte-level homophone-set candidacy check): NOT SUPPORTED

- The lane's falsifier pattern (crowd13 homophone-cd PREREG): successor-
  segregation is evidence AGAINST free homophony and FOR a positional split.
  Here the segregation is perfect — P(follower=29 | stem-life)=1,
  P(follower=29 | determiner-life)=0. 86's two lives are NOT free homophones
  cycling per the 1690 order; they are positionally conditioned. Free-
  homophone candidacy for the two lives: REJECTED by the lane's own criterion.
- 86 vs 77 (the other 'le' candidate, n=44, provisional): 77 takes
  D-followers in 10/44 windows (44 x2, 66 x1, 78 x7) — same positional slot
  as 86's determiner-life — but 77→86 adjacency occurs x5 and the two groups
  co-occur inside windows repeatedly (#9, #11, #14, #15, #20, #21), which is
  inconsistent with complementary homophone distribution; the resulting
  "le le" readings already fail. 77's own value is provisional and entangled
  with the S5 fence. Homophone-set candidacy for 86 (with 77 or otherwise):
  NOT ESTABLISHED at battery level — fenced for the red team, not resolved
  here.

## Adverses

- §7 (polyvalence declaration is a red-team act): RESPECTED. This battery
  tests candidacy only and returns NULL; no polyvalence (or split) is
  declared. The declaration question is packaged as follow-up 3 for the red
  team.
- @888 adverse stands: CONFIRMED and kept standing. #12 @889 ("pour [86] ent
  le [76]") remains ungrammatical under every banked/provisional assignment
  (no elision rescue: 06='ent' granted, 77='le' provisional follows). It is
  now additionally a clause-1 violator — fenced with byte-level cause, not
  resolved.
- 1690 uniformity necessary-but-insufficient: NOTED as a limit — the clause-2
  results are consistency checks, not promotion grounds.

## Verdict: NULL

The positional split rule as stated (exceptionless "iff") is violated by 2
of 32 windows, both byte-confirmed and both coinciding with standing
adverses — so it cannot be promoted. It is not killed either: the
distributional segregation is strong and genuine (30/32 conform with perfect
follower mutual exclusivity; uniformity not violated at the lane's standard;
no third-life signal), and both violators are windows the lane already flags
for re-segmentation. Killing would misreport a live structural signal as
dead. The honest result is NULL: the split candidacy survives at 30/32 with
two adverse-window exceptions; the exceptionless rule is not established;
declaration remains a red-team act.

## Follow-up targets (null regenerates work)

1. `reseg-86-553-889` (priority 2): re-segment the two violating windows —
   @553 "00 86 59 34" (pour-[86]-est-i, row a3_01) and @889 "00 86 06 77"
   (pour-[86]-ent-le, row a5_08). Bar: for each window, kill the
   standalone-word assumption iff a cleaner multi-group word parse is
   demonstrated on bytes; if 86 goes word-internal, name the host word.
2. `split-86-amended-rule` (priority 2): re-test the positional split with
   59/06 dispositioned — amended exception clause with byte-level cause per
   window, or third-life candidacy. Bar: promote the amended rule iff it is
   exceptionless over all 32 windows and every non-conforming window is
   fenced with byte-level cause (no bare "adverse" fences).
3. `redteam-86-split-docket` (priority 1): package for red-team adjudication —
   the 30/32 segregation table, uniformity results (runs z=-1.72,
   permutation p≈0.384), homophone-set candidacy rejection per the lane's
   segregation criterion, and the §7 declaration question (positional split
   vs polyvalence vs homophone set). Declaration is a red-team act; this
   battery does not declare.

R5005, sealed gate instances, and the red-team adjudication queue were not
touched. No standing verdict was contradicted or downgraded.
