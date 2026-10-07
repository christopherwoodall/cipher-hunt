# RED-TEAM ADJUDICATION — Bedrock fleet (2026-10-07)

Adjudicator's own work: fresh Python, no verifier code imported or copied, from
primary sources only (`data/upstream-ct_R5005.digits.txt`,
`data/upstream-offsets.json`, `code/side-keyhunt/repaired_offsets.json`,
`code/crowd4/phase_map_repaired.json`, `code/crowd/contactor_results.json`).
Cross-checked against both verifier artifacts, NOTES.md, STATE.md, REPORT.md,
and the cited lane code.

## 1. The six stale counts — CONFIRMED (genuine staleness)

Independent recomputation (fresh pairing code, both parses):

| group | claimed | repaired (mine) | old parse (mine) | claim == old? |
|---|---|---|---|---|
| 64 | 46 | **47** | 46 | yes |
| 00 | 54 | **55** | 54 | yes |
| 11 | 44 | **45** | 44 | yes |
| 82 | 38 | **39** | 38 | yes |
| 34 | 10 | **11** | 10 | yes |
| 29 | 47 | **45** | 47 | yes |

Spot-verified byte-level (direct `==` string scan on the repaired stream):
n00=55, n64=47. Matches both verifiers exactly.

Ruling: **CONFIRMED**. Every failing value equals the pre-repair 1846-pair
count exactly — the lane updated n62 (34→35) and n06 (46→44) after F32 but left
these six at pre-repair values. Not a derivation error; an incomplete
post-repair sweep.

Bonus correction (ranks): the Phase-A crib-block rank claims are stale AND were
partly wrong even under the old parse. Repaired-parse competition ranks
(1 + #groups strictly higher), recomputed by me: **11→4, 70→51, 82→9, 34→69,
29→4, 40→34, 46→19, 00→1, 24→2, 64→3, 87→15**. (Old-parse competition ranks were
11→6, 70→52, 82→9, 34→71, 29→3, 40→34, 46→19 — so the claimed "rank 56/8/70/2"
were never exactly right under either parse; the rank convention was never
pinned.) Recommend: recompute all rank claims under a stated convention.

## 2. Blast radius — per-cite verdict

| # | cite | stale number | corrected | verdict | note |
|---|---|---|---|---|---|
| 1 | NOTES.md:24–26 Phase-A crib block (counts + ranks + "29=er at rank 2…top French syllable") | ×44/×38/×10/×47 etc. | ×45/×39/×11/×45; ranks 4/51/9/69/4/34/19 | **verdict stands** | qualitative claims hold: all seven cribs present; 29=er at rank 4/96 is still a top French syllable. Numbers must be corrected |
| 2 | NOTES.md:44–45 H1 "82=m → 16, 11/38 (29%)" | 11/38 | **11/39 = 28.2%** | **verdict stands** | H1 PLAUSIBLE (1/4), not confirmed; rounding-only change |
| 3 | NOTES.md:66–67 erratum prose "(the 44 is the frequency of 11=la itself)" | 44 | **45**; P(87\|11)=7/45=0.156 | **verdict stands** | prose correction only; the erratum's substance (ratio direction) unaffected |
| 4 | NOTES.md:166–172 / STATE.md Attempt-3 H3 legs | rank(64)=4; "28/28 distinct followers/predecessors"; top-follower share 0.07; P(87\|64)=0.109 | **rank 3**; 28 followers/**29** predecessors; share **0.064**; P(87\|64)=5/47=**0.106** (recomputed by me from repaired stream) | **verdict stands** | all four legs still hold qualitatively (top-word band, #1 follower of ce, negative control 46→64=0, free-word profile). 64="qui" is provisional anyway, demoted on factor-2-band grounds (F20) unrelated to n64 |
| 5 | NOTES.md:187, 800 (F17) "(00 leads at 54)" | 54 | **55** | **verdict stands** | "24 rank 2/96" holds (verifier A); 00 still rank 1 |
| 6 | `code/crowd4/closer64_87_results.json` (closer battery) | freq64=46; P(64)=46/1846=0.02492; P(29\|64)=3/46; binom_ge_3_46_* | 47; 47/1847=**0.02545**; 3/47=**0.0638**; n=47 | **verdict stands** | stale artifact — the script loads the OLD offsets via `crib_attack.load_pairs` (old-parse loader), so the recorded JSON is pre-repair. L4 binomial exclusion *strengthens* marginally with n=47. The battery's downstream use (64="qui" → demoted provisional) rested on the factor-2 band, not n64. **Re-run under repaired offsets** |
| 7 | NOTES.md:340 "29=er 182× and 82=m 60× over era" | — | **~175×** and **~62×** (scale by 45/47 and 39/38) | **verdict stands** | still ≫ — calibration finding (rigid syllabification DEAD, F30) unaffected |
| 8 | NOTES.md:440 + `code/sidepath/phonetic_rules.json` F-C "cipher 29=er at 2.55% (rank 3), 67× mismatch" | 2.55%, rank 3, 67× | **2.44%** (45/1847), rank 4, **~64×** | **verdict stands** | segmentation-mismatch finding unaffected |
| 9 | NOTES.md:88–89, 742–744 (F11); STATE.md:63 "A→C→B→A … chi²=181.3" | old-parse values | repaired: **A→B→C→A, chi²=366.3** (4df, n=1514) per B; lane's REPORT.md already carries this as "F11 (revised)" | **superseded — update prose** | structural verdict (3-phase rotation exists) stands; the direction name + chi² belong to the old parse |
| 10 | NOTES.md:1091–1092 (F43); STATE.md:16; REPORT.md:620–621 lag-3 "z=+5.6 (0.4219/0.3530), p≈1e-8" | decimals | B: z=**4.77** (obs 0.4048/exp 0.3491) on lane labels; z=**4.6** own labels | **verdict stands, decimals soften** | significance (z≈+5, p~1e-6..1e-8) reproduces. **Lag-2 z=−3.18 was not recomputed by either verifier — UNCHECKED, flag it** |
| 11 | `code/crowd3/morphologist_results.json` (`"pairs":1846`, counts 06=46/29=47/82=38) | old parse | 1847; 06=**44**, 29=**45**, 82=**39** | **verdict stands** | stale artifact (old-parse loader). Verdicts were red-team-adjudicated; era legs shift ~4% (e.g. 06 rate leg 1.26×→1.21×) — no flip. **Re-run under repaired offsets** |
| 12 | STATE.md checkpoint Attempt-3 "rank(64)=4" | 4 | **3** | **verdict stands** | leg-strengthens directionally (top-word band) |
| 13 | REPORT.md:121 "(rank 2 on the old parse)" | — | rank 4 on repaired | **honest as written** | REPORT.md already marks old-parse counts explicitly; only the "repaired-parse counts in fig 1" needs the fig to exist — verify fig 1 is in report_assets/ |

Bottom line for blast radius: **zero verdict flips**. Every PROMOTE/DEMOTE/KILL/NULL
survives its correction. The damage is confined to prose numbers, two stale
result-JSON artifacts (#6, #11), and rank claims.

## 3. Cycle direction naming — AMBIGUOUS-as-contradiction; labeling artifact

Facts:
- F11 (old parse, old Jaccard labels): A→C→B→A, P(A→C)=0.418, P(C→B)=0.450,
  P(B→A)=0.476, chi²=181.3/4df. Confirmed in `code/crowd/contactor_results.json`
  (`block_transition_counts`: A→C=268 dominant from A, C→B=252 from C, B→A=243
  from B).
- Repaired parse, `phase_map_repaired.json` labels: A→B 0.545, B→C 0.498,
  C→A 0.624, chi²=366.3/4df, n=1514. Recomputed exactly by B; my own transition
  table from the repaired stream matches B's P matrix to the printed decimal.
- **A pure label permutation cannot reverse a 3-cycle's orientation**
  (A→C→B→A reversed is A→B→C→A, and no permutation of {A,B,C} maps one to the
  other while preserving the labels). So this is not *just* a relabeling of one
  matrix — the repaired clustering (61/96 groups changed phase per the lane's
  own flag) is a genuinely different partition.
- B's independent Hellinger k-means found the same *package* (3 clusters,
  chi²=555.4, suppressed self-transitions) with a dominant 0→1→2→0 cycle, while
  the cosine variant put the *reverse* direction on top (0→2→1→0: 1.766 vs
  0→1→2→0: 0.71). **Direction itself is clustering-fragile.**

Ruling: **not a real contradiction of the phenomenon; the direction name is a
labeling/clustering artifact.** The robust, labeling-independent claims are:
(i) three phases emerge, (ii) self-transitions suppressed, (iii) a dominant
directed 3-cycle with chi² ≫ 1e-6 across parses, labelings, and metrics
(181.3 old / 366.3 repaired / 555–561 independent). The lane must **stop
asserting a fixed named direction as an intrinsic property**.

Recommended standing wording (extends REPORT.md's already-revised F11):
> "3-phase rotational contact structure: a dominant directed 3-cycle,
> chi²=366.3 (4df) under `phase_map_repaired.json` (reproduced z≈+5
> independently; old-parse banked value chi²=181.3 with a different naming).
> Cycle direction names (A→C→B→A vs A→B→C→A) are labeling-relative and
> clustering-fragile (61/96 groups changed phase on re-clustering; an
> independent geometry flips the dominant direction) — do not cite a fixed
> direction; cite the rotation."

NOTES.md:88–89, 742–744 and STATE.md:63 should adopt the REPORT.md revised-F11
wording. REPORT.md Fig-6 caption and the revised F11 already say this —
they are the standing text; the other two files lag.

## 4. Lag-3 decimals — significance STANDS; exact decimals UNCONFIRMED

- Claimed: P(same phase at lag 3)=0.4219 vs 0.3530 Markov-expected, z=+5.6, p≈1e-8.
- B (lane labels, A/B/C positions only): obs 0.4048 vs exp 0.3491, z=**4.77**.
- B (own independent labels): obs 0.4344 vs exp 0.3824, z=**4.6**.
- B's diagnosis: residual gap likely from R-class handling or label version.
  Both derivations give z≈+5, p~1e-6..1e-8 — the "genuine period-3 rhythm"
  verdict reproduces at the order-of-magnitude level; the exact decimals do not.

Ruling: **keep the significance claim, soften the decimals.** Recommended:
"lag-3 same-phase excess z≈+5 (p~1e-6–1e-8 depending on label version; lane's
pinned value z=+5.6 under its own labels)". **Lag-2 z=−3.18 was checked by
neither verifier — flag as UNCHECKED**, not as refuted.

## 5. The repair premise — epistemic status CONFIRMED

Both verifiers converge: the F32 repair is **VALID-given-premise** (crib occurs
twice in the raw stream; repaired parse lands `11 70 82 34 29 40` on rows
a5_03/a6_03 at pairs 754/1034; original offsets leave the a5_03 occurrence
off-phase) and the premise — that the erased pencil gloss sits over row a5_03 —
is **UNVERIFIABLE from available sources** (no manuscript images re-examined).

Recommended standing wording (REINDEX.md already records this correctly; elevate
it to STATE.md standing facts and the F32 mentions):
> "F32 repair is **conditionally canonical**: valid if and only if the
> gloss-line identification (erased 'la première' over row a5_03, per
> Bourdeau's REINDEX notes) is correct. Manuscript-image verification is the
> standing unblocker; if the line-tag is wrong, the 1846-pair parse revives.
> All repaired-parse findings inherit this conditionality."

Also one task-text correction (from A, verified by me): the original-offset
stream has the crib once at **old-index 1033** — the "1034" in the task text is
the new-index value after the +1 shift. F12's prose already carries the
"@1034 (old @1033)" clarification in the remap table.

## 6. Verifier independence — CONFIRMED, no derivation ambiguity

A and B used separately written code (fresh pairing logic in both; B adds
independent k-means geometry). Overlapping facts and their agreement:

parse 1847/96 ✓ · repair locality (a5_03 only, +1 pair) ✓ · crib pairs
754/1034 and rows a5_03/a6_03 ✓ · raw crib at 1532/2108 (A) ✓ ·
n64=47, n11=45 ✓ · n87=32, n96=21, n46=29, n77=44 ✓ ·
gloss-premise UNVERIFIABLE / repair VALID-given-premise ✓ ·
crib-position byte identity with lane artifacts (frenchman62_leg3, A) ✓.

**Zero overlapping disagreements.** No derivation ambiguity found — the six
mismatches are lane staleness, not verifier error. (Disjoint fact sets:
A verified windows/bigrams/trigrams; B verified phase structure/rotation —
both PASS.)

## Bottom line

**The foundation is solid.** The parse, transcription, repair validity (given
its recorded premise), crib positions, group counts (corrected), rank-1/2,
windows/bigrams/trigrams, and the rotation/lag-3 packages all re-derive
independently. The six mismatches are genuine post-F32 staleness in prose and
two old-parse artifacts — and **no downstream verdict changes** when corrected.

**Must be corrected before building further (blocking nothing, but don't
let it rot):**
1. NOTES.md Phase-A block: six counts + seven ranks → repaired values
   (n64=47, n00=55, n11=45, n82=39, n34=11, n29=45; ranks 4/1/4/9/69/4/34/19),
   pin a rank convention.
2. NOTES.md F11 + STATE.md:63: adopt REPORT.md's revised F11 wording
   (A→B→C→A under repaired labels, chi²=366.3; direction names
   labeling-relative).
3. Lag-3 decimals: soften to z≈+5 (p~1e-6–1e-8); mark lag-2 z=−3.18 UNCHECKED.
4. Re-run `code/crowd4/closer64_87_results.json` and
   `code/crowd3/morphologist_results.json` under repaired offsets
   (both currently old-parse artifacts via `crib_attack.load_pairs`).
5. Elevate the F32 conditional-canonical wording into STATE.md standing facts.
6. F17 "00 leads at 54" → 55; H3 "rank(64)=4" → 3; H1 "11/38 (29%)" → 11/39
   (28.2%); phonetic-rules "2.55%/67×" → 2.44%/64×.
