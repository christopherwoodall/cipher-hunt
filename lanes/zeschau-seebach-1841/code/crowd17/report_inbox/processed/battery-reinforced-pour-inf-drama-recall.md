# battery-reinforced-pour-inf-drama-recall — report

Target id: `reinforced-pour-inf-drama-recall`. Run date: 2026-10-09.
Worker: 9c681550-ef50-4d46-b6a1-3baae0f7ed59.

## Bar (verbatim, pre-registered before testing)

"0 genuine with pause-mark variants confirms the zero is not a
pattern-form artifact; any genuine re-opens the pairing"

Numbered pass/fail clauses (restated before testing, not modified after):

1. Run the governed-infinitive census on the drama corpus with the
   separator class extended to comma + em-dash + parenthesis + hyphen
   (`, ; : - — ( )`) and a 400-char window (400-char cap). If at least
   one GENUINE dislocated reinforced-demonstrative head + governed
   exclamatory infinitive appears among the new variants: the pairing
   re-opens (promote).
2. Re-search the 6 windows that were uncapped in the parent run with the
   widened window. If any resolves to genuine: the pairing re-opens
   (promote). If all 6 resolve to excluded (no "!", finite clause, or
   false P3 hit): the parent zero is not a truncation artifact, and the
   whole pairing stays fenced across both registers (null per §4 — zero
   is an absence, not a refutation).

Corpus note (from the task brief, followed verbatim): 14 distinct plays
/ 2,969,582 chars; one Hernani edition — kept `hugo-hernani-1870.txt`,
excluded `hugo-hernani.txt`.

## Method

1. Read BATTERY-PROTOCOL.md first. Created the lock
   `code/crowd17/next-token/locks/reinforced-pour-inf-drama-recall.lock`
   on start (agent id + UTC timestamp; no lock, stale or fresh, existed
   for this id); deleted on completion.
2. Gate: drama corpus verified present on disk (matches the task brief's
   14 files / 2,969,582 chars; provenance in
   `code/side-period/corpus/PROVENANCE.md`).
3. Wrote a re-runnable two-pass census script,
   `code/crowd17/next-token/reinforced_pour_inf_drama_recall_census.py`:
   - Pass A = parent-run settings verbatim: DEM separators `[,;:]`
     only, 180-char cap, "!" filter, GOV_INF pattern on
     after-separator text. Identifies the 41 hits and the 6 uncapped
     windows by identity (offsets + files recorded).
   - Pass B = recall repair: separators `[,;:\-—()]` (em-dash, hyphen,
     parentheses added), 400-char window with 400-char cap, same "!"
     filter and GOV_INF. Every pass-A uncapped window is re-searched
     individually.
   - The excluded Hernani edition (`hugo-hernani.txt`, 173,559 chars)
     is run separately with pass-B settings so the edition choice
     cannot hide an attestation.
4. Raw output:
   `code/crowd17/next-token/reinforced-pour-inf-drama-recall_census.json`
   (per-file sizes, pass A/B hit counts, all candidate windows with
   @-offsets). R5005 untouched; no standing verdict contradicted.

## Pass-A identity check

Pass A reproduces the parent run exactly: 41 dem-comma hits, 6 uncapped,
1 candidate. The 41/6 counts match `battery-reinforced-pour-inf-drama`,
so the 6 windows below are the same 6 windows (offsets identical).

## Extended separators (clause 1): zero new hits

Pass B (dash/paren/hyphen separators, 400-char window) finds the SAME
41 hits as pass A — the extended separator class adds zero new
reinforced-head windows. Separators after reinforced demonstratives in
this corpus are comma/semicolon/colon only; the pause-mark variant is
not an attested search form, and the parent zero is not a separator
artifact.

## The 6 uncapped windows, re-searched (clause 2)

| file @offset | head | pass-B window end | classification |
|---|---|---|---|
| vigny-chatterton-1835.txt @151996 | celle-ci, | `.` (play preface) | excluded: no "!" (P2), declarative prose preface |
| hugo-ruy-blas.txt @3153 | ceux-là ; | `.` (Hugo's preface) | excluded: no "!" (P2), declarative preface |
| hugo-ruy-blas.txt @34184 | Celui-là, | `!` — now a candidate | **false P3:** gov hit is "à quatre" = preposition + numeral ("quatre" ends in -re), not an infinitive. The exclaimed phrase "Voir pendre à quatre clous au gibet de la ville !" is a modal/perception-governed bare exclamatory infinitive, not a pour/à/de-governed one. Not the searched shape — excluded with cause. |
| dumas-tour-de-nesle.txt @79885 | celui-ci, | uncapped at 400 (narrative) | excluded: no "!" (P2); narrative stage/description prose with no sentence end inside 400 chars — residual deep-narrative gap, recorded as follow-up 2 below |
| dumas-tour-de-nesle.txt @79936 | ceux-ci, | `.` (narrative) | excluded: no "!" (P2), narrative description |
| dumas-kean.txt @43821 | Ceux-là, | `!` — now a candidate | excluded: the "!" terminates a long finite-clause chain ("...ils abaissent ce qui est grand !"); gov hit "de + de produire" is inside a noun phrase ("l'impuissance de produire"), not an exclamatory infinitive. Excluded with cause. |

Remaining candidate (from both passes): scribe-verre-d-eau.txt @36952
("ceux-là, je ne suis pas libre de les accueillir… !") — already
classified in the parent run: dislocated topic resumed by clitic "les"
inside a finite negative clause; the de-governed infinitive is not the
exclaimed phrase. Excluded with cause (same as parent).

Excluded Hernani edition (hugo-hernani.txt, Hetzel 1889, 173,559 chars):
0 hits with pass-B settings. The edition choice hides nothing.

## Per-clause pass/fail

1. FAIL (confirmed zero): pause-mark variants add no windows and no
   candidates — the zero is not a pattern-form artifact.
2. FAIL (confirmed zero): 6/6 uncapped windows resolve to excluded
   (4× no-"!" declarative/narrative, 2× new candidates both excluded
   with cause). The truncation is not load-bearing.

## Verdict: NULL (pairing fenced; recall gap closed, not load-bearing)

0 genuine dislocated reinforced-demonstrative + governed exclamatory
infinitive attestations remain in the drama corpus after the recall
repair. The widened separator class, the 400-char window, and the
excluded-edition run change nothing: the "celui-là, pour rire !" shape
is unattested in 2,969,582 chars of 19th-century French drama, and with
the parent battery 0 genuine in 30.6M chars across prose and drama.

Side observation (recorded, not the bar): hugo-ruy-blas.txt @34184
shows the register DOES have bare exclamatory infinitives under
modal/perception government in reinforced-head windows ("Voir pendre
à quatre clous au gibet de la ville !") — the fence is specifically
about the pour/à/de-governed shape. Routed to follow-up 1.

## Follow-ups (nulls regenerate work; never end it)

1. `reinforced-modal-inf-drama` (P2): census reinforced-demonstrative
   heads + modal/perception-governed bare exclamatory infinitive in the
   drama corpus ("Celui-là, — … Voir pendre à quatre clous … !",
   ruy-blas @34184). Pins whether the reinforced-head licensor class
   survives with a modal/perception governor.
2. `reinforced-head-narrative-uncapped-drama` (P3): close the residual
   deep-narrative recall gap — the one window (tour-de-nesle @79885)
   still uncapped at 400 chars; narrative-heavy plays may need
   punctuation-aware windows.

Already queued (not duplicated): `reinforced-pour-inf-drama` parent
follow-ups `reinforced-pour-inf-drama-recall` (this battery),
`gov-excl-inf-register-drama`, `reinforced-head-topology-drama`.
