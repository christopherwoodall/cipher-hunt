# RED-TEAM ADJUDICATION — Seebach word-pattern side fleet
Date: 2026-10-07. Adjudicator: red team (kill authority over every claim).
Scope: pattern-matcher (`matcher/`, inbox `report_inbox/pattern-matcher-proposals.md`)
and polyvalence-tester (`polyvalence/POLYVALENCE_REPORT.md`, inbox
`report_inbox/polyvalence-tester-verdict.md`).
Lane conventions applied: ≥2 independent checks before any promotion; provisional vs
ground-truth marked everywhere (NOTES.md/STATE.md). Positions below are OLD-parse
(1,846 pairs — the matcher ran pre-repair); F32 re-index: old n<748 unchanged,
old n≥773 → n+1. So @507 unchanged; @1035–1038 → @1036–1039; @1241 → @1242; @1402 → @1403.

Verification performed (not trusted on testimony):
- Re-derived the matcher's ground-truth control from `lexicon/lexicon.jsonl` directly.
- Re-ran `polyvalence/polyvalence_test.py` (deterministic; console output matches the
  report's §2 table exactly) and `polyvalence/synthetic_breakdown.py`.
- Recomputed per-pattern smart inflation for 3|AAB, 5|ABCDA, 3|ABA from the archived code.
- Rebuilt the canonical 1,847-pair stream from `code/side-keyhunt/repaired_offsets.json`
  and re-checked every tester islet spot-check count.
- Re-derived the @507 and cela+X lookups; inspected `code/crowd3/segmenter_results.json`
  boundary probs and Viterbi bounds at both cela+X spots.
- Enumerated all 26 stamped proposals from `matcher/match_results.json` (11 @cut 0.5,
  15 @cut 0.7, overlap 4 — counts verified).
- DISCLOSURE: re-running the two tester scripts overwrote `polyvalence/results.json`
  (deterministic-identical output, verified) and `polyvalence/synthetic_breakdown.json`
  (regenerated from current code; the prior archived JSON is not recoverable — the lane
  has no git here. The code is the source of truth; the JSON is regenerable.)

---

## RULING 1 — The matcher's control failure is SOUND (not fragile)

**Claim under test** (`report_inbox/pattern-matcher-proposals.md`, "Ground-truth control
fails"): the known word "première" tail @1035–1038 = 82-34-29-40 (m|i|er|e, four GT
anchors) returns zero lexicon candidates at every tier — therefore the encipherer's
by-ear units (standalone m, i) are absent from the lexicon's syllable inventory
('m' in 1 of 11,870 entries), and the instrument cannot be trusted on unknowns.

**Re-derivation (mine):** tail lookup m|i|er|e against `lexicon/lexicon.jsonl` →
0 hits orth, 0 hits phon. 'm' as a syllable: 1/11,870 entries — and that entry is the
word "m" itself (freq 125; the elision token m', per
`report_inbox/lexicographer-lexicon.md` caveats), i.e. ZERO polysyllabic words contain
a standalone-'m' syllable. Stronger than the matcher stated.

**The diérèse attack fails.** The lexicographer deliberately uses maximal diérèse
splitting — `i|è`, giving `pre-mi-è-re` (see `report_inbox/lexicographer-lexicon.md`,
"Enlightenment") — the most letter-splitting reasonable convention. It still yields
'mi', never 'm|i'. In "première" the 'i' follows a consonant ('m'), so no diérèse
convention applies at all. A standalone consonant 'm' as a syllable is phonotactically
impossible in French: no syllabifier, however aggressive, emits it. The gap is proven
by the pencil cribs themselves (82=m pinned as a unit), fully independent of the
lexicographer's choices. This is a true unit-inventory gap, not a syllabifier artifact.

**Scope refinement (not a fragility):** the control is effectively a SINGLE-unit test.
The 'm' gap drives 100% of the zero — 'i' is in-inventory (198 orth / 264 phon
entries), 'er' in 58, 'e' in 223. "FOUR ground-truth anchors" overstates the control's
breadth; it tests one inventory gap, not four. Conclusion unchanged.

**The tail (not the full word) is the correct, strongest control:** it gives the
instrument its best chance (4 groups vs the lexicon's 4 syllables for "première");
the full 6-group 11-70-82-34-29-40 word fails on n-mismatch as well. Both fail for the
same root cause. The matcher chose correctly.

**Prescription check:** the diagnosis (need the encipherer's own unit inventory) is
right, but the pointer is questionable — round-4 WO5 aims at `data/upstream-syll*.py`,
which N29 already suspects is NOT the encipherer's table (all three annealers failed
on it). The inventory must be LEARNED from cribs + recovered readings, not adopted
from upstream's 180-unit table.

**Minor nit (immaterial):** SELFTEST's "'i' in 205 entries" reproduces as 198 (orth) /
264 (phon) — counting-rule drift, not material.

**RULING 1 VERDICT: SOUND.** The control failure stands, is not fragile, and is the
binding constraint on the instrument. It is the fourth independent line converging on
F30 (by-ear cutting).

---

## RULING 2 — The 26 stamped proposals: ALL DEAD; the tester verdict resurrects none

26 = 11 (cut 0.5) + 15 (cut 0.7) proposal instances = 12 unique words, overlap 4
(@144 quiconque, @200 morcela, @239 laborieusement, @664 pionnier — verified in
`matcher/match_results.json`). Grouped by shared weakness:

**Class A — provisional-anchor echo (7 unique spans): "quiconque" ×7.**
Every instance anchors on 64=qui (PROV-STRONG) ALONE, 0 GT anchors; seven different
cipher words (64-41, 64-77, 64-98-65, 64-21, 64-02-58, 64-31-10, 64-47-68) all
"propose" the same lexicon word. 64=qui has re-promotion BLOCKED (N27). **KILL** —
not even lead-grade; pure method artifact.

**Class B — hapax accidents (freq ≤17, ≤1 GT anchor):** morcela (f1; 87 PROV-STRONG +
11 GT), laborieusement (f1; 11 GT), outrepassé (f1; 52 LEAD), envahi ×3 (f1; 34 GT),
apercevrions ×2 (f1; 46 GT), susquehanna (f1; 46 GT + 24 LEAD — register pollution, a
Tocqueville-americana token in a Saxon despatch), ancêtres (f5; 24 LEAD + 87
PROV-STRONG, 0 GT), perfectionnement (f2; 62 LEAD + 94 PROV-STRONG, 0 GT), prévienne
(f1; 70 GT + 94 PROV-STRONG), nécessairement (f17; 94 PROV-STRONG, 0 GT).
Verified per-proposal from `match_results.json`: ZERO have ≥2 GT anchors. None clears
the lane's ≥2-independent-checks bar. **KILL.**

**Class C — variant artifacts:** "pionnier" ×2 via V-orth-iersplit (flagged by the
matcher itself); "quiconque" via V-phon-finalmerge (2-syllable ki|konk coerced from a
3-syllable word). **KILL.**

**Does VALID-WITH-RESTRICTIONS resurrect any? NO.** The tester verdict governs RECALL
(words missed through polyvalence distortion); all 26 were found — none were missed.
The verdict adds no positive evidence for any candidate. Applied honestly, restriction
4 (group-level consistency) kills Class C HARDER: "pionnier" at [664,667] (03-62-06-00)
and [1534,1537] (41-62-06-21) needs 06="ni", inconsistent with every live 06 reading
(verb-stem class PROV per F25, restricted-"ent" PLAUSIBLE per N19, /mɑ̃/ KILLED per
N17). Restriction 5: exactly one proposal ("outrepassé") is in the 52 at-risk list —
freq 1, single LEAD anchor, no independent check. Dead.

The orthogonal control failure (Ruling 1) is the binding constraint — the tester
verdict's own §8 agrees. **All 26 stay dead.** Update the stamps from
PROVISIONAL-PENDING-POLYVALENCE-VERDICT to DEAD with class reasons; none enter the
lane even as leads.

---

## RULING 3 — The tester's 7 restrictions: adjudicated

**R1 — Use the polyvalence-expanded index. SOUND, necessary in the strong form.**
Two corrections: (a) the "acceptable alternative" (swallow ~0.5% recall) is valid ONLY
under per-position non-determinism; under a deterministic encipherer the at-risk loss
is 52/1597 ≈ 3.3% of poly-words and 100% on the at-risk list (the report's own §7
caveat). Recommend the expanded index unconditionally — it is cheap, exact, and
q-independent. (b) Implementability gap: the archived reachable-sets cover phon/orth
only, not the 8 by-ear variants the matcher actually queries — rebuild per variant
before use.

**R2 — Never naive pattern-expansion. SOUND, necessary.** Reproduced exactly:
3|ABA 23→4,659 (202x), 3|AAB 2→4,636 (2318x), 2|AA 4→3,222 (805x), 3|ABB 8→4,644
(580x) — from `polyvalence/results.json` reverse test.

**R3 — Candidate generation only from repetition-bearing patterns. DEMOTED to
instrument-level recommendation.** Sound design advice, but NOT a polyvalence gate
condition: the analysis shows non-repetition patterns suffer ≈1.00x inflation — no
polyvalence damage there. As a standing gate it is over-restrictive (it would forbid
anchored non-repetition lookups once the inventory is fixed). Scope it to the current
dictionary-alphabet instrument.

**R4 — Group-level consistency when 06/94/52/59 present. SOUND, necessary.**
Enhancement: tighten with the lane's F33 conditioning rules (94="en" iff pre=82 or
suc=87; 52="pas" iff negation-frame; 06 restricted-"ent" iff trigram-internal) — the
tester's per-position q model is coarser than the lane's conditioned polyvalence.
The expanded index (superset over all reachable patterns) stays correct regardless.

**R5 — Flag the 52 at-risk words. SOUND, necessary.** Verified: 52 unique words
(the §4 mechanism counts sum to 55 = overlap, consistent); "8 mechanisms" confirmed on
recount (the an/man + an/ant bullet holds two); every §4 named word reproduces in the
risk set.

**R6 — Re-run on model change. NECESSARY but INSUFFICIENT — missing parse-change
coverage.** The tester's islet spot-checks (§1) are on the OLD 1,846-pair parse. On
the canonical 1,847-pair parse (rebuilt from `code/side-keyhunt/repaired_offsets.json`):
06 ×44 (was 46), 94→59 ×3 (was ×2) — the se→52/59 weight basis changes n=5→n=6,
0.6/0.4→0.5/0.5; 94→82 ×4, 94→52 ×3, 94-82-06 ×3, 06→77 ×6, 06→11 ×4 unchanged;
06→29 ×4 (known, N29). Verdict is ROBUST to this (recomputed: worst case 0.380→0.375,
overall 0.995→0.9948), but inventories AND weights must be re-derived on the canonical
parse before any reuse. Extend R6: re-run on model, parse, or inventory change.

**R7 — Segmentation is the larger threat ("must tolerate n-mismatch"). Honest scope
delimiter, NOT an implementable restriction** — "tolerate n-mismatch" states no
mechanism. Keep as a fence on the verdict (the gate covers polyvalence only), not as a
gate condition.

**R8 — NEW (proposed): prefer the orthographic alphabet for repetition-pattern
candidate generation.** The report's §2 shows orth repetition-words survival = 1.000
("sé"/"se" distinct in orth — no split risk); ALL the split risk lives in the phon
alphabet. Use phon as backup only.

**Traceability flag (F26.6-class):** the report's §6 synthetic table does NOT
reproduce from the archived code. K=0 row ✓ (0.995 / 0.931 / 6.0x, all seeds). But the
repetition-survival column for K=3/10/30 (tabled 0.914 / 0.891 / 0.879) vs the code
(seeds 11/22/33): K=3 → 0.931–0.941, K=10 → 0.931–0.941, K=30 → 0.895–0.930. Max smart
inflation 6.0x ✓ at every K. The qualitative graceful-degradation claim holds
(arguably stronger under the code's numbers), but the tabled K≥3 numbers must be
REGENERATED, not cited. Minor: "all others ≤2x" (§3b) is actually ≤2.1x (4|ABCA) —
immaterial.

**Numbers that DID reproduce exactly** (re-run): §2 forward table — all 0.995,
at-risk 0.834, rep-at-risk 0.380, rep-all 0.931, islet06 0.993, islet94 0.992, islet52
0.994 (q=0.5, phon); control 200/200 unit survival; MC max|exact−mc|=0.0037. §3b smart
expansion — 3|AAB 2→12 (6.00x; new: ennemi/ennemis/néanmoins/passeports…),
5|ABCDA 3→13 (4.33x), 3|ABA 23→26 (1.13x).

**RULING 3 VERDICT: VALID-WITH-RESTRICTIONS stands**, with R1 strengthened, R3 demoted
to recommendation, R6 extended to parse/inventory changes, R7 fenced as non-gate, R8
added, and the §6 table flagged for regeneration.

---

## RULING 4 — Leads

**@507 NULL (77-62-94): re-derived, REFRAMED — zero constraining force on 77.**
The lookup is NULL only at T3 (62=on LEAD + 94=ne PROV-STRONG both pinned). At
T1/T2 (94=ne pinned, 62 free): 51 survivors, top "personne". 'on' is a healthy
inventory item (388 entries) — this is NOT the 'm' disease; it is a genuine lexical
gap: French has essentially no 3-syllable X|on|ne word with medial bare "on" (the
'on' always arrives with a consonant: bon-/con-/son-/ton-). Crucially, the NULL holds
for EVERY possible first syllable — it discriminates nothing among 77="pas"/"le"/"que"
or any other reading. It is fully explained by cutting mismatch: the lexicon cuts
per|son|ne; the cipher (frenchman's reading, already in the lane) cuts pers|on|ne.
**Ruling: not a 77-datum at all. Record as corroboration of F30 (by-ear cutting),
not as a 77 lead.** The matcher's "small datum for the 77 investigation" framing is
wrong. It also does not threaten 62="on" (LEAD) — the by-ear cut explains the miss.

**cela+X NULLs (@1241: 87-11-00-33; @1402: 87-11-00-11): NON-EVIDENCE, open
segmentation question.** The gluing is the SEGMENTER's own output, not a matcher
threshold artifact: Viterbi MAP bounds [...,1241,1245,...] and [...,1402,1406,...]
glue at both spots, and per-boundary probs after the 11 are 0.4082 / 0.4782 (<0.5 at
both cuts). Unresolved between (a) segmenter miss — plausible, control M1=0.72
(~28% miss rate) and 5/23 provisional recall — and (b) real 4-group words (another
F30 datum). Either way the NULL carries no lexical information and does not
discriminate 87=ce (the cela reading is intact regardless of what follows).
**Ruling: keep as open segmentation uncertainty, not a lead.**

---

## RULING 5 — FLEET VERDICT and merge recommendations

**What enters NOTES.md:**
- **N32 (null):** pattern-matcher HONEST NULL — upheld. Control failure sound
  (Ruling 1); 26 proposals dead by class (Ruling 2); 25 crib-drag targets 0
  proposals. The null is exemplary control-first work; its diagnosis (unit inventory)
  is the binding constraint. Files: `code/side-wordpattern/matcher/`
  (`matcher.py`, `match_results.json`, `README.md`).
- **N33 (gate, not a promotion):** polyvalence gate VALID-WITH-RESTRICTIONS —
  forward/reverse numbers verified by independent re-run (Ruling 3). Gates the
  instrument; promotes nothing. Files: `code/side-wordpattern/polyvalence/`.
- **F34 (finding, small):** @507 NULL reframed — explained by per|son|ne vs
  pers|on|ne cutting mismatch; zero constraint on 77∈{pas,le,que}; corroborates F30.
- **F35 (finding, process):** tester's islet inventories/weights are old-parse;
  se→52/59 basis changed n=5→n=6 (0.6/0.4→0.5/0.5); verdict robust (0.380→0.375)
  but re-derivation on the canonical parse is required before reuse (extends R6).
- **Adjudicated restrictions R1–R8** (Ruling 3) enter as the standing gate for any
  future pattern-matching work: R1 strong-form expanded index (rebuilt per variant),
  R2, R4 (+F33 tightening), R5, R6 extended, R8 new; R3 demoted to instrument-level
  recommendation; R7 fenced as scope delimiter; §6 table flagged for regeneration
  (do not cite 0.914/0.891/0.879).

**What the main fleet SHOULD reuse:**
- The expanded-index construction (exact reachable sets per word) — banked in
  `polyvalence/results.json`, reusable once the inventory is fixed and rebuilt per
  by-ear variant.
- R2 (never naive expansion), R4/R5 as coded gates, the control-first discipline
  (the matcher's honest null is the lane's best example of it).
- The "quiconque echo" as a standing caution: provisional-anchor echoes masquerade
  as convergent proposals — any future proposal set must be checked for
  single-anchor provenance.

**What the main fleet SHOULD NOT reuse:**
- The dictionary-alphabet lexicon for lookup (F30 — wrong unit alphabet).
- The 26 stamped proposals (all dead; restamp as DEAD with class reasons).
- The §6 K≥3 tabled numbers; the old-parse islet counts/weights.
- R3 as a standing gate; R7 as an actionable restriction.
- The WO5 pointer as stated: `data/upstream-syll*.py` is suspect per N29 — the
  inventory must be LEARNED from cribs + recovered readings, not adopted upstream.

**Net of the side fleet:** zero promotions, two nulls, two small findings, one
adjudicated 8-rule gate, one banked (needs-rebuild) infrastructure artifact. The bar held.

---

## Caveats
- The matcher ran on the old 1,846-pair parse; all positions above are old-parse
  (F32 re-index applies).
- I verified the control, the proposal enumeration, and spot lookups directly, but
  did not re-run the matcher's full 367/301-word sweep (trusted `match_results.json`
  after the above checks).
- `synthetic_breakdown.json` was overwritten during verification (see disclosure);
  the §6 discrepancy is against the code, which stands as the source of truth.
- The tester's q remains unidentified (swept 0.05–0.9); the verdict holds across the
  sweep, and the expanded-index recommendation is q-independent.
