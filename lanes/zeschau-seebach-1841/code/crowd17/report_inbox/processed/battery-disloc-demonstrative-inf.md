# Battery report: disloc-demonstrative-inf

- Target id: `disloc-demonstrative-inf`
- Claim: "corpus test for dislocated demonstrative + bare exclamatory infinitive
  in the wider 19th-century register"
- Date: 2026-10-09
- Worker: battery worker (subagent 8c089861-922d-4222-be03-eb137d993267)
- Stream: not applicable — corpus census against period French, per target
  charter. The 1,847-pair repaired parse was not used. R5005, sealed gate
  instances, and the red-team adjudication queue were not touched.

Terms (ASD-STE100): "dislocation" = a topic moved to the front of the clause,
set off by a pause, and resumed by a pronoun ("Moi, je sais" = "me, I know").
"Tonic" = the stressed form of a pronoun (moi, cela, ça). "Clitic" = the
unstressed form (me, ce). "Exclamatory infinitive" = an infinitive used as an
exclamation ("Moi, me taire !" = "me, to shut up!"). "Bare" = the infinitive
stands alone, with no preposition (de, pour), no "que", and no resumptive
clitic between the topic and the verb.

## Parentage

Follow-up #1 of the battery-level NULL `ce87-1028-role` (P3, queued by its
report). That battery's arm (a) combines two attested pieces — tonic
demonstratives own the fronted-topic slot (cela/ceci/ça, 335x), and the shape
precedent "Moi, voler !" shows a dislocated tonic topic + bare exclamatory
infinitive — but the specific DEMONSTRATIVE + bare-infinitive combination is
unattested. This battery tests that combination in the wider register.
Does not duplicate `ceci-1841-corpus` (tests "faire ceci" attestation — a
different construction) or the parent `ce87-topic-licensing` kill (about bare
atonic "ce", not tonic demonstratives).

## Bar (verbatim, pre-registered before testing)

">=1 genuine demonstrative attestation strengthens arm (a) to promote-grade;
confirmed zero keeps it fenced"

Numbered pass/fail clauses (restated before testing, not modified after):

1. At least one GENUINE dislocated-demonstrative + bare-exclamatory-infinitive
   attestation ("cela/ceci/ça, [inf] !") exists in the wider 19th-century
   register. If yes: arm (a) of ce87-1028-role is strengthened to
   promote-grade (promote).
2. If clause 1's census is a confirmed zero — every candidate window
   classified, false friends and OCR excluded with cause — arm (a) stays
   fenced (null per §4: inconclusive as a kill, since zero is an absence).

## Method

1. Read BATTERY-PROTOCOL.md first. Created the lock
   `code/crowd17/next-token/locks/disloc-demonstrative-inf.lock` on start
   (no stale lock for this id existed); deleted on completion.
2. Ran a reproducible census script:
   `code/crowd17/next-token/disloc_demonstrative_census.py`. Raw results in
   `code/crowd17/next-token/disloc-demonstrative-inf_census.json`.
3. Corpus, named with sizes (character counts, computed in-session):
   - 1841-register lane corpus (French files only): 18 files, 25,670,258
     characters — guizot-memoires t1/t2/t3/t5-t6, nesselrode v7/v8/v9/v10,
     revue-deux-mondes-1841 q1/q2/q3/q4, metternich-papiere v4/v6,
     talleyrand-memoires-v1, pozzo-di-borgo-correspondance-v1,
     levant-correspondence-1841-p3.
   - Wider 19th-century register (beyond the lane's 1841 corpus): 3 files,
     1,987,682 characters — data/gutenberg-17489-miserables1.txt (Les
     Misérables tome 1, 1862), data/gutenberg-30513-tocqueville-t1.txt
     (Démocratie en Amérique t1, 1835),
     data/gutenberg-30514-tocqueville-t2.txt (t2, 1840).
   - Total: 21 files, 27,657,940 characters of 19th-century French.
   - German files excluded with cause (register is French, not 1841 French):
     allgemeine-zeitung-augsburg-1841-01-11 through -01-24 (14 files) and
     adb-zeschau-heinrich-anton-von.txt.
4. Search patterns (verbatim, from the script):
   - P1 (dislocation): `DEM\s*[,;:]` where DEM = cela|ceci|ça|cel[àa]|cec[iy],
     case-insensitive. Window = text from the demonstrative through the next
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

- 1841 register: 385 demonstrative-comma hits → 6 exclamatory candidates.
- Wider 19th: 62 demonstrative-comma hits → 9 exclamatory candidates.
- **0 of 15 candidates is genuine.** Classification below (all windows
  shown verbatim; "/" marks line breaks in the source):

1841-register candidates:
1. `cela:  „Ob!` (metternich-papiere-v4) — OCR/noise; German quote follows.
   Excluded with cause.
2. `ceci,  —  Fun  en  de*pit  et  aux  /  depens  de  Fautre!`
   (metternich-papiere-v6) — OCR noise ("Fun"/"Fautre" = German "von"
   misread). Excluded with cause.
3. `cela,  un  vagabondage  éternel ,  sans  but  !`
   (revue-deux-mondes-1841-q1) — noun appositive, no infinitive at all.
4. `cela ,  papa !` (rdm-1841-q4) — vocative noun.
5. `cela,  vous!` (rdm-1841-q4) — pronoun interjection, no verb.
6. `ça,  l'ami!` (rdm-1841-q4) — vocative noun.

Wider-register candidates (all Les Misérables t1, 1862):
7. `cela, mais pour moi, / c'est si loin!` — "c'est" + adjective; no
   infinitive.
8. `Ça, c'est une idée!` — "c'est" + noun; no infinitive.
9. `cela, même pour rire!` — the infinitive "rire" is governed by the
   preposition "pour" (purpose adjunct). This is NOT a bare infinitive;
   the bar construction requires the infinitive to stand bare. Excluded
   with cause (nearest near-miss in the whole census).
10. `cela, elle erre gaîment, la douce / amourette!` — finite clause
    ("elle erre"); "amourette" is a noun in -re, false infinitive-shaped
    hit.
11. `ceci: moi Tholomyès, je suis une illusion; mais elle ne / m'entend
    même pas, la blonde fille des chimères!` — "ceci:" introduces a
    statement with finite clauses; the "!" belongs to a far downstream
    noun phrase after a semicolon/colon chain. Not a dislocated topic
    heading an infinitive.
12. `ceci: "Mon but est atteint!` — quotation introduction; finite.
13. `cela, achève!` — imperative finite verb, not an infinitive.
14. `cela, la chiourme, le carcan, la veste / rouge, la chaîne au pied, la
    fatigue, le cachot, le lit de camp, toutes / ces horreurs connues!` —
    noun enumeration (appositive list); no verb.
15. `ça, je ne peux pas dire, on parle contre moi, / on me dit: répondez!` —
    finite clause ("je ne peux pas dire"); the "!" is a downstream
    imperative.

### Due-diligence checks

- Shape precedent re-derived: "Moi, voler !" confirmed in
  revue-deux-mondes-1841-q1 ("nne impérieusement de se lever et d'aller
  voler. — Moi, voler! répond le bon Charlemagne..."). The tonic-topic +
  bare-exclamatory-infinitive SHAPE is genuinely attested in the 1841
  register — only the demonstrative head is missing. The precedent is the
  thing that makes this null (not kill): the combination is grammatical
  shape-wise, just unattested with a demonstrative head.
- Bare-"ce" check: 0 occurrences of `ce,` + infinitive-shaped word + "!"
  in the same sentence across all 21 files. No adverse to the standing
  `ce87-topic-licensing` KILL (bare "ce" cannot head the construction).

## Per-clause pass/fail

1. ≥1 genuine "cela/ceci/ça, [bare infinitive] !" attestation in the wider
   19th-century register: **FAIL (confirmed zero).** 15/15 candidates
   classified; 0 genuine in 27,657,940 characters (25.67M 1841-register +
   1.99M wider). Nearest near-miss is `cela, même pour rire!` — excluded
   because "pour" governs the infinitive; the bar requires a bare
   infinitive.
2. Confirmed zero → arm (a) stays fenced: **EXECUTED.** Zero is an absence,
   not a refutation — the "Moi, voler !" precedent proves the shape is
   grammatical in 1841 French, so the demonstrative-headed version stays
   possible-but-unattested. Per §4 this is a **null**, not a kill.

## Adverses, answered

- None pre-registered ("Adverses: none listed").
- Self-check: does this null contradict the standing KILL
  (ce87-topic-licensing, bare "ce" cannot head an exclamatory infinitive)?
  No — this battery tested tonic demonstratives, a different construction,
  and independently re-confirmed zero bare-"ce" hits with the "!" filter.
  The kill stands untouched.
- Self-check: does this null contradict the battery-level NULL
  (ce87-1028-role) whose arm (a) it tests? No — the bar anticipated exactly
  this outcome ("confirmed zero keeps it fenced"); arm (a) remains fenced
  as chartered.
- §5.2: no standing red-team verdict touched; no overwrite, no escalation
  required.

## Verdict: NULL (fence per clause 2)

Zero genuine dislocated-demonstrative + bare-exclamatory-infinitive
attestations in 27.66M characters of 19th-century French (15 candidates
all classified: 2 OCR/noise, 13 grammatical false friends — nouns,
vocatives, finite clauses, "pour"-governed infinitives). The shape
precedent "Moi, voler !" keeps the construction possible but unattested;
arm (a) of ce87-1028-role stays fenced. Work regenerates via the follow-ups
below.

## Follow-ups (nulls regenerate work)

1. **disloc-demonstrative-drama** (P3): the exclamatory infinitive is a
   dramatic register form (the one attested precedent is quoted speech in
   RDM). Extend the census to 19th-century French DRAMA (Hugo, Dumas,
   Scribe, vaudeville) — "Moi, me taire !"-type lines suggest theatre is
   the natural habitat of bare exclamatory infinitives. Bar: ≥1 genuine
   "cela/ceci/ça, [bare inf] !" in drama promotes arm (a); confirmed zero
   fences it at drama-register level. (Does not duplicate this battery:
   new corpus family, not a re-run.)
2. **disloc-demonstrative-reinforced** (P3): test the reinforced
   demonstrative heads (celui-là, ceux-là, ça-là) + bare exclamatory
   infinitive in the same 27.66M-char corpus. If the bare tonic head is
   blocked, the reinforced/là-marked head may license the pairing.
   Bar: ≥1 genuine attestation re-opens the tonic-demonstrative +
   bare-infinitive pairing at promote-grade; confirmed zero keeps the
   whole family fenced. (Does not duplicate: different demonstrative
   inventory, this battery's DEM regex excluded là-forms.)
3. **ce01-slot-1029-infinitive-avenue** (P3): if arm (a) stays fenced after
   follow-ups 1–2, the @1028-1040 skeleton's exclamatory-infinitive avenue
   is closed on two fronts (bare-"ce" killed by ce87-topic-licensing;
   tonic-demonstrative fenced here). Commission a replacement-role battery
   for 87@1028 under standing values WITHOUT the infinitive assumption.
   Bar: one grammatical 1841-French parse of @1028-1040, or fence the
   residual. (Coordinates with, does not duplicate, skeleton-1032-revise /
   quice-verb-1024 — this is the post-fence replacement commission.)

Note for the supervisor: follow-ups 1–2 are new corpus/census work
(suggested P3); follow-up 3 is a commission that fires only if 1–2 also
come back fenced — the supervisor may hold it behind the fence of 1–2's
verdicts.

## Bookkeeping

- Census script: code/crowd17/next-token/disloc_demonstrative_census.py
  (re-runnable; outputs disloc-demonstrative-inf_census.json with per-file
  sizes, hit counts, and all 15 candidate windows).
- Report: code/crowd17/report_inbox/battery-disloc-demonstrative-inf.md
  (this file).
- battery-queue.json: `disloc-demonstrative-inf` queued -> verdict/null via
  temp-file + rename (pre-write assert confirmed queued/verdictless; JSON
  re-validated post-write; own entry only; claim/bars/evidence/adverses
  preserved).
- Lock created on start (agent id + UTC timestamp), deleted on completion.
- R5005, sealed gates, red-team queue untouched. Every number traces to
  the named corpus files or the census script; no invented data.
