# CONDITIONER report — 84 conflict + 00 conflict (round-7 WOs 1–2)

2026-10-07 · conditioner agent · bars pre-registered in
`code/crowd7/conditioner/PREREG.md` BEFORE any new computation · evidence
`code/crowd7/conditioner/conditioner_results.json` + `conditioner_84_00.py` ·
positions 0-based repaired 1,847-pair starts per red-team verify_f26_17.py
(61/61 PASS, supersedes NOTES.md). **No status changes merged — verdicts below
are recommendations for red-team ruling.**

## WO-1: the 84 conflict — rule R REFUTED as a partition; two conditioned islets banked

**Verdict: the Closer's conditioned-polyvalence rule ("en" iff pre∈{46,94,82};
noun iff pre∈{77,11}) FAILS the F33 zero-free-cases bar — 13 of 25 84-occurrences
have predecessors outside both sets. Neither unconditioned side survives either.
Recommended: kill both unconditioned claims; bank TWO conditioned islets at LEAD
(partial polyvalence); 13 windows UNCLASSIFIED.**

Pre-registered bars vs results:
- **B1 coverage: FAIL.** Full 84 table (pre→84→suc): en-class {167:(82,53),
  310:(46,24), 473:(46,24), 1665:(94,64)}; noun-class {146:(77,29), 260:(77,74),
  1058:(77,09), 1447:(77,59), 1485:(77,24), 1620:(11,78), 1764:(77,09),
  1803:(77,59)}; FREE 13: pres ∈ {66×2, 89×2, 91, 53×2, 65, 48, 06, 17, 32, 74}
  @[154,276,391,412,788,857,1021,1151,1189,1290,1378,1418,1501]. Rule R is dead
  as a full partition — it was fitted on 12/25 windows.
- **B2 en-islet coherence (n=4, n_eff=3):** @167 "m'en" ✓ GT-anchored (82=m);
  @310/@473 "qu'en"+24 ✓ GT-anchored (46=que), byte-identical trigram
  46-84-24 (n_eff=1); @1665 94-84-64 = "n'en qui" — ADVERSE (single, n=1;
  94="ne" prov-strong, direct "n'en qui" ungrammatical, no verb slot).
  Islet holds LEAD on 2 independent GT-anchored legs; adverse noted, not kill-grade.
- **B3 noun-islet coherence (n=8, n_eff=6):** @1447/@1803 «le [noun] est» ✓✓
  clean (59="est" STRONG LEAD; byte-identical, n_eff=1); @146 «le X»+29("er" GT)
  compatible (word-internal or boundary); @260/@1058/@1764/@1485 compatible,
  no break; @1620 «la X»+78 soft tension only (78 polyvalent). Zero adverses.
  Islet holds LEAD; identity still NULL.
- **B4 independence: PASS.** En-legs (E1/E2/E5) and noun legs rest on disjoint
  occurrence sets — no double-count.
- Side comparison on the full 25 (per pre-registered fallback): "en"-only is
  dead — E4 revives ("l'en" ×7 @[145,259,1057,1446,1484,1763,1802] under
  77="le"), "la en" @1620 impossible, 13 windows unexplained. Noun-only is
  dead — cannot explain "qu'en" ×2 (E2, GT-anchored, n_eff=1), "m'en" (E5,
  GT-anchored), and @1665 "ne [noun]" is ungrammatical. **Both unconditioned
  versions KILLED.**
- E4 ("l'en" 141×/63×) dissolves under the islet outcome: all seven 77→84 and
  the 11→84 windows are noun-class, so the blocker applies to zero occurrences.

**Remaining blockers / open:** (1) 13 free windows unidentified — 84's full
value inventory unknown, no post-hoc fitting (F33); (2) @1665 adverse for the
en-islet; (3) noun identity NULL; (4) «que 84 24» ×2 (byte-identical,
n_eff=1) hinges on 24's identity — under H1's 24="en" lead the en-read would be
"qu'en en" (strained; flagged, not graded).

## WO-2: the 00 conflict — conditioned polyvalence SUPPORTED; rate blockers STAND

**Verdict: rule S (00="le" iff pre=96; 00="pour" elsewhere) PASSES C2/C3/C4,
but C1 FAILS — the diplomatic corpus does NOT repair B1/B3. Recommended:
00="pour" stays STRONG LEAD (blockers standing, unchanged); 00="le" holds LEAD
as a conditioned islet (pre=96, n=3, n_eff=3). Conflict resolved as conditioned
polyvalence at LEAD-grade; no provisional promotion.**

Method parity check first: re-tokenized Tocqueville t1+t2 with the closer's
exact tokenizer reproduces B1=6.22× / B3=3.85× exactly. r1=P(00)/P("pour"),
r3=P(46|00)/P("que"|"pour"); P(00)=55/1847=0.02978, P(46|00)=4/55=0.07273.

- **C1 rate-repair: FAIL.** Diplomatic rates (elision-split word model):
  despatches-primary (Nesselrode v8 + Levant 1841, N=372,751): r1=**9.14×**,
  r3=3.27×. Full diplomatic French (N=3,960,009): r1=5.05×, r3=4.00×.
  Per-file r1 ∈ [4.01, 15.33]× (Levant 15.33× — "pour" P=0.00194 in Levant
  despatches, rarest of all; Metternich 7.46/8.67×), r3 ∈ [2.12, 12.70]×
  (best r3 = Guizot mémoires t5–t6 at 2.12×, n=73, still over the 2× band;
  its r1=4.17×). **No corpus brings either ratio ≤2×; the despatch register
  makes B1 worse, not better.** B1/B3 block provisional — standing.
- **C2 incompatibility: PASS.** 96→00 @47/@465/@960, successors @48=92,
  @466=33, @961=86: "par pour X" ungrammatical at all three — tension confirmed.
- **C3 islet coherence: PASS.** Zero free cases (exactly the three 96→00
  windows); «par le 92» ✓, «par le 33» ✓ clean; «par le 86» @961 — 86 is the
  M1 infinitive-allomorph, but M1's environment is the 00-governor environment
  which is "le" (not "pour") at this window, so 86@961 is unclassified by M1:
  2 clean + 1 unknown, acceptable at LEAD. Null 0.5% stands; three
  non-byte-identical windows (n_eff=3).
- **C4 battery integrity: PASS.** Dropping the 3 pre=96 windows: 00→86 11 vs
  00→06 0 (B2a survives), P(86|00)=11/52=0.2115 (B2b), 06→00 ×4 (B5),
  00→46 ×4, 00→11 ×4 — every leg intact. (Note: one of the 12 00→86 was the
  @961 le-window itself.)

**Remaining blockers:** B1 (4–15× over all diplomatic registers) and B3
(2.1–12.7×) still block 00="pour" provisional; the "le"-islet is n=3 and
cannot carry more than LEAD. The «par le» frames are now cleanly separated
from the "pour" battery — no double-count either way.

## Files
- `code/crowd7/conditioner/PREREG.md` — pre-registered bars (written pre-computation)
- `code/crowd7/conditioner/conditioner_84_00.py` — all re-derivations
- `code/crowd7/conditioner/conditioner_results.json` — full 84/00 tables + per-file
  diplomatic rates (evidence: no redactions, full values)
