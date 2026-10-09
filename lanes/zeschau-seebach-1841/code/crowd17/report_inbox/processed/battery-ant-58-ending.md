# Battery verdict: ant-58-ending

**Verdict: KILL** — 58='ant' (present-participle ending) is dead at kill grade.
One window forces 58 non-verbal under standing values; the promote side reaches
only 2 of the required 3 legs.

## Bar (verbatim from battery-queue.json)

> promote 58='ant' iff >=3 windows parse as participle endings with independent
> frames; kill iff any window forces 58 non-verbal.

Numbered clauses:

1. **Promote clause** — >=3 windows parse as participle endings with independent
   frames.
2. **Kill clause** — any window forces 58 non-verbal.

## Method

- Read BATTERY-PROTOCOL.md first; lock created on start, deleted on completion.
- Re-derived the repaired 1,847-pair stream exactly per
  `code/side-keyhunt/repair_parse.py` (`repaired_offsets.json` +
  `data/upstream-ct_R5005.txt`; byte-exact
  `[digits[i:i+2] for i in range(o, len(digits)-1, 2)]`). 1,847 pairs / 96
  groups confirmed. `canonical.py` never touched.
- 58 census on the repaired stream: **n=7**, 1-based @56, @123, @158, @611,
  @1203, @1696, @1757. The "58 follows 85 x3" count re-derives exactly
  (@56, @1696, @1757).
- Standing values used: pencil 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que;
  granted 87=ce, 64=qui, 96=par, 17=fois, 79="tout" (A5), 00="pour" (A9),
  84="on" (A15), 47="ce" (A4); frames 85 verb-stem (A3), 24=en (A3 GT);
  HOLD 45="ce" (A11, strengthened R18-014); 67 sole true polyvalence (§7).
  1841 diplomatic French throughout.
- Coordination with en85-gerund-reaudit (verdict promote, processed/): its bar
  owned the "en [85]" gerund frames; it explicitly left 58 open
  ("58 open as the gerund's complement (cf. ant-58-ending follow-up ...,
  not assumed here)"). This battery tests 58's value only — no gerund-frame
  bar re-litigated, no duplication.

## Window-by-window

Convention: @ = 1-based position of 58 on the repaired stream.

### @56 (a1_01): `92 79 37 11 79 85 [58] 35 53 12 41 08 34` — FAIL (promote leg)

58's left neighbor is 85 (verb-stem A3), but 85's left neighbor is 79="tout"
(A5 granted). The claim's own theory needs the gerund frame "en [85]-ant";
here there is no "en" (24) — only "tout". "tout [85]ant" is ungrammatical in
1841 French (bare participle needs "en" or a host clause; "tout" provides
neither). Worse, the wider window shows "11 79" = "la tout" — the banked-value
contradiction recorded in round 18 (@52-53). The window does not parse as a
participle ending under standing values. Fenced, not a leg.

### @123 (a1_03): `21 60 90 19 [58] 66 98 82 48` — INCONCLUSIVE

Left neighbor 19 is fully open. "19-ant" could be a participle-shaped word,
but no independent frame establishes it (no "en", no host clause, 66/98 open).
Epistemic fail — not a leg, not a kill.

### @158 (a1_04): `66 84 26 35 [58] 35 93 52 94` — INCONCLUSIVE

Left and right neighbors both 35 (open). No frame. Not a leg, not a kill.

### @611 (a4_00): `64 39 64 02 [58] 47 77 87 83` — INCONCLUSIVE

Left neighbor 02 open; "02-ant ce" (47="ce" A4) is conceivable ("portant ce"-
shaped) but 02's value is open and no independent frame forces it. Not a leg,
not a kill.

### @1203 (a7_00): `96 82 16 64 29 45 [58] 47 43 55 61 21 65` — KILL-GRADE

58's left neighbor is 45, right neighbor is 47.

- 45="ce" per the A11 HOLD — "not negotiable" in the battery protocol and
  **strengthened by R18-014** ("Installs 45='ce' at @314 — NOT 45='dict'").
- The rival 45="dict" reading is unavailable here: battery-dict-45-
  host-inventory (verdict promote, narrow) certified 'verdict' (78-45) as the
  **sole** host of 45="dict". At @1203, 45's neighbors are 29/58 — no 78
  involvement — so 'dict' is excluded and 'ce' holds.
- 47="ce" per the A4 allophone-tier grant.
- For 58='ant' (a bound present-participle ending) to parse, it must compose
  with its left neighbor 45: "ce" + "ant" = **"ceant" — not a French word**.
  Rightward attachment to 47 is morphologically impossible ("ant"+"ce" is not
  a word either; endings attach left).
- No rescue exists under standing values. 58 is forced non-verbal at this
  window: it cannot be the 'ant' participle ending. Since §7 reserves
  polyvalence for the red team (67 is the sole true polyvalence), the global
  claim 58='ant' is falsified.

### @1696 (a8_06): `14 60 27 46 24 85 [58] 15 23 91 85 33 94` — LEG (promote side)

"46 24 85 58" = "que en [85]-ant": 46="que" (pencil) forces the "qu'en"
elision, 24="en" (A3 GT), 85 verb-stem (A3 frame). The gerund frame is
independent and the 'ant' ending composes with the verb stem. This is a clean
participle-ending leg. (Rival segmentation "en [85] [58]" also parses — the
en85-gerund-reaudit promoted that frame without deciding 58 — but the
'ending' segmentation is grammatical and frame-independent, so it counts as
a leg for clause 1.)

### @1757 (a8_08): `07 28 89 26 24 85 [58] 17 78 41 15` — LEG (promote side, weaker)

Same "24 85 58" = "en [85]-ant" gerund shape as @1696. The ending+frame parse
holds; the successor 17="fois" (granted) makes the wider window strained
("en [85]ant fois" lacks a determiner), but the participle-ending parse with
its independent gerund frame stands. Counted as a leg with the caveat noted.

## Per-clause results

1. **Promote clause: FAIL** — 2 legs (@1696, @1757) < 3 required. @56 fails
   ("la tout" contradiction + ungrammatical "tout"+participle); @123/@158/@611
   are epistemically inconclusive (open neighbors, no independent frame).
2. **Kill clause: FIRES** — @1203 forces 58 non-verbal: 45="ce" (A11 HOLD,
   R18-strengthened; 'dict' excluded by the certified sole-host finding) +
   47="ce" (A4) makes "ceant" a non-word, so 58 cannot be the 'ant' ending
   there. One incompatible window kills the global claim (§7: no
   battery-level polyvalence).

## Adverses

- "58's value fully open": answered — no prior value verdict on 58 exists;
  this kill names nothing and constrains nothing beyond 58≠'ant'.
- "coordinate with en85-gerund-reaudit (owns the gerund-frame bar), do not
  duplicate": honored — the gerund frames were not re-litigated. The re-audit's
  promote verdict is not contradicted: its gerund confirmations survive under
  the "en [85] [58]" segmentation, which this battery leaves intact. Only the
  'ending' rival segmentation of @1694/@1755 is closed off, and the re-audit
  explicitly declined to decide 58.

## Standing-state check

No standing verdict contradicted or downgraded. R5005, sealed gate instances,
and the red-team adjudication queue untouched.

## Residuals (not decided)

- The two gerund windows (@1696/@1757) now favor the "en [85] [58]" complement
  segmentation by elimination of the 'ending' rival; 58's value there remains
  open.
- @123/@158/@611 remain open windows for any future 58-value hypothesis.
- @56's "11 79" = "la tout" contradiction stands as recorded in round 18.

## Verdict: KILL

58='ant' is dead: @1203 forces 58 non-verbal under the A11 HOLD, and the
promote side reaches only 2 of 3 required legs.
