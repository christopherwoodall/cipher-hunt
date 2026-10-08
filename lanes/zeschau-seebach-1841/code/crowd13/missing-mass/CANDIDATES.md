# Ranked homophone candidates — priors, NOT promotions (round 13, WO-6)

Method: contact vectors (concatenated pre+suc count vectors, repaired 1,847-pair
stream) recomputed independently by this agent; cosine similarity; mutual
nearest-distinct-neighbor check; phase coherence against the lane's phase maps
(`code/crowd4/phase_map_repaired.json`, cross-checked with
`code/crowd7/keystruct/phase_cache.json` — they agree on all groups below).

Evidence grades: **P1** = mutual-NN + phase match + rate-compatible.
**P1c** = P1 on contact but era-budget conflict (flagged). **P2** = function-word
centroid top-ranked + rate-compatible + no conflicting class assignment.
**P3** = rate or shape only.

## A. Reconstructor §b proposal sets — independent validation

All 13 proposed pairs re-verified as mutual nearest DISTINCT neighbors
(self-sim excluded; rank 2 = nearest non-self). Similarities reproduce the
reconstructor's values to ±0.003. Phase column below uses the lane's phase maps.

| set | sim | mut-NN | phase (lane maps) | n | reconstructor status | this agent |
|---|---|---|---|---|---|---|
| 48,94 | 0.643 | yes (2/2) | B/B ✓ | 38/37 | PROPOSE (48 ne-class) | **P1c** — contact P1; era-budget conflict (see §C) |
| 52,59 | 0.557 | yes (2/2) | C/C ✓ | 27/27 | PROPOSE (52 est-class) | **P1c** — contact P1; era-budget conflict (see §C) |
| 47,87 | 0.496 | yes (2/3) | A/A ✓ | 28/32 | PROPOSE (positional allophones) | resolved per F56 reframe; no action |
| 76,78 | 0.539 | yes (2/2) | C/C ✓ | 21/31 | PROPOSE (76 in ver/er frames) | **P1** — cleanest surviving set |
| 12,32 | 0.523 | yes (2/2) | A/A ✓ | 23/13 | WATCH (on-class; 62 fenced) | **P2** — needs 62="on" promotion first |
| 82,42 | 0.546 | yes (2/2) | A/A ✓ | 39/20 | WATCH (42 m-adjacent) | **P2** |
| 33,86 | 0.702 | yes (2/2) | **A/B ✗** | 25/32 | PROPOSE (strongest) | **DEMOTE→WATCH** — see §B |
| 17,67 | 0.509 | yes (2/2) | A/A ✓ | 15/38 | WATCH only | no change |
| 24,79 | 0.512 | yes (2/2) | C/C ✓ | 52/18 | DEMOTE (uniformity) | stays demoted |
| 06,44 | 0.545 | yes (2/2) | B/B ✓ | 44/15 | DEMOTE (uniformity) | stays demoted |
| 40,80 | 0.519 | yes (2/2) | A/B ✗ | 21/17 | DEMOTE (phase) | stays demoted |
| 85,87 | 0.574 | yes (2/2) | R/A ✗ | 15/32 | DEMOTE (phase) | stays demoted |
| 66,86 | 0.600 | yes (2/3) | A/B ✗ | 19/32 | DEMOTE (phase) | stays demoted |

Note: mutual-NN alone does NOT discriminate PROPOSE from DEMOTE — the demoted
sets are equally mutual-NN. The phase and uniformity filters do the work.

## B. Phase discrepancy — {33,86} (adversarial finding)

The reconstructor's §b table lists {33,86} as phase B,B. The lane's phase maps
say **33=A, 86=B** (phase_map_repaired.json AND crowd7/keystruct/phase_cache.json
agree). Every other §b row's phase column matches the maps; only {33,86}
disagrees. By the reconstructor's own rule (homophonic aliasing is
contact-coherent — true homophones share phase), {33,86} fails the same-phase
filter and drops from PROPOSE to WATCH. Supporting context: 33=infinitive-class
(F79 GRANT) vs 86=verb-stem-class (F40) — different phases AND different
classes is two independent strikes against shared value (cf. the 47/87
positional-allophone precedent). The uniformity χ² (0.86, p=0.35) still holds,
so the set is not dead — but it is no longer the strongest set. **{76,78}
inherits "strongest surviving set."** Council should rule whether the
reconstructor's B,B was a different phase definition or an error.

## C. The ne/est era-budget conflicts (P1c grades)

- **48 as ne-class homophone (via 94="ne" prov-strong):** contact evidence is
  P1 — 48 is the #1 unidentified neighbor of 94 (sim 0.643; next is 16 at
  0.529), mutual-NN, phase B/B, n 38/37 near-uniform. **But** the era ne budget
  is 23.8 occ while 94 alone carries 37 (1.55×); adding 48 → 75 (3.2×). The
  "48 is the ne-class homophone" prior stands on contact and FAILS on budget.
  Resolutions available to council: (i) 94="ne" is wrong; (ii) this despatch is
  negation-dense vs the corpus; (iii) 94/48 cover a broader ne-class
  (ne+n'+verb-ne fragments) than the comparator. Prior: **P1c — keep, flagged.**
- **52 as est-class homophone (via 59="est" prov):** contact P1 (0.557,
  mutual-NN, C/C, n 27/27 identical). Era est budget 7.7 (mix) / 12.4 (v8);
  59 alone carries 27 (2–3.5×); adding 52 → 54 (4–7×). Same conflict shape as
  ne. Prior: **P1c — keep, flagged.** The 47/87 precedent suggests testing
  positional-allophone structure (complementary distribution) before free
  homophony for both sets.

## D. Uncovered-syllable priors (the actual missing mass)

Top-deficit syllables with NO identified cell: de (2.9 cells), en (1.3),
ne (1.2), les (1.1), te (1.1), et (1.3), ti/tion (1.3), u/ou-class (3.0),
a (2.8), qu-remainder (1.0). Per-cell rate ≈ 19 occ.
Function-word centroid (built from 11,87,46,64,96,77,94) top unidentified,
excluding groups with class assignments (06,33,86,47,78,84):

| rank | group | centroid-sim | n | phase | rate-band fit |
|---|---|---|---|---|---|
| 1 | 01 | 0.472 | 28 | B | de/les/te/et |
| 2 | 98 | 0.470 | 40 | R | de (high-n; R outlier) |
| 3 | 14 | 0.454 | 15 | B | de |
| 4 | 88 | 0.407 | 23 | R | de/les/te/et |
| 5 | 16 | 0.400 | 28 | B | de/les/te/et |
| 6 | 43 | 0.400 | 16 | B | de |
| 7 | 44 | 0.386 | 15 | B | de |
| 8 | 63 | 0.366 | 12 | B | de (low-n) |
| 9 | 08 | 0.364 | 18 | B | de/les/te |
| 10 | 37 | 0.362 | 28 | A | de/les/te/et |
| 11 | 91 | 0.338 | 21 | C | les/te/et |
| 12 | 67 | 0.337 | 38 | A | — (et/veut fork; excluded from pool) |

**de-class (~3 cells): P2 pool = {01, 98, 14, 88, 16, 43, 44, 08, 37}.**
les/te/et-class (~1 cell each): P2 pool = {01, 88, 16, 37, 91} (n 21–28 band);
contact evidence cannot yet separate les vs te vs et — honest three-way tie.
en-class: 24 (n=52) is the lane's local hypothesis but carries 2× the en
budget — needs the broader-class or despatch-density resolution (same tension
as §C). ti/tion and u/a classes: no contact prior computed (different expected
contact shape); open.
**Strongest-prior unidentified groups overall: 48 (P1c, ne), 52 (P1c, est),
76 (P1, ver/er), 01 (P2, de-pool top), 98 (P2, de-pool).**
