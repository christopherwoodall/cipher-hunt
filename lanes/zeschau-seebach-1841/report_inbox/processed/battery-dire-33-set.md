# Battery report — dire-33-set (33 = {dire, [X]er} 2-member set)

Worker: battery-worker-subagent-783d6363. Date: 2026-10-08.
Lock: `locks/dire-33-set.lock` created 2026-10-08T05:07:00Z, no prior lock existed.
Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`), parsed per `repair_parse.py`. `canonical.py`
not used. R5005 not touched. All counts re-derived in this run.

Coordination note: `erstem-33-id` is queued with no report on disk. This
battery ran the coherence + contact-profile work that bar (a) requires, and
left the deep naming of X to `erstem-33-id`. No duplication: no separate
valency battery was built here.

## Bar (verbatim, from battery-queue.json)

`resolve iff (a) the 5 stem windows cohere as ONE -er infinitive X (identify via contact profile); (b) all 20 whole-windows parse as 'dire'; (c) no window needs a third value (<=10% orphan)`

Numbered clauses (pre-registered BEFORE testing, not modified after):

1. (a) — the 5 stem windows (@273, @626, @1232, @1424, @1477) cohere as ONE
   -er infinitive X, and X is identified via its contact profile.
2. (b) — all 20 whole-windows parse as "dire".
3. (c) — no window needs a third value: orphan rate <= 10% (<= 2 of 25).

## Method

33 occurs 25 times in the stream. Successor census re-derived: 29 x5, 21 x3,
46 x2, 16 x2, 79 x2, 42 x2, 00 x2, 55/01/73/96/66/98/94 x1 — matches the
prior battery. The 5 stem windows are the five `33-29` bigrams
(@273/@626/@1232/@1424/@1477); the other 20 occurrences are whole-windows.
Verified frames: `67-33-29` x3 (@273/@1424/@1477), `33-29-87` x2
(@626/@1424), `00-33` x8, `67-33-46` x2 (@1451/@1624). The @1421-24 chain
`15-33-21-67-33-29-87` needs both members (whole "dire" at @1421, stem at
@1424) in one window.

Standing values used: 29="er", 82="m", 40="e", 12="n" (banked/promoted);
87="ce", 64="qui", 96="par", 46="que", 79="tout", 00="pour", 47="ce"
(allophone tier), 84="on" (A15), 94="ne" (promoted); 67 et/veut sole
polyvalence with the positional rule (67="veut" iff follower
infinitive-shaped). A10 (33+29 stem/whole HOLD) respected throughout.

## Clause (a) — stem coherence and X identification

Stem windows:

- @273 `47-11-06-67-33-29-89-84-91` = "veut [X]er [89], on [91]"
  (67="veut" by positional rule; 84="on").
- @626 `37-33-29-87-78` = "[37] [X]er ce [78]" (87="ce").
- @1232 `47-33-29-85-56` = "ce/se [X]er [85] [56]" (47="ce").
- @1424 `67-33-29-87-63` = "veut [X]er ce [63]".
- @1477 `67-33-29-82-16-98` = "veut [X]er m[16] [98]" (82="m").

Coherence evidence (all from the stream):

- All five share the byte-shape `33-29` with 29="er" (banked GT). The only
  alternative segmentations contradict granted values: `29-89-84` /
  `29-82-16` as "erreur" break 84="on" (A15) and 82="m" (GT) — dissolved in
  the prior battery; `33-29-87` as word-internal "erce…" breaks 87="ce"
  (promoted). The stem reading is forced, not chosen.
- Governor set {veut x3, ce/se x1, [37] x1}: all infinitive-selecting
  contexts, mutually compatible. Complement set {ce x2, [89] x1, [85] x1,
  m[16] x1}: all nominal/pronominal, compatible with one transitive -er verb.
- 33 is the corpus's top -er stem (5x; next 86/06 at 4x). Its contact
  profile is unique: the only stem with 47 as governor (besides 11, n=2)
  and the only stem with 87 ("ce") after -29 (besides one 84-29-87 window,
  @146 "l'on er ce", where no stem reading exists).
- Formulaic reuse: `33-29-87` byte-identical x2, `67-33-29` x3.
- X is valency-distinct from the 86 stem: 86-29 takes "pour" (00) x2 and
  never "ce"; 33-29 takes "ce" (87) x2 and never "pour".
- No window forces a second stem: no contradictory valency anywhere in
  the five.

Identification: NOT achieved. The contact profile narrows X to transitive
-er verbs governing "ce"-NPs under "vouloir" — a family
(donner / montrer / prouver / trouver / porter / envoyer / laisser /
prononcer …), not one verb. The discriminating complements are unreadable:
89 open, 16 open (frame-82-16 queued), 85 open (A3 frame only). "laisser"
is suggestive ("se laisser [85]" @1232 is idiomatic; "vouloir laisser" is a
top collocate) but "veut laisser me [16]" needs 16 = infinitive, which is
unproven. Naming X on this evidence would be a guess.

Clause (a): FAIL — coherence demonstrated, identification not achieved, and
the bar explicitly requires identification.

## Clause (b) — the 20 whole-windows as "dire"

- @24 `…29-47-33-55…` = "…er, se dire [55]" ✓ (47 allophone tier)
- @186 `00-33-16` = "pour dire [16]" ✓
- @265 `52-33-42` = "[52] dire [42]" ✓ (dire + direct object; 42/52 open)
- @408 `00-33-01` = "pour dire [01]" ✓
- @467 `96-00-33-79-80` = "par | pour dire tout [80]" ✓ (33="dire" after
  "pour"; 96 attaches left per the A14 set grant; 79-80 fenced below)
- @776 `15-33-73` = "[15] dire [73]" ✓ (dire + direct object)
- @846 `00-33-96-40-62` = "pour dire, par e[62]…" ✓ ("par exemple"-shaped;
  40="e" letter)
- @936 `00-33-21-64-37-01` = "pour dire [21], qui [37-01]" ✓ (byte-identical
  x2 with @1630; A12 unit)
- @1000 `96-82-33-00` = "…par(?) me dire pour [86]" ✓ ("me dire" = "tell me"
  parses; the 96 attachment is fenced, not 33)
- @1088 `00-33-79-80` = "pour dire tout [80]" ✓ (79-80 fenced)
- @1149 `67-33-66` = "veut dire [66], on…" ✓ (67="veut" positional)
- @1245 `00-33-16` = "pour dire [16]" ✓ (downstream "00-67-46" fenced, not 33)
- @1421 `15-33-21` = "[15] dire [21]" ✓ (chain with stem @1424)
- @1451 `67-33-46` = "veut dire que [92]" ✓ (F1 idiom)
- @1502 first 33: `74-84-33-42` = "…[74] on dire [42]" ✗ ORPHAN — 84="on" is
  granted (A15); "on" + infinitive is ungrammatical; no re-segmentation is
  available without breaking granted values or the A10 HOLD.
- @1504 second 33: `42-33-00-86` = "[42] dire | pour [86]…" ✓ (clause-final
  "dire"; "pour [86]" opens a new clause)
- @1624 `67-33-46` = "veut dire que [56]" ✓ (F1 idiom)
- @1630 = @936 ✓
- @1642 `12-33-98` = "…[56]n dire [98]" ✓ (12="n" letter; "dire" + object)
- @1700 `85-33-94-30` = "[85] dire ne [30]" ✗ ORPHAN — 94="ne" is promoted;
  "dire ne [30]" is ungrammatical order for negation; the "n'importe"
  rescue needs 30="importe" (fights the queued pas-30 lead) and the
  "contredire" rescue needs 85="contre" (fights A3's verb-stem frames).

18 of 20 parse cleanly as "dire". Fenced (not counted against 33): the
79-80 tail (@467/@1088), the 96 attachment (@1000), downstream of @1245.

Clause (b): FAIL as literally written (2 of 20 do not parse) — but inside
the orphan tolerance of clause (c).

## Clause (c) — orphan rate

Orphans: @1502-first-33, @1700 = 2 of 25 = 8% <= 10%. No window needs a
third value beyond the two fenced orphans.

Clause (c): PASS.

## Adverses disposition

- "croire ties dire on whole-frames": NOT ANSWERED. Every whole-window
  parse in (b) works identically for "croire" ("pour croire" x8,
  "veut croire que" x2, "me croire"). The tie stands; `croire-33-tiebreak`
  remains queued and still owns this question.
- "X unidentified": NOT ANSWERED (see (a)). `erstem-33-id` still owns it.
- "89/16 values open": still open (`frame-82-16` queued; 89 untouched).

## Verdict: null

The 2-member set is unfalsified — 18 whole-windows parse as "dire", the 5
stem windows cohere as one -er stem with a unique contact profile, orphans
sit at 8% inside tolerance — but clause (a) fails on identification and two
adverses stand unanswered, so this is inconclusive, not a promotion. Not a
kill: no window forces the set false and no cleaner rival is demonstrated
for either member. Consistent with A10 ("'dire' recorded as leading
partial, unpromoted") — no red-team contradiction, no escalation.

## Follow-ups (null regenerates work)

1. **x-33-laisser-test** — claim: X = "laisser". Bars: (i) 16 resolves as
   infinitive (via frame-82-16) so "veut laisser me [16-inf]" @1477 parses;
   (ii) 85 resolves as infinitive so "se laisser [85-inf]" @1232 parses;
   (iii) no stem window contradicts. Evidence: "vouloir laisser"
   collocation; "se laisser"+infinitive idiom; transitive "laisser ce [N]".
   Adverses: "donner"/"montrer"/"prononcer" rivals (if ver-78 lands
   "verdict", "prononcer ce verdict" beats "laisser"); pronoun-order strain
   at @1477. Coordinate with erstem-33-id — do not duplicate its battery.
2. **orphan-1502** — claim: @1501–1507 "74-84-33-42-33-00-86" parses under
   {dire, X} with at most one stated new assumption. Bars: resolve with the
   assumption named, or confirm as genuine orphan. Evidence: sole "84-33"
   bigram in the corpus; second 33 in the same window parses fine. Note:
   a third orphan anywhere in the set pushes 3/25 = 12% over tolerance and
   kills the set — this target guards that threshold.
3. **ne-30-1700** — claim: @1700 "85-33-94-30" = "[85] dire n'importe [20]"
   (30 = "importe", rival to queued pas-30). Bars: iff 30's value reconciles
   @559/@1716 (pas-30's ne-frames) with @1700 under one value; else fence
   @1700 as orphan and leave pas-30 standing. Evidence: "dire n'importe
   [quoi]" is a live French phrase; 94="ne" promoted. Adverses: pas-30's
   "n'est 30" frames need 30="pas"; "contredire" needs 85="contre" vs A3.
