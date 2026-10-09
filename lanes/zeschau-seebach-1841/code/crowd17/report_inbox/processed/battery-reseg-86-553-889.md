# Battery verdict: reseg-86-553-889 — re-segmentation of the two 86 violators

Date: 2026-10-08. Worker: f76ac9f0-9308-48c4-ae5b-e0e330f26f19 (battery worker).
Lock: code/crowd17/next-token/locks/reseg-86-553-889.lock (created 2026-10-09T02:19:53Z; no prior lock; deleted on completion).
Target id: reseg-86-553-889. Queue status at take: queued, priority 2.
Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
data/upstream-ct_R5005.txt, parsed like code/side-keyhunt/repair_parse.py).
canonical.py never used. R5005, sealed gate instances, red-team adjudication
queue untouched. No data invented. @-offsets are 0-based stream indices.

## Bar (pre-registered verbatim from battery-queue.json, BEFORE testing)

"for each window, kill the standalone-word assumption iff a cleaner multi-group word parse is demonstrated on bytes; if 86 goes word-internal, name the host word"

Listed adverses: none stated.

### Numbered clauses (operative, pre-registered)

1. @553 ("00 86 59 34", row a3_01): kill the standalone-word assumption for
   86 iff a cleaner multi-group word parse is demonstrated on bytes; if 86
   goes word-internal, name the host word.
2. @889 ("00 86 06 77", row a5_08): kill the standalone-word assumption for
   86 iff a cleaner multi-group word parse is demonstrated on bytes; if 86
   goes word-internal, name the host word.

## Method

1. Re-parsed the repaired stream per code/side-keyhunt/repair_parse.py;
   extracted ±10-group windows at @553 and @889 with row ids and raw bytes.
2. Banked values used (protocol §7): pencil 11=la, 70=pre, 82=m, 34=i,
   29=er, 40=e, 46=que; granted 87=ce, 64=qui, 96=par, 17=fois, 79=tout,
   00=pour, 84=on, 47=ce; battery-promoted (caveated, pending ratification)
   12=n, 48=e, 30=pas, 06=ent, 94=ne; provisional 59=est, 77=le.
3. For each window, attempted word-internal parses for 86 in both
   directions (86 + right neighbor as one word; 86 + left neighbor as one
   word), requiring: (a) the host word is real 1841 French, (b) every
   group in the host word is assigned (no unparsed residue inside the
   word), (c) the resulting clause is grammatical, (d) 86's inferred
   syllable is consistent with its independently established frames.
4. Checked the candidate against the standing red-team fence of @889
   (code/crowd5/redteam/rulings.md; code/crowd5/morph47_06.md) for
   contradiction per protocol §5.2. Did not touch the red-team queue.

## Window-level evidence

### @553 (row a3_01, offset 0; raw "…4655810086593417862…")

Full local parse (±10):
`[543]42 [544]06=ent [545]00=pour [546]46=que [547]24 [548]47=ce [549]46=que
[550]55 [551]81 [552]00=pour [553]86 [554]59=*est [555]34=i [556]17=fois
[557]86 [558]94=?ne [559]59=*est [560]30=pas [561]67 [562]11=la [563]43`

= "…que 24 ce que 55 81 pour [86] est-i fois [86] n'est pas et/veut la [43]…"
(row continues into a3_02: "94 59 30" = the stream's only "n'est pas"
trigram, per battery-est-59-frames).

Distributional facts (re-derived): "86→59" is hapax (@553 only); "59→34"
is hapax (@554 only); "34→17" is hapax (@555 only). 34 (n=11) takes 29
("er") as successor x3 — consistent with pencil 34="i" as a letter
("…i-er…", cf. "premiere" = 11 70 82 34 29 40).

Re-segmentation attempts (all fail to demonstrate):

- (a) "86 59 34" = X + "est" + "i" as one word ("esti…" host): every
  French "esti" word fails on the byte continuation — "estime/estimer"
  need 82 ("m") at [556], have 17 ("fois"); "estival", "pestiféré",
  "digestif", "investir", "festival", "bestial" all need non-"fois"
  continuations or contradict 59="est". No host word demonstrable.
- (b) "86 59" = X + "est" word-final ("…reste/peste/geste/manifest…"):
  none yields a grammatical "pour [X-est] i fois" clause; "34=i" left
  dangling in every attempt.
- (c) "00 86" = one word ("pourquoi"/"pourtant"/"pourvoir"): "00 86"
  takes followers {59, 50, 48, 70, 06, 56×4, 52, 29×2} across its 12
  windows — "pourquoi-er" (@1375/@1825 "00 86 29") and "pourtant-er" are
  not words, killing the single-word reading globally; per-window at
  @553, "pourquoi/pourtant est-i fois" leaves "est-i" unparsed.
- (d) 86 = "voi" (see @889 finding): "pour voir est-i fois" — "pour
  voir" parses, but "est-i" (59="est" provisional + 34="i") admits no
  grammatical continuation ("est-il" needs "l"; "est" + "y" needs a
  verb; "est" + "une fois" contradicts pencil 34="i").
- (e) Digit-level phase shift on row a3_01: no crib or gloss anchors a
  phase change on this row; rejected as undemonstrable (canonicality
  caveat noted, not litigated).

Result: no cleaner multi-group word parse demonstrated. The
standalone-word assumption for 86 at @553 is NOT killed. The window
remains a genuine residual ("pour [86] est-i fois"); the defect
localizes to "59 34" ("est-i"), not to 86's wordhood.

### @889 (row a5_08, offset 1)

Full local parse (±10):
`[879]08 [880]31 [881]79=tout [882]68 [883]37 [884]03 [885]02 [886]00=pour
[887]… wait — stream indices: [886]03 [887]02 [888]00=pour [889]86
[890]06=ent [891]77=*le [892]76 [893]01 [894]98 [895]82=m [896]14 [897]98
[898]83 [899]86 …`

= "…tout 68 37 03 02 pour [86] ent le [76] 01 98 m 14 98 83 86…"

Distributional fact (re-derived): "86→06" is hapax (@889 only), confirming
the red-team observation.

**Demonstrated parse: "00 86 06" = "pourvoient" (3rd plural present of
"pourvoir", to provide/supply).**

- Spelling: "pourvoient" = p-o-u-r-v-o-i-e-n-t = 00 ("pour", A9 granted)
  + 86 ("voi") + 06 ("ent", battery-promoted). Every group assigned, no
  residue.
- 86 = "voi" is independently grounded: 86→29 ×4 (@431, @1375, @1391,
  @1825) reads "voir" in all four — "pour voir" ×2 ("in order to see"),
  "veut voir" (@1391; 67="veut" by the positional rule since "86 29" is
  infinitive-shaped), "le voir" (@431, substantivized infinitive). The
  same stem "voi" composes with "er" (86-29) and with "pour…ent"
  (00-86-06). Two independent compositions, one stem value.
- Clause: "…03 02 pourvoient le [76]…" = "…[03] [02] provide (3pl) the
  [76]…" — fully grammatical; "pourvoir" v.t. = to supply/fill
  (diplomatic register: "pourvoir [un poste]"). Subject "03 02"
  (unvalued NP) precedes; "le [76]" (77="le" provisional) is the direct
  object.
- Precedent for a granted group as word-internal prefix: 70="pre" in
  "premiere" (11 70 82 34 29 40, pencil gloss). "pour" as verbal prefix
  in "pourvoir" is the same mechanism — no re-valuing of 00, no §7
  polyvalence issue (same spelling "pour").
- Rival parses lose: "pour [86] [06]" as three words = "pour voir
  [verb-ent]" ("pour" + finite verb — ungrammatical); "pour [86=le?]
  [06]" = "pour le [verb]" — ungrammatical; elision "l'ent…" needs
  "remise/… " after 06, contradicted by 77="le" (cf. battery-stem-86).
  "pourvoient" is the unique grammatical parse.

Result: cleaner multi-group word parse DEMONSTRATED on bytes. 86 goes
word-internal; host word = **"pourvoient"**. The standalone-word
assumption for 86 at @889 is KILLED per the bar.

**Red-team contradiction (§5.2):** code/crowd5/redteam/rulings.md and
code/crowd5/morph47_06.md fence @889 as clause-boundary ("00 86 | 06 77").
The "pourvoient" parse says "00 86 06" is ONE word — no clause boundary
exists. This contradicts the standing red-team fence on mechanism. It
does NOT contradict M1's material conclusion: M1 excluded @889 as a
falsifier, and under "pourvoient" there is no "86→06" word-bigram at all,
so M1's falsifier-exclusion holds a fortiori. The contradiction is
flagged, not overwritten; adjudication is escalated to the red team.

## Per-clause pass/fail

1. **@553: NOT DEMONSTRATED (standalone-word assumption stands).** Five
   re-segmentation families attempted on bytes (esti-host, -est-final,
   00+86 single word, 86="voi" composition, digit phase shift); all fail
   on continuation bytes or global distribution. The window's defect
   ("est-i") is orthogonal to 86's wordhood.
2. **@889: DEMONSTRATED — host word "pourvoient" named; standalone-word
   assumption killed per the bar.** 86 = "voi" word-internal, composed as
   "pour"+"voi"+"ent"; independently consistent with 86-29 = "voir" ×4.
   **CONTRADICTS the standing red-team clause-boundary fence** — flagged
   per §5.2, not overwritten.

## Verdict: NULL

Per protocol §5.2, the @889 finding contradicts a standing red-team fence
("00 86 | 06 77" clause-boundary), so the target result is marked NULL
with the contradiction as the headline, escalated to the red team. This
is not a "nothing found" null: clause 2's bar condition (cleaner
multi-group word parse demonstrated, host word named) is met at battery
level — "pourvoient" — and the distributional consequence (no "86→06"
word-bigram exists; M1's falsifier-exclusion strengthened) is recorded
for adjudication. Clause 1 (@553) is a clean negative: no re-segmentation
demonstrable; standalone-word assumption stands; residual fenced to the
"59 34" ("est-i") locus.

## Follow-up targets (null regenerates work)

1. `redteam-889-pourvoient` (priority 1): red-team adjudication of the
   "pourvoient" parse (00="pour" + 86="voi" + 06="ent") against the
   standing clause-boundary fence of @889. Bar: adjudicate mechanism
   (one word vs clause boundary); M1's falsifier-exclusion is preserved
   either way — state which mechanism the bytes support. Escalation, not
   a battery decision.
2. `voir-86-sweep` (priority 2): global test of 86 = "voi" (stem of
   "voir"). Predicts: "pour voir" ×2 (@1375, @1825), "veut voir" (@1391),
   "le voir" (@431), "la voir" (@671: "11 86 24" = "to see her/it [24]"),
   "pourvoient" (@889). Bar: promote 86="voi" iff all 32 windows parse
   with "voi"/"voir"/"pourvoir"-family compositions and zero hard
   contradictions; kill iff any window forces otherwise. (Coordinates
   with split-86-amended-rule; does not duplicate it — this names a
   value, that tests the rule.)
3. `reseg-553-retry` (priority 3): @553 residual "59 34" ("est-i") with
   86="voi" ("pour voir est-i fois"). Narrower bar: demonstrate a parse
   of "59 34" as "est"+"i"/"est"+"y" with grammatical continuation, or
   fence "59 34 17" as a genuine residual with stated cause. Does not
   re-litigate 86's wordhood at @553.

## Constraints compliance

- Tested only on the repaired 1,847-pair stream (repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed like repair_parse.py). canonical.py
  never touched. R5005 never touched. No data invented; every number
  re-derived above.
- Sealed gate instances and the red-team adjudication queue untouched
  (red-team documents read, not modified).
- No standing verdict downgraded or overwritten; the @889 contradiction
  is flagged per §5.2 with this null verdict.
- 86 polyvalence NOT declared. 86="voi" is a battery-level inference
  (two independent compositions), not a promotion; value promotion is
  the red team's act.
- Sibling target split-86-amended-rule noted as running in parallel; not
  blocked on, not duplicated (this target names the "pourvoient" word;
  that target tests the amended positional rule).
