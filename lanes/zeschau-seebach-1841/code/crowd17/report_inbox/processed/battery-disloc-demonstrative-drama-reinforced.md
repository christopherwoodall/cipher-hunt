# Battery report: disloc-demonstrative-drama-reinforced

- Target id: `disloc-demonstrative-drama-reinforced`
- Claim: "extend the drama census to the reinforced-head inventory (celui-la,
  ceux-la, celle-la, celles-la, celui-ci, ceux-ci, celle-ci, celles-ci)"
- Date: 2026-10-09
- Worker: battery worker (subagent 2411173d-b805-4dc7-96db-45e05b0c5a7a)
- Stream: not applicable — corpus census against period French drama, per
  target charter. The 1,847-pair repaired parse was not used. R5005, sealed
  gate instances, and the red-team adjudication queue were not touched.

Terms (ASD-STE100): "dislocation" = a topic moved to the front of the clause,
set off by a pause, and resumed by a pronoun ("Celui-là, je le sauverai" =
"that one, I will save him"). "Reinforced head" = a demonstrative compound
marked with -là or -ci (celui-là, ceux-ci), as opposed to the bare tonic
heads (cela, ceci, ça). "Bare exclamatory infinitive" = an infinitive used as
an exclamation with no preposition (de, pour), no "que", and no governing
verb between the topic and the verb ("Moi, voler !" = "me, steal !").

## Parentage

Follow-up of the NULL `disloc-demonstrative-reinforced` (2026-10-09, this
morning), which fenced the reinforced-head inventory in the 27.66M-char
prose corpus (231 reinforced-head-comma hits; 0 genuine in 27,657,940
chars). Its follow-up #1 chartered this battery: run the SAME reinforced
inventory and classification taxonomy against the newly ingested drama
corpus — the natural habitat of bare exclamatory infinitives (Hernani:
"Gouverner tout cela ! — Monter, si l'on vous nomme !"). Does not duplicate
the sibling drama batteries (`disloc-demonstrative-drama` bare heads,
`disloc-demonstrative-quoted-drama` bare heads in dialogue): different
demonstrative inventory, same corpus family.

## Gate

Gate per queue evidence: drama corpus ingested (11 files, 1,573,255 chars,
commit 517a0075). VERIFIED ON DISK, then corrected: the queue note's
"11 files, 1,573,255 chars" counts only the wikisource batch (PROVENANCE.md:
"Total wikisource drama ingest: 1,658,808 bytes (1,573,255 characters by
Python count) across 11 files"). Combined with the archive.org Family 9
batch (1,598,104 bytes), the lane holds **15 French drama files = 14 unique
plays** — Hernani in two editions (`hugo-hernani-1870.txt`, Jenkins 1870;
`hugo-hernani.txt`, Hetzel 1889). Per the queue's corpus note and
PROVENANCE.md, ONE edition per play was used: `hugo-hernani.txt` (Hetzel
1889) EXCLUDED; `hugo-hernani-1870.txt` (the gate-ingest edition) kept. All
15 files carry provenance (source URL, retrieval time/method, sha256) in
`code/side-period/corpus/PROVENANCE.md` ("Family 9" and "wikisource ingest"
sections). Gate NOT rewritten — it only grew, and the bar's corpus condition
("the ingested drama corpus") is satisfied by the full register.

## Bar (verbatim, pre-registered before testing)

">=1 genuine reinforced-head attestation in drama re-opens the pairing;
confirmed zero fences the whole family at drama-register level too"

Numbered pass/fail clauses (restated before testing, not modified after):

1. At least one GENUINE dislocated reinforced-demonstrative head
   (celui-là / ceux-là / celle-là / celles-là / celui-ci / ceux-ci /
   celle-ci / celles-ci) + bare exclamatory infinitive
   ("celui-là, [inf] !") exists in the ingested drama corpus. If yes: the
   tonic-demonstrative + bare-infinitive pairing re-opens (promote).
2. If clause 1's census is a confirmed zero — every candidate window
   classified, false friends excluded with cause — the whole
   tonic-demonstrative + bare-infinitive family stays fenced at the
   drama-register level too (null per §4: inconclusive as a kill, since
   zero is an absence).

## Method

1. Read BATTERY-PROTOCOL.md first. Created the lock
   `code/crowd17/next-token/locks/disloc-demonstrative-drama-reinforced.lock`
   on start (no lock, stale or fresh, existed for this id); deleted on
   completion.
2. Ran a reproducible census script:
   `code/crowd17/next-token/disloc_demonstrative_drama_reinforced_census.py`
   (same reinforced-head inventory and taxonomy as the parent's
   `disloc_demonstrative_reinforced_census.py`; corpus switched to the 14
   unique drama plays). Raw results in
   `code/crowd17/next-token/disloc-demonstrative-drama-reinforced_census.json`
   (per-file sizes, hit counts, all 8 candidate windows).
3. Corpus (14 unique plays, 2,969,582 characters, measured by the script):
   hugo-hernani-1870.txt (203,769), hugo-burgraves.txt (151,408),
   hugo-ruy-blas.txt (198,265), dumas-mariage-louis-xv-1841.txt (204,641),
   dumas-antony.txt (102,234), dumas-henri-iii.txt (128,462),
   dumas-kean.txt (152,233), dumas-tour-de-nesle.txt (132,586),
   scribe-bertrand-et-raton.txt (182,448), scribe-verre-d-eau.txt (146,451),
   labiche-chapeau-de-paille.txt (118,567),
   labiche-martin-poudre-aux-yeux.txt (87,042),
   vigny-chatterton-1835.txt (188,780),
   musset-comedies-proverbes-1850.txt (972,696; 10 plays).
   Excluded with cause: hugo-hernani.txt (Hetzel 1889; duplicate Hernani
   edition — one edition per play per queue note); all German newspaper
   files (wrong language/register).
4. Search patterns (verbatim, from the script — same as the parent's):
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
     candidates were classified by hand with ±250-char context (regex
     cannot separate -er infinitives from nouns/adjectives in -er).

## Window-level evidence

### Census yields

- 41 reinforced-head-comma hits across the 14 plays → 8 exclamatory
  candidates (2,969,582 characters).
- **0 of 8 candidates is genuine.** Classification below (windows verbatim;
  "/" marks line breaks in the source):

1. `ceux-là, morbleu !` (dumas-henri-iii.txt) — "Quant à ceux-là, morbleu !
   j'ai fait une croix blanche sur leur porte..." Topic + interjection,
   then a FINITE clause ("j'ai fait"); no infinitive at all. Excluded
   with cause.
2. `celui-là, il faut le sauver… Oh !` (dumas-tour-de-nesle.txt) — "il
   faut le sauver": the infinitive "sauver" is governed by the modal "il
   faut", not bare, and is not headed by the demonstrative (resumed "le"
   object). Excluded with cause: governed infinitive, finite modal
   frame.
3. `ceux-là, et, s'il fallait les perdre ou les voir compromis…
   j'aimerais mieux mourir !` (scribe-bertrand-et-raton.txt) — "ceux-là"
   resumes "mon honneur, ma réputation" ("je n'ai plus que ceux-là");
   the "!" belongs to "j'aimerais mieux mourir !" where "mourir" is
   governed by "aimerais". Excluded with cause: the exclamatory infinitive
   is not headed by the dislocated demonstrative; it is governed by the
   conditional verb.
4. `ceux-là, je ne suis pas libre de les accueillir… lui, surtout…
   ancien ministre, je ne puis le voir sans exciter la défiance et les
   plaintes des nouveaux !` (scribe-verre-d-eau.txt) — finite clauses
   follow; "accueillir"/"voir" are governed ("de", "pouvoir"); the "!"
   belongs to the finite "je ne puis" clause. Excluded with cause.
5. `celui-là, j'en suis sûre… Et la reine jusque-là froide et sévère, a
   dit, d'un air de bonté : N'en parlons plus, qu'elle vienne !`
   (scribe-verre-d-eau.txt) — "Oh ! celui-là, j'en suis sûre" is a finite
   clause; the "!" belongs to the quoted subjunctive "qu'elle vienne".
   Excluded with cause: no infinitive; "!" is subjunctive, not an
   exclamatory infinitive.
6. `celle-ci, pleine de jeunes gens, / de valets!` (musset-comedies-
   proverbes-1850.txt) — "une maison comme celle-ci": the demonstrative
   sits inside a prepositional phrase; the "!" ends an adjectival
   exclamation ("pleine de jeunes gens, de valets!"). No infinitive at
   all. Excluded with cause.
7. `celui-ci : Cordiani !` (musset-comedies-proverbes-1850.txt) —
   "...qu'on me réponde par celui-ci : Cordiani !" Naming/introduction
   with colon; "Cordiani" is a proper noun. Excluded with cause: no verb
   at all.
8. `celui-là : Je peux si je veux!` (musset-comedies-proverbes-1850.txt) —
   "quel mot que celui-là : Je peux si je veux !" The demonstrative is
   anaphoric to "quel mot" and the "word" is quoted; a finite clause
   follows. Excluded with cause: no infinitive; citation construction.

### Due-diligence checks

- The reinforced-head inventory is real in drama: 41 DEM_REINF-comma
  hits across all 14 plays (Musset 11, Scribe 5, Hugo 8, Dumas 15, Vigny
  2, Labiche 1), so the zero is not an empty-search artifact — the heads
  exist in topic position, they just never head a bare exclamatory
  infinitive.
- The register has the infinitive construction: Hernani's "Gouverner tout
  cela ! — Monter, si l'on vous nomme !" (bare exclamatory infinitives,
  demonstrative as OBJECT). The register has the topic shape; it never
  combines them with a reinforced head.
- The near-misses are all preposition/modal/conditional-governed
  infinitives (candidates 2, 3, 4) or finite/nominal constructions
  (1, 5, 6, 7, 8) — exactly the parent-census failure taxonomy, now at
  drama register.

## Per-clause pass/fail

1. ≥1 genuine reinforced-head + bare-exclamatory-infinitive attestation in
   the drama corpus: **FAIL (confirmed zero).** 8/8 candidates classified;
   0 genuine in 2,969,582 characters. The reinforced heads themselves are
   frequent (41 topic-position hits), so the pairing's absence is a real
   gap, not a corpus gap.
2. Confirmed zero → whole family stays fenced at drama-register level:
   **EXECUTED.** Zero is an absence, not a refutation — the register's own
   bare exclamatory infinitives ("Gouverner tout cela !") prove the shape
   is grammatical in drama, and the reinforced demonstrative head — the
   most deictically forceful topic of all — fails to license it even once.
   Per §4 this is a **null**, not a kill.

## Adverses, answered

- None pre-registered ("Adverses: none listed").
- Self-check: does this null contradict the sibling NULL
  (`disloc-demonstrative-drama` bare heads in drama, confirmed zero)?
  No — the bar anticipated exactly this outcome; the family fence is now
  complete at drama-register level (bare + reinforced heads).
- Self-check: does this null contradict the parent NULL
  (`disloc-demonstrative-reinforced`, 27.66M-char prose)? No — same fence,
  new register.
- Self-check: does this null contradict the standing KILL
  (ce87-topic-licensing, bare "ce" cannot head the construction)? No —
  different inventory (tonic vs atonic); nothing bare-"ce" surfaced.
- Queue-count correction: the queue evidence's "11 files, 1,573,255 chars"
  is the wikisource batch only; the full ingested drama register is 15
  files / 14 unique plays / 2,969,582 chars (measured). The census covers
  all of it; the gate is satisfied, not rewritten.
- §5.2: no standing red-team verdict touched; no overwrite, no escalation
  required.

## Verdict: NULL (fence per clause 2)

Zero genuine dislocated reinforced-demonstrative + bare-exclamatory-infinitive
attestations in 2,969,582 characters of 19th-century French drama (8
candidates all classified with cause: 2 modal/conditional-governed
infinitives, 2 preposition-governed infinitives, 1 finite clause with
interjection, 1 quotation introduction, 1 adjectival exclamation, 1 quoted
subjunctive). The parent hypothesis — that the drama register might
license what prose blocks — is not supported. Combined with the sibling
bare-head drama fence, the whole tonic-demonstrative + bare-infinitive
family is now fenced at the drama-register level. Work regenerates via the
follow-ups below.

## Follow-ups (nulls regenerate work)

1. **disloc-tonic-personal-census** (P3): the surviving positive space is
   the personal tonic pronouns — "Moi, voler !" (parent battery precedent)
   proves a PERSONAL tonic topic licenses the bare exclamatory infinitive.
   Census dislocated personal tonic pronouns (moi, toi, lui, elle, nous,
   vous, eux) + bare exclamatory infinitive across the full drama register
   (14 plays, 2,969,582 chars). Bar: ≥1 genuine attestation per pronoun
   pins the licensor class to personal pronouns; confirmed zero for a
   pronoun fences it too. (Positive-space census; not a re-run of either
   demonstrative inventory.)
2. **disloc-reinforced-prep-inf-drama** (P3): the drama near-misses are
   governed infinitives (candidates 2, 3, 4: "il faut le sauver", "aimerais
   mieux mourir", "de les accueillir"). Test whether reinforced heads
   license the EXCLAMATORY infinitive when the infinitive is GOVERNED
   ("celui-là, pour rire !" shape) in the same drama register. Bar: ≥1
   genuine attestation pinpoints the fence exactly at the BARE infinitive
   (topic licit, bare construction blocked); confirmed zero extends the
   fence to governed-exclamatory. (Narrower bar, different construction —
   not a re-run.)
3. **disloc-reinforced-comedy-extension** (P3): Scribe contributes the
   only infinitive-rich near-misses (2 of 3), while Labiche comedies show
   only 1 reinforced-head-comma hit total. Census the reinforced-head +
   bare-exclamatory-infinitive pairing in remaining public-domain
   Scribe/Labiche comedy on fr.wikisource (same harvest method as the
   wikisource ingest, provenance per Family 9 rules). Bar: ≥1 genuine
   re-opens at the comedy-register level; confirmed zero closes it.
   (Fresh surface, not a re-run.)

## Bookkeeping

- Census script: code/crowd17/next-token/disloc_demonstrative_drama_reinforced_census.py
  (re-runnable; same taxonomy as disloc_demonstrative_reinforced_census.py;
  outputs disloc-demonstrative-drama-reinforced_census.json with per-file
  sizes, hit counts, and all 8 candidate windows).
- Report: code/crowd17/report_inbox/battery-disloc-demonstrative-drama-reinforced.md
  (this file).
- battery-queue.json: `disloc-demonstrative-drama-reinforced` queued ->
  verdict/null via temp-file + rename (pre-write assert confirmed
  queued/verdictless; JSON re-validated post-write; own entry only;
  claim/bars/evidence/adverses preserved).
- Lock created on start (agent id + UTC timestamp), deleted on completion.
  No stale lock for this target existed.
- R5005, sealed gates, red-team queue untouched. Every number traces to
  the named corpus files or the census script; no invented data.
