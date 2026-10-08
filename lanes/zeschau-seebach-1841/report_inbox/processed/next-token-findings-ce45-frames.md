# Next-token findings: ce45 frames (45 followers)

Finder beat: ce45-frames (wave 2). Stream: repaired 1,847-pair parse
(`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`,
parsed like `repair_parse.py`; `canonical.py` never used; R5005 untouched).
All 45 (n=22) occurrences extracted ±3 groups. Windows below use @pair offsets
of the target group itself.

Standing constraints respected: 45="ce" is a HOLD (A11), not a grant — this
beat tests its frame support, never re-litigates it as a value claim.
78="ver" is queued (ver-78), not granted — all "verdict" readings are stated
as conditional. 94="ne" is battery-promoted 2026-10-07, pending red-team
ratification — used with that caveat. Settled kills respected (48-word
values, 81="prin", 84="fait", {48,94} homophone-set, 09/92 "-ère").
Banked: 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que (pencil);
87=ce, 64=qui, 96=par, 17=fois, 47="ce" (allophone tier), 84="on"
(granted); 59=est, 77="le" provisional.

## Headline null: no second mirror frame-type on the follower side

The A11 HOLD needs >=2 mirrored frame-types (has ~1.5: '45-64' x3, plus
'45-46' x1 as the half). Follower census, 45 vs 87:

- Shared successors: 64 (87 x5 / 45 x3), 46 (87 x3 / 45 x1),
  01 (87 x2 / 45 x1), 08 (87 x1 / 45 x1).
- Only 64 reaches >=2 windows at 45. 46/01/08 are x1 each.
- 45's three biggest follower clusters — 93 x3, 23 x3, 28 x2 (8/22 windows)
  — have ZERO 87-contact (87->93 x0, 87->23 x0, 87->28 x0, 87->13 x0).

Predecessor-side check also fails on frame extension: 96->87 x3 are all
'96-87-46' ("par ce que" x3), but 96->45 x2 are '96-45-93' (@603) and
'96-45-36' (@1214) — contact mirrors, frame does not. 76->87 x2 vs 76->45 x2
likewise diverge after the target (11/76 vs 91/94).

Result: the second mirror frame-type is NOT FOUND. The A11 adverse stands.
The '45-46' @437 "ce que" x1 (mirrors 87->46 x3 and 47->46 x3) remains the
half-mirror. The complementarity leg re-verifies on the repaired stream:
24->45 x0 vs 24->87 x10.

## Follower clusters (de-duplicated before counting)

- **93 x3**: '74-45-93' x2 (@262, @478) + '96-45-93' x1 (@603). No 87-mirror.
- **64 x3**: '45-64-96-43-87-01' x2 (@340, @1024, byte-identical 6-gram) +
  '78-45-64' x1 (@314). Mirrors 87->64 x5 ("ce qui").
- **23 x3**: @678, @1055, @1551 — all distinct contexts. No 87-mirror.
- **28 x2**: @104 ('59-45-28'), @697 ('50-45-28'). No 87-mirror.
- **13 x2**: '78-45-13-55-61' x2 (@574, @1165, byte-identical 5-gram).
  No 87-mirror.
- **Singles**: 91 (@14), 54 (@332), 88 (@401), 46 (@437), 94 (@569),
  08 (@974), 01 (@983), 58 (@1201), 36 (@1214).

## Predecessor clusters

- **78 x4** (@314, @574, @983, @1165) — the 'verdict' fork, see F4.
- **74 x3** (@262, @478, @1055).
- **76 x2** (@14, @569); **50 x2** (@332, @697); **96 x2** (@603, @1214).
- Singles: 59 (@104), 14 (@340), 11 (@401), 63 (@437), 77 (@678),
  51 (@974), 64 (@1024), 29 (@1201), 92 (@1551).

## Ranked frames

**F1 (HIGH). '45-64-96-43-87-01' x2 (@340, @1024) — "ce qui par [43] ce [01]".**
Byte-identical 6-gram; 87="ce" sits inside it. Under 45="ce": "…ce qui
par [43] ce [01]…" — clean diplomatic French if 43 is a noun (noun-43's
candidates: suite/condition/maniere/mesure). The dict rival has NO "ver"
contact here (predecessors are 14 and 64), so F1 discriminates FOR 45="ce"
and AGAINST 45="dict". Adverses: "qui ce qui" left edge (@340's 14,
@1024's 64-92) needs a parse; 43's value is open (feeds noun-43 and the
f-qui-par beat).

**F2 (HIGH). '78-45-13-55-61' x2 (@574, @1165) — "verdict [13-55-61]".**
Byte-identical 5-gram. Under 78="ver" (queued) + 45="dict": "verdict
[13-55-61]" x2 — clean noun frame; @574's extended tail reads
"…61 94=ne 82=m 06" = "…[13-55-61], ne me/m'[06]…" (negation frame, 94="ne"
battery-promoted). Under 45="ce": "ver ce" x2 — ungrammatical. F2
discriminates FOR dict-45 and AGAINST 45="ce" (conditional on 78="ver").
Adverses: @1165's "21 67" left context is awkward ("et/veut verdict");
78="ver" is queued, not granted (joint constraint with ver-78).

**F3 (HIGH). The 93-cluster: '74-45-93' x2 (@262, @478) + '96-45-93' (@603).**
Under 45="ce" this is "ce [93]" x3 — but 93 is verb-shaped per the queued
verb-93 target ("takes 29='er' once, followed by 59 once; @101 'on ne [93]
est'"). "ce"+verb is ungrammatical French. The cluster is hostile to
45="ce" AND to 45="dict" (no "ver" contact at 74/96). Joint constraint with
verb-93: if 93 promotes verb-shaped, these 3 windows become kill-grade
adverses for A11. @262's left edge is "77-84" = "l'on" (A15): "l'on 74 ce
[93]…".

**F4 (MEDIUM-HIGH). '78-45' x4 contact — the fork itself.**
@314 ('78-45-64' = "verdict qui est [32]?"/"ver ce qui…"),
@574 + @1165 (F2, "verdict [13-55-61]"),
@983 ('47-78-45-01' = "ce verdict [01]…", 47="ce" allophone).
'ce verdict' x2 verified: @573 (78 with 87="ce" predecessor) and @982 (78
with 47="ce" predecessor). Under dict-45 all four read "verdict…"; under
45="ce" all four read "ver ce…" (bad). This is the 78/45 joint constraint:
if ver-78 promotes, 45="ce" dies at 4/22 windows unless a positional rule
saves it.

**F5 (MEDIUM). '45-46' @437 — "ce que" x1.** `16 78 63 [45] 46 43 98` =
"…[63] ce que [43] 98" — the canonical 'ce' frame, mirrors 87->46 x3 and
47->46 x3. Single window: the "0.5" mirror, unchanged.

**F6 (MEDIUM-LOW). '59-45-28' @104 — "est-ce [28]" candidate.**
`94 93 59 [45] 28 00 46` = "…est ce [28] pour que". "est-ce" is a core 'ce'
frame, but the canonical continuation is "que" (46), not 28. Input to the
queued est-59-frames battery: 28 must be named there.

**F7 (LOW). '96-45' x2 predecessor contact.** Contact mirrors 96->87 x3,
but the frame diverges ("par ce que" x3 vs "par ce [93]/[36]"). Not a
mirror frame-type; recorded so the red team need not re-derive it.

## Ranked battery targets

1. **fork-78-45-adjudication** (priority 1). Claim: the 78-45 x4 contact
   adjudicates the 45="ce" HOLD against the 45="dict" rival. Bars: (a) run
   joint with ver-78 — if 78="ver" promotes, the four windows (@314, @574,
   @983, @1165) must read "verdict…" (45="dict" at minimum at these windows)
   or 45="ce" is killed at 4/22 windows; (b) state any positional rule that
   lets both claims survive, with per-window parses. Evidence: F4; 'ce
   verdict' x2 @573/@982. Adverses: 78="ver" queued not granted; 45="ce" is
   a HOLD. This does not duplicate dict-45 (syllable-profile bar) or
   ce-45-mirror2 (positive mirror search) — it is the fork adjudication both
   feed.
2. **frame-74-45-93** (priority 2). Claim: the 45->93 x3 cluster resolves
   under one parse. Bars: (a) all three windows parse with 93's class
   stated; (b) joint with verb-93 — if 93 is verb-shaped, record 45!="ce"
   at these windows as a kill-grade adverse for A11 (do not promote around
   it). Evidence: F3; 87->93 x0. Adverses: 93's class open; 74 vs 96 left
   contexts differ.
3. **dict-frame-78-45-13-55-61** (priority 2). Claim: the byte-identical
   5-gram x2 reads "verdict [13-55-61]" under 78="ver"+45="dict". Bars:
   (a) both windows parse with 13-55-61 named as one unit; (b) @574's
   "…61 94 82 06" parses as a "ne me/m'" negation frame; (c) @1165's "21 67"
   left context fenced with stated cause. Evidence: F2. Adverses: 78="ver"
   queued; this bar does not duplicate dict-45's ("'verdict' frames parse +
   45 contact profile matches '-dict' syllable") — it is the narrowed
   5-gram instance of it.
4. **ce-frame-45-64-96-43-87-01** (priority 2). Claim: the byte-identical
   6-gram x2 reads "ce qui par [43] ce [01]" under 45="ce". Bars: (a) both
   windows parse with 43 named (coordinate with noun-43); (b) the "qui ce
   qui" left edges (@340's 14, @1024's 64) parsed or fenced. Evidence: F1;
   no 78-contact (dict unavailable here). Adverses: 43's value open.
5. **est-ce-104** (priority 3). Input to est-59-frames: @104 "59-45-28".
   Bar (for that battery): 28 named with "est-ce [28] pour que" parsing.
   Evidence: F6; 59="est" provisional + 45="ce" HOLD + 00="pour" + 46="que".
   Adverses: 28 unknown; "est-ce" normally takes 46 not 28.

## Nulls and anomalies (reported, not hidden)

- **Second mirror frame-type: NOT FOUND** (headline null, see above). The
  A11 adverse stands; ce-45-mirror2's positive bar is unmet on current
  evidence. Follow-ups are targets 1–4 above.
- **@678 ("77-45") and @401 ("11-45")**: article+"ce" ("le ce", "la ce")
  is ungrammatical under 45="ce" and meaningless under 45="dict". Genuine
  residuals — either 77/11 are not articles here or the boundary parse is
  wrong. Not forced.
- **@1201 ("29-45")**: `16 64 29 [45] 58 47 43` = "qui er ce [58]…".
  Word-internal "…erce" candidate (cf. queued frame-29-47's "[stem]erce"
  note: exercer/commerce/percer) — would make 45 sub-lexical here, fitting
  neither queued claim. Flagged, not decided.
- **@332**: `00 92 50 [45] 54 88 40` = "pour 92 50 ce [54] 88 e" — unparsed
  under every standing value; the hardest 45 window.
- **@569**: `97 13 76 [45] 94 52 87` = "…76 ce ne [52] ce…" — "ce ne" with
  no visible "pas"/verb; resists the negation frame.
- **Scatter note (observation, not battery-grade)**: 45 has 14 distinct
  successors / 22 windows (0.64) vs 87's 16/32 (0.50) and 47's 17/28
  (0.61). 45 is the most scattered, but 47 — a granted "ce" — is nearly as
  scattered, and n=22 is small. Weak; recorded for the record only.
- **No formula contamination**: no 45 window sits in a known formula
  ('96-21' vient-parvenir, '94-07-06-94'); the three repeated sub-frames
  ('78-45-13-55-61' x2, '74-45-93' x2, '45-64-96-43-87-01' x2) were
  de-duplicated before counting.

## Method

Repaired 1,847-pair parse; every 45 occurrence (22) ±3 groups; clustered by
follower pattern first; predictions from 1840s French diplomatic register;
byte-identical sub-frame repeats de-duplicated before counting; no formula
windows present. Full window inventory below.

## Window inventory (all 22 windows, ±3, glossed)

- @14 (a1_00): `62 98 76 [45] 91 53 17=fois`
- @104 (a1_03): `94 93 59=est? [45] 28 00=pour 46=que`
- @262 (a2_02): `77=le? 84=on 74 [45] 93 52 33`
- @314 (a2_04): `24 37 78 [45] 64=qui 59=est? 32`
- @332 (a2_05): `00=pour 92 50 [45] 54 88 40=e`
- @340 (a2_05): `64=qui 31 14 [45] 64=qui 96=par 43`
- @401 (a2_08): `48 06 11=la [45] 88 53 34=i`
- @437 (a2_09): `16 78 63 [45] 46=que 43 98`
- @478 (a2_11): `37 78 74 [45] 93 00=pour 13`
- @569 (a3_02): `97 13 76 [45] 94 52 87=ce`
- @574 (a3_02): `52 87=ce 78 [45] 13 55 61`
- @603 (a4_00): `39 26 96=par [45] 93 54 64=qui`
- @678 (a5_00): `64=qui 37 77=le? [45] 23 09 07`
- @697 (a5_01): `46=que 02 50 [45] 28 94 60`
- @974 (a6_01): `98 48 51 [45] 08 01 00=pour`
- @983 (a6_01): `76 47=ce 78 [45] 01 24 89`
- @1024 (a6_03): `84=on 92 64=qui [45] 64=qui 96=par 43`
- @1055 (a6_04): `29=er 74 74 [45] 23 77=le? 84=on`
- @1165 (a6_09): `21 67=et/veut 78 [45] 13 55 61`
- @1201 (a7_00): `16 64=qui 29=er [45] 58 47=ce 43`
- @1214 (a7_00): `32 48 96=par [45] 36 77=le? 83`
- @1551 (a8_00): `12 94 92 [45] 23 99 13`
