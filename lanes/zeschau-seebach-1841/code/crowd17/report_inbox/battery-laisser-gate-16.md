# Battery report — laisser-gate-16 (16's class adjudication; laisser lead re-test)

Worker: battery-worker-laisser-gate-16 (subagent bb39fbc4). Date: 2026-10-09.
Lock: `code/crowd17/next-token/locks/laisser-gate-16.lock` created 2026-10-09T04:24:25Z;
no prior lock existed; deleted on completion.
Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`), parsed per `code/side-keyhunt/repair_parse.py`
(replicated in-worker, not `canonical.py`). R5005 not touched. Every count
below re-derived from the stream in this run. No observed values redacted.

## Bar (pre-registered verbatim, from battery-queue.json)

`(a) 16's class named with all 28 windows parsing; (b) the '62-16' x4 / '12-16' x3
finite-verb signals vs '16-00' x4 noun signals adjudicated without lane-illegal
polyvalence (§7); (c) @1480 parses as '[X]er me [inf]' with zero contradiction`

Adverses (queue): `62='on' is lead-grade only (collision-62-84 verdict); 16's
class is frame-82-16's lane — coordinate`

## Numbered clauses (pre-registered BEFORE testing, not modified after)

1. 16's class is named with all 28 windows parsing.
2. The '62-16' x4 / '12-16' x3 finite-verb signals vs '16-00' x4 noun signals are
   adjudicated without lane-illegal polyvalence (§7).
3. @1480 (1-based) parses as '[X]er me [inf]' with zero contradiction.

## Method

Independently re-derived the full 16 census on the repaired stream (assert
1,847 pairs; assert 96 types; n(16)=28 confirmed, byte-identical windows to
frame-82-16's census): predecessors 62 x4, 12 x3, 82 x11, 33 x2, 42 x2,
65/32/49/86/67/89 x1; successors 00 x4, 91 x2, 76 x2, 24 x2, 01 x2, singletons
14/56/52/78/08/77/92/88/29/96/64/02/06/97/98/59.
Spot-tested the doubled frame @1195–1198 and @1480 under each candidate class
(noun, infinitive, finite verb). Coordinated with frame-82-16 (null,
2026-10-09): its eliminations ("même"/"mais"/noun/infinitive kills) and its
finite-verb lead were adopted as prior evidence, not re-litigated; its
contradiction headline was re-verified against the queue rather than assumed.
Tested only against the repaired stream; 1841 diplomatic French only.

## Window-level evidence

### Clause 1 (class named, all 28 parsing): FAIL — two independent blockers

Blocker A — the doubled frame is a universal killer. @1195–1198 (1-based,
row a7_00): `82 16 96 82 16 64` = "m'[16] par m'[16] qui". Tested under every
candidate class: noun ("m'[noun] par m'[noun] qui" — "m'" + noun
ungrammatical), infinitive ("m'aimer par m'aimer qui" — ungrammatical),
finite verb ("m'a par m'a qui" — ungrammatical), pronoun, adverb. All fail.
Independently confirms frame-82-16's finding: no class parses all 28.

Blocker B — the standing battery promote. gate-satisfiability-16-85
(verdict/promote, 2026-10-08) assigned 16=infinitive as the single-class
assignment under which every banked frame parses. Naming the finite-verb class
(which fits 24/28 of my census) would overwrite that verdict; protocol §5
forbids overwriting a standing verdict at battery level. The contradiction is
headlined below for the red team, not resolved here.

### Clause 2 (signal adjudication under §7): done at frame level; resolves no class

- 62-16 x4 (@84, @660, @1143, @1299): 62="on" is lead-grade only per
  collision-62-84, NOT granted. "on/il [infinitive]" is ungrammatical IF 62 is
  a subject pronoun — but that premise is lead-tier, so the frame is tiered,
  not a banked contradiction. This is the genuine tier dispute between the two
  batteries, not a battery-decidable fact.
- 12-16 x3 (@243, @845, @1432): 12="n" is banked GT. "n'[16]" as literary
  negation selects a finite verb; no grammatical infinitive reading of
  "n'[infinitive]" exists at any of the three windows (no "pas" present).
- 16-00 x4 (@188, @660, @845, @1247): under the finite-verb lead this is
  "a/est pour" ("avoir/être pour" — grammatical), answering the queue's
  noun-signal framing; the noun shape bites only under the killed noun/infinitive
  readings.
No polyvalence declared (§7 intact). The adjudication does not resolve to a
namable class because of clause 1's blockers.

### Clause 3 (@1480 as '[X]er me [inf]', zero contradiction): FAIL

@1480 (1-based, row a7_10): `29 82 16 98 62` = "er m[16] [98] [62]",
in "67 33 29 82 16 98" = "veut [X]er m[16] [98]".
- Under finite-16: "veut [X]er m'a [98=vient]" — "m'a vient" is
  ungrammatical; requires an unevidenced clause boundary between 16 and 98.
- Under infinitive-16: "veut [X]er m'aimer [98=vient]" — likewise
  ungrammatical with no byte-evidenced boundary.
Zero contradiction is unachievable under either assignment at battery grade.

## Adverses disposition

- "62='on' is lead-grade only (collision-62-84 verdict)": HONORED — the 62-16
  x4 frames are tiered as lead-grade evidence, not banked contradictions, in
  the clause-2 adjudication.
- "16's class is frame-82-16's lane — coordinate": COORDINATED — its census
  (byte-identical), eliminations, and contradiction headline adopted; this
  battery added the independent doubled-frame spot-test, the @1480 clause-3
  test, and the §5 standing-verdict check. Nothing duplicated, nothing
  re-litigated.

## CONTRADICTION HEADLINE (per §5, escalated not overwritten)

This battery's class-lead evidence (finite verb, vowel-initial "a"/"est" via
m'/n' elision, fits 24/28 census windows, answers the 16-00 adverse)
contradicts battery verdict gate-satisfiability-16-85 (promote, 2026-10-08),
which assigned 16=infinitive with the infinitive gates "satisfiable at all".
The crux is the tiering of the 62-16 x4 frames (lead-grade subject pronoun vs
banked infinitive assignment) plus the doubled frame, which neither battery's
class assignment parses. Red-team adjudication should take both reports
together; no red-team verdict on 16 exists; the registry has no 16 cell.
The laisser lead ('laisser' at LEAD strength per x-33-laisser-test) remains
gated on this decision — clause 3's failure means the '[X]er me [inf]' arm
cannot proceed at battery grade either.

## Verdict: NULL

16's class cannot be named at battery grade: the doubled frame defeats every
class, and the finite-verb lead contradicts a standing battery promote that
§5 forbids overwriting. Nothing contradicted or downgraded; §7 intact;
`canonical.py` never used; R5005, sealed gates, red-team queue untouched.

## Follow-ups proposed (all verified absent from battery-queue.json)

1. `doubled-1195-offset-audit` (P2): verify row a7_00's offset/pairing around
   @1195–1202 (canonicality caveat: 68 of 70 upstream row offsets unvalidated).
   A mispaired row dissolves the doubled frame and makes clause 1 testable.
2. `val-16-a-vs-est` (P2): discriminate 16="a" vs 16="est" on the 26
   non-doubled windows (keys: 16-91 x2, 16-76 x2, @877/@1833 residuals).
3. `class-62-16-windows` (P3): test 62's class at the four 62-16 windows
   (@84/@660/@1143/@1299). If 62 is non-pronominal there, the finite-verb
   lead weakens and the gate battery's infinitive assignment strengthens.
