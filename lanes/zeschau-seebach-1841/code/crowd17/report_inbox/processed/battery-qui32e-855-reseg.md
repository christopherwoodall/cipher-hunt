# Battery report: qui32e-855-reseg

- Target id: `qui32e-855-reseg`
- Claim: "re-segmentation sweep at @855"
- Date: 2026-10-09
- Worker: battery worker (subagent a24b6434-1e9f-41fb-998d-9ae0cb1237ca)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py;
  1,847 pairs / 96 types asserted in-session). All @-offsets are 0-based
  repaired-stream pair indices. `canonical.py` never used. R5005, sealed
  gates, red-team adjudication queue untouched.

## Context

@855 is the fem-32e residual: "qui 32e on" — the only one of the four
"32 48" windows (byte-verified in-session: exactly 4, @449/@855/@1176/@1211)
whose morphology ("32e", intact) admits no grammatical parse under
adjective-32. Standing: 48='e' is an R17 letter-tier grant, classified
word-final/stem-bound at @856 per fem-e-48; 64='qui' granted; 84='on'
A15; 32's adjective arm unresolved (adj-32 NULL); 32's verb-lexeme class
battery-PROMOTED (verb-32, pending red-team ratification). This battery
adopts both 32-arm standings as premises, re-litigates neither.

## Bar (verbatim from battery-queue.json, pre-registered before testing)

"test 48='e' positionality at this window and exhaust byte-evidenced clause
boundaries; either kill the residual or promote the fence"

Numbered clauses (restated before testing, not modified after):

1. (C1) 48's positionality at @855–856 is decided on bytes: word-final
   (stem-bound to 32), word-internal/word-initial, or standalone.
2. (C2) All byte-evidenced clause boundaries around the residual are
   exhausted; each is shown grammatical (with stated conditions) or dead.
3. (C3) The residual is killed at kill grade, or the fence is promoted
   (with the surviving conditional leg stated).

## Method

1. Re-derived the repaired parse in-session; asserted 1,847 pairs / 96 types.
   Never used canonical.py.
2. Byte-confirmed the window: @853=51, @854=64(qui), @855=32, @856=48(e),
   @857=84(on), @858=02, @859=24 — all on row a5_07 (canonical offset 1).
3. Tested 48's positionality against the letter-tier grant and French
   phonotactics; enumerated clause-boundary positions under standing values
   only.

## Window-level evidence

### C1 — 48's positionality

- **Word-final, stem-bound to 32: HOLDS.** Matches fem-e-48's standing
  classification and the letter-tier grant; morphology "32e" intact, same as
  the other three windows.
- **Standalone "e": KILLED.** No French word "e" exists in 1841 French;
  "qui 32 e on" parses nothing.
- **Word-initial ("e on…"): KILLED.** "e" as a word-initial letter gives
  no French word at @856–857 ("eon" is not a word); 34='i' is the only
  standalone letter-value tier and 48 is 'e', not 'i'.

### C2 — clause boundaries exhausted

- **Boundary between 64|32: DEAD.** "qui" is a relative pronoun; it must
  attach to a verb. Splitting "qui | 32e" is ungrammatical value-independently.
- **Boundary after 48 ("qui 32e | on 02 24…"): CONDITIONAL.** Left core
  "51 qui 32e" parses cleanly iff 32 is verb-class: "51 [32-V]e" =
  noun + "qui" + finite verb (3sg -e), with 48 as verbal inflection — the
  same morphology the letter grant requires. This is admissible at battery
  grade: verb-32 is battery-PROMOTED (pending red-team ratification).
  Right edge "on 02 24…" stays fenced (02 open; 02's adverb arm fenced in
  adv-02-858), so the boundary shape is a conditional leg, not a full parse.
- **Boundary before 64 ("…51 | qui 32e on"): DEAD for the left core.**
  "qui" still needs a verb under standing values; nothing changes.
- **Boundary after 84 ("qui 32e on | 02 24…"): DEAD for the left core.**
  Right-edge licensing doesn't rescue "qui 32e" under adjective-32.
- **"qui 32e on" as one clause: DEAD** under adjective-32 (stated fence from
  fem-32e; 64=qui granted needs a finite verb, 32-adjective can't supply one).

The exhaustive set reduces to one live shape: **48 word-final/inflectional
+ 32 verb-class + clause boundary after 48.**

### C3 — kill vs fence

The residual is **not** killed: the verb-32 conditional leg parses
"51 qui [32-V]e" with zero new assumptions beyond the battery-promoted
32-verb class. The fence is therefore **promoted** with the conditional leg
stated. No value was named; no standing or red-team verdict contradicted
or downgraded; §7 intact (no polyvalence declared — 32's adjective/verb
arms remain unresolved at battery level, which is exactly the fence).

## Per-clause pass/fail

1. C1 PASS — 48 is word-final, stem-bound; the two rival positionalities
   are kill-grade dead.
2. C2 PASS — four boundary positions tested; three dead, one conditional
   on battery-promoted 32-verb-class.
3. C3 PASS — residual not killed; fence promoted with stated conditional leg.

No adverses listed in the queue entry.

## Verdict: PROMOTE (of the fence, battery grade)

@855's fence is promoted with the stated conditional leg: "51 qui [32-V]e |
on…" parses under battery-promoted verb-32 (pending red-team ratification).
The residual's survival condition is now explicit: if the red team
ratifies 32-verb-class, the @855 residual dissolves into a clean relative
clause; if 32 resolves adjective-only, the fence stands.

## Caveats

- 32-verb-class is battery-promoted, not red-team-ratified; the leg is
  battery grade only.
- Right edge "on 02 24…" is fenced, not parsed (02's value open; adv-02-858
  NULL).
- Row a5_07 carries unvalidated upstream offsets (canonicality caveat).

## Optional follow-up candidates (not required — verdict is promote)

- `val-32-verb-e-paradigm` (P3): find a second "32 48" or "qui 32" verb-frame
  window to license the 3sg "-e" verb reading independently.
- `on02-24-frame` (P3): license the right edge "on [02] [24]" once 02's
  class resolves.

## Bookkeeping

- Report: code/crowd17/report_inbox/battery-qui32e-855-reseg.md
- Queue: `battery-queue.json` → `qui32e-855-reseg` status `verdict`,
  result `promote`, date 2026-10-09 (pre-write assert confirmed no prior
  verdict; temp-file + rename; JSON re-validated; only this entry touched)
- Lock created on start, deleted on completion.
- R5005, sealed gates, red-team adjudication queue untouched.
