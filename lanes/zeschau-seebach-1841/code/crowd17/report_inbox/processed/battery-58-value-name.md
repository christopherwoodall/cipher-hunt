# Battery `58-value-name` — verdict: NULL (fence)

## Bar (verbatim, pre-registered)
"One French noun fitting all three frames with zero ungranted assumptions; fence if the lexical field underdetermines. Value only; class standing not re-opened."

Restated:
- C1: one French noun fits @1756 "[58] fois" with zero ungranted assumptions.
- C2: the same noun fits @1695 "qu'en [85] [58]" with zero ungranted assumptions.
- C3: the same noun fits @1202 "ce [58]" with zero ungranted assumptions.
- C4 (else-arm): if no single noun fits all three, fence with stated cause.

## Method
Re-derived the repaired 1,847-pair / 96-type stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`
(parsed like `repair_parse.py`; asserts held: 1847 pairs, 96 types).
`canonical.py` never used. Adopted premises: 17=fois (promoted),
46=que (banked ground truth), 47=ce (A4 granted), 24 finite/modal-shaped
verb class (R17-009), 85 verb-stem (A3 grant), 45=ce (A11 HOLD, ungranted),
58 nominal class (`58-complement-1695` PROMOTE, not re-opened).

## Window-level evidence (byte-exact, 0-based)

**W1 @1756** (row a8_08): `@1753..1759 = 26 24 85 | 58 | 17 78 41`
→ "…[24] [85] [58] fois [78]…". 58 directly precedes 17='fois'; @1755=85
(verb-stem). n(58)=7: [55, 122, 157, 610, 1202, 1695, 1756].

**W2 @1695** (row a8_06): `@1690..1698 = 60 27 46 24 | 85 58 | 15 23 91`
→ "…[27] que [24] [85] [58] [15]…". CORRECTION to the claim's shorthand:
the window is "que [24] [85] [58]", NOT "qu'en [85] [58]" (@1693=24, not 14).
58 is the bare direct object of the 85-infinitive governed by modal 24.
"85 58" bigram also at @1755–1756 — the same verb+object geometry in both
windows.

**W3 @1202** (row a7_00): `@1199..1205 = 64 29 45 | 58 | 47 43 55`
→ "…qui er [45] [58] ce [43]…". Under the A11 HOLD (45='ce', ungranted),
"ce [58]" forces 58 to be a masculine singular noun.

## Per-clause results

- **C1: frame A forces a non-noun slot.** In 1841 French, the only words that
  can stand bare directly before "fois" are determiners, numerals, and
  indefinite adjectives: "chaque fois", "une/deux/trois fois",
  "plusieurs/quelques/maintes/mille/cent fois", "d'autre fois",
  "quelque fois". No bare common noun can directly precede "fois"
  (*"jour fois", *"temps fois" — ungrammatical every period). The wider
  context strengthens the numeral reading: "…[24] [85] [58] fois…" =
  "…[modal] [verb] deux fois" ("répéter deux fois"-shaped) — fully
  grammatical with 58 = numeral.
- **C2: frame B coheres with the numeral/determiner reading.** "que [24]
  [85] [58] [15]" = "que [modal] [verb] deux/plusieurs/quelques [15]"
  ("que veut répéter deux [15]"-shaped) — grammatical iff @1696=15 is a
  (plural) noun. The bare-object-noun reading ("prendre conseil"-shaped)
  is also live, but the A∧B pair jointly favors {numeral, indefinite
  determiner}: "deux/plusieurs/quelques" fits both windows with zero new
  assumptions.
- **C3: frame C forces a masculine noun** ("ce [58]" under the A11 hold) —
  disjoint from the determiner/numeral set. "ce deux", "ce plusieurs",
  "ce quelques", "ce chaque" are all ungrammatical.
- **C4 FIRES.** A∧B cohere on {numeral, indefinite determiner}; C requires
  a masculine noun. The three frames are jointly unsatisfiable by a single
  French noun. The only rescue would be a polyvalent 58, barred at battery
  level (§7: 67 is the sole true polyvalence).

**Verdict rationale:** the bar's promote condition (ONE French noun fitting
all three frames) is not underdetermined — it is excluded. Per the bar's
else-arm: NULL, fence with stated cause. Two compounding notes:
(a) frame C itself rests on the ungranted A11 HOLD (45='ce'), so the bar's
"zero ungranted assumptions" standard cannot be met on the current premises
even before the lexical exclusion; (b) the A∧B numeral reading tensions
against 58's battery-grade nominal class (`58-complement-1695` PROMOTE) —
class standing is NOT re-opened here; the tension is escalated, not resolved.

## Scope
Fences value-naming only. Untouched: 58's nominal class standing
(`58-complement-1695` PROMOTE), `58-noun-adjudicate` NULL, all red-team 58
items, §7 (no polyvalence declared). No standing/red-team verdict
contradicted or downgraded. Canonical-stream caveat stands (rows a8_08,
a8_06, a7_00 offsets unvalidated).

## Follow-ups (all verified ABSENT from battery-queue.json)
1. `58-a11-hold-test` (P3) — 45='ce' at @1201 is an ungranted A11 HOLD; test
   the "45 58" frame under rival 45 values. If 45 is not 'ce', frame C
   dissolves and the A∧B numeral/determiner reading becomes the live value
   hypothesis (with the class tension below).
2. `58-det-numeral-tension` (P2, red-team input) — the A∧B frames cohere on
   a numeral/determiner value ("deux/plusieurs/quelques"-shaped), which
   contradicts 58's battery-grade nominal class. Package the byte evidence
   for red-team adjudication; battery grade cannot resolve a class conflict.
3. `15-noun-verify` (P3) — test 15's class at @1696; a (plural) noun there
   licenses the "que [24] [85] [58=deux/plusieurs] [15]" parse and sharpens
   follow-up 2's package.
