# Battery report: val-73-776-frame

- Target id: `val-73-776-frame`
- Claim: "name 73 at @776 `[15] [33] [73] [37]`: if 73 resolves nominal, test `croire [73] [37-pred]` vs `dire [73] [37-pred]` selectionally (`croire [NP] [adjectif]` is licensed French; `dire [NP] [adjectif]` is not standard)"
- Date: 2026-10-09
- Worker: battery worker (subagent e13b1322-3545-4613-82d8-b402be2071de)
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json`
  + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`;
  1,847 pairs / 96 types re-derived in-session, asserts held). `canonical.py`
  never used. R5005, sealed gate instances, and the red-team adjudication
  queue untouched. Lock `code/crowd17/next-token/locks/val-73-776-frame.lock`
  created on start, deleted on completion. No fresh lock existed for this id
  (no collision).

## Parentage

Follow-up 2 of the NULL `battery-dire-33-asymmetry-no21.md` (2026-10-09):
the dire/croire asymmetry at 33's windows was fenced as 21-load-bearing;
this battery tests the one 21-independent frame left open, @776's
`[15] [33] [73] [37]`, via the croire/dire predicative-selectional
asymmetry — conditional on 73 resolving nominal.

## Bar (verbatim, pre-registered before testing)

"land the asymmetry iff 73's named value yields a frame grammatical under exactly one candidate"

Restated as numbered pass/fail clauses (fixed BEFORE the stream census, not
modified after):

- **C1:** 73 resolves to a named value at battery grade from the repaired
  stream (n(73) = 6 census).
- **C2:** the named value is nominal (the claim's conditional antecedent).
- **C3:** with 73 nominal and 37 predicative (A1 grant: 37/32/42
  predicative, value open), exactly one of "croire [73] [37-pred]" /
  "dire [73] [37-pred]" is grammatical French.
- **Resolve-arm:** C1 ∧ C2 ∧ C3 all pass → PROMOTE (the asymmetry finding).
  **Else-arm:** NULL with follow-ups. **Kill-arm:** only if a window forces
  the conditional claim false at kill grade or a cleaner rival value for 73
  is demonstrated on the same frames.

## Method

1. Read BATTERY-PROTOCOL.md in full first; verified target `queued` in
   battery-queue.json; created/deleted the lock.
2. Re-derived the repaired stream in-session (1,847 pairs / 96 types,
   asserts held).
3. Full census of 73: **n(73) = 6**, byte-exact on the repaired stream.
4. Naming attempt: distributional + geometric class screen against the
   standing values (§7: 84="on" A15, 47="ce" A4, 34=i crib letter,
   37 predicative A1), testing nominal vs verb-shaped vs letter readings
   on all six windows. No value invented; every number traces to the stream.
5. Coordinated with (never re-litigated or downgraded):
   battery-dire-33-asymmetry-no21 (NULL, 2026-10-09 — parent, 21-fence),
   croire-33-tiebreak (NULL), A10 HOLD (33+29 stem/whole), A15 (84="on"),
   §7 standing values.

## Census (repaired stream, 0-based @; ±5 context; row ids)

- @268: `93 52 33 42 06 73 47 11 06 67 33` [a2_02]
- @392: `91 36 62 91 84 73 34 67 64 79 82` [a2_07]
- @777: `07 06 94 15 33 73 37 08 29 89 11` [a5_04]
- @1110: `78 65 63 00 66 73 41 65 38 30 69` [a6_06]
- @1347: `52 38 47 86 66 73 34 62 48 77 78` [a7_05]
- @1534: `21 65 63 00 66 73 41 62 06 21 62` [a8_00]

Note on @-offsets: the target id's "@776" is 33's position in the parent
report's center=33 convention; 73 sits at 0-based index 777, giving the
frame @775=15, @776=33, @777=73, @778=37. Byte-identical to the parent's
window.

Predecessor set: {06, 84, 33, 66×3}. Successor set: {47, 34, 37, 41×2, 34}.
No determiner (11/77/47-det) ever precedes 73; `66 73 41` recurs
byte-identical @1110/@1534; `66 73 34` @1347.

## Window-level evidence (naming screen)

**W1 — @392 `84 73 34` = "on [73] i".** 84="on" is an A15 grant (§7,
standing). "on" is exclusively a subject pronoun: "on" + bare noun is
ungrammatical French; "on" + 3sg verb is the canonical frame (cf. the
A15 legs 84→59 ×4 "on est"). This window selects VERB-SHAPED 73 and
excludes nominal 73. The follower 34=i (crib letter) is then the next
word's onset or a stem letter — compatible with a verb-stem reading,
incompatible with nothing about the verb screen itself.

**W2 — @268 `06 73 47` = "[06] [73] ce".** 47="ce" is the A4 allophone-tier
pronoun grant. Verb + "ce" as direct object is clean French ("dit ce",
"pense ce"); bare-noun + postposed "ce" is ungrammatical in this order
(demonstrative precedes: "ce [noun]"). Second verb-shaped window,
second strike against nominal.

**W3 — @777 `15 33 73 37` (the test frame).** 37 is predicative-frame
granted (A1; value open). Under a nominal 73 this is exactly the
croire/dire selectional testbed. Under a verb-shaped 73 it parses as
"[33] [verb] [37-pred]" — ungrammatical under BOTH candidates ("dire
faire" ✗, "croire faire" ✗), i.e. no asymmetry available.

**W4/W5/W6 — `66 73 41` ×2 (@1110/@1534), `66 73 34` (@1347).** 66 unnamed;
the trigram's recurrence is the strongest distributional anchor for 73
but does not name it. Consistent with verb-shaped 73 ("[66] [verb]
[41/34]"); no nominal geometry (no determiner, no adjective agreement
cell).

**Letter-reading check.** 73 as a single letter (mixed-granularity cipher:
82=m, 34=i, 40=e are letters) was screened: no single letter yields a
clean parse across all six windows ("on d i" @392 is suggestive but
`06 d ce` @268 and `33 d 37` @777 fail to cohere). No letter value named
at battery grade.

**Net:** 73 is underdetermined as a VALUE (n=6; letter / verb-stem / 3sg-verb
all live) but its two most diagnostic windows are verb-shaped, and nominal
is disfavored by both independent grammatical facts (W1, W2).

## Per-clause results

- **C1: FAIL.** No unique named value for 73 at battery grade. n=6
  underdetermines it; the `66 73 41` ×2 trigram anchors the distribution
  but names nothing.
- **C2: FAIL.** The conditional antecedent does not hold: W1 (@392
  `84 73 34`, "on [73]") and W2 (@268 `06 73 47`, "[73] ce") are
  verb-shaped by standing French grammar under standing grants (A15,
  A4); no nominal geometry exists at any of the six windows.
- **C3: MOOT** (antecedent fails). Recorded for the record: the selectional
  logic itself is SOUND — "croire [NP] [adjectif]" ✓ ("je le crois
  capable") vs "dire [NP] [adjectif]" ✗ (standard French requires
  "dire de [NP] qu'il est [adj]"). If the red team ever names 73 nominal,
  the asymmetry would land on this logic alone.
- **Resolve-arm: not met. Kill-arm: not met** (the conditional claim is
  vacated, not falsified — no window forces "if nominal then test" false,
  and no cleaner rival value for 73 was demonstrated). **Else-arm TAKEN:
  verdict NULL.**

## Fence (stated cause)

The @776 `[15] [33] [73] [37]` asymmetry is **antecedent-fenced**: 73 does
not resolve nominal at battery grade — its diagnostic windows are
verb-shaped (`84 73` "on [73]" @392, `73 47` "[73] ce" @268) — so the
croire/dire predicative-selectional test has no nominal NP to operate on.
The bar's grammaticality arm (C3) is intact and would land the asymmetry
immediately if 73 were ever named nominal; only the antecedent fails. The
frame re-opens iff the red team names 73 nominal (contingent re-run queued
below) or a battery names 73's verb value (verb-class battery queued below).

## Standing-verdict check

No standing verdict contradicted or downgraded: A15 (84="on") reinforced
as the load-bearing leg of W1; A4 (47="ce") reinforced via W2; A1 (37
predicative) untouched; A10 HOLD untouched; the parent's 21-fence confirmed
(this battery was its follow-up 2, and the 21-independent avenue is now
closed at the antecedent). §7 intact. No red-team contradiction, no
escalation.

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `val-73-verbclass` (P3) — name 73's verb class/value from the
   verb-shaped windows: cohort test on "on [X]" successor profiles across
   the stream (84→59 ×4 "on est" is the template cohort) plus the
   `66 73 41` ×2 / `66 73 34` trigram family. Bar: name a single value iff
   it parses all six 73 windows with zero contradiction; else fence the
   verb arm with the surviving candidate set.
2. `w73-66-trigram` (P4) — `66 73 41` ×2 (@1110/@1534) + `66 73 34`
   (@1347): if 66 resolves at battery grade (ne/se/y-shaped candidates),
   re-run the nominal-vs-verb screen on 73 with the trigram disambiguated.
   Bar: name 66 iff a single value parses its full window set; then re-test
   73's class.
3. `nom73-contingent-rerun` (P4) — contingent re-run of THIS battery's C3
   if the red team ever names 73 nominal: apply "croire [73] [37-pred]"
   vs "dire [73] [37-pred]" at @777. Bar: as written here ("land the
   asymmetry iff 73's named value yields a frame grammatical under exactly
   one candidate"); C3's selectional logic is pre-verified sound.
