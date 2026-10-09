# Battery report: reinforced-pour-inf-widercorpus

- Target id: `reinforced-pour-inf-widercorpus`
- Claim: governed census with the reinforced-head inventory on a second
  19th-century French corpus.
- Date: 2026-10-09
- Worker: battery worker (subagent 37d956b6-6159-4798-9ee7-c62e56c2766f)
- Stream: not applicable — corpus census against period French, per target
  charter. The 1,847-pair repaired parse was not used. R5005, sealed gate
  instances, and the red-team adjudication queue were not touched.

Terms (ASD-STE100): "reinforced head" = a demonstrative compound marked
with -là or -ci (celui-là, ceux-là, celle-là, celles-là, celui-ci,
ceux-ci, celle-ci, celles-ci). "Exclamatory infinitive" = an infinitive
used as an exclamation ("Moi, me taire !"). "Governed" = the infinitive
is governed by a preposition (pour / à / de), as in "celui-là, pour
rire !". "Genuine attestation" = the reinforced head actually heads an
exclamatory infinitive phrase, not a downstream finite clause.

## Parentage

Follow-up of the NULL `reinforced-pour-inf-diagnostic` (2026-10-09),
which fenced the reinforced-head + governed-exclamatory-infinitive
pairing at 0/4 genuine in the 27.66M-char 1841-register + wider-19c
corpus. This battery runs the same governed search on a SECOND
19th-century French corpus untouched by the diagnostic and by the
in-flight drama sibling (`reinforced-pour-inf-drama`): 14 vaudeville
comedies (11 Labiche + 3 Scribe). Does not duplicate the drama sibling
(drama register), the diagnostic (register + miserables/tocqueville),
or the recall-gap batteries (same corpus, widened search).

## Bar (verbatim, pre-registered before testing)

">=1 genuine attestation re-opens at register level; confirmed zero
hardens the fence."

Numbered pass/fail clauses (restated before testing, not modified
after):

1. At least one GENUINE dislocated reinforced-demonstrative head +
   governed exclamatory infinitive ("celui-là, pour rire !" shape)
   exists in the second 19c corpus. If yes: the pairing re-opens at
   register level (comedy/vaudeville licenses what the register
   corpus fences).
2. If the census is a confirmed zero — every candidate window
   classified, inventory presence verified so the zero is not an
   empty-search artifact — the fence hardens at register level.

## Method

1. Read BATTERY-PROTOCOL.md first. Created the lock
   `code/crowd17/next-token/locks/reinforced-pour-inf-widercorpus.lock`
   on start (agent id + UTC timestamp; no stale lock for this id
   existed); deleted on completion.
2. Re-ran the diagnostic's P1/P2/P3 verbatim (same DEM_REINF
   inventory, same 180-char window, same P2 "!" filter, same P3
   governor filter) in a new script:
   `code/crowd17/next-token/reinforced_pour_inf_widercorpus_census.py`.
   Raw results in
   `code/crowd17/next-token/reinforced-pour-inf-widercorpus_census.json`.
3. Corpus (all 19th-century French, provenance in the file headers):
   - labiche-29-degres-ombre, labiche-affaire-rue-lourcine,
     labiche-baron-fourchevif, labiche-doit-on-le-dire,
     labiche-edgard-bonne, labiche-la-cagnotte, labiche-main-leste,
     labiche-misanthrope-auvergnat, labiche-noces-bouchencoeur,
     labiche-prix-martin, labiche-voyage-perrichon (Calmann-Lévy
     Théâtre complet, 1898 editions of 1850s–1870s plays);
   - scribe-charlatanisme (1834 ed. of 1825 play), scribe-le-lorgnon
     (1833), scribe-le-savant (1832).
   - Total: 14 files, 1,030,838 characters.
   - Deliberately excluded: labiche-chapeau-de-paille,
     labiche-martin-poudre-aux-yeux, scribe-bertrand-et-raton,
     scribe-verre-d-eau (all in the drama sibling's corpus —
     duplication avoided).

## Window-level evidence

### Census yields

- 14 files, 1,030,838 characters, **6 dem-comma hits**, 0 governed-inf
  exclamatory candidates.
- Inventory presence check: 6/1.03M chars = 5.8 hits per 1M chars, vs
  231/27.66M = 8.4 per 1M in the diagnostic corpus. Same order of
  magnitude — the heads exist in topic position in comedy; the zero
  is a genuine absence of the pairing, not an empty-search artifact.

### All 6 dem windows hand-classified (P2/P3 due diligence)

1. `ceux-là, on ne les coupe jamais !`
   (labiche-baron-fourchevif) — passes P2 ("!"), but the window is a
   finite clause ("on ne les coupe jamais"); no infinitive at all.
   Excluded with cause.
2. `ceux-ci, je vais chercher les autres rideaux… Montez…`
   (labiche-edgard-bonne) — no "!" (P2 drop, correct); finite clause.
   Excluded with cause.
3. `celui-là, il vit tout seul, dans des endroits noirs, comme un
   colimaçon !` (labiche-misanthrope-auvergnat) — passes P2, but
   finite clause ("il vit…"); no infinitive. Excluded with cause.
4. `celui-ci, je l’ai traité en conscience.`
   (scribe-charlatanisme) — finite, no "!". Excluded with cause.
5. `Celui-là, fidèle et sensible, / Ne me vole pas, j’en suis sûr.`
   (scribe-le-lorgnon) — verse; finite imperative ("ne me vole pas").
   Excluded with cause.
6. `celui-là, j’espère, ne sera pas exigeant sur la dot.`
   (scribe-le-savant) — finite. Excluded with cause.

### Due-diligence checks

- No window contains any infinitive governed by the head — not even
  a false-positive GOV_INF match. The P3 zero is total, not a
  classification judgment call.
- The comedy register is otherwise the natural habitat of
  exclamatory syntax (all 6 windows carry "!" or strong exclamatory
  force), so the pairing's absence here is informative, not a
  register mismatch.
- Limitation: same as the diagnostic — P1 admits only [,;:] after
  the head; dash-delimited dislocations and >180-char windows are
  unsearched here too (owned by reinforced-pour-inf-recall).

## Per-clause pass/fail

1. ≥1 genuine reinforced-head + governed-exclamatory-infinitive
   attestation in the 14-comedy corpus: **FAIL (confirmed zero).**
   6/6 dem windows classified; 0 candidates, 0 genuine in 1,030,838
   characters.
2. Confirmed zero → fence hardens at register level: **EXECUTED.**
   The pairing is now fenced across three independent 19c French
   corpora: the 1841 register (0/4 genuine, 27.66M chars), the
   comedy register (0/6 dem windows with an infinitive at all,
   1.03M chars), plus the in-flight drama sibling's verdict
   pending. Zero is an absence, not a refutation — the personal
   tonic precedent ("Moi, voler !") keeps the construction
   grammatical; the failure stays local to the reinforced-head
   licensing.

## Adverses, answered

- None pre-registered ("Adverses: none listed").
- Self-check: does this verdict contradict the diagnostic NULL or
  the drama sibling (in flight)? No — it completes them. All three
  converge on the fenced pairing.
- Self-check: does the comedy-register choice contradict the
  diagnostic's register claim? No — the bar explicitly asked for a
  second corpus, and comedy is where exclamatory syntax lives.
- §5.2: no standing red-team verdict touched; no overwrite, no
  escalation required.

## Verdict: PROMOTE (fence hardened, bar clause 2)

Confirmed zero genuine dislocated reinforced-demonstrative + governed
exclamatory infinitive attestations in a second 19th-century French
corpus (1,030,838 chars, 14 vaudeville comedies; 6/6 dem windows
classified: finite clauses and imperatives only, no governed
infinitive anywhere). The fence is now register-triangulated:
1841 register + comedy, with drama pending. No follow-ups per §4
(promote).

## Bookkeeping

- Census script:
  code/crowd17/next-token/reinforced_pour_inf_widercorpus_census.py
  (re-runnable; P1/P2/P3 verbatim from
  reinforced_pour_inf_diagnostic_census.py; outputs
  reinforced-pour-inf-widercorpus_census.json with per-file sizes,
  hit counts, and the 6 dem windows).
- Report: code/crowd17/report_inbox/battery-reinforced-pour-inf-widercorpus.md
  (this file).
- battery-queue.json: `reinforced-pour-inf-widercorpus` queued ->
  verdict/promote via temp-file + rename (pre-write assert confirmed
  queued/verdictless; JSON re-validated post-write; own entry only;
  claim/bars/evidence/adverses preserved).
- Lock created on start (agent id + UTC timestamp), deleted on
  completion. No stale lock for this target existed.
- R5005, sealed gates, red-team queue untouched. Every number traces
  to the named corpus files or the census script; no invented data.
