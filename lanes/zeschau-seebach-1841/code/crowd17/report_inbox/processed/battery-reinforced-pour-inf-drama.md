# Battery report: reinforced-pour-inf-drama

- Target id: `reinforced-pour-inf-drama`
- Claim: "run the governed-infinitive search in the drama corpus once ingested"
- Date: 2026-10-09
- Worker: battery worker (subagent d03e1b58-82f4-4016-9fd1-b669924c759b)
- Stream: not applicable — corpus census against period French drama, per
  target charter. The 1,847-pair repaired parse was not used. R5005, sealed
  gate instances, and the red-team adjudication queue were not touched.

Terms (ASD-STE100): "reinforced head" = a demonstrative compound marked
with -là or -ci (celui-là, ceux-là, celle-là, celles-là, celui-ci,
ceux-ci, celle-ci, celles-ci), as opposed to the bare tonic heads (cela,
ceci, ça). "Exclamatory infinitive" = an infinitive used as an
exclamation ("Moi, me taire !" = "me, to shut up!"). "Governed" = the
infinitive is governed by a preposition (pour / à / de), as in
"celui-là, pour rire !". "Genuine attestation" = the reinforced head
actually governs/heads an exclamatory infinitive: the infinitive is the
exclaimed phrase, not embedded in a downstream finite clause.

## Parentage

Follow-up #3 of the NULL `reinforced-pour-inf-diagnostic` (2026-10-09),
which found 0 genuine reinforced-head + governed-exclamatory-infinitive
attestations in 27.66M characters of 19th-century French prose (4
candidates, all classified). This battery runs the SAME governed search
in the newly ingested drama corpus — the theorised natural habitat of
exclamatory infinitives. Does not duplicate `disloc-demonstrative-drama`
(bare tonic heads, drama corpus), `disloc-demonstrative-inf`
(bare heads, bare infinitive, prose), `disloc-demonstrative-reinforced`
(reinforced heads, bare infinitive, prose), or `reinforced-pour-inf-recall`
(same prose corpus, widened recall — this is a new corpus, not a re-run).

## Bar (verbatim, pre-registered before testing)

"same governed-search bars as reinforced-pour-inf-diagnostic, run against
the ingested drama corpus"

Numbered pass/fail clauses (the parent's bars, restated against the drama
corpus before testing, not modified after):

1. At least one GENUINE dislocated reinforced-demonstrative head
   (celui-là / ceux-là / celle-là / celles-là / celui-ci / ceux-ci /
   celle-ci / celles-ci) + governed exclamatory infinitive ("celui-là,
   pour rire !") exists in the drama corpus. If yes: the pairing
   re-opens at register level (promote).
2. If clause 1's census is a confirmed zero — every candidate window
   classified, false friends and OCR excluded with cause — the whole
   reinforced-head + exclamatory-infinitive pairing is fenced across
   BOTH registers (null per §4: zero is an absence, not a refutation).

## Method

1. Read BATTERY-PROTOCOL.md first. Created the lock
   `code/crowd17/next-token/locks/reinforced-pour-inf-drama.lock` on start
   (agent id + UTC timestamp; no lock, stale or fresh, existed for this
   id); deleted on completion.
2. Gate check: the queue evidence claimed "drama corpus ingested
   (11 files, 1,573,255 chars, commit 517a0075)". Verified on disk:
   PROVENANCE.md Family 9 (archive.org ingest, 4 files) plus the
   wikisource ingest (11 files, 1,573,255 characters by Python count —
   matches the queue note). All 14 distinct-play files present.
3. Ran a reproducible census script:
   `code/crowd17/next-token/reinforced_pour_inf_drama_census.py`
   (SAME DEM_REINF inventory and SAME P1/P2/P3 patterns as
   reinforced_pour_inf_diagnostic_census.py; new corpus list only).
   Raw results in
   `code/crowd17/next-token/reinforced-pour-inf-drama_census.json`.
4. Corpus, with provenance (PROVENANCE.md, Family 9 + wikisource Family):
   - archive.org OCR: dumas-mariage-louis-xv-1841.txt (Un mariage sous
     Louis XV, comédie 1841), vigny-chatterton-1835.txt (Chatterton),
     musset-comedies-proverbes-1850.txt (10 plays incl. Lorenzaccio,
     Le Chandelier, On ne badine pas avec l'amour).
   - wikisource: hugo-hernani.txt (Hernani, Hetzel 1889 — ONE Hernani
     edition; hugo-hernani-1870.txt excluded per one-edition-per-play),
     hugo-ruy-blas.txt, hugo-burgraves.txt, dumas-antony.txt,
     dumas-tour-de-nesle.txt, dumas-henri-iii.txt, dumas-kean.txt,
     scribe-bertrand-et-raton.txt, scribe-verre-d-eau.txt,
     labiche-chapeau-de-paille.txt, labiche-martin-poudre-aux-yeux.txt.
   - Total census: 14 files, 2,939,372 characters of 19th-century
     French drama (14 distinct plays; Musset volume holds 10 plays).
5. Search patterns (verbatim, identical to the diagnostic battery):
   - P1 (dislocation): DEM_REINF =
     `((?:celui|ceux|celle|celles)[-–— ]?(?:l[àa]|ci)|ça[-–— ]?(?:l[àa]|ci))`,
     case-insensitive, followed by `[,;:]`. Window = text from the
     demonstrative through the next sentence-ending `[!?.]`, capped at
     180 characters.
   - P2 (exclamatory filter): the window must contain "!" before its end.
   - P3 (governed-infinitive candidate): `\b(pour|à|a|de|d['’])\s+
     (?:[a-zàâäçéèêëîïôöùûü'-]{1,6}\s+){0,2}
     \b[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b` applied to the window
     text AFTER the comma, case-insensitive. The single candidate was
     classified by hand against the full-line context.

## Window-level evidence

### Census yields

- Drama register: 41 dem-comma hits across 14 files → **1**
  governed-infinitive exclamatory candidate → **0 genuine**.
- Per-file dem-comma hits: musset-comedies-proverbes-1850 11,
  hugo-ruy-blas 6, dumas-tour-de-nesle 6, dumas-kean 4,
  scribe-verre-d-eau 3, hugo-burgraves 2, dumas-mariage-louis-xv-1841 2,
  vigny-chatterton-1835 2, scribe-bertrand-et-raton 2, dumas-antony 1,
  dumas-henri-iii 1, labiche-chapeau-de-paille 1, hugo-hernani 0,
  labiche-martin-poudre-aux-yeux 0.
- The reinforced-head inventory is real in drama: 41 dem-comma hits,
  so the zero is not an empty-search artifact — the heads exist in
  topic position; they never head an exclamatory infinitive.

### The single candidate, classified

1. scribe-verre-d-eau.txt, char offset 36952 (line 525):
   `ceux-là, je ne suis pas libre de les accueillir… lui, surtout…
   ancien ministre, je ne puis le voir sans exciter la défiance et
   les plaintes des nouveaux !`
   — "ceux-là," is a dislocated topic resumed by the clitic "les"
   ("de les accueillir" = to welcome THEM). The infinitive
   "accueillir" is "de"-governed but embedded in the finite negative
   clause "je ne suis pas libre de les accueillir" — it is not an
   exclamatory infinitive ("Moi, me taire !" shape). The "!"
   terminates the whole sentence; the head does not govern an
   exclaimed infinitive. Near-miss (topic + governed infinitive in
   the same sentence), not genuine. Excluded with cause.

### Due-diligence checks

- Excluded-edition spot-check: `hugo-hernani-1870.txt` (second Hernani
  edition, excluded per one-edition-per-play) was run through the same
  search: 0 dem-comma hits → 0 candidates. The edition choice hides
  nothing.
- Recall-gap audit: 6 of the 41 dem-comma hits have no sentence-end
  within the 180-char cap (they were still searched through P2/P3 on
  the full 180-char segment — not dropped). Same fenced limitation as
  the parent: a governed exclamatory infinitive beyond 180 chars, or
  a dash/parenthesis-delimited dislocation ("celui-là — pour rire !"),
  falls outside this census. These are unsearched windows, not
  zero-evidence; follow-up #2 closes them.
- Register positive control (from the drama-ingest battery): drama
  DOES use bare exclamatory infinitives — Hernani "Gouverner tout
  cela !" — but with the demonstrative as OBJECT after the infinitive,
  never as a fronted topic. The register has the infinitive shape;
  it does not pair it with a reinforced-demonstrative topic.

## Per-clause pass/fail

1. ≥1 genuine reinforced-head + governed-exclamatory-infinitive
   attestation in the 2.94M-char drama corpus: **FAIL (confirmed
   zero).** 1/1 candidate classified; 0 genuine in 2,939,372 characters.
2. Confirmed zero → pairing fenced across both registers:
   **EXECUTED.** The zero is specific to the HEAD licensing: reinforced
   heads occur in topic position in drama (41 hits) and exclamatory
   infinitives occur in drama (Hernani positive control), but they never
   pair. Prose (0/27.66M) + drama (0/2.94M) = 30.6M characters with no
   genuine attestation. Per §4 this is a **null**, not a kill.

## Adverses, answered

- None pre-registered ("Adverses: null").
- Self-check: does this null contradict the parent NULL
  (reinforced-pour-inf-diagnostic)? No — it completes the two-register
  program the parent's follow-up #3 commissioned: the pairing is now
  fenced in prose AND drama.
- Self-check: does it contradict the sibling NULL
  `disloc-demonstrative-drama` (bare tonic heads, drama, 0 genuine)?
  No — different head inventory (reinforced vs bare); the fence is
  consistent across both head classes.
- Self-check: does it contradict the in-flight
  `reinforced-pour-inf-recall` (recall-gap re-run on prose)? No —
  this battery runs the diagnostic's exact search on a NEW corpus; the
  recall battery closes search gaps in the OLD corpus. Complementary,
  not duplicative.
- §5.2: no standing red-team verdict touched; no overwrite, no
  escalation required.

## Verdict: NULL (pairing fenced across both registers per clause 2)

Zero genuine dislocated reinforced-demonstrative + governed exclamatory
infinitive attestations in 2.94M characters of 19th-century French drama
(1/1 candidate classified: dislocated topic resumed by clitic inside a
finite clause — the "de"-governed infinitive is not the exclaimed
phrase). Combined with the parent battery: 0 genuine in 30.6M
characters of 19th-century French across prose and drama. The
"celui-là, pour rire !" shape is unattested in both registers; the
whole reinforced-head + exclamatory-infinitive pairing stays fenced.
Work regenerates via the follow-ups below.

## Follow-ups (nulls regenerate work)

1. **reinforced-pour-inf-drama-recall** (P2/P3): close the two recall
   gaps INSIDE the drama corpus this battery fenced — admit
   dash/parenthesis pause marks after the head ("celui-là — pour
   rire !"; P1 currently only [,;:]) and re-search the 6 uncapped
   windows with a longer window. Bar: ≥1 genuine attestation in the
   widened drama search re-opens the pairing; confirmed zero closes
   the recall gap in drama and hardens the cross-register fence.
   (Different search, not a re-run — targets unsearched windows only.)
2. **gov-excl-inf-register-drama** (P3): corpus-wide census of governed
   exclamatory infinitives ("pour rire !", "à donner lecture !", "de
   croire !") with ANY topic in the same 14-play drama corpus, pairing
   the prose-side `gov-excl-inf-register` arm. Bar: if the construction
   is unattested drama-wide, the zero here is register-level (the
   construction itself is absent from drama print, so head-licensing
   is moot); if it attests with other topics, the demonstrative-head
   gap is specific and the cross-register fence stands. (Coordinates
   with, does not duplicate, `gov-excl-inf-register`.)
3. **reinforced-head-topology-drama** (P3): syntactic census of the 41
   dem-comma topic windows in drama — how do reinforced heads in
   topic position actually resolve (finite clause? clitic resumption?
   quotation introduction?). The drama battery gives a real sample
   (41 hits vs the prose 231). Bar: if ≥2 windows show a reinforced
   head licensing a governed infinitive as a COMPLEMENT (not an
   exclamation), the licensing question reframes from "never governs
   infinitives" to "governs, but never exclamatory" — a sharper fence
   with a stated positive boundary. (Discriminating frames; sharpens
   the fenced claim instead of just re-testing it.)

## Bookkeeping

- Census script:
  code/crowd17/next-token/reinforced_pour_inf_drama_census.py
  (re-runnable; same DEM_REINF inventory and P1/P2/P3 as
  reinforced_pour_inf_diagnostic_census.py; outputs
  reinforced-pour-inf-drama_census.json with per-file sizes, hit
  counts, and the single candidate window).
- Report: code/crowd17/report_inbox/battery-reinforced-pour-inf-drama.md
  (this file).
- battery-queue.json: `reinforced-pour-inf-drama` queued -> verdict/null
  via temp-file + rename (pre-write assert confirmed queued/verdictless;
  JSON re-validated post-write; own entry only; claim/bars/evidence/
  adverses preserved).
- Lock created on start (agent id + UTC timestamp), deleted on
  completion. No stale lock for this target existed.
- R5005, sealed gates, red-team queue untouched. Every number traces
  to the named corpus files or the census script; no invented data.
