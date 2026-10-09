# Battery report: disloc-demonstrative-reinforced

- Target id: `disloc-demonstrative-reinforced`
- Claim: "test reinforced demonstrative heads (celui-la, ceux-la, ca-la)
  + bare exclamatory infinitive in the 27.66M-char corpus"
- Date: 2026-10-09
- Worker: battery worker (subagent 0735664b-1824-4f2c-a431-d821a5657587)
- Stream: not applicable — corpus census against period French, per target
  charter. The 1,847-pair repaired parse was not used. R5005, sealed gate
  instances, and the red-team adjudication queue were not touched.

Terms (ASD-STE100): "dislocation" = a topic moved to the front of the clause,
set off by a pause, and resumed by a pronoun ("Moi, je sais" = "me, I know").
"Tonic" = the stressed form of a pronoun (moi, celui-là). "Exclamatory
infinitive" = an infinitive used as an exclamation ("Moi, me taire !" = "me,
to shut up!"). "Bare" = the infinitive stands alone, with no preposition
(de, pour), no "que", and no resumptive clitic between the topic and the
verb. "Reinforced head" = a demonstrative compound marked with -là or -ci
(celui-là, ceux-là, celle-ci), as opposed to the bare tonic heads
(cela, ceci, ça) tested by disloc-demonstrative-inf.

## Parentage

Follow-up #2 of the NULL `disloc-demonstrative-inf` (2026-10-09). That
battery fenced the bare tonic heads (cela/ceci/ça): 0 genuine attestations
of the dislocated-tonic + bare-exclamatory-infinitive pairing in 27.66M
characters — but its DEM regex excluded là-forms. The parent's working
hypothesis: if the bare tonic head is blocked, the reinforced/là-marked head
may license the pairing. This battery tests that hypothesis. Does not
duplicate `disloc-demonstrative-inf` (different demonstrative inventory),
`disloc-demonstrative-drama` (in-flight sibling; drama corpus family), or
`dislocation-ce-sweep` (about bare atonic "ce").

## Bar (verbatim, pre-registered before testing)

">=1 genuine attestation re-opens the tonic-demonstrative + bare-infinitive
pairing at promote-grade; confirmed zero keeps the whole family fenced"

Numbered pass/fail clauses (restated before testing, not modified after):

1. At least one GENUINE dislocated reinforced-demonstrative head
   (celui-là / ceux-là / ça-là / celle-là / celles-là / celui-ci /
   ceux-ci / celle-ci / celles-ci) + bare exclamatory infinitive
   ("celui-là, [inf] !") exists in the 27.66M-char corpus. If yes: the
   tonic-demonstrative + bare-infinitive pairing re-opens at
   promote-grade (promote).
2. If clause 1's census is a confirmed zero — every candidate window
   classified, false friends and OCR excluded with cause — the whole
   tonic-demonstrative + bare-infinitive family stays fenced (null per §4:
   inconclusive as a kill, since zero is an absence).

## Method

1. Read BATTERY-PROTOCOL.md first. Created the lock
   `code/crowd17/next-token/locks/disloc-demonstrative-reinforced.lock` on
   start (no stale lock for this id existed — the only nearby lock was the
   in-flight sibling `disloc-demonstrative-drama.lock`); deleted on
   completion.
2. Ran a reproducible census script:
   `code/crowd17/next-token/disloc_demonstrative_reinforced_census.py`
   (extends `disloc_demonstrative_census.py`: same corpus, new DEM
   inventory). Raw results in
   `code/crowd17/next-token/disloc-demonstrative-reinforced_census.json`.
3. Corpus, identical to disloc-demonstrative-inf (character counts recomputed
   in-session, matching to the character):
   - 1841-register lane corpus (French files only): 18 files, 25,670,258
     characters — guizot-memoires t1/t2/t3/t5-t6, nesselrode v7/v8/v9/v10,
     revue-deux-mondes-1841 q1/q2/q3/q4, metternich-papiere v4/v6,
     talleyrand-memoires-v1, pozzo-di-borgo-correspondance-v1,
     levant-correspondence-1841-p3.
   - Wider 19th-century register: 3 files, 1,987,682 characters —
     data/gutenberg-17489-miserables1.txt (Les Misérables tome 1, 1862),
     data/gutenberg-30513-tocqueville-t1.txt (Démocratie en Amérique t1,
     1835), data/gutenberg-30514-tocqueville-t2.txt (t2, 1840).
   - Total: 21 files, 27,657,940 characters of 19th-century French.
   - German files excluded with cause (register is French, not 1841 French):
     allgemeine-zeitung-augsburg-1841-01-11 through -01-24 (14 files) and
     adb-zeschau-heinrich-anton-von.txt.
4. Search patterns (verbatim, from the script):
   - P1 (dislocation): `DEM_REINF\s*[,;:]` where DEM_REINF =
     `((?:celui|ceux|celle|celles)[-–— ]?(?:l[àa]|ci)|ça[-–— ]?(?:l[àa]|ci))`,
     case-insensitive — hyphen or space forms of celui-là, ceux-là,
     celle-là, celles-là, celui-ci, ceux-ci, celle-ci, celles-ci, ça-là,
     ça-ci. Window = text from the demonstrative through the next
     sentence-ending `[!?.]`, capped at 180 characters.
   - P2 (exclamatory filter): the window must contain "!" before its end.
     Rationale: the bar construction is a BARE EXCLAMATORY infinitive; a
     window without "!" cannot instantiate it.
   - P3 (infinitive candidate): an infinitive-shaped word
     (`[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)`) inside the window. All
     candidates were classified by hand (regex cannot separate -er
     infinitives from nouns/adjectives in -er).

## Window-level evidence

### Census yields

- 1841 register: 231 reinforced-head-comma hits (206 in 1841 register, 25 in
  wider 19c) → 7 exclamatory candidates (all in the 1841 register; wider
  19c contributed 0).
- **0 of 7 candidates is genuine.** Classification below (windows verbatim;
  "/" marks line breaks in the source):

1. `celle-ci,  je  me  suis  convaincu  qu'il  n'y  a / aucun  inconvénient
   à  en  donner  lecture  in  extenso  ; / qu'il  y  a  même  nécessité  à
   le  faire,  puisqu'il  en  es!` (nesselrode-v10) — finite clause ("je me
   suis convaincu..."); the infinitives "donner" and "faire" are governed
   by the preposition "à". Not a bare infinitive. Excluded with cause.
2. `celle-ci, / de  celle-là,  et  comme  on  a  vite  fait  de  faire
   penser / hommes  et  femmes  sur  toute  chose!` (nesselrode-v8) —
   "faire penser" is governed by "de" ("on a vite fait de faire penser");
   the "!" belongs to the downstream clause, not an exclamatory
   infinitive headed by the topic. Excluded with cause.
3. `celle-là,  et  comme  on  a  vite  fait  de  faire  penser / hommes  et
   femmes  sur  toute  chose!` (nesselrode-v8) — same sentence as #2; the
   topic chain "celle-là, ... de faire penser..." is "de"-governed.
   Excluded with cause.
4. `celle-ci  :  Bon / Dieu ,  béni  sois-tu  pour  m'avoir  donné  de
   bons  yeux!` (revue-deux-mondes-1841-q1) — prayer/vocative after the
   colon; "m'avoir" is a past infinitive governed by "pour". Excluded
   with cause.
5. `celui-ci,  prononcé / en  bon  normand  : // —  Je  pardonne  au
   marin,  c'est  un  brave!` (revue-deux-mondes-1841-q2) — quotation
   introduction ("celui-ci" names the speaker); no infinitive at all.
6. `celle-ci,  qu'elle  se  montre!` (revue-deux-mondes-1841-q3) —
   subjunctive finite clause ("qu'elle se montre"); "montre" is a false
   infinitive-shaped hit anyway. Excluded with cause.
7. `celles-ci  :  «  Cela  est  vrai  !` (revue-deux-mondes-1841-q4) —
   quotation introduction; no verb at all.

### Due-diligence checks

- The reinforced-head inventory is real in this corpus: 231
  DEM_REINF-comma hits, so the zero is not an empty-search artifact — the
  heads exist in topic position, they just never head a bare exclamatory
  infinitive.
- Bare-"ce" re-check inside the same runs: no `ce,` + bare-infinitive +
  "!" windows re-surfaced with reinforced heads — no adverse to the
  standing `ce87-topic-licensing` KILL.
- The nearest shape in the whole corpus remains the bare-head precedent
  "Moi, voler !" (re-derived by disloc-demonstrative-inf): a PERSONAL
  tonic pronoun can head the bare exclamatory infinitive. That keeps this
  a null (not a kill): the construction is grammatical with a tonic topic,
  and the reinforced demonstrative head — the most deictically forceful
  topic of all — fails to license it even once in 27.66M characters.
  The fence now covers bare heads (fenced 2026-10-09) AND reinforced heads
  (fenced here): the whole tonic-demonstrative family is fenced.

## Per-clause pass/fail

1. ≥1 genuine reinforced-head + bare-exclamatory-infinitive attestation in
   the 27.66M-char corpus: **FAIL (confirmed zero).** 7/7 candidates
   classified; 0 genuine in 27,657,940 characters. The reinforced heads
   themselves are frequent (231 hits), so the pairing's absence is a real
   gap, not a corpus gap.
2. Confirmed zero → whole family stays fenced: **EXECUTED.** Zero is an
   absence, not a refutation — the "Moi, voler !" precedent proves the
   shape is grammatical in 1841 French, so the reinforced-headed version
   stays possible-but-unattested. Per §4 this is a **null**, not a kill.

## Adverses, answered

- None pre-registered ("Adverses: none listed").
- Self-check: does this null contradict the parent NULL
  (disloc-demonstrative-inf)? No — the bar anticipated exactly this
  outcome ("confirmed zero keeps the whole family fenced"); the family
  fence is now complete (bare + reinforced heads).
- Self-check: does this null contradict the standing KILL
  (ce87-topic-licensing, bare "ce" cannot head the construction)? No —
  different construction (tonic vs atonic); nothing bare-"ce" surfaced.
- §5.2: no standing red-team verdict touched; no overwrite, no escalation
  required.

## Verdict: NULL (fence per clause 2)

Zero genuine dislocated reinforced-demonstrative + bare-exclamatory-infinitive
attestations in 27.66M characters of 19th-century French (7 candidates all
classified: 3 finite-clause or "de"-/"à"-/"pour"-governed infinitives, 2
quotation introductions, 1 vocative, 1 subjunctive finite clause). The
parent hypothesis — that a reinforced/là-marked head might license what the
bare head blocks — is not supported. Combined with the parent fence on bare
heads, the whole tonic-demonstrative + bare-infinitive family is now fenced.
Work regenerates via the follow-ups below.

## Follow-ups (nulls regenerate work)

1. **disloc-demonstrative-drama-reinforced** (P3): the in-flight sibling
   `disloc-demonstrative-drama` censuses the bare heads in the drama corpus
   (the natural habitat of bare exclamatory infinitives). Extend it to the
   reinforced-head inventory used here (celui-là, ceux-là, celle-là,
   celles-là, celui-ci, ceux-ci, celle-ci, celles-ci). Bar: ≥1 genuine
   reinforced-head attestation in drama re-opens the pairing; confirmed zero
   fences the whole family at drama-register level too. (Coordinates with,
   does not duplicate, the in-flight drama battery: new inventory on a new
   corpus family.)
2. **disloc-topic-inventory-excl-inf** (P3): census ALL bare exclamatory
   infinitives in the 27.66M-char corpus (topic, infinitive, verb-frame)
   and tabulate which topics license them — "Moi, voler !" shows a
   personal tonic pronoun works. Bar: if any non-pronominal topic
   (demonstrative excluded, nouns/others) licenses the bare exclamatory
   infinitive, the demonstrative gap is sampling noise → re-open the
   family; if only personal pronouns do, the fence holds and the residual
   closes. (Discriminating frames; not a re-run of either demonstrative
   census.)
3. **reinforced-pour-inf-diagnostic** (P3): the near-misses across both
   censuses are preposition-governed infinitives (pour/à/de). Test whether
   reinforced heads license the EXCLAMATORY infinitive when the infinitive
   is governed ("celui-là, pour rire !" shape) in the same 27.66M-char
   corpus. Bar: ≥1 genuine attestation pinpoints the fence exactly at the
   BARE infinitive (topic licit, bare construction blocked); confirmed
   zero keeps the whole pairing family fenced. (Narrower bar, different
   construction — not a re-run.)

## Bookkeeping

- Census script: code/crowd17/next-token/disloc_demonstrative_reinforced_census.py
  (re-runnable; extends disloc_demonstrative_census.py; outputs
  disloc-demonstrative-reinforced_census.json with per-file sizes, hit
  counts, and all 7 candidate windows).
- Report: code/crowd17/report_inbox/battery-disloc-demonstrative-reinforced.md
  (this file).
- battery-queue.json: `disloc-demonstrative-reinforced` queued ->
  verdict/null via temp-file + rename (pre-write assert confirmed
  queued/verdictless; JSON re-validated post-write; own entry only;
  claim/bars/evidence/adverses preserved).
- Lock created on start (agent id + UTC timestamp), deleted on completion.
  No stale lock for this target existed.
- R5005, sealed gates, red-team queue untouched. Every number traces to
  the named corpus files or the census script; no invented data.
