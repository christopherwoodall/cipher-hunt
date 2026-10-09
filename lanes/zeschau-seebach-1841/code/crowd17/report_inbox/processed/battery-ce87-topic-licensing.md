# Battery report: ce87-topic-licensing

- Target id: `ce87-topic-licensing`
- Claim: "adversarial: if bare 'ce' can't head the exclamation (clitics can't be dislocated), both A/B die and the imp-80-set skeleton must be revised"
- Date: 2026-10-09
- Worker: battery worker (subagent eea0da8a-95e1-41ff-82c5-5f6a1b76de4e)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py).
  Re-derived in-session: 1,847 pairs; byte-verified @1028-1040 =
  "87 01 03 29 80 77 11 70 82 34 29 40 17". Never used canonical.py.
  R5005, sealed gates, red-team queue untouched.
- Lock: code/crowd17/next-token/locks/ce87-topic-licensing.lock (created at
  start, deleted on completion; no prior lock for this id existed).

Terms (ASD-STE100): "dislocation" = a topic moved to the front of the
clause, set off by a pause, and resumed by a pronoun ("Moi, je sais" =
"me, I know"). "Tonic" = the stressed form of a pronoun (moi, cela, ça).
"Clitic" = the unstressed form (me, ce). "Exclamatory infinitive" = an
infinitive used as an exclamation ("Moi, me taire !" = "me, to shut up!").

## Bar (verbatim, pre-registered before testing)

"test whether a bare 'ce' topic can head an exclamatory infinitive clause
in 1841 French (1841 register + clitic-dislocation grammar); if yes, A/B
survive; if no, both die and the imp-80-set skeleton is revised"

Numbered pass/fail clauses (restated before testing, not modified after):

1. A bare-'ce' (87) topic can head an exclamatory infinitive clause in
   1841 French: grammatical in the 1841 register, and permitted by
   clitic-dislocation grammar.
2. If clause 1 fails: candidates A ('c'en') and B ('ce se') at @1029 are
   both killed, and the imp-80-set skeleton
   ("ce [01] - [03]er! [80]-le, la premiere fois!") must be revised, with
   87's role at @1028 re-opened.

## Method

1. Read BATTERY-PROTOCOL.md first. Created/deleted the lock per protocol.
2. Re-derived the repaired stream in-session (1,847 pairs). Byte-verified
   the clause: @1028-1040 = "87 01 03 29 80 77 11 70 82 34 29 40 17"
   (row a6_03); left context @1024-1027 = "45 64 96 43". canonical.py
   never used.
3. Ran a corpus census for bare-"ce" fronting in the lane's 1841-register
   period corpus (code/side-period/corpus/): 24,431,196 characters over
   guizot-memoires (t1/t2/t3/t5-t6), nesselrode v7-v10 (v8 covers 1840-46),
   revue-deux-mondes-1841 (q1-q4), metternich-papiere (v4/v6),
   talleyrand-memoires-v1, pozzo-di-borgo-correspondance-v1,
   levant-correspondence-1841-p3, allgemeine-zeitung-augsburg-1841 (Jan run).
4. Checked period grammar: Littré (1872-77) art. "ce"; Beauzée, Encyclopédie
   1re éd., art. "Ce" (via dicocitations, PD); standing lane findings
   Calvet & Chompret and TLFi (re-used from ce-inf-1841, not re-fetched).
5. Checked every standing verdict that touches 87 or this clause. None is
   contradicted or downgraded (see Adverses).

## Window-level evidence

### The clause under test (byte-exact, repaired stream)

@1024-1042 (row a6_03):
`45 64 96 43 87 01 03 29 80 77 11 70 82 34 29 40 17 77 82`

The A/B parses under test (from ce01-slot-1029):
- A: "Ce, en [03]er! [80]-le, la premiere fois!" (01='en'; topic "ce",
  exclamatory infinitive with partitive "en" resuming the topic).
- B: "Ce, se [03]er! [80]-le, la premiere fois!" (01='se'; topic "ce",
  exclamatory infinitive with reflexive "se" coindexed with the topic).

Both require 87='ce' to sit as a bare dislocated topic heading an
exclamatory infinitive clause. That is the single shared assumption under
test here.

### Corpus census: bare "ce" never heads a fronted topic, never an infinitive

1. **"ce, [infinitive]" = 0 in 24.4M characters.** Zero occurrences of a
   bare "ce" followed by a comma and an infinitive (with or without "en")
   anywhere in the 1841-register corpus.
2. **All 27 bare "ce," occurrences are non-topics.** Every hit is one of:
   interrogative clefts ("qu'est-ce,", "est-ce,", "qu'étaient-ce,",
   "que serait-ce," — subject-verb inversion, not dislocation);
   the valediction formula "sur ce," (x7, = "on that note", never
   followed by an infinitive); OCR hyphen artifacts ("Fran- ce,",
   "disgräce,"); "qui est ce, M. Hubert" (predicate nominal). None is a
   dislocated topic; none heads an infinitive clause.
3. **The one apparent hit is an OCR line-wrap.** guizot-memoires-t5-t6
   lines 18142-43: "de ce sacr.- / ce, se rapprocher des trois autres".
   Raw text shows "sacr.-" at line end: the word is "sacrifice" split
   across the line break, i.e. "de ce sacrifice, se rapprocher..." (an
   absolute construction, "satisfied by this sacrifice, [England] to draw
   closer..."). Excluded with cause. It is not a bare-"ce" dislocation.
4. **Tonic demonstratives own the fronted-topic slot.** "cela," x291,
   "ceci," x39, "ça," x5 — fronted demonstrative topics always use the
   tonic forms. Tonic-head + infinitive constructions: 22 matches.
   The corpus's licensed "c'est + infinitive" route is "c'est ... que de
   + inf." (x27) — it requires "que de", never a bare infinitive, and
   never a dislocated bare "ce".
5. **Grammar: "ce" is atonic; dislocation requires tonic forms.**
   Littré's pronunciation note for "ce": unstressed /sə/ ("se tas").
   Beauzée (Encyclopédie, PD): the particles "ci" and "là" added to the
   substantive "ce" formed "ceci" and "cela" — these are the standalone
   forms used when the demonstrative stands alone. A clitic cannot carry
   the stress that a dislocated topic requires; the French paradigm puts
   the tonic form in that slot ("Moi, me taire !", "Lui, se lever !",
   "Cela, nous ne voulons le faire que..." — the last from Guizot t2 in
   this corpus). Standing lane findings (ce-inf-1841): "ce" precedes a
   verb or a relative pronoun and is never followed by a noun (Calvet &
   Chompret); "ce" with verbs other than "être" is archaic even for the
   classical period (TLFi). An exclamatory infinitive's expressed subject,
   when present, is tonic. *"Ce, en [03]er !" and *"Ce, se [03]er !" are
   therefore ungrammatical in 1841 French — not merely strained.

## Per-clause pass/fail

1. Bare-'ce' topic can head an exclamatory infinitive in 1841 French:
   **FAIL, kill grade.** Zero corpus attestations in 24.4M characters of
   1841-register French; all 27 bare "ce," hits classified as clefts,
   formula, or OCR; the fronted-demonstrative slot belongs to the tonic
   forms (cela/ceci/ça, 335x); grammar positively establishes "ce" as
   atonic and dislocation as tonic-only. The rule against it is
   positively established, not an absence of evidence.
2. Consequence arm: **EXECUTED.** Candidates A and B at @1029 are both
   killed — both parse only via the now-refuted bare-'ce'-topic +
   exclamatory-infinitive assumption, which was their single shared
   load-bearing element (ce01-slot-1029 found no other grammatical route
   for either). The imp-80-set skeleton
   ("ce [01] - [03]er! [80]-le, la premiere fois!") must be revised; 87's
   role at @1028 is re-opened (87='ce' promoted value stands; only its
   role in this clause is open).

## Adverses, answered

- "both A/B parse only via strained bare-'ce'-topic + exclamatory
  infinitive (sub-kill-grade, shared); a negative answer here is a
  skeleton-level kill": UPGRADED and ANSWERED. The strain is kill-grade,
  not sub-kill-grade: the period corpus and the atonic/tonic grammar rule
  refute the construction positively. Skeleton-level kill recorded.
- Tension note (not a contradiction): ce01-slot-1029 graded this strain
  "sub-kill-grade" and chartered this battery to attack it. That report
  is battery-level NULL, not a red-team verdict; this battery is the
  chartered attack, and its outcome (kill) is what the charter
  anticipated ("if none exists (kill-grade: clitics cannot be
  dislocated...), both A and B die").
- No standing red-team verdict touched: the red-team report has 0
  mentions of @1028; imp-80-set is battery-level NULL. 87='ce' (promoted)
  is not downgraded — the value stands; only its role at @1028 re-opens.
- cela-87-11 ("cela" = 87+11, promoted) unaffected: that verdict is about
  composition, not about bare-"ce" dislocation.

## Verdict: KILL

Headline: bare "ce" cannot head an exclamatory infinitive clause in 1841
French — clitics cannot be dislocated, and the 1841-register corpus (zero
attestations in 24.4M characters; tonic cela/ceci/ça own the slot)
positively confirms the grammar rule. Candidates A ('c'en') and B
('ce se') at @1029 are both dead: their single shared load-bearing
assumption is refuted, and ce01-slot-1029 found no alternative grammatical
route for either. The imp-80-set skeleton for @1028-1040 must be revised;
87's role at @1028 is re-opened (87='ce' value itself stands).

## Follow-ups (kill; skeleton revision is mandated by the bar)

1. **skeleton-1032-revise** (P1): re-parse @1028-1040
   ("45 64 96 43 87 01 03 29 80 77 11 70 82 34 29 40 17") under standing
   values without the killed bare-"ce"-topic. Bar: one grammatical
   1841-French parse with <=1 non-granted value assumption, or fence the
   residual. 87='ce' value stands; its role is the open question.
2. **ce87-1028-role** (P2): discriminate 87's role at @1028 once the
   skeleton is reworked (cleft arm "ce qui par [43] ce..."? left edge of a
   "c'est ... que de" structure? other?). Bar: >=2 frame-legs under one
   role or fence.
3. **dislocation-ce-sweep** (P3): widen the negative census to the full
   19th-century register (beyond the lane's 1841 corpus) as
   negative-confirmation of this kill. Bar: if a genuine bare-"ce"
   dislocation attestation appears, this kill re-opens; else the kill is
   confirmed at register level.

Note for the supervisor: ce01-1029-redteam-package (queued by
ce01-slot-1029) is now moot as an A-vs-B adjudication — both candidates
are dead. The red-team package should be re-scoped to the skeleton
revision (follow-ups 1-2), not the A/B race.

## Bookkeeping

- Report: code/crowd17/report_inbox/battery-ce87-topic-licensing.md (this file).
- battery-queue.json: `ce87-topic-licensing` queued -> verdict/kill via
  temp-file + rename (pre-write assert confirmed queued/verdictless;
  JSON re-validated post-write; own entry only; evidence/adverses
  preserved, new evidence appended).
- Lock created on start (agent id + UTC timestamp), deleted on completion.
- Stream re-derived in-session (1,847 pairs); canonical.py never used;
  R5005, sealed gates, red-team queue untouched.
- Every number traces to the stream or the cited corpus files; no
  invented data.
