# Battery verdict: det-86-dlife-value — 86's determiner-life value over the 26 D-windows

Date: 2026-10-09. Worker: subagent det-86-dlife-value (battery worker).
Lock: code/crowd17/next-token/locks/det-86-dlife-value.lock (created
2026-10-09T08:15:23Z; no stale lock; deleted on completion).
Target id: det-86-dlife-value. Queue status at take: queued, priority 3.
Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py;
n=1847 asserted). canonical.py never used. R5005, sealed gate instances,
red-team adjudication queue untouched. No data invented. @-offsets are
0-based stream indices.

## Bar (pre-registered verbatim from battery-queue.json, BEFORE testing)

"promote iff one value parses all 26 with zero hard contradictions"

### Numbered clauses (operative, pre-registered)

1. PROMOTE iff one candidate value among {le, la, les, un, une, son, sa, ce}
   parses all 26 D-windows of 86 grammatically with zero hard contradictions.
2. KILL iff a window forces the claim false at kill grade (some D-window
   rules out every candidate on standing values), or a distributional test
   rejects the uniform-value hypothesis at the lane's standard.
3. Otherwise NULL.

Adverses (pre-registered): "Complement to this sweep; does not declare the
split (red-team act)." Honored: no split declared at battery level anywhere
below.

## Method

1. Re-parsed the repaired stream per repair_parse.py; extracted all 32
   windows of 86 independently (n=32 confirmed; the 26 D / 6 V partition
   re-derived: D = follower not in {29,59,06}; all 26 @-offsets match
   battery-split-86-amended-rule 26/26).
2. Values usable at kill grade: pencil (11=la, 70=pre, 82=m, 34=i, 29=er,
   40=e, 46=que) + red-team granted (87=ce, 64=qui, 96=par, 17=fois,
   79=tout, 00=pour, 84=on, 47=ce). Battery-promoted values (94=ne, 30=pas,
   12=n, 48=e, 24=finite-verb class, 06=ent) cited as caveated, never as
   kill-grade forcing.
3. Each D-window tested under each of the 8 candidate determiner values
   for French grammaticality; window-level evidence stated with bytes.

## Window-level evidence (all 26 D-windows; L2 L1 [86] R1 R2 R3)

Legend: OK-8 = parses under all 8 candidates; OPEN = no standing-value
force either way; KILL-8 = hard contradiction for all 8 candidates on
pencil/granted bytes.

Kill-grade contradictions (each independently falsifies the uniform claim):

- D00 @175 (a1_05): `09 87 [86] 21 69 14` = "[09] ce(87=ce GRANTED) [86]
  [21]...". Every candidate yields a double determiner ("ce le", "ce la",
  "ce les", "ce un", "ce une", "ce son", "ce sa", "ce ce") — ungrammatical
  in 1841 French. Word-internal rescue ("87-86" = "cele") is not French,
  and reseg-86-problem-windows KILLED the word-internal rival at this
  window (fusion contradicts the A-level 87=ce grant). KILL-8.
- D04 @671 (a5_00): `67 11 [86] 24 80 03` = "[67] la(11=la PENCIL) [86]
  [24]...". Every candidate yields double determiner ("la le", "la la",
  ...). Word-internal rescue KILLED by reseg-86-problem-windows
  (contradicts pencil ground truth). KILL-8.
- D21 @1345 (a7_05): `38 47 [86] 66 73 34` = "[38] ce(47=ce GRANTED) [86]
  [66]...". "ce" + any candidate = double determiner, ungrammatical;
  "47-86" fusion contradicts the A4 grant. KILL-8.

Supporting contradictions (battery-level, not kill-grade):

- D17 @1131 (a6_07): `52 37 [86] 24 77 86` = "[52] [37] [86] [24]...".
  24 = finite verb (battery-promoted class, pending ratification). Under the
  determiner reading, "[DET] [finite verb]" is ungrammatical for all 8
  candidates. Loophole fenced: "le/la/les" + finite verb parses as
  OBJECT CLITIC + verb — that is pronoun-life, outside this bar; declaring
  it needs its own battery (queued as follow-up 3). Not promoted, fenced.
- D13 @962 (a6_00): `96 00 [86] 56 41 19` = "par(96) pour(00) [86] [56]...".
  "par pour" is ungrammatical under GRANTED values, so the window fails to
  parse under ANY candidate — but the defect is orthogonal to 86's value
  (breaks under every 86 value; discriminates nothing). Gated on queued
  par-pour-962-adjudicate (verdict null 2026-10-09). Fenced, not counted
  as a candidate-specific contradiction.

Clean under all 8 candidates (8 windows — the le-subset's 9 minus D13):

- D03 @661 (a4_02): `16 00 [86] 50 80 03` = "pour [86] [50]..." — "pour
  DET [50]", 50 nominal-strong ("la 50" x2). OK-8.
- D11 @948 (a6_00): `98 96 [86] 01 77 86` = "par [86] [01]..." — "par DET
  [01]", 01 nominal-strong ("ce 01" x2). OK-8.
- D14 @1002 (a6_02): `33 00 [86] 56 47 91` = "pour DET [56] ce [91]" —
  56 nominal-weak-positive (@131 "par [56] qui"). OK-8.
- D15 @1099 (a6_06): `29 67 [86] 52 82 94` = "er et(67 positional: 52 not
  infinitive-shaped) DET [52] m..." — "et DET [52]", 52 nominal-strong
  ("la 52" x3). OK-8.
- D16 @1128 (a6_07): `43 00 [86] 52 37 86` = "pour DET [52]...". OK-8.
- D22 @1458 (a7_09): `21 67 [86] 66 79 17` = "et DET [66] tout fois" —
  66 nominal-strong ("pour 66" x7). OK-8.
- D23 @1506 (a7_11): `33 00 [86] 56 41 12` = "pour DET [56]...". OK-8.
- D25 @1792 (a8_09): `03 00 [86] 56 42 94` = "pour DET [56]...". OK-8.

Open/neutral (no standing-value force; 12 windows):

- D01 @300 (a2_04): `40 97 [86] 91 18 89` — neighbors 97/91/18 unvalued;
  "[DET] [91]" neutral. OPEN.
- D02 @557 (a3_01): `34 17 [86] 94 59 30` = "i fois [86] [94] [59] [30]" —
  "fois DET..." heads a new NP; neutral under all 8 on standing values.
  OPEN.
- D05 @716 (a5_01): `00 66 [86] 01 02 21` = "pour [66] DET [01]..." —
  asyndetic double NP is odd but not a hard contradiction on standing
  values. OPEN (tension noted).
- D06 @728 (a5_02): `11 00 [86] 48 88 11` = "la pour DET [48]..." —
  48's value not granted; neutral. OPEN.
- D07 @799 (a5_04): `44 77 [86] 44 74 62` — 77="le" provisional only;
  "le DET" strained but provisional-caveated, not kill-grade. OPEN.
- D08 @867 (a5_07): `46 00 [86] 70 87 77` = "que pour DET pre(70) ce..." —
  70="pre" prefix-compatible; neutral. OPEN.
- D09 @878 (a5_08): `16 77 [86] 78 17 08` — provisional-77 caveat;
  78="ver" is a battery lead, not granted. OPEN.
- D10 @899 (a5_08): `98 83 [86] 16 92 67` — neighbors open. OPEN.
- D12 @951 (a6_00): `01 77 [86] 96 87 46` — provisional-77 caveat. OPEN.
- D18 @1134 (a6_08): `24 77 [86] 20 62 98` — 24 finite-verb (battery),
  77 provisional; "le DET" caveated. OPEN.
- D19 @1147 (a6_08): `98 98 [86] 67 33 66` — 98 open; no standing-value
  force. OPEN (tension noted).
- D20 @1335 (a7_05): `39 83 [86] 71 64 60` — 83 "de"-lead open, 71 open.
  OPEN.
- D24 @1739 (a8_07): `48 52 [86] 12 34 94` — 52 unvalued; neutral. OPEN.

## Per-clause pass/fail

1. **PROMOTE: FAIL.** No candidate parses all 26. Best case is 8/26 clean
   (all 8 candidates); the other 18 windows are open, fenced, or hard
   contradictions. Every candidate fails at D00, D04, and D21.
2. **KILL: PASS.** D00 (@175, 87=ce granted), D04 (@671, 11=la pencil),
   and D21 (@1345, 47=ce granted) each independently force all 8
   candidates false: "ce/la/ce + determiner" is ungrammatical, and the
   word-internal rescue was killed at kill grade by reseg-86-problem-windows
   (2026-10-09). The uniform-candidate claim is falsified.
3. NULL not reached.

## Adverses

- "Complement to this sweep; does not declare the split (red-team act)":
  HONORED. This kill is of the uniform VALUE claim only; no split is
  declared. The D-life remains positionally real (amended rule, battery
  level); its value structure is heterogeneous and red-team's to partition.
- §5.2 check: no standing red-team verdict names 86's D-life value; the
  amended-rule battery-promote is positional and value-free, uncontradicted.
  The le-subset battery's recorded global kill of 86="le" is generalized,
  not contradicted.

## Verdict: KILL

86's determiner-life value is NOT one value from {le, la, les, un, une,
son, sa, ce} uniform over all 26 D-windows. Three windows (@175 with
87=ce granted, @671 with 11=la pencil, @1345 with 47=ce granted) each
independently falsify every candidate at kill grade. Surviving structure:
8 windows parse cleanly under all 8 candidates (the le-subset's "le"-life
minus the par-pour defect at @962); the det-left windows (#0/#6/#24) need
a different value or a finer partition — red-team's act.

## Follow-up targets (kill; proposed to keep the pipeline turning)

1. `det-86-dlife-partition` (P2): partition the 26 D-windows into
   distributional sub-lives — le-life 9 (left in {00,96,67}, follower in
   {50,01,52,56,66}; exceptionless left-frame split re-derived here),
   det-left 3 (left in {87,11,47}: @175/@671/@1345), 77-adjacent 4
   (@799/@878/@951/@1134), residual 10 — and name per-subset value
   hypotheses with byte evidence. Bar: a subset-value promotes iff it
   parses all its windows with zero hard contradictions; kill any
   subset-value a pencil/granted window forces false. Does not declare
   any split (red-team act).
2. `noun-86-dlife` (P3): test 86 as a NOUN in D-windows — the noun reading
   parses exactly the three det-left windows that kill all determiner
   candidates ("ce [N]" @175/@1345, "la [N] [V]" @671 with 24 finite-verb).
   Bar: name the noun value with >=2 determiner-anchored frames + zero
   hard contradictions on standing values; kill iff a pencil/granted
   window forces it false.
3. `clitic-86-77-windows` (P3): test 86 as object clitic (le/la/les) in the
   four 77-adjacent D-windows (@799, @878, @951, @1134). Bar: promote iff
   all four parse as [subject] clitic [finite verb] with stated
   subject/verb values + zero hard contradictions on standing values;
   kill iff any window forces the clitic reading false.

## Constraints compliance

- Tested only on the repaired 1,847-pair stream; canonical.py never
  touched; R5005, sealed gates, red-team queue untouched.
- No standing verdict downgraded or overwritten; no red-team verdict
  contradicted.
- 86 polyvalence NOT declared; no new polyvalence implied.
- Sibling reports coordinated, not duplicated: voir-86-sweep (complement),
  split-86-amended-rule (positional frame), le-86-determiner-subset
  (9-window fence adopted), reseg-86-problem-windows (kill-grade rescue
  closure adopted).
