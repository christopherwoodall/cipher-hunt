# BREAK THE FRAME — The Assumption Killer's Attack Plan

**Role:** red-team cryptanalyst, reporting directly to the parent. No coordinator.
**Date:** 2026-10-07. **Lane:** zeschau-seebach-1841 (R5005).
**Standing order honored:** null rounds do not stop the lane. This document does not
stop it either — it tells it where the floor might be missing.

**Thesis:** Ten null rounds is the signature of a local maximum. The lane's
methodology (pre-registered bars, red-team adjudication, falsifiers) is excellent
*within* its frame. This plan attacks the frame itself: the load-bearing
assumptions nobody is checking because they were set before round 1.

---

## 1. Ranked assumptions by P(wrong) × cost-if-wrong

| # | Assumption | P(wrong) | Cost | P×C | Status |
|---|---|---|---|---|---|
| 1 | The 68 unverified per-row EM offsets (upstream "EM on pair frequency") | 0.20 | 0.85 | **0.17** | UNTESTED — Kill Experiment 1 |
| 2 | Anchor ground truth: 46=que (single pencil gloss); @1034 crib = "la première" (digit identity); anchors never leave-one-out tested | 0.12 | 0.80 | **0.096** | UNTESTED — Kill Experiment 2 |
| 3 | By-ear syllabification is the right (and consistent) model of the clerk | 0.18 | 0.50 | 0.09 | Actively probed, never killed — sketched probe §5 |
| 4 | Gloss (i) line-tag: the erased "la pre m i er e" belongs on row a5_03 | 0.07 | 0.60 | 0.042 | Unverifiable without manuscript images — blast radius §4 |
| 5 | 96-group closure: no nulls (petit-chiffre doctrine F35 + upstream null-digit negative) | 0.12 | 0.30 | 0.036 | Noted §5 |
| 6 | Diplomatic register is right (Nesselrode v8, Guizot despatches) | 0.04 | 0.70 | 0.028 | Strengthened, not attacked |
| 7 | The despatch is entirely French (Zeschau wrote German elsewhere) | 0.08 | 0.30 | 0.024 | Noted §5 |
| 8 | Digit transcription is image-accurate (bedrock verified internal consistency only) | 0.04 | 0.30 | 0.012 | Noted §5 |

Probabilities are the Killer's honest priors, not lane doctrine. Costs are
fractional: 1.0 = lane restarts from the digit stream.

**What the ranking says:** the two scariest things are (1) the 70-parameter
offset model nobody validated, and (2) the anchor set nobody stress-tested.
Both are pre-round-1 inheritances. Everything the lane does well (rounds 1–12)
sits on top of them.

---

## 2. KILL EXPERIMENT 1 — The 70-row offset model

### The assumption under attack

The canonical parse pairs each manuscript row independently (`[s[i:i+2] for i in
range(o, len(s)-1, 2)]`), with per-row offsets `o ∈ {0,1}` chosen by upstream's
EM "on pair frequency." This drops **70 digits** (31 leading-offset + 39
trailing-odd) and yields 1,847 pairs. Only **2 of 70** rows have manuscript
constraints: a5_03 (gloss i, repaired 1→0) and a8_05 (gloss ii). The other 68
rows' offsets rest on an instrument the lane itself voided (F26:
"EM-on-pair-frequency is exactly the kind of weak instrument this lane has
already voided elsewhere").

### The Killer's work (all recomputed from `data/upstream-ct_R5005.txt`)

**Fact 1 — the alternative is viable, not garbage.** Continuous pairing of the
3,764-digit stream (0 parameters, 0 dropped digits) yields 1,882 pairs and:

| Check | Lane (M0) | Continuous (M1) |
|---|---|---|
| Crib `11 70 82 34 29 40` occurrences | 2 (@754, @1034) | 2 (@766, @1054, raw 1532/2108) |
| "par ce que" `96 87 46` | 3 | 2 |
| `24 87 64` formula | 3 | 2 |
| Pair IC | 0.0142 | 0.0133 (within 7%) |
| Shared bigram tokens | — | 1,148 / 1,846 (62%) |
| Gloss (i), raw 1532 even | ✓ | ✓ |
| Gloss (ii), raw 3453 odd pair-start | ✓ | ✗ (the single falsifier) |

M1 satisfies every manuscript-grounded fact except gloss (ii). A single
parity flip (one dropped digit) anywhere in raw (2108, 3453) fixes (ii) while
preserving the crib — so **M1+1flip (1 parameter) satisfies both glosses**.
M0 uses 70 parameters to satisfy the same two constraints.

**Fact 2 — the EM's 31 offset=1 choices are consistent with random.** 31/70 rows
at offset=1; implied global phase split 33/37. Under a weak unigram-pair
objective, ~35/70 offset=1 is the noise expectation. The lane has no evidence
the EM did better than chance on any individual row beyond the two glossed ones.

**Fact 3 — the crib cannot arbitrate.** Crib contexts under M0 and M1 are
byte-identical (`64 02 97 40 67 | 11 70 82 34 29 40` and `01 03 29 80 77 | 11
70 82 34 29 40` under both). The ground-truth positions are exactly where the
two models agree — the assumption is untestable at the only verified points.
This is what makes it insidious, not what makes it safe.

**Fact 4 — pilot of the spanning test: inconclusive (1–1–3).** Under continuous
pairing, 38 row boundaries have a pair spanning the boundary; 5 pre-flip ones
are anchored groups (82, 34, 77, 46, 29). Of their anchored bigram contexts:
1 French-plausible (`46→77` = "que le"), 1 French-implausible (`11→77` = "la
le"), 3 uninformative. This neither kills nor vindicates row-independence —
which is precisely why the full experiment must be run.

### The experiment (fully specified, pre-registered)

**Name:** Row-boundary spanning bigrams.
**Assumption under attack:** pairs do not span manuscript row boundaries
(per-row independent pairing; the 70 dropped digits are artifacts).
**Falsifier:** French-meaningful pairs spanning row boundaries.

**Procedure:**
1. Build M1+1flip: continuous pairing from digit 0, single digit dropped at
   row boundary b*, with b* ∈ (2108, 3453) chosen ADVERSARIALLY — the boundary
   maximizing the count in step 3 (give the alternative its best shot).
2. Extract all row-boundary-spanning pairs under M1+1flip (69 boundaries).
3. Count "gold spanning bigrams": bigrams (g1,g2) with both groups in the
   12-known set {11,70,82,34,29,40,46,87,64,96,59,77}, where the bigram spans a
   row boundary AND is French-plausible, defined pre-registered as: member of
   the 8 lane-confirmed bigrams {(11,70),(70,82),(82,34),(34,29),(29,40),
   (87,64),(87,46),(96,87)} OR attested >50× as a word bigram in the clean
   3.96M diplomatic corpus.
4. Also count French-IMPLAUSIBLE fully-anchored spanning bigrams (same 12-set,
   bigram attested 0× in the corpus and ungrammatical, e.g. "la le").

**Pre-registered bar:**
- If gold spanning bigrams ≥ 3 AND gold:implausible ≥ 3:1 → **REJECT
  row-independence.** The per-row offset model is wrong; pairs span rows.
- If implausible ≥ gold → **row-independence HOLDS** (spanning pairs are chance
  juxtapositions; M0's model justified).
- Else → **INCONCLUSIVE** (the data cannot distinguish; the 68-offset model
  stands as a permanent caveat, and the parsimony argument below remains).

**Parsimony rider (no experiment needed, pure logic):** M0 spends 70 parameters
to satisfy 2 gloss constraints. M1+1flip spends 1. Under M0's null, the 31
offset=1 rows are EM noise. The lane's "conditionally canonical" caveat covers
the gloss premise but NOT the offset-model premise — the deeper conditionality
was never written down. Even if the experiment is inconclusive, STATE.md must
carry: "canonical parse is conditionally canonical on (a) the gloss line-tag
AND (b) upstream's 70 EM offsets, of which 68 are unvalidated."

**If it kills:** blast radius is SEVERE but RECOVERABLE (§4, second scenario).

---

## 3. KILL EXPERIMENT 2 — The anchor ground-truth audit

### The assumption under attack

Seven values treated as ground truth: 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e
(one erased gloss, "la pre m i er e", + digit identity at a second position),
46=que (a second erased gloss, single occurrence). The 7 anchors are the
lane's highest-leverage facts — every battery conditions on them — and they
have NEVER been stress-tested. Two specific fragilities:

**Fragility A — 46=que rests on one pencil mark.** It is the highest-leverage
anchor (que-frames underpin 87=ce via 87→46 ×3, 00=pour via 00→46 ×4, ISLET 10
depends on 46="que" GT). Supporting legs cited by the lane are circular (they
established the provisionals). Adversarial note: 59→46 ×2 TENSIONS 46=que
(round 7: "est que" adverse). The Killer's check: 46 occurs 29×; the despatch
does NOT end with it (last pair is 93, row a8_11 — the "dangling que" anomaly
does not exist; gloss (ii) is mid-despatch at row a8_05's end).

**Fragility B — @1034 = "la première" is digit identity, not manuscript.**
The pencil only glosses @754. @1034 is inferred because the digits match. But
F33 establishes CONDITIONED polyvalence (one group → multiple values by
context) — so digit identity does not entail value identity. The Killer's work:
contexts extracted — @754: pre=67/suc=20; @1034: pre=77(le)/suc=17; internal
contexts identical. Current islet registry: NONE of {11,70,82,34,29,40} has a
conditioned reading. Clean on today's registry — but the crib groups were never
TESTED for polyvalence (they're GT, assumed fixed). The test below forces it.

### The experiment (fully specified, pre-registered)

**Name:** Anchor leave-one-out + @1034 polyvalence audit.
**Assumption under attack:** all 7 anchors are ground truth; @1034 reads "la
première".

**Procedure, Part A (46=que):**
1. DROP 46=que from the anchor set. Re-run the 87=ce battery EXCLUDING every
   46-involving leg (the 87→46 ×3 "ce que" leg is voided for this run).
2. If 87=ce still promotes (≥2 independent legs without 46) AND 64=qui holds,
   proceed. (If not, 46=que was load-bearing for the provisionals — escalate
   immediately; the lane's 12 values are built on sand.)
3. Re-derive 46: given 87=ce, 87's followers are 64 (qui) ×5 and 46 ×3. Test
   46 against French P(·|ce) profile AND 46's predecessor profile against
   French P(·|que)-predecessors, on the clean diplomatic corpus.

**Procedure, Part B (@1034):**
1. For each crib group g ∈ {11,70,82,34,29,40}, list every conditioning
   trigger in the islet registry (exact features: pre∈{...}, suc∈{...}).
2. Check g's @1034 context (pre=77/suc=17 for 11; pre=29/suc=17 for 40;
   internal for the rest) against every trigger.
3. Additionally run the registry's polyvalence TEST (not just its registry)
   on each crib group: the F33 battery (conditioned-vs-free) with the group
   as subject — the test the lane never ran because the groups are GT.

**Pre-registered bars:**
- Part A: 46=que is RE-DERIVED iff ≥2 independent legs (follower-profile +
  predecessor-profile, or French bigram rates at the lane's promotion bar)
  WITHOUT assuming it. If it fails: 46=que is demoted to "single-gloss GT"
  — usable, but STATE.md must flag that the lane's highest-leverage anchor
  rests on one erased pencil mark, and ISLET 10's dependency is marked
  conditional.
- Part B: if ANY crib group has a triggered conditioned alternative at @1034:
  the @1034 crib reading is COMPROMISED for that group → the "two occurrences"
  claim drops to one-and-a-half → re-derive treating @1034's compromised
  groups as unknown. If none: the two-occurrence claim is ROBUST (stated
  formally for the first time).

**The Killer's prior:** Part A re-derives (French "ce que" is too strong;
expect 2+ legs). Part B comes back clean (registry already checked by hand
above). The value isn't in expecting a kill — it's in converting "ground
truth" from a courtesy title into a tested claim. The lane promotes values on
≥2 legs; its own anchors should meet its own bar.

---

## 4. BLAST RADIUS — if the parse repair fell

**Scenario:** gloss (i) is mis-tagged (the erased "la pre m i er e" belongs on a
row other than a5_03). Then a5_03's offset reverts 0→1 (upstream EM), and:

**Direct (mechanical, bounded):**
- Pairs 748–772 (25 pairs, row a5_03) RE-PAIR to different content
  (old off-phase read `71 17 08 23 42 94 02` at old 753–759).
- The @754 "la première" occurrence is LOST. The crib count goes 2 → 1.
- Pairs ≥773: content IDENTICAL, indices shift −1 (pure renumbering).

**Anchors:** all 7 SURVIVE — 11,70,82,34,29,40 at @1034 (a6_03, untouched);
46 at a8_05 (untouched). The anchor set does not depend on the repair.

**Findings to redo (concrete list):**
- F26-14 chiasmus (67→11 @753 "immediately before the @754 crib") — @753 is
  inside the repaired region; the adjacency claim must be re-examined.
- Every battery that used @754 as a crib window (the "two occurrences"
  framing; @754-context legs).
- ISLET 3's W06 ([579,737,1183,1354]) — verified CLEAR of 748–772, no redo.
- Rotation/contact statistics — recompute; expect <5% shift (25/1,847 pairs).
- Report figures citing @754 — regenerate.

**Honest verdict: MODERATE and BOUNDED, not catastrophic.** The F32 repair was
minimal by design (one row, even digit count), so its failure is minimal too.
~1 round of re-derivation. The lane's "conditionally canonical" wording already
prices this in — this section is the receipt.

**Contrast — if KILL EXPERIMENT 1 kills M0 (the whole offset model):**
- SEVERE: all 1,847 pairs re-derived (~1,881 under M1+1flip); every positional
  finding re-mapped (indices shift non-uniformly); bigram/contact statistics
  recomputed; the 35 restored pairs analyzed for missed cribs; the islet
  registry rebuilt; all 12 rounds' batteries re-run under the new parse.
- RECOVERABLE: the 7 anchors survive (gloss-pinned); the methodology
  (pre-registered bars, red-team adjudication, falsifier discipline) survives
  intact; the corpora survive. ~2–3 rounds to rebuild. The lane's real asset
  was never its pair indices — it was its method. This is the scenario that
  justifies running Kill Experiment 1 NOW rather than after round 20.

---

## 5. Other noted risks (ranked, not fully funded)

**#3 — By-ear consistency (P×C 0.09).** The Frenchman proved over-splitting
(46=que writes /k/ separately); the model is "by-ear, approximately." Sketched
probe: for every putative /k/-initial syllable group, measure split-vs-merged
rate; pre-registered bar — if /k/-splitting is <80% consistent, by-ear is
UNRELIABLE as a tiling prior and every by-ear battery needs per-case
justification (no global "by-ear" premise). The lane's falsifier discipline
partially covers this; the probe makes it explicit.

**#5 — Nulls (0.036).** F35's "petit-chiffre has no nulls" is doctrine about
the family + upstream's null-digit negative. Sketched probe: null-hunt battery
— for each group with n<8, test contact-profile uniformity (a null's contacts
should be ~uniform random); pre-registered bar: any group with χ² uniformity
p>0.5 AND zero bigram structure gets a null workup. Cheap; never run.

**#6 — Register (0.028).** Now STRENGTHENED (Nesselrode v8 = full-1841
diplomatic French). Not attacked. Standing note: if Zeschau's idiolect
deviates (Saxon chancery Germanisms in French), the first symptom will be
systematic residual misfits in the best-supported islets — watch ISLET 10's
leftovers.

**#7 — German passages (0.024).** R5007/R5008 are German; R5005 is DECODE-tagged
French and the cribs are French. Sketched probe: scan the stream for German
function-word cribs (der/die/das/und) via the crib-derived inventory method;
any hit → the lane needs a language-segmentation pass before French batteries
run on those windows.

**#8 — Transcription (0.012).** Bedrock verified the transcription FILE's
internal consistency, not the reading of the manuscript. Single-digit errors
add noise, not bias — EXCEPT on crib rows, where the crib match itself
validates the digits. Standing caveat, no action without manuscript access.

**Structural caveat (not ranked): provisionals-as-GT creep.** The lane's
batteries increasingly condition on provisionals (87=ce, 64=qui, 96=par,
59=est, 77=le) as if GT; the methodology-ruling (B2) says a 7/7-matching table
that contradicts a provisional triggers review of the PROVISIONAL. The
islet registry records dependencies honestly ("If any falls, the dependent arm
re-opens"). The Killer's note: Kill Experiment 2's leave-one-out should be
extended to provisionals on a rotating schedule — no value should be both
load-bearing and untested. The red team owns this.

---

## 6. What the Killer actually believes

Ranked by expected information value, the lane should run:

1. **Kill Experiment 2 NOW** (cheap, decisive, high-leverage). Expected
   outcome: anchors re-derived, @1034 robust — but "ground truth" becomes a
   tested claim instead of a courtesy title. If 46=que wobbles, the lane
   learns its most important fact about its own foundation.
2. **Kill Experiment 1 NEXT** (moderate cost, existential). Expected outcome:
   probably inconclusive — but "probably" is not a result, and the parsimony
   rider (70 params vs 1) means the burden of proof is on M0, not on the
   challenger. The current state — 68 unvalidated offsets under a voided
   instrument — is the largest unpriced risk in the lane.
3. **Write the deeper conditionality into STATE.md** regardless of outcomes:
   "conditionally canonical on (a) the gloss line-tag AND (b) upstream's 70 EM
   offsets, 68 unvalidated." The lane prices (a); it does not price (b).

Ten null rounds built a magnificent instrument. This plan points it at the two
things the instrument was never calibrated against: the parse it reads through,
and the anchors it steers by. If both hold — and the Killer's priors say they
mostly will — the lane proceeds with a tested foundation instead of an
inherited one. If either breaks, it breaks early and cheaply, which is the
only way breaking is useful.

— The Assumption Killer, 2026-10-07
