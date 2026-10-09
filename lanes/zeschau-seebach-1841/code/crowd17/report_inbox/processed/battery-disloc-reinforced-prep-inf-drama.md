# Battery report: disloc-reinforced-prep-inf-drama

- Target id: `disloc-reinforced-prep-inf-drama`
- Claim: "test whether reinforced demonstrative heads license the governed
  exclamatory infinitive in drama ('celui-là, pour rire !')"
- Date: 2026-10-09
- Worker: battery worker (subagent 72db091d-e9b1-45a8-84a6-14a064caeb86)
- Stream: not applicable — corpus census against period French drama, per
  target charter. The 1,847-pair repaired parse was not used. R5005, sealed
  gate instances, and the red-team adjudication queue were not touched.

Terms (ASD-STE100): "dislocation" = a topic moved to the front of the
clause, set off by a pause, and resumed by a pronoun ("Celui-là, je le
sauverai" = "that one, I will save him"). "Reinforced head" = a
demonstrative compound marked with -là or -ci (celui-là, ceux-ci), as
opposed to the bare tonic heads (cela, ceci, ça). "Governed exclamatory
infinitive" = an infinitive led by a preposition (pour, de) that carries
exclamatory force ("celui-là, pour rire !" = "that one — what a laugh !").

## Parentage

Follow-up of the NULL `disloc-demonstrative-drama-reinforced`
(2026-10-09): its drama near-misses were governed (non-exclamatory)
infinitives (candidates 2, 3, 4: "il faut le sauver", "aimerais mieux
mourir", "de les accueillir"). This battery tests the remaining arm —
whether reinforced heads license the EXCLAMATORY infinitive when the
infinitive is governed ("celui-là, pour rire !" shape) — in the same
drama register.

## Gate

Corpus verified on disk before testing: `code/side-period/corpus/`
holds the ingested drama register — 15 files = 14 unique plays
(2,969,582 characters, measured by the census script). ONE edition per
play per the queue corpus note: `hugo-hernani.txt` (Hetzel 1889)
EXCLUDED; `hugo-hernani-1870.txt` (the gate-ingest edition) kept. All
files carry provenance in `code/side-period/corpus/PROVENANCE.md`
(Families 9 + wikisource ingest). Gate NOT rewritten — the bar's corpus
condition ("the ingested drama corpus") is satisfied at full scope.

## Bar (verbatim, pre-registered before testing)

">=1 genuine governed exclamatory infinitive under a reinforced head in
drama pins the fence exactly at BARE; confirmed zero fences the whole
governed family at drama level"

Numbered pass/fail clauses (restated before testing, not modified after):

1. At least one GENUINE governed exclamatory infinitive ("pour/de/à +
   infinitive" with exclamatory illocutionary force, not a plain
   governed infinitive inside a finite or conditional clause) under a
   dislocated reinforced demonstrative head exists in the ingested drama
   corpus. If yes: the fence is pinned exactly at the BARE infinitive —
   the topic is licit, the bare construction is blocked (promote).
2. If clause 1's census is a confirmed zero — every candidate window
   classified, false friends excluded with cause — the whole governed
   family stays fenced at the drama-register level too (null per §4:
   zero is an absence, not a refutation).

## Method

1. Read BATTERY-PROTOCOL.md first. Created the lock
   `code/crowd17/next-token/locks/disloc-reinforced-prep-inf-drama.lock`
   on start (no lock, stale or fresh, existed for this id); deleted on
   completion.
2. Ran a reproducible census script:
   `code/crowd17/next-token/disloc_reinforced_prep_inf_drama_census.py`
   (same P1/P2 taxonomy as the parent's
   `disloc_demonstrative_drama_reinforced_census.py`; P3 narrowed to
   governed infinitives). Raw results in
   `code/crowd17/next-token/disloc-reinforced-prep-inf-drama_census.json`.
3. Search patterns (verbatim, from the script):
   - P1 (dislocation): `DEM_REINF\s*[,;:]` where DEM_REINF =
     `((?:celui|ceux|celle|celles)[-–— ]?(?:l[àa]|ci)|ça[-–— ]?(?:l[àa]|ci))`,
     case-insensitive — hyphen or space forms. Window = text from the
     demonstrative through the next sentence-ending `[!?.]`, capped at
     180 characters.
   - P2 (exclamatory filter): the window must contain "!" before its
     end.
   - P3 (governed-infinitive candidate):
     `\b(?:pour|de|d'|d’|à)\s+[a-zàâäçéèêëîïôöùûü']{2,}(er|ir|re|oir)\b`,
     case-insensitive — a preposition directly followed by an
     infinitive-shaped word inside the window. All candidates classified
     by hand with ±250-char context (regex cannot judge exclamatory
     illocutionary force).
   - Recall-gap control: re-ran with a clitic-tolerant P3 allowing up
     to 2 intervening short words between preposition and infinitive
     (`\b(?:pour|de|d'|d’|à)\s+(?:[a-z…']{1,5}\s+){0,2}[inf]`), catching
     shapes like "de les accueillir".
   - Register positive control: counted bare "pour/de [inf] !"
     occurrences across the corpus (ungoverned-by-head) to prove the
     register has governed-exclamatory infinitives at all.

## Window-level evidence

### Census yields

- 41 reinforced-head-comma hits across the 14 plays (identical to the
  parent census — taxonomy consistent) → strict-P3 (preposition-adjacent
  governed infinitive) candidates: **0**.
- Clitic-tolerant P3 re-run: **1** candidate (scribe-verre-d-eau.txt,
  @36952): "ceux-là, je ne suis pas libre de les accueillir… lui,
  surtout… ancien ministre, je ne puis le voir sans exciter la défiance
  et les plaintes des nouveaux !" — parent-census candidate 4, already
  classified: finite clauses follow; "accueillir" is governed by
  "libre de" inside a finite clause; the "!" belongs to the finite "je ne
  puis … !" clause. The demonstrative is a dislocated topic resumed by
  the clitic "les". **Excluded with cause: not an exclamatory
  infinitive; the "!" is on a finite clause.**
- **0 genuine.** Confirmed zero: both the strict and the clitic-tolerant
  patterns return nothing genuine; the one escapee was already excluded
  with cause by the parent battery.
- Register positive control: the corpus contains 193 "pour/de [inf] !"
  hits (hugo-hernani-1870 16, hugo-burgraves 12, hugo-ruy-blas 13,
  dumas-mariage-louis-xv-1841 4, dumas-antony 6, dumas-henri-iii 6,
  dumas-kean 7, dumas-tour-de-nesle 6, scribe-bertrand-et-raton 17,
  scribe-verre-d-eau 17, labiche-chapeau-de-paille 18,
  labiche-martin-poudre-aux-yeux 14, vigny-chatterton-1835 8,
  musset-comedies-proverbes-1850 49) — the drama register HAS
  governed-exclamatory infinitives; it just never puts one under a
  reinforced demonstrative head.

### Due-diligence checks

- Not an empty-search artifact: 41 reinforced-head topic-position hits
  across all 14 plays; reinforced heads are frequent, they just never
  license the governed-exclamatory infinitive.
- Not a pattern artifact: both strict (preposition-adjacent) and
  clitic-tolerant governed-infinitive patterns were run; only the
  already-excluded parent candidate 4 escapes.
- No standing verdict contradicted (parent NULLs anticipated this arm;
  no red-team verdict touched).

## Per-clause pass/fail

1. ≥1 genuine governed exclamatory infinitive under a reinforced head in
   drama: **FAIL (confirmed zero).** 0 strict + 0 genuine of 1
   clitic-tolerant candidates in 2,969,582 characters; the register
   positive control (193 "pour/de [inf] !") proves the zero is a real
   gap, not a register gap.
2. Confirmed zero → whole governed family fenced at drama-register
   level: **EXECUTED.** Per §4 this is a **null**, not a kill — zero is
   an absence. Combined with the parent battery's bare-infinitive fence,
   the reinforced-demonstrative topic is now fenced for BOTH the bare
   and the governed exclamatory infinitive at drama register: the
   topic is licit in topic position, but it licenses neither
   exclamatory-infinitive shape even once.

## Adverses, answered

- None pre-registered ("Adverses: none listed").
- Self-check: does this null contradict the parent NULL
  (`disloc-demonstrative-drama-reinforced`)? No — it completes the arm
  the parent proposed; the governed-exclamatory shape fails exactly
  where the bare shape failed.
- Self-check: does this null contradict the sibling NULLs (bare-head
  drama fence, prose reinforced fence)? No — consistent: no tonic
  demonstrative head licenses the exclamatory infinitive in any tested
  inventory or register.
- §5.2: no standing red-team verdict touched; no overwrite, no
  escalation required.

## Verdict: NULL (fence per clause 2)

Zero genuine governed exclamatory infinitives under a dislocated
reinforced demonstrative head in 2,969,582 characters of 19th-century
French drama. The governed family is now fenced at drama-register level;
together with the parent battery's bare-infinitive fence, the
reinforced-head + exclamatory-infinitive pairing fails at BOTH
construction shapes. Work regenerates via the follow-ups below.

## Follow-ups (nulls regenerate work)

1. **disloc-governed-excl-prose-recall** (P2): the prose parent battery
   (`disloc-demonstrative-reinforced`, 27.66M chars) ran 231
   reinforced-head-comma hits through the BARE-infinitive taxonomy; its
   governed-infinitive near-misses were excluded by hand without a
   dedicated governed-exclamatory pass. Re-run the governed-exclamatory
   P3 (strict + clitic-tolerant) against the prose dem-comma hit
   inventory. Bar: ≥1 genuine pins the fence at BARE/register boundary;
   confirmed zero fences the governed family in prose too.
2. **personal-tonic-governed-excl-drama** (P2): the surviving
   positive-space question is whether PERSONAL tonic topics license the
   governed exclamatory infinitive in drama ("Moi, pour rire !" shape).
   Census dislocated personal tonic pronouns (moi, toi, lui, elle, nous,
   vous, eux) + governed exclamatory infinitive in the 14-play drama
   register. Bar: ≥1 genuine pins the fence as
   demonstrative-specific; confirmed zero generalizes it to all
   dislocated topics.
3. **reinforced-head-governed-topology-drama** (P3): classify the
   resolutions of ALL 41 drama dem-comma windows (drop the "!" filter)
   to map how reinforced-head topics actually resolve in drama — modal
   frames, "de"-governed infinitives, finite clauses, citations. Bar:
   full-resolution map sharpens the fence statement from "never
   exclamatory" to the precise licit set.

## Bookkeeping

- Census script: code/crowd17/next-token/disloc_reinforced_prep_inf_drama_census.py
  (re-runnable; same P1/P2 taxonomy as
  disloc_demonstrative_drama_reinforced_census.py, P3 narrowed to
  governed infinitives; outputs
  disloc-reinforced-prep-inf-drama_census.json with per-file sizes,
  hit counts, register positive-control counts).
- Report: code/crowd17/report_inbox/battery-disloc-reinforced-prep-inf-drama.md
  (this file).
- battery-queue.json: `disloc-reinforced-prep-inf-drama` queued ->
  verdict/null via temp-file + rename (pre-write assert confirmed
  queued/verdictless; JSON re-validated post-write; own entry only;
  claim/bars/evidence/adverses preserved).
- Lock created on start (agent id + UTC timestamp), deleted on
  completion. No stale lock for this target existed.
- R5005, sealed gates, red-team queue untouched. Every number traces to
  the named corpus files or the census script; no invented data.
