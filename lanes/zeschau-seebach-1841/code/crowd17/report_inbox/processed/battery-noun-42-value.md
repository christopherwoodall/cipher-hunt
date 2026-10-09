# Battery verdict: noun-42-value — name 42's value from its 20 windows

Date: 2026-10-09. Worker: 8f07bcbb-a1c1-4c2e-b3f5-noun42worker.

Parent: `par-42-complement` (verdict null, 2026-10-09), follow-up #1. The parent
fenced the "est [42] par …" leftward route (complement-side failure: "par pour"
is a 34.55M-char corpus zero) and left 42's value open.

## Bar (verbatim from battery-queue.json)

"name one value fitting >=3 of the 20 windows with battery-grade evidence,
else fence the value route"

Numbered clauses (fixed BEFORE the window census, not modified after):

- **C1:** Name one specific French value for 42 that fits >=3 of its 20
  windows with battery-grade evidence — clean grammatical parse under
  standing values, <=1 ungranted assumption per window, no invented
  grammar or values (§3).
- **C2 (else-arm):** Fence the value route with stated cause.

## Method

- Re-derived the full 1,847-pair / 96-type stream from
  `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`
  (parse per `code/side-keyhunt/repair_parse.py`; asserts held: 1,847 pairs,
  96 types). `canonical.py` never touched.
- Full 20-window census of 42 re-derived (0-based @79/@205/@219/@266/@282/
  @428/@464/@488/@493/@543/@784/@1072/@1144/@1187/@1410/@1503/@1617/@1794/
  @1814/@1838 — byte-identical to the parent's list).
- Adopted (never re-litigated): 42=["noun","cls"] (val-42-nominal PROMOTE,
  red-team granted R19-055); A1 predicative frame; T3 "29→42" fence with
  word-internal "er[42]" as the live rival (val-42-nominal); the 42-06 verb
  legs as the escalated polyvalence question (§7, red-team venue, no venue
  yet per R19-415); pencil 11=la, 29=er, 46=que; granted 87=ce, 96=par,
  00=pour (A9), 79=tout, 84=on, 47=ce; provisional 59=est; R24 (24
  finite/modal iff follower != 85).
- Corpus test for the leading candidate over the lane's 1841 diplomatic
  corpus (`code/side-period/corpus/`, 76 files, 34,437,222 chars):
  NFKD accent-strip + lowercase, hyphenated line-breaks joined,
  letter-boundary matches (per R19-193).
- R5005, sealed gates, red-team adjudication queue untouched.

## Window-level evidence (0-based @-offsets, ±4 context)

| @ | context | left frame | right frame |
|---|---------|-----------|-------------|
| 79 | 11 00 11 29 [42] 98 51 62 | la pour la er→ | →98 |
| 205 | 87 11 92 63 [42] 06 77 44 | ce la [92] [63-vb]→ | →ent |
| 219 | 06 59 46 29 [42] 16 24 89 | ent est que er→ | →16 |
| 266 | 45 93 52 33 [42] 06 73 47 | [93] [52] [33-stem]→ | →ent |
| 282 | 37 61 20 61 [42] 48 52 89 | [61] [20] [61]→ | →e |
| 428 | 14 62 48 76 [42] 63 77 86 | [62] e [76-noun]→ | →[63-vb] |
| 464 | 79 87 11 59 [42] 96 00 33 | tout ce la est→ | →par pour [33] |
| 488 | 01 19 64 76 [42] 41 20 67 | [19] qui [76-noun]→ | →41 |
| 493 | 41 20 67 78 [42] 94 02 79 | [78]→ | →ne [02] |
| 543 | 12 44 29 48 [42] 06 00 46 | [44] er e→ | →ent |
| 784 | 29 89 11 24 [42] 94 74 65 | er [89] la [24-fin]→ | →ne [74] |
| 1072 | 39 11 44 74 [42] 98 98 12 | [44] [74]→ | →98 98 |
| 1144 | 78 62 16 29 [42] 98 98 86 | [62] [16] er→ | →98 98 |
| 1187 | 82 06 06 59 [42] 06 84 59 | m ent ent est→ | →ent on est |
| 1410 | 11 95 46 52 [42] 16 97 69 | la [95] que [52]→ | →16 |
| 1503 | 41 74 84 33 [42] 33 00 86 | [74] on [33-stem]→ | →[33] pour |
| 1617 | 71 48 31 76 [42] 44 11 84 | [48] [31] [76-noun]→ | →44 |
| 1794 | 03 00 86 56 [42] 94 59 37 | pour [86] [56]→ | →ne est [37] |
| 1814 | 61 15 93 50 [42] 06 29 37 | [93] [50]→ | →ent er |
| 1838 | 36 69 64 22 [42] 44 83 21 | [69] qui [22]→ | →44 |

Structural demands on any single value V:
- (a) "29 42" ×3 (@79/@219/@1144): 29='er' cannot be word-final here
  ("laer"/"quer" not French — adopted fence), so "er"+V is ONE word:
  V completes an "er-"-initial word (syllable demand).
- (b) T1 "42 94" ×3 (@493/@784/@1794), T2 "est [42]" ×2 (@464/@1187),
  T4 "76 [42]" ×3 (@428/@488/@1617), object slots (@205/@266/@1503):
  V is a standalone noun word (word demand).

## Candidate tests (C1)

**V='erreur' (f.)** — the T3-driven candidate ("l'erreur" at @79):
- @79: "la pour l'erreur [98]" — FIT, 0 ungranted assumptions (elision
  "la"→"l'" is standard French orthography; the lane already practices
  "ne"+"est"→"n'est" elision, cf. subj-42-ne-frame).
- All 16 standalone windows: 'erreur' as a BARE noun in subject /
  predicate / object slots. Corpus test (34,437,222 chars): bare "erreur"
  is a ZERO — "c'est erreur" 0, "est erreur" 0, "erreur ne" 0,
  "erreur n'est" 0, "erreur est" 0 — against "l'erreur" 86×. The register
  requires the determiner; the windows supply none. KILL at every
  standalone window.
- Score: **1/20**. FAIL.

**"er"+C inventory exhaustion** — every French noun of shape "er"+C where
C is independently a French word (so V=C could satisfy both (a) and (b)):
- erreur/reur — 'reur' not a word; as full word: 1/20 (above).
- ermine/mine — 'mine' is a word. @79 "l'ermine" FIT; @464 "tout cela
  est mine" ✗; @1794 "mine n'est" bare ✗. 1/20.
- erre/re — 're' is a word (musical note). @79 "l'erre" FIT; standalone
  windows ✗ ("tout cela est re"). 1/20.
- ergot/got, erratum/ratum, ers/rs — remainder not a French word. 0/20.
- (Obscure botanical "erbine" excluded with cause: not standard French.)
- Score: no inventory member exceeds **1/20**. FAIL.

**Spot-checks of other noun families** (masculine bare-capable, proper
nouns): every candidate either needs a determiner the windows lack
(T1/T2/T4/object slots are bare) or fails the predicative frames
(@464 "tout cela est X" rejects proper nouns and profession nouns
semantically). No candidate reaches 2 clean fits, let alone 3.

**Joint-unsatisfiability finding:** demands (a) and (b) cannot be met by
one value. (a) forces V to be a syllable completing an "er-"-word; (b)
forces V to be a standalone noun word. The "er"+C inventory (the only
bridge) is exhausted at 1/20 per member. Resolving (a)-vs-(b) requires
either a second value for 42 (polyvalence — §7 bars; red-team venue only,
and distinct from the already-escalated nominal-vs-42ent question) or
overturning the adopted T3 fence (red-team venue).

## Per-clause results

- **C1: FAIL.** Best candidate 'erreur' fits 1/20; the "er"+C inventory
  is exhausted with no member above 1/20; no other noun family reaches 3.
  Naming any value would invent data (§3).
- **C2: EXECUTED — the value route is FENCED** with stated cause:
  (i) the only compositionally evidenced value ('erreur' via "er[42]" ×3)
  is corpus-killed as a bare noun at all 16 standalone windows
  (34.4M-char zero vs "l'erreur" 86×); (ii) the standalone windows select
  no value (any noun merely compatible — cf. val-42-estframes); (iii) the
  syllable demand (a) and word demand (b) are jointly unsatisfiable by one
  value.

## Fence scope

- Fences ONLY the battery-grade value-naming route for 42. Untouched:
  42=["noun","cls"] (R19-055 grant); A1 predicative frame; the adopted T3
  fence and its "er[42]" rival; the 42-06 verb legs and their escalated
  polyvalence question; the queued compositional targets
  (val-42-erreur — 'reur' SYLLABLE hypothesis, distinct claim, consistent
  with this fence; val-42-lettertier; val-42-282-fem; val-42-ne-noun;
  subj-42-class; w2-42-94-24en-gate).
- Coordination note for val-42-erreur: 'erreur'-as-full-word is dead
  (corpus zero above); that target's syllable-only reading is unaffected.
- No standing/red-team verdict contradicted or downgraded; §7 intact; no
  polyvalence declared. Canonical-stream caveat stands.

## Verdict: NULL (fence executed per the bar's else-arm)

## Follow-up targets (null regenerates work; all verified ABSENT from battery-queue.json)

1. `val-42-det-gap` (P3) — census determiner adjacency across 42's 20
   windows ("le/la/ce/un" cells immediately left of 42). Bar: if 42 is
   systematically determiner-less in argument positions, restrict the
   value inventory to bare-capable nouns (proper nouns, pronoun-class
   "rien"-family — the latter contradicts R19-055, so report as
   contradiction-headline null per §5 if it fires); else fence the
   restriction.
2. `poly-42-syllable-word` (P3) — red-team INPUT package (battery gathers
   only, no adjudication): the (a)-syllable vs (b)-word joint-
   unsatisfiability proof with the exhausted "er"+C inventory, as a second
   leg for the R20 42-polyvalence venue alongside the already-escalated
   nominal-vs-42ent question. Bar: evidence package delivered with byte
   citations; no class/split/value declared.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-noun-42-value.md` (this file).
- battery-queue.json: `noun-42-value` queued → verdict/null via temp-file
  + rename (own entry only; pre-write assert confirmed queued/verdictless;
  JSON re-validated post-write; no downgrade).
- Lock `code/crowd17/next-token/locks/noun-42-value.lock`: created on
  start, deleted on completion.
- R5005, sealed gates, red-team adjudication queue untouched.
