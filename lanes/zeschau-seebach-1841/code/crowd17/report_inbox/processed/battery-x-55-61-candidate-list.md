# Battery report: x-55-61-candidate-list

Target: `x-55-61-candidate-list`. Claim: the French candidate space for X
is enumerable and rankable under the detachable-slot reading.
Date: 2026-10-09. Worker: battery worker (subagent f3195d4f).
Lock `locks/x-55-61-candidate-list.lock` created 2026-10-09T08:34:09Z (no
pre-existing lock for this id); deleted on completion.

## Bar (verbatim from battery-queue.json, pre-registered before testing)

"(a) state the grammatical constraints each window imposes on X (number,
gender if determinable, part of speech); (b) enumerate the candidate space
with per-window exclusion criteria, killing candidates that fail any
window's agreement test; (c) if the space collapses to one candidate with
stated slot values, name X"

## Bar restated (numbered pass/fail clauses; frozen before testing)

1. Enumerate the French candidate space for X (one word over the 55-61
   bigram, 13/43 as detachable preceding slot) with per-window exclusion
   criteria stated.
2. Rank the candidates by byte-evidence under standing values.
3. Kill candidates that fail any window's agreement test at kill grade;
   fence the survivors. If the space collapses to one candidate with stated
   slot values, name X.

Adverses (from queue): "all five values open; ne-ce-1169's null (94-87
frame outside X's span)".

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`,
parsed per `code/side-keyhunt/repair_parse.py` (byte-exact stride-2 pairing
per row offset); asserted 1,847 pairs / 96 types before testing.
`canonical.py` never used. R5005, sealed gates, red-team adjudication queue
untouched. Every number below re-derived in-session; no prior counts trusted.

Standing values used (protocol section 7): banked GT 11=la, 82=m, 40=e,
46=que, 70=pre, 34=i, 29=er; granted 87=ce, 64=qui, 96=par, 17=fois,
79=tout, 00=pour, 84=on, 47=ce; provisional 59=est, 77=le.
Battery-adopted premises (cited, not re-litigated):
- subj-55-61-word (verdict KILL, 2026-10-09): the plural-noun value for the
  55-61 word is forced false — W3 (@1205) forces 55-61 verb-shaped, and
  section 7's sole-polyvalence rule bars a noun-at-W1/verb-at-W3 split at
  battery level.
- seg-55-61-21-stem (verdict PROMOTE, 2026-10-09): W3 parses as
  "[58] ce(47) [43] prend(55-61, finite 3sg) [21-noun DO]. [65] qui est(59)
  [32]e par(96) [36]" — noun/adjective/infinitive/subjunctive readings of
  55-61 killed at this window.
- merge-gate-w1-x55-61 (verdict PROMOTE, 2026-10-09): the W1
  subject-reading of X is killed as a merge hypothesis; name-55-61-core
  re-scoped to W2/W3 frames (the re-scope does not exempt W1 from the
  uniformity bar here — see below).
- 94="ne" STRONG LEAD (R17-001, battery); 55 = verb class (battery-grade,
  2026-10-09); 21 = noun class, 65 = noun class (registry).
- ne-ce-1169 (verdict NULL): the "94 87" = "ne ce" hapax is fenced as a
  stream-unique bigram outside X's span; adopted, not re-litigated.
Values of 13, 43, 55, 61, 21 remain open (stated, not hidden).

## Window-level evidence (re-derived)

55-61 bigram: exactly x3 stream-wide. Predecessors (13, 13, 43);
successors (94, 94, 21). All byte-exact:

- W1 @576-577 (row a3_02): `…76 45 94 52 87 78 45 | 13 55 61 | 94 82 06 06
  50 10 19` = "…verdict(78-45, LEAD) [13] X ne(94, STRONG LEAD)
  mentent(82-06-06, conditional)". X immediately precedes "ne" + 3pl verb.
- W2 @1167-1168 (row a6_09): `…82 44 83 21 67 78 45 | 13 55 61 | 94 87 83
  21 85 36 74` = "…verdict [13] X ne(94) ce(87) [83] [21-noun]". The
  "94 87" = "ne ce" bigram is the fenced hapax (ne-ce-1169).
- W3 @1205-1206 (row a7_00): `…82 16 64 29 45 58 47 | 43 55 61 | 21 65 64
  59 32 48 96` = "…ce(47, granted) [43] X [21-noun] [65-noun] qui(64)
  est(59, provisional)…".

## Per-window constraints on X (bar clause a)

- **W1 (@576):** X sits in "[13] X ne mentent". A plural noun X parses as
  the 3pl subject ("les X ne mentent"); a finite verb X gives "V ne V"
  (two finite verbs, no conjunction — kill grade); an infinitive,
  determiner, preposition, pronoun, or interjection X has no licensed role
  (kill grade). An adjective X survives only if 13 is a plural noun head
  ("les [13] [adj] ne mentent" — weak but grammatical); a relative "qui" X
  survives if 13 is a plural noun antecedent ("[13] qui ne mentent").
  Number: plural if nominal; gender: undeterminable.
- **W2 (@1167):** X sits in "[13] X ne ce [83] [21]". The "ne ce" bigram is
  X-independent (fenced hapax); no X value repairs it. A finite verb X
  gives "V ne ce" (kill grade). A noun X does not fix "ne ce" either —
  the window's grammaticality is X-independent. Constraint: X's value is
  non-discriminating here; the window contributes no surviving class.
- **W3 (@1205):** X is forced to finite-3sg-verb class by the promoted
  discriminator ("prend" + noun object; noun/adjective/infinitive/
  subjunctive readings killed at this window). Number: singular
  (agreement with "ce [43]"); POS: finite verb.

Under section 7's sole-polyvalence rule, X takes ONE value across windows
at battery level — a conditioned noun-at-W1/verb-at-W3 split is red-team
venue, not declarable here (this is exactly the bar subj-55-61-word
already enforced).

## Candidate enumeration with per-window exclusion (bar clause b)

Candidates are French words over the 55-61 bigram (letter-level
segmentation is tensed per seg-55-61-21-stem; candidates are word-level).
"Survives" = at least one grammatical parse under standing values.

| # | Candidate class | W1 @576 | W2 @1167 | W3 @1205 | Verdict |
|---|---|---|---|---|---|
| 1 | plural nouns (témoins, hommes, serments, …) | survives (subject slot) | neutral | **KILLED** (adopted: subj-55-61-word kill grade) | KILLED |
| 2 | singular nouns | KILLED (3pl agreement) | neutral | KILLED (two head nouns) | KILLED |
| 3 | finite 3sg verbs (prend, tient, voit, met, porte, …) | **KILLED** ("V ne V" — "prend ne mentent" ungrammatical; two finite verbs / V-ne-V, no rescue: clause boundary leaves "ne mentent" subjectless = pro-drop ✗; 94="ne" is the standing STRONG LEAD) | KILLED ("V ne ce" — "prend ne ce" ungrammatical; "ne ce" fenced hapax) | survives (demonstrated: "prend") | KILLED |
| 4 | finite 3pl verbs (prennent, tiennent, …) | KILLED (two finite verbs) | KILLED | KILLED (singular "ce [43]" subject) | KILLED |
| 5 | infinitives (prendre, tenir, voir, …) | KILLED ("…X-inf ne mentent" ✗) | KILLED | KILLED (no finite verb in clause) | KILLED |
| 6 | adjectives | weak-survives (iff 13 = plural noun head) | neutral | **KILLED** ("ce [43] [adj] [21]": adj between two nouns — modifies 43? then bare "[21]" ✗; modifies 21? 21 is noun class ✗; predicative? no copula ✗) | KILLED |
| 7 | adverbs (bien, mal, souvent, …) | weak (non-standard "…[adv] ne V" order) | neutral | KILLED ("ce [43] [adv] [21]" ✗) | KILLED |
| 8 | relative "qui" | survives ("[13-noun] qui ne mentent") | neutral | **KILLED** ("qui" + noun + noun, no verb ✗) | KILLED |
| 9 | "que" | KILLED ("que ne mentent" — null subject ✗) | KILLED | KILLED | KILLED |
| 10 | determiners (les, des, ces) | KILLED (determiner needs a noun) | KILLED | KILLED | KILLED |
| 11 | prepositions (de, par, pour) | KILLED | KILLED | KILLED | KILLED |
| 12 | personal pronouns (ils, elles) | KILLED ("[13] ils" double subject ✗) | KILLED | KILLED | KILLED |
| 13 | interjections | KILLED (subject missing ✗) | KILLED | KILLED | KILLED |

**Ranking (bar clause b, second half):** the nearest misses are (3)
finite-3sg-verb ("prend" — survives W3, demonstrated there, killed at
W1/W2) and (8) relative "qui" (survives W1, killed at W3). No class
survives more than one discriminating window. **The space collapses to
zero, not one.**

## Per-clause pass/fail

1. **PASS.** Candidate space enumerated with per-window exclusion
   criteria stated (table above); every class tested against W1/W2/W3.
2. **PASS.** Ranked by byte-evidence: "prend" ranks first on W3's
   demonstrated frame but is killed at W1/W2; "qui" ranks second on W1
   but is killed at W3; all others die earlier.
3. **KILL-GRADE RESULT.** Every candidate class fails at least one
   window's agreement test at kill grade; the space collapses to ZERO
   candidates. Bar (c)'s antecedent ("collapses to one candidate") does
   not fire — there is no X to name. Substantive finding: under section
   7's sole-polyvalence rule, the detachable-slot reading itself (one
   French word X over 55-61 spanning the windows) is **KILLED at kill
   grade** — W3 forces finite-verb class while W1 and W2 kill finite-verb
   X, and the noun alternative is already kill-grade dead.

## Adverses answered

- "all five values open": confirmed — 13, 43, 55, 61, 21 values remain
  open; no value was named or invented here.
- "ne-ce-1169's null (94-87 frame outside X's span)": adopted as premise
  — W2's "ne ce" hapax is X-independent, which is why W2 is
  non-discriminating rather than X-killing.

No standing or red-team verdict contradicted or downgraded: the kill is
consistent with subj-55-61-word (KILL, plural-noun), seg-55-61-21-stem
(PROMOTE, W3 "prend" — the reading that kills X at W1), and
merge-gate-w1-x55-61 (PROMOTE, re-scope). Section 7 intact (no
polyvalence declared).

## Verdict: KILL

The detachable-slot reading — one French word X over the 55-61 bigram at
all three windows — is killed at kill grade: the candidate space is
enumerable and rankable, and it collapses to zero. W3's promoted
finite-verb reading ("prend") is ungrammatical at W1 ("V ne V") and W2
("V ne ce"); the plural-noun alternative is already kill-grade dead
(subj-55-61-word); no other word class survives both W1 and W3. This does
not kill 55 or 61 individually, nor the 55-61-94 word-unit hypothesis
(seg-55-61-94-word's "reprenne"-family, verdict null) — it kills only the
detachable-slot one-word-over-55-61 framing.

## Follow-ups proposed (kill verdict — no null follow-ups required; these
are the live redirect ends, both verified ABSENT from the queue)

1. **w1-55-61-reseg** (priority 3): re-test W1 under non-detachable
   segmentations (13-55-61 or 55-61-94 as one word, e.g. the
   "reprenne"/"reprennent" family); coordinate with seg-55-61-94-word's
   follow-ups, do not duplicate.
2. **w2-5561-nece-frame** (priority 3): W2's grammaticality is X-independent
   ("ne ce" hapax); fence W2 as a "ne ce"-driven residual, or test whether
   any 55-61 value parses once ne-ce-1169's fence is accounted for.

## Bookkeeping

- Report: code/crowd17/report_inbox/battery-x-55-61-candidate-list.md
- Queue: `x-55-61-candidate-list` queued -> verdict/kill via temp-file +
  rename (pre-write assert confirmed queued/verdictless; JSON re-validated
  post-write; own entry only; no downgrade).
- Lock created on start (2026-10-09T08:34:09Z), deleted on completion.
- `canonical.py` never used. R5005, sealed gates, red-team adjudication
  queue untouched.
