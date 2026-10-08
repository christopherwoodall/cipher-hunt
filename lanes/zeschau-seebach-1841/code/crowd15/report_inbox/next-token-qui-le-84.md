# Battery A13 — "qui le 84" ×3 (@144, @1445, @1801)

Date: 2026-10-07. Runner: battery-runner (resumed, round 15).
Stream: repaired 1,847-pair parse recomputed in-session
(`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`,
per `code/side-keyhunt/repair_parse.py`).

Source: finder P5 (next-token-findings-qui.md).
Windows: @144 `67-[64-77-84]-29-87` ("qui le 84 er ce"),
@1445 `[37]-64-77-84-59-36` ("qui le 84 est 36"),
@1801 `[79-ce]-64-77-84-59-35` ("qui le 84 est 35").
Slot-3 alternation: 29="er" (@144) vs 59="est" (@1445/@1801).
Standing: 77="le" provisional; 84 polyvalent (F53: 84="en" arm pre∈{46,94,82}
n=4; 84=masc-noun arm pre∈{77,11} n=8; 13/25 unclassified — re-derive n).

## Pre-registered bar (written BEFORE touching data)

- **Step 1 — 84's contact profile (re-derived):** full predecessor/
  successor census of 84. Classify each 84-window into the known arms
  ("en"-arm, masc-noun arm) or unclassified; count.
- **Step 2 — the three windows:** which 84-arm does each fall in?
  - @144: "qui le 84 er ce" — if 84="en"-arm: "qui l'en [29]…"?
    if masc-noun: "qui le [84-noun] er…"?
  - @1445/@1801: "qui le 84 est [36/35]" — "qui le [84] est [noun/adj]".
- **PROMOTE** a reading of "qui le 84" iff ≥2 windows land in the SAME
  84-arm with a grammatical parse and no contradiction.
- **HOLD** if the three windows split across arms or the parse needs
  84's value (which this battery does not promote).
- **Do NOT re-derive 77="le"** (finder's explicit constraint); the frame
  is conditional on it — say so.
- The 29/59 slot-3 alternation ("er" vs "est") must be addressed: same
  frame with different slot-3, or two frames? Decide with cause.

## Data

### Step 1 — 84's contact profile (re-derived, n=25)

preds: 77×7, 66×2, 89×2, 46×2, 53×2, 82×1, 91, 65, 48, 06, 17, 32.
sucs: 59×4, 24×3, 02×2, 92×2, 09×2, 29, 26, 53, 74, 91, 73, 51.

Arm classification:
- **masc-noun arm (pre=77): 7×** — all seven 77-84 windows, INCLUDING the
  three "qui le 84" windows (@144, @1445, @1801). (11-84 @1619 per
  ANOMALIES makes 8; 11 not in top-12 preds — accepted from inventory.)
- **"en"-arm (pre∈{46,94,82}):** 46-84 ×2, 82-84 ×1 = 3 (ANOMALIES's
  94-84@1664 not in preds — 94→84 may be 1× below the top-12 cutoff;
  arm stands at 3–4).
- Unclassified: ~14/25 (consistent with F53's partial polyvalence).

### Step 2 — the three windows (all pre=77 → masc-noun arm)

| pos | window | parse |
|---|---|---|
| @144 | 67-64-77-84-29-87 | "[67] qui le [84-N] [29]er ce" |
| @1445 | 37-64-77-84-59-36 | "[37] qui le [84-N] est [36]" |
| @1801 | 87-64-77-84-59-35 | "ce qui le [84-N] est [35]" |

**"le [84] est [X]" ×2** (@1445, @1801): "the [N] is [36/35]" — clean
noun+est frame, the strongest leg. (36/35 consecutive — weak link noted,
not built on.)
**"qui le [84]" ×3**: the trigram head is stable across all three;
"qui"'s integration is loose (cf. A7's clause-boundary parse — "qui"
closes the prior clause).

### Slot-3 alternation — two sub-frames, decided with cause

- Sub-frame (i) "qui le [N] est [X]" ×2 (@1445, @1801): grammatical,
  "84-59" = "[N] est" is the distributional anchor (84→59 ×4 globally,
  top successor).
- Sub-frame (ii) "qui le [N] [29]er ce" ×1 (@144): "le [N]" + "er"+"ce"
  — the infinitive-ish tail is unparsed. HELD, not forced.
One head ("qui le [84-N]"), two continuations. The alternation is real;
(i) promotes, (ii) waits.

### "le"+verb rival (77="le" as object pronoun)

"qui le [84-verb]" ("who [verb]s it") is grammatical — but 84's sucs
(59×4 "est", 24×3…) are noun-like, not verb-like ("[verb] est" is odd;
"[N] est" is clean). The masc-noun arm wins on distribution. The rival
is recorded and disfavored, not killed (77="le" is provisional either way).

## Verdict

- **PROMOTE the "qui le [84-noun]" unit** (3×, all in the pre=77 masc-noun
  arm, grammatical head) **+ the "le [N] est [X]" sub-frame** (2×,
  distributionally anchored by 84→59 ×4). Conditional on 77="le"
  (finder's constraint honored — not re-derived).
- **HOLD** @144's "[29]er ce" tail (sub-frame ii, single window).
- **84's value NOT promoted** — noun-arm confirmed distributionally;
  the noun itself unnamed. 84's remaining ~14 unclassified windows untouched.
- **77="le" dependency stated:** if 77 falls, this frame falls with it.
