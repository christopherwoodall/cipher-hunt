# Battery verdict: poly-42-syllable-word — red-team INPUT package: the (a)-syllable vs (b)-word joint-unsatisfiability proof for 42

Date: 2026-10-09. Worker: 4e6a019b-2c5f-470a-bd72-c58e83b6264e (subagent).

Parent: follow-up #2 from the NULL verdict battery-noun-42-value (2026-10-09).
This battery is gather-only. It packages the parent's joint-unsatisfiability
proof as a second leg for the R20 42-polyvalence venue, alongside the
already-escalated nominal-vs-42ent question (stem-42-verb / "42 06" ×5).

## Bar (verbatim from battery-queue.json)

"evidence package delivered with byte citations; no class/split/value declared."

Numbered clauses (fixed before gathering):

- **C1:** Evidence package delivered with byte citations.
- **C2:** No class, split, or value declared. Adjudication belongs to the red team.

## Method

1. Read BATTERY-PROTOCOL.md first. Created
   `locks/poly-42-syllable-word.lock` on start; deleted on completion.
2. Re-derived the repaired stream in-session from
   `code/side-keyhunt/repaired_offsets.json` +
   `data/upstream-ct_R5005.txt` via `repair_parse.py`: 1,847 pairs, 96
   types, asserts held. `canonical.py` never used.
3. Adopted (never re-litigated): the parent's window-level census and
   candidate tests (noun-42-value NULL, 2026-10-09); val-42-nominal's
   PROMOTE of 42=["noun","cls"] (red-team granted R19-055); the adopted
   T3 fence ("29 42" word-internal, "laer"/"quer" not French); pencil
   29='er', 46='que', 11='la'; granted 94='ne', 59 (provisional 'est'),
   64='qui'.
4. Fresh in-session checks (this battery): byte-counts of the key bigrams
   on the repaired stream; corpus counts over
   `code/side-period/corpus/` (99 files; the 170-byte HTTP 500 stub
   `revue-deux-mondes-1840-q1.txt` excluded; 59,233,361 chars; NFKD
   accent-strip + lowercase; `\b…\b` letter-boundary matches).
5. R20 venue status checked against
   `code/crowd17/report_inbox/processed/next-token-redteam-r20.md`.

## Package contents

### 1. The (a)-syllable demand — "29 42" ×3

Byte-verified in-session: the "29 42" bigram occurs exactly 3×
stream-wide, at 29-positions 0-based @78, @218, @1143 (42 at
@79/@219/@1144). Windows:

- @79: `11 00 11 29 [42] 98 51 62` = "la pour la er → [42] vient …"
- @219: `06 59 46 29 [42] 16 24 89` = "ent est que er → [42] …"
- @1144: `78 62 16 29 [42] 98 98 86` = "ver [62] [16] er → [42] vient …"

Under standing values 29='er' (pencil GT) cannot be word-final here:
"laer" is a corpus zero (0 hits in 59.2M chars); the 119 standalone
"quer" hits are ALL hyphenated line-break artifacts ("man- quer",
"provo- quer" = "manquer", "provoquer" fragments), never the word
"quer". So at all three windows "er"+42 must be ONE word: 42 supplies a
syllable completing an "er-"-initial French word. **This is the syllable
demand (a).**

### 2. The (b)-word demand — standalone noun windows

The remaining windows require 42 as a standalone noun word (adopted from
the parent's census, counts re-verified in-session):

- T1 "42 94" ×3: @493, @784, @1794 ("[42] ne …" — 94='ne' STRONG LEAD is
  a standalone negator particle, forcing a word boundary after 42).
- T2 "est [42]" ×2: "59 42" ×2 at @463/@1186 ("tout ce la est [42]",
  "mentent est [42]" — predicative nominal complement, A1 frame).
- T4 "76 [42]" ×3: "76 42" ×3 at @427/@487/@1616 ("e le [76-noun] [42]
  …", "[76-noun] [42] [41]" — 76 is noun-class, so 42 is a second
  nominal element, a standalone word).
- Object slots: @205 (@205=42, "…[63-vb] [42] ent…" — verb-object
  contact), @266 ("[33-stem] [42] ent…"), @1503 ("on [33-stem] [42]
  [33]…").

**This is the word demand (b):** at these windows 42 is a standalone noun
word, incompatible with a sub-lexical syllable reading.

### 3. The "er"+C inventory exhaustion (the only bridge between (a) and (b))

The only way one value could satisfy both demands is an "er"+C shape
where C is independently a French word. Full inventory (parent's,
spot-verified against the 59.2M-char corpus this session):

| member | 'er'-word at T3 windows | standalone C | joint score |
|---|---|---|---|
| erreur / 'reur' | "l'erreur" ✓ (129 corpus hits) | bare "erreur" = corpus zero ("est erreur" 0, "c'est erreur" 0 — the register demands the determiner) | **1/20** |
| ermine / 'mine' | "l'ermine" = corpus zero | 'mine' attested (240×) but "tout cela est mine" ✗ | **1/20** |
| erre / 're' | "l'erre" = corpus zero | 're' attested (42×) but "tout cela est re" ✗ | **1/20** |
| ergot / 'got' | "l'ergot" = corpus zero | remainder not a French word | **0/20** |
| erratum / 'ratum' | unattested | remainder not a French word | **0/20** |
| ers / 'rs' | unattested | remainder not a French word | **0/20** |

No inventory member exceeds 1/20. (Obscure botanical "erbine" excluded
with cause by the parent: not standard French.) Spot-checks of other
noun families (masculine bare-capable, proper nouns) reached no candidate
above 2/20 — the bare argument positions reject determiner-needing
nouns and the predicative frames reject proper/profession nouns.

### 4. The joint-unsatisfiability finding

Demands (a) and (b) cannot be met by one value of 42:

- (a) forces 42 to be a **syllable** completing an "er-"-initial word
  ("29 42" ×3).
- (b) forces 42 to be a **standalone noun word** (T1/T2/T4/object slots).

The "er"+C inventory — the only compositional bridge — is exhausted at
≤1/20 per member. The corpus check this session hardens the T3 side:
among the six inventory members, only "l'erreur" is a real elided form
(129×), and bare "erreur" is a confirmed zero, so the single T3-fit
candidate dies at all 16 standalone windows. Resolving (a)-vs-(b)
requires either a second value for 42 (polyvalence — §7, red-team venue
only) or overturning the adopted T3 fence (red-team venue).

### 5. Relationship to the other venue leg (nominal-vs-42ent)

The already-escalated nominal-vs-42ent question rests on the "42 06" ×5
windows (@205/@266/@543/@1187/@1814, byte-verified in-session), where
06='ent' (3pl ending, granted-conditional R17-007) pulls 42 toward a
verb-stem reading against 42=["noun","cls"] (R19-055). This package is
the **second, independent leg** for the same venue: even within the
noun-class reading, (a)-syllable and (b)-word are jointly
unsatisfiable by one value.

### 6. R20 venue status

- "42 polyvalence venue | DEFER — the venue is a queued red-team
  target, not in this docket" (R20 report, §9 tally).
- R20-081 (val-42-det-gap): GRANT-WITH-CORRECTIONS — restricts 42's
  value inventory to bare-capable nouns (proper nouns adopted;
  pronoun-class 'rien'-family escalated per §5). This shrinks the (b)
  inventory further and is consistent with this package's exhaustion
  result.
- The companion redteam-42-tier-input package (delivered 2026-10-09)
  summarized: 42-06 escalated, 42-94 killed, 29/33 compositions fail at
  battery grade, 40 vacuous, 42-48 → val-42-282-fem KILL.

## Adjudication question for the red team (no declaration made)

1. Declare a §7 conditioned split/polyvalence for 42: (a)-syllable at
   the "29 42" ×3 windows vs (b)-standalone-noun elsewhere — alongside
   the already-escalated nominal-vs-42ent question.
2. Alternatively, overturn the adopted T3 fence (the "laer"/"quer"
   non-word evidence — note this session's finding that all 119
   standalone "quer" corpus hits are hyphenation artifacts).
3. Or keep both questions fenced and the 42 venue deferred.

## Per-clause results

- **C1: PASS.** Package delivered with byte citations above (all stream
  counts re-derived in-session on the repaired 1,847-pair/96-type
  stream; corpus counts from 59,233,361 chars of 1841 French with the
  HTTP 500 stub excluded).
- **C2: PASS.** No class, split, or value declared; nothing overturned.

## Scope

Gather-only. No bankable content beyond the record; §7 intact — no
polyvalence declared, no value named, no class granted. Untouched:
42=["noun","cls"] (R19-055), the adopted T3 fence, the 42-06 verb legs,
the R20 venue deferral, R20-081's det-gap restriction, all standing and
red-team verdicts. No contradiction or downgrade. Canonical-stream
caveat stands (row offsets in the cited windows unvalidated). Per the
gather-only precedent, no follow-ups proposed — the red-team venue owns
the next step.

## Verdict: NULL (gather-only package delivered)

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-poly-42-syllable-word.md`
  (this file).
- Queue: `poly-42-syllable-word` queued → `verdict`/`null`, 2026-10-09
  (pre-write assert passed — was queued/verdictless; target-id-unique
  tmp `battery-queue.json.poly-42-syllable-word.tmp` + atomic rename;
  disk re-validated; own entry only; no downgrade; no tmp leftover).
- Lock `code/crowd17/next-token/locks/poly-42-syllable-word.lock`:
  created on start, deleted on completion (verified gone).
- R5005, sealed gates, red-team adjudication queue untouched.
