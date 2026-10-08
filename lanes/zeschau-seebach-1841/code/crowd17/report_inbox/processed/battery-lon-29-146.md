# Battery report: lon-29-146 — @146 '64 77 84 29 87 64' single-parse resolution

- Target: `lon-29-146`
- Claim: @146 '64 77 84 29 87 64' resolves to one parse
- Verdict: **null** (residual FENCED with stated cause; frame promotion untouched)
- Date: 2026-10-08
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed like code/side-keyhunt/repair_parse.py).
  canonical.py never used. R5005 untouched.
- Lock: locks/lon-29-146.lock (created on start, deleted on completion).

## 1. Pre-registered bar (verbatim)

> resolve iff one parse covers 77-84-29-87 with 29's syllabic profile
> (29->40='e' x9 vs 29->87 x3) and zero contradiction; else fence

Numbered pass/fail clauses (frozen before testing; not modified after seeing data):

1. **C1 — one parse covers the full 77-84-29-87 span** (@145–148).
2. **C2 — the parse uses 29's syllabic profile**: 29='er' as word-final of an
   -er stem, per the attested follower pattern (29->40='e' x9; 29->87 x3 as a
   word-boundary "[stem]er | ce" pattern).
3. **C3 — zero contradiction with standing values**: 64='qui', 77='le'
   (provisional), 84='on' (A15, unconditioned after the collision-62-84 battery),
   29='er' (banked), 87='ce' (granted). The frame-qui-77-84 promotion (A13/A15)
   is a given — this battery resolves or fences a residual on it; it does not
   re-litigate it.

## 2. Method

Re-derived all counts from the repaired stream in this run (python3 against
repaired_offsets.json + upstream-ct_R5005.txt). n(29)=45; n(84)=25.
Enumerated every placement of 29='er' in the @144–149 window
('64 77 84 29 87 64' = "qui l'on [29] ce qui") and checked each against 29's
re-derived contact profile and standing values.

## 3. Window-level evidence

- **Target window @144–149** (row a1_04): 64-77-84-29-87-64 =
  "qui l'on [29] ce qui [96-47-46 = 'par ce que']".
  '84 29' (@146–147) is **unique stream-wide**: 84->29 x1 of n(84)=25.
- **84 successor census**: 59 x4, 24 x3, 02 x2, 92 x2, 09 x2, 29 x1, 26 x1,
  53 x1, 74 x1, 91 x1, 73 x1, 51 x1. Every other successor is 'on'-compatible;
  only 29 resists. The anomaly is strictly local to @146.
- **Sister '64 77 84' windows parse cleanly**: @1445 ('37 64 77 84 59 36')
  = "[37] qui l'on est [36]"; @1801 ('87 64 77 84 59 35') = "ce qui l'on est
  [35]". Both take 84->59 ('on est'). Only @144 has 84->29.
- **29's profile** (re-derived): predecessors 33 x5, 86 x4, 06 x4, 34 x3,
  64 x3, 03 x3 (stem-shaped; 84 x1 = this window only). Successors:
  40 x9, 89 x5, 47 x4, 80 x4, 42 x3, 85 x3, 87 x3, 82 x3. 29='er' is
  overwhelmingly word-final of an -er stem; 29 word-initial is unattested.
- **The other two 29-87 windows** (@627: '33 29 87 78'; @1425: '33 29 87 63')
  both show the word-boundary pattern "[stem]er | ce [X]" (cf. erstem-33-id
  "[X]er ce" frames). The @147 29-87 junction matches that pattern exactly —
  the failure is the LEFT context (84='on' cannot be the stem), not the
  29-87 junction.

## 4. Parse attempts (all under standing values)

- (a) 29='er' word-final, attaching left to 84: "on"+"er" = "oner" — not a
  French word. FAIL.
- (b) 29='er' word-initial before 87='ce': no French word is "[er]ce"-shaped
  with 'ce' as an independent word; 29 word-initial is unattested stream-wide
  (its sole 84-predecessor is this window). FAIL.
- (c) 29='er' as a standalone word: 'er' is not a French word. FAIL.
- (d) 29-87 word-internal ("erce") with 87 as a syllable: re-litigates the
  granted 87='ce' word value — forbidden by the brief. FAIL.
- (e) "qui l'on erre ce qui" (29-87 as "erre"): two subjects ('qui' + 'on')
  and no verb slot — ungrammatical. FAIL.

No placement of 29 covers the span. Adverses:

- **"29 rarely word-initial (pre {33 x5, 86 x4, 06 x4, 34 x3})" — ANSWERED**:
  re-derived exactly; 84->29 x1 stream-wide (this window) confirms the profile
  has no word-initial-after-'on' support. This is the fence cause, not a
  contradiction.
- **"frame-qui-77-84 PROMOTED — residual, not re-litigation" — HONORED**:
  the promotion stands on its 77-independent legs (A15 "qu'on en" x2,
  "mon"@166) and the two sister '64 77 84' windows re-derived clean above.
  Nothing here touches the frame.

## 5. Per-clause verdict

- **C1 — FAIL**: no single parse covers 77-84-29-87; all five placements
  exhausted above.
- **C2 — vacuous** (no parse to profile-check); noted: the 29-87 junction
  matches the attested "[stem]er | ce" pattern, sharpening the fence to the
  84 left context.
- **C3 — PASS (by fencing)**: no standing value is contradicted; the window
  is fenced instead.

Bar's resolve arm not met; bar's explicit else arm taken: **FENCE**.

## 6. Verdict: null — @146 fenced as residual R3

@146 ('84-29') is fenced as a genuine 1-window residual under the promoted
frame-qui-77-84, joining A15-C3's fenced R1 (@1619) and R2 (@1664). Stated
cause: '84 29' is unique stream-wide; 29='er' can neither attach left to
'on' nor open a word before 'ce' under its re-derived profile, so no parse
covers 77-84-29-87 with zero contradiction. The frame-qui-77-84 promotion,
the 84='on' grant, and the 'l'on' legs are untouched. This null does not
contradict any standing red-team verdict; nothing is downgraded.

## 7. Follow-ups (null regenerates work)

1. **lon-legs-census** — re-derive all 7 'l'on' legs (@145/259/1057/1446/
   1484/1763/1802) under post-collision unconditioned 84='on'; grade each
   leg's dependence on provisional 77='le' (A15-C1 inheritance); record
   @146 as fenced R3 alongside R1/R2.
2. **fence-84-29-gate** — gated re-parse of @146 under a hypothetical
   non-'on' 84 reading. Gated: declaring a second polyvalence is a red-team
   act (§7, 67 sole true polyvalence). Battery gathers only the evidence
   (84-successor census: 29 x1 unique vs all other successors 'on'-
   compatible) for red-team adjudication.
3. **profile-29-left** — full left-context census of 29 (n=45): test whether
   any 29 window parses with 29 word-initial. A positive would un-fence
   @146; a negative closes the word-initial question lane-wide.
