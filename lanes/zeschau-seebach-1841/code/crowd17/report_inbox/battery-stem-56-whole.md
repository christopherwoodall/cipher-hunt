# Battery report: stem-56-whole

Target: `stem-56-whole`. Date: 2026-10-09. Worker: 7a30b68e-7a46-485b-89f6-c37af900a5d0.
Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`, parsed like `code/side-keyhunt/repair_parse.py`;
1,847 pairs / 96 types re-verified in-worker). `canonical.py` never used. R5005,
sealed gates, red-team queue untouched. @-offsets are 0-based stream indices
(queue convention; brief's @795/@1626/@1745 match).

## Bar (verbatim, pre-registered)

"<=10% orphan rate per A10; red-team eyes on whether the noun/verb class
alternation needs a second-polyvalence declaration or resolves via
substantivization/inflection"

Numbered clauses (fixed before testing, not modified after):

1. C1 — the A10 orphan-rate test is applied to 56's stem/whole status across
   all n(56) windows: one uniform status (all-stem or all-whole) covers the
   windows with <=10% orphan (stem-44-nominal formulation of the A10 standard).
2. C2 — red-team-eyes analysis delivered: does 56's noun/verb class
   alternation need a second-polyvalence declaration, or does it resolve via
   substantivization/inflection? (Analysis only; battery declares no
   polyvalence per §7.)

## The A10 standard as applied

Precedents: dire-33-set (two-member set {stem-X, whole-'dire'}, orphans 2/25 =
8% <= 10% → set unfalsified, HELD as A10); stem-44-nominal (uniform test:
whole-only orphans 13.3% > 10%, stem-only 86.7% → neither meets bar → NULL,
split fenced for red team). Decision rule used here (stem-44-nominal
formulation): ONE uniform status covers all windows with <=10% orphan; if met,
the status is decided. "Forced" follows the 44 methodology: a window is an
orphan of a status iff that status strands a non-word or overturns a
banked/granted value (nameability standard for compositions).

## Method

Full census of 56's 23 windows on the repaired stream (indices
[70, 132, 193, 243, 502, 514, 795, 836, 932, 963, 1003, 1235, 1277, 1282,
1326, 1507, 1571, 1626, 1640, 1654, 1732, 1745, 1793] — byte-re-derived, not
copied). Each window tested for (a) forced stem-level composition
(whole-word parse strands a non-word / violates standing values) and
(b) nameable word-internal composition (without overturning banked/granted
values). Standing values used: pencil GT (11=la, 70=pre, 82=m, 34=i, 29=er,
40=e, 46=que); granted (87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour,
84=on, 47=ce); battery-standing (94=ne STRONG LEAD, 30=pas, 06=ent,
12=n, 48=e); provisional (59=est, 77=le). 56's value open throughout
(name-56-verb still queued; no value named here — no duplication).

## Window-level evidence (stem-level vs whole-word)

**Forced stem-level: 1 window.**

- @1745 (a8_07/a8_08): "94 82 46 |56| 40 06 65" = "ne m que [56]e ent [65]".
  Whole-word 56 strands "40 06": "40 06" is a stream hapax (1x, this window);
  "56 40" occurs 1x stream-wide (this window); "e"+"ent" is not a French
  word, and no alternative segmentation parses ("56 40"|"06" strands "ent";
  "56"|"40 06" strands "eent"). The stem parse "que [56]e-ent" (Xéent-class
  3pl verb: cf. "créent", "agréent") parses with zero contradiction
  (rightedge-56-1745 C2, PASS — adopted as premise, not re-litigated).
  FORCED STEM-LEVEL. The stranding is 56-driven (it vanishes iff 56 is
  stem-level), so the orphan cannot be fenced to a neighbor.

**Whole-word: 22 windows** (no nameable word-internal composition; whole-word
token parses; letter-tier adjacencies checked individually below).

- @70 (a1_02): "13 24 |56| 87 14 24". R=87='ce' granted — rightward
  composition overturns a granted value; leftward "24"+"56" (24 verb-class)
  not nameable. WHOLE.
- @132 (a1_03): "32 96 |56| 64 21 65". L=96='par' granted, R=64='qui' banked
  GT — both compositions overturn standing values. WHOLE (forced).
- @193 (a2_00): "87 98 |56| 47 01 21". R=47='ce' granted; L=98 finite-verb
  class (prof-98 whole-word) — "98"+"56" not nameable. WHOLE (forced).
- @243 (a2_01): "12 16 |56| 43 00 66". No nameable composition either side
  (16 conflicted/fenced, 43 value open; no French word statable). WHOLE.
- @502 (a3_00): "29 40 |56| 39 68 21". L=40='e' attaches LEFTWARD to 29
  ("11 29 40" -ere ending per fem-e-48; 40 never word-initial at battery
  grade) — not stranded, belongs to 29's word. Rightward "56"+"39" not
  nameable. WHOLE.
- @514 (a3_00): "65 88 |56| 87 77 80". R=87='ce' granted; L=88 verb class —
  not nameable. WHOLE (forced).
- @795 (a5_04): "07 64 |56| 37 44 77". L=64='qui' banked GT; R=37
  predicative frame (A1) — "56"+"37" not nameable (no stem+predicative
  license). Bare-56 verb window: "qui [56]" finite-verb slot. WHOLE.
- @836 (a5_06): "59 35 |56| 17 98 20". R=17='fois' granted — rightward
  composition overturns it; L=35 noun class — not nameable. WHOLE (forced).
- @932 (a5_10): "98 83 |56| 69 26 00". L=83 ('de' conditioned word);
  R=69 noun class (battery) — neither composition nameable. WHOLE.
- @963 (a6_00): "00 86 |56| 41 19 24". L=86, R=41 (§7 split candidate) —
  no nameable word either side. WHOLE.
- @1003 (a6_02): "00 86 |56| 47 91 11". R=47='ce' granted; L=86 not
  nameable. WHOLE (forced).
- @1235 (a7_01): "29 85 |56| 10 03 40". L=85 verb-stem frame; R=10 open —
  no nameable composition. WHOLE.
- @1277 (a7_03): "76 48 |56| 85 48 53". L=48='e': 48's attachment (to 76,
  a promoted masculine noun) is 48's own open question, identical under
  stem-56 or whole-56 — not 56-driven, not a 56-orphan. R=85 not nameable.
  56 itself a clean token. WHOLE.
- @1282 (a7_03): "53 61 |56| 32 98 55". L=61 (locus-level "premier");
  R=32 verb lexeme (R17-008 class-level) — neither composition nameable.
  WHOLE.
- @1326 (a7_04): "62 98 |56| 30 06 62". R=30='pas' promoted — "56pas"
  word-internal fails per w2-pas-nelicense (no verb ends "-pas");
  composition would overturn promoted 30. L=98 finite-verb class — not
  nameable. WHOLE (forced).
- @1507 (a7_11): "00 86 |56| 41 12 61". As @963. WHOLE.
- @1571 (a8_01): "62 48 |56| 32 28 52". L=48='e' — same as @1277: 48's
  question, not 56-driven. R=32 verb lexeme — not nameable. WHOLE.
- @1626 (a8_03): "33 46 |56| 69 26 00". L=46='que' banked GT; R=69 noun
  class — not nameable. Bare-56 verb window: "que [56]" finite-verb slot.
  WHOLE (forced).
- @1640 (a8_04): "74 35 |56| 12 33 98". R=12='n' letter-tier: 12's
  composition with 33 ("n"+"dire"-stem) is 12's own open question,
  identical under stem-56 or whole-56 — not 56-driven, not a 56-orphan.
  L=35 noun class — not nameable. 56 a clean token. WHOLE.
- @1654 (a8_04): "16 01 |56| 37 11 24". L=01 open; R=37 predicative frame —
  neither nameable. WHOLE.
- @1732 (a8_07): "15 01 |56| 30 06 60". R=30='pas' promoted ("56pas"
  fails); L=01 open — not nameable. w5-pas-verb PROMOTE: 56 = finite verb
  (class-level) negated by bare 'pas' — whole-word finite verb. WHOLE
  (forced).
- @1793 (a8_09): "03 00 86 |56| 42 94 59". L=86; R=42 predicative frame —
  neither nameable. WHOLE.

## Orphan computation (A10)

- n(56) = 23.
- Uniform whole-only: orphans = {@1745} = 1/23 = **4.3% <= 10%** → MEETS bar.
- Uniform stem-only: orphans = 22/23 = 95.7% → fails.
- Two-member set {stem-56, bare-56}: orphans 0/23 = 0% → unfalsified
  (recorded; declaration reserved per §7, see below).

## Per-clause pass/fail

- **C1 — PASS.** One uniform status (whole-word / bare-56) covers 22/23
  windows with 1 orphan (4.3%) <= 10%. The A10 stem/whole status of 56 is
  decided: 56 is whole-word (bare-56). @1745 is the single budgeted orphan,
  fenced with stated cause (clean "[56]e-ent" stem parse per
  rightedge-56-1745 C2; stranding 56-driven; within the 10% budget — the
  budget exists for exactly this).
- **C2 — PASS (delivered below).** Red-team-eyes analysis on the noun/verb
  class alternation.

## C2 — red-team eyes: 56's noun/verb class alternation

Class profile (segmentation held at whole-word per C1; classes are
window-level, no class uniformity claimed):

- **Verb-forced (4 windows):** @795 "qui [56]" (relative "qui" requires a
  finite verb); @1626 "que [56]" (same); @1732 "[56] pas" (w5-pas-verb
  PROMOTE: finite verb, class-level); @1745 "que [56]e-ent" (verb stem +
  3pl ending; the orphan window).
- **Nominal (2 forced, ~8 leaning):** @132 "par [56] qui" — "qui" needs a
  nominal antecedent (forced); @836 "[56] fois" — "N fois" quantifier slot
  (forced); "56 87" x2 (@70/@514) + "56 47" x2 (@193/@1003) pre-"ce"
  (leaning — "V ce" ungrammatical in this position); "56 37" x2
  (@795/@1654) + "56 32" x2 (@1282/@1571) + "56 42" x1 (@1793)
  pre-predicative subject slots (leaning).

- **Inflection test:** one verb stem X (Xéent class) covers all four verb
  windows by inflection alone — bare X as 3sg ("il X": @795/@1626/@1732;
  -er 3sg present is the bare stem) vs X+"e"+"ent" as 3pl ("ils Xent":
  @1745). Inflection reconciles stem/bare. It does NOT reconcile
  noun/verb: a bare stem in nominal slots ("par [X] qui", "[X] fois") is
  unlicensed in 1841 French.
- **Substantivization test:** French substantivizes infinitives ("le
  boire"), not bare stems. A bare-stem substantivization for the nominal
  windows is unlicensed. Fails.
- **Finding for red-team eyes:** the noun/verb alternation is genuine and
  does not resolve via inflection or substantivization at battery grade.
  Open routes: (a) second-polyvalence declaration for 56 (red-team act
  under §7 — 67 et/veut is currently the sole true polyvalence);
  (b) re-analysis of the nominal windows; (c) the homophony route.
  name-56-verb (queued) owns the verb-identity question; a poly-56 docket
  would own the class split. Battery declares neither.

## Adverses answered

- **§7 sole-polyvalence (67):** answered — the verdict declares a UNIFORM
  segmentation status (whole-word), not a polyvalence. The @1745 orphan is
  fenced with stated cause inside the A10 10% budget, not declared as a
  second value. The class-alternation polyvalence question is escalated to
  red-team eyes per the bar, not decided.
- **Coordinate with name-56-verb, do not duplicate:** answered — no value
  named for 56 anywhere in this report; the verb-identity (Xéent-class
  discrimination: créer/agréer/suppléer/…) remains entirely with
  name-56-verb.

## Verdict

**PROMOTE** — 56's A10 stem/whole status is adjudicated: 56 is whole-word
(bare-56) across the stream; uniform whole-only carries 1 orphan in 23
(4.3%) <= 10% bar. @1745 ("que [56]e-ent") is fenced as the single budgeted
orphan with stated cause. Promotes no value, names no verb, declares no
polyvalence. Standing state untouched: rightedge-56-1745 NULL stands (its
C2 stem parse adopted as the orphan's stated cause, not re-litigated);
w5-pas-verb PROMOTE (56 finite verb @1732) compatible — whole-word finite
verb; pasent-subject-26-56 kill (56-as-subject dead) compatible; §7 intact.

## Bookkeeping

- Report: this file.
- battery-queue.json: `stem-56-whole` → status `verdict`, result `promote`,
  date 2026-10-09 (temp-file + rename, own entry only; pre-write assert
  confirmed status `queued` — the pre-existing `"verdict": null` key is a
  null placeholder, not a verdict; JSON re-validated post-write).
- Lock `locks/stem-56-whole.lock`: created on start, deleted on completion.
