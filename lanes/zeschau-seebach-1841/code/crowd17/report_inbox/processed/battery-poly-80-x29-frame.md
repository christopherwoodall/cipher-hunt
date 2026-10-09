# Battery report: poly-80-x29-frame

- Target id: `poly-80-x29-frame`
- Claim: "re-segmentation audit of the @1032/@1156 split feeds the poly-80-docket"
- Date: 2026-10-09
- Worker: battery worker (subagent 4e43222d-557e-4778-80a0-0742ff12aed8)
- Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` +
  `code/side-keyhunt/repaired_offsets.json`, parsed like
  `code/side-keyhunt/repair_parse.py`; n=1847 asserted, 96 groups asserted).
  All @-offsets are 0-based repaired-stream indices. `canonical.py` never used.
  R5005 not touched.
- Lock: `code/crowd17/next-token/locks/poly-80-x29-frame.lock` (created at
  start, deleted at end; no prior lock existed).

## Bar (verbatim, pre-registered before testing)

"re-segment @1030-1033 ('[03]er [80]-le' imperative+enclitic) and
@1154-1157 ('[92]er [80] fois' determiner+fois) with window-level parses;
package both as docket evidence for poly-80-docket"

Numbered pass/fail clauses (restated before testing, not modified after):

1. (C1) W1 (@1030–1033, row a6_03): produce a window-level parse of
   "03 29 80 77" as "[03]er [80]-le" = infinitive + imperative verb with
   enclitic 'le', licensed by standing values; state the cause of death of
   the nominal/determiner rival readings at this window.
2. (C2) W2 (@1154–1157, row a6_09): produce a window-level parse of
   "92 29 80 17" as "[92]er [80] fois" = infinitive + determiner/quantifier +
   "fois", licensed by standing values; state the cause of death of the
   verbal rival reading at this window.
3. (C3) Package both windows as docket evidence for the poly-80-docket.
   Per §7, no polyvalence is declared at battery level — evidence gathered
   for the red team only.
4. (C4) Adverses answered: the §7 sole-polyvalence adverse (battery gathers
   only, never declares).

## Method

1. Re-derived the repaired stream in-session (1,847 pairs, 96 types).
   Never used `canonical.py`. R5005 not touched.
2. Byte-exact census: the "29 80" collocation occurs exactly 4x
   stream-wide — @1031 (a6_03), @1155 (a6_09), @1321 (a7_04), @1595 (a8_02).
3. Row offsets: a6_03 = 0, a6_09 = 0 (repaired stream; upstream offsets
   unvalidated — canonicality caveat stands).
4. Standing values spent (banked/granted/promoted/provisional only):
   11="la" (banked GT), 29="er" (banked GT), 64="qui" (granted),
   96="par" (promoted), 17="fois" (promoted), 00="pour" (A9, leg-1
   class-level), 77="le" (provisional), 82="m" (banked letter),
   A8 (80/89 verb-frames granted, value open), R18-011 (92 = verb class,
   subset-scoped).

## Window W1 — @1030–1033, row a6_03 (C1)

Stream bytes, @1025–1044:

    64 96 43 87 01 03 29 80 77 11 70 82 34 29 40 17 77 82 63 11
    qui par [43] ce [01] [03]er [80] le la pre m i er e fois le m [63] la

Key anchors: @1034–1039 = "11 70 82 34 29 40" = "la première" — the
gloss-anchored crib (the a6_03 occurrence per repair_parse.py's gloss
check), banked ground truth. @1040 = 17 = "fois" (promoted). So the
right edge is the fully byte-anchored French phrase "la première fois".

**Re-segmentation (bar's reading):** @1030–1031 "03 29" = "[03]er"
(infinitive; 03 = verb stem in the "03 29" frame, A10-holding stem
battery premise, cited not re-litigated). @1032–1033 "80 77" =
"[80]-le": 80 is an imperative verb stem and 77 = 'le' (provisional)
is its enclitic direct-object pronoun. A8 grants the 80 verb-frame
(value open). French imperative + enclitic object is ordinary
("prends-le", "donne-le"); the following "la première fois" parses
as a temporal adverbial NP ("for the first time"). Full local read:

    …[03]er | [80]-le | la première fois | le m…

**Rival readings at W1 (cause of death):**
- 80 nominal ("le [80]" with 77 = determiner): kill grade. The byte
  sequence is "80 77 11 70" = "[80] le la pre…" — two stacked
  determiners ("le" + "la première") with no head between them is
  ungrammatical in every register of 1841 French. No licensed head
  can sit between 77 and 11; 80 cannot rescue it (a postposed
  adjective would need to precede "la première", not follow it).
- 80 determiner/quantifier: kill grade for the same reason — a
  determiner before "le la première" is a determiner pile-up.
- Verbal-80 is the sole licensed survivor at this window.

**Clause-boundary caveat (stated, not hidden):** the imperative needs
a clause boundary between the "[03]er" infinitive and "[80]-le"
(the left run "ce [01] [03]er" is not fully licensed at battery
grade: 01's general values are kill-grade dead, bound "-ci" lives
only in ce-contexts — this is one, but the bound-ci battery owns
that question). The re-segmentation stands on the "80 77" byte
contact and the determiner-pile-up kill of the rivals; it does not
license the left edge.

## Window W2 — @1154–1157, row a6_09 (C2)

Stream bytes, @1144–1166:

    42 98 98 86 67 33 66 84 02 00 92 29 80 17 77 82 44 83 21
    [42] [98] [98] [86] et [33] [66] on [02] pour [92]er [80] fois le m [44] [83] [21]

Row boundary: @1152 = "02" is the last pair of row a6_08; @1153 =
"00" ("pour") is the first pair of row a6_09. The stream is
continuous across the boundary (per repair_parse.py's per-row
tokenization; noted, not adjudicated).

**Re-segmentation (bar's reading):** @1154–1155 "92 29" = "[92]er"
(infinitive; 92 = verb class subset-scoped per R18). "pour [92]er"
is a licensed pour+infinitive purpose frame (A9). @1156 "80" =
determiner/quantifier, @1157 = 17 = "fois" (promoted): "[80] fois" =
e.g. "une fois" / "deux fois". "fois" never stands bare in the lane
(evidence: standing fois-frames); the det/quant slot is mandatory,
and 80 is its sole occupant. Full local read:

    pour [92]er | [80] fois | le m…

**Rival readings at W2 (cause of death):**
- 80 verbal (finite or imperative): kill grade. "[92]er [80-V]
  fois" = infinitive + finite verb with no conjunction or governor —
  ungrammatical; and bare "fois" as a verb's direct object is
  ungrammatical ("fois" needs det/quant/num). The enclitic variant
  "[80]-le" is also dead: 77 does not follow 80 (17 intervenes).
- 80 nominal: kill grade. "[N] fois" — a bare noun before "fois" —
  is ungrammatical; "fois" takes a determiner, not a bare noun
  modifier, in this position.
- Determiner/quantifier-80 is the sole licensed survivor at this
  window.

## Docket evidence package for the poly-80-docket (C3)

| window | 80's role | licensed reading | killed rivals |
|---|---|---|---|
| W1 @1030–1033 (a6_03, off 0) | verbal: imperative stem + enclitic 'le' (77 provisional) | "[03]er [80]-le la première fois" — imperative + enclitic + temporal NP | nominal-80 (kill: "le la première" determiner pile-up); determiner-80 (kill: same pile-up) |
| W2 @1154–1157 (a6_09, off 0) | determiner/quantifier | "pour [92]er [80] fois" — pour+infinitive + [80] fois | verbal-80 (kill: "[V] fois" bare-fois); nominal-80 (kill: "[N] fois"); enclitic (kill: no adjacent 77) |

- The role split occurs INSIDE the "29 80" collocation (4x
  stream-wide: @1031, @1155, @1321, @1595). Uniform-role hypotheses
  each die on ≥1 window — adopted from the owning battery
  `x29-80-collocation` (null, 2026-10-09), cited not re-run.
- A8 (80/89 verb-frames, value open) licenses the verbal role; the
  determiner role is licensed by 17="fois" (promoted) needing its
  det/quant slot.
- Canonicality caveat: both rows are offset-0 with unvalidated
  upstream offsets. The kills hold on the canonical stream per
  protocol.
- **No polyvalence declared.** Per §7 (67 et/veut the sole true
  polyvalence), this battery gathers evidence only. The red team
  owns the poly-80-docket adjudication. The two docket-adjacent
  windows (@1321, @1595) are owned by `x29-80-collocation` and
  `x29-80-1596-nominal` (null); not duplicated here.

## Per-clause pass/fail

1. (C1) W1 re-segmentation: PASS — "[03]er [80]-le" parses under
   standing values (A8 + 77='le' provisional); nominal and
   determiner rivals killed at kill grade on the "le la première"
   byte evidence. Left-edge "[03]er" boundary caveat stated.
2. (C2) W2 re-segmentation: PASS — "pour [92]er [80] fois" parses
   under standing values (A9 + 92 verb class + 17='fois'); verbal,
   nominal, and enclitic rivals killed at kill grade.
3. (C3) Docket package: PASS — both windows packaged with role,
   licensed reading, killed rivals, and caveats above; no
   polyvalence declared (§7 intact).
4. (C4) Adverse answered: §7 sole-polyvalence respected — battery
   gathers evidence for the red-team poly-80-docket only; nothing
   was dispatched to the red-team adjudication queue.

## Verdict: PROMOTE (finding grade — evidence package)

Both pre-registered re-segmentations are delivered with
window-level parses, licensed under standing values, with rival
readings killed at kill grade on byte evidence. The package is
ready for the red-team poly-80-docket. Red-team ratification is
required before any banked use. No follow-ups required (promote,
not null).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-poly-80-x29-frame.md`
- Queue: `battery-queue.json` → `poly-80-x29-frame` status `verdict`,
  result `promote`, date 2026-10-09 (pre-write assert passed — was
  `queued`/verdictless; temp-file + rename; JSON re-validated; only
  this entry touched; no downgrade — no prior verdict existed).
- Lock created at start, deleted on completion.
- `canonical.py` never used; R5005, sealed gates, red-team
  adjudication queue untouched.
- No standing or red-team verdict contradicted or downgraded; §7 intact.
