# HOMOPHONE-SET BATTERY (sets A/B) — VERDICT

**Executor:** homophone-battery · **Date:** 2026-10-07 · **Round:** 13 (council work order 2)
**Stream:** repaired 1,847-pair (`code/side-keyhunt/repaired_offsets.json`), rebuilt via
`code/council/drag/common.py::load_stream` (asserts: 1847 pairs, 96 groups,
pairs[754:760]=la-première). **Corpus:** clean diplomatic pool per PREREG (F77: v8 "ment" VOID).
**Artifacts:** `PREREG.md` (bars), `battery_stats.py` → `battery_results.json`,
`battery_frames.py` → `battery_frames.json`. All counts re-derived; no standing numbers reused.

**Drag status:** `code/council/drag/drag_hits.json` LANDED mid-battery (9 primary, 0 veto;
bar k≥3, contra==0). **Zero hits involve 33, 86, 48, or 94** (hits: "le prince"×2,
"tout ce qui"×4, "par ce que"×3 — groups {77,81,87},{24,87,64},{79,87,64},{96,87,46}).
Nothing to fold in. Disclosed per work order.

## Pre-registered bar compliance note

The PREREG set marginal-homogeneity bars (χ² p>0.05 pass / p<0.01 split). The work order's
frame test ("does 86 parse in 33's 'pour'-frames") is intrinsically JOINT — a frame is
(pre, suc), per F59's per-window discipline. The joint (pre,suc) analysis below is the
primary battery; marginals are supplementary. Where the joint and marginal tests disagree,
the joint governs (it is the sharper, work-order-literal test). This refinement is
disclosed, not post-hoc: the PREREG already named "frame-interchangeability legs" as
PROMOTE requirements.

---

## SET A {33, 86} — verdict: **SPLIT** (same class, different values)

Contact sim 0.702↔0.702 (mutual #1 NN — the table's "strongest set"). n33=25, n86=32.

| # | Test (pre-registered) | Result | Reads |
|---|---|---|---|
| 1 | Uniformity χ² vs uniform | χ²=0.8596, df=1, **p=0.3538** | Re-derives table's χ²=0.86/p=0.35 exactly. 1690 uniformity HOLDS. |
| 2 | Runs (cycling vs clumping) | R=28, E=29.07, SD=3.68, **z=-0.291** | Interleaved. True cycling, not positional clumping. |
| 3 | Predecessor marginals χ² | 6.573, df=4, **p=0.160** | Not rejected — but 77→86 ×5 vs 33←77 ×0 sits inside it (see 6). |
| 4 | Successor marginals χ² | 6.151, df=6, **p=0.407** | Not rejected. |
| 5 | **Joint (pre,suc) frame overlap** | 19 + 28 = 45 distinct frames, **2 shared** (4.4%); disjoint frac **0.9556** | Shared: ('67','29') [3 vs 1], ('67','66') [1 vs 1]. |
| 6 | 86 in 33's char-frames (≥2) | **1/11**, binomial p=**0.0017** | 86 significantly depleted in 33's frames. |
| 7 | 33 in 86's char-frames (≥2) | **0/6**, binomial p=**0.0313** | 33 significantly depleted in 86's frames. |
| 8 | Fisher: 33 depleted in 77-frames | 0/25 vs 5/32, p=**0.0481** | 77="le"-frames are 86-only. |
| 9 | Fisher: 86 depleted in 33's pour-successors {16,79,21} | 0/12 vs 6/8, p=**0.0007** | 86 never takes 33's dominant pour-completions. |
| 10 | Pour-frame successors | 33: {16×2,79×2,21×2,01,96}; 86: {56×4,29×2,59,50,48,70,06,52} | **Disjoint.** Zero overlap in 20 pour-frames. |
| 11 | 29-completion frames | 33-29 ×5 (pre: 67×3,37,47); 86-29 ×4 (pre: 77,00×2,67) | Shared ('67','29') only. |
| L1 | 86 in 33's signature frames | 86: pour×12, 29×4 | Pre-existing (F40); circular as a confirming leg. |
| L2 | 33 in 86's signature frames | 33←77: 0/5; 33→56: 0/4 | **FAIL.** |

**Why SPLIT, not PROMOTE:** Tests 1–4 (distribution-level) all pass — uniformity, cycling,
marginal homogeneity. But the frame battery (tests 5–10, the work order's literal test)
fails decisively: 86 does not parse in 33's (pre,suc) frames and vice versa, at
p=0.0017/0.031 on characteristic frames and p=0.0007 on pour-successors. Under the lane's
standing Fork-S model (F79 GRANT implies 33=stem; F22 sub-word chunks), disjoint
completions in pour-frames mean different infinitives → different stems → not the same
cell. The 0.70 contact similarity is CLASS-level (both verb stems in infinitive frames),
not value-level. This is the 06/86 pattern (F40: same class, complementary distribution),
not the 47/87 pattern (same value, positional). **F60's lesson is confirmed in the
positive direction: contact similarity was necessary (all distribution tests pass) but
not sufficient (frames do not interchange).**

**Why SPLIT, not KILL:** The pairing is real — mutual nearest neighbors at 0.702,
shared predecessors (00: 8 vs 12; 67: 6 vs 3), shared suc==29, shared ('67','29')
"veut [stem]er" frame. KILL is for spurious similarities ({24,79}-style); this one is
systematic class resemblance.

**Implication for 33's value:** 33 is its OWN infinitive stem, not 86's homophone.
The 8 "pour 33" frames are 33's alone — the identifier33 infinitive hunt proceeds on
those 8, not 20. 86's 12 "pour 86" frames belong to a different stem (verb-stem-class
per F40 stands). The shared ('67','29') frame is consistent with different infinitives
after "veut" (cf. "veut parler" vs "veut donner"). **Do not merge 33+86 windows in any
downstream ID battery.** The Table Reconstructor's §b {33,86} proposal is retired as a
homophone set; reclassify as class-mates.

**Falsifier that would overturn:** a second independent frame type (beyond '67'-governed)
where 33 and 86 interchange at 1690 rates, or a value ID for 33 that also parses 86's
77-frames and 56-frames.

---

## SET B {48, 94} — verdict: **SPLIT (class-level, not value-level)**

Contact sim 0.643↔0.643 (mutual #1 NN). n48=38, n94=37. 94="ne" prov-strong;
48≠"ne" kill-grade (F60). **PROMOTE pre-barred** (would require 48="ne").

| # | Test (pre-registered) | Result | Reads |
|---|---|---|---|
| 1 | Uniformity χ² vs uniform | χ²=0.0133, df=1, **p=0.9081** | "Near-perfect" re-derived. |
| 2 | Runs (cycling vs clumping) | R=37, E=38.49, SD=4.30, **z=-0.347** | Interleaved. |
| 3 | Predecessor marginals χ² | 7.518, df=8, **p=0.4819** | Indistinguishable. Top: 94: 62×9,12×3,42×3,82×3; 48: 62×6,12×5,82×4,32×4. |
| 4 | Successor marginals χ² | 7.261, df=8, **p=0.5088** | Indistinguishable. |
| 5 | **Joint (pre,suc) frame overlap** | 32 + 36 = 67 distinct, **1 shared** (1.5%); disjoint frac **0.9851** | Shared: ('65','29') [1 vs 1] — and that frame is tense for 94="ne" (see below). |
| 6 | 48 in 94's char-frames (≥2) | **0/10**, binomial p=**0.00085** | 48 significantly depleted in 94's frames. |
| 7 | 94 in 48's char-frames (≥2) | 0/4, p=0.0659 | Marginal depletion. |
| 8 | 48 in 94's frames, value V≠ne | Joint frames disjoint → no substitution parse | See "value" below. |

**Why SPLIT:** 48 and 94 are statistically interchangeable at the DISTRIBUTION level
(uniformity p=0.91, runs z=-0.35, marginals p≈0.5, mutual NN) — a real, systematic
relationship, not a spurious one. But they are NOT homophones: F60 kill-grade fixes
different values, and the joint frames are 98.5% disjoint (48 depleted in 94's
characteristic frames at p=0.00085). The similarity is CLASS-level: both are
pre-verbal monosyllables drawing from the same predecessor/successor pools ("on",
"m", etc.) while occupying different (pre,suc) combinations — exactly what two
different words in the same slot look like. Neither 48 nor 94 follows "pour" (0× both),
consistent with the pre-verbal-particle class.

**The "different value" test (work order):** At the joint level, 48 does not occur in
94's frames, so there is no "48 parses in 94's frames" to gloss — the frames are
disjoint. At the marginal level, 48 shares 94's predecessor pool (notably 62="on" ×6
vs ×9). In the shared marginal "on _" slot, 94="ne" parses ("on ne") while 48 parses
as no tested value (F83 Path A fenced all 10 "on 48" syllables). **48's value is
constrained, not identified:** it must be a ne-CLASS sequential item (pre-verbal,
ne-like marginals) with its own joint frames, and ≠"ne".

**Implication for 48's identity:**
- The "de ce que" islet (@863, frame ('74','47')→46) is **48-specific**: 94's 37 windows
  never precede 47. The LEAD-weak islet survives this battery untouched — and the SPLIT
  verdict is compatible with it (48 has its own frames because it has its own value).
- The ne-like marginals (p≈0.5 indistinguishable from "ne") CONVERGE with the blitz's
  S2 adverse ("on-48"×6): a clean syllable reading has no account of 48 occupying
  word-level pre-verbal slots. This tensions (not kills) the vowel-initial syllable
  tier — any syllable candidate must explain ne-like sequential distribution.
- H_stem (verb stem, UNTESTED per blitz): a stem occupies the verb slot, not the
  pre-verbal particle slot; 48's ne-like marginals tension it the same way. Testable
  prediction banked: if 48 is H_stem, its "ne-like" marginals must come from a
  construction where stems precede verbs (e.g. auxiliaries) — name it or drop it.
- Cleanest open direction (not a promotion): another pre-verbal particle/pronoun-class
  word with ne-like distribution, ≠ne, ≠de-unconditioned. Adjudicator's call whether
  to open that battery.

**Falsifier that would overturn:** a (pre,suc) frame with ≥3 windows where 48 and 94
interchange at 1690 rates with distinct-but-both-grammatical values, or a 48 value ID
that parses in 94's ('62','79')/"on ne" frames.

---

## Cross-set notes

1. **F60's lesson, both directions:** {33,86} shows contact similarity + full
   distribution-level agreement still failing at the frame level (necessary ≠
   sufficient). {48,94} shows distribution-level indistinguishability coexisting with
   kill-grade different values. The frame battery (joint (pre,suc)) is the discriminator
   the contact vector is not.
2. **1690 uniformity is confirmed as necessary-but-insufficient** in both sets
   (p=0.35 and p=0.91, both pass; both sets still split).
3. **Table-reconstruction §b updates:** {33,86} → SPLIT (class-mates, cf. 06/86);
   {48,94} → SPLIT (class-mates, ne-distributed); {47,87} remains the positional-allophone
   prototype. Proposed §b status changes: move both sets from PROPOSE to SPLIT with the
   class/value distinction recorded.
4. **No coordinator-applied bars were used;** per lane rule, these verdicts need the
   adjudicator's ruling before entering the status line. ≥2 independent legs support
   each SPLIT (setA: tests 6+9+10; setB: tests 6+8+F60).

## Files
- `code/crowd13/homophone-ab/PREREG.md` — pre-registered bars (written before battery stats)
- `code/crowd13/homophone-ab/battery_stats.py` → `battery_results.json` — uniformity, runs, marginals
- `code/crowd13/homophone-ab/battery_frames.py` → `battery_frames.json` — joint frames, binomial/Fisher
- `code/crowd13/homophone-ab/VERDICT.md` — this file
