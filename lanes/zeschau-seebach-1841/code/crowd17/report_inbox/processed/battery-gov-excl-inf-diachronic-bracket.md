# Battery report: gov-excl-inf-diachronic-bracket

- Target id: `gov-excl-inf-diachronic-bracket`
- Claim: corpus census of late-19th-century French fiction (e.g. Zola, Maupassant) to bracket the governed exclamatory-infinitive construction's emergence: absent 1841, present 1907.
- Date: 2026-10-09
- Worker: battery worker (session 398b1ea2-deb6-4f61-933c-79cf3082483c)
- Corpus: `code/crowd17/next-token/corpus-late19c/` — 6 French texts (Zola: Nana 1880, Germinal 1885, L'Assommoir 1877; Maupassant: Pierre et Jean 1888, La Maison Tellier 1881, Contes du jour et de la nuit 1885), 3,758,522 chars, all verified inLanguage=fr on the Gutenberg ebook page before download, provenance + sha256 in `corpus-late19c/PROVENANCE.md`. R5005, sealed gate instances, and the red-team adjudication queue untouched.

Terms (ASD-STE100): "governed exclamatory infinitive" = a preposition-governed
infinitive phrase (pour / à / de + infinitive) that IS itself the exclaimed
element ("pour rire !"). "Genuine attestation" = the "!" terminates the
governed infinitive phrase itself; the infinitive is not embedded in a finite
matrix clause whose "!" belongs to the matrix, and not embedded in an exclaimed
noun phrase. "Bracket" = the construction is absent at the lower date (1841)
and present at the upper date; a genuine late-19th-c attestation narrows the
emergence window to 1841–1877.

## Bar (verbatim, pre-registered before testing)

"Bar: census a late-19th-century French fiction corpus (e.g. Zola, Maupassant)
to bracket the construction's emergence: absent 1841, present 1907 — when does
it appear?"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** a genuine attestation in the late-19th-c corpus brackets the
   emergence (the construction already existed in 1877–1888 French fiction).
2. **C2:** confirmed zero in the late-19th-c corpus keeps the question open
   (the emergence window stays 1841–1907).

Verdict rule: C1 PASS → promote; C1 FAIL + C2 holds → null (question open,
1–3 follow-ups proposed).

## Method

1. Read BATTERY-PROTOCOL.md first. Created
   `code/crowd17/next-token/locks/gov-excl-inf-diachronic-bracket.lock` on
   start (session id + 2026-10-09T12:06:36Z UTC); to be deleted on completion.
2. Replicated the P1 candidate design of `gov_excl_inf_modern_census.py`
   verbatim (`gov_excl_inf_late19c_census.py`): 120-char lookback per "!",
   GOV_INF pattern (pour|à|a|de|d' + ≤2 short words + infinitive-shaped
   -er/-ir/-re/-oir), closest match, no [.;] between infinitive and "!".
3. 612 candidates → 413 tight (dist ≤ 40) hand-classified individually;
   199 wide (dist > 40) scanned, with a targeted grep of the "Merci, pour X!",
   "A quoi bon? pour X", "Mais de X!" shapes across the whole wide band.
4. `canonical.py` never used (corpus battery; no cipher stream needed).
   1841 diplomatic French register for the corpus-side claim; the census is
   late-19th-c literary French as the bracket requires.

## Window-level evidence (all byte-verified against the source files)

Census: 3,758,522 chars, 6,074 "!", 612 candidates, 413 tight hand-reviewed.

**Six genuine attestations** (full context + grammaticality note in
`gov-excl-inf-late19c_classification.json`):

- G1 — Zola, *Nana* (1880), pg5250: «— Ah! non, par exemple! **pour ne
  rien voir!** répondit-il.» "!" terminates the pour-infinitive phrase;
  elliptical reason for the refusal "non"; "répondit-il" is a reporting verb
  after the "!". No finite matrix clause.
- G2 — Zola, *L'Assommoir* (1877), pg6497: «— Ah bien! dit madame Putois,
  on est trop bête de se confier à elles. **Merci, pour se faire
  estropier!**...» Ironic "Merci" + exclaimed pour-infinitive; "dit madame
  Putois" is a reporting verb before the clause. No finite matrix clause.
- G3 — Maupassant, *La Maison Tellier* (1881), pg11596: «— Mais **de
  m'épouser**, pardine!» — the de-governed infinitive stands alone as the
  exclaimed answer to «Quoi, not'maître?»; "pardine" is an interjection.
  No finite matrix clause.
- G4 — Zola, *Nana* (1880), pg5250: «Mais les femmes refusaient,
  absolument. **Merci, pour perdre à coup sûr!**» Same ironic
  "Merci, pour X!" shape. No finite matrix clause.
- G5 — Zola, *Germinal* (1885), pg5711: «— Fallait peut-être sauter sur
  le chef. **Merci! pour avoir des ennuis!**» Same shape. No finite matrix
  clause.
- G6 — Zola, *Germinal* (1885), pg5711: «— A quoi bon? **pour vous
  entendre dire des bêtises inutiles!**...» The pour-infinitive answers
  "A quoi bon?"; the "!" terminates the governed phrase itself. No finite
  matrix clause.

**Near-miss recorded (not genuine):** Zola, *Nana* — «ce serait trop
bête! cria Bordenave... **Dix mille francs pour lâcher Rose!**» — the
exclaimed head is the noun phrase "Dix mille francs" with a purpose adjunct;
embedded in an exclaimed NP, so excluded per the definition.

**Non-genuine families in the tight band:** finite-matrix clauses carrying
the "!" ("C'est cochon de dormir jusqu'à six heures!", "Que pouvait-il avoir,
cet amour, pour s'abîmer ainsi?", "Fallait peut-être sauter sur le chef"
matrix legs); exclaimed noun/adverb phrases ("À ce soir!", "A bas le
traître!", "A la Victoire!", "Que ça de genre!", "Espèce de couleuvre!");
bare infinitives with no governor ("Quel rêve! être les maîtres...");
imperatives; regex false positives ("à l'air", "à la fenêtre",
"pour quatre sous", "de la misère").

**Wide band:** 199 candidates scanned; 1 shape-pattern hit
("à quoi bon vivre" in indirect discourse — finite interrogative matrix);
0 genuine.

## Per-clause pass/fail

1. **C1 — PASS.** Six genuine attestations in 1877–1888 French fiction,
   verified against the source bytes. The construction predates 1907: the
   emergence window narrows from [1841, 1907] to **[1841, 1877]**.
2. **C2 — moot.** A confirmed zero did not hold.

Adverses listed: none.

## Verdict: PROMOTE

The governed exclamatory infinitive already existed in French literary
dialogue by 1877 (Zola, *L'Assommoir*). The diachronic bracket is now
1841 → 1877: absent from 1841 French print (standing register-battery zero),
present in 1877 fiction. This does not restore the A/B @1029 arms — that kill
rests on the clitic/tonic dislocation rule (ce01-1029-redteam-package), not
on the register fence — but it hardens the general re-open of governed
exclamatory infinitives at register level.

## Caveats (stated, not hidden)

- All six attestations are dialogue-elliptical fragments, not fully
  conventionalized "pour rire!"; the construction is rare even here
  (6 of 6,074 "!", ~3.76M chars).
- The 1841 zero remains the standing register fact for diplomatic print.
- n=6; register (literary dialogue) and period (1877–1888) are fixed.

## Follow-ups (promote needs none; one optional continuation)

1. `gov-excl-inf-corpus-pre1841` (P4) — corpus check: is the construction
   attested in pre-1841 French fiction (e.g. Balzac, Sand)? If yes, the
   1841 print-register zero is even more register-specific than thought;
   if zero, the 1841 boundary holds.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-gov-excl-inf-diachronic-bracket.md` (this file).
- Census: `code/crowd17/next-token/gov-excl-inf-late19c_census.json`;
  classification: `code/crowd17/next-token/gov-excl-inf-late19c_classification.json`;
  script: `code/crowd17/next-token/gov_excl_inf_late19c_census.py`;
  corpus + provenance: `code/crowd17/next-token/corpus-late19c/`.
- Queue: `gov-excl-inf-diachronic-bracket` → status `verdict`, result
  `promote`, 2026-10-09 (pre-write assert passed — was queued/verdictless;
  temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `locks/gov-excl-inf-diachronic-bracket.lock`: created on start,
  deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched;
  no standing/red-team verdict contradicted or downgraded; §7 intact.
