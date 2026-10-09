# Battery report: ce01-slot-1029

- Target id: `ce01-slot-1029`
- Claim: "Discriminate 01's value at @1029 ('c'en' vs 'ce se' vs clause-boundary) against 01's full 28-window profile, closing the last open slot of the @1032 clause."
- Date: 2026-10-09
- Worker: battery worker (subagent b2f93943-5539-4025-a8a8-66d6c81b2f10)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py).
  Re-derived in-session: 1,847 pairs, 96 types. All @-offsets are 0-based
  repaired-stream indices. n(01) = 28, confirmed. Never used canonical.py.
  R5005, sealed gates, red-team queue untouched.
- Lock: code/crowd17/next-token/locks/ce01-slot-1029.lock (created at start,
  deleted on completion; no prior lock for this id existed).

## Bar (verbatim, pre-registered before testing)

"discriminate 01's value at @1029 ('c'en' vs 'ce se' vs clause-boundary)
against 01's full 28-window profile; 'ci' killed, 'en'/'tain' local
elsewhere. Closes the last open slot of the @1032 clause."

Numbered pass/fail clauses (restated before testing, not modified after):

1. One of the three candidates ('c'en' = 01='en'; 'ce se' = 01='se';
   clause-boundary = 01 valueless with a boundary at its slot) yields a
   grammatical 1841-French parse of "ce [01] [03]er [80]-le, la premiere
   fois" under standing values, and the other two are decided (killed or
   disfavored with stated cause).
2. The surviving candidate is consistent with 01's full 28-window profile:
   no window forces it false; standing locality holds ('en' local to the
   three 01-24 windows per disc-01-24-ci-X; 'ci'/'faisant' killed per
   ci-01-value; 'se' killed only at 01-24 per the brief).
3. Every listed adverse is answered (see Adverses).
4. A cleaner rival value demonstrated on the same frames kills the claim
   (protocol section 4).

## Method

1. Read BATTERY-PROTOCOL.md first. Created/deleted the lock per protocol.
2. Re-derived the repaired stream in-session (1,847 pairs / 96 types).
   Byte-verified the clause: seq[1028]='87', seq[1029]='01',
   @1028-1040 = "87 01 03 29 80 77 11 70 82 34 29 40 17" (13 groups).
   ERRATUM on the brief: the evidence field says "@1028-1038" but lists
   all 13 groups; the true span is @1028-1040. All offsets below use the
   verified span.
3. Enumerated all 28 windows of 01 with +-6 context (census in evidence).
4. Tested each candidate against 1841 French grammar under standing
   values: 87='ce' (granted), 29='er' (GT), 11='la'/70='pre'/82='m'/
   34='i'/40='e' (GT), 17='fois' (promoted), 77='le' (provisional),
   03-29='[03]er' infinitive with 03 a verb stem (imp-80-set),
   80-77='[80]-le' imperative + enclitic (imp-80-set lead).
5. Checked every standing verdict that touches 01 or this clause
   (ci-01-value KILL, disc-01-24-ci-X PROMOTE, ce-inf-1841 KILL,
   rival-37-01-certain KILL, wordinternal-37-01 PROMOTE,
   faisant-absolute-01 KILL, imp-80-set NULL, ci-bound-01 NULL,
   edge-1024-clause-boundary KILL, clause-boundary-precedent KILL).
   None is contradicted or downgraded.

## Window-level evidence

### The target window (byte-exact, repaired stream)

@1024-1042 (row a6_03):
`45 64 96 43 87 01 03 29 80 77 11 70 82 34 29 40 17 77 82`
= "ce(45) qui(64) par(96) [43] ce(87) [01] [03]er [80]-le(77)
   la(11) pre(70) m(82) i(34) er(29) e(40) fois(17) le(77) m(82)"

Working skeleton (imp-80-set, battery-grade lead, adopted not
re-litigated): "ce [01] - [03]er! [80]-le, la premiere fois!"
(exclamatory infinitive + imperative with enclitic 'le').

### 01's 28-window census (0-based @, +-6 context)

- @34 (a1_00): `34 24 30 03 64 32 >>01<< 08 91 39 64 41 01`
- @40 (a1_01): `01 08 91 39 64 41 >>01<< 24 88 43 81 30 62` ('en' local)
- @195 (a2_00): `66 24 87 98 56 47 >>01<< 21 60 08 67 76 87` (ce-context)
- @255 (a2_02): `44 94 65 63 00 66 >>01<< 91 32 43 77 84 74`
- @295 (a2_03): `09 64 29 40 65 16 >>01<< 11 78 40 97 86 91`
- @327 (a2_05): `92 60 15 63 71 10 >>01<< 19 00 92 50 45 54`
- @345 (a2_05): `14 45 64 96 43 87 >>01<< 06 70 12 94 74 67` (ce-context)
- @409 (a2_08): `53 34 69 26 00 33 >>01<< 02 53 84 51 37 78`
- @484 (a2_11): `45 93 00 13 52 30 >>01<< 19 64 76 42 41 20`
- @596 (a4_00): `41 09 00 92 79 85 >>01<< 29 40 03 39 26 96` ('-cier' lead)
- @717 (a5_01): `71 12 63 00 66 86 >>01<< 02 21 80 77 03 91`
- @828 (a5_06): `13 24 87 59 38 82 >>01<< 24 87 11 77 76 59` ('en' local)
- @893 (a5_08): `02 00 86 06 77 76 >>01<< 98 82 14 98 83 86`
- @940 (a5_10): `26 00 33 21 64 37 >>01<< 07 50 40 08 62 98` (37-01 unit)
- @949 (a6_00): `40 08 62 98 96 86 >>01<< 77 86 96 87 46 24`
- @970 (a6_00): `41 19 24 06 77 76 >>01<< 98 48 51 45 08 01`
- @976 (a6_01): `01 98 48 51 45 08 >>01<< 00 92 07 76 47 78`
- @984 (a6_01): `92 07 76 47 78 45 >>01<< 24 89 48 01 76 49` ('en' local)
- @988 (a6_01): `78 45 01 24 89 48 >>01<< 76 49 24 26 30 03`
- @1029 (a6_03): `64 45 64 96 43 87 >>01<< 03 29 80 77 11 70` (TARGET)
- @1255 (a7_02): `46 26 30 06 65 46 >>01<< 61 31 29 69 88 01`
- @1261 (a7_02): `01 61 31 29 69 88 >>01<< 09 11 50 46 69 88`
- @1440 (a7_08): `64 52 82 16 24 85 >>01<< 52 68 59 37 64 77`
- @1462 (a7_09): `21 67 86 66 79 17 >>01<< 21 62 48 21 02 62`
- @1634 (a8_03): `26 00 33 21 64 37 >>01<< 74 87 74 74 35 56` (37-01 unit)
- @1653 (a8_04): `31 10 03 38 82 16 >>01<< 56 37 11 24 48 47`
- @1731 (a8_07): `98 39 88 24 30 15 >>01<< 56 30 06 60 12 48`
- @1818 (a8_10): `93 50 42 06 29 37 >>01<< 02 09 19 00 97 00` (37-01 unit)

Profile notes: 01 never row-initial (0/28); 21 distinct predecessors
(promiscuous, token-like, not marker-like); successors show no
clause-initial enrichment (00 x1, 46 x0, 94 x0 after 01).

### Candidate A: 'c'en' (01='en') -> "Ce, en [03]er! [80]-le, ..."

- Parse: left-dislocation + exclamatory infinitive. Topic "ce",
  comment "en [03]er!" with partitive "en" resuming the topic
  ("this: to [03] of it!"), then imperative "[80]-le", adverbial
  "la premiere fois". Shape parallels "Moi, en parler!" /
  "Eux, en profiter!" (exclamatory infinitive with proclitic "en"
  is grammatical).
- Strain (stated, sub-kill-grade): the topic is bare "ce", an
  unstressed clitic; dislocation topics and exclamatory subjects
  are normally tonic ("cela/moi"). The strain is shared with B
  and lacks period-corpus backing at kill grade (cf. ce-inf-1841's
  standard). Not kill-grade.
- Profile support (three legs):
  (a) 'en' is an established 01 value: promoted local to the three
      01-24 windows (disc-01-24-ci-X, battery-level).
  (b) Elision precedent: "ce en" -> "c'en" matches "m'en" @828
      ("82-01-24" = "m' en fait"), where the lane already accepts
      invisible elision before vowel-initial 01='en'.
  (c) Second "ce en" leg: @984's promoted parse is "ce(45) en(01)
      fait(24) [89]" -- the "ce en" bigram already parses cleanly
      at a second window.
- Blockers (why A cannot promote at battery level):
  (a) Hard constraint: the brief lists "01='en' local to the three
      01-24 windows" as a standing constraint; a fourth 'en' window
      revises disc-01-24-ci-X's scope.
  (b) Section 7: bound '-ci' is live (null, not killed) at @1029;
      naming 01='en' there risks a second polyvalence ('en'/'-ci').
      disc-01-24-ci-X consequence 5 flags exactly this unification
      as RED-TEAM-ONLY. Not declared here.

### Candidate B: 'ce se' (01='se') -> "Ce, se [03]er! [80]-le, ..."

- Parse: same dislocation + exclamatory infinitive, reflexive
  resumption: "Ce, se [03]er!" parallels "Moi, me taire!" /
  "Lui, se lever!" ("se" = accusative subject of the infinitive,
  coindexed with topic "ce": "this: to [03] itself!").
- Same bare-"ce" strain as A (shared, sub-kill-grade).
- 'se' is killed only at 01-24 (brief's adverse; the kill sits at
  @828 at kill grade: "m' se" cannot stack two object clitics;
  @40/@984 admit "se" grammatically but 'en' was promoted there).
  @1029 is outside that kill's scope.
- Disfavored vs A on profile (three counts):
  (a) 'se' is unattested for 01 anywhere in the 28-window profile;
      'en' has three promoted legs.
  (b) No phonological precedent: "ce se" has no elision parallel
      to "m'en"/"c'en".
  (c) No second "ce se" leg: @984's "ce se fait" is inside the
      01-24 'se'-kill scope; @345 "ce se [06-ent]" and @195
      "ce se [21]" do not parse.
- Red-team scope: the brief's adverse states conditioned 'ce se'
  use "stays a red-team question". B cannot promote at battery
  level regardless of grammar.

### Candidate C: clause-boundary (01 valueless, boundary at its slot)

- KILLED. Two independent grounds:
  (a) Prior kill covers it: edge-1024-clause-boundary (KILL,
      2026-10-08) rejected every boundary split in @1020-@1029
      ("no alternative boundary position parses"). The remaining
      untested split @1029|@1030 fails by the same logic: the left
      side "ce qui par [43] ce [01]" has no finite verb under any
      live 01 value ('en'/'se'/valueless/bound-'-ci'-fenced), so no
      split at 01's slot yields two complete clauses. A boundary
      before 87 (@1027|@1028) strands verbless "par [43]"; not
      01's slot in any case.
  (b) Distributional mismatch: in 28 windows 01 is never
      row-initial, has 21 distinct predecessors, and its successors
      show no clause-initial enrichment -- a token distribution,
      not a marker distribution. Lane boundary mechanisms are
      dead (clause-boundary-precedent KILL).
- C also strands "ce" ("par [43] ce" is ungrammatical), giving
  "ce" no role, while A/B at least give it a topic role.

## Per-clause pass/fail

1. One candidate parses cleanly and the others are decided: FAIL.
   No candidate parses without strain: A and B share the bare-"ce"
   topic strain (sub-kill-grade); C is killed. No value is named.
2. Profile consistency: PASS for A (three supporting legs; nothing
   forces 'en' false at @1029); PASS-WITH-SCOPE-FLAG for A-promote
   (blocked: locality hard constraint + section 7 polyvalence risk);
   B consistent but disfavored and red-team-scoped; C killed.
3. Adverses: answered (see below).
4. Cleaner rival on the same frames: none demonstrated beyond the
   three candidates; C's kill is recorded above.

## Adverses, answered

- "01's value at @1029 is OPEN": still open after this battery --
  the verdict is null, not a premature naming. The openness is
  now structured (C killed, A favored over B, both need red team).
- "ce-inf-1841 killed 'ce'+infinitive at kill grade": HONORED. A/B
  do not govern the infinitive by "ce": "ce" is a dislocated topic,
  the infinitive is independent/exclamatory. The kill's scope
  ("ce" as determiner/governor of a substantivized infinitive,
  "ce" as bare object) is not entered.
- "'@1029 ceci [03]er [80]-le' premise is STALE": HONORED. The
  bound-'-ci' reading is not used anywhere in this battery.
  Cross-target note for the supervisor: residual-1029-infinitive
  is still queued carrying that stale premise and needs re-brief.
- "01='en' local to the three 01-24 windows": HONORED as a hard
  constraint -- A is not promoted, precisely for this reason.
- "01='tain' local to 37-01 x3 (rival-37-01-certain)": STALE --
  correction recorded. rival-37-01-certain (KILL, 2026-10-09)
  killed 'tain'/"certain" at kill grade at all three 37-01
  windows; the live local reading is 01='fait' (syllable,
  wordinternal-37-01 PROMOTE). 'tain' is dead everywhere, not
  local. This does not affect the A/B/C discrimination ('tain'
  was not a candidate).
- "'se' killed only at 01-24; conditioned 'ce se' stays a
  red-team question": HONORED. B is not promoted; its scope is
  left to the red team.

## Verdict: NULL

Candidate C (clause-boundary) is killed as a candidate. Candidates
A ('c'en') and B ('ce se') both survive grammatically (shared
sub-kill-grade bare-"ce" strain), with the 28-window profile
favoring A decisively ('en' established locally for 01; "c'en"
elision precedented by "m'en" @828; second "ce en" leg @984;
'se' unattested for 01). Neither can promote at battery level:
A hits the brief's 'en'-locality hard constraint and the section 7
polyvalence flag; B is explicitly red-team-scoped. The @1032
clause's last open slot therefore goes to the red team as a clean
two-horse race (A vs B), not as a battery promote.

No standing verdict contradicted or downgraded. No second
polyvalence declared. Section 7 intact.

## Follow-up targets (nulls regenerate work)

1. **ce01-1029-redteam-package** (P2): evidence package for red-team
   adjudication of 'c'en' (A) vs 'ce se' (B) at @1029. Bar: package
   files this report's discrimination (C killed per edge-1024 +
   verbless-left extension; A's three profile legs; B's three
   disfavor counts; the bare-"ce" shared strain; the 'en'-locality
   and polyvalence blockers) and the red team names 01's value or
   kills both. Closes the @1032 clause one way or the other.
2. **stem-03-en-se-licensing** (P3): once stem-03-value names [03]'s
   verb value, test clitic licensing at @1029. Bar: [03]'s value
   licenses exactly one of {'en' (A: verb taking partitive/object
   "en"), 'se' (B: pronominal verb)}; kill the unlicensed candidate
   at @1029 at kill grade. Coordinates with (does not duplicate)
   stem-03-value.
3. **ce87-topic-licensing** (P3): attack the shared strain of A and
   B -- bare "ce" (87) as exclamatory-infinitive/dislocation topic
   at @1029. Bar: find period-corpus or lane-internal precedent for
   bare 'ce' heading an exclamatory infinitive or a dislocation;
   if none exists (kill-grade: clitics cannot be dislocated, and
   exclamatory subjects must be tonic), both A and B die and the
   imp-80-set skeleton ("ce [01] - [03]er!") must be revised, with
   87's role at @1028 re-opened.

## Bookkeeping

- Report: code/crowd17/report_inbox/battery-ce01-slot-1029.md (this file).
- battery-queue.json: `ce01-slot-1029` queued -> verdict/null via
  temp-file + rename (pre-write assert confirmed queued/verdictless;
  JSON re-validated post-write; own entry only).
- Lock created on start (agent id + UTC timestamp), deleted on completion.
- Stream re-derived in-session (1,847 pairs / 96 types); canonical.py
  never used; R5005, sealed gates, red-team queue untouched.
- Every number traces to the stream; no invented data.
