# Synthetic Control — Seebach Homophonic Solver (side fleet)

**Status:** built 2026-10-07. **Pre-registered** (this document is the registration;
the pass bar below was fixed before any solver sees the instances).

## 1. What this is

Six independent synthetic instances of a French two-digit syllabary cipher,
each with a planted ground-truth key. The new homophonic solver must pass the
quantitative bar in §4 on ALL six instances BEFORE touching R5005. This is the
lane's control-first rule (cf. `code/crowd/annealer_results.md` N5,
`code/crowd3/scorer_smith_results.md` — both prior solvers died on their
controls).

**Every file under `instances/` is SYNTHETIC** (labelled in headers/filenames).
This is the one sanctioned exception to "never invent ciphertext".

## 2. Generator (`generator.py`)

Deterministic (seeded). Rebuild: `python3 generator.py --build-all`.
Self-test: `python3 generator.py --self-test`. Calibration: `python3
generator.py --calibrate` (writes `calibration.json`).

### 2.1 Plaintext
Les Misérables Tome 1 (1862), `data/gutenberg-17489-miserables1.txt`
(sha256 `a5de514b…` in `data/SHA256SUMS.txt`). Six non-overlapping 4,000-word
slices. **Deliberately NOT Tocqueville**: the solver's reference model trains
on Tocqueville (1835/1840), and the real R5005 plaintext (1841 diplomatic
French) is register-gapped from Tocqueville (F10: `n("cela")/n("ce")` 6.7× Les
Mis vs Tocqueville; `code/crowd3/report_inbox/frenchman-ear-check.md`: "genre,
not formality"). Using Tocqueville as synthetic plaintext — as the round-3
scorer control did (Tocqueville-t2 plaintext vs t1+t2 reference) — is
IN-DISTRIBUTION for the solver and easier than the real problem. Les Mis
preserves the register gap. It is also the same plaintext family as the
round-1 annealer control (which failed at 1/88 ≈ chance), so results are
directly comparable.

Natural "première" tokens are scrubbed from each slice (counts in meta), then
the crib phrase **"la première" is inserted once** at a recorded word offset
(first feasible of [400, 800, 1200, 1600, 2000]).

### 2.2 Cell pipeline (per word)
1. `syllabify` (the lane's rule syllabifier, `code/crowd2/scorer_smith.py`).
2. With prob `p_er_free=0.8`: re-syllabify trailing "-er"
   (`"parler"→"parl|er"`). The lane syllabifier traps "-er" inside
   `"ler"/"ner"`; real 29=`er` is rank 3 (47/1846), so the real encipherer
   freed it. (Fidelity caveat §6: the Les Mis slice is -er-poor; synthetic
   `er` lands below real rates.)
3. With prob `p_letter_split=0.03`/word: `encipher_split` (rare letter cells;
   real cipher: `i`=10, `e`=21 — NOT the always-on split that floods the
   stream with letters).
4. Ear noise (by-ear spelling, the real encipherer's documented habit —
   `frenchman-ear-check.md`: "prend"→"pre" @1331, "personne" in TWO spellings
   `per|so|nne` @160 vs `pers|on|ne` @508):
   - mute-e elision `p_mute_e=0.15` ("prend"→"pre" analogue),
   - adjacent-cell merge `p_merge=0.10` (inconsistent cuts),
   - long-cell split `p_split=0.05`,
   - double-consonant simplification `p_alt=0.08`.
   Rates are at/above the crowd4 segmenter control's calibrated ear-cutting
   knobs (`p_merge` 0.08, `p_split` 0.04, `p_alt` 0.06 —
   `code/crowd4/control.py`), which a real instrument survived.
5. Anchor cells (`la pre m i er e que`) are NEVER altered by noise (crib
   integrity). The planted crib word is force-cut to
   `pre|m|i|er|e` (mirrors the real @1033 reading; the rule syllabifier
   gives `pre|mi|è|r|e` — the deviation IS the ear-cut phenomenon).

### 2.3 Planted key (96 groups)
- Group labels: the **identical 96 labels** as R5005 (`00`–`99` minus
  `05/25/72/75`, via `code/crib_attack.py:load_pairs`).
- 7 anchors pinned to the REAL crib values:
  `11=la 70=pre 82=m 34=i 29=er 40=e 46=que`.
- 89 remaining groups → top-`T` non-anchor cells (nominal `T=56`, effective
  54–55 after the fixpoint that drops cells with zero kept occurrences),
  **frequency-weighted** (largest-remainder ∝ cell frequency; ≥1 group/cell).
  Common cells get the most homophone aliases — the historical syllabary
  design and the worst case for frequency attacks. (Round-1 used
  uniform-random mapping: easier.)
- **Polyvalence**: `n_poly=6` mid-frequency groups get one secondary cell
  each (real: 3 established islets — 06 /ɑ̃/ vs /mɑ̃/, 94 ne/en, 52 pas/se;
  STATE.md F25/F31 "established but unquantified", so 6 = 2× the known
  count). Secondary emitted with `p_poly_use=0.5`, ignoring phase
  (deliberate impurity, like real 06).
- **Phase rhythm**: occurrence phases follow a diluted global cycle
  `[B,A,C]` with purity `q_cycle=0.5` (**calibrated** — see §3), giving the
  `B→A, A→C, C→B` edges = the `A→C→B→A` rotation. Emission is phase-biased:
  each cell's aliases are dealt round-robin to phases; the phase's alias is
  picked with `p_emit_phase=0.85`, else a random alias (encipherer noise).

### 2.4 Stream assembly
- Keep only words fully inside the inventory (crib exempt); keep-rate
  42.5–46.8% (documented per instance).
- Emit with per-position ground truth (planted cell recorded).
- Coverage repair: every group occurs ≥1 (the real vocabulary is 96 by
  definition, incl. freq-1 groups); a handful of pairs/instance at most.
- Take an 1846-pair window covering all 96 groups + the crib (minimal
  covering window → earliest feasible placement; deterministic).
- Assert: 1846 pairs, 96 groups, crib `11-70-82-34-29-40` reads EXACTLY ONCE
  at the recorded offset (verified for all 6; see §5).

## 3. Calibration

`q_cycle` swept on the pilot seed (T=56): q=0.4→73.8, 0.5→257.0, 0.6→531.0
(monotonic). Certified `q_cycle=0.5`: pilot occurrence-phase 3×3 χ²=257.0,
in the pre-registered band **[181, 320]** (lower bound = real measured 181.3,
`code/crowd/contactor_results.json`; upper bound 1.8× real — beyond that the
rotation is unrealistically clean). `calibration.json` holds the table.

Per-instance occurrence-phase χ² (the rotation the solver's bigram machinery
faces): 257.0, 252.9, 181.2, 203.9, 249.3, 272.1 — all in band, mean 236
(1.3× real). The contactor's unsupervised χ² on the same streams: 36.6, 0.4,
787.3, 375.5, 6.2, 2.9 — the detector is noisy (documented design history in
`generator.py`: positional and morphological phase models were tried and
rejected; Jaccard clustering recovers planted phases at purity ~0.5, making
its χ² a coin flip). The occurrence-phase χ² is the calibrated quantity; the
unsupervised number is reported as-is with this caveat.

## 4. Pass criterion (PRE-REGISTERED)

N=6 instances (seeds 184101–184106). The solver receives per instance:
`SYNTHETIC-ct-<seed>.pairs.txt` + `SYNTHETIC-crib-<seed>.json` (the 7 anchor
values as crib facts, crib phrase + pair offset — mirroring the real
disclosure) + the Tocqueville reference corpus. Keys (`SYNTHETIC-key-*.json`)
stay SEALED with the Runner until scoring.

The solver outputs a 96-group → cell mapping (one cell/group; unassigned =
wrong). Two metrics, both required:

| metric | definition | chance (computed) | BAR |
|---|---|---|---|
| PRIMARY | exact recovery of planted PRIMARY cell, 89 non-anchor groups | 0.0216 ± 0.0153 | **mean ≥ 0.20, min ≥ 0.10** |
| SECONDARY | decode accuracy, all 1846 pairs (anchors given, auto-correct) | 0.1434 ± 0.0167 | **mean ≥ 0.30, min ≥ 0.22** |

Chance = analytic + 2,000 Monte-Carlo random permutations of the 89
non-anchor primary cells (anchors pinned), in `chance_baseline.json`
(computed, not guessed). Additionally both means must clear μ_chance + 5σ
(0.098 / 0.227) — the absolute floors dominate.

**Why these numbers:**
- 0.20 primary = 9.3× chance. Round-1 annealer: 1/88 = 0.011 on an EASIER
  control (no polyvalence, no rhythm, no noise, 8 anchors). Scorer3 v1–v3:
  top-1 0.045–0.091 on an easier top-40 subset. A solver that cannot clear
  0.20 has no business touching R5005.
- 0.10 min = 4.6× chance: no instance may sit at chance.
- 0.30 secondary = 2.1× chance; consistent with 20% key recovery
  (0.143 + 0.20×0.857 ≈ 0.314). Oracle (planted key) decodes 0.898–0.926,
  so the bar is far below ceiling — achievable in principle.
- 0.22 min = 1.5× chance; worst-instance floor.

**Verdict rule:** PASS = all four inequalities hold. Anything else = FAIL:
stop, do not touch R5005, report per-instance numbers.

## 5. Built instances

| seed | occ χ² | unsup χ² | T_eff | keep | islets | crib@pair | oracle |
|---|---|---|---|---|---|---|---|
| 184101 | 257.0 | 36.6 | 54 | 42.5% | 6 | 287 | 0.906 |
| 184102 | 252.9 | 0.4 | 55 | 46.8% | 6 | 321 | 0.919 |
| 184103 | 181.2 | 787.3 | 54 | 43.6% | 6 | 219 | 0.901 |
| 184104 | 203.9 | 375.5 | 55 | 46.5% | 6 | 45 | 0.918 |
| 184105 | 249.3 | 6.2 | 54 | 45.8% | 6 | 212 | 0.926 |
| 184106 | 272.1 | 2.9 | 55 | 46.7% | 6 | 208 | 0.898 |

(All: 1846 pairs, 96 groups, crib `11-70-82-34-29-40` exactly once,
coverage repair 0 pairs needed. Full numbers in `build_summary.json`.)

Files per instance (`instances/`):
- `SYNTHETIC-ct-<seed>.pairs.txt` — the cipher text (solver sees this)
- `SYNTHETIC-crib-<seed>.json` — crib facts (solver sees this)
- `SYNTHETIC-key-<seed>.json` — planted key (**SEALED**, Runner only)
- `SYNTHETIC-meta-<seed>.json` — provenance, params, diagnostics, sha256

## 6. Difficulty justification (Red-Team defense)

| axis | real R5005 | prior controls | THIS control | verdict |
|---|---|---|---|---|
| length / groups / anchors | 1846 / 96 / 7 pinned | same | **identical** (same labels, same 7 values) | = |
| plaintext register | diplomatic vs Tocqueville ref (gap proven, F10) | R1: Les Mis (gap kept); R3: Tocqueville-t2 (**in-distribution, easier**) | Les Mis (gap kept, mirrors real) | ≥ R3, = R1 |
| homophony | 96 « ~700 syllables (forced) | R1: uniform-random (easier) | frequency-weighted (common cells most aliases) | ≥ |
| polyvalence | 3 established (06/94/52), unquantified | **not modelled** | 6 islets, 2× known count | ≥ |
| phase rhythm | χ²=181.3, A→C→B→A | **not modelled** | occurrence χ² 181–272, same cycle | ≥ |
| ear noise | personne×2 spellings, prend→pre | R1: none; crowd4: p_merge .08/.04/.06 | p_merge .10, p_split .05, p_alt .08, p_mute_e .15 | ≥ |
| anchor count pinned | 7 | R1: 8 (easier) | 7 | ≥ R1 |

**Known fidelity caveats** (documented, not hidden):
- Synthetic `er` is rarer than real (Les Mis slice is -er-poor; 29=`er`
  ~5–15× vs real 47×). Anchor coverage overall 13–17% vs real 11% — close.
- `i`/`e` letter-cell rates differ from real (generative syllabification
  ≠ the real encipherer's cuts — this mirrors F30: the solver's rigid
  syllabifier won't match the generator, as with the real cipher).
- The contactor's unsupervised χ² is a noisy detector on synthetic
  (0.4–787); the calibrated quantity is the occurrence-phase χ².
- Polyvalent secondaries cap the oracle at 0.90–0.93 (a perfect single-cell
  key cannot exceed this — the bar sits well below).

## 7. Difficulty knobs (for the Runner / future hardening)

All in `generator.py:PARAMS`: `p_mute_e`, `p_merge`, `p_split`, `p_alt`,
`p_letter_split`, `p_er_free` (noise); `n_poly`, `p_poly_use` (polyvalence);
`q_cycle` (rotation strength — calibrated); `p_emit_phase` (emission
fidelity); `T` via `t_candidates` (inventory/homophony density);
`crib_word_offsets`, `slice_words`, `seeds`. To harden: raise noise,
`n_poly`, or lower `q_cycle`/`T`; re-run `--build-all` (deterministic).

## 8. Runner protocol

1. Solver sees ONLY: `SYNTHETIC-ct-*.pairs.txt`, `SYNTHETIC-crib-*.json`,
   and `data/gutenberg-30513-tocqueville-t1.txt` +
   `data/gutenberg-30514-tocqueville-t2.txt` (the era reference).
2. Keys stay sealed until all six solver outputs are in.
3. Score PRIMARY/SECONDARY per §4 against the sealed keys.
4. PASS → solver may touch R5005. FAIL → stop; the Solver Smith repairs
   against the control (never against R5005).
5. Optional negative control (Runner's call): the round-1 annealer should
   score ≈chance on these instances (it scored 1/88 on an easier control).

## 9. Provenance

- Plaintext: `data/gutenberg-17489-miserables1.txt` (sha256 in
  `data/SHA256SUMS.txt`).
- Syllabifier: `code/crowd2/scorer_smith.py` (`syllabify`, `encipher_split`).
- Group labels: `code/crib_attack.py:load_pairs` (1846 pairs / 96 groups,
  `data/attempt1_results.json`).
- Real numbers cited: `code/crowd/contactor_results.json` (χ²=181.3),
  `code/crowd/annealer_results.md` (1/88), 
...[truncated 1279 chars]
