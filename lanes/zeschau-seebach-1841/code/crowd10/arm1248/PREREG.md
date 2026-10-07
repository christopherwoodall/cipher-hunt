# PREREG — @1248 NON-FINITE ARM-BUILDER (round 10, work order 4)

Timestamp: 2026-10-07 15:45 CDT. Worker: arm1248 (executor).
Preregistered BEFORE any new analysis for this work order was run.
Prior data read: the standing record (NOTES.md F63/F67, STATE.md, finisher67
prereg/results_r9.json, frenchman-register.md Gate 4) — used for DESIGN only.

## Frame (design facts, from the record — not new data)

- Window: pair @1248, cipher frame 00-67-46 (67 at @1248; @1247; @1249).
- 00="pour" STRONG LEAD (F54) — conditional, as in finisher67 Bar N1.
- 46="que" GT (pencil crib). 67 value unknown.
- Fork arms "et"/"veut" both era-0 in this frame (finisher67 Bar N1, F67);
  @1248 NEITHER-fence currently upheld; 62-WO3 blocker carried (F67/F69).

## Gate 4 bound (frenchman, binding for this work order)

67@1248's value is era-bounded to {cela, peu}-class NON-VERBS or an
INFINITIVE (empêcher-class). Finite-verb third arms are era-0 and EXCLUDED
(Gate 4 veto). Era "pour X que" middles: v8 {cela:3, empêcher:1};
primary {peu:1, médiatrice:1}.

## Admitted candidates (exhaustive under Gate 4)

- C1: 67@1248 = "cela" (non-verb demonstrative; v8 n=3)
- C2: 67@1248 = "peu" (non-verb quantifier; "pour peu que" locution; primary n=1)
- C3: 67@1248 = infinitive (empêcher-class; v8 n=1 for "empêcher")
- C4: 67@1248 = médiatrice-class noun (primary n=1; lives or dies on constituency)

Admissibility rule (Gate-4 compliance): candidate must be NON-FINITE /
non-verb. Any candidate failing this is excluded WITHOUT scoring (no
re-litigation of the Gate 4 veto).

## What counts as a leg (pre-registered bar)

A leg = an INDEPENDENT check supporting a SPECIFIC candidate, each leg
having era support. An ARM = a candidate with ≥2 passing legs (Gate-4
compliant). Legs:

- **L1 (era frame rate):** n_v8("pour X que") ≥ 2 for the specific candidate X
  (cela), or n_v8("pour INF que" with INF any infinitive) ≥ 2 for the
  infinitive class. Threshold n≥2 pre-registered (singletons excluded as
  noise — same as finisher67 F3). FAIL = n ≤ 1.
- **L2 (era constituency):** ≥1 actual era hit (v8 or primary) of the exact
  frame "pour X que" must parse as the intended construction (cela =
  anaphoric "pour cela, que…"-class or purpose; peu = concessive
  "pour peu que + subjunctive"; empêcher = purpose-infinitive + que-clause;
  médiatrice-class = noun reading). I must READ the hit context, not trust
  trigram counts. FAIL = all hits parse otherwise (e.g. clause-boundary
  artefact).
- **L3 (cipher-side contact):** pre-registered V-specific contact predictions
  tested on the cipher:
  - 67's successor set must include 46 (observed: 46 at @1249 — the frame
    itself), and 67's OTHER successors/predecessors must not contradict V's
    era contact class (e.g. for "cela": era cela-adjacent contacts; for peu:
    era peu-adjacent; tested via v8 adjacency, NOT manual tiling).
  - Pre-registered adverse for C1/C3: 67→46 elsewhere (if 67→46 occurs at
    other positions, V's class must license it); pre-side: is 00 at @1247
    actually the F54 "pour" islet frame (00→67 must be a F54-licensed 00
    frame)?
- **L4 (window coherence):** the full ±6 window around @1248 with candidate
  V substituted must yield a grammatical 1840s-French reading given all
  standing conditional values — judged against the era corpus, not by fiat.
  (Admitted as a leg only if it discriminates: it must be possible for it
  to FAIL.)

Independence requirement: L1 (counts) and L2 (constituency) are different
kinds; L3 (cipher contact) is instrument-independent of the era legs; L4
(window coherence) is a different kind again. Passing L1+L2 for the same
candidate counts as 2 legs ONLY because rate and constituency are
different evidence kinds (counts can pass while parse fails, and vice
versa).

## 62-WO3 blocker (pre-registered)

Check: does any group-62 occur in @1248 ± 6 such that its on/il resolution
would change the arm reading? CONFIRM = a 62 sits in the window with a
frame that could interact (pre/suc of 67 or of 00); REFUTE = no 62 in the
window or the 62 present is in a frame independent of the "pour 67 que"
reading (e.g. part of a different word, ≥2 groups away with no frame
ambiguity).

## Decision rule (pre-registered)

- If any candidate passes ≥2 legs → ARM BUILT: report the candidate, the
  passing legs, and the conditioning (red team adjudicates).
- Else → FENCE @1248 PERMANENTLY with the honest-null writeup: exactly what
  was tried (all four candidates, all legs, exact numbers), and why each
  failed. A permanent fence requires the complete record.
- No re-litigation of: 48="ne" kill, H_verb kill, 86=que-family, unconditioned
  84s, three mergers, refuge concretizations, retired WO-6 bar.

## Rate bars

Nesselrode v8 (lane tokenizer verbatim, `split_nesselrode` from
code/crowd8/ratemodel/ratemodel.py) + frenchman's primary corpus (as cited
in Gate 4). NEVER score manual-tiling bearing counts.

## Expected design-time outcomes (not results)

C1 (cela): L1 expected PASS (v8 n=3); L2 uncertain (need to read the hits —
"il faut pour cela que je tire…" may parse as "il faut pour cela"+"que je
tire", i.e. NOT a purpose "pour cela que" frame); L3/L4 unknown.
C2 (peu): L1 expected FAIL (n_v8=0; primary singleton).
C3 (infinitive): L1 expected FAIL at n≥2 unless ≥2 distinct infinitives
attested in v8 (only "empêcher" known).
C4 (médiatrice): L1 expected FAIL; L2 likely FAIL on constituency.
Honest expectation: the arm probably FAILS → permanent fence with full
record. The bar is set where it is so that a pass is meaningful.
