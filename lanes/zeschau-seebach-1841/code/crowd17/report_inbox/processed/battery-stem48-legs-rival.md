# Battery verdict: stem48-legs-rival

Target: `stem48-legs-rival` (priority 2). Follow-up to battery-stem48-exclusive-legs (null, 2026-10-08).

## Bar (verbatim from battery-queue.json)

"The stem-requirement stands iff no grammatical letter-'e' parse is found at either window; a parse at either window re-opens battery-stem48-exclusive-legs Clause 1."

Numbered clauses:
- C1: A grammatical letter-'e' parse (48='e', standing battery-promoted value) exists at @1229. If yes, parent Clause 1 re-opens.
- C2: A grammatical letter-'e' parse (48='e') exists at @1589. If yes, parent Clause 1 re-opens.
- Decision rule: no parse at either window → the stem-requirement stands and the rival letter-'e' claim is killed.

Claim under test: "Rival letter-'e' parses of the 2 exclusive legs — test @1229 and @1589 for a grammatical letter-'e' parse."
Adverses: none listed.

## Method

- Stream re-derived independently from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt` using the `repair_parse.py` convention (`pairs = [s[i:i+2] for i in range(o, len(s)-1, 2)]`, 1,847 pairs). `canonical.py` never touched. R5005, sealed gates, red-team queue untouched.
- Windows confirmed: @1229 = pair 48 on row a7_01; @1589 = pair 48 on row a8_02. The 48-29-47 trigram is byte-identical at both windows (re-derived, not cited).
- Standing values used: 11=la, 70=pre, 82=m, 29=er, 40=e, 46=que (pencil); 87=ce, 64=qui, 79=tout, 47=ce (A4), 30=pas (promoted/granted); 48='e' (battery-promoted, pending ratification — the value under test); 65=noun (battery-promoted 2026-10-08, unratified — used only as a constraint, flagged where load-bearing).
- 1841 diplomatic French lexicon/grammar throughout. 47="se" is NOT a standing value (A4 allophone tier covers the "ce"-level 47/87 phenomenon, not "se"); "se"-readings counted as new-value assumptions and still tested.

## Window evidence

@1229 (a7_01, pairs 1219–1247):
`61 24 48 30 09 20 57 64 79 82 48* 29 47 33 29 85 56 10 03 40 67 77 81 87 11 00 33 16 00`
Local: `... 64 79 82 48 29 47 33 29 85 ...` = "qui tout m e er ce [33-INF] er [85-stem]".

@1589 (a8_02, pairs 1581–1609):
`53 12 44 00 36 70 64 65 48* 29 47 08 81 03 29 80 67 77 81 82 98 00 44 70 39 11 92 65 23`
Local: `... 70 64 65 48 29 47 08 81 ...` = "pre qui [65] e er ce [08] [81]".

## Segmentation exhaustion

### @1229 — "82 48 29 47" = m,e,er,ce (82=m and 29=er banked, not open to re-read)

| Grouping | Reading | Result |
|---|---|---|
| m\|e\|er\|ce | "er" as word | "er" is not a French word — dead |
| m\|e\|erce | "erce" word | no French word is or starts "erce" — dead |
| m\|eer\|ce | "eer" | no French word contains "eer" — dead |
| m\|eerce | — | none — dead |
| me\|er\|ce | "er" as word | dead (as above) |
| me\|erce | brief's H1: 48 word-final 'e', 29-47 word-internal "erce" | no "erce"-initial word — dead |
| meer\|ce | "meer" | Dutch, not 1841 French — dead |
| meerce | — | none — dead |
| m'\|er… | elision + "er"-initial word | "erreur/errer/ermitage/ers" give no grammatical "tout m'er…" — dead |
| 82 word-final of prev | "tout m" | "m" alone ungrammatical — dead |
| 48 as clitic-'e' | "me"/"ne"/"de"/"le"/"se"/"que" | needs l/n/d/s/q before 48; 82='m' gives only "me", then "er ce" still dead — dead |

-éer-verb rescue (créer/agréer): needs "cré"/"agré" before 48; 82='m' fixed — dead.

### @1589 — "65 48 29 47" = [65],e,er,ce (65 value open, noun-class battery-promoted)

| Grouping | Reading | Result |
|---|---|---|
| [65]\|e\|er\|ce | "er" as word | dead |
| [65]\|e\|erce | brief's H1 | no "erce"-initial word — dead |
| [65]\|eer\|ce | "eer" | dead |
| [65]\|eerce | — | dead |
| [65]e\|er\|ce | "er" as word | dead |
| [65]e\|erce | H1 variant | dead |
| [65]eer\|ce / [65]eerce | — | dead |
| averse-type | 47="se" (new value) + 65="av" (new value) → "averse" | 2 new values AND "qui averse" ungrammatical (qui+noun) AND determiner gap — dead |
| 65-final-'n' + "ne" | 48 as clitic | 48 alone cannot be "ne" — dead |
| -éer verb | 65="cré"/"agré" | 65 noun-class; "cré" not a noun — dead (fails even without the class grant) |

"qui [65-noun]" and the missing determiner were noted but not needed: every 48-containing segmentation already fails.

## Per-clause pass/fail

- C1 (@1229 grammatical letter-'e' parse exists): FAIL — no parse found; rival claim fails at this window.
- C2 (@1589 grammatical letter-'e' parse exists): FAIL — no parse found; rival claim fails at this window.

## Verdict: KILL

No grammatical letter-'e' parse exists at either exclusive leg. The rival letter-'e' claim is eliminated at both windows at kill grade. Per the bar's decision rule, **the stem-requirement stands**: @1229 and @1589 still require the stem reading, confirming battery-stem48-exclusive-legs Clause 1 (its RETIRE test stays failed). Parent Clause 1 is NOT re-opened.

Scope notes:
- This battery kills the rival-parse claim only. It does not promote the stem-requirement or the A7-L2 frame — those belong to the parent battery / red team (parent nulled overall on the Clause-2 10% ceiling; untouched here).
- No standing verdict contradicted or downgraded: 48='e' (battery-promoted) is untouched — the finding is that these two windows are not letter-'e' windows, which the standing value permits.
- 65=noun (battery-promoted, unratified) was used as a constraint in two sub-tests; both fail independently of it.
- Natural next steps remain the already-queued `stem48-scope-fence` (P3) and `stem48-65-value` (P3); no new follow-ups proposed (kill verdict).
