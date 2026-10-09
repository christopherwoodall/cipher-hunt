# Battery report: disloc-demonstrative-drama

- Target id: `disloc-demonstrative-drama`
- Claim: "19th-century French DRAMA census for dislocated demonstrative
  (cela/ceci/ca) + bare exclamatory infinitive"
- Date: 2026-10-09
- Worker: battery worker (subagent 199f78ad-0b5d-41db-82ae-b78feab30a86)
- Stream: not applicable — corpus census against period French drama, per
  target charter. The 1,847-pair repaired parse was not used. R5005, sealed
  gate instances, and the red-team adjudication queue were not touched.

Terms (ASD-STE100): "dislocation" = a topic moved to the front of the clause,
set off by a pause, and resumed by a pronoun ("Moi, je sais" = "me, I know").
"Tonic" = the stressed form of a pronoun (moi, cela, ça). "Bare exclamatory
infinitive" = an infinitive used as an exclamation with no preposition,
no "que", and no resumptive clitic between the topic and the verb
("Moi, voler !").

## Parentage

Follow-up #1 of the battery-level NULL `disloc-demonstrative-inf`
(2026-10-09, verdict: null, fenced). That battery found 0 genuine
dislocated-demonstrative + bare-exclamatory-infinitive attestations in
27.66M characters of 19th-century French prose (15 candidates, all
classified). This battery extends the census to the drama register, the
theorised natural habitat of bare exclamatory infinitives.

## Bar (verbatim, pre-registered before testing)

">=1 genuine 'cela/ceci/ca, [bare inf] !' in drama promotes arm (a);
confirmed zero fences it at drama-register level"

Numbered pass/fail clauses (restated before testing, not modified after):

1. At least one GENUINE "cela/ceci/ça, [bare infinitive] !" attestation in
   19th-century French DRAMA exists. If yes: arm (a) of ce87-1028-role is
   strengthened to promote-grade (promote).
2. If clause 1's census is a confirmed zero — every candidate window
   classified, false friends and OCR excluded with cause — arm (a) stays
   fenced at the drama-register level (null per §4: inconclusive as a kill,
   since zero is an absence).

## Method

1. Read BATTERY-PROTOCOL.md first. Created the lock
   `code/crowd17/next-token/locks/disloc-demonstrative-drama.lock` on start
   (no lock, stale or fresh, existed for this id); deleted on completion.
2. Target charter requires: census 19th-century French DRAMA texts using
   only corpora already present in the lane or its side dirs; no fetching
   of copyrighted works off the open web.
3. Inventoried the lane and the wider workspace for drama texts:
   - Lane corpora (code/side-period/corpus/): guizot-memoires
     t1/t2/t3/t5-t6, nesselrode v7/v8/v9/v10, revue-deux-mondes-1841
     q1/q2/q3/q4, metternich-papiere v4/v6, talleyrand-memoires-v1,
     pozzo-di-borgo-correspondance-v1, levant-correspondence-1841-p3
     (all French prose; 14 German newspaper files excluded with cause —
     wrong language, not drama).
   - Lane data/: data/gutenberg-17489-miserables1.txt (Les Misérables
     tome 1), data/gutenberg-30513-tocqueville-t1.txt,
     data/gutenberg-30514-tocqueville-t2.txt (prose).
   - Workspace-wide `find` (maxdepth 4) for *hugo* / *dumas* / *scribe* /
     *vaudeville* / *theatre* / *theater* / *piece* / *corpus*: zero drama
     hits. Only non-lane matches were unrelated math-paper titles.
   - Result: the lane holds NO 19th-century French drama texts at all.
     Everything present is prose (memoirs, correspondence, newspapers,
     criticism, novels).
4. Because the charter forbids fetching new works from the web, I did not
   pull public-domain Hugo/Dumas/Scribe editions. The census could not be
   run: there is no drama corpus to census.

## Window-level evidence

- Candidate windows found: 0. Not because the construction is absent from
  drama — because no drama text exists in the in-lane corpus to search.
- Corpus inventory (character counts from the disloc-demonstrative-inf
  census): 27,657,940 characters of 19th-century French, all prose
  (25.67M 1841-register + 1.99M wider). Drama share: 0 characters.
- This is a corpus-availability finding, not a linguistic finding. Clause 1
  could not be attempted and clause 2 could not be executed — a census
  cannot return a confirmed zero over an empty set, and treating "no corpus"
  as "zero attestations" would be an invented number, which §7 forbids.

## Per-clause pass/fail

1. ≥1 genuine "cela/ceci/ça, [bare inf] !" attestation in 19th-century
   French drama: **UNTESTABLE.** No drama corpus in the lane; web fetching
   prohibited by the target charter. No claim made either way.
2. Confirmed zero → arm (a) fenced at drama-register level: **NOT
   EXECUTED.** An absence of corpus is not a confirmed zero; recording one
   would fabricate evidence.

Per BATTERY-PROTOCOL.md §2: a genuinely untestable bar is recorded as a
finding and counts as a **null** (§4) — not silently rewritten, not
promoted, not killed.

## Adverses, answered

- None pre-registered ("Adverses: null").
- Self-check: this null does not touch arm (a)'s fencing status from
  disloc-demonstrative-inf — arm (a) of ce87-1028-role remains fenced as
  chartered by the parent battery; this battery adds nothing and removes
  nothing. The standing `ce87-topic-licensing` KILL is untouched.
- §5.2: no standing red-team verdict touched; no overwrite, no escalation
  required.

## Verdict: NULL (bar untestable as written — corpus gap)

The 19th-century French drama census cannot run because the lane holds no
drama corpus (0 drama texts in 27.66M characters of in-lane French; Hugo,
Dumas, Scribe, vaudeville all absent from the lane and the workspace).
The construction's status in the drama register stays open. Work
regenerates via the follow-ups below.

## Follow-ups (nulls regenerate work)

1. **disloc-demonstrative-drama-ingest** (P1 commission): the blocker is
   corpus, not method. Commission an ingest pass: harvest public-domain
   19th-century French drama (Hugo plays — Hernani, Ruy Blas, Les
   Burgraves; Dumas père; Scribe; vaudeville one-acts) from
   gutenberg.org / wikisource with provenance notes (source URL,
   retrieval time, sha256) into the lane corpus dir. Copyright note:
   all named authors died 1861–1885, so the works are public domain —
   the fetch bar is charter-of-battery, not law-of-copyright. Once the
   corpus lands, this battery's exact bars become testable.
2. **disloc-demonstrative-quoted-drama** (P3): run the census NOW on the
   closest in-lane drama proxy — quoted-dialogue windows inside the
   revue-deux-mondes-1841 corpus («...» / "..." / em-dash dialogue).
   The single shape precedent ('Moi, voler !') is itself quoted speech
   in RDM, so RDM's quoted material is already a mixed-register sample
   touching theatre. Bar: ≥1 genuine "cela/ceci/ça, [bare inf] !" in
   quoted-dialogue promotes arm (a); confirmed zero fences it at
   quoted-drama level. (Does not duplicate disloc-demonstrative-inf:
   quoted-dialogue-only windows, not the full corpus.)
3. **disloc-demonstrative-drama-reissue** (P3, hold behind follow-up 1):
   once the drama corpus is ingested, re-run this battery with the same
   pre-registered bars. The supervisor may hold this until follow-up 1
   lands. (Does not duplicate: this battery ran no census; the reissue
   is the census.)

Note for the supervisor: do NOT re-queue disloc-demonstrative-reinforced
(it is already queued); none of the three follow-ups above duplicates it.

## Bookkeeping

- Lock: created on start (agent id 199f78ad-0b5d-41db-82ae-b78feab30a86 +
  2026-10-09T08:19:08Z), deleted on completion. No stale lock existed.
- Report: code/crowd17/report_inbox/battery-disloc-demonstrative-drama.md
  (this file).
- battery-queue.json: `disloc-demonstrative-drama` queued -> verdict/null
  via temp-file + rename (pre-write assert confirmed queued/verdictless;
  JSON re-validated post-write; own entry only; claim/bars/evidence/
  adverses preserved).
- R5005, sealed gates, red-team queue untouched. No numbers invented;
  the only count asserted is the prose-corpus size from the parent
  battery's census and the drama-corpus count of zero.
