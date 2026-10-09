# Battery `reinforced-pour-inf-interro` — verdict: PROMOTE

## Bar (verbatim, pre-registered)
">=1 genuine attestation re-opens the pairing; confirmed zero keeps the fence"

Numbered clauses:
- C1 (re-open arm): FAIL — 0 genuine attestations under the widened '?' termination.
- C2 (fence arm): PASS — confirmed zero; the reinforced-head + governed-infinitive exclamatory fence stands, now hardened against the '?' termination variant.

No adverses listed.

## Method
Verbatim replication of the parent census (`reinforced_pour_inf_diagnostic_census.py`),
changing ONLY the P2 termination filter: windows must contain "?" instead of "!".
- P1 (dislocation): DEM_REINF regex, reinforced demonstrative head + `[,;:]`.
- Window: demonstrative through the next `[!?.]` (inclusive), capped at 180 chars.
- P3 (governed-infinitive candidate): `(pour|à|a|de|d')` + up to two short tokens +
  infinitive-shaped word, applied to text after the comma.
- Corpora (identical to parent): 60 French files of `code/side-period/corpus`
  (32,706,795 chars; German files excluded) + 3 wider 19th-century files
  (1,987,682 chars: misérables t.1 1862, tocqueville t.1 1835, t.2 1840).
- Script: `code/crowd17/next-token/reinforced_pour_inf_interro_census.py` pattern
  (inline run; output `code/crowd17/next-token/reinforced-pour-inf-interro_census.json`).

Corpus gate: 279 dem-comma hits (1841 register) + 25 (wider) = 304, comparable
to the parent's yield.

## Window-level evidence

**Candidate 1 — musset-comedies-proverbes-1850:**
"celui-là, et il a un maître à danser ?"
NOT genuine. The head "celui-là" is the subject of a finite clause ("il a un
maître à danser"); "à danser" is governed by the noun "maître". The '?'
terminates a finite interrogative clause, not an exclamatory infinitive under
the dislocated head.

**Candidate 2 — revue-deux-mondes-1841-q2:**
"celle-ci : Comment se débarrasser de la terre enlevée en faisant un trou si
grand, et où la mettre cette terre?"
NOT genuine. The infinitive "se débarrasser" is governed by the interrogative
adverb "Comment"; this is a standard interrogative clause ("Comment V-inf ?"),
not the reinforced-head + governed exclamatory-infinitive pairing. The '?'
force falls on the interrogative clause, not on an exclamatory infinitive.

Wider 19th-century corpus: 0 candidates.

## Per-clause pass/fail
- C1 re-open: FAIL (0/2 genuine, 0 candidates wider).
- C2 fence: PASS — confirmed zero keeps the fence.

## Verdict: PROMOTE (fence executed, bar's second arm)

The '?' termination variant adds no genuine attestations: 2 candidates over
34.7M chars, both non-genuine on stated causes. The reinforced-head family
fence now reads: reinforced heads govern infinitives but never license the
exclamatory pairing — under '!' (parent), and under '?' (this battery).
No follow-ups per §4 (promote).

## Scope
- Terminates the '?' variant only; does not re-litigate the parent's '!'
  findings or the prose/drama register splits.
- No stream cells implicated (corpus battery); no standing/red-team verdict
  contradicted or downgraded; §7 intact.

## Bookkeeping
- Script + data: `code/crowd17/next-token/reinforced-pour-inf-interro_census.json`
  (census output; method replicated inline from the parent's script).
- Queue: `reinforced-pour-inf-interro` → `status: verdict`,
  `verdict: {result: promote, report: code/crowd17/report_inbox/battery-reinforced-pour-inf-interro.md, date: 2026-10-09}`.
- Lock created on start (2026-10-09T15:33:52Z), deleted on completion.
- R5005, sealed gates, red-team adjudication queue untouched.
- `canonical.py` never used; stream untouched (corpus battery).
