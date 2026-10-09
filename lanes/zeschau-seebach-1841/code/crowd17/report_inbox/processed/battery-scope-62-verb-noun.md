# Battery verdict: scope-62-verb-noun

**Verdict: NULL** — clause 1 is met (all 35 windows are classified below),
but clause 2 triggers the §7 package: the alternation cannot be carried
by one lexeme at battery grade. The 62-94 frame family (9 windows)
resists the {règn-, trôn-} one-lexeme account, and the demonstrated
cleaner rival (62='il', collision battery) needs a second lexeme that
only the red team can declare. The battery declares no polyvalence.
The §7 split candidacy is packaged for the red team (follow-up 1).

## Bar (verbatim, pre-registered)

> "Classify all 35 windows as stem-verbal vs nominal."
> "If the alternation cannot be carried by one lexeme, package the §7 split candidacy for the red team (battery declares no polyvalence)."

Restated as numbered clauses (before testing):

- **C1**: Classify all 35 windows of 62 as stem-verbal vs nominal,
  with @-offsets and the frame evidence for each class decision.
- **C2**: If the alternation cannot be carried by one lexeme, package
  the §7 split candidacy for the red team. The battery declares no
  polyvalence; it only delivers the evidence package.

Claim (from queue): Map 62's verb-stem vs nominal windows under the
surviving {règn-, trôn-} stem: C1 forces verb-stem at @665/@1536
(06 as finite '-ent' per the 06 decision rule); C2's @1315 forces
non-verbal; @425 supports nominal ('le [62]e').

## Method

Read BATTERY-PROTOCOL.md first. Created
`locks/scope-62-verb-noun.lock` on start (agent id + UTC timestamp).
Re-derived the repaired stream in-session from
`code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt` (parsed per `repair_parse.py`):
**1,847 pairs / 96 types verified**. `canonical.py` never touched.
R5005, sealed gates, red-team adjudication queue untouched.

All @-offsets are 0-based pair indices (queue convention).

Standing values used as premises (never re-litigated): 62 = {règn-,
trôn-} stem (val-62-ne-noun); 06='ent' with the ent-06-host-census
decision rule (finite 3pl '-ent' iff left neighbor is a verb stem);
94='ne', 48='e' (letter tier), 98='vient' (battery-promoted, pending
ratification), 77='le' (provisional), 21 = noun class (value
kill-closed), 79='tout', 00='pour', 84='on'; 62='il' = demonstrated
rival, NOT promoted (collision-62-84); @508 standing locus promote
("le [62]ne", conditional) adopted, not re-litigated.

Classification rule: **stem-verbal** = 62 functions as a verb
(finite 3sg 'règne'/'trône', 3pl '[62]ent', or verb-stem with verbal
dependents); **nominal** = 62 functions as a noun (subject, object,
after determiner, apposition). Noun/verb homography within one
French word is not §7 polyvalence (per R17-008's 32 precedent).

## C1: all 35 windows classified

### STEM-VERBAL (forced) — 2 windows

- **@665** (a4_02): `80 03 [62] 06 00 20 67` — 62+06 = '[62]ent'
  ('règnent'/'trônent', 3pl). 06 cannot attach rightward (00='pour'
  is a whole word). STEM-VERBAL, forced per the 06 decision rule.
  (Subject placement residual fenced by the parent battery.)
- **@1536** (a8_00): `73 41 [62] 06 21 62` — same: '[62]ent' 3pl.
  Left neighbor is 41 (no prefix candidate). STEM-VERBAL, forced.

### STEM-VERBAL-LEAN — 1 window

- **@1349** (a7_05): `86 66 73 34 [62] 48 77 78 94` — 'y [62]e'
  (34='i' as 'y'): 'y règne/trône' (3sg, 'reigns there') is the
  clean parse; the noun reading needs 'y' + noun (bad). The
  'le [78]' tail is strained (intransitive verb + determiner),
  fenced with cause. STEM-VERBAL-LEAN.

### NOMINAL — 8 windows

- **@11** (a1_00): `18 93 [62] 98 76 45` — '[93] [62] vient [76]':
  62 as subject noun of finite 98='vient'. V-V reading
  ungrammatical. NOMINAL (subject).
- **@425** (a2_09): `36 29 47 14 [62] 48 76 42` — 'le [62]e'
  ('le règne'/'le trône'), conditional on 14='le' (parent C2).
  NOMINAL.
- **@508** (a3_00): `77 [62] 94 64 98 65` — 'le [62]ne qui vient':
  standing locus promote adopted, not re-litigated. NOMINAL.
- **@802** (a5_05): `86 44 74 [62] 98 53 69` — '[74] [62] vient [53]':
  subject of 'vient'. NOMINAL.
- **@945** (a5_10): `50 40 08 [62] 98 96 86` — '[08] [62] vient [96]':
  subject of 'vient'. NOMINAL.
- **@1136** (a6_08): `77 86 20 [62] 98 00 98` — '[20] [62] vient':
  subject of 'vient'. NOMINAL.
- **@1315** (a7_04): `44 00 36 74 [62] 48 98 15` — '[62]e' before
  finite 98: V-V ungrammatical, so non-verbal (parent C2). NOMINAL.
- **@1324** (a7_04): `29 80 08 [62] 98 56 30` — '[08] [62] vient':
  subject of 'vient'. NOMINAL.

### AMBIGUOUS / STRAINED / UNDERDETERMINED — 21 windows

- **@46** (a1_01): `81 30 [62] 96 00 92` — 'pas [62] par pour':
  noun-head reading strained; verb reading needs an absent
  subject/ne. STRAINED, noun-lean.
- **@82** (a1_02): `42 98 51 [62] 16 14 06` — 62-16 family (x4);
  neighbors 51/16 value-open. UNDERDETERMINED.
- **@100** (a1_02): `29 85 08 21 [62] 94 93 59` — 62-94 family:
  under {règn-, trôn-}, '[21-N] [62] ne est [45]' is apposition,
  strained. Rival 'il ne' parses cleaner (demonstrated, not
  promoted). STRAINED; rival fenced.
- **@360** (a2_06): `47 11 21 [62] 48 76 47` — parent C2: 3sg verb
  'la [21] règne' vs nominal apposition; both strained, no forced
  contradiction. AMBIGUOUS.
- **@389** (a2_07): `37 43 91 36 [62] 91 84 73` — '[36] [62] [91]':
  both neighbors value-open. UNDERDETERMINED.
- **@446** (a2_09): `50 78 41 10 [62] 61 59 32` — '[10] [62] [61]':
  both neighbors value-open. UNDERDETERMINED.
- **@658** (a4_02): `24 26 30 03 [62] 16 00 86` — GATED on
  re-prefix-03-665 (03 as 're-' prefix). Provisional:
  stem-verbal-lean if 03 is prefixal, else noun-lean. Not decided
  here; fenced to the queued target.
- **@761** (a5_03): `34 29 40 20 [62] 94 59 39` — 62-94 family:
  '[20] [62] ne est' strained under {règn-, trôn-}; 'il ne' rival
  cleaner. STRAINED; rival fenced.
- **@840** (a5_06): `56 17 98 20 [62] 94 26 12` — 62-94 family:
  same as @761. STRAINED; rival fenced.
- **@849** (a5_06): `33 96 40 [62] 21 67 91` — '[40] [62] [21-N]':
  follower 21 is noun-class; verb reading orphaned without
  subject. STRAINED, noun-lean.
- **@1065** (a6_04): `83 82 96 21 [62] 18 70 39` — 'par [21] [62] [18]':
  apposition (strained) vs orphaned verb. STRAINED/AMBIGUOUS.
- **@1141** (a6_08): `00 98 78 [62] 16 29 42` — 62-16 family;
  '[78] [62] [16]' strained both arms. UNDERDETERMINED.
- **@1297** (a7_03): `94 52 80 04 [62] 16 02 70` — 62-16 family.
  UNDERDETERMINED.
- **@1329** (a7_04): `56 30 06 [62] 94 70 52` — 62-94 family:
  strained under {règn-, trôn-}; 'il ne' rival cleaner. STRAINED;
  rival fenced.
- **@1454** (a7_09): `33 46 92 [62] 61 21 67` — '[92] [62] [61]':
  both neighbors value-open. UNDERDETERMINED.
- **@1464** (a7_09): `79 17 01 21 [62] 48 21 02` — parent C2:
  N-'[62]e'-N; noun apposition vs 3sg verb, both strained.
  AMBIGUOUS.
- **@1468** (a7_09): `62 48 21 02 [62] 38 26 12` — '[02] [62] [38]':
  both neighbors value-open. UNDERDETERMINED.
- **@1482** (a7_10): `29 82 16 98 [62] 46 77 84` — 'vient [62] que':
  V-V impossible, so noun-lean (post-verbal nominal, strained).
  STRAINED, noun-lean.
- **@1539** (a8_00): `62 06 21 [62] 93 88 77` — '[21-N] [62] [93]':
  93 has no value; apposition strained; verb orphaned. STRAINED,
  noun-lean.
- **@1569** (a8_01): `50 29 24 74 [62] 48 56 32` — parent C2:
  compatible as noun or verb-stem, neighbors open. AMBIGUOUS.
- **@1704** (a8_06): `94 30 20 [62] 94 88 26` — 62-94 family:
  same as @761. STRAINED; rival fenced.
- **@1772** (a8_09): `26 37 78 [62] 94 24 87` — 62-94 family:
  strained under {règn-, trôn-}; 'il ne' rival cleaner. STRAINED;
  rival fenced.

### RESIDUAL (unparsed under all readings) — 2 windows

- **@1362** (a7_06): `35 13 92 [62] 94 79 14 60` — the 62-94-79
  twin. 'ne tout [14]' is unparsed under {règn-, trôn-} AND under
  the 'il' rival (frame-62-94-79 battery: NULL). RESIDUAL.
- **@1686** (a8_05): `46 79 65 13 93 [62] 94 79 14 60` — the twin of
  @1362 (neque-instance-sweep). Same: unparsed. RESIDUAL.

Tally: 2 + 1 + 8 + 21 + 2 = 34, plus @658 gated = 35. All windows
covered. **C1: PASS.**

## C2: the §7 package

The noun/verb alternation itself CAN be carried by one lexeme:
'règne'/'trône' are one French word with nominal and verbal uses
(the R17-008/32 precedent: inflectional, not lexical polyvalence).

What one lexeme cannot carry: the **62-94 frame family** (9 windows).
Under {règn-, trôn-}, eight of nine (@100, @761, @840, @1329, @1362,
@1686, @1704, @1772) are strained, and the collision battery
demonstrated a cleaner rival — 62='il' ('il ne', 8 clean) — which is
a DIFFERENT lexeme (pronoun), not a second use of the same word.
Holding both needs two lexemes for 62, i.e. a second polyvalence.
Per §7 only the red team can declare one; the battery declares no
polyvalence. The ninth window (@508) is the fenced standing promote
('le [62]ne'), adopted, not re-litigated.

The 62-94-79 twins (@1362/@1686) are a further hard residual:
unparsed under every reading tried so far.

**C2: PACKAGE DELIVERED** — the §7 split candidacy (62-94 family:
'il' vs {règn-, trôn-} vs residual 62-94-79) goes to the red team
as follow-up 1. No polyvalence is declared at battery level.

## Verdict: NULL

Not PROMOTE: no single value can be named across all 35 windows at
battery grade; clause 2's outcome is a red-team package, not a
battery-grade close.
Not KILL: no clause fails at kill grade — C1 classifies all 35,
and the parent C1/C2 scope findings are not contradicted.

## Follow-ups proposed (for supervisor queuing)

1. `redteam-62-split` (P2) — §7 split candidacy for 62. The 62-94
   frame family (9 windows): is 62='il' at these frames (collision
   battery, demonstrated not promoted) vs 62={règn-, trôn-} one
   lexeme elsewhere, with the 62-94-79 twins (@1362/@1686) as the
   hard residual? Battery cannot declare a second polyvalence —
   red-team adjudication only. Bar: adjudicate with the
   frame-level evidence re-derived; fence, split, or close.
2. `val-16-62-frames` (P4) — Name 16's value at the 62-16 x4
   cluster (@82/@1141/@1297; @658 after re-prefix-03-665 lands).
   A landed 16 value disambiguates four strained windows. Bar:
   name 16 iff >=2 of the four windows parse under one value with
   zero new assumptions.
3. `stem-62-7994-residual` (P3) — Resolve the 62-94-79 twin
   (@1362/@1686), unparsed under all readings. Narrower bar: test
   79's value ('tout' granted) at these windows, or 14/60 as the
   missing verb. Bar: produce ONE grammatical parse of the twin
   frames, or confirm as a genuine residual with stated cause.

## Adverses

None listed on the queue target. Fenced with stated cause:
- @658 gated on re-prefix-03-665 (queued; not duplicated here).
- The missing 3pl subject for '[62]ent' at @665/@1536 is the
  parent battery's fenced residual (bar is a word-form test).
- The @508 'trône' standing promote is adopted (regne-trone-tiebreak
  escalation untouched); the corpus règne lean is red-team venue.

## Standing state

No standing verdict contradicted or downgraded. §7 intact (no
polyvalence declared). Canonical-stream caveat stands (row a5_03's
upstream offset is the repaired choice; row a3_00's offset
unvalidated).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-scope-62-verb-noun.md`
  (this file)
- Queue: `battery-queue.json` `scope-62-verb-noun` → status
  `verdict`, result `null`, date 2026-10-09 (pre-write assert
  confirmed `queued`/verdictless; temp-file + rename; JSON
  re-validated post-write; own entry only)
- Lock: `locks/scope-62-verb-noun.lock` created on start, deleted
  on completion
