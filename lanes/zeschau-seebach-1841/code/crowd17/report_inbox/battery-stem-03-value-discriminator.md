# Battery report: stem-03-value-discriminator

- Target id: `stem-03-value-discriminator`
- Claim: the @1320/@1594 '03 29' legs are genuine but value-nondiscriminating;
  test whether 24's finite/modal subclass selection at @1320 or a future 81
  value at @1594 constrains the stem
- Date: 2026-10-09
- Stream: repaired 1,847-pair / 96-type parse (code/side-keyhunt/repaired_offsets.json
  + data/upstream-ct_R5005.txt, parsed like code/side-keyhunt/repair_parse.py);
  asserts held (1,847 pairs, 96 types). All @-offsets are 0-based repaired-stream
  indices. Never used canonical.py. R5005, sealed gate instances, red-team
  adjudication queue untouched.
- Lock: code/crowd17/next-token/locks/stem-03-value-discriminator.lock
  (created 2026-10-09T20:12:34Z, agent id + timestamp; no prior lock; deleted
  on completion).

## Bar (verbatim, pre-registered before testing)

"name the stem value iff an independent standing constraint picks exactly one
-er stem with zero new assumptions; else fence value-naming at these legs"

Numbered clauses (restated before testing, not modified after):

1. **C1 (name):** an independent standing constraint picks exactly one -er stem
   for 03 at @1320/@1594 with zero new assumptions -> name the stem value
   (PROMOTE).
2. **C2 (fence):** otherwise -> fence value-naming at these legs (NULL).

## Method

1. Re-derived the repaired stream in-session (1,847 pairs / 96 types confirmed).
2. Byte-verified the two target windows and the "03 29 80" trigram census.
3. Tested Arm A: 24's finite/modal subclass selection at @1319-1321
   ("24 [03]er [80]").
4. Tested Arm B: 81's standing value at @1593-1595 ("81 [03]er [80]").
5. Checked registry standing (24=["verb","cls"], 03=["verb-stem","cls"],
   81 not registered) and the processed reports battery-stem-03-value (NULL),
   battery-24-en-verb-conflict (NULL, mutual kill at red team), and today's
   val-24-1132-name (NULL).

## Findings

### The two windows (re-derived, byte-exact)

- @1319-1321 (row a7_04): "...98 15 **[24] [03][29] [80]** 08 62 98 56 30"
  = "[24] [stem]er [80] ...". 24 is the immediate left neighbor of the
  '03 29' bigram at 0-based @1320-1321.
- @1593-1595 (row a8_02): "...47 08 **[81] [03][29] [80]** 67 77 81 82 98 00"
  = "[81] [stem]er [80] et le [81] m [98] pour". 81 is the immediate left
  neighbor at 0-based @1594-1595.
- "03 29 80" is a fixed trigram exactly 3x stream-wide (0-based @1030, @1320,
  @1594). The legs are genuine (adopted from battery-stem-03-value, verified
  in-session): 03 = verb-stem class (registry), 29='er' pencil ground truth.

### Arm A: 24's finite/modal subclass at @1320 — no discrimination

- Standing constraints: 24 = ["verb","cls"] (registry); R17-009 class-level
  GRANT "finite verb, modal-shaped". 24's VALUE is open: the en-vs-verb mutual
  kill is escalated to the red team (battery-24-en-verb-conflict, verdict/null);
  today's val-24-1132-name (verdict/null) narrowed the rival set to
  "savoir"/"vouloir" with no battery-grade discriminator ("dire" killed at
  @1132; "faire"/"laisser" dead globally; "pouvoir"/"devoir" killed conditional
  on uniformity).
- The class-level "modal-shaped finite verb" constraint is satisfied by EVERY
  -er stem: modal + bare infinitive admits any infinitive lexeme
  ("peut/doit/veut [V]er" with V = cesser, observer, remarquer, constater,
  declarer, signifier, notifier, publier, passer, porter, adresser, expedier,
  verifier, examiner, regler, payer, agreer, accepter, executer, ...). French
  modal and finite verbs governing bare infinitives select on the infinitive's
  argument structure, never on the stem's lexeme; no verb selects between -er
  stems at battery grade.
- Invoking any specific modal subclass value (vouloir/savoir/pouvoir/devoir)
  is a new assumption — barred by the bar itself ("zero new assumptions").
- Note: battery-stem-03-value's Clause 2 premised "24='faire' battery-promoted";
  that value is now dead (faire-dead globally, adopted from val-24-1132-name).
  This arm re-tests under the correct standing constraint (modal-shaped class)
  and still finds zero discrimination.
- Result: Arm A fails — no independent standing constraint from 24 picks
  exactly one -er stem.

### Arm B: a future 81 value at @1594 — no standing constraint exists

- 81 is NOT in the registry (no standing class or value). §7-standing kills
  hold: 81="prin" dead. 81's windows (n=14): "55 81" x6 (@26/@524/@551/
  @1086/@1095/@1670), "77 81" x4 (@745/@1241/@1402/@1599), plus @44 ("88 43 81"),
  @93 ("98 81"), @1513 ("39 81"), @1593 ("08 81") — class fully open.
- The claim's "a future 81 value" is hypothetical: there is no standing 81
  value to test, and positing one is a new assumption by definition.
- Even structurally, a word immediately before an infinitive ("ce [08] [81]
  [V]er") selects no stem lexeme under standing values.
- Result: Arm B fails — no independent standing constraint from 81 exists.

### Adverse honored

- Leg genuineness: adopted (claim grants; verified in-session, trigram x3).
- §7 intact: no polyvalence or conditioned split declared; 03's stem-vs-nominal
  split shape remains red-team venue (stem-03-nounfamily already verdict).
- No standing or red-team verdict contradicted or downgraded. No downgrade of
  the prior stem-03-value NULL (this battery is its named successor arm).

## Verdict: NULL (fence executed)

C1 fails on both arms (no independent standing constraint picks exactly one
-er stem with zero new assumptions); the bar's else-arm fires: value-naming
at @1320/@1594 is fenced. Not a kill: no window forces a specific value
false; the naming claim is unsatisfied, not falsified.

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `stem-03-24-vouloir-select` (P3) — if the red team ratifies 24='vouloir'
   (or another modal value), re-test whether vouloir's infinitive-complement
   semantics narrows the -er stem field at @1320. Gated on the red-team ruling.
2. `val-81-55-collocation` (P3) — name 81's class via the "55 81" x6
   collocation; a standing 81 class may constrain the @1594 left edge.
3. `stem-03-80-role-select` (P4) — resolve 80's role in the fixed "03 29 80"
   trigram; if 80 names as a governing verb with selectional restrictions,
   re-test stem discrimination.

## Bookkeeping

- Report: code/crowd17/report_inbox/battery-stem-03-value-discriminator.md
  (this file).
- battery-queue.json: `stem-03-value-discriminator` queued -> verdict/null
  (pre-write assert confirmed queued/verdictless; target-id-unique temp
  `battery-queue.json.stem-03-value-discriminator.tmp` + atomic rename; own
  entry only; no downgrade; disk re-validated; no tmp leftover).
- Lock created 2026-10-09T20:12:34Z (no prior lock), deleted on completion.
- R5005, sealed gates, red-team adjudication queue untouched. canonical.py
  never used; every number traces to the repaired stream.
