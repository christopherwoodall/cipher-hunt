# Battery verdict: residual-86-finer — verdict NULL (fence outcome; all 10 windows fenced with stated cause)

Date: 2026-10-09. Worker: dce9bcf5-f5d0-43df-a188-df6802862098 (battery worker).
Lock: `code/crowd17/next-token/locks/residual-86-finer.lock` created
2026-10-09T18:05:00Z; no prior lock existed; deleted on completion.
Target id: residual-86-finer. Queue status at take: queued, priority 3.
Stream: repaired 1,847-pair / 96-type parse (`code/side-keyhunt/repaired_offsets.json` +
`data/upstream-ct_R5005.txt`), parsed per `code/side-keyhunt/repair_parse.py`
(asserts held: 1847 pairs, 96 types). `canonical.py` never used. R5005, sealed
gate instances, red-team adjudication queue untouched. No data invented;
every number re-derived below. @-offsets are 0-based stream indices.

## Bar (verbatim, from battery-queue.json)

"resolve iff the residual 10 partitions into frame-consistent subsets or
each window is fenced with stated cause"

Numbered clauses:
1. C1 (partition arm): the residual 10 partitions into frame-consistent
   subsets, each carrying a sub-subset value hypothesis that parses all
   its windows with zero hard contradictions on standing values → resolve.
2. C2 (fence arm): every one of the 10 windows is fenced with a stated
   cause → resolve via fence.
3. C3: no window left unaddressed.

## Method

Residual set inherited from det-86-dlife-partition Subset 4 (2026-10-09,
PROMOTE): the 10 of 86's 26 D-windows not covered by le-life / det-left /
77-adjacent. Re-derived all 32 86-windows byte-exact with ±4 context on the
repaired stream (n(86)=32 confirmed). Tested each of the 10 against standing
values only (§7: pencil 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que;
granted 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce;
provisional 59=est, 77=le; 94=ne STRONG LEAD, not granted). Prior
battery verdicts adopted, not re-litigated: orphan86-300 (KILL),
orphan86-716 (KILL), orphan86-1131-1147 (KILL), det-86-dlife-partition
(PROMOTE), val-86-inf-locus (NULL), syll-83-de-1829 (NULL), plus-jamais-tiebreak
(NULL). Checked today's new verdicts for re-opening force: val-08-successor-class
(08='t' confirm), val-52-630-frame (52 split-shaped), val-76-class-census
(76=noun) — none re-opens any of the 10 windows (recorded per window below).

## Window-level evidence

### Subset A — 00-left defective-left family (@728, @867)

- @728 (a5_02): `65 64 11 00 [86] 48 88 11 24` = "…qui la pour [86] 48 88 la 24".
  11=la (pencil), 00=pour (granted). "la pour" is ungrammatical under
  pencil+granted values under EVERY 86 value — orthogonal granted-defect,
  discriminating nothing about 86. Fenced (defect family of @962's
  "par pour"; par-pour-962-adjudicate).
- @867 (a5_07): `48 47 46 00 [86] 70 87 77 89` = "…ce que pour [86] pre ce le".
  46=que (pencil GT), 00=pour (granted). "que pour" ungrammatical under
  granted values under every 86 value — orthogonal granted-defect. Fenced.

Frame-consistent subset with one common stated cause: left-frame defect
independent of 86's value.

### Subset B — 83-left pair (@899, @1335)

- @899 (a5_08): `82 14 98 83 [86] 16 92 67` = "m [14] vient [83] [86] 16 92 et/veut".
- @1335 (a7_05): `70 52 39 83 [86] 71 64 60` = "pre 52 39 [83] [86] 71 qui 60".
  Frame: "83 [86]" ×2, frame-consistent. 83's '-de'-final fork per
  syll-83-de-1829 (NULL, today): the verb fork is fenced at kill grade
  (no French verb ends in orthographic 'de' that can host finite 24
  adjacently); the NOUN fork stays live ("[38]de" as noun subject).
  With 83 a live noun-shape, "de [86]" forces no 86 value: 86='le' → no
  contradiction at either window; 86=noun → no contradiction; neither
  parses with positive force. Fenced with stated cause: 83's value open,
  no zero-contradiction parse selects an 86 value.

### Subset C — confirmed orphans, kill-grade resolution failures adopted (@300, @716, @1131, @1147)

- @300 (a2_04): `11 78 40 97 [86] 91 18 89` — orphan86-300 KILL: resolution
  via 97's or 78's class refuted at kill grade; @300 orphan CONFIRMED.
  Nothing in today's verdicts re-opens it (52/76/08 results are
  window-orthogonal).
- @716 (a5_01): `12 63 00 66 [86] 01 02 21` — orphan86-716 KILL: no 66 class
  makes "pour [66] [86] [01]" parse with zero contradiction; @716 orphan
  CONFIRMED.
- @1131 (a6_07): `00 86 52 37 [86] 24 77 86` — orphan86-1131-1147 KILL:
  failures localize to 86's own slot. Today's 52 split-shape
  (val-52-630-frame) leaves "52 37 [86]" unresolved — 52's tiers do not
  rescue 86's slot.
- @1147 (a6_08): `29 42 98 98 [86] 67 33 66` — orphan86-1131-1147 KILL:
  no stated neighbor assumption yields a zero-contradiction whole-parse.

Fenced with stated cause: adopted kill-grade resolution failures;
failures localized to 86's slot, not to fenceable neighbors.

### Subset D — open-neighbor fences (@557, @1739)

- @557 (a3_01): `86 59 34 17 [86] 94 59 30` = "[86] est(?) i fois [86] ne(?) est(?) pas(?)".
  59=est provisional, 34=i pencil, 17=fois promoted, 94=ne STRONG LEAD
  (not granted), 30 open/caveated. 86='le' → "fois le" needs a clause
  boundary; the absolute construction ("une fois le [N]...") keeps it
  grammatical but the noun never materializes (94=ne-lead follows).
  86=noun → bare noun after "fois" strained (proper-noun rescue
  unevidenced). Fenced tension, not kill-grade on standing values.
- @1739 (a8_07): `60 12 48 52 [86] 12 34 94` = "60 n(?) 48 52 [86] n(?) i ne".
  12=n pencil GT, 34=i, 94=ne-lead; 48, 52, 60 open. 52's 'plus'/'jamais'
  tie is fenced unbreakable at battery grade today (plus-jamais-tiebreak
  NULL). No standing value constrains 86 here: 'le', noun, and
  word-internal readings all contradiction-free and all force-free.
  Fenced with stated cause: fully open neighbors, no discriminating
  value.

## Per-clause pass/fail

1. C1 (partition arm): FAIL. No sub-subset carries a value hypothesis
   that parses all its windows with zero hard contradictions:
   - Subset A: discriminates nothing about 86 (defect is left of 86).
   - Subset B: 83's noun fork is live but selects no 86 value.
   - Subset C: confirmed orphans — resolution failures localize to
     86's own slot.
   - Subset D: fully open; every hypothesis is force-free.
   The 86='le' and 86=noun hypotheses were already tested across all 10
   by det-86-dlife-partition §4a/4b → NULL; nothing in today's verdicts
   changes any window's standing.
2. C2 (fence arm): PASS. All 10 windows fenced with stated cause:
   A = orthogonal granted-defect (×2), B = 83-value-open fence (×2),
   C = adopted kill-grade orphan confirmations (×4), D = open-neighbor /
   fenced-tension fences (×2).
3. C3: PASS. 10/10 addressed; no window left unaddressed.

## Verdict: NULL (fence outcome)

Per precedent (plus-jamais-tiebreak, word-12-06-1121, val-31-1257-word),
"fence" bars that fence resolve to NULL. The residual-10 is heterogeneous
on current bytes with no positively forced value at any sub-subset; every
window carries a stated fence cause. No standing/red-team verdict
contradicted; §7 intact (no split declared, no second polyvalence named).
The clitic-vs-noun adjudication the parent suggested for @1131/@1147
awaits 24's class / 67's positional ratification — red-team venue, not
battery work.

## Follow-ups (null regenerates work)

1. `residual-86-83pair` (P4): when 83's noun fork lands a value
   (noun-38de-1829-host or successor), re-test @899/@1335 for 86's role
   after "de [38]de". Bar: name 86's role iff the landed 83 value forces
   it with zero new assumptions.
2. `residual-86-557-fois` (P4): re-test the @557 absolute-construction
   reading ("fois [86]") once 59='est' ratifies and 94/30 values land.
   Bar: promote the 'le' or noun reading iff the landed values close the
   absolute construction with zero contradiction.
3. `redteam-86-residual-closure` (P2, gather-only): package this report's
   10-window fence inventory as red-team closure input for the 86 split
   docket (redteam-86-split-docket already queued). Battery gathers; red
   team decides.

## Bookkeeping

- Queue entry `residual-86-finer` was queued/verdictless with no lock at
  take (pre-write assert passed); updated to `status: verdict`,
  `verdict: null` via temp-file + rename; own entry only; no downgrade;
  disk re-validated.
- Lock created on start (2026-10-09T18:05:00Z), deleted on completion
  (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
