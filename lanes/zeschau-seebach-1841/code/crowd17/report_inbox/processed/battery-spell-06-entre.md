# Battery report: spell-06-entre

- Target id: `spell-06-entre`
- Claim: "resolve the 'entreprenne' spelling hole — census 06-initial words for an 'entre' value vs 06='ent'"
- Date: 2026-10-09
- Worker: battery worker (subagent 1d3c5d94-78db-4fb0-9814-63e7269ad58a)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py;
  n=1847 asserted, 96 types asserted). All @-offsets are 0-based repaired-stream indices.
  `canonical.py` never used. R5005 not touched.
- Lock: code/crowd17/next-token/locks/spell-06-entre.lock (created at start,
  deleted on completion; no prior lock existed).

## Bar (verbatim, pre-registered before testing)

"if no "entre" license exists, kill the @346–349 verb-ID leg (ent-06 F3's "value evidence, not ending evidence" claim falls with it)"

Numbered pass/fail clauses (restated before testing, not modified after):

1. (C1) Census 06-initial words stream-wide for an "entre" value vs 06="ent":
   enumerate every 06 window and test whether any licenses 06 spelling "entre"
   (as word-initial syllable of a longer word, or as a standalone word).
2. (C2) Determine whether an "entre" license exists independently of the
   @346–349 leg itself (the leg cannot license itself).
3. (C3) If C2 finds no "entre" license, KILL the @346–349 verb-ID leg at kill
   grade; ent-06 F3's "value evidence, not ending evidence" claim falls with it.

## Background: the spelling hole

ent-06 F3 (code/crowd17/report_inbox/processed/battery-ent-06.md:43) reads
@346–349 as:

> "06-70-12-94" = "entreprenne". 06='ent' + 70='pre' + 12='n' + 94='ne' =
> "entreprenne", 3sg subjunctive of entreprendre ("[01] entreprenne [74]" —
> verb ID solid; "Uses 06='ent' word-initially: value evidence, not ending
> evidence").

Byte verification (re-derived in-session): @346=06, @347=70, @348=12, @349=94,
all row a2_05 pos 22–25, consecutive; context @344–350 = "87 01 06 70 12 94 74".

The equation is misspelled. Concatenating the stated values:

- 06="ent" (e,n,t) + 70="pre" (pencil GT) + 12="n" (per the "70-12-94"="prenne"
  battery) + 94="ne" (R17-001 STRONG LEAD)
- = "ent" + "pre" + "n" + "ne" = **"entprenne"** (e,n,t,p,r,e,n,n,e — 9 letters)

"entreprenne" is e,n,t,r,e,p,r,e,n,n,e (11 letters). "entprenne" ≠ "entreprenne":
the leg's spelling omits the "re" syllable. For the four groups to spell
"entreprenne", 06 must carry **"entre"** (5 letters): "entre"+"pre"+"n"+"ne" =
"entreprenne". The F3 leg therefore silently requires 06="entre" — a value
distinct from the promoted single value 06="ent" (ent-06 PROMOTE; re-confirmed
"single value; no polyvalence" by 06-forces-84 C2 and the ent-06-host-census
decision rule).

Rescue attempts exhausted (all dead without inventing values or contradicting
standing verdicts):

- 70≠"pre": 70="pre" is banked pencil ground truth — not re-litigated.
- 12="re": gives "pre"+"re"+"ne"="prerene", contradicting the established
  "70-12-94"="prenne"; still would not yield "entreprenne" with 06="ent".
- 94≠"ne": R17-001 94="ne" STRONG LEAD; no alternative yields a French word.
- Word boundary "ent | prenne": "ent" is not a French word.
- "01 06" as a unit ("01"="entr", 06="e"): contradicts promoted 06="ent";
  pure invention.

## Census: 06-initial words (C1)

n(06) = 44 stream-wide (@6/@85/@184/@206/@215/@267/@271/@319/@346/@370/@399/
@470/@522/@544/@580/@581/@666/@738/@773/@789/@890/@967/@1080/@1091/@1096/
@1120/@1122/@1184/@1185/@1188/@1252/@1328/@1355/@1388/@1475/@1537/@1562/
@1667/@1709/@1720/@1734/@1747/@1762/@1815 — all byte-verified).

### Family 1 — 06-initial "entre+X" compounds

"06 70" occurs **exactly once stream-wide** (@346) — the leg itself. No other
06 successor continues "entre" into a nameable French word:

- 77="le" → "entrele" ✗; 11="la" → "entrela" ✗; 00="pour" → "entrepour" ✗;
  59 → "entreest" ✗; 29="er" → "entreer" ✗; 94="ne" → "entrene" ✗;
  84="on" → "entreon" ✗; 06 → "entreent" ✗.
- 67 (et/veut §7 polyvalence): "entre et"/"entre veut" ungrammatical ✗.
- Open successors (88/73/21/55/50/52/43/14/65/62/60/91): no nameable
  "entre+X" French word without inventing values — per lane doctrine, no license.
- A 5-letter "entre" for one cell would also be the longest value in the cipher
  (longest standing: "fois"/"tout"/"pour", 4 letters) — extraordinary, needing
  independent evidence. None exists.

### Family 2 — standalone 06 = "entre" (preposition or 3sg of entrer)

No clean parse at any of the 44 windows. The three superficially plausible
windows all fail:

- @789 ("65 84 06 77 64" = "[65-noun] on [06] le qui"): "on entre" is clean,
  but the tail "le qui" (77="le" provisional + 64="qui" granted) is
  ungrammatical under every 06 reading. Not a license.
- @1080 ("78 64 06 52 89" = "[78] qui [06] 52 [89]"): "qui entre" is clean,
  but 52 and 89 are both open/split — the frame never closes. Not a license.
- @1667 ("84 64 06 91 11" = "on qui [06] 91 la"): "on qui" already strained;
  91 open. Not a license.
- @319 ("94 06 11" = "ne [06] la"): "ne entre la" — "entrer" takes no direct
  object; preposition after negator ungrammatical. Dead.
- @271 ("11 06 67" = "la [06] et/veut"): article cannot precede preposition or
  supply a verb subject. Dead.
- @1252/@1328/@1562/@1734 ("pas [06] …"): adverb "pas" licenses neither a
  preposition nor a finite verb after it. Dead ×4.
- @370 ("17 06 21" = "fois [06] [21-noun]"): "fois entre [noun]" ungrammatical
  (needs "de"). Dead.
- @1096 ("81 06 29" = "[81-noun] [06] er"): "entreer" not French. Dead.
- @1709 ("12 06 29"): "entreer" not French. Dead.
- @1388 ("16 06 29"): same. Dead.
- @967 ("24 06 77"): modal + finite "entre" ungrammatical; preposition after
  modal ungrammatical. Dead.
- @522 ("77 06 55" = "le [06] [55-V]"): article + preposition/verb dead. Dead.
- Remaining windows: 06 is a 3pl ending ([80]ent @470/@1091, [60]ent @1475,
  [93]ent @1762), word-internal ("mentent" @580/@581/@1184/@1185), bound
  ("[48]e" @399, "m'ent" @1355), or has open neighbors that cannot license
  (fenced, not licensing).

### C2 verdict

**No "entre" license exists.** The only "entre"-shaped reading stream-wide is
the @346–349 leg itself, which cannot license itself (circular). Every other
window either kills "entre" at kill grade or is fenced on open neighbors.

## Per-clause pass/fail

1. **C1 PASS** — census complete: 44/44 windows examined; "06 70" unique to
   @346; no independent "entre+X" compound; no clean standalone "entre".
2. **C2 PASS** — no "entre" license exists (circular self-license excluded).
3. **C3 PASS** — the kill disjunct fires: the @346–349 verb-ID leg is KILLED at
   kill grade. Under every licensed value the four groups spell "entprenne",
   which is not French; the leg's equation requires the unlicensed 5-letter
   value 06="entre". ent-06 F3's "value evidence, not ending evidence" claim
   falls with it.

Adverses: none listed. No standing or red-team verdict contradicted or
downgraded — the kill is scoped to the @346–349 leg only. 06="ent" (single
value) stands on its other legs; §7 intact (no polyvalence declared or needed).

## Downstream note (not adjudicated here)

ent-06-host-census adopted @347 as one of its 18 syllable-windows ("Word-initial
'ent' of 'entreprenne'"). With F3 killed, @347's predecessor (01) is open, so
@347 reverts to the fenced set (like the census's other 19 open-predecessor
windows). The host-census decision rule itself (finite ending iff left neighbor
is a verb stem; else syllable) does not depend on @347 — it is supported by
5+2 ending windows and 17 other syllable windows. Reclassification of @347 is
red-team/supervisor venue; this battery changes nothing outside its own queue
entry.

## Caveats

- Canonicality: row a2_05 offset 0 = upstream, unvalidated; the window is
  row-internal and consecutive, so the "06 70 12 94" adjacency holds on the
  canonical stream per protocol. A rival-phase sweep (phase02-a2_05-reseg,
  queued) could dissolve it — offset adoption is a red-team act.
- Kill verdict — no follow-ups required per protocol. (The natural next venue
  for any future 06="entre" claim is the red-team §7 docket, which would need
  independent byte evidence that does not currently exist.)

## Bookkeeping

- Report: code/crowd17/report_inbox/battery-spell-06-entre.md
- Queue: `spell-06-entre` → status `verdict`, result `kill`, 2026-10-09
  (pre-write assert passed — was queued/verdictless; temp-file + rename;
  JSON re-validated; only this entry touched; no downgrade)
- Lock created on start, deleted on completion (verified gone)
- `canonical.py` never used; R5005, sealed gates, red-team adjudication queue
  untouched
