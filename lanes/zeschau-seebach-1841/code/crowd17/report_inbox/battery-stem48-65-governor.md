# Battery report: stem48-65-governor — 2026-10-09

Worker: 9d3922e1-fcc4-4976-9e47-85819f6e4402. Stream: repaired 1,847-pair parse
(code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parsed per
code/side-keyhunt/repair_parse.py). @-offsets below are 0-based pair indices
(@1589 = 48; the 65 token is @1588). Lock: locks/stem48-65-governor.lock created
2026-10-09T06:05:33Z (no fresh lock present). canonical.py not used. R5005,
sealed gates, red-team queue untouched.

## Standing facts (not re-litigated)

- 65 = NOUN-CLASS promoted (R18); 65's syntactic role at @1589 is unnameable
  under standing values (battery-stem48-65-value, null, 2026-10-09). Not
  re-argued here.
- "48-29" at @1589 = "[65] [STEM]er" infinitive (stem48-exclusive-legs:
  ungrammatical under 48='e', grammatical under 48=verb-stem; STEM-REQUIRED).
  "48 29" occurs exactly x2 in the stream (@1229, @1589 — the two A7-L2
  exclusive legs).
- 64="qui" granted unconditioned; "qui"+bare infinitive ungrammatical (lane
  precedent battery-at21-82-43-29). 00="pour" (A9 leg-1 class-level).
  80/89 = A8 verb-frames (value open). 24 = finite modal verb
  (ne-24-profile, battery-grade; the 24-en-verb-conflict is red-team venue,
  not resolved here).

## Bar (verbatim, pre-registered BEFORE testing)

1. "Produce a full-window grammatical parse of the @1589 window with every
   token licensed,"
2. "or confirm the window as a syntax orphan with the orphan's locus named
   (65? qui? the 64-65 boundary?)."
3. "Do not re-litigate the null: 65's role at @1589 is unnameable under
   standing values; this is governor discovery."

## Numbered clauses (restated before testing; bar unmodified)

1. PARSE-OR-ORPHAN: (a) a full-window grammatical parse of the @1589 window
   with every token licensed, OR (b) the window confirmed as a syntax orphan
   with the orphan's locus named.
2. NO-RELITIGATION: 65's role at @1589 is not re-litigated; this battery is
   governor discovery only.

## Method

Re-derived the @1589 window byte-by-byte from the repaired stream (never
canonical.py). Applied standing values only; open tokens left open. Tested
each named governor candidate (24, 00, 80) against 1841 French grammar, then
swept every other token in @1578–1605 for governor candidacy. Ran three
censuses: (i) "24 ... X-29" governance distance (n(24)=52); (ii) "00 ... X-29"
(n(00)=55); (iii) "X-29 ... 80" leftward (n(80)=17). Checked the "48 29"
bigram lane-wide and the 9-left slot of both hits.

## Evidence — the @1589 window

Row a8_02, stream @1578–1605 (0-based):

`47 98 24 53 12 44 00 36 70 64 65 48 29 47 08 81 03 29 80 67 77 81 82 98 00 44`

Standing values applied:

`ce(47) [98] [24] [53] n(12) [44] pour(00) [36] pre(70) qui(64) [65-noun]
[STEM]er(48-29) ce(47) [08] [81] [03]er(03-29) [80-verbframe] et(67; follower
77 not infinitive-shaped) le(77) [81] me(82) [98] pour(00) [44]`

### Governor candidate tests

**1. 24 (@1580) governs "[65] [STEM]er ce [08]"? FAIL.**
- Distance 9 with "53 12 44 pour [36]pre qui [65]" intervening. French modals
  govern infinitives adjacently or across clitics only; a relative-clause
  boundary ("qui [65]") between modal and infinitive is unlicensed, and
  gapping across it was already killed (stem48-65-value candidate 9).
- Lane precedent for 24+infinitive is ADJACENT: @1319 "24 03 29 80"
  ("24 [03]er"). No window shows 24 governing an infinitive at distance >1.
- Census: 13 of 52 "24" tokens have an "X-29" within +12, but every instance
  except @1580 and @1220 is adjacent or near-adjacent; the two distance-9
  instances are exactly the two A7-L2 legs (see parallel below), where the
  "qui" block applies equally.

**2. 00 (@1584, "pour") governs "[65] [STEM]er ce [08]"? FAIL.**
- 00 is saturated: it governs the adjacent "[36]pre" ("pour [36]pre").
  "pour" takes one complement.
- "pour"+infinitive is adjacent-only in this stream: @1153 "00 92 29"
  ("pour [92]er [80]") is the clean precedent. At @1584 the adjacent
  constituent is the noun "[36]", not an infinitive.
- The interrogative-infinitive route ("pour qui [65] [STEM]er") fails twice:
  (a) 65 intervenes between "qui" and the infinitive — French interrogative
  infinitives bar expressed subjects; (b) "ce" (@1591) would be a second
  accusative (no double accusatives). Both causes stated in stem48-65-value
  candidate 3; adopted here, not re-litigated.

**3. 80 (@1596, A8 verb-frame) governs "[65] [STEM]er ce [08]"? FAIL.**
- Directionality: 80 sits 7 tokens DOWNSTREAM of the infinitive
  ("[STEM]er ce [08] [81] [03]er [80]"). French verbs do not take leftward
  infinitive complements.
- 80's own infinitive construction is the adjacent "[X]er [80]" (x4:
  @1030 "03 29 80", @1154 "92 29 80", @1320 "03 29 80", @1594 "03 29 80").
  Whatever its parse (candidate: infinitive-subject + finite 80), it binds
  the NEAREST infinitive — "[03]er" @1594–1595, not one 7 tokens away with
  "ce [08] [81]" intervening.

### Governor sweep (all other tokens @1578–1605): none available

- 98 (@1579): distance 10, same "qui" block as 24; "ce [98] [24]" is itself
  two adjacent finite verbs under battery standing (unlicensed; dependent on
  the red-team 24-en-verb-conflict venue — noted, not resolved).
- 36 (@1585), 81 (@1593): nouns; French nouns take infinitive complements
  via "de"/"à" only; neither present in the window.
- 64 (@1587): "qui" — relatives do not govern infinitives.
- 65 (@1588): the infinitive's own stem slot; self-governance impossible.
- 03 (@1594): itself infinitive ("[03]er"); infinitives do not govern
  infinitives.
- 98 (@1601): downstream; locally licensed as "le [81] me [98]" (subject +
  clitic + finite verb) — its complement is "me", not the @1589 infinitive.
- 47/53/12/44/70/77/82/08: pronouns, letters, open tokens, prepositions —
  none govern infinitives.

### Positive finding: the "24 at i-9" parallel (byte-exact)

"48 29" occurs exactly twice (@1229, @1589). BOTH have 24 exactly 9 tokens
to the left:

- @1229: `24 48 30 09 20 57 64 79 82 | 48 29 47 33` ("24 [48] 30 [09] [20]
  [57] qui tout me [STEM]er ce [33]er")
- @1589: `24 53 12 44 00 36 70 64 65 | 48 29 47 08` ("24 [53] [12] [44] pour
  [36]pre qui [65] [STEM]er ce [08]")

Common envelope: 24 @ i-9, 64 ("qui") @ i-2/i-3, "48 29" @ i/i+1, 47 ("ce")
@ i+2. With n(24)=52 over 1,847 pairs, P(24 at exactly i-9) ≈ 0.028 per
window; both exclusive legs hitting it is ≈ 0.0008 — not coincidence. The
parallel does NOT license 24 as governor (the "qui" block applies in both
windows), but it is a structural signature shared by the two exclusive A7-L2
legs, delivered as scope-ruling input.

### Orphan confirmation

No licensed governor exists for "[65] [STEM]er ce [08]" (@1588–1592): all
three named candidates fail with stated grammatical causes, and the sweep
exhausts the alternatives. The infinitive phrase parses locally (stem48
battery, uncontested) but is syntactically unattached — a syntax orphan.

**Orphan's locus: the "qui [65]" span (@1587–1588), primary defect the
unclosable "qui" (@1587).** "qui" (granted) projects no relative clause:
no finite verb follows it (80 cannot close it — the intervening material
"[65] [STEM]er ce [08] [81] [03]er" forms no clause; 98 is structurally
unavailable), and the interrogative re-read is blocked by the intervening
65 (prior battery, cited not re-litigated). This unclosable "qui [65]"
severs the infinitive from its only upstream governors — 24 (relative-
boundary block) and 00 (interrogative block) — while 80 fails independently
on directionality. 65's own role remains unnameable per the prior null
(cited, not renamed).

Corroboration: the window's left edge "ce [98] [24] [53][12][44]" is
independently unlicensed under battery standing (two adjacent finite verbs),
so no matrix clause exists that could host the infinitive even if the
"qui" block were lifted.

## Per-clause pass/fail

1. PARSE-OR-ORPHAN: **PASS via (b).** No full-window parse is attainable
   ("qui [65] [STEM]er" unlicensed; left edge "ce [98] [24]" unlicensed).
   The window is confirmed as a syntax orphan with the locus named:
   the "qui [65]" span @1587–1588, primary defect the unclosable "qui"
   @1587.
2. NO-RELITIGATION: **PASS.** 65's role at @1589 is not named or renamed;
   the prior null (battery-stem48-65-value) is cited as a premise. This
   battery did governor discovery only.

## Verdict: PROMOTE (battery-grade; needs red-team ratification)

All bar clauses pass; no adverses were listed. The promoted finding: the
@1589 infinitive "[65] [STEM]er ce [08]" is a confirmed syntax orphan —
governorless under standing values — with the breakage localized to the
unclosable "qui [65]" (@1587–1588). Plus the byte-exact "24 at i-9"
signature shared by both exclusive A7-L2 legs (@1229/@1589), delivered as
A7-L2 scope-ruling input.

## Follow-up targets (leads, not nulls)

1. **24-nine-left-envelope** (priority 2): "48 29" x2 both carry 24 at
   exactly i-9 with "qui" at i-2/i-3. Census: for every "X 29" infinitive-
   shaped token lane-wide, record the token at i-9; test whether "24 @ i-9"
   recurs beyond the two A7-L2 legs. Bar: envelope census with @-offsets;
   if "24 @ i-9" recurs at further infinitive windows, name the
   construction; if the two legs are the only hits, fence as a two-leg
   signature for the A7-L2 scope docket.
2. **infsub-80-frame** (priority 3): "[X]er [80]" x4 (@1030/@1154/@1320/
   @1594). Test the infinitive-subject reading ("to-[X] [80-s]") against
   the A8 verb-frame grant at all four windows, without overwriting the
   grant. Bar: all four windows parsed under one 80-frame statement, or
   the readings split with stated cause per window.

## Provenance

n(24)=52, n(00)=55, n(80)=17, n("48 29")=2, n("98 24")=1, n("X 29 80")=4 —
all re-derived from the repaired stream in-work. No invented data, no
invented constructions; every rejected governor carries its stated
grammatical cause. Lock created on start, deleted on completion.
