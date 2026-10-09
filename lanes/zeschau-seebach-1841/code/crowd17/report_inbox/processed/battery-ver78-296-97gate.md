# Battery report: ver78-296-97gate

Target: ver78-296-97gate | priority 3
Claim: "the @296 re-parse re-runs cleanly once frame-97-profile AND stem-86 have verdict"
Worker: 8451e519-50df-4064-b643-141babba38e4 | 2026-10-09

## Bar (verbatim, pre-registered)

"(a) 97 and 86 values/frames taken from their verdict batteries; (b) the one-word read demonstrated, or the residual re-fenced with the then-current failure stated"

## Bar restated (numbered pass/fail clauses; frozen before testing)

1. 97 and 86 carry the values/frames given by their own batteries
   (frame-97-profile, stem-86 — both at verdict, not re-litigated here).
2. The string 11-78-40-97-86 (@296..@300) reads as one French word under
   the licensed frames — or the residual is re-fenced with the then-current
   failure stated.

## Method

Read BATTERY-PROTOCOL.md first; created `locks/ver78-296-97gate.lock` on
start (deleted on completion). Re-derived the repaired 1,847-pair /
96-type stream in-session from `code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`, parsed exactly like
`code/side-keyhunt/repair_parse.py` (stride-2 pairing per row offset);
asserted 1,847 pairs, 96 types. `canonical.py` never used. R5005, sealed
gates, red-team queue untouched. @-offsets are 0-based stream indices.

## Clause 1 — frames taken from the verdict batteries: PASS

The gate adverse ("do not force before both batteries verdict") is
ANSWERED: both batteries are at verdict.

- **frame-97-profile (PROMOTE, 2026-10-08):** 97 is INFINITIVE class
  (seven frame-legs over six windows; "pour 97" x4, "97 que", "80 97",
  "pour 97 pour 86er" parallel). Value open, not named. The 97-86 @299
  contact fenced as hapax/distributionally inert.
- **stem-86 (NULL, 2026-10-08):** no single value parses all 32 windows.
  86='le' dead as a global value at kill grade (#0 "ce le", #6 "la le").
  Residue: determiner-life vs stem-life. Standing frames adopted from
  verdicts: A9 INF-class grant, R17-012 substantivized-infinitive/noun
  frame ('le 86' x5).

Frame-97-profile's unlock note required only that stem-86 reach verdict
("stays gated until stem-86 ... runs"); stem-86 ran and verdict
NULL satisfies the queue bar's "have verdict" wording.

## Window re-derived (@296..@300, bytes)

- @296: 11 (row a2_03, last pair of the row)
- @297: 78 (row a2_04) — row boundary between @296 and @297
- @298: 40 | @299: 97 | @300: 86
- Right tail: 91 18 89 88 02 88 20 17 46 84 ...

So the 5-gram is "11 78 40 97 86" = "la" + "ver" + "e" + [97-INF] + [86],
under 11='la' (banked GT pencil), 40='e' (banked GT), 78='ver' LEAD
(R16-005/R17-006). Confirmed: the 97-86 bigram at @299 is a stream hapax
(re-derived; 86-97 x0).

## Clause 2 — one-word read demonstrated? FAIL; residual re-fenced

Lexical families admitted by "la"+"ver"+"e"+[97]+[86] (lexical sweep
adopted from battery-ver78-296-reparse, re-checked under the new frames):

1. **"lavèrent"** (requires 97='n', 86='t'): DEAD under the new licensed
   frames. 97='n' contradicts frame-97-profile's PROMOTE (97 is
   infinitive-class: "pour 97" x4 bare-infinitive slots, infinitive-
   parallel "pour 97 pour 86er"; a letter reading is not an infinitive)
   and was independently killed ("pour n" ungrammatical; collision with
   promoted 12='n' with no homophone test). 86='t' fails "pour 86" x12
   and the A9 INF-class frame. Re-reading 97 as a letter at this locus
   would declare a second 97-value = §7 polyvalence, a red-team act.
2. **"véreux"/"véreuse"** (requires 97+86 = "use"/"ux"): DEAD. 97='u' or
   'us' fails the "pour 97" x4 frame exactly as above; 86='s' fails the
   "pour 86" x12 frame. "la véreuse" is two words anyway, and noun-less.
3. **"laver"+...** (11+78+40 = "laver"): DEAD — 11='la' is pencil ground
   truth; composing it as the letters "la" of "laver" contradicts a
   banked GT value. Closed.
4. **Multi-word parses** ("la ver-e [INF] [86]", "la vere [INF] [86]"):
   DEAD — "vere" is not a French word (battery-lere-296-rival, kill).

New battery-state compared to ver78-296-reparse: the 'l'ere' rival read
is now DEAD at kill grade (battery-lere-296-rival, 2026-10-09) — the
residual no longer has a rival parked beside it. What remains is the
fenced 1-window residual with no licensed completion.

**The re-parse does NOT run cleanly.** The residual is RE-FENCED with
the then-current failure stated:

- (i) 97 carries a licensed CLASS (infinitive) but no value; every
  French completion of the 5-gram requires a letter/syllable 97
  ('n', 'u', 'us') that the infinitive-class PROMOTE forbids at this
  locus (§7: no second 97-value declared here).
- (ii) 86 carries no licensed value (stem-86 NULL; 'le'-global killed
  at #0/#6; INF-class frames give no value at this locus).
- (iii) The 'l'ere' rival is dead, so the fence no longer rests on the
  rival — it rests on (i)+(ii).
- (iv) R16-005 fence respected: @296 stays the red-team-fenced
  1-window residual; nothing in R16-005/R17-006/R17-014 is contradicted
  or downgraded.

Phase caveat (stated, not hidden): the 5-gram STRADDLES a row boundary
(a2_03 ends @296, a2_04 begins @297). Under a2_04's rival offset-1 the
"97 86" contact dissolves (legal re-parse, zero novel groups); the
residual is a canonical-offset object, like seg-a1_01/reseg-1481-98/
frame-43-21-43-doublet. Per protocol the fence is tested on the
repaired stream; the canonicality caveat stands. Revival requires a
licensed 97/86 completion or a byte-anchored offset.

## Adverses answered

- "gate only — do not force before both batteries verdict": ANSWERED —
  both batteries verdict (frame-97-profile PROMOTE 2026-10-08,
  stem-86 NULL 2026-10-08). Nothing was forced.

## Verdict: NULL

Not promote: neither bar clause's positive arm passes — the one-word
read is not demonstrated under the licensed frames. Not kill: no window
forces the claim false; @296 stays compatible with 78='ver' as the
R16-005-fenced 1-window residual. The residual's fence REASON updates
per clause 2(iii): fenced for lack of a licensed 97/86 completion,
not for the (now-dead) 'l'ere' rival. No standing verdict contradicted
or downgraded; §7 intact (no polyvalence declared).

## Follow-up targets (null regenerates work)

1. **rere-296-residual** (P4): post-rival re-examination of @296's
   fence reason — track whether a licensed 97/86 completion ever
   emerges (97 value batteries, 86 'le'-life splits). Bar: re-run the
   clause-2 lexical sweep iff any battery names a 97 value or an 86
   value completing "vere..."; else keep the residual fenced.
2. **reseg-a2_03-a2_04-97gate** (P3): offset-1 constraint sweep of rows
   a2_03/a2_04 — the 5-gram straddles a row boundary and is
   phase-fragile. Bar: clean across the full window iff the rival
   phase preserves every pair with zero novel groups; fence iff the
   contact dissolves or a novel group appears. (Third candidate of the
   same mechanism family as seg-a1_01/reseg-1481-98/frame-43-21-43-
   doublet.)

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-ver78-296-97gate.md`
  (this file)
- Queue: `battery-queue.json` → `ver78-296-97gate` status `verdict`,
  result `null`, date 2026-10-09 (temp-file + rename; pre-write assert
  confirmed `queued`/verdictless; JSON re-validated post-write;
  no other entry touched; no verdict downgraded)
- Lock: created on start, deleted on completion
- `canonical.py` never used; R5005, sealed gates, red-team queue
  untouched
