# Battery report: w2-knot-etque

Target: `w2-knot-etque`. Claim: 'et que' @1248 coordination — sentence-boundary
analysis over a7_00-a7_02 tests coordination with the @1191 '46'-clause
('...84 59 46 07 24 82 16 96...'). Date: 2026-10-09.
Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`, parsed like `code/side-keyhunt/repair_parse.py`;
1,847 pairs / 96 types re-verified in-session). Never used `canonical.py`.
R5005, sealed gates, red-team queue untouched.

## Bar (verbatim, from the queue)

"demonstrate the parallel 'que'-clause with a complete parse, or fence
'00 67 46' as a permanent A9 residual with the 57-token gap as the stated cause"

Numbered clauses (fixed before testing, not modified after):

1. C1 — DEMONSTRATE: produce a complete grammatical parse of a parallel
   'que'-clause for the 'et que' coordination (complete = every token
   assigned a role, ≤1 unstated assumption, 1841-grammatical under standing
   values). PASS iff such a parse is demonstrated on the bytes.
2. C2 — FENCE: if C1 fails, fence '00 67 46' as a permanent A9 residual with
   the 57-token gap as the stated cause. PASS iff the fence is executed with
   the cause stated honestly.

Standing values used: 46='que' (banked), 84='on' (A15, conditions C1–C3),
59=est (provisional), 64='qui' (granted), 96='par' (granted), 67='et'/'veut'
(sole polyvalence; positional rule: 'veut' iff follower infinitive-shaped),
26 finite-verb class (battery-promoted), 30='pas' (promote-conditional),
06='ent' (promote), 65 noun-class (promoted), 24 verb-class
(battery-promoted). No new values declared.

## Window-level evidence (@-offsets; 0-based in this report)

Byte inventory over rows a7_00–a7_02 (0b1191 = start of a7_00; a7_01 starts
0b1219; a7_02 starts 0b1248; a7_03 starts 0b1276):

- '00 67 46' is a stream-wide hapax at 0b1247–1249 ('00' ends a7_01,
  '67 46' opens a7_02 — the row break sits between 00 and 67).
- '67 46' occurs exactly twice stream-wide: 0b471 ('80 06 67 46 84 24' —
  'et/veut qu'on [24-verb]', a subject sits between 'que' and the verb) and
  0b1248 (the locus: 'que' directly abuts verb-class 26, no subject slot).
- '46' inventory in a7_00–a7_02: 0b1191 ('42 06 84 59 46 07 24 82 16'),
  0b1249 (the locus), 0b1254 ('30 06 65 46 01 61'), 0b1265 ('50 46 69 88').
  The ONLY '46' before the locus in the whole a7_00–a7_02 span is 0b1191.
- Next '46' before 0b1191 is at 0b954 ('87 46 24 85' = "ce que [24-verb]"
  — a complete-looking 'que'-clause but 293 tokens before the locus).
- Gap: 0b1191 → 0b1247 = 56 tokens; 0b1190 → 0b1247 = 57 tokens
  (matches the queue bar's "57-token gap"). Gap content spans a row boundary
  (a7_00/a7_01 at 0b1219) and includes a full relative clause
  ('64 29 45 ... 64 59 32 48' = 'qui er ... qui est 32e') plus a
  '61 24 48 30 ...' window — no parallel structure to 'et que [26] pas'.

## Per-clause pass/fail

### C1 — DEMONSTRATE: FAIL

The only plausible parallel arm is the 0b1191 clause
'...84 59 46 07 24 82 16 96...'. Attempted complete parse:
"[06] on est que [07] [24-verb] m[16] par m'[16] qui er…". Three unstated
assumptions are required, each unlicensed:

1. "on est que [07]" is not a licensed construction — "est que" needs
   'ne' ("on n'est que…") or a different frame; no ne-drop precedent exists
   in the lane (parent reseg-3006-w2's C1 finding, adopted as premise).
2. 07's class is open — the would-be subject of the 24-verb is unidentified.
3. 16's role in "m[16] par m'[16]" is open.

A parse carrying ≥3 unstated assumptions is not a "complete parse". The 0b954
candidate is 293 tokens back (no licensed coordination span of that length;
the parent's 57-token span was already ruled implausible — a 293-token span
is beyond reach). No other '46' candidate exists in the span. The coordination
itself is additionally defective at kill grade independent of the parallel
clause: the second conjunct 'que [26]' (0b1249–1250) has no subject — 46
directly abuts verb-class 26 — and the only licensed stream-wide template for
'67 46' (0b471: 'et/veut qu'on [24-verb]') places a subject ('on') between
'que' and the verb. French does not pro-drop; a subjectless 'que'-clause
cannot coordinate with the 0b1191 arm, which has its own subject slot (07).

### C2 — FENCE: EXECUTED

'00 67 46' is fenced as a permanent A9 residual. Stated cause:
(1) the 57-token gap to the only candidate parallel clause (0b1191), with no
parallel structure anywhere in the span;
(2) the coordination's own second conjunct 'que [26]' is subjectless at kill
grade (46 abuts verb-class 26 directly; licensed '67 46' template at 0b471
requires an intervening subject);
(3) the 'pour'-head has no first conjunct — the left edge is '33 16 00'
('[33] [16] pour' at 0b1245–1247), so 'pour et que' is conjunct-less;
(4) the 'veut' arm is dead under the §7 positional rule (follower 46='que'
is not infinitive-shaped, so 67='et' is forced);
(5) word-internal rescues fail — no French word spans 'pour' + 'et' before
'que' (parent C4, adopted).

"Permanent" is used in the queue bar's sense: this fence is not expected to
re-open under routine batteries. Honest re-open conditions (red-team venue):
a licensed complete parse of the 0b1191 'est que [07] [24]' clause (needs
ne-drop precedent, 07's class, and 16's role — three separate rulings), a
demonstrated parallel clause elsewhere, or a licensed subjectless
'que'-conjunct construction.

## Adverses

None listed on the target. No standing or red-team verdict contradicted;
§7 intact. The a5_03 flip's downstream-shift caveat is noted (canonical
stream verdict per protocol); every count above was re-derived in-session.

## Verdict: NULL (fence executed per the bar's second disjunct)

## Follow-ups proposed (1–3, all verified absent from battery-queue.json)

1. `estque-07-subject` (P3) — once 07's class is battery-resolved, re-attempt
   the complete parse of the 0b1191 'est que [07] [24]' clause; this is the
   only remaining ladder to re-opening the coordination (the ne-drop
   precedent question stays red-team venue).
2. `a7-rowbreak-et` (P4) — test whether the a7_01/a7_02 row boundary licenses
   a sentence break before '67' (sentence-initial 'Et que' template) under
   standing values; a boundary avenue distinct from coordination.
3. `pour-et-unit` (P4) — close the remaining word-internal arm: test whether
   '00 67' composes a licensed French word/unit at 0b1247–1248; kill if no
   unit licenses 'pour+et' before 'que'.
