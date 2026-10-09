# Battery report: ce01-slot-1029-infinitive-avenue

- Target id: `ce01-slot-1029-infinitive-avenue`
- Claim: "replacement-role battery for 87@1028 under standing values WITHOUT the exclamatory-infinitive assumption"
- Date: 2026-10-09
- Worker: battery worker (subagent 21a7f9b7-de08-41b7-9661-88ef36b9e800)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py).
  Re-derived in-session: 1,847 pairs, 96 types confirmed. canonical.py never
  used. R5005, sealed gates, red-team queue untouched.
- Lock: code/crowd17/next-token/locks/ce01-slot-1029-infinitive-avenue.lock
  (created at start, deleted on completion; no prior lock for this id existed).

Terms (ASD-STE100): "exclamatory infinitive" = an infinitive used as an
exclamation ("Moi, me taire !" = "me, to shut up!"). "Tonic" = the stressed
form (moi, cela, ceci). "Clitic" = the unstressed form (me, ce). "Governor" =
the word that licenses the infinitive (a modal: "doit [03]er").

## Gate check (from the target's evidence field)

This target fires only if disloc-demonstrative-drama AND
disloc-demonstrative-reinforced both come back fenced. Confirmed:
- `disloc-demonstrative-drama`: verdict null (2026-10-09). The original run
  was a corpus gap (no drama in lane); the follow-up
  `disloc-demonstrative-drama-ingest` then ingested 1.57M characters of
  19th-century French drama (Hugo/Dumas/Vigny/Musset) and found zero
  attestations of dislocated-demonstrative + bare-exclamatory-infinitive.
- `disloc-demonstrative-reinforced`: verdict null (2026-10-09) — 0 genuine
  reinforced-head (celui-là/ceux-là/celle-là/...) + bare-exclamatory-infinitive
  attestations in 27.66M characters of 19th-century French.
The exclamatory-infinitive avenue is therefore closed on both fronts named
in the gate: bare-'ce' killed by ce87-topic-licensing (KILL), and the
tonic-demonstrative + bare-infinitive family fenced at prose- and
drama-register level. Gate FIRED; this battery proceeds.

## Bar (verbatim, pre-registered before testing)

"one grammatical 1841-French parse of @1028-1040, or fence the residual"

Numbered pass/fail clauses (restated before testing, not modified after):

1. Produce ONE grammatical 1841-French parse of @1028-1040 under standing
   values that does NOT use the exclamatory-infinitive assumption (neither
   the killed bare-'ce'-topic nor the fenced tonic-demonstrative topic
   heading a bare exclamatory infinitive).
2. If clause 1 fails: fence the residual with stated cause (which groups
   parse, which groups strand, and why every non-exclamatory role dies).

## Method

1. Read BATTERY-PROTOCOL.md first. Created/deleted the lock per protocol.
2. Re-derived the repaired stream in-session. Byte-verified the window:
   @1028-1040 = "87 01 03 29 80 77 11 70 82 34 29 40 17" (row a6_03);
   left context @1024-1027 = "45 64 96 43"; tail @1041-1043 = "77 82 63".
3. Adopted as premises (not re-litigated): 87='ce' (promoted), 29='er' (GT),
   11='la'/70='pre'/82='m'/34='i'/40='e' (GT), 17='fois' (promoted),
   77='le' (provisional), 03-29='[03]er' infinitive with 03 a verb stem
   (conditioned 03 split, battery-grade, imp-80-set), 80-77='[80]-le'
   imperative 80-stem + enclitic 'le' (poly-80-x29-frame C1, battery-grade),
   ce87-topic-licensing KILL (bare-'ce' topic dead), ce-inf-1841 KILL
   ('ce'+infinitive nominalization dead), ci-01-value KILL (01='ci' dead),
   edge-1024-clause-boundary KILL, ce01-slot-1029 NULL (01 'en'/'se'/boundary
   discrimination; candidate C killed), disloc-demonstrative-inf/reinforced
   NULLs (tonic-demonstrative + bare-infinitive family fenced).
4. Enumerated every non-exclamatory role for 87@1028 and every 01 value
   that could license the infinitive, and tested each against 1841 French
   grammar under standing values. No new corpus run was needed: the
   governing grammar rules are already positively established by the
   adopted kills (Littré/TLFi/Calvet & Chompret findings inside
   ce-inf-1841 and ce87-topic-licensing).

## Window-level evidence

### The window (byte-exact, repaired stream)

@1028-1040 (row a6_03): `87 01 03 29 80 77 11 70 82 34 29 40 17`
= "ce(87) [01] [03]er [80]-le(77) la(11) pre(70) m(82) i(34) er(29) e(40)
   fois(17)"

### The right half is forced and clean (no exclamatory infinitive involved)

@1032-1040 = "[80]-le, la première fois!" — imperative verb stem (80,
battery-grade verb class) + enclitic object 'le' (77, provisional) +
temporal adverbial "la première fois" (byte-anchored pencil crib: 11/70/
82/34/29/40 GT, 17=fois promoted). "Faites-le, la première fois !" is
fully grammatical 1841 French. The enclitic 'le' after the verb stem
forces the imperative reading (proclitic order "il le [80]" is excluded
by the byte order 80-77). This half parses with zero new assumptions and
does not depend on anything left of @1032.

### The left half: every non-exclamatory avenue dies

@1028-1031 = "87 01 03 29" = "ce [01] [03]er" must be a grammatical clause
(or attach to the imperative) with [03]er in a NON-exclamatory role. Each
avenue:

- **A. 01 = finite modal governing the infinitive** ("ce peut/doit [03]er"):
  DEAD. TLFi (via ce-inf-1841, finding 3): "ce" with verbs other than
  "être" is "rare... plus ou moins archaïque" even for the classical
  period — "ce" is not a live 1841 subject for lexical verbs. Independently,
  01 has no modal/finite-verb leg anywhere in its 28-window profile
  (ce01-slot-1029 census: 'en'/'se'/'ci'/'tain'/'fait'-syllable/boundary —
  never verb-shaped).
- **B. 01 = 'est' ("c'est [03]er")**: DEAD twice over. 01 has no 'est' leg
  (59='est' is provisional; 01's profile never shows it), and "c'est" +
  bare infinitive is ungrammatical anyway — the only licensed "c'est" +
  infinitive route is "c'est ... que de + inf." (TLFi, x27 corpus
  attestations per ce87-topic-licensing), which needs "que de", absent here.
- **C. 01 = preposition ("ce de/à/pour [03]er")**: DEAD. "ce" + preposition
  + infinitive has no grammatical frame ("*ce de changer"); 01≠00
  ('pour' is A9 leg-1 class-level on 00).
- **D. "ce" + infinitive nominalization** ("ce [01][03]er" as determiner +
  substantivized infinitive, or 01 elided): DEAD at kill grade —
  ce-inf-1841 KILL. Littré: the substantivized infinitive takes "le"
  ("Le boire est un infinitif employé comme substantif"); demonstrative +
  infinitive is Old French only (Buridant/Darmesteter).
- **E. 01 = 'se', non-dislocated ("ce se [03]er")**: DEAD. "ce" cannot be
  the subject of the lexical verb (avenue A kill), so "ce se [03]er" has
  no frame; the B-candidate's only grammatical route was the now-killed
  bare-'ce' dislocation (ce87-topic-licensing).
- **F. 01 = 'en', non-dislocated ("c'en [03]er")**: DEAD. No grammatical
  "c'en" + infinitive frame exists ("c'en est fait" needs "est fait";
  "s'en [inf]" needs the reflexive subject, not "ce"); the A-candidate's
  only route was the killed dislocation.
- **G. 01 = 'ne' ("ce ne [03]er")**: DEAD. 94 is the lane's 'ne' particle;
  bare "ne" + infinitive as a main clause is ungrammatical, and "ce" cannot
  be the subject anyway (avenue A).
- **H. Imperative governing a preceding infinitive** ("[03]er, [80]-le"
  as causative/complement): DEAD. French causative "faire" + infinitive
  requires "faire" BEFORE the infinitive; no construction puts a bare
  infinitive before its governing imperative.
- **I. 87 = determiner + nominal 01** ("ce [01-noun] [03]er"): DEAD. 01 has
  no nominal leg in 28 windows (Calvet & Chompret via ce-inf-1841: "ce"
  is "never immediately followed by a noun" in the pronominal reading;
  as a determiner it needs a noun 01 cannot supply), and [03]er would
  still dangle ungoverned.
- **J. 87-01 = "ceci" (tonic demonstrative)**: EXCLUDED by this target's
  bar — it is the exclamatory-infinitive avenue (skeleton-1032-revise's
  battery-grade parse "Ceci, [03]er! [80]-le, la première fois!"). Noted
  for the record: the avenue is additionally fenced at corpus level
  (disloc-demonstrative-inf/reinforced: 0 attestations in 27.66M prose
  characters; drama-ingest: 0 in 1.57M drama characters).
- **K. Bare-'ce' dislocated topic**: KILLED (ce87-topic-licensing) —
  clitics cannot be dislocated; zero attestations in 24.4M characters.
- **L. Clause boundary at 01's slot / 01 valueless**: KILLED
  (edge-1024-clause-boundary; ce01-slot-1029 candidate C).
- **M. "c'est ... que de" cleft**: DEAD — needs 59='est' adjacent plus
  "que de"; @1029=01, no "que de" present.
- **N. 01 = '-ci' bound** ("ceci" via bound morpheme): KILLED
  (ci-01-value); the surviving bound-'-ci' null (ci-bound-01) is the
  exclamatory-infinitive avenue, excluded by the bar.

No avenue survives. The enumeration is exhaustive over 87's standing-value
roles (subject / determiner / topic / fused compound / stranded) crossed
with 01's live values ('en' local, 'se' red-team-scoped, 'fait'-syllable
word-internal, open) and the infinitive's non-exclamatory governors
(modal / preposition / cleft / nominalization / imperative / fronting).

## Per-clause pass/fail

1. One grammatical 1841-French parse of @1028-1040 WITHOUT the
   exclamatory-infinitive assumption: **FAIL.** The right half
   (@1032-1040) parses cleanly as "[80]-le, la première fois!", but the
   left half (@1028-1031, "ce [01] [03]er") admits no grammatical
   non-exclamatory role for the infinitive: every governor (avenues A–I,
   M) is ungrammatical or valueless under standing values, and every
   topic/dislocation route (K–L, N) is killed, with J excluded by the bar.
2. Fence the residual with stated cause: **EXECUTED.** The residual is
   @1028-1031 "ce [01] [03]er": unparseable under standing values without
   the exclamatory-infinitive assumption. The fence is drawn exactly at
   the left half; @1032-1040 "[80]-le, la première fois!" stands as a
   clean imperative clause at battery grade (poly-80-x29-frame C1).
   Re-opening the residual needs a red-team act, not another battery
   avenue (see follow-ups).

## Adverses, answered

- None pre-registered on the target ("ADVERSES: None").
- Self-check — does this null contradict skeleton-1032-revise's PROMOTE
  ("Ceci, [03]er! [80]-le, la première fois!")? No. That promote is
  battery-grade (unratified) and explicitly USES the exclamatory-infinitive
  assumption; this battery tests the complement space WITHOUT it. The two
  results are consistent: with the assumption, the window parses; without
  it, the left half strands. §7 intact; no standing or red-team verdict
  touched or downgraded (Round 18 has zero mentions of @1028).
- Note: the task brief lists PRIORITY 2; battery-queue.json records
  priority 3 for this id. The queue's value is authoritative; no
  reprioritization was performed by this worker.

## Verdict: NULL (residual fenced per clause 2)

No grammatical 1841-French parse of @1028-1040 exists under standing
values once the exclamatory-infinitive assumption is removed. The window
splits into a stranded left half (@1028-1031 "ce [01] [03]er", fenced with
cause above) and a clean right half (@1032-1040 "[80]-le, la première
fois!", battery-grade imperative clause). Work regenerates via the
follow-ups below.

## Follow-ups (nulls regenerate work; all verified absent from the queue)

1. **01-verbclass-probe** (P3): the one avenue closed here on profile
   grounds rather than grammar grounds is A (01 as finite modal). Test 01
   for finite-verb/modal shape across its full 28-window profile
   (ce01-slot-1029's census never tested verb-ness). Bar: 0/28 verb-shaped
   kills the modal-governor avenue at kill grade and hardens this fence;
   ≥1 verb-shaped window re-opens @1029 with 01 as infinitive governor
   (subject to the TLFi "ce"+lexical-verb archaism constraint, which the
   red team would then need to adjudicate).
2. **stem-03-en-se-licensing** (P3, already queued — coordinate, do not
   duplicate): once 03's verb value is named, test whether it licenses any
   non-exclamatory frame at @1030 (e.g. a verb selecting a "ce"-headed
   complement). Bar: the named value either supplies the missing governor
   for @1028-1031 or the residual fence stands.
3. **Red-team escalation — @1028-1031 residual**: 87's role at @1028 and
   01's value at @1029 are now both fenced at battery level with no
   remaining battery-testable avenue (this battery closed the last one).
   Re-opening needs red-team acts: adjudication of 01's value, 03's
   noun-arm split, or 87's determiner arm with a nominal 01. Package this
   report's avenue-kill table (A–N) as the battery input.

## Bookkeeping

- Report: code/crowd17/report_inbox/battery-ce01-slot-1029-infinitive-avenue.md
  (this file).
- battery-queue.json: `ce01-slot-1029-infinitive-avenue` queued -> verdict/null
  via temp-file + rename (pre-write assert confirmed queued with null verdict
  field; JSON re-validated post-write; own entry only; claim/bars/evidence/
  adverses preserved).
- Lock created on start (agent id + UTC timestamp), deleted on completion.
- Stream re-derived in-session (1,847 pairs / 96 types); canonical.py never
  used; R5005, sealed gates, red-team queue untouched.
- Every number traces to the stream or the cited battery reports; no invented
  data. No standing verdict contradicted or downgraded.
