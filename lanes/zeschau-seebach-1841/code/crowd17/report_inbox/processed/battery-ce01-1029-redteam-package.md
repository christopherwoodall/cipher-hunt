# Battery report: ce01-1029-redteam-package

- Target id: `ce01-1029-redteam-package`
- Claim: "adjudication package for the @1029 'c'en' vs 'ce se' two-horse race (evidence only)"
- Date: 2026-10-09
- Worker: battery worker (subagent be6adbe6-2e5a-4402-b268-dda1d9193b28)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` +
  `code/side-keyhunt/repaired_offsets.json`, parsed per
  `code/side-keyhunt/repair_parse.py`). Verified in-session: 1,847 pairs,
  96 types; locus @1028-1040 = "87 01 03 29 80 77 11 70 82 34 29 40 17"
  (row a6_03); left edge @1024-1027 = "45 64 96 43"; n(01)=28 confirmed.
  `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
- Lock: `code/crowd17/next-token/locks/ce01-1029-redteam-package.lock`
  (created at start, deleted on completion; no stale lock present).

Terms (ASD-STE100): "evidence package" = all the battery evidence for the
red team to adjudicate. "Two-horse race" = two candidate readings A and B
left standing against each other. "Kill grade" = proof that a reading is
false. "Sub-kill-grade" = a strain below proof. "Dissolution" = two cipher
groups read as one French word (cela = 87+11). "Dislocation" = a topic
moved to the front of the clause, set off by a pause, and resumed by a
pronoun ("Moi, je sais"). "Tonic" = the stressed form (moi, cela, ceci).
"Clitic" = the unstressed form (me, ce).

## Bar (verbatim from target, pre-registered before testing)

"package the A-vs-B evidence for red-team adjudication: candidate C
killed (edge-1024-clause-boundary + @1029|@1030 extension), A's 3
profile legs ('en' local value, 'm'en' @828 precedent, @984 'ce en
fait' second leg), B's unattested 'se'; no value named, no promote
claimed"

Numbered pass/fail clauses (restated before testing, not modified after):

1. Candidate C (clause-boundary at 01's slot) is packaged as killed:
   edge-1024-clause-boundary + the @1029|@1030 extension, with byte
   evidence.
2. Candidate A ('c'en', 01='en') is packaged with its three profile
   legs ('en' local value at the three 01-24 windows; "m'en" @828
   elision precedent; @984 "ce en fait" second leg) and its blockers
   ('en'-locality hard constraint; section-7 polyvalence risk).
3. Candidate B ('ce se', 01='se') is packaged with the three disfavor
   counts ('se' unattested for 01; no elision precedent; no second
   "ce se" leg) and its red-team scope.
4. No cipher value is named and no promote is claimed for any value.
5. The supervisor note (ce87-topic-licensing killed both A and B; the
   package is re-scoped to the imp-80-set skeleton revision) is
   answered with stated cause.

## Method

1. Read BATTERY-PROTOCOL.md first. Created/deleted the lock per protocol.
2. Re-derived the repaired stream in-session. Byte-verified the clause
   and the 01 profile basics (see header).
3. Adopted as premises (not re-litigated): ce01-slot-1029 NULL (the
   A/B/C discrimination), ce87-topic-licensing KILL (both A and B dead),
   skeleton-1032-revise PROMOTE (revised skeleton "Ceci, [03]er!
   [80]-le, la première fois!"), ce87-1028-role NULL (87's role fenced,
   ceci-compound leading), dislocation-ce-sweep PROMOTE (kill confirmed
   at wider register level), gov-excl-inf-drama PROMOTE and
   gov-excl-inf-modern PROMOTE (1841 zero period-bound).
4. This is an evidence-only package. It names no value, claims no
   promote, declares no polyvalence, and touches no red-team verdict.

## Part I — the A-vs-B evidence as chartered

### The clause (byte-exact, re-derived in-session)

@1024-1042 (row a6_03):
`45 64 96 43 | 87 01 03 29 80 77 11 70 82 34 29 40 17 77 82`
= "ce(45) qui(64) par(96) [43] ce(87) [01] [03]er [80]-le(77)
   la(11) pre(70) m(82) i(34) er(29) e(40) fois(17) le(77) m(82)"

Working skeleton at packaging time (imp-80-set, battery-grade lead):
"ce [01] - [03]er! [80]-le, la premiere fois!" (exclamatory infinitive
+ imperative with enclitic 'le').

### Candidate A: 'c'en' (01='en') — profile legs

- Leg 1 ('en' local value): 'en' is an established 01 value at the
  three 01-24 windows (disc-01-24-ci-X, battery-level). Verified
  in-session: @40 ("39 64 41 [01] 24 88"), @828 ("59 38 82 [01] 24
  87 11" = "m' en"), @984 ("47 78 45 [01] 24 89" = "ce en").
- Leg 2 (elision precedent): "ce en" -> "c'en" matches "m'en" @828,
  where the lane already accepts invisible elision before vowel-initial
  01='en'.
- Leg 3 (second "ce en" leg): @984's promoted parse is "ce(45) en(01)
  fait(24) [89]" — the "ce en" bigram parses cleanly at a second
  window.
- Grammatical shape: "Ce, en [03]er!" (left-dislocation + exclamatory
  infinitive; partitive "en" resumes the topic) parallels "Moi, en
  parler!" / "Eux, en profiter!".
- Shared strain (sub-kill-grade at packaging time): the topic is bare
  "ce", an unstressed clitic; dislocation topics and exclamatory
  subjects are normally tonic ("cela/moi"). Lacked period-corpus
  backing at kill grade.

### A's blockers

- 'en'-locality hard constraint: 01='en' is local to the three 01-24
  windows per disc-01-24-ci-X; a fourth 'en' window at @1029 revises
  that scope.
- Section-7 polyvalence risk: bound '-ci' is live (NULL, not killed) at
  @1029; naming 01='en' there risks a second polyvalence ('en'/'-ci').
  disc-01-24-ci-X consequence 5 flags exactly this unification as
  RED-TEAM-ONLY. Not declared at battery level.

### Candidate B: 'ce se' (01='se') — disfavor counts

- Count 1: 'se' is unattested for 01 anywhere in the 28-window profile.
- Count 2: no phonological precedent — "ce se" has no elision parallel
  to "m'en"/"c'en".
- Count 3: no second "ce se" leg — @984's "ce se fait" is inside the
  01-24 'se'-kill scope; @345 "ce se [06-ent]" and @195 "ce se [21]"
  do not parse.
- Grammatical shape: "Ce, se [03]er!" (reflexive resumption, "se" =
  accusative subject coindexed with topic "ce") parallels "Moi, me
  taire!" / "Lui, se lever!". Same bare-"ce" strain as A (shared,
  sub-kill-grade).
- Scope: 'se' is killed only at 01-24; the conditioned 'ce se' use
  "stays a red-team question" (brief's adverse). B could not promote
  at battery level regardless of grammar.

### Candidate C: clause-boundary — killed

- Ground (a): edge-1024-clause-boundary (KILL, 2026-10-08) rejected
  every boundary split in @1020-@1029. The remaining untested split
  @1029|@1030 fails by the same logic: the left side "ce qui par [43]
  ce [01]" has no finite verb under any live 01 value
  ('en'/'se'/valueless/bound-'-ci'-fenced), so no split at 01's slot
  yields two complete clauses. A boundary before 87 (@1027|@1028)
  strands verbless "par [43]".
- Ground (b): distributional mismatch — in 28 windows 01 is never
  row-initial (0/28, verified in-session), has 21 distinct
  predecessors (promiscuous, token-like), and its successors show no
  clause-initial enrichment (00 x1, 46 x0, 94 x0 after 01). A token
  distribution, not a marker distribution. Lane boundary mechanisms are
  dead (clause-boundary-precedent KILL).
- C also strands "ce" ("par [43] ce" is ungrammatical), giving "ce" no
  role, while A/B at least give it a topic role.

## Part II — post-package battery events (the re-scope)

### ce87-topic-licensing (battery KILL, 2026-10-09): both A and B dead

The bar's chartered attack on the shared strain returned at kill
grade. Adopted, not re-litigated:

- Bare "ce" cannot head an exclamatory infinitive clause in 1841
  French. Zero attestations in 24.4M characters of 1841-register
  French; all 27 bare "ce," hits classified as clefts, formula
  ("sur ce,"), or OCR artifacts; the fronted-demonstrative slot
  belongs to the tonic forms (cela/ceci/ça, 335x).
- Grammar: "ce" is atonic (Littré); dislocation requires tonic forms
  (Beauzée: ceci/cela are the standalone forms). Clitics cannot carry
  the stress a dislocated topic requires.
- Both A and B parse ONLY via the bare-'ce'-topic + exclamatory-
  infinitive assumption (their single shared load-bearing element);
  ce01-slot-1029 found no alternative grammatical route for either.
- Consequence: the imp-80-set skeleton must be revised; 87's role at
  @1028 is re-opened (87='ce' value stands; only its role is open).

### dislocation-ce-sweep (battery PROMOTE, 2026-10-09)

Confirms the kill at the wider 19th-century register level.

### Why the A-vs-B adjudication is moot

- A is dead at kill grade, so its 'en'-locality blocker is MOOT: no
  fourth-'en' window exists anymore. The disc-01-24-ci-X locality
  constraint is untouched.
- B is dead at kill grade; its red-team scope is MOOT.
- Section 7: no polyvalence was declared. The 'en'/'-ci' unification
  question now lives with the 'ceci' compound reading, red-team venue.
- No cipher value is named and no promote is claimed for 01.

## Part III — the re-scoped adjudication (imp-80-set skeleton revision)

### skeleton-1032-revise (battery PROMOTE, 2026-10-09)

Revised skeleton: **"Ceci, [03]er! [80]-le, la première fois!"**

- @1028-1029 "87 01" = "ceci" (fused tonic demonstrative). Dissolution
  model granted (cela = 87+11, n=7; ceci = 87-61 promoted @644). The
  killed construction was a *bare clitic* "ce" topic; "ceci" is the
  *tonic* form — exactly the form the kill's grammar prescription
  demands in the dislocation slot. Zero reliance on the dead reading.
- @1030-1031 "03 29" = "[03]er" (exclamatory infinitive, 29="er" banked
  GT, 03 verb stem under the conditioned split).
- @1032-1033 "80 77" = "[80]-le" (imperative 80-stem + enclitic 'le',
  from poly-80-x29-frame PROMOTE).
- @1034-1040 "11 70 82 34 29 40 17" = "la première fois" (pencil crib
  + granted "fois").
- Sole non-granted value: bound "-ci" at 01 (battery-NULL, surviving,
  ce-context-licensed) = 1, within the <=1 allowance.
- Red-team ratification still needed before banked use.

### ce87-1028-role (battery NULL, fence, 2026-10-09)

87's role at @1028 is fenced, not named. Ranked arms: (a) 87-01 =
"ceci", tonic demonstrative topic — LEADING, but blocked on the
battery-NULL 01='-ci' premise and the unattested
demonstrative+bare-infinitive combination (0x in 24.4M chars; one
shape precedent, "Moi, voler !" in RDM 1841-q1); (b) standalone "ce",
stranded residual — role-less under all standing values; (c)
leftward 43-87 attachment — no precedent.

### Open red-team calls (evidence only, undecided)

1. 01's value at @1029: bound '-ci' (leading, battery-NULL) vs
   valueless/strand arm. Stem-03-en-se-licensing is queued (P3) to
   license-test 01's value once stem-03-value names [03].
2. 03's and 80's verb VALUES: class-level reads only (conditioned 03
   split; A8 verb-frame). Their names stay open.
3. The left-edge "ce qui par [43]" verbless strain: no finite verb
   under any live reading ("ce qui" needs a verb after the "par [43]"
   parenthesis); edge-1024-clause-boundary's KILL means no boundary
   rescues it. Leftedge-1024-43-governor and quice-verb-1024 are
   queued (P3).
4. Whether the ceci-based skeleton is ratified for banked use.
   Ceci-1029-ratify-feed is queued (P4).

## Part IV — register footnotes (post-race corpus results)

- gov-excl-inf-drama PROMOTE (2026-10-09): one genuine governed
  exclamatory infinitive in the drama corpus ("Pour conspirer !…"
  in Scribe's *Bertrand et Raton*; 1 of 839, dialogue-anaphoric).
- gov-excl-inf-modern PROMOTE (2026-10-09): the 1841 zero is
  period-bound — one genuine in early-20th-century fiction (Leroux,
  *Le mystère de la chambre jaune*, 1907: "De ne pas pénétrer dans
  la chambre!"; 1 of 1.53M chars).
- These re-open the governed-exclamatory-infinitive avenue at register
  level generally, but do NOT restore A or B: that kill rests on the
  clitic/tonic dislocation rule (bare "ce" as topic), not on
  exclamatory infinitives per se. A bare-"ce" topic remains unattested
  everywhere searched.

## Per-clause pass/fail

1. C packaged as killed: **PASS.** Grounds (a) and (b) with byte
   evidence, adopted from edge-1024-clause-boundary (KILL) and
   ce01-slot-1029, with the @1029|@1030 extension stated.
2. A packaged with three legs + blockers: **PASS.** Legs 1-3 verified
   in-session at their loci; 'en'-locality and §7 blockers stated
   with the disc-01-24-ci-X citations.
3. B packaged with three disfavor counts + red-team scope: **PASS.**
   Counts and scope stated as in the parent report.
4. No value named, no promote claimed: **PASS.** 01's value, 87's
   role, 03's and 80's values all stay open; every live question is
   marked red-team venue or battery-queued.
5. Supervisor note answered: **PASS.** The A/B adjudication is moot
   (both dead at kill grade); the package is re-scoped to the
   skeleton revision, with all four open red-team calls and their
   queued batteries named.

## Adverses, answered

- "§7 sole-polyvalence: battery packages only, never decides; A's
  fourth 'en' window risks revising disc-01-24-ci-X locality —
  red-team call": ANSWERED. The package decides nothing; and since A
  is dead, there is no fourth-'en' window — the locality risk is moot.
  The 'en'/'-ci' unification question now attaches to the 'ceci'
  compound, red-team venue (see call 1 above).
- "ce87-topic-licensing KILLED both A ('c'en') and B ('ce se') — this
  package is moot for the A-vs-B adjudication and should be re-scoped
  to the imp-80-set skeleton revision": ANSWERED. Re-scoped as
  directed: Parts II-III document the kill and the current skeleton-
  revision state with all queued continuations.

## Verdict: PROMOTE

The evidence package is complete and current: the A-vs-B evidence as
chartered (C killed, A's three legs and blockers, B's disfavor
counts), the post-charter battery events that killed both A and B at
kill grade (ce87-topic-licensing KILL, confirmed by
dislocation-ce-sweep PROMOTE), the re-scoped skeleton revision
(skeleton-1032-revise PROMOTE; ce87-1028-role fenced; four open
red-team calls with their queued batteries named), and the register
footnotes that re-open governed exclamatory infinitives without
restoring A or B. "Promote" marks the package's completeness — no
cipher value is named, no promote is claimed for any value, no
polyvalence is declared, and no standing or red-team verdict is
contradicted or downgraded. §7 intact.

Every number traces to the re-derived repaired stream or to the
cited battery reports; no invented data.

## Follow-ups (promote — continuations already in flight, none new)

The re-scoped follow-ups named by the supervisor note are already
queued or have verdicts; nothing new is proposed:

- leftedge-1024-43-governor (queued P3), quice-verb-1024 (queued P3)
  — the "ce qui par [43]" left edge.
- stem-03-en-se-licensing (queued P3) — 01's value test once 03
  is named.
- ceci-1029-ratify-feed (queued P4) — feeds the 'ceci' read to the
  red-team docket.
- disloc-demonstrative-inf (verdict null, 2026-10-09) — fenced the
  demonstrative+bare-infinitive arm at register level.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-ce01-1029-redteam-package.md`
  (this file).
- battery-queue.json: `ce01-1029-redteam-package` queued -> verdict/
  promote via temp-file + rename (pre-write assert confirmed
  queued/verdictless; JSON re-validated post-write; own entry only;
  no downgrade).
- Lock created on start (agent id + UTC timestamp), deleted on
  completion (verified gone).
- Stream re-derived in-session (1,847 pairs / 96 types); canonical.py
  never used; R5005, sealed gates, red-team queue untouched.
