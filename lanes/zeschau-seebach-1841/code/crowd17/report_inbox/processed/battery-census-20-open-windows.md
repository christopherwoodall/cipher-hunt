# Battery report: census-20-open-windows

- Target id: `census-20-open-windows`
- Claim: "slot-classify 20's nine unexamined windows (@490/@642/@668/@703/@741/@873/@958/@1135/@1224) window-local."
- Date: 2026-10-09
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed like code/side-keyhunt/repair_parse.py;
  n=1847 asserted, 96 types asserted). All @-offsets are 0-based repaired-stream indices.
  `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.
- Lock: code/crowd17/next-token/locks/census-20-open-windows.lock (created at start,
  deleted on completion; no prior lock existed).

## Bar (verbatim, pre-registered before testing)

"for each window, record the forced slot (verbal / det-adj / noun / particle / unforced) with the licensing frame; no cross-window value claim"

Numbered pass/fail clauses (restated before testing, not modified after):

1. (C1) Each of the nine listed windows is slot-classified window-local
   against standing values, with the licensing frame stated.
2. (C2) No cross-window value claim is made for 20 (class/value naming stays
   with the poly-20 red-team docket; §7 binds).
3. (C3) No standing verdict contradicted or downgraded.

## Method

Re-derived the repaired parse in-session; asserted 1,847 pairs / 96 types.
Window contexts re-derived byte-exact at ±8 around each target (all nine
targets confirmed as 20). Standing values used as premises only:
11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que, 87=ce, 64=qui, 96=par,
17=fois, 79=tout, 00=pour, 84=on, 47=ce; 59=est / 77=le provisional;
24 finite-modal promoted; 98='vient' battery-promoted; 06='ent' promoted;
48='e' inflectional promoted; 62='il' demonstrated; 77-89 "le [89]e" noun arm
(from noun26-89-class). Kill constraints honored: 20="fois" dead; poly-20
docket (NOUN vs DET/ADJ) is red-team venue; inf-20-nepas killed the verbal-20
value-search bar but the verbal *face* stands.

## Window-level evidence (±8 context, target bracketed)

### W1 @490 (a2_11)
`52 30 01 19 64 76 42 41 [20] 67 78 42 94 02 79 88 47`
- Left neighbor 41 has an open three-arm split (finite-verb / determiner /
  letter); right neighbor 67 = et/veut (sole true polyvalence).
- Under 41-det: "det [20-noun]" parses; under 41-verb: "V [20]" needs a
  nominal/modifier reading. No determiner precedes 20 directly; no particle
  frame.
- **Slot: unforced.** Classification pivots on 41's unresolved class; no
  window-local frame forces one slot.

### W2 @642 (a4_01)
`63 74 46 60 67 77 89 48 [20] 24 87 61 88 77 78 52 82`
- Left edge is the closed NP "le [89]e" (77-89 arm A, noun forced).
- Right edge is modal-24 + "ce".
- Noun-20 needs an unlicensed clause boundary ("le [89]e. [20] …");
  verbal-20 clashes with modal adjacency ("[V] [24-modal] ce" — "24 ce" is
  ungrammatical); participle-20 leaves "24 87 61" unparseable.
- **Slot: unforced.** 20 sits between a complete NP and a modal; no licensed
  frame reaches it from either side.

### W3 @668 (a5_00)
`00 86 50 80 03 62 06 00 [20] 67 11 86 24 80 03 64 37`
- Left is 00="pour" (A9). Right neighbor 67 resolves positionally: follower
  11="la" is not infinitive-shaped, so 67="et" (positional rule).
- Under 20=inf: "pour [20-inf] et la [86]…" — A9 frame parses.
- Under 20=noun: "pour [20-noun] et la…" — "pour N et…" parses.
- **Slot: unforced.** Clean two-way tie between noun and infinitive; both
  licensing frames are live.

### W4 @703 (a5_01)
`02 50 45 28 94 60 12 98 [20] 12 66 21 35 53 12 48 71`
- Left neighbor 98='vient' (battery-promoted, vient-98-894-reaudit confirmed).
- "venir" + bare infinitive is the licensed construction ("venir faire").
- Noun-20 dies: "vient [20-noun]" needs "de" ("venir de N"); without it,
  ungrammatical. Det-adj and particle slots have no licensing frame.
- **Slot: verbal (infinitive).** Licensed frame: "vient [20-INF] [12]…".

### W5 @741 (a5_02)
`85 93 76 18 82 06 00 36 [20] 30 67 77 81 85 28 00 64`
- Left "pour [36]" (36 class-open); right "30=pas" is a verbal negator with
  no preceding verb under standing values.
- Noun-20: "pour [36] [20-noun] pas" strands "pas". Infinitive-20:
  "pour [36] [20-inf] pas" needs a "ne" that isn't there. No frame licenses
  20 from either neighbor.
- **Slot: unforced.** The window is frame-open on both edges.

### W6 @873 (a5_07)
`46 00 86 70 87 77 89 48 [20] 74 49 16 77 86 78 17 08`
- Left edge is the closed NP "le [89]e" (same arm as @642); right neighbor 74
  is class-open (fenced).
- "le [89]e [20-fin] [74]" parses as clean S-V-X with zero new assumptions
  (subject + finite verb + complement). The noun alternative requires an
  unlicensed clause boundary ("…le [89]e. [20-noun] 74…").
- **Slot: verbal (finite).** Consistent with inf-20-nepas's surviving verbal
  face. The clause-boundary noun alternative is fenced, not licensed.

### W7 @958 (a6_00)
`77 86 96 87 46 24 85 04 [20] 67 96 00 86 56 41 19 24`
- Right edge "67 96 00" = "et/veut par pour": "par pour" is ungrammatical
  under standing values (pasX-adverb-census's "@45 'par pour' impossibility";
  positional "96 00 = par contre" is red-team venue, not adopted here).
- The frame ruptures independently of 20's value — no 20 slot can be
  decided inside a window that doesn't parse.
- **Slot: unforced.** Value-independent right-edge rupture; classification
  re-opens if the red team ratifies "96 00 = par contre".

### W8 @1135 (a6_08)
`00 86 52 37 86 24 77 86 [20] 62 98 00 98 78 62 16 29`
- Left "86 24 77 86" is murky: 24-modal precedes 77-86, and 86's INF-life
  leaves "[86-INF] [24-modal] le [86]" without a clean parse.
- Right anchor "62 98" = "il vient" (62='il' demonstrated, 98='vient').
- Noun-20 needs a bare N–N boundary; finite-verb-20 collides with "il vient"
  (two finite verbs); infinitive-20 has no governor; adverb-20 has no
  established class. No frame forces.
- **Slot: unforced.** Neither neighbor licenses a single slot; the right
  "il vient" anchor is noted for future governor tests.

### W9 @1224 (a7_01)
`77 83 92 61 24 48 30 09 [20] 57 64 79 82 48 29 47 33`
- Left "24 48 30 09" is opaque: modal-24 + inflectional-'e' 48 + "pas" 30 +
  open 09 admits no licensed frame.
- No governor, no determiner, no particle frame reaches 20 from either side.
- **Slot: unforced.** Frame-open on both edges.

## Per-clause pass/fail

1. **C1 PASS** — all nine windows slot-classified window-local with licensing
   frames stated: verbal ×2 (@703 infinitive, @873 finite); unforced ×7
   (@490, @642, @668, @741, @958, @1135, @1224). No window shows a
   det-adj or particle slot under standing values.
2. **C2 PASS** — no value named for 20; the noun/infinitive tension at @668
   and the verbal slots at @703/@873 are class-level observations only. The
   poly-20 red-team docket is untouched.
3. **C3 PASS** — no standing verdict contradicted or downgraded; §7 intact.
   The @873 finite-verb classification rests on inf-20-nepas's surviving
   verbal face and 77-89's noun arm, both battery-standing.

## Census tally (for downstream use)

| Window | Slot | Licensing frame / cause |
|---|---|---|
| @490 | unforced | pivots on 41's open three-arm split |
| @642 | unforced | closed NP left, modal-24 right, no bridge |
| @668 | unforced | noun/inf tie under "pour [20]" |
| @703 | verbal (inf) | "vient [INF]" — noun dies without "de" |
| @741 | unforced | "pas" stranded, frame-open both edges |
| @873 | verbal (finite) | "le [89]e [20] 74" S-V-X, zero new assumptions |
| @958 | unforced | "par pour" right-edge rupture, value-independent |
| @1135 | unforced | murky left "86 24 77 86", right "il vient" |
| @1224 | unforced | opaque "24 48 30 09" left edge |

Notes for future batteries: @668 is the cleanest noun/infinitive discriminator
(pivots on nothing else once tested); @958 re-opens iff red team ratifies
"96 00 = par contre"; @1135's "il vient" anchor is the natural governor test
for infinitive-20. No follow-ups required (promote, not null); these are
observations, not obligations.

## Bookkeeping

- Report: code/crowd17/report_inbox/battery-census-20-open-windows.md
- Queue: `census-20-open-windows` → status `verdict`, result `promote`,
  date 2026-10-09 (pre-write assert passed — was queued/verdictless;
  temp-file + rename; JSON re-validated; only this entry touched; no downgrade)
- Lock created at start, deleted on completion (verified gone)
- R5005, sealed gates, red-team adjudication queue untouched; no existing
  verdict contradicted or downgraded.
