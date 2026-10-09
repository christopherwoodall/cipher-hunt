# Battery report: disloc-demonstrative-quoted-drama

- Target id: `disloc-demonstrative-quoted-drama`
- Claim: "run the dislocated-demonstrative + bare exclamatory infinitive
  census on quoted-dialogue windows inside the revue-deux-mondes-1841 corpus"
- Date: 2026-10-09
- Worker: battery worker (subagent 5a14ebc2-e070-43f7-a63f-9f56d9d842c6)
- Stream: not applicable — corpus census against period French, per target
  charter and the disloc-demonstrative-inf precedent. The 1,847-pair
  repaired parse was not used. R5005, sealed gate instances, and the
  red-team adjudication queue were not touched.

Terms (ASD-STE100): "dislocation" = a topic moved to the front of the
clause, set off by a pause, and resumed by a pronoun. "Tonic" = the
stressed form of a pronoun (cela, ça). "Bare exclamatory infinitive" =
an infinitive used as an exclamation with no preposition (de, pour), no
"que", no resumptive clitic. "Quoted-dialogue windows" = text inside
guillemet quotes («...»), straight double quotes ("..."), or em-dash
dialogue paragraphs (— ...).

## Parentage

Follow-up of the battery-level NULL `disloc-demonstrative-drama`
(2026-10-09): that battery's corpus blocker left the drama register
untested; this battery narrows to the theatre-adjacent material that
already exists in-lane — the quoted speech inside revue-deux-mondes-1841,
where the single shape precedent ("Moi, voler !", RDM 1841-q1) lives.
Does not duplicate `disloc-demonstrative-inf` (full-corpus windows) —
quoted-dialogue-only windows, not the full corpus.

## Bar (verbatim, pre-registered before testing)

">=1 genuine 'cela/ceci/ca, [bare inf] !' in quoted-dialogue promotes arm
(a); confirmed zero fences it at quoted-drama level"

Numbered pass/fail clauses (restated before testing, not modified after):

1. At least one GENUINE "cela/ceci/ça, [bare infinitive] !" attestation
   exists inside a quoted-dialogue window of the revue-deux-mondes-1841
   corpus. If yes: arm (a) of ce87-1028-role is promoted.
2. If clause 1's census is a confirmed zero — every candidate window
   classified, false friends excluded with cause — arm (a) is fenced at
   quoted-drama level (null per §4: inconclusive as a kill, since zero is
   an absence).

## Method

1. Read BATTERY-PROTOCOL.md first. Created the lock
   `code/crowd17/next-token/locks/disloc-demonstrative-quoted-drama.lock`
   on start (no stale lock for this id existed); deleted on completion.
2. Ran a reproducible census script:
   `code/crowd17/next-token/disloc_demonstrative_quoted_drama_census.py`.
   Raw results in
   `code/crowd17/next-token/disloc-demonstrative-quoted-drama_census.json`.
   It reuses the verbatim DEM/INF patterns and the window rule of
   `disloc_demonstrative_census.py` (P1–P3), applied to dialogue spans
   only.
3. Corpus, named with sizes (character counts, computed in-session):
   - revue-deux-mondes-1841-q1.txt: 3,013,552 chars → 713 dialogue spans,
     2,245,389 dialogue chars, 37 dem-comma hits in dialogue.
   - revue-deux-mondes-1841-q2.txt: 2,964,405 chars → 730 dialogue spans,
     2,375,587 dialogue chars, 43 dem-comma hits in dialogue.
   - revue-deux-mondes-1841-q3.txt: 3,054,350 chars → 530 dialogue spans,
     2,584,536 dialogue chars, 37 dem-comma hits in dialogue.
   - revue-deux-mondes-1841-q4.txt: 3,165,234 chars → 1,617 dialogue
     spans, 3,110,318 dialogue chars, 52 dem-comma hits in dialogue.
   - Totals: 12,197,541 corpus chars; 3,590 dialogue spans;
     ~10,315,830 dialogue chars; 169 dem-comma hits in dialogue →
     **6 exclamatory candidates (3 unique occurrences)**.
4. Dialogue-span extraction: D1 guillemet «...» (non-greedy DOTALL);
   D2 straight double quote "..." (non-greedy DOTALL, span ≥ 4 chars);
   D3 em-dash paragraphs (blank-line separated, paragraph starts with
   — or –). Spans may overlap; candidates were deduped by (file,
   window) before classification.
5. Due-diligence controls run in-session:
   - Positive control: the shape precedent "Moi,  voler!" (double space
     in the OCR) sits inside a dquote dialogue span in q1
     (span length 33,057 chars; window: "...— Moi,  voler!  répond  le
     bon  Charlemagne..."). The extraction + pipeline cover the known
     precedent's context — the pipeline is validated.
   - Cedilla-less OCR check: `ca,` (no cedilla) + "!" + infinitive-shaped
     word in dialogue windows: 0 candidates across all 4 files.
   - Method caveat: unmatched quote marks produce monster spans
     (>20,000 chars; 22–39 per file). They inflate dialogue-char counts
     but cannot hide a genuine hit — the DEM/INF pipeline searched the
     full span text, and every candidate was classified.

## Window-level evidence

Candidates (all shown verbatim; "/" marks line breaks in the source;
char_offset = offset of the window start in the corpus file):

1. `cela,  un  vagabondage  éternel ,  sans  but  !`
   (revue-deux-mondes-1841-q1.txt, char_offset 231004; INF hits: none) —
   noun appositive ("un vagabondage éternel, sans but"); no infinitive
   at all. Same occurrence as parent-census candidate #3, here confirmed
   inside a dialogue span. Excluded: not a dislocation heading a verb.
2. `cela ,  papa !` (revue-deux-mondes-1841-q4.txt, char_offset 746551;
   INF hits: none) — vocative noun ("papa"). Same occurrence as
   parent-census candidate #4. Excluded.
3. `cela,  vous!` (revue-deux-mondes-1841-q4.txt, char_offset 815763;
   INF hits: none) — pronoun interjection, no verb. Same occurrence as
   parent-census candidate #5. Excluded.

Each occurrence appeared twice in the raw census (overlapping dquote +
em-dash spans) — deduped to 3 unique windows above. Zero of the 6
windows contains any infinitive-shaped word (INF hits: none), so none
can instantiate the bar construction by construction. **0 of 3 genuine.**

## Per-clause pass/fail

1. ≥1 genuine "cela/ceci/ça, [bare infinitive] !" attestation in
   quoted-dialogue windows of RDM 1841: **FAIL (confirmed zero).**
   169 dem-comma hits in dialogue → 3 unique exclamatory candidates,
   all classified (1 noun appositive, 1 vocative, 1 pronoun
   interjection); 0 genuine in ~10.3M dialogue chars.
2. Confirmed zero → arm (a) fenced at quoted-drama level: **EXECUTED.**
   Zero is an absence, not a refutation — the "Moi, voler !" precedent
   keeps the demonstrative-headed version possible but unattested.
   Per §4 this is a **null**, not a kill.

## Adverses, answered

- None pre-registered ("Adverses: none listed").
- Self-check: no contradiction with the standing KILL
  (ce87-topic-licensing, bare "ce" cannot head the construction) — this
  battery tested tonic demonstratives only, and the cedilla-less-"ca"
  control came back zero.
- Self-check: no contradiction with the parent NULL
  (disloc-demonstrative-drama) — the bar anticipated exactly this
  outcome ("confirmed zero fences it at quoted-drama level").
- §5.2: no standing red-team verdict touched; no overwrite, no
  escalation required.

## Verdict: NULL (fence per clause 2)

Zero genuine dislocated-demonstrative + bare-exclamatory-infinitive
attestations in ~10.3M characters of quoted dialogue inside
revue-deux-mondes-1841 (3 unique candidates, all classified: 1 noun
appositive, 1 vocative, 1 pronoun interjection; none contains an
infinitive-shaped word). Arm (a) of ce87-1028-role stays fenced — now at
quoted-drama level, alongside the full-corpus fence. Work regenerates
via the follow-ups below.

## Follow-ups (nulls regenerate work)

None of these duplicates a queued target (checked against
battery-queue.json: `disloc-demonstrative-drama-reissue` and
`disloc-demonstrative-drama-reinforced` cover the gated drama-census
re-runs; `disloc-topic-inventory-excl-inf` covers the full-corpus topic
inventory):

1. **disloc-demonstrative-inversion** (P3): invert the tested word order —
   census postposed demonstratives ("[bare inf] !, cela/ceci/ça" e.g.
   "Voler, cela !") in RDM quoted-dialogue windows. If the tonic head
   licenses the pairing from post-topic position, the bar construction
   would never show up in the tested order and the fence is an
   artefact of word order. Bar: ≥1 genuine postposed-demonstrative +
   bare exclamatory infinitive attestation re-opens arm (a) in inverted
   form; confirmed zero fences it.
2. **disloc-demonstrative-drama-dialogue** (P3, GATED on
   disloc-demonstrative-drama-ingest): once the drama corpus lands, run
   the quoted-dialogue census (same D1–D3 extraction, same DEM/INF) on
   the ingested plays only. Dialogue in a play is actual theatre
   speech — if the pairing exists anywhere, it exists there. Bar: ≥1
   genuine attestation in drama dialogue promotes arm (a) as
   drama-specific; confirmed zero fences the family at dialogue level
   across both registers. (Does not duplicate
   disloc-demonstrative-drama-reissue: dialogue-scoped, not full-text.)
3. **quoted-dialogue-goldset** (P3): this run found unmatched quote marks
   producing >20k-char monster spans in the OCR text. Build a
   hand-verified quoted-dialogue gold set (≥200 dialogue spans,
   provenance-noted) from RDM q1 as a control corpus for future
   dialogue-scoped batteries. Bar: gold set lands in the lane corpus
   dir with provenance; ≥200 spans hand-verified as true dialogue.

## Bookkeeping

- Census script:
  code/crowd17/next-token/disloc_demonstrative_quoted_drama_census.py
  (re-runnable; outputs disloc-demonstrative-quoted-drama_census.json
  with per-file sizes, dialogue-span counts, dem-comma hits in
  dialogue, and all 6 candidate windows).
- Report: code/crowd17/report_inbox/battery-disloc-demonstrative-quoted-drama.md
  (this file).
- battery-queue.json: `disloc-demonstrative-quoted-drama` queued ->
  verdict/null via temp-file + rename (pre-write assert confirmed
  queued/verdictless; JSON re-validated post-write; own entry only;
  claim/bars/evidence/adverses preserved).
- Lock created on start (agent id + UTC timestamp), deleted on
  completion.
- R5005, sealed gates, red-team queue untouched. Every number traces to
  the named corpus files or the census script; no invented data.
