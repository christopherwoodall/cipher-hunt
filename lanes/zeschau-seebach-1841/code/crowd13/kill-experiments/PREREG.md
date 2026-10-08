# PREREGISTRATION — Kill Experiments 1 & 2, Seebach round 13 (council round)

**Locked 2026-10-07 by the red-team assumption killer, BEFORE any experiment
computation.** I both run and rule these experiments; no other agent
adjudicates. Killer's priors (not results): KE2-A re-derives, KE2-B comes back
clean, KE1 inconclusive.

## Shared machinery (both experiments)

- **Stream:** repaired canonical 1,847-pair parse via
  `code/crowd4/repaired_parse.py::load_pairs_repaired()` (asserts 1,847 pairs,
  96 groups, cribs @754 and @1034). All cipher-side counts re-derived by me
  from this stream — no lane numbers trusted.
- **Corpus:** the clean diplomatic pool = CORE
  (`nesselrode-v7.txt`, `nesselrode-v9.txt`, `nesselrode-v10.txt`,
  `guizot-memoires-t5-t6.txt`, `levant-correspondence-1841-p3.txt`) +
  POOL_EXTRA (`revue-deux-mondes-1841-q1..q4.txt`, `metternich-papiere-v4.txt`,
  `metternich-papiere-v6.txt`, `talleyrand-memoires-v1.txt`,
  `pozzo-di-borgo-correspondance-v1.txt`) = 13 files under
  `code/side-period/corpus/`. **nesselrode-v8 VOID for all phrase/bigram
  queries** (OCR word-splits — per `code/council/drag/build_inventory.py`
  docstring; the "clean pool" definition).
- **Tokenizer:** `code/council/drag/common.py::tok_elision`, verbatim.
  Elided forms (`qu'`, `c'`, `l'`, …) are separate tokens from their full
  forms (`que`, `ce`, `la`, …) — matching the cipher's own 46-vs-86
  distinction (ISLET 9).
- **12-known set:** {11,70,82,34,29,40,46,87,64,96,59,77}.
  Word-valued map for corpus bigram checks:
  {11:la, 46:que, 87:ce, 64:qui, 96:par, 77:le}; 59:est counts as word-valued
  **iff** its stream predecessor ∈ {64,94,93} (ISLET 10's exact rule —
  locked here to prevent post-hoc fiddling). 70/82/34/29/40 are syllables,
  never word-bigram-eligible.

---

## KILL EXPERIMENT 2 — Part A: 46=que leave-one-out (RUN FIRST)

### Gate G — 87=ce without any 46-involving leg

46-involving legs (VOIDED for this run): N1's P(46|87) CI prong, N2's
exhaustive inversion (cipher profile needs P(que|87)=3/32), N3's "parce que"
frame (also admitted circular), F6's P(46|87,pre=96)=3/3 reframing,
attempt-3's P(que|87)=0.094 check, F27's joint 24-inversion (needs P(V|que)).

Remaining legs, re-derived by me on stream + clean pool:
- **G1 (qui-prong rival kill):** cipher P(64|87)=k/32 with 95% Wilson CI;
  era P(qui|R)=0 for all six rivals R∈{se,ne,le,je,on,en} (recomputed on the
  clean pool); era P(qui|ce) inside the Wilson CI. HOLDS iff all three.
- **G2 (diversity profile):** 87 has ≥20 distinct followers AND ≥20 distinct
  predecessors (attempt-3 measured 28/28; bar set at 20 as the function-word
  floor). HOLDS iff both.
- **G3 (cela-leg):** 87→11 count ≥5 (attempt-3: ×7). Stands
  register-dependent regardless of outcome.
- **64=qui check:** HOLDS iff ≥2 of its non-46 legs hold —
  (a) 87→64 ×5 with P(64|87) in-band vs era P(qui|ce) at factor-3;
  (b) "qui" is the #1 era follower of "ce";
  (c) 24-87-64 ×3 formula present (F17).

**Gate bar:** 87=ce PROMOTES iff ≥2 of {G1,G2,G3} HOLD **and** 64=qui HOLDS.
(G1's P(64|87) datum is shared with 64=qui-(a) — counted once; independence
accounted.) If the gate FAILS → ESCALATE IMMEDIATELY to the coordinator:
46=que was load-bearing for the provisionals; do NOT proceed to re-derivation.

### Re-derivation of 46 (only if gate passes; 87=ce and 64=qui taken as given)

- **R1 (follower profile):** cipher side — rank(64)=1 among 87's followers
  AND rank(46) ≤ 3 among 87's followers. Corpus side — rank("qui")=1 among
  followers of "ce" AND rank("que") ≤ 3 among followers of "ce".
  **PASSES iff all four.**
- **R2 (predecessor profile):** corpus — rank("ce" among predecessors of
  "que") ≤ 5. Cipher — rank(87 among predecessors of 46) ≤ 5. Rate check —
  P(87|_46)/P(ce|_que) within factor 3. **PASSES iff all three.**

**Verdict bar:** 46=que is **RE-DERIVED iff R1 AND R2 both PASS**
(≥2 independent legs, follower vs predecessor, nothing assumed).
Otherwise 46=que is **DEMOTED to "single-gloss GT"** — usable, but STATE.md
must flag that the lane's highest-leverage anchor rests on one erased pencil
mark, and ISLET 10's dependency on 46="que" is marked **conditional**.
Disclosed adverse, not in the bar (round-7 tension): 59→46 ×2 ("est que").

---

## KILL EXPERIMENT 2 — Part B: @1034 polyvalence audit

### B1 — registry trigger check (mechanical)

For each g ∈ {11,70,82,34,29,40}: extract (pre,suc) at g's @1034 occurrence
from the repaired stream (11@1034, 70@1035, 82@1036, 34@1037, 29@1038,
40@1039). Check against **every** (group, trigger→reading) rule banked in
`code/crowd9/conditioner/islet_registry.md`
(84: pre∈{82,66,89}; 00: pre=96; 06: pre=82; 96: pre=64&suc=47;
59: pre∈{64,94,93}→est / pre=84→verb-final; 52: pre∈{94,70};
94: pre=82 / suc=87).
**TRIGGERED iff the registry banks a conditioned reading *for g itself*
whose trigger fires at g's @1034 context.** Pattern-only matches against
other groups' triggers are recorded but do NOT fire (triggers are
group-specific under F33).

### B2 — F33 conditioned-vs-free battery (g as subject; never run — they're GT)

For each g with free value v (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e):
1. Census every occurrence with (pre, suc) on the repaired stream.
2. Split-hunt over the fixed feature family
   T ∈ {pre=x : n(T)≥2} ∪ {suc=y : n(T)≥2}: test the free reading under T
   for (i) grammatical contradiction under banked neighbor values
   (judged by hand, each documented), or (ii) era-bigram adverse —
   French (v, neighbor-value) bigram 0×/pool where the neighbor is banked.
3. A conditioned alternative **PROMOTES** iff: exact trigger stated,
   n(T) ≥ 3, ≥2 independent legs (two distinct contradiction types, or
   contradiction + era-rate adverse with the complement clean),
   biconditional predicted windows all clean.

**Verdict bar:** any PROMOTED conditioned alternative firing at @1034 →
the "two occurrences" claim drops to **one-and-a-half** for that group
(re-derive treating @1034's compromised groups as unknown). If none:
the two-occurrence claim is **ROBUST** (stated formally for the first time).

---

## KILL EXPERIMENT 1 — offset-model spanning-bigram test (RUN AFTER KE2)

**M1+1flip construction:** continuous pairing from digit 0 of
`data/upstream-ct_R5005.digits.txt` (3,764 digits), single digit dropped at
row boundary b* — the drop removes the last digit of the row above b*
(raw offset b*−1). b* ∈ {row boundaries with raw offset in (2108,3453)}
(25 candidates; verified 2026-10-07) chosen **ADVERSARIALLY** = the boundary
maximizing the gold count below (the alternative gets its best shot).
All 25 candidates' counts reported for transparency.

**Spanning bigrams:** for each of the 69 row boundaries B: the spanning pair
p_B is the M1+1flip pair whose two digits' original raw offsets (d1,d2)
satisfy d1 < B ≤ d2 (offsets tracked explicitly through the drop).
For each p_B ∈ 12-set, form bigram tokens (pre(p_B),p_B) and (p_B,suc(p_B))
wherever the neighbor ∈ 12-set. Each such token "spans a row boundary".

**Classification (per bigram token):**
- **GOLD** iff bigram ∈ {(11,70),(70,82),(82,34),(34,29),(29,40),(87,64),
  (87,46),(96,87)} (the 8 lane-confirmed) **OR** both groups word-valued
  (per the map above, incl. the 59 rule) AND the French word bigram is
  attested **>50×** in the clean pool.
- **IMPLAUSIBLE** iff both groups word-valued AND the French word bigram is
  **0×** in the clean pool AND ungrammatical in standard French (each
  candidate judged by hand and documented — e.g. "la le").
- Else **UNINFORMATIVE** (syllable-valued groups can never be implausible;
  only the 8-confirmed membership can make them gold).

**Bar (LOCKED, verbatim from the work order):**
- gold ≥ 3 AND gold:implausible ≥ 3:1 → **REJECT row-independence.**
  M0 is wrong; pairs span rows. **STOP IMMEDIATELY** — report the numbers
  to the coordinator, do NO further analysis. The coordinator halts the
  round; the parent re-plans. This overrides everything else.
- implausible ≥ gold → **row-independence HOLDS** (spanning pairs are
  chance juxtapositions; M0's model justified).
- Else → **INCONCLUSIVE** (the data cannot distinguish; the 68-offset model
  stands as a permanent caveat).

**Parsimony rider (no experiment needed):** recorded regardless — M0 spends
70 parameters to satisfy 2 gloss constraints; M1+1flip spends 1.

---

## Regardless of outcomes

Report the deeper conditionality verbatim for STATE.md:
"canonical parse is conditionally canonical on (a) the gloss line-tag AND (b)
upstream's 70 EM offsets, 68 unvalidated."

## Outputs

- Code + results: `code/crowd13/kill-experiments/`
  (`ke2a_46_loo.py`, `ke2b_1034_audit.py`, `ke1_spanning.py`,
  `ke2a_results.json`, `ke2b_results.json`, `ke1_results.json`).
- Report-inbox note per REPORTING.md: `report_inbox/redteam-ke2-ke1.md`.
- Verdicts returned to the coordinator with leg counts and blast-radius notes.

— Red-team assumption killer, 2026-10-07
