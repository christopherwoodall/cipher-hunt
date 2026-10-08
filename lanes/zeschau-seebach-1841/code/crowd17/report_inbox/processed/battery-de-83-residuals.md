# Battery report: de-83-residuals — the two hostile 83 cells under conditioned 83='de'

- Target id: `de-83-residuals` (priority 2)
- Claim: "Resolve the two newly-noted hostile cells under any surviving conditioned 83='de'"
- Date: 2026-10-08
- Worker: f3a15afe-5ffb-4ad4-af9c-ca5bb3ef5cdf
- Verdict: **promote** — both windows fenced with stated cause; adverses answered.
- Lock: created `code/crowd17/next-token/locks/de-83-residuals.lock` 2026-10-08T18:39:14Z, deleted on completion. No stale lock encountered.

## Bar (verbatim, pre-registered)

"both windows parse or are fenced with stated cause"

## Bar restated as numbered pass/fail clauses

1. @1334 ('39-83-86', stream-verified @1333=39/@1334=83/@1335=86, row a7_05 mid-row): parses under conditioned 83='de' or is fenced with stated cause.
2. @1829 (brief shorthand "'83-24'" corrected from stream: trigram is 38-83-24, @1828=38/@1829=83/@1830=24, row a8_11 mid-row): parses under conditioned 83='de' or is fenced with stated cause.

## Method

Parsed the repaired stream per code/side-keyhunt/repair_parse.py
(code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt):
1,847 pairs confirmed. Never used canonical.py. Never touched R5005.
No invented data; every number below traces to the stream.

Re-derived the 83 census: n(83)=15 at @228/@614/@898/@907/@911/@931/@1061/
@1161/@1171/@1217/@1334/@1612/@1784/@1829/@1840 — byte-identical to the
fence-911-de profile. Both target windows are mid-row (a7_05 spans
@1332–@1358; a8_11 spans @1822–@1846): no row-boundary artifact at either.

Standing values used: 39=/a/ promoted, allophone tier ("a"/"a"/word-internal
'a'; a-39 battery 2026-10-08, word-internal class demonstrated at 70-39-11
x2 "pre-a-la" -> "prealable"); 86 INF-class granted (infclass-86);
24 = finite verb, class-level promoted (ne-24-profile 2026-10-08);
70='pre' banked; 64='qui' granted; 94='ne' promoted; 30='pas' promoted.
38 and 52 are open (n(38)=7, n(52)=27; no standing value).

## Window-level evidence

### @1334 — row a7_05: `... 30 06 62 94 70 52 [39 83 86] 71 64 60 08 65 64 ...`

- Word-level reading "a de [INF]" (39='a'/'a', 83='de', 86=INF): ungrammatical
  as separate words — "a"/"a" + "de" never adjacent in French.
- Word-internal fork: 39=/a/ is promoted WITH word-internal 'a' as a
  demonstrated realization (a-39 battery: 70-39-11 "pre-a-la" x2). Reading:
  "[pre[52]a] de [86-INF]". "de + INF" is grammatical; 86=INF granted; the
  lane already treats 83-86 as "'de'+INF" (cf. @898) and the parvenir-thirds
  finder calls @1334's "'de'+INF core clean". The a-39 battery left @1334
  "neutral ('52 a 83')" — underdetermined, not hostile.
- The hostile reading REQUIRES 39 to be the separate word "a"/"a". The
  promoted allophone-tier status of 39 keeps the word-internal reading live,
  and under it the window is 'de'+INF-clean. The window therefore does not
  force 83 != 'de'.
- Residual, stated: the host word "pre[52]a" cannot be named while 52 is open
  (52's value unconstrained by any of its 27 windows in a way tested here).
  This is a named open value, not a contradiction.

### @1829 — row a8_11: `... 00 97 00 86 29 82 [38 83 24] 82 16 59 36 69 64 ...`

- 24 is a class-level promoted FINITE verb (ne-24-profile); right context
  `24 82 16` = modal + "m"(82) + INF-shaped ("peut me [dire]"-shaped).
- "de" + finite verb is ungrammatical in French under ANY 'de' hypothesis —
  this is grammar, not conditioning. So no word-level 83='de' reading can
  survive here, conditioned or not.
- Fence attempts, tested and broken:
  - (a) Clause boundary between 83 and 24 ("...38 de | [24]..."): strands
    "de" clause-finally. French has no preposition stranding. Broken.
  - (b) Quantifier + noun ellipsis ("38 de [O]" with elided noun): 38's value
    is open, but the only French quantifier fitting "38 de" with any support
    would be 'pas' — and 30='pas' is promoted (collision blocks 38='pas').
    No other quantifier candidate. Broken.
  - (c) 38-83 as one '-de'-final word (syllabic 83): live fork, but OWNED by
    queued syll-83-de (P3) — fenced to it here, not duplicated, not resolved.
- Consequence: @1829 is OUT of the word-'de' class. Any surviving conditioned
  83='de' excludes finite-verb followers as a matter of French grammar, so
  this window is not a counterexample to it — it is fenced as out-of-class,
  with 83's value here open (syllabic fork owned by syll-83-de).

## Per-clause verdict

- Clause 1 (@1334): PASS — fenced with stated cause. Hostility dissolved via
  the demonstrated word-internal-39 fork; "de+INF" core clean; residual is
  the named open host word (52), fenced to a follow-up below.
- Clause 2 (@1829): PASS — fenced with stated cause. Word-level 'de' impossible
  (24 finite, promoted; boundary and ellipsis fences tested and broken); the
  window is out-of-class for any surviving conditioned word-'de'; 83's value
  here is open with the syllabic fork fenced to queued syll-83-de.

## Verdict

**promote.** Both bar clauses pass (both windows fenced with stated cause);
every listed adverse is answered (below). No standing red-team verdict is
contradicted (none exists on 83='de'; the queued escalate-83-de-kill concerns
UNCONDITIONED 83='de' and is untouched).

Epistemic caveats, stated up front:
- The @1334 fence is conditional on the word-internal-39 fork, demonstrated
  as a class (70-39-11 x2) but not decided at this locus; the decider is 52's
  value (follow-up below).
- The @1334 fence dissolves if the red team kills the 83='de' lead outright
  (no conditioning survives). The @1829 fence is grammar-based and stands
  regardless of the adjudication.

## Adverses answered

- de-83-sweep (queued P3): coordinated, not duplicated. This battery's fences
  feed its 15-window sweep — @1334's host-word question (52) and @1829's
  out-of-class status are inputs; its global promote/kill verdict is not
  pre-empted here.
- frame-87-83-cede (queued P3): untouched. Neither target window involves
  87-83; the 'cede' fence is not re-litigated.
- syll-83-de (queued P3): @1829's '-de'-final-word fork explicitly fenced TO
  it, not resolved here — no duplication.

## Standing red-team check

No standing red-team verdict on 83='de' exists, so nothing is overwritten.
The queued escalate-83-de-kill (P1) owns the unconditioned-lead adjudication;
this report's conditioned-scope fences are consistent with it.

## Suggested next battery (optional; not a null follow-up)

- **profile-52-host-word** (P3): decide the "pre[52]a" host word at @1334.
  Bar: name a French "pre?a" lexeme governing "de+INF" (e.g. test
  52="scri" -> "prescrira de [INF]") across 52's 27 windows, or kill the
  word-internal-39 reading at @1334. Discriminating frames: 70-52-39 (@1334)
  vs 52-38-37 x2 (@383/@1343) vs 94-52-80 x2 (@1294/@1807).
