# Battery verdict: frame-vient-parvenir

## Bar (verbatim from battery-queue.json, pre-registered)

"resolve iff thirds profile as homophone set (permutation test) + 83='de' cross-checks"

Restated as numbered clauses:
- **C1:** the thirds (60/62/68) profile as a homophone set — permutation test on context distributions (labels exchangeable).
- **C2:** 83='de' cross-checks hold at the two other 98-83 windows.

Claim: the "vient de me parvenir" thirds (60/62/68) are a 3-cell homophone set.
Priority: 3. Adverse (pre-registered): "French of 98 unconfirmed".

## Method

Read BATTERY-PROTOCOL.md first. Lock created on start, deleted on completion.
Re-derived the repaired 1,847-pair / 96-type stream from
`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`
(parsed per `repair_parse.py`; 1,847 pairs / 96 types verified).
`canonical.py` never touched. R5005, sealed gates, red-team queue untouched.
All @-offsets below are 1-based (lane convention).

## Window-level evidence (byte-traced)

### The formula (evidence field: byte-identical x3, thirds vary)

| @ (98) | 6-gram | row |
|---|---|---|
| 228 | 98 83 82 96 21 **60** | a2_01 |
| 1061 | 98 83 82 96 21 **62** | a6_04 |
| 1784 | 98 83 82 96 21 **68** | a8_09 |

- `96 21` bigram census: exactly 3 occurrences stream-wide (@231, @1064, @1787
  1-based) — all inside the formula. **Formula-bound confirmed**; 96-21 occurs
  nowhere else globally.
- Frame parse under standing values: 98 = finite verb (battery-promoted by
  `battery-prof-98.md`, 2026-10-09, needs red-team ratification), 82 = 'm'
  (GT), 96 = 'par' (promoted), 83 = 'de' (conditioned, see C2), 21 open.
  The frame reads "vient de m(e) par X" — the frame itself is NOT at issue.

### C1 — permutation test on 60/62/68 contexts

Full censuses (n: 60=18, 62=35, 68=8):

- 60 successors: 03 x4, 08 x2, 71 x2, 67 x2, 12 x2, 90, 09, 15, 65, 06, 27
- 62 successors: 94 x9, 48 x6, 98 x5, 16 x4, 61 x2, 06 x2, 96, 91, 21, 18, 38, 46, 93
- 68 successors: 21 x2, 37, 00, 52, 59, 06, 47

Permutation test (labels exchangeable under homophony; chi-square of
homogeneity, Monte Carlo p, 5,000 permutations, seed fixed):

- Successors, all three cells: chi2 = 43.28, **p = 0.0002** — homogeneity REJECTED.
- Predecessors, all three cells: chi2 = 14.18, p = 0.44 — not rejected.
- Pairwise successors: 60 vs 62 p = 0.0002 (heterogeneous); 62 vs 68 p = 0.028
  (heterogeneous); 60 vs 68 p = 0.099 (not significant, thin data).

Driver: 62's successor profile is dominated by 94 x9 and 48 x6 — the same
word-internal bigrams at the heart of the killed 62-selector claim
(`battery-sel-62-48-94.md`, KILL 2026-10-09). 62 has a distinct distributional
life from 60/68; the labels are not exchangeable.

Frequency check (standing rule: uniformity necessary but insufficient for
homophony): 35 / 18 / 8 — far from uniform. Second strike, same conclusion.

**C1: FAIL at kill grade** — the bar's own named decider rejects the
homophone-set profile at the lane's distributional standard (p = 0.0002).

### C2 — 83='de' cross-checks at the two other 98-83 windows

98-83 occurs x5 stream-wide (@228, @898, @931, @1061, @1784); the non-formula
two:

- @898 (row a5_08): `82 14 | 98 83 | 86 16 92` — "[14] vient de [86]…" parses
  under conditioned 83='de' (86 infinitive-shaped per the open inf-83-fork).
- @931 (row a5_10): `48 82 | 98 83 | 56 69 26` — "me vient de [56]…" parses
  under conditioned 83='de'.

Both cross-checks hold. Consistent with `battery-de-83-sweep.md` (NULL,
2026-10-09): unconditioned 83='de' is dead at @911 ("qui de est", kill-grade),
but the conditioned "vient de" environment parses cleanly.

**C2: PASS** (as conditioned parses; no global 83='de' claimed).

### Adverse answered

"French of 98 unconfirmed" — answered at battery grade by `battery-prof-98.md`
(PROMOTE, 2026-10-09): 98 = finite verb, 98-83 x5 all parse as "vient de X"
frames. Cited, not re-derived; pending red-team ratification like all battery
promotes.

## Verdict: KILL

The 3-cell homophone-set claim (60/62/68 = one plaintext, "nir") is dead at
kill grade: the permutation test rejects successor homogeneity at p = 0.0002,
and the frequency split (35/18/8) violates the uniformity necessary condition.
The kill is narrow — it kills the SET, not the frame:

- The `98 83 82 96 21` formula stands ("vient de m(e) par X", 96-21
  formula-bound x3).
- Conditioned 83='de' in the "vient de" environment stands (both cross-checks).
- No value is named for any third; 60/62/68 values stay open.
- Residual for the red team (not a battery claim): 60 vs 68 are
  successor-homogeneous (p = 0.099, thin) — a 2-cell {60,68} candidate remains
  logically open but unproven. 62 is excluded from any such set by its
  94/48-dominated profile.

No standing verdict contradicted or downgraded. No polyvalence declared (§7
intact). `canonical.py` never used. No follow-ups required for a kill verdict;
the {60,68} residual is flagged above for red-team adjudication.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-frame-vient-parvenir.md`
- Queue: `frame-vient-parvenir` → status `verdict`, result `kill`, date 2026-10-09
  (temp-file + rename, pre-write assert confirmed queued/verdictless, JSON
  re-validated post-write)
- Lock created on start with agent id + UTC timestamp, deleted on completion.
