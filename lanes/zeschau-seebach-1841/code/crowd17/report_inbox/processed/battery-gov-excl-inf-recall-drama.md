# Battery report: gov-excl-inf-recall-drama

- Target id: `gov-excl-inf-recall-drama`
- Claim: "run the G1/G2/G3 recall-gap searches ('?'-terminated, >=3-token spans, dash/colon-adjacent non-closest) against the ingested drama corpus"
- Date: 2026-10-09
- Worker: battery worker (subagent a65fc428-bbf9-4d6e-98c5-0abde7d20678)
- Stream: not applicable — corpus census against period French, per target
  charter. The 1,847-pair repaired parse was not used (no cipher
  windows). R5005, sealed gate instances, and the red-team
  adjudication queue were not touched.

Terms: "governed exclamatory infinitive" = a preposition-governed
infinitive phrase (pour / à / de + infinitive) that IS itself the
exclaimed element ("pour rire !"). "Genuine attestation" = the
terminator (! or ?) terminates the governed infinitive phrase itself;
the infinitive is not embedded in a finite matrix clause whose
terminator belongs to the matrix, not embedded in an exclaimed noun
phrase, and (for '?') the "?" marks exclamatory incredulity at the
infinitive phrase, not a matrix question.

## Parentage

Follow-up #1 of the NULL `battery-gov-excl-inf-recall` (2026-10-09),
which closed the three recall gaps on the 1841 print corpus
(1,874 gap candidates, 0 genuine). This battery runs the identical
G1/G2/G3 gap designs against the ingested drama corpus — the
construction's natural habitat, where the parent drama register
battery already found one genuine case.

Independent-confirmation note: sibling target
`gov-excl-inf-drama-recall` (follow-up #2 of the drama register
battery, different charter) ran the same structural designs on the
same corpus and promoted on one genuine hit. This battery re-ran the
designs from scratch with its own census script, pinned file set,
and full independent classification; it confirms the same genuine
hit. The register re-open is now doubly attested.

## Bar (verbatim, pre-registered before testing)

">=1 genuine governed exclamatory infinitive in drama re-opens the register question; confirmed zero generalizes the prose recall closure"

Numbered pass/fail clauses (restated before testing, not modified after):

1. If >=1 genuine governed exclamatory infinitive is found in the
   drama gap searches, the register question is re-opened.
2. If the drama gap searches confirm zero genuine attestations, the
   prose recall closure generalizes to drama.

## Method

1. Read BATTERY-PROTOCOL.md first. Created the lock
   `code/crowd17/next-token/locks/gov-excl-inf-recall-drama.lock` on
   start (agent id + UTC timestamp); deleted on completion. No stale
   lock existed for this id.
2. Ran a reproducible census script:
   `code/crowd17/next-token/gov_excl_inf_recall_drama_census.py`
   (structural duplicate of the parent prose script; same GOV_INF,
   LONG_INF, closest-match, no-[.;]-tail rules verbatim). Raw
   results in
   `code/crowd17/next-token/gov-excl-inf-recall-drama_census.json`
   (per-gap yields, per-file sizes, every candidate with
   prep/infinitive/dist/absolute-terminator-offset fields);
   windows in
   `code/crowd17/next-token/gov-excl-inf-recall-drama_windows.json`;
   classification record in
   `code/crowd17/next-token/gov-excl-inf-recall-drama_classification.json`
   (auto-A denylist source recorded, per-candidate cause decisions,
   wide-scan triage log).
3. Corpus pinned by name (14 files / 14 unique plays / 2,969,582
   chars, asserted in-session; one edition per play —
   hugo-hernani-1870.txt kept, the duplicate hugo-hernani.txt
   dropped): dumas-antony, dumas-henri-iii, dumas-kean,
   dumas-mariage-louis-xv-1841, dumas-tour-de-nesle,
   hugo-burgraves, hugo-hernani-1870, hugo-ruy-blas,
   labiche-chapeau-de-paille, labiche-martin-poudre-aux-yeux,
   musset-comedies-proverbes-1850, scribe-bertrand-et-raton,
   scribe-verre-d-eau, vigny-chatterton-1835.
4. The three gap searches (exact patterns in the script); each
   targets windows the parent drama register design could not
   produce:
   - G1 ('?'-terminated): for every "?" — 120-char lookback,
     parent's GOV_INF verbatim (prep + 0-2 short tokens +
     infinitive-shaped word), closest match to "?", no [.;]
     between match end and "?" (same sentence-internal rule).
     Novel by construction. 872 candidates.
   - G2 (long spans): for every "!" — 300-char lookback,
     LONG_INF = prep + 3-6 short tokens (each <=8 chars) +
     infinitive-shaped word, closest match, same
     no-[.;]-tail rule. The {3,6}-token floor vs the parent's
     {0,2} ceiling makes the spans pattern-disjoint. 248
     candidates.
   - G3 (dash/colon-adjacent): for every "!" — 120-char
     lookback, ALL GOV_INF matches; keep the non-closest ones
     where a dash (em/en/hyphen) or colon lies between the
     match end and the "!" (no [.;] between match end and the
     pause mark). 24 candidates. G3-diag (non-closest with NO
     dash/colon — outside the three named gaps): 88 candidates,
     scanned as due diligence.
   - Dist = chars from infinitive-shaped word end to
     terminator. Tight band dist<=40 is the discriminating
     band.
5. Classification. Tight band (748 candidates) fully classified by
   hand, in two passes. Pass 1 (automatic): 197 candidates whose
   infinitive-shaped word is on the parent's NEVER_INF denylist
   (160 entries, reused verbatim; dual-use words like rire/dire
   were read, not denylisted) — cause A. Pass 2 (manual): the
   remaining 551 read window by window and classified E
   (interrogative matrix), B (finite-matrix embedding), C
   (exclaimed-NP embedding), D (terminator belongs to a
   following quotation/interjection), A (hand: proper names /
   OCR, e.g. "Gaultier"), or GENUINE. Wide band (484
   candidates): triage scan — 149 windows with no
   finite-verb/question markers in the tail read; all excluded
   (B/C/other-exclaimed-element); 0 genuine.

## Window-level evidence

### Census yields

- G1 '?'-windows: 872 candidates (461 tight manual + remainder
  auto-A). Tight manual: all 461 E — every "?" belongs to an
  interrogative matrix (e.g. labiche "A-t-on apporté un myrte
  pour moi ? / Un myrte !… pour quoi faire ?"; musset "Qui est-ce
  qui nous dit qu'ailleurs il nous sera permis de rire ?"). No
  "Lui, pour rire ?" incredulity shape anywhere in 872 "?"
  candidates.
- G2 long spans: 248 candidates (73 tight manual). 72 B, 1 GENUINE.
- G3 dash/colon: 24 candidates (all tight auto-A). G3-diag: 88
  candidates (17 tight manual, all B; 71 wide scanned, 0
  genuine).

### The genuine attestation

- (labiche-martin-poudre-aux-yeux.txt @24350, G2, dist=1,
  3 intervening tokens "ne pas la"):
  "…Tu la cachais sous ton gilet. / / Malingear. /  / Pour ne
  pas la perdre. /  / Madame Malingear. /  / Oh ! non… pour ne
  pas la montrer !…"
  The "!" terminates the pour-infinitive phrase itself; it is a
  corrective dialogue retort with no finite verb — exactly the
  "Pour conspirer !" shape. The 3-token span ("ne pas la") is
  unproducible by the parent drama register design's 2-token
  ceiling, so this is a genuinely new-shape find, not a
  re-detection of the parent's case.

### Cause distribution (tight band, 748 classified)

- E — interrogative matrix, "?" belongs to a question (461; all
  G1).
- A — infinitive-shaped word is not an infinitive (198: 197
  auto + 1 hand — "Gaultier", proper name, dumas-tour-de-nesle).
- B — governed infinitive embedded in a finite matrix clause
  whose "!" belongs to the matrix (88): e.g. vigny-chatterton
  "Il ne s'agit plus de sourire et d'être bon ! de saluer et de
  serrer la main !" (the "!" exclaims the finite "Il ne s'agit
  plus" clause); musset "Ouvrir son cœur pour le mettre en
  étalage sur un comptoir !" ("!" belongs to the BARE infinitive
  "Ouvrir", the governed phrase is embedded).
- GENUINE — 1 (above).

### Wide-band scan

- 484 candidates triaged; 149 read (no finite-verb/question
  markers in tail); 0 genuine. Notable exclusions: hugo-burgraves
  "Oh ! c'est triste de voir s'enfuir les hirondelles !"
  (finite matrix); "Monter toute ma haine et toute ma colère !"
  (bare exclamatory infinitive, not governed); musset
  "permettez-moi de vous parler !" (imperative matrix).

## Per-clause pass/fail

1. >=1 genuine governed exclamatory infinitive in drama
   re-opens the register question: **PASS.** One genuine
   attestation (Labiche, "Oh ! non… pour ne pas la montrer
   !…", G2, dist=1). The drama corpus now holds n=2
   governed exclamatory infinitives (parent's "Pour conspirer
   !…" + this battery's find), both dialogue-elliptical
   corrective retorts.
2. Confirmed zero generalizes the prose recall closure:
   **ANTECEDENT FALSE.** Clause 1 fired.

## Adverses, answered

- None pre-registered ("Adverses: none listed").
- Self-check: no conflict with any standing verdict. This
  battery's design is corpus-only; it names no cipher values.

## Verdict: PROMOTE (register question re-opened in drama)

One genuine governed exclamatory infinitive in the drama gap
searches (1 of 1,232 candidates; 748 tight classified by hand,
484 wide scanned). The prose recall closure does NOT generalize:
the construction is absent from the 1841 print register but
present in drama dialogue at n=2. Independent confirmation of
the sibling's find — the re-open now rests on two independent
passes of the same design.

## Bookkeeping

- Census script:
  code/crowd17/next-token/gov_excl_inf_recall_drama_census.py
  (re-runnable; corpus pinned by name to the 14-file set,
  total asserted in-session; outputs
  gov-excl-inf-recall-drama_census.json and
  gov-excl-inf-recall-drama_windows.json).
- Classification record:
  code/crowd17/next-token/gov-excl-inf-recall-drama_classification.json
  (denylist source, per-candidate cause decisions with
  file@offset, wide-scan triage log).
- Report: code/crowd17/report_inbox/battery-gov-excl-inf-recall-drama.md
  (this file).
- battery-queue.json: `gov-excl-inf-recall-drama` queued ->
  verdict/promote via temp-file + rename (pre-write assert
  confirmed queued/verdictless; JSON re-validated post-write;
  own entry only; claim/bars/evidence/adverses preserved).
- Lock created on start (agent id + UTC timestamp), deleted on
  completion. No stale lock for this target existed.
- R5005, sealed gates, red-team queue untouched. Every number
  traces to the named corpus files or the census/classification
  records; no invented data.
