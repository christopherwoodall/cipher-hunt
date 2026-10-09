# Battery report: neque-79-twin-frame

- Target id: `neque-79-twin-frame` (priority 3)
- Claim: "'13 {92|93} 62 94 79 14 60' is one licensed repeated frame; @1687 is its short close"
- Date: 2026-10-09
- Worker: battery worker (subagent aaae31d9-1849-4b89-8fe6-8c372db5f208)
- Stream: repaired 1,847-pair / 96-type parse re-derived in-session from
  `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`,
  parsed per `code/side-keyhunt/repair_parse.py` (asserts held: 1847 pairs,
  96 types). `canonical.py` never used. R5005, sealed gate instances, and the
  red-team adjudication queue untouched. @-offsets are 0-based pair indices.
- Parent: finder `neque-instance-sweep` (wave 3),
  `code/crowd17/report_inbox/next-token-findings-neque-instance-sweep.md`;
  grandparent battery `neque-bracket-verb-search` (NULL).

## Bar (verbatim from battery-queue.json, pre-registered BEFORE testing)

"(a) the same plaintext shape parses at both @1363 and @1687 under standing
values with the same 14/60 readings; (b) the @1363 44-pair interior contains
a licensed verb or clause head that the @1687 close lacks — the short close
must be consistent with the long close's structure, not with an invented verb"

Brief-variance note: the dispatch brief rendered (b) as "the @1363 44-pair
interior contains no contradiction under the stated frame". Per protocol §2
the queue's verbatim bar above is the one tested, not the brief's rendering.

## Numbered pass/fail clauses (fixed before data examination)

- **C1** (bar a): the plaintext shape "13 {92|93} 62 94 79 14 60" yields a
  grammatical parse under standing values, identical at @1363 and @1687,
  with 14 and 60 read the same at both loci.
- **C2** (bar b, part 1): the @1363 44-pair interior (@1364–@1407) contains
  a licensed verb or clause head that the @1687 4-pair close (@1688–@1691)
  lacks.
- **C3** (bar b, part 2): the @1687 short close is consistent with the
  @1363 long close's structure without inventing a verb.
- Verdict rule: PROMOTE iff C1+C2+C3 pass and both adverses answered. KILL
  iff a window forces the claim false or a distributional test rejects at
  the lane's standard. Else NULL.

## Method

1. Read BATTERY-PROTOCOL.md first. Created
   `code/crowd17/next-token/locks/neque-79-twin-frame.lock` on start
   (agent id + 2026-10-09T10:37:29Z); no stale lock present.
2. Re-derived the repaired stream byte-exact in-session; re-ran the
   finder's census claims independently ('94 79' adjacency, '79 14 60'
   trigram, pre-contexts, interiors).
3. Tested C1 by attempting every grammatically conceivable parse of the
   shared shape under standing values (pencil GT; granted 87=ce, 64=qui,
   96=par, 17=fois, 79=tout A5, 00=pour A9, 84=on A15, 47=ce A4;
   battery-promoted 94='ne' used as given per the adverse, never ratified;
   14='en' battery-promoted; 98 finite clause-head verb battery-promoted;
   24 finite-verb class R17-009; 46='que', 29='er', 82='m' banked).
4. Adopted without re-litigation: `npframe-60-detleft-closeout` (NULL —
   instance-B "ne…que" bracket's verb slot empty, fenced residual),
   `en14-value-tighten` (PROMOTE — 14='en', positive legs at exactly
   @1366/@1690), `ne-94-right-context` (PROMOTE — 94='ne' particle/syllabic
   split), `neque-bracket-verb-search` (NULL), `frame-62-94-79`
   (instance-B analysis).

## Window-level evidence (all byte-exact, re-derived)

### Locus geometry (finder's claims reproduced exactly)

- '94 79' adjacency: exactly 2x stream-wide, @1363 and @1687. CONFIRMED.
- '79 14 60' trigram: exactly 2x stream-wide, @1364 and @1688. CONFIRMED.
- @1363 (row a7_06): `… 64(qui) 35 | 13 92 62 94 79 14 60 03 30 82 16 91 67
  98 00 86 29 89 84 92 69 13 24 65 68 52 82 16 06 29 67 86 29 89 16 76 47
  78 48 40 67 77 81 87 11 00 11 95 | 46(que)@1408 …`
  Interior @1364–@1407 = 44 pairs. CONFIRMED.
- @1687 (row a8_05): `… 44 00(pour) 46(que) 79(tout) 65 | 13 93 62 94 79 14
  60 27 | 46(que)@1692 24 85 58 …`
  Interior @1688–@1691 = 4 pairs (`79 14 60 27`). CONFIRMED.
- Pre-contexts: "13 92 62 94" @1360–1363 (1x stream-wide); "13 93 62 94"
  @1684–1687 (1x stream-wide). CONFIRMED.
- Post-46: @1363 → `52 42 16`; @1687 → `24 85 58` (finder's contexts match).

### C1: parse attempts (all fail under standing values)

Standing glosses at both loci: `…[13] [{92|93}] [62] ne(94) tout(79) en(14)
[60] …`. 14='en' holds at both — the en14-value-tighten positive legs are
exactly @1366 ("[62] 94 tout en [60]") and @1690 (same frame). 60 is unnamed
at both; "tout en [60]" is the standing adverbial frame at both (same open
reading). The parse dies on 94:

- **Negator arm:** French "ne" must be immediately preverbal (clitics only).
  At both loci "tout en [60]" intervenes between "ne" and every verb
  candidate. Long candidates: 60 (blocked by "tout en"), 03@1367 (verb
  STEM, stem-03 promote — not finite), 98@1373 (9 groups away:
  "tout en [60] [03] [30] m' [16] [91] [67]" intervene — unreachable),
  24@1382 (unreachable). Short candidates: 60 (blocked), 27@1691 (stream
  hapax, class open — npframe-60-detleft-closeout C1), 24@1693 (across
  "que"@1692, a new clause — unreachable). No reachable finite verb at
  either locus.
- **Restrictive "ne … que" arm** ("only"): needs "ne" + verb. Same
  unreachable-verb defect at both loci.
- **Expletive-"ne" arm:** expletive "ne" sits AFTER "que" (comparatives,
  "avant que", "craindre que"); order here is "ne … que". Dead at both.
- **Syllabic/particle-94 arm** (ne-94-right-context's split): no licensed
  composition — "[62]ne", "netout", "netouten" are non-words; 62's and
  94's values are not composable under any standing license.
- **"Other-function" 94 arm:** the census's 11 other-function windows are
  window-specific; none licenses this configuration.

Result: no complete grammatical parse of the shared shape exists under
standing values at either locus. This is the same defect the parent
battery fenced ("the bracket's verb slot is empty under standing values:
'tout' cannot head it").

### C1, second defect: the {92|93} uniformity is unlicensed

For "one … frame", 92 and 93 must be frame-equivalent at the slot. Census:

- n(92)=22, n(93)=14.
- Shared (pre,fol) contexts: exactly ONE — ('13','62'), i.e. the twin
  loci themselves.
- 92 top predecessors: 00×6, 11×3, 94×2, 84×2. 93 top predecessors:
  45×3, 13×2, 15×2. Disjoint.
- 92 top followers: 79×2, 69×2, 60×2, 64×2, 62×2. 93 top followers:
  62×2, 52×2, rest singletons. Overlap: only '62'×2.
- The equivalence is supported ONLY by the data it is meant to explain
  (circular); the broader profiles diverge. Without 92~93, the "one frame"
  is two singleton 7-grams ("13 92 62 94 79 14 60" 1x; "13 93 62 94 79 14
  60" 1x) sharing the 4-gram "94 79 14 60" (2x).

**C1: FAIL** (no grammatical parse; uniformity premise unlicensed).

### C2: interior verb inventory (factually true, structurally inert)

- Long interior @1364–@1407 contains @1373=98 (finite clause-head verb,
  battery-promoted 'vient' profile) and @1382=24 (finite verb, R17-009
  class-level). Both licensed. The 98 heads its own separate licensed
  clause "98 00(pour) 86 29(er)" = "[vient] pour [86]er" (vient-complement
  inventory {de, pour, elided clitic}).
- Short close interior @1688–@1691 = `79 14 60 27`: no finite verb
  (79='tout', 14='en', 60 open, 27 hapax-open).
- So the long interior does contain licensed verbs/clause heads the short
  close lacks. **C2: PASS as a distributional fact.**

### C3: consistency test (fails)

The long interior's verbs do NOT license the "ne"-frame: "ne"@1363 cannot
govern 98@1373 or 24@1382 (non-adjacent; hard French preverbal-"ne"
constraint). The 98-clause is a separate licensed clause, not the
"ne"-bracket's head. There is therefore no licensed "long close
structure" for this frame — the long close is a fenced residual for the
"ne … que" frame exactly as the short close is. The short close's
"que [24]" (46='que' banked; 24 finite-verb class) opens a NEW subordinate
clause; it does not supply the "ne"-bracket's verb. A short close cannot
be "consistent with" a long-close structure that does not exist.

**C3: FAIL.**

### Adverses answered

- **@1363's interior formula contamination — fenced with stated cause.**
  The tail @1403–@1407 (`87 11 00 11 95` = "ce la pour la [95]") matches the
  cela-formula tail region (formula-tails finder T1, adopted from the
  finder report); per the beat method's de-duplication rule it is excluded
  from the licensing analysis. The C2 verbs (98@1373, 24@1382) sit well
  before the tail and are unaffected by the fence.
- **94='ne' stays battery-promoted pending ratification.** Used as given
  in every parse attempt above; never ratified, never re-litigated, never
  contradicted. This target makes no 94-value claim.

## Per-clause results

- C1 (same shape parses, same 14/60 readings): **FAIL** — "ne" has no
  reachable finite verb at either locus; 92/93 equivalence is circular
  (sole shared context is the twin itself).
- C2 (long interior has licensed verb the short close lacks): **PASS**
  (98@1373, 24@1382 licensed; short interior verb-less) — but the verbs
  belong to other clauses and do not license the "ne"-frame.
- C3 (short close consistent with long close's structure): **FAIL** — no
  licensed long-close structure exists for this frame at either locus.

## Verdict: NULL

The distributional twin is real — byte-identical "94 79 14 60" 2x
stream-wide with near-identical pre-contexts is a genuine observation,
and the finder is not overruled on the facts. But the frame is not
grammatically licensed at battery grade at either locus: the "ne"-bracket's
verb slot is empty at both, the long interior's licensed verbs (98, 24)
are not governed by "ne" and head other clauses, and the {92|93}
uniformity has no independent distributional support. This CONFIRMS the
parent battery `npframe-60-detleft-closeout`'s fence of the instance-B
"ne…que" frame as a residual; it does not overturn it. No standing or
red-team verdict contradicted or downgraded; §7 intact (no polyvalence
declared or needed). Canonical-stream caveat stands (rows a7_06/a8_05
offsets unvalidated).

## Follow-ups proposed (all verified ABSENT from battery-queue.json, 1012 targets)

1. `val-92-93-equivalence` (P3) — distributional equivalence test of 92~93
   under the lane's homophony standard (contact-profile overlap, n=22/14,
   current sole shared context ('13','62')). If rejected, the 7-gram "one
   frame" claim dies independently and the repetition reduces to the
   4-gram "94 79 14 60".
2. `neque-verb-slot-wide` (P3) — census the "ne … que" verb slot across
   all 16 nearest-46 "94…46" windows (finder's wider set): if the verb slot
   is empty in all 16 under standing values, fence the "ne…que"-bracket
   family as a systematic residual rather than a per-window accident.
3. `neque-79-rerun-gated` (P4) — gated re-run of this bar once the red-team
   60 docket names 60's class/value; a ratified verb-60 (or other named
   class) re-tests whether "ne [60]" becomes licensable with "tout en"
   reanalyzed.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-neque-79-twin-frame.md` (this file).
- Queue: `neque-79-twin-frame` → status `verdict`, result `null`,
  2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file +
  rename; JSON re-validated; own entry only; no downgrade).
- Lock `code/crowd17/next-token/locks/neque-79-twin-frame.lock`: created on
  start, deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
