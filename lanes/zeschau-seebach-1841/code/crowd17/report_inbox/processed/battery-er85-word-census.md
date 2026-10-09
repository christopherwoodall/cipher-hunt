# Battery `er85-word-census` — verdict: PROMOTE (census complete; zero composition; rescue arm dead)

## Bar (verbatim, pre-registered)
"word composition census with battery-grade evidence; a clean 'er...'-word at @96 or @1233 would rescue the finite-63 strand at @373."

Numbered clauses (derived before testing, not modified after):
- C1: census all '29 85' windows byte-exact with battery-grade evidence.
- C2: a clean 'er...'-word at @96 or @1233 composes under standing values → rescues the finite-63 strand at @373.
- C3: if no window composes, the 'er[85]'-word route is fenced as exhausted and the @373 strand receives no rescue (hardened).

Adverses: none listed.

## Method
Re-derived the repaired 1,847-pair / 96-type stream in-session from
`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`
(same parse as `repair_parse.py`; asserts held: 1,847 pairs, 96 types).
`canonical.py` never used. Standing values per BATTERY-PROTOCOL.md §7:
29='er' banked ground truth; 85 = verb-stem frame grant only (A3), value open;
no frame licenses '29 85' composition. §3 bars inventing values.

## Findings

'29 85' occurs exactly 3× stream-wide (byte-exact bigram census):

| window | row | context (±4) |
|---|---|---|
| @96 | a1_02 | 41 98 81 97 46 **29 85** 08 21 62 |
| @374 | a2_06 | 17 06 21 65 63 **29 85** 82 48 00 |
| @1233 | a7_01 | 82 48 29 47 33 **29 85** 56 10 03 |

- **C1 PASS.** All three windows censused byte-exact.
- **Zero windows compose '29 85' as a word under standing values.**
  A one-word 'er[85]' requires 85's letter content; 85's value is open
  everywhere (A3 frame grant only — confirmed by
  `battery-contredire-85-33-vehicle`: "85's value (open; A3 verb-stem frame
  grant only)"). Naming any 'er...'-word would invent a value for 85,
  barred by §3. The lane's only licensed 'er'-initial word is
  '29 40'='erre' (R18-012: "qui erre" @291/@685, "cela erre" @500) —
  not '29 85'. No frame or hold licenses '29 85' composition (the licensed
  infinitive composition runs stem+'er', e.g. '03 29', never 'er'+stem).
  - @96: "97 [46=que] er[85] 08" — 'er[85]' unnameable; 46='que' cannot take an '-er' suffix, so no suffixal rival either.
  - @374: "65 [63] er[85] 82" — 'er[85]' unnameable. Note the boundary rival '[63]er' | '[85]' (63 verb-class + 'er' infinitive composition) needs 63's value — unvalued, red-team/battery venue, not this target.
  - @1233: "[47=ce] [33] er[85] 56" — 'er[85]' unnameable; 33's value tied (dire/croire), no suffixal license.
- **C2 does not fire.** No clean 'er...'-word exists at @96 or @1233.
- **C3 FIRES.** The 'er[85]'-word route is fenced as exhausted (n=3,
  all fail with the same stated cause). The finite-63 strand at @373
  receives no rescue from this route; the `locus-368-fullparse` fence
  stands unchanged. The finite-63 question remains with the already-queued
  `fin63-373-rerun` venue.

## Scope
Fences only the '29 85' → one-word-'er[85]' composition route. Untouched:
85's A3 frame and open value; 63's verb class and the '[63]er' infinitive
rival (needs 63's value); R24 'en'+85; the '29 40'='erre' finding; §7
(67 sole polyvalence). No standing or red-team verdict contradicted or
downgraded. Canonical-stream caveat stands (rows a1_02/a2_06/a7_01
unvalidated).

## Verdict: PROMOTE
Census complete with battery-grade evidence; definitive zero; the rescue
consequence resolved negatively with stated cause. Adverses: none.

No follow-ups required per §4 (promote). Open question noted, not queued:
naming 63's value at @373 would test the '[63]er' infinitive rival at
@373–374 (already covered by queued `fin63-373-rerun`).

## Bookkeeping
- Lock `locks/er85-word-census.lock` created on start, deleted on completion.
- Queue `er85-word-census` → `status: verdict`, `result: promote`, 2026-10-09.
- R5005, sealed gate instances, red-team adjudication queue untouched.
