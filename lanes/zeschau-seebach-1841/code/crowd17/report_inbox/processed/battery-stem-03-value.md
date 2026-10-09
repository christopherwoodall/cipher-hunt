# Battery report: stem-03-value

- Target id: `stem-03-value`
- Claim: name 03's verb-stem value using the three "[03]er" infinitives
- Date: 2026-10-09
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed like code/side-keyhunt/repair_parse.py).
  All @-offsets are 0-based repaired-stream indices. n(03)=20.
  Never used canonical.py. R5005, sealed gates, red-team queue untouched.
- Lock: code/crowd17/next-token/locks/stem-03-value.lock (created at start,
  deleted at end; no prior lock existed).

## Bar (verbatim, pre-registered before testing)

"name 03's stem value via the three "[03]er" infinitives (@1030/@1320/@1594),
constrained by causative "faire [03]er" @1322 and the "80-le" imperative at
@1032/@720"

Numbered pass/fail clauses (restated before testing, not modified after):

1. One stem value V is named such that "[V]er" parses grammatically (1841
   diplomatic French) at all three infinitive windows @1030, @1320, @1594.
2. The naming is consistent with the causative "faire [V]er" at @1319-1322
   (24='faire' battery-promoted).
3. The naming is consistent with the following "80-le" imperative frame at
   @1032 (and the @720-721 parallel).
4. Adverse honored: coordinates with (does not duplicate) queued `stem-03`
   (class bar) — this target names the VALUE, that one the class; no
   polyvalence declared at battery level (§7).

## Method

1. Re-derived the repaired stream in-session (1,847 pairs / 96 types confirmed).
2. Full census of 03 (n=20) with ±6 context; byte-verified the three
   "03 29" infinitives and their followers.
3. Tested candidate stems against all three windows with 1841 grammar;
   checked standing kills/constraints (§7).
4. Checked the "80-le" imperative constraint at @1032-1033 and @720-721.

## Findings

### The three infinitive windows (re-derived, glossed with standing values)

- @1030 (row a6_03): "87 01 03 29 80 77 11 70 82 34 29 40 17"
  = "ce [01] [03]er [80]-le la première fois [77] [82]"
  (87=ce granted, 29=er / 11=la / 70=pre / 82=m / 34=i / 40=e GT,
  17=fois promoted, 77=le provisional).
- @1320 (row a7_04): "15 24 03 29 80 08 62 98 56"
  = "[15] faire [03]er [80] [08] [62] [98] [56]"
  (24='faire' battery-promoted; "24 03 29" @1319-1321 is the stream's ONLY
  "faire + X + er" trigram — the causative frame is unique to 03).
- @1594 (row a8_02): "47 08 81 03 29 80 67 77 81 82 98 00"
  = "ce [08] [81] [03]er [80] et le [81] m [98] pour"
  (47=ce granted, 67=et positional rule).

"03 29 80" is a fixed trigram x3 (@1030/@1320/@1594); the only other
"X 29 80" in the stream is "92 29 80" @1154-1156 ("[92]er [80] fois",
det-80-1156-corrob: 92's verb value open).

### Clause 1: FAIL — the stem value is underdetermined

Dozens of -er verb stems parse all three windows grammatically because the
load-bearing neighbors are OPEN (01, 80, 15, 08, 81 all unvalued):

- "faire [V]er" admits: cesser, observer, remarquer, constater, déclarer,
  signifier, notifier, publier, passer, porter, adresser, expédier,
  vérifier, examiner, régler, payer, agréer, accepter, exécuter, and more.
- Window @1030 ("ce [01] [V]er! [80]-le, la première fois!") and @1594
  ("ce [08] [81] [V]er [80] et le...") admit any of the above with suitable
  (ungranted) values for 01/08/81/80. No banked or promoted neighbor forces
  a choice: the only fixed neighbors are 87/47=ce, 29=er, 11=la-première,
  17=fois, 77=le (provisional), 24=faire (battery), 67=et.
- A battery promote requires the value to be FORCED, not merely compatible.
  Nothing in the three windows selects one stem over the others.

### Clause 2: consistent but non-discriminating

"faire [03]er" @1319-1321 is byte-solid (unique causative trigram), and 03's
verb-stem class here is already established (imp-80-set). But causation is
compatible with every -er verb above; it does not name the stem.

### Clause 3: consistent but non-discriminating

"80-le" = imperative + enclitic 'le' at @1032-1033 and @720-721 (imp-80-set,
enclitic diagnostic n=2). Any exclamatory infinitive can precede an
imperative ("[V]er! [80]-le, la première fois!"); the frame constrains 80's
role, not 03's value. Note @720-721: 03 FOLLOWS "80-le" ("[02] [21]
[80]-le [03] [91]"), which favors a nominal/word reading of 03 there —
more §7 material, not a naming constraint.

### 03's full 20-window profile resists any monovalent stem (adverse context)

For the record (coordinates with queued `stem-03`, does not duplicate it):

- Verb-stem family: "[03]er" x3 (@1030/@1320/@1594), all followed by 80.
- Noun/word family: "[03] qui" x4 (@31/@336/@674/@1645), "pas [03]" x3
  (@31/@657/@994 — "24 (26) 30 03" frames), "ce [03]" x2 (@1014 "47 03 24",
  @1790 "47 03 00"), "[03] à" x3 (@599/@691/@1675 "03 39", 39=/a/ lead),
  "[03]e" x1 (@1237 "03 40"), "[03] pas" x1 (@1367 "03 30", 30=pas promoted).
- No single French lexeme was found that is simultaneously an -er verb stem
  fitting "faire [V]er" and a word fitting "pas [V]" / "[V] qui" / "ce [V]"
  (tested: manquer, douter, compter, honorer, marcher, jouer, oublier,
  payer, essayer, employer, envoyer, passer, porter, and others — each
  fails at least one family at battery grade). This is the §7 question in
  miniature; NOT declared here — escalated via follow-up, red team owns it.

## Verdict: NULL

Clause 1 fails: no stem value is forced by the three infinitive windows —
the open neighbors (01/80/08/81/15) admit dozens of grammatical -er verbs,
and no monovalent candidate covers 03's full profile. Clauses 2-3 are
consistent with the stem class but do not discriminate a value. Not a kill:
no window forces a specific value false; the claim is unsatisfied, not
falsified. No standing verdict contradicted or downgraded. No second
polyvalence declared (§7); the split-profile evidence is gathered below
for the red team.

## Follow-ups proposed (for supervisor queuing)

1. `stem-03-nounfamily` (P2) — test whether 03's non-infinitive windows
   ("pas [03]" x3, "[03] qui" x4, "ce [03]" x2, "[03] à" x3, "[03]e" @1237)
   converge on one noun/word value; if yes, package the stem-vs-noun split
   for red-team adjudication (conditioned split vs polyvalence).
2. `x29-80-collocation` (P2) — resolve the "[X]er [80]" collocation x4
   (03 x3 @1030/@1320/@1594, 92 x1 @1154); name 80's role in this frame.
   Naming 80 here constrains 03's stem through the shared "80-le"
   imperative link.
3. `faire-complement-field` (P3) — census "faire" complements stream-wide
   ("faire [03]er" x1, "faire [80]" x2, "faire [85]" x5, "faire ce" x10):
   build the semantic field of 24's infinitive objects to narrow 03's stem.

## Bookkeeping

- Report: code/crowd17/report_inbox/battery-stem-03-value.md (this file).
- battery-queue.json: `stem-03-value` queued → verdict/null (temp-file +
  rename, own entry only, pre-write assert confirmed no prior verdict;
  JSON re-validated after write).
- Lock created on start (agent id + UTC timestamp), deleted on completion.
- No standing verdict contradicted or downgraded. R5005, sealed gates,
  red-team queue untouched. canonical.py never used; every number
  re-derived on the repaired 1,847-pair stream.
