# Battery report: residual-1029-infinitive

- Target id: `residual-1029-infinitive`
- Claim: "@1029 'ceci [03]er [80]-le' resolves once 03's class resolves or fences as 03/80-driven residual"
- Date: 2026-10-09
- Worker: battery worker (subagent 82f0d6a3-06a1-4859-b127-bbe5293a966b)
- Stream: repaired 1,847-pair / 96-type parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed per repair_parse.py). Re-derived in-session:
  **1,847 pairs, 96 types confirmed.** `canonical.py` never used. R5005, sealed
  gates, red-team queue untouched.
- Lock: code/crowd17/next-token/locks/residual-1029-infinitive.lock (created on
  start with agent id + UTC timestamp, deleted on completion).

## Bar (verbatim, pre-registered before testing)

"parse in full context once 03's class resolves (coordinate with queued imp-80-set
and stem-03); test the exclamatory-infinitive reading against the word-order
problem and the word-internal '01-03' lead; fence as a 03/80-driven residual
with stated cause if unparseable"

Numbered pass/fail clauses (restated before testing, not modified after):

1. (C1) Parse the @1029 window in full context now that 03's class has resolved
   (stem-03 battery PROMOTE, 2026-10-09), coordinating with imp-80-set and stem-03.
2. (C2) Test the exclamatory-infinitive reading against (a) the word-order
   problem and (b) the word-internal '01-03' lead.
3. (C3) If unparseable, fence as a 03/80-driven residual with stated cause.

## Coordination reads (premises adopted, not re-litigated)

- **stem-03 → verdict/promote (battery grade, 2026-10-09):** 03 = verb stem
  (class, value open). Three independent infinitive frames: F1 "faire [03]er"
  @1321 (1b, a7_04), F2 exclamatory "[03]er!" @1031 (1b, a6_03, the locus),
  F3 80-frame "[03]er" @1595 (1b, a8_02). Note: @-offsets in that report are
  1-based; the locus "03 29" is 0b1030–1031 / 1b@1031–1032.
- **imp-80-set → verdict/null:** the imperative set stands at n=2 on the
  enclitic diagnostic ('80-77' = "[80]-le"), but the @1032 reading "[03]er
  [80]-le" as imperative + enclitic is battery grade (no ungranted assumption
  beyond provisional 77='le'). The report explicitly flags this target's old
  "@1029 'ceci…'" premise as STALE (01='ci' standalone killed, ci-01-value);
  the surviving form is bound-'-ci' (ci-bound-01 null). 80's mood alternation
  is red-team venue; not declared here.
- **ce01-slot-1029-infinitive-avenue → verdict/null:** fenced @1028–1031
  ("ce [01] [03]er") WITHOUT the exclamatory-infinitive assumption; killed
  avenues A–N (grammar/archaism/profile). With the assumption, the window
  parses (consistent with skeleton-1032-revise's battery-grade PROMOTE).
- **01-verbclass-probe → verdict/null:** avenue A (01 as finite modal) is
  re-opened at profile level — 0b1255 (1b@1256, row a7_02) is verb-shaped
  for 01 ("…[06] [65-N] que [01] [61]…" = inversion "que [01-V] [61-S]",
  P1 preferred; P2 nominal-subject live). §7 tension is red-team venue.
- **skeleton-1032-revise → verdict/promote (battery grade, unratified):**
  "Ceci, [03]er! [80]-le, la première fois!" with bound-01='-ci' as the sole
  non-granted assumption.
- **Corpus program (disloc-demonstrative-*):** demonstrative-headed bare
  exclamatory infinitives fenced at 7+ levels (RDM full corpus, RDM quoted
  dialogue, RDM inversion, drama full text ×2 editions, drama dialogue
  comma-heads, drama full-text non-comma separators, drama dialogue
  non-comma separators, prose clause-initial, prose separators, epistolary,
  comedy recall) — 0 genuine across ~45M chars. The head-inventory battery
  found the licensing contrast: tonic-pronoun topics DO license bare
  exclamatory infinitives (5 genuine: "moi, fuir devant le duc de Guise!",
  "moi, céder la place à Kemble...", "… Eux rire…", "…moi, épouser une autre
  femme!", "Moi, déprécier le commerce !"), demonstratives never do
  (0/13 candidates genuine).

## Window-level evidence (all byte-verified)

Locus + full context (0-based 0b; 1-based 1b = 0b+1), all on row a6_03:

- 0b1019–1028 (1b@1020–@1029): `91 53 84 92 64 45 64 96 43 87`
  = "…[91] [53] on(84) [92] qui(64) [45] qui(64) par(96) [43] ‖ ce(87)…"
  — the "…qui [45] qui par [43]" relative clause closes; clean sentence
  boundary at 0b1027|1028 (1b@1028|@1029).
- 0b1028–1040 (1b@1029–@1041): `87 01 03 29 80 77 11 70 82 34 29 40 17`
  = "ce [01] [03]er [80]-le la pre mi er e fois" (11/70/82/34/29/40 GT,
  17=fois promoted → "la première fois", the anchored pencil crib).
- 0b1041–1046 (1b@1042–@1047): `77 82 63 11 67 76`
  = "le(77, provisional) m'(82, GT) [63] la(11) et(67, positional) [76]…"
  — new clause begins; clean sentence boundary at 0b1040|1041
  (1b@1041|@1042).

### C1: full-context parse with 03 resolved

**"Ceci, [03-stem]er! [80]-le, la première fois!"**

- 87='ce' granted; 01 = bound '-ci' (battery-level null, ci-bound-01; 01='ci'
  standalone killed — the RE-BRIEF from imp-80-set's stale-premise flag is
  applied).
- 03 = verb stem (stem-03 PROMOTE, battery grade). "03 29" = "[03-stem]er",
  an unconditional infinitive under 29='er' GT. The exclamatory-infinitive
  leg no longer needs the conditioned-split hedge that the avenue battery
  adopted.
- 80 = imperative verb class (imp-80-set's enclitic diagnostic, battery
  grade); 77='le' provisional → "[80]-le", imperative + enclitic object.
  Byte order 80-77 excludes proclitic "il le [80]".
- "la première fois" = byte-anchored crib, temporal adverbial.
- Left boundary (0b1027|1028) and right boundary (0b1040|1041) are both
  byte-clean clause breaks under standing values.

New vs. the avenue battery's NULL: the infinitive leg is now battery grade
(03's class resolved); the left half is no longer stranded once the
exclamatory-infinitive reading is admitted — which this bar explicitly tests.

### C2a: the word-order problem

The reading requires dislocated tonic-demonstrative "ceci" heading a bare
exclamatory infinitive. The corpus program fences this exact shape at 7+
levels with 0 genuine demonstrative-headed attestations, while tonic-pronoun
heads are attested (5 genuine). **This is a register-fence at null grade —
zero is an absence (per §4), not a kill.** It does not contradict any
standing or red-team verdict (Round 18 has zero mentions of @1028). The
reading stands at battery grade with the fence as a stated caveat. The
corpus fence is the strongest counter-evidence against this promote and is
flagged for red-team awareness.

### C2b: the word-internal '01-03' lead

"01 03" census: **stream hapax — exactly 1 occurrence in 1,847 pairs, at the
locus itself** (0b1029). "01 03 29" likewise 1/1847. Neither 01 nor 03 has
any letter-tier value anywhere (both value-open), so no French word can be
composed without invention. The lead is fenced as untestable at battery
grade — not a rescue, and it does not disturb the parse.

### Avenue A re-check (new from 01-verbclass-probe)

01's verb-ness (0b1255 inversion parse) does NOT rescue @1028–1031: avenue
A's death had two legs, and only the profile leg fell. The TLFi archaism
leg ("ce" as subject of a lexical verb is rare/archaic in 1841, via
ce-inf-1841) was never re-litigated, and the @1256 parse is inversion
("que [01-V] [61-S]") — no inversion is available at @1029 because the
follower (03, verb stem) is not nominal. "ce [01-V] [03-stem]er" stays dead
at battery grade at this window. The §7 01 tension (nominal vs verbal) is
red-team venue.

### C3: not fired

The window parses at battery grade (above); no 03/80-driven residual fence
is drawn.

## Per-clause pass/fail

1. **C1: PASS** — full-context parse lands (above) with 03's class resolved.
2. **C2: PASS** — word-order problem tested (null-grade register fence,
   stated as caveat, not kill-grade); '01-03' lead fenced (hapax,
   untestable).
3. **C3: N/A** — parseable; the residual is not fenced.

## Adverses, answered

- "80's mood open (red-team act per §7)": answered — the parse needs only
  the local imperative, which is battery grade via imp-80-set's enclitic
  diagnostic ('80-77' x2). No mood alternation is declared; §7 is honored;
  the poly-80 docket (queued P1) is untouched.
- "coordinate with queued imp-80-set and stem-03": done — imp-80-set's NULL
  (with its stale-premise re-brief applied) and stem-03's PROMOTE are both
  adopted as premises above.

## Verdict: PROMOTE

The claim's condition is met: 03's class resolved (verb stem, battery grade),
and "@1029 'ceci [03]er [80]-le'" now parses in full context at battery
grade as "Ceci, [03-stem]er! [80]-le, la première fois!" The result converges
with (does not duplicate) skeleton-1032-revise's PROMOTE; what is new here:
03-class resolution removing the conditioned-split hedge, the 7-level
register-fence caveat, the @1256/TLFi avenue-A note, and the '01-03' hapax
fence. No standing or red-team verdict is contradicted or downgraded; §7
intact. Canonical-stream caveat stands (row a6_03's offset is unvalidated).
Promote, not null — no follow-ups required.

## Red-team headline (not a finding)

The 7-level corpus fence on demonstrative-headed bare exclamatory
infinitives is the strongest counter-evidence against this promote: the
parse's topic head ("ceci") is exactly the fenced shape, while tonic
pronouns (which the letter cannot deploy at 87) do license it. The promote
is battery grade; the fence is null grade. Adjudication of which carries
more weight is red-team venue.
