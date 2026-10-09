# Battery `lex-52-deinf-register` — 1841 diplomatic-register attestation census

**Target:** `lex-52-deinf-register` (P3)
**Date:** 2026-10-09
**Stream:** repaired 1,847-pair parse, `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt` (re-derived in-session; asserts held). `canonical.py` never used.

## Bar (verbatim from battery-queue.json)

> "Cite dated diplomatic attestations; drop candidates with zero attestation; kill the tie-break iff none attested."

## Bar restated as numbered pass/fail clauses (pre-registered before testing)

1. **C1:** Cite dated diplomatic attestations for the candidate word forms ("prescrira", "préserva", "prévoira") in the 1841 diplomatic-register corpus.
2. **C2:** Drop candidates with zero attestation from the three-way tie.
3. **C3:** Kill the tie-break (the register/attestation route) iff none of the candidates is attested in the construction the locus requires ("X de + INF").

## Method

- Census over the lane's 63-file 1841 diplomatic corpus (`code/side-period/corpus/`, 32,547,082 chars, per `PROVENANCE.md`: Nesselrode vols 7–10 incl. the full 1841 run in vol 8, Pozzo di Borgo, Talleyrand Mémoires, Guizot Mémoires, Metternich papers, Levant correspondence 1841, Revue des Deux Mondes 1841, Allgemeine Zeitung 1841, etc.).
- Per the standing corpus-zero rule (R19-193: zeros require whitespace-normalized search): text denormalized (NFKD accent-strip + lowercase), hyphenated line breaks joined, letter-boundary matches only. Both accented and unaccented OCR spellings caught (pr[eé]serva etc.).
- Two passes: (a) exact word forms with letter boundaries; (b) lemma-level "stem ... de" constructions to test whether the de-government is register-native in any tense.

## Findings

### Word-form census (denormalized, hyphen-joined, letter-boundary)

| Form | Hits | Genuine |
|---|---|---|
| **prescrira** | 0 | 0 |
| **préserva** | 1 | 1 — `talleyrand-memoires-v1.txt`: "qui le préserva de la position plus que critique où il aurait été" (passé simple 3sg; "de" + **noun**, not + infinitive) |
| **prévoira** | 0 | 0 |

- One false positive excluded: `levant-correspondence-1841-p3.txt` "preserva- tion" — a line-break hyphenation of "preservation" (joined away in the hyphen-join pass).
- Dated-register note: the Talleyrand attestation is in the *Mémoires du prince de Talleyrand* (1840s diplomatic memoirs) — the diplomatic register, though narrative rather than correspondence.

### Lemma-level "stem + de" census

| Lemma pattern | Constructions found | de + INF |
|---|---|---|
| prescrir- ... de | 0 | 0 |
| préserver ... de | 7 — "les préserver de tout acte d'injustice", "le préserva de la position", "préservés de la destruction", "me préserver de la funeste tentation", "la préserver de toute attaque extérieure", "le préserver de toute atteinte", "les lauriers préservaient de la foudre" | **0** — all 7 are de + noun |
| prévoir ... de | 1 — "on ne peut plus rien prévoir de bon" (de + adjective) | **0** |

### C1 — PASS

Dated diplomatic attestations cited: one genuine word-form attestation (préserva, Talleyrand Mémoires v1) and 8 lemma-level "de" constructions, all recorded above.

### C2 — applied with stated limits

- At word-form level: "prescrira" and "prévoira" dropped (zero attestation); "préserva" survives as the sole attested form.
- **Tense-asymmetry caveat (recorded, not litigated):** "prescrira"/"prévoira" are 3sg futures, "préserva" is 3sg passé simple. Diplomatic correspondence uses future-tense forms of these verbs rarely; narrative memoirs use passé simple freely. The future-form zeros are register-expected and cannot by themselves kill the viability of "prescrira"/"prévoira" as 1841 lexemes.
- Corpus zeros do not falsify the parent battery's lexicon-verified government claims ("prescrire de + INF", "préserver de + INF", "prévoir de + INF" as grammatical 1841 French) — lexicon ≠ corpus.

### C3 — FIRES at construction level

The tie-break's purpose (per the target claim) is to discriminate the three candidates by "register/attestation fit" for the locus, which requires "X de + INF" (86 is INF-class, A9). At construction level the count is **0 / 0 / 0** in 32.5M chars: no candidate is attested with de+INF in this register. The register-native "préserver de" pattern is de + noun only (7/7) — neutral-to-slightly-adverse to préserva at the de+INF locus. The register route cannot break the tie. **The tie-break is killed.**

## Per-clause summary

- C1 (cite attestations): **PASS**
- C2 (drop zero-attestation candidates): **applied** — prescrira/prévoira dropped at word-form level, with the tense-asymmetry caveat
- C3 (kill tie-break iff none attested): **FIRES** — none attested in the de+INF construction

## Verdict: NULL

The three-way tie (prescrira / préserva / prévoira) is **not broken** — no candidate is attested in the required "X de + INF" construction in 1841 diplomatic French, so the register cannot discriminate them. The tie-break route itself is closed at battery grade. No value named for 52. No standing/red-team verdict contradicted or downgraded (§7 intact; 67 sole polyvalence). Canonical-stream caveat stands (locus straddles a7_04/a7_05, both offsets unvalidated; no stream claims made here).

## Adverses

None listed on the queue target. Parent findings adopted as premises, not re-litigated: the three-way tie, the 27-window census, and the de+INF government per lexeme (battery-profile-52-host-word NULL, 2026-10-09). Noted: its clean conditional decider remains the queued `adj-52-37-value-rerun`; its sibling follow-ups `syll-52-locus-1334` (verdict null) and `phase-a7_05-1334` (queued) are already in the queue — not re-proposed.

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `lex-52-deinf-widen` (P4) — widen the de+INF census beyond the 32.5M-char diplomatic corpus into the lane's ingested drama/fiction corpora (Zola/Maupassant late-19c set, 14-play drama set); harden the construction zeros across registers or find the first attestation.
2. `prescrir-stem-corpus` (P3) — census the prescrir- stem across all period corpora; the "prescrire de" lemma is wholly absent (0 constructions) — a stem-level zero would drop "prescrira" by lemma, not merely by word-form zero, removing the tense-asymmetry rescue.

## Bookkeeping

- Report: this file.
- Queue: `lex-52-deinf-register` → `status: verdict`, `result: null`, date 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated from disk; only this entry changed; no downgrade).
- Lock: created on start (2026-10-09T~12:43Z), deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
