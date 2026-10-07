# PHONETICIAN verdict — CV-structure tests (side-rotation, 2026-10-07)

Pre-registration: `code/side-rotation/prereg_phonetician.md` (banked before any
statistic was computed; one hand-tabulation correction made pre-execution,
documented there). Script: `phonetician.py`. Raw numbers:
`phonetician_results.json`.

## Method (as pre-registered)

Fisher exact (Freeman-Halton, probability definition) by full enumeration of
fixed-margin tables, two-sided, α=0.05. Phases from
`code/crowd4/phase_map_repaired.json` (marginals A=32/B=27/C=17 verified in
code; all 16 anchors in A/B/C). Phonetic values from the crib-learned
inventory F44 (`code/crowd5/unit_inventory.json`), NOT standard French:
spelling does not decide ("pas"=/pa/ is OPEN; "er"=/eʀ/ is CLOSED).
Frenchman ear checks borrowed from `code/crowd3/frenchman_results.md`
(er|e segmentation, by-ear "pre", /kɔ̃/ fusion) — read, not re-staffed.
Test set: 7 GT cribs + 87/64/96/94 provisional + 62 STRONG LEAD +
78/47/77 LEADs + 52 STRONG-bounded, every status marked (n=16).
Excluded pre-registered: 06/86 (class-level, no phonetic value), 67.

## Verdicts

| test | table (A/B/C) | n | exact p | verdict |
|---|---|---|---|---|
| T-Pa open/closed × phase | open [4,6,3]; closed [1,0,2] | 16 | 0.2500 | NULL |
| T-Pb tier × phase | Tier0 [2,4,1]; Prov [1,2,1]; Lead [2,0,3] | 16 | 0.3465 | NULL |
| T-Pc sonority × phase | light [2,1,0]; balanced [2,4,4]; heavy [1,1,1] | 16 | 0.7752 | NULL |
| T-Pa2 GT+prov only (robustness) | open [2,6,0]; closed [1,0,2] | 11 | **0.0242** | LEAN — gated, not a claim |
| T-Pa3 78="ver" recode (sensitivity) | open [4,6,2]; closed [1,0,3] | 16 | 0.0687 | NULL |
| T-Pc2 sonority, GT+prov only | — | 11 | 1.0000 | NULL |

**Overall: CONSTRAINED NULL.** The phases carry no detectable fine phonetic
structure among the anchored groups — not in open/closed syllable shape, not
in inventory tier, not in consonant/vowel sonority balance.

## The T-Pa2 lean (flagged, gated, probably artifactual)

T-Pa2 (p=0.0242, independently re-derived by brute-force hypergeometric
enumeration — same number) passes the pre-registered α=0.05 but **fails the
Bonferroni gate α/3≈0.0167**, and per the pre-registered decision rule it is
NOT a claim until the Red Team re-derives it. Three reasons to read it as
noise rather than signal:

1. **It is tier-confounded.** The entire effect is "no open GT/provisional
   unit sits in phase C." The three open C-phase units (77=le, 78=me, 52=pas)
   are ALL LEAD-tier — excluding LEADs mechanically manufactured the "open
   avoids C" pattern. The tier test itself (T-Pb) is null (p=0.35).
2. **It does not survive the 78 rival reading.** Recoding 78 as word-internal
   "ver" (/vɛʀ/, closed — the inventory's own flagged rival) moves the primary
   test to p=0.069 and the lean evaporates with it.
3. **The positive bar was unreachable for T-Pa by design.** Minimum p
   attainable under the T-Pa margins = 0.0357 > 0.0167: NO possible table
   could have passed Bonferroni. (T-Pc's bar was reachable in principle —
   min p = 0.0001 — and still returned p=0.78.)

## Power (honest)

- n=16 (n=11 in variants) by construction. Simulation (20k draws): power to
  detect even a *deterministic* alternative (all 3 closed units forced into
  phase C) = **0.40**; all 3 heavy units forced into A = **0.44**.
- These tests can only see maximal, deterministic phonetic-phase lockstep,
  and even that less than half the time. A null here kills only STRONG
  phonetic-phase structure, not subtle structure.

## What the null implies for the process hypothesis

This is the third granularity at which the phases refuse linguistic meaning:
word-position (N15) → morphological/polyvalence/unit-size/syntactic
(F43 T1–T4) → now fine phonetics (open/closed, tier, sonority). Every
linguistic slot the lane has tested comes back null, while the rotation
itself stays loud (chi²=366.3), global (T5b), distributed (T5a), and
period-3 beyond first-order Markov (E1, z=+5.6). That combination is exactly
what the table-geometry leading hypothesis predicts: the encipherer cycling
through linguistically ARBITRARY table columns — rotation real, cluster
assignment fragile, and no phonetic/linguistic content in the phases to find.
The phonetician's null tightens the fence around that hypothesis; it does
not touch E1 or the rotation's reality.

## Caveats

- 9 of 16 phonetic values are provisional/lead/bounded, not crib-proof. The
  GT+prov variants (n=11) address this; both are null or gated.
- Statuses 96=par ("CONFIRMED 4/4 but inherits 87's provisionality") and
  87=ce (red-team-demoted) inherit uncertainty downstream — noted, tiered as
  provisional per the work order.
- The Fisher probability-definition exact test is conservative; other exact
  definitions would shift p slightly, not the verdicts.
