# PRE-REGISTRATION — Round-8 01-CLOSER battery: 01="est" allophony vs mutual exclusivity

Date: 2026-10-07. Executor: 01-CLOSER (round-8 work order 3).
Status under test: **01="est" MEDIUM** (frenchman @295 ear window `65 16 01 11 78`;
A1 "c'est"×3 = 87→01 ×2 @344/@1028 + 47→01 ×1 @194; I2 verb-shaped profile).
Provisional counterpart: **59="est"** (F52, red-team GRANTED — four legs, all
01-independent: S1 1.10× vs Nesselrode v8, S2 "qui est" 3/47, S3 "n'est" 3/37,
rivals dead 9–51×).

Standing facts (banked, re-derived not re-litigated): n01=28, n59=27 (usage
split 28:27 over 1,847 repaired pairs); {64,94}→{01,59} forced "est"-frames go
6/6 to 59, 0/6 to 01 (p=0.014 under the 27:28 usage-split null); 01/59 share 6
predecessors (15,16,48,76,86,87) and 2 followers (19,24) — overlapping, not
complementary; @824 (87→59) frame hostile under 24="en" STRONG; 87→01 ×2 vs
87→59 ×1 ("c'est" frame splits). Round-7 denied 01 MEDIUM→WEAK (no
pre-registered bar; I1's >3× bar fails on Nesselrode v8 at 2.24×).

## Hypotheses

- **H_allo**: /ɛ/→{01,59} is conditioned homophony. F33 requires every live
  polyvalence in this key to carry a verified positional/lexical conditioning
  rule (06, 52, 94 all do; zero cases of free polyvalence). H_allo therefore
  predicts a complete, statable conditioning rule separating 01-tokens from
  59-tokens.
- **H_excl**: 01 and 59 cannot both be "est". 59="est" is provisional with
  01-independent legs; the symmetry-breaker is leg count and leg independence
  (59: 4 banked legs + 2 refreshed + rival re-kill; 01: 1 ear window + the
  A1/I2 legs that ride on 01 itself). The mirror (59 falls instead) re-opens
  iff C6 fails.

## Checks (pre-registered; run after this file is written)

**C1 — conditioning-context scan (H_allo's positive leg).** Positions of 01
(n=28) and 59 (n=27) from the repaired stream. Six pre-registered families:
  1. predecessor group identity (raw);
  2. predecessor banked-value class {64=qui, 94=ne, 87=ce, 46=que, 77=le-prov,
     11=la, GT-letters(70,82,34,29,40), other};
  3. follower banked-value class {46=que, 11=la, 77=le-prov, 19, 24, other};
  4. contact phase of the neighboring groups (banked `code/crowd4/phase_map_repaired.json`
     maps GROUP→phase, so per-token conditioning uses the predecessor's phase
     class {A,B,C,R,other} as the primary test; the successor's phase class is
     reported as a diagnostic only, not a bar);
  5. the binary rule pre∈{64,94}→59 (scored as a candidate rule: accuracy);
  6. formula membership (inside a banked formula span vs outside:
     64-96-43-87-01 ×2, 24-87-64 ×3, 77-78-94-82-06 ×2, 06-77-78-18-71-10-01).
Per family: contingency table over (01-tokens, 59-tokens) × levels; chi² p
(Fisher-Freeman-Halton where feasible); best binary partition of levels by
majority, token accuracy per glyph. Multiple testing: Bonferroni over m=6.
Bar: family qualifies iff corrected p<0.05 AND ≥90% of 01-tokens AND ≥90% of
59-tokens fall on their predicted side (F33-grade: a rule that misclassifies
>10% of either glyph is not a rule). **C1-PASS = some family qualifies with a
stated positional/lexical rule. C1-FAIL = no family qualifies.**

**C2 — forced-"est"-frame exclusivity (H_excl's positive leg).**
Pre-registered enumeration rule (not count): all stream positions i where
pairs[i]∈{01,59} AND pairs[i-1]∈{64,94} ("qui est"/"n'est" — the only frames
grammatically forced to "est" under banked values, independent of 01/59
identity). Null A (both-hold-same-word, unconditioned): each such frame goes
to 59 w.p. 27/55, to 01 w.p. 28/55. Bar D2: one-sided binomial p<0.05 for the
observed 01-count. Fresh-data condition: every {64,94}→{01,59} in the repaired
stream is enumerated by rule (banked 6/6 re-derived; any new slots reported);
if any NEW forced slot goes to 01, D2 does not fire. Pre-registered
counter-leg: the "c'est" frame (87→01 ×2 vs 87→59 ×1, 87="ce" provisional) is
scored separately — if it splits, exclusivity-by-frame is rejected in that
frame; the counter-leg is a statistical wash unless it rejects Null A in the
01-direction at p<0.05 (pre-register: it will not — expected p≈0.51).

**C3 — 01 rival screen on Nesselrode v8 (the fair-battery leg).** Pre-registered
rival set: {doute, dit, fait, veut, peut} (59's killed set, L5) + {ait, sont,
ont}. Unigram ratios P(01)/P(word) on Nesselrode v8 (elision-split
tokenization per `diplomatic_rates.py`). Bar: "est" is unique survivor iff
every rival is ≥5× away (either direction) — mirroring L5. Named interaction:
"ait" (subjunctive /ɛ/ — the natural allophone): report 46→01 / 64→01 counts;
if "ait" survives the unigram bar it becomes 01's named alternative (01 keeps
MEDIUM; H_excl gains a landing spot; H_allo gains a re-read, not a kill).

**C4 — joint-unigram discipline leg (I1 refresh; the bar that must hold on
Nesselrode v8).** Joint (27+28)/1847 vs Nesselrode v8 P("est"). Pre-registered
bar: both-hold-as-same-word rejected iff joint/N8 > 3× (I1's bar). Expected to
FAIL (round 7: 2.24×) — recorded as the discipline leg: no demotion via this
route. Also report the 01-alone ratio P(01)/N8-P("est") (expected ≈1.14×,
in-band — H_allo's rate leg, reported honestly).

**C5 — @295 founding-window audit.** Re-derive the `65 16 01 11 78` window in
repaired positions by content search. Pre-registered bar: PASS if the window
admits a grammatical reading with 01="est" under banked values (16="i" HOLD,
78={ver,er} fork) with no hostility; report the best reading. Qualitative —
not a demotion leg alone.

**C6 — symmetry-break audit (mirror check).** Recompute 59's four legs from
`code/crowd7/closer/diplomatic_rates.json` + stream (S1 1.10×, S2, S3, L5
rivals 9–51×). If any leg fails on Nesselrode v8, the exclusivity verdict's
direction (59 wins) is SUSPENDED and the mirror (01 survives, 59 re-opened)
is reported instead. C6 must hold for DEMOTE.

## Verdict rule (pre-registered)

- **PROMOTE 01 MEDIUM→provisional** iff: C1-PASS (qualifying conditioning rule
  stated, corrected p<0.05, ≥90% both-side separation) AND C5-PASS AND C3 keeps
  "est" the unique survivor for 01 AND the "c'est" split is consistent with
  the stated rule (87→01 ×2 fall on 01's side — checked, not assumed) AND ≥2
  independent checks among {C1, C3, C5} pass.
- **DEMOTE 01 MEDIUM→WEAK** iff ALL of: (D1) C1-FAIL — no qualifying
  conditioning rule (H_allo's positive leg dead at F33 grade); (D2) C2's bar
  fires (p<0.05, fresh-data non-contradiction holds); (D3) C6 holds (59's legs
  intact — symmetry breaks toward 59). Single-leg demotion forbidden (lane
  rule: demotion needs ≥2 independent checks). No demotion via C4.
- **CONFIRM MEDIUM** otherwise — including genuine ties (C1 inconclusive but
  C2 live; C2's counter-leg significant; C3 surfaces a live rival for 01).

## Conditioning-vs-symmetry reporting (required by the work order)

- If H_allo: state the conditioning rule exactly (which family, which levels,
  the separation table, corrected p).
- If H_excl: state the symmetry-breaker (which legs 59 holds that 01 lacks;
  59's 01-independence; what 01's windows become under re-reading).
- Either way: state what would falsify the verdict (the mirror conditions).

## Method notes

- Canonical parse: repaired 1,847-pair (`code/side-keyhunt/repaired_offsets.json`);
  positions per `code/crowd4/REINDEX.md`; phase map banked at
  `code/crowd4/phase_map_repaired.json`.
- Comparator: Nesselrode v8 (`code/side-period/corpus/nesselrode-v8.txt`) —
  actual 1840–46 chancellery correspondence; NOT Tocqueville, for any rate bar.
- Script: `code/crowd8/closer01/battery.py` → `results.json`. Report note at
  `code/crowd8/report_inbox/closer01-01-est.md` per REPORTING.md.
- No claim merges without red-team ruling. This verdict is a recommendation.
