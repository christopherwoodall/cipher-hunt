# Battery `de83-39-1334` — pre-register the 39-value collision check at @1334

- Worker session: battery-worker-de83-39-1334 (8b668f55-604e-435a-8166-7decb931fcf8)
- Date: 2026-10-09 (UTC 06:05 start)
- Lock: created `code/crowd17/next-token/locks/de83-39-1334.lock` on start, deleted on completion.
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
  `data/upstream-ct_R5005.txt`, parsed like `code/side-keyhunt/repair_parse.py`);
  1,847 pairs / 96 types re-derived in-session. `canonical.py` never used.
  R5005, sealed gates, red-team adjudication queue untouched.
- Evidence origin: `battery-de-83-sweep` NULL (2026-10-09), follow-up #2.

## Bar (verbatim from battery-queue.json)

"if 39='a/a' ever promotes, '39 83 86' = 'a de [INF]' becomes a new contradiction; test 39's open values against 'de' compatibility now"

## Bar restated as numbered pass/fail clauses (pre-registered before testing)

1. **C1:** the @1334 window is byte-exactly "39 83 86" on the repaired stream.
2. **C2:** 39's open values (from `battery-a-39` PROMOTE, pending ratification) are each
   tested for grammatical compatibility with 83='de' + 86 INF-class; the result is
   recorded as a conditional collision matrix.
3. **C3:** the record states the exact trigger condition under which the collision
   becomes a live contradiction (which values must ratify).

## Method

Re-derived the repaired stream in-session. Located "39 83" bigrams stream-wide.
Pulled 39's live value candidates from `report_inbox/processed/battery-a-39.md`
(PROMOTE, pending ratification: 39 = word "a", word "à", or word-internal letter
'a'; no other live candidate). Pulled 83's standing: `battery-de-83-sweep` NULL
(2026-10-09) — 83='de' is a lead at 11 non-contested windows, not a promote;
conditioned 'de' is red-team territory. Pulled 86's standing from
`code/table-grid/table-registry.json`: `86 -> ["INF", "cls"]`.
Tested each 39 reading against 1841 diplomatic French grammar at the window.

## Window-level evidence

- "39 83" is a **stream hapax**: exactly 1x, at 0-based @1333–1334.
- Window (0-based): @1332=52, **@1333=39, @1334=83, @1335=86**, @1336=71, @1337=64
  ('qui'), @1338=60, @1339=08, @1340=65, @1341=64 — all on row a7_05 (pos 0–9),
  fully mid-row; no row edge, gloss, or formula marker at contact.
- Under 83='de': the window reads "[39] de [86-INF]".

## Per-clause results

- **C1: PASS.** Byte-confirmed on the re-derived stream: @1333=39, @1334=83,
  @1335=86, row a7_05, mid-row.
- **C2: PASS.** Collision matrix under 83='de' + 86 INF-class:
  - 39 = word "a" (avoir 3sg): "a de [INF]" — **ungrammatical** in 1841 French.
    "avoir de + infinitive" is not a French construction (bare "a de parler"
    does not exist; "avoir de quoi + inf" is idiomatic and inapplicable).
    → **COLLISION.**
  - 39 = word "à" (preposition): "à de [INF]" — **ungrammatical** in 1841
    French. Prepositions do not stack "à de" before an infinitive (the
    partitive-de + noun construction, e.g. "prêt à de grandes choses",
    requires a noun, and 86 is INF-class, not a noun).
    → **COLLISION.**
  - 39 = word-internal letter 'a': compatible only if 39 composes leftward
    into 52's word ("[52-word]a de [INF]"). French common words ending in -a
    are vanishingly rare ("là", "déjà", loanwords); no 52 value statable
    under standing values supports this. Fenced as a narrow conditional
    rescue, not a clean reading.
  - No other 39 value is live, so no further arm is tested.
- **C3: PASS.** Trigger condition recorded below.

## Verdict: PROMOTE (finding grade — conditional-collision pre-registration)

The collision check is complete and on record. **If and only if BOTH
39='a/à' AND 83='de' ratify**, @1334 becomes a live contradiction ("a de
[INF]" / "à de [INF]" both ungrammatical) that must be resolved by re-tiering
one value, a word-boundary rescue, or red-team adjudication. Until then no live
contradiction is asserted — both values are unratified battery-grade claims.

## Adverse answered

- Queue adverse "39's value open (a-39 battery-promoted, pending ratification)":
  answered by the conditional structure — the collision is explicitly
  conditional, not asserted as a standing contradiction. 83='de' is likewise
  unratified (de-83-sweep NULL).

## Scope guards (not hidden)

- This promotes no value and no class: 83='de' stays a lead; 39='a/à' stays
  battery-promoted pending ratification; 86's INF class is untouched.
- **Phase caveat:** the "39 83" bigram is a canonical-stream hapax and is
  phase-fragile. Row a7_05 (55 digits, repaired offset 0, no gloss) sits on
  phase-uncertainty soil (−0.85 nats in `battery-phase-likelihood-row-sweep`,
  rival phase favored). Under a7_05's offset-1 re-parse the row yields 27
  pairs with **no 39 and no 83 at all** — the collision site dissolves.
  The pre-registration lives on the canonical stream per protocol.
- The conditional re-test (when 39 or 83 ratifies) is recorded here as the
  trigger; it is not queued as a separate target.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-de83-39-1334.md`
- Queue: `de83-39-1334` → status `verdict`, result `promote`, date 2026-10-09
  (temp-file + rename, pre-write assert passed, JSON re-validated).
- Lock created on start, deleted on completion.
- No standing verdict contradicted or downgraded; §7 intact.
