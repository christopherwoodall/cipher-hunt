# Battery report: det14-elsewhere

- Target id: `det14-elsewhere`
- Claim: 14='le'-determiner has legs outside the frame
- Date: 2026-10-09
- Worker: battery worker (agent fb38f291-9fa6-44ca-bfb6-440ab21a45dc). Lock
  `code/crowd17/next-token/locks/det14-elsewhere.lock` created
  2026-10-09T06:06:00Z; no prior/stale lock existed; deleted on completion
  after queue confirm.
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` +
  `data/upstream-ct_R5005.txt`), parsed per `code/side-keyhunt/repair_parse.py`
  (`load_rows` + `parse`). 1,847 pairs / 96 groups re-derived. R5005 untouched.
  `canonical.py` never used. No invented data.
- Coordinates with (not duplicating): battery-tout-14-rerun null (2026-10-08,
  which designed this target), battery-stem-14-id (2026-10-09, 14 census n=15),
  battery-ce-le-verb-frame null (2026-10-08, "ce le" stack fenced as 77-value
  residual), battery-le-14-kill-1121 (14='le' killed at @1121 only).

Indexing convention: @-offsets are 0-indexed pair indices into the repaired
stream, citing the 14 token's own index.

## Bar (pre-registered verbatim, from battery-queue.json)

"record a determiner leg iff >=2 of @72/@141/@339/@586 parse as determiner +
named nominal head with zero contradictions; else fence 14's determiner value
to the frame tail"

Numbered clauses (pre-registered BEFORE testing, not modified after):

1. >=2 of @72/@141/@339/@586 parse as 14='le'-determiner followed by a NAMED
   nominal head, with zero contradictions -> record a determiner leg.
2. Else (fewer than 2) -> fence 14's determiner value to the frame tail
   (the '79 14 60 03' windows @1365/@1689, owned by queued le14-adj60-tail).

## Window-level evidence (fresh re-derivation)

14 census: n=15 @72, 84, 117, 141, 178, 339, 424, 458, 586, 623, 813, 896,
1121, 1365, 1689 — matches stem-14-id exactly.

Standing values used: banked 11=la, 29=er, 46=que, 82=m; promoted 87=ce,
64=qui, 00=pour (A9 leg-1), 77=le (provisional), 59=est (provisional);
class-level 24=verb, 21=noun, 31=VERBAL, 65=noun; lead-grade 45=ce/dict;
67 positional et/veut rule (67='veut' iff follower infinitive-shaped).

- @72 (row a1_02): `24 56 | 87 | 14 | 24 | 87 11` = "[56] ce [14] [24-verb] ce la".
  Right neighbor 24=['verb','cls'] -> no nominal head available; a determiner
  leg needs a nominal head, and the only candidate slot is occupied by a verb.
  Left neighbor 87='ce' (prom) -> "ce le" preverbal stack, fenced as a 77-value
  residual by ce-le-verb-frame (NULL, 2026-10-08); the exact A8 frame
  ("87 77 [80/89]") does not apply here (follower is 24, middle is 14) and was
  fenced, not granted. NO LEG.
- @141 (row a1_04): `65 13 | 66 | 14 | 74 | 67 64` = "[65-noun] [13] [66] [14]
  [74] et(67) qui(64)" (67='et': follower 74 not infinitive-shaped).
  Right neighbor 74 is open at every tier (registry: none). 74 census: n=34,
  heavily "49 74"/"74 74" unit-like; no window forces a nominal reading.
  "66 le [74]" is not contradictory, but the bar requires a NAMED nominal head,
  and 74 cannot be named at battery grade. NO LEG (head unnamed, not
  contradictory).
- @339 (row a2_05): `03 64 | 31 | 14 | 45 | 64 96` = "[03] qui(64) [31-verb]
  [14] ce(45) qui(64) par(96)" (31=['VERBAL','cls']).
  Right neighbor 45=['ce/dict','lead']. Under 45='ce': "le ce" is a double
  determiner, ungrammatical. Under 45='dict' (syllable): "le [syllable]" is
  ungrammatical. Left neighbor 31 is verb-class; no rescue available.
  NO LEG. DETERMINER-HOSTILE at kill grade.
- @586 (row a3_02): `10 19 | 18 | 14 | 00 | 97 41` = "[10] [19] [18] [14]
  pour(00) [97] [41]" (00='pour', prom A9).
  Right neighbor 00='pour' -> "le pour" is determiner + preposition,
  ungrammatical in 1841 diplomatic French. Left neighbor 18 open; no rescue.
  NO LEG. DETERMINER-HOSTILE at kill grade.

Leg count in the pre-registered set: 0/4.

## Per-clause pass/fail

- C1 (record a determiner leg): FAIL. 0/4 windows parse as determiner + named
  nominal head. @339 and @586 are determiner-hostile at kill grade ("le ce",
  "le pour"); @72 has no nominal head (24=verb-class, "ce le" stack fenced);
  @141's head (74) is unnamed at every tier.
- C2 (fence to the frame tail): FIRES. 14's determiner value is fenced to the
  frame-tail windows @1365 (a7_06: '62 94 79 14 60 03 30') and @1689 (a8_05:
  '62 94 79 14 60 27 46'), where "tout le [60-adj] [03-N]" is the live
  adjective-rival parse. Venue: le14-adj60-tail (queued).

## Adverses answered

- "several windows look determiner-hostile": CONFIRMED. @339 ("le ce" double
  determiner) and @586 ("le pour" determiner + preposition) are hostile at
  kill grade; @72 is effectively hostile (verb-class head).
- "heads unnamed": CONFIRMED. @141's head 74 is open at every tier (n=34
  census, no forced nominal reading); no battery-grade name exists.

## Material caveat (not a bar rewrite; red-team scope question)

@117 (row a1_03, NOT in the pre-registered set): `68 21 | 67 | 14 | 21 | 60 90`
= "[68] [21-noun] et [14] [21-noun] [60] [90]". 67='et' per the positional rule
(follower 21=['noun','cls'] is not infinitive-shaped); 14='le'-determiner +
21=['noun','cls'] named nominal head parses with zero contradictions at battery
grade. This window lies outside both the tested set AND the frame tail, so the
bar's fence scope ("to the frame tail") may be too narrow. @117 is already
covered by queued det-14-census (testing @72/@117/@178) and sits in the
red-team 14/77 homophony docket per stem-14-id (2026-10-09). The fence executes
per the pre-registered bar; the red team owns the scope question. The bar is
not modified post-data.

## Verdict

**NULL (fence executed)** — 0/4 pre-registered windows yield a determiner leg;
C1 fails, C2 fires: 14's determiner value is fenced to the frame-tail windows
@1365/@1689 (venue: queued le14-adj60-tail). No standing verdict contradicted.
The claim "14='le'-determiner has legs outside the frame" fails at all four
pre-registered windows.

## Follow-ups (work regenerates; none duplicate queued targets)

1. **noun-74-census** (priority 3). Claim: 74 has a namable class, which would
   rescue @141's "le [74]" as a determiner leg. Bars: "name 74's class iff a
   single class covers >=2/3 of its 34 windows with zero contradictions; else
   fence 74 as class-open and @141 stays headless." Evidence: this report's
   n=34 74 census ("49 74"/"74 74" unit-like, no forced nominal reading).
   Adverses: 74's distribution is diffuse; the unit reading may win.
2. Already-queued coverage (no new target needed): det-14-census (queued)
   tests @72/@117/@178 and will adjudicate the @117 "et le [21-noun]" parse;
   le14-adj60-tail (queued) owns the frame-tail "tout le [60-adj] [03-N]"
   parse.

## Queue/registry state

- `battery-queue.json`: `det14-elsewhere` queued -> verdict/null via this
  report. No other entry touched; no verdict downgraded.
- Lock `locks/det14-elsewhere.lock` deleted on completion after queue confirm.
