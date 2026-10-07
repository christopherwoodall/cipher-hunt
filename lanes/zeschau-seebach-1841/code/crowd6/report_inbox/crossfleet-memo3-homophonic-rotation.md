# CROSS-FLEET MEMO 3 — homophonic solver CONTROL-FAIL: two rotation findings for the main fleet

Date: 2026-10-07 (round-6 curation) · From: homophonic solver fleet (coordinator-relayed)
Status: CONTROL-FAIL, R5005 untouched (gate held). Full report:
`code/side-homophonic/runs/RUN-REPORT.md`. Design: `code/side-homophonic/control/CONTROL-DESIGN.md`.
Solver method notes: `code/side-homophonic/solver/METHOD.md`.

## Finding 1 — the contactor's unsupervised χ² is a NOISY DETECTOR (instrument flag)

On 6 synthetic controls with TRUE occurrence-phase χ² of 181–272, the
identical unsupervised pipeline (Jaccard clustering → phase labels → χ²)
reads **36.6, 0.4, 787.3, 375.5, 6.2, 2.9** — in-band on 0/6. The design
doc's own caveat: "Jaccard clustering recovers planted phases at purity
~0.5, making its χ² a coin flip" (`CONTROL-DESIGN.md` §3). The solver's
χ²-gated prior was DEMOTED on this basis (red-team 2026-10-07, METHOD.md §5).

Precise scope for the main fleet (three-way distinction):
- (a) Rhythm EXISTENCE — confirmed by the label-free lag-3 test (z=+5.6,
  p≈1e-8; round-6 Segmenter). Different instrument, NOT impugned.
- (b) Exact χ² MAGNITUDE (181.3 original; 366.3 recomputed) — noisy. No
  main-fleet argument may lean on the value.
- (c) Phase MAPPING (which group → A/B/C) — ~0.5 purity, coin flip. Any
  per-group phase argument (e.g. "X is phase C, therefore word-final")
  stands on a noisy instrument and must be flagged/demoted unless
  independently supported.
- Null streams (uniform random) measure χ²∈[2,33]: "rhythm exists" does
  not imply "mapping is right."

Action: review all rotation work orders for 181.3-dependence; the
Segmenter's round-6 package needs this flag applied per-thread.

## Finding 2 — contact-coherent aliasing: POSITIVE key-structure clue (round-7 work order)

The control generator proved by construction (`generator.py`): uniform-random
homophone aliasing fragments contact profiles and the rotation VANISHES
(χ²=3.9). The rotation only survives when aliases are dealt phase-coherently
(each cell's aliases round-robin to phases; emission picks the
occurrence-phase primary). R5005 shows visible rotation ⇒ the real
key-maker's aliasing is CONTACT-COHERENT, not uniform-random.

This is consistent with F33's conditioned polyvalence — the conditioning
rules ARE contact-coherence made explicit. Round-7 work order: invert the
aliasing via phase-conditioned contact profiles to propose homophone sets;
test whether merging candidate alias sets under F33 rules improves
assignment coherence. (A Smith-rebuild side fleet is re-attacking the
solver with length-normalized word scoring through the same control —
no main-fleet action unless its gate passes.)
