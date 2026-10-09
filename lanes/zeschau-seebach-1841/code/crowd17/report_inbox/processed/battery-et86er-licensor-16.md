# Battery verdict: et86er-licensor-16

## Bar (verbatim, pre-registered)

"name the licensor with >=2 frame-legs or fence 16 as the blocker; census '16 X 29' (2x: @1198, @1387), the '06 29 67 86' formula's two instances (@1098 et-rule vs @1390 contested), and 16's full contact profile (n=28)"

## Restated clauses (fixed before testing, not modified after)

- **C1:** '16 X 29' occurs exactly 2x (@1198, @1387) — byte-verified.
- **C2:** The '06 29 67 86' formula's two instances byte-verified (@1098 et-rule, @1390 contested).
- **C3:** 16's full contact profile censused (n=28).
- **C4:** Name the licensor of the "[06]er et [86]er" coordination with >=2 frame-legs.
- **C5 (fallback):** Fence 16 as the blocker with stated cause.
- **Verdict rule (pre-registered):** promote iff C1–C4 pass AND both adverses answered; null iff C4 fails (fence executed under C5) — the licensor stays unnamed.

## Conditional scope (caveat, stated before testing)

The claim's antecedent — "if R_et3 survives" — is unmet: R_et3
(`battery67_final.json`, red-team-graded) vs the §7 positional rule
(BATTERY-PROTOCOL.md, granted) at @1390 is pending red-team
adjudication (`r-et3-vs-positional-redteam`, P1, queued). Everything
below is conditional on R_et3 surviving. If the red team retires R_et3,
this battery moots.

## Method

Read BATTERY-PROTOCOL.md first. Created
`locks/et86er-licensor-16.lock` on start (agent id + UTC timestamp; no
pre-existing lock). Re-derived the 1,847-pair / 96-type stream from
`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`
parsed per `repair_parse.py` (asserts held: 1847 pairs, 96 types).
`canonical.py` never touched. R5005, sealed gates, and the red-team
adjudication queue untouched. All @-offsets are 0-based token offsets on
the repaired stream. Standing values adopted as premises (29='er' GT,
64='qui' granted, 82='m' banked GT, 00='pour' A9, 06='ent' verb ending
promoted, 86 infinitive-class A9); nothing re-litigated.

## Window-level evidence

### C1 — '16 X 29' census (exactly 2x, byte-exact)

- @1198 (a7_00): `16 96 82 | 16 64 29 | 45 52` → X=64 ('qui', granted).
  "16 qui"+"er": no infinitive shape; "qui" cannot sit inside a bare
  infinitive. Not a licensor frame.
- @1387 (a7_07): `68 52 82 | 16 06 29 | 67 86 29` → X=06. The locus
  itself ("[16] [06]er et [86]er"). Circular as a frame-leg — excluded
  from leg-counting.
- Control: the only other "16 29"-adjacent window is @1142
  (`62 16 29 42 98`, "il [16]er"): 29 attaches to 16 itself (16 as verb
  stem, "16er" = the stem's own infinitive) — 16 is the infinitive's
  stem here, not its licensor.

### C2 — formula instances (byte-exact)

- @1098 (a6_06): `...06 29 | 67 | 86 52...` — R_et3 fires (pre=29,
  pre2=06); §7 positional rule does NOT fire (suc=86, suc2=52, not 29).
  Uncontested et-reading.
- @1390 (a7_07): `...06 29 | 67 | 86 29...` — R_et3 fires AND the §7
  positional rule fires (suc=86, suc2=29). Contested (pending red team).
- '06 29 67 86' occurs exactly 2x stream-wide (@1096, @1388 as the
  formula's head) — confirmed.

### C3 — 16's full contact profile (n=28)

Windows: @83, @187, @220, @242, @294, @382, @434, @533, @537, @659,
@844, @876, @900, @903, @1142, @1195, @1198, @1246, @1298, @1370,
@1387, @1394, @1411, @1431, @1437, @1480, @1652, @1832.

- Predecessors: 82 x11 ("m[16]"), 62 x4, 12 x3, 33 x2, 42 x2, 65/32/49/
  86/67/89 x1. — "m'" (82, banked GT) attaches to verbs: 16 is
  verb-class (ordinary transitive profile, not a modal).
- Followers: 00 x4 (@187, @659, @844, @1246 — all "16 pour [INF]";
  pour-governed, not bare), 24 x2, 01 x2, 91 x2, 76 x2, and 16
  singletons (14, 56, 52, 78, 08, 77, 92, 88, 29, 96, 64, 02, 06, 97,
  98, 59). No follower is a bare infinitive except the locus's 06.

### C4 — licensor frame-leg audit (16 as licensor)

A frame-leg = a non-circular window where 16 licenses/governs a bare
infinitive or infinitive coordination. Audit:

1. @1387 — the locus. Circular; excluded.
2. @1198 ("16 64 29") — 64='qui' granted; no infinitive shape. Dead.
3. @1142 ("16 29") — 16 is the stem of its own infinitive, not a
   licensor. Dead.
4. "16 00 [INF]" x4 — pour-governed complements; 16's profile is
   verb+pour-phrase, not verb+bare-infinitive. Dead for BARE licensing.
5. "16 24" x2 — 24 is modal/finite; 16 precedes the modal, licenses
   nothing. Dead.
6. All other 20 windows — no infinitive-shaped complement. Dead.

**Result: 0 non-circular frame-legs.** The >=2 requirement fails by a
wide margin. 16 demonstrably never licenses a bare infinitive in its
other 27 windows; its profile is an ordinary transitive verb
("m[16]" x11, "16 pour [inf]" x4) — not a modal or bare-infinitive
governor.

### C5 — fence 16 as the blocker (executed)

16 is fenced as the blocker: it is the only overt licensor candidate
left-adjacent to the coordination, and its 28-window profile excludes
bare-infinitive licensing (0/27 non-locus windows). Under a surviving
R_et3, the et-reading at @1390 therefore leaves "[06]er et [86]er"
unlicensed at battery level — the licensor problem stands. No new
polyvalence declared; §7 intact. No standing or red-team verdict
contradicted or downgraded (the R_et3-vs-positional-rule conflict is
red-team venue, untouched).

## Adverses answered

- "16's value open": answered — the fence is class/function-level (16
  is not a bare-infinitive licensor); no value named, none needed.
- "the coordination's licensor may not exist - fence honestly":
  answered — fenced honestly; no licensor invented; the locus's only
  frame is circular.

## Per-clause results

- C1: PASS (2x byte-verified: @1198 X=64, @1387 X=06).
- C2: PASS (both instances byte-verified; @1098 uncontested,
  @1390 contested).
- C3: PASS (n=28 censused in full).
- C4: FAIL (0 frame-legs, need >=2).
- C5: EXECUTED — 16 fenced as the blocker.

## Verdict: NULL (fence executed; licensor unnamed; R_et3-conditional)

## Follow-ups proposed (for supervisor queuing; all verified absent from queue)

1. `licensor-86er-exclamatory` (P3) — test the non-governor arm: is
   "[06]er et [86]er" @1390 an exclamatory infinitive (licensed by
   illocutionary force, as the @1028–1040 skeleton), which would make
   the missing overt licensor grammatical? Parse @1387–1396 under the
   exclamatory-infinitive frame with stated assumptions.
2. `verb-16-value` (P3) — name 16's verb value from its 28-window
   profile ("m[16]" x11 + "16 pour" x4); if 16 resolves as a
   factive/modal verb, re-test the licensor question against the named
   value.
3. `coord-Xer-et-Yer-census` (P4) — census all "[X]er et [Y]er"
   coordinations stream-wide; a licensed parallel elsewhere (with an
   overt governor) would supply the missing frame-leg family for the
   @1390 shape.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-et86er-licensor-16.md`
  (this file).
- Queue: `battery-queue.json` `et86er-licensor-16` → status `verdict`,
  result `null`, date 2026-10-09 (pre-write assert passed —
  queued/verdictless; temp-file + rename; JSON re-validated; own entry
  only).
- Lock: created on start with agent id + UTC timestamp; deleted on
  completion.
- `canonical.py` never used; R5005, sealed gates, red-team queue
  untouched; no invented numbers.
