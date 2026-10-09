# Battery `gov-excl-inf-drama-grade` — verdict: PROMOTE

## Bar (verbatim, pre-registered)

"audit the 10 genuine drama cases (6 comedy, 4 drame); all-fragment confirms
the fragment-grade grammar; >=1 standalone re-opens the grammar"

→ C1 (all audited cases are dialogue-elliptical fragments → fragment-grade
grammar confirmed) / C2 (≥1 standalone case exists → grammar re-opened).
One fork; whichever fires decides the audit.

Adverses: none listed.

## Method

Case-by-case grading of every standing-genuine drama governed-exclamatory-
infinitive attestation, from the byte-verified contexts in the parent
batteries' reports, re-checked against the corpus files under
`code/side-period/corpus/` (byte offsets re-read in-session, 2026-10-09;
`canonical.py` never used — this is a corpus battery, the cipher stream is
not its evidence base).

Operational grade:
- FRAGMENT — the exclaimed infinitive phrase lacks a constituent (matrix,
  subject, purpose head) supplied by the dialogue context: Q/A replies,
  echo fragments, corrective retorts.
- STANDALONE — self-contained exclaimed governed-infinitive phrase: no
  missing constituent, explicit subject if any, not anaphoric on another
  speaker's turn.

Count caveat (stated, not hidden): the bar says 10 (6 comedy, 4 drame),
repeating the comedy-skew report's tally. The standing record is
**12**: the comedy-skew tally drops the recall-drama find
("pour ne pas la montrer !", Labiche *Martin Poudre-aux-yeux*, still
standing genuine, never re-graded) and one n2 Labiche case. I audited
all 12 standing cases; the decisive result holds under either count.

## Case evidence (all 12)

**Comedy (8): 2 Scribe + 6 Labiche — all FRAGMENT.**

1. Scribe, *Bertrand et Raton* — Rantzau: "Pour conspirer !… Votre
   majesté avait grand tort." Reply to the Queen's reproach ("vous en
   qui j'espérais !…"); elliptical purpose-retort.
2. Scribe, *Le Savant* — Hantz: "À louer ! notre appartement est à
   louer ?" Echo of Frédéric's "qui est à louer".
3. Labiche, *Martin Poudre-aux-yeux* — Mme Malingear: "Oh ! non…
   pour ne pas la montrer !…" Corrective retort of "Pour ne pas la
   perdre."; no finite matrix in the retort.
4. Labiche, *Edgard et sa bonne* — Florestine: "Pour lui causer !"
   Answer to Edgard's "Pour quoi faire ?"
5. Labiche, *Edgard et sa bonne* — Henriette: "Pour polker !"
   Answer to "Pour quoi faire ?"
6. Labiche, *Voyage de M. Perrichon* — Majorin: "Pas pour être
   témoin !…" Elliptical purpose reply (why he cannot be second).
7. Labiche, *Prix Martin* — Martin, à part: "Oui, oui ! de quitter
   ma femme !" Echo of Agénor's "que de te quitter".
8. Labiche, *Le Misanthrope et l'Auvergnat* — Chiffonnet: "au
   carnaval seulement… pour me mettre en garde-française !"
   Elliptical retort to "vous portez perruque ?"

**Drame (4): 3 Hugo + 1 Dumas fils — 3 FRAGMENT, 1 STANDALONE.**

9. Hugo, *Le Roi s'amuse* — Triboulet: "…vous rêvez, / De vouloir
   des savants !" Corrective retort; no finite verb; dialogue-anaphoric.
10. Hugo, *Le Roi s'amuse* — Le Roi: "De vouloir des savants ! Moi,
    foi de gentilhomme !…" Echo of Triboulet.
11. Hugo, *Lucrèce Borgia* (@106314) — Lucrezia: "À mon tour
    maintenant, à moi de parler haut et de vous écraser la tête du
    talon !" **STANDALONE.** Explicit subject ("moi"), not anaphoric
    on any prior turn; a complete independent "à moi de"-infinitive
    phrase exclaimed in its own right; no constituent supplied by
    dialogue ellipsis. Genuine per the standing taxonomy ("!" closes
    the de-infinitive phrase; no finite matrix; not embedded in an
    exclaimed NP) — the grade here concerns only the fragment axis.
12. Dumas fils, *La Dame aux camélias* — Prudence: "Pour payer !"
    Answer to Armand's "Et pourquoi ces ventes et ces
    engagements ?"

## Per-clause pass/fail

- C1 (all-fragment → fragment-grade grammar confirmed): **FAIL.**
  Case 11 is standalone.
- C2 (≥1 standalone → grammar re-opened): **FIRES.** Case 11
  (Hugo, *Lucrèce Borgia*, @106314) is a standalone governed
  exclamatory infinitive in drama.

## Verdict: PROMOTE

The audit delivered its decisive answer: 11/12 standing drama cases are
dialogue-elliptical fragments, but the fragment-grade grammar is NOT
confirmed — one case (Lucrezia's "à moi de parler haut et de vous
écraser la tête du talon !") is a self-contained, subject-explicit,
non-anaphoric exclaimed infinitive phrase. The grammar is re-opened:
the construction can stand as an independent exclamation, not only as
a dialogue fragment.

Scope: case-level corpus finding. No standing or red-team verdict
contradicted or downgraded (all parent battery verdicts adopted as
premises); §7 intact. R5005, sealed gate instances, and the red-team
adjudication queue untouched.

## Follow-ups

Promote per §4 carries no mandatory follow-ups. Optional, for the
supervisor:
1. `gov-excl-inf-independent-amoide` (P4) — census the independent
   "à moi de / à toi de + inf" exclamatory construction in the drama
   corpus; decides whether case 11 is an idiolectal one-off or a
   conventionalized standalone mold.
2. `gov-excl-inf-comedy-tally-repair` (P4) — repair the standing
   genuine-case tally (10 → 12) in the finder/state notes so later
   batteries inherit the full inventory.

## Bookkeeping

- Lock: `code/crowd17/next-token/locks/gov-excl-inf-drama-grade.lock`
  created 2026-10-09T13:18:12Z, deleted on completion (verified gone).
- Queue: `gov-excl-inf-drama-grade` → `status: verdict`,
  `result: promote`, 2026-10-09 (pre-write assert passed —
  was queued/verdictless; temp-file + rename; JSON re-validated
  from disk; own entry only; no downgrade).
