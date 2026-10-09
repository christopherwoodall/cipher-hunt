# Battery `gov-excl-inf-drama-n3` — verdict: PROMOTE

## Bar (verbatim, pre-registered)

"genuine count rises above n=2 (gov-excl-inf-recall-drama's count) with
multi-playwright attestation; else fence as drama-concentrated"

→ C1 (genuine count > n=2, verified in-session) / C2 (multi-playwright
attestation) / C3 (else fence as drama-concentrated). C1 PASS, C2 PASS,
C3 antecedent false.

## Method

1. Read BATTERY-PROTOCOL.md first. Created the lock
   `code/crowd17/next-token/locks/gov-excl-inf-drama-n3.lock` on start
   (agent id + UTC timestamp); deleted on completion. No stale lock for
   this id existed.
2. Reproducible census script:
   `code/crowd17/next-token/gov_excl_inf_drama_n3_census.py`
   (P1/P2 verbatim from `gov_excl_inf_register_drama_census.py` via
   the n2 script; DRAMA list replaced with the full 35-file corpus
   pinned by name — the parent 14 + the n2 14 + the comedy-skew 7;
   duplicate `hugo-hernani.txt` edition excluded, one edition per
   play). Raw output:
   `code/crowd17/next-token/gov-excl-inf-drama-n3_census.json`
   (per-file sizes, "!" counts, all 1,725 candidate windows with
   prep/infinitive/dist/byte_offset fields).
3. **No further drama ingest found.** A corpus-directory sweep shows no
   drama text file ingested after the comedy-skew widening (newest
   drama file: `dumas-fils-dame-camelias.txt`, 2026-10-09 12:56 —
   before this target was dispatched). The n3 charter's "further
   ingest" trigger is absent, so this battery executed the charter as
   a full-corpus verification re-run: identical census, full 35-file
   set, all genuine claims byte-re-verified in-session.
4. Candidate-set reproduction check: the re-run yields 1,725
   candidates = 839 + 515 + 371, with **zero per-file count
   mismatches** against the three prior census JSONs
   (register-drama, n2, comedy-skew). The candidate universe is fully
   covered by the prior hand classifications; no new windows exist
   to classify. Every claimed genuine window was re-read from disk
   bytes at its absolute offset.

## Findings

### Definitive cumulative count: n=12 (arithmetic correction)

The prior reports undercounted. Byte-verified genuine windows:

**Comedy (8):**
1. scribe-bertrand-et-raton.txt @20520 (pour/conspirer, dist 1) —
   RANTZAU: "Pour conspirer !…"
2. labiche-martin-poudre-aux-yeux.txt @24350 (pour/montrer, G2,
   3 tokens "ne pas la") — Mme MALINGEAR: "Oh ! non… pour ne pas
   la montrer !…"
3. scribe-le-savant.txt @30006 (à/louer, dist 1) — HANTZ: "À
   louer !…"
4. labiche-edgard-bonne.txt @14015 (pour/causer, dist 1) —
   "Pour lui causer !…"
5. labiche-edgard-bonne.txt @41764 (pour/polker, dist 1) —
   "Pour polker !"
6. labiche-voyage-perrichon.txt @76864 (pour/être, dist 8) —
   MAJORIN: "Pas pour être témoin !…"
7. labiche-prix-martin.txt @67381 (de/quitter, dist 10) —
   "de quitter ma femme !"
8. labiche-misanthrope-auvergnat.txt @31899 (pour/mettre, dist
   20) — "pour me mettre en garde-française !"

**Drame (4):**
9. hugo-roi-samuse.txt @18467 (de/vouloir, dist 13) —
   TRIBOULET: "De vouloir des savants !"
10. hugo-roi-samuse.txt @18500 (de/vouloir, dist 13) — LE ROI
    (echo): "De vouloir des savants !"
11. hugo-lucrece-borgia.txt @106314 (de/écraser, dist 18) —
    "…à moi de parler haut et de vous écraser la tête du
    talon !"
12. dumas-fils-dame-camelias.txt @57990 (pour/payer, dist 1) —
    PRUDENCE: "Pour payer !…"

Corrections to the standing arithmetic: `gov-excl-inf-drama-n2`
reported "6 genuine (2 Scribe, 4 Labiche)" but its own window list
holds 1 Scribe + 5 Labiche; `gov-excl-inf-drama-comedy-skew`
reported "10 genuine — 6 comedy, 4 drame" but the comedy column is
8 (2 Scribe + 6 Labiche). Definitive: **n=12 — 2 Scribe, 6
Labiche, 3 Hugo, 1 Dumas fils; 8 comedy, 4 drame.**

Corpus totals (verified in-session): 35 files, 5,206,628 chars,
27,486 "!", 1,725 P1/P2 candidates (1,114 tight, dist ≤ 40).

### Per-clause pass/fail

1. Genuine count > n=2: **PASS.** n=12, every window
   byte-verified above with file@offset.
2. Multi-playwright attestation: **PASS.** Scribe, Labiche, Hugo,
   Dumas fils — four playwrights across comedy and drame.
3. Fence as drama-concentrated: **ANTECEDENT FALSE.** The
   construction is drama-wide (falsified at comedy-skew by the
   Hugo/Dumas fils drame attestations, confirmed here).

## Adverses, answered

- None pre-registered. Self-check: no cipher values named (corpus
  census only); no standing or red-team verdict contradicted;
  §7 intact; R5005, sealed gates, red-team adjudication queue
  untouched.

## Caveats (stated, not hidden)

- All 12 genuine are dialogue-elliptical fragments (Q/A replies,
  echoes, corrective retorts) at the parent battery's fragment
  grade. A fully conventionalized standalone ("pour rire !"-grade)
  governed exclamatory infinitive remains unattested in the drama
  corpus.
- This was a verification re-run, not a new-ingest re-run: no
  drama file has been ingested since the comedy-skew widening. If
  future ingest arrives, the charter ("re-run on further ingest")
  can fire again — the script and pinned list make that trivial.
- Prior classification coverage is adopted from the three earlier
  batteries (candidate sets reproduce exactly, zero mismatches);
  the genuine list itself is independently byte-verified here,
  not inherited.

## Verdict: PROMOTE

The genuine count is verified at n=12 — well above n=2 — with
four-playwright attestation across comedy and drame. The
"drama-concentrated" fence does not stand.

## Follow-ups (promote; optional, not mandatory)

None new. The comedy-skew battery's `gov-excl-inf-tragedy-n2`
(tragédie coverage) and `gov-excl-inf-drama-grade` (fragment-grade
audit) continuations stand as the open next steps; not re-proposed
here to avoid duplicate queue entries.

## Bookkeeping

- Census script:
  `code/crowd17/next-token/gov_excl_inf_drama_n3_census.py`
  (verbatim P1/P2; 35-file pinned list; outputs
  `gov-excl-inf-drama-n3_census.json`).
- Report: `code/crowd17/report_inbox/battery-gov-excl-inf-drama-n3.md`
  (this file).
- Queue: `gov-excl-inf-drama-n3` → `status: verdict`,
  `result: promote`, 2026-10-09 (pre-write assert passed — was
  queued/verdictless; temp-file + rename; JSON re-validated from
  disk: 1,239 targets; own entry only; claim/bars/adverses
  preserved; no downgrade).
- Lock created on start, deleted on completion (verified gone).
  R5005, sealed gate instances, red-team adjudication queue
  untouched. Every number traces to the named corpus files or the
  census record; no invented data.
