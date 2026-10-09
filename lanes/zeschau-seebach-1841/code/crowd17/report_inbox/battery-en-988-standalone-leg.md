# Battery report: `en-988-standalone-leg` — verdict PROMOTE

**Target:** `en-988-standalone-leg` (Seebach lane battery worker)
**Date:** 2026-10-09
**Worker:** agent a688da04-6ad5-4069-87a2-7fa1024ba7ed

## Bar (verbatim, pre-registered before testing)

"discriminate lead vs coincidence: only support is the single clean window (fol=76 promoted masculine noun)"

Numbered pass/fail clauses (restated before testing, not modified after):

1. (Name arm) 01='en' at @988 is supported by >=2 independent legs -> name the local reading.
2. (Fence arm) If fewer than 2 independent legs, fence 'en'@988 as coincidence.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`
(parsed per `repair_parse.py`; asserts held: 1,847 pairs, 96 types).
`canonical.py` never used. Byte-verified the @988 locus, censused all 28
01-windows' followers, all 38 48-windows' followers, and all 21 76-windows'
predecessors. No R5005, sealed gates, or red-team queue touched.

## Window-level evidence

**Locus (byte-exact):** @987-988 = `48 01` (stream-unique), @988 = 01,
follower 76 (`01 76` stream-unique). Row a6_01.
Full context @984-996: `01 24 89 48 01 76 49 24 26 30 03 60 67`.

**Leg 1 — right edge (nominal complement):** fol=76 is a promoted masculine
noun (R19-111; independently confirmed by battery-val-76-class-census with
granted-value "ce [76]" legs at @1273/@1275, no longer dependent on
provisional 77="le"). "en [N-masc]" ("en France"-shaped) is therefore a
licensed prepositional reading. Rivals die at this locus: 'on'+noun is
ungrammatical (the uniform-'on' kill at @988 stands); the 'fait'-syllable
reading needs the A12 37-01 frame, absent here. No other 01 window offers a
nominal follower under standing values: 11='la' (GT) -> "en la" kill-grade
@295; 77='le' (provisional) -> kill-grade @949; 98='vient' hostile
@893/@970; 24/29/00/08 hostile. @988 remains the sole 'en'-preposition
window — consistent with a local, non-uniform reading.

**Leg 2 — left edge (preposition slot frame):** 48 takes prepositional
complements in 3 independent windows under standing values:
- @377: `82 48 00 11` = "m [48] pour la" (82='m' GT, 00='pour' granted, 11='la' GT)
- @1212: `32 48 96 45` = "[32] [48] par ce" (96='par' granted, 45='ce' A11)
- @1525: `24 11 11 48 96 87` = "[24] la la [48] par ce" ("48 par ce" trigram clean)

"48 [prep] [nominal]" is therefore a licensed frame, and 01 occupies the
preposition slot at @988. Leg 2 is independent of leg 1 (left-edge frame
evidence vs right-edge complement evidence); neither assumes 01='en'.
Jointly with rival elimination, 'en' is the surviving preposition reading.

## Per-clause pass/fail

1. Name arm (>=2 independent legs): PASS — leg 1 (nominal complement) and
   leg 2 (preposition-slot frame) are independent and jointly discriminate
   'en' from the dead rivals at this locus.
2. Fence arm: does not fire.

## Verdict: PROMOTE

The @988 'en'-local reading is promoted: "48 [en] [76-N]" — preposition
'en' with masculine-noun complement, inside 48's licensed
verb+preposition frame.

## Scope

Locus-level promote only. Does NOT name a uniform 01='en' (dead at 9
windows per battery-val-01-census). Does NOT touch R20-016 ('en'-local LEAD
at the 01-24 windows — different reading, different locus). The surviving
local readings ('en'@988 preposition, 'en'@01-24 pronoun, 'on'@893/@970/@40,
'fait'-syllable in 37-01 x3) remain mutually exclusive as a uniform value;
their reconciliation is the red-team split/polyvalence venue
(redteam-01-split-docket). No standing/red-team verdict contradicted or
downgraded; §7 intact (no polyvalence declared). No §4 follow-ups required
(promote); the red-team docket item already exists.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-en-988-standalone-leg.md`
- Queue: `en-988-standalone-leg` -> `status: verdict`, `result: promote`, 2026-10-09
- Lock: created on start (agent id + 2026-10-09T17:58Z), deleted on completion
- Adverses: none listed on target
