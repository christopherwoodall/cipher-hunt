# Battery `la-400-residual` — verdict: NULL (fence executed per the bar's else-arm)

## Bar (verbatim, pre-registered)

> "produce one grammatical 1841-French parse licensing @400 'la' as clause tail, or fence it as a canonical-offset object with the offset hypothesis stated"

Restated as numbered clauses (before testing):
- **C1:** one grammatical 1841-French parse licenses @400 'la' as clause tail under standing values (11='la' pencil preserved; no new values invented).
- **C2:** if C1 fails, fence @400 as a canonical-offset object with the offset hypothesis stated (no R5005 edit).

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`
(asserts: 1847 pairs, 96 types held). `canonical.py` never used. R5005, sealed
gates, red-team adjudication queue untouched.

Locus: 0-based @400, first pair of row a2_08 (row join @399|@400).
Window @390–411 byte-confirmed:

```
@390 91 | @391 84 | @392 73 | @393 34 | @394 67 | @395 64 | @396 79 |
@397 82 | @398 48 | @399 06 | @400 11 | @401 45 | @402 88 | @403 53 |
@404 34 | @405 69 | @406 26 | @407 00 | @408 33 | @409 01 | @410 02 | @411 53
```

Adopted standing values: 11='la' (pencil GT), 84='on', 34='i', 67='et'
(positional rule; follower 64 not infinitive-shaped), 64='qui', 79='tout',
82='m', 48='e', 00='pour', 46='que'. 45='ce' (A4/A11, demonstrative-pronoun
role per parent). 88 verb-class (battery grade). 06='ent' bound ending, but
@399's predecessor is 48, not 82 — outside the F61 licensed scope
(f61-06-scope-precise: pre=82 positions exactly @580/@738/@1184/@1355), so
@399 'ent' is unhosted. 91, 73 unvalued.

Parent's §6/B1a/B1b/B2 adopted as premises, not re-litigated: leftward
article reading dead (follower 45='ce'), leftward object-pronoun reading dead
(no imperative/infinitive host; post-verbal "-ent-la" after 3pl indicative
ungrammatical), B2 (11 non-'la') dead (pencil GT + §7).

## C1 — independent license attempt (FAIL)

Three remaining angles tested; all dead at battery grade:

1. **Article + elided noun.** Bare 'la' as article requires a following noun;
   follower is 45='ce'. An elided-noun rescue ("la [N]") invents the noun
   (§3). Dead.
2. **Object pronoun, rightward.** Next verb-class cell is 88 at @402, but the
   intervening 45='ce' breaks clitic position ("la ce [V]" ungrammatical;
   parent B4 killed the determiner frame here). No governing verb leftward
   either. Dead.
3. **Adverbial/interjectional 'là'.** The numeric cell cannot distinguish
   'la'/'là', so this angle gets maximal charity — and still fails. A
   deictic/interjectional 'là' clause tail ("mettez-le là"-shaped) needs a
   complete host clause. The left sequence @390–399 is not a clause at
   battery grade: @399 'ent' is unhosted (no F61 frame, no named verb stem
   precedes any 06 stream-wide per ent-06-host-214), and 91/73 are unvalued.
   'là' cannot tail a non-clause. Declaring 11='là' as distinct from 'la'
   would be an 11 polyvalence, barred by §7 (67 sole polyvalence) without a
   red-team act. Dead.

No grammatical 1841-French parse licenses @400 'la' as clause tail under
standing values. **C1 FAIL.**

## C2 — canonical-offset fence (FIRES)

Offset hypothesis, stated without touching R5005:
- @400 is exactly the head pair of row a2_08; the row join sits at @399|@400.
- a2_08's upstream offset is **1** (unvalidated — 68/70 upstream row offsets
  are unvalidated per the canonicality caveat). Raw head digits:
  `01145885334692600330`.
- At offset 0 the row head pairs as **"01 14 58 85 ..."** instead of
  "11 45 88 53 ...": the dangling '11' never appears.
- Flipping the offset changes the row's pair count (25 vs 24) and the stream
  total (1848 vs 1847), so the flip itself is sealed-gate/R5005 venue, not a
  battery decision. This battery states the hypothesis; it applies nothing.
- @400 'la' therefore joins the fenced canonical-offset-object list
  (parent §6: 43-21-43 frame, 81-30 @44-45, 78-40 bigrams, 77-62 singleton,
  @345, @1596, 86 problem windows, 78-45 loci). The upstream row boundary
  between @399 and @400 is recorded as a datum, not evidence.

**C2 FIRES.** Fence, not kill: a red-team offset adjudication or a future
named left-clause parse re-opens it.

## Adverses answered

- **11='la' pencil (do not revalue 11):** preserved. B2-style revaluation
  rejected; no 11 polyvalence declared (§7).
- **Do not touch R5005:** honored. No stream edit; the offset-0 alternative
  is a stated hypothesis only.

No standing/red-team verdict contradicted or downgraded; §7 intact;
canonical-stream caveat stands (rows a2_07/a2_08 offsets unvalidated).

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `a208-offset-package` (P4) — package the offset-0 vs offset-1 evidence
   for row a2_08 (pair counts, head-digit pairings, downstream consequences)
   as a red-team input; the 1847-vs-1848 total makes this canonicality
   venue, not battery.
2. `la-400-interjection-corpus` (P3) — corpus test: does bare
   interjectional "là/la" occur clause-finally in 1841 French dialogue?
   A genuine licensed pattern re-opens the C1 arm.
3. `left-399-clause-parse` (P3) — parse the @390–399 left sequence as a
   complete clause; a licensed full clause sharpens (or dissolves) the
   tail question independent of the offset hypothesis.

## Bookkeeping

- Report: code/crowd17/report_inbox/battery-la-400-residual.md (this file).
- Queue: `la-400-residual` → `status: verdict`, `result: null`, 2026-10-09
  (pre-write assert passed — was queued/verdictless; temp-file + rename;
  JSON re-validated; own entry only; no downgrade).
- Lock created on start, deleted on completion (verified gone). R5005,
  sealed gates, red-team adjudication queue untouched.
