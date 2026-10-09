# Battery `58-noun-adjudicate` — verdict: NULL (fence; stricter distributional bar unmet)

Target: fair distributional test of 58's noun-class vs known nouns 21/26/81 in determiner slots.
Date: 2026-10-09. Worker: agent de8295a2-b36e-49d7-8ae1-50140c8a7d69.
Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` +
`code/side-keyhunt/repaired_offsets.json`, parsed per
`code/side-keyhunt/repair_parse.py`; 1,847 pairs / 96 types re-derived
in-work, asserts held). `canonical.py` never used. R5005, sealed gate
instances, red-team adjudication queue untouched. Lock
`code/crowd17/next-token/locks/58-noun-adjudicate.lock` created on start
(2026-10-09T12:02:00Z); no prior/stale lock existed; deleted on completion.

Indexing: @-offsets are 0-based pair indices.

## Bar (verbatim, pre-registered from battery-queue.json BEFORE testing)

"promote noun-class iff 58 matches known-noun (21/26/81) distribution in
>=2 independent determiner/demonstrative slots with the 24-conflict
adjudicated; kill noun-class iff any window forces non-nominal under the
adjudicated standings"

Numbered clauses (fixed BEFORE the stream census, not modified after):

- **C1 (promote):** 58 matches known-noun (21/26/81) distribution in >=2
  independent determiner/demonstrative slots, with the 24-conflict
  adjudicated in its per-window consequences for 58.
- **C2 (kill):** any window forces non-nominal under the adjudicated
  standings.
- **Verdict rule:** promote iff C1 passes; kill iff C2 passes; else NULL
  (fence) with follow-ups per §4.

Terms (ASD-STE100): "determiner slot" = a window where 58 follows a
determiner or demonstrative (11=la, 47=ce, 87=ce, 79=tout, 77=le,
45='ce' A11 hold). "Adjudicated standings" = the standing battery
verdicts current at run time, including 58-complement-1695's 2026-10-09
PROMOTE (58 = nominal, noun-class) and 24-en-verb-conflict's per-window
consequences. "Kill grade" = a window where every nominal parse is
ungrammatical under standing values.

## Method

1. Read BATTERY-PROTOCOL.md first. Created the lock on start; deleted on
   completion.
2. Re-derived the repaired stream byte-exact per `repair_parse.py`
   (asserts: 1,847 pairs, 96 types). All @-offsets below are 0-based.
3. Re-derived the full census of 58 and the determiner/demonstrative
   predecessor counts for 21, 26, 81 in-session (not copied from prior
   batteries).
4. Adopted as premises, not re-litigated: pencil GT (11=la, 70=pre,
   82=m, 34=i, 29=er, 40=e, 46=que); granted 87=ce, 64=qui, 96=par,
   17=fois, 79="tout" (A5), 00="pour" (A9), 84="on" (A15), 47="ce" (A4);
   provisional 77=le, 59=est; A3 85 verb-stem; A11 45="ce" HOLD
   (R18-strengthened); 21 noun-class (cls), 26 noun (lead), 81
   masculine-abstract-noun (battery standing); 58 = nominal noun-class
   (battery PROMOTE 58-complement-1695, 2026-10-09); §7 (67 et/veut sole
   polyvalence). 1841 diplomatic French throughout.

## Window-level evidence (@-offsets, 0-based)

**58 census (byte-exact, re-derived): n=7.**
Positions: [55, 122, 157, 610, 1202, 1695, 1756].
Predecessors: {85:3, 19:1, 35:1, 02:1, 45:1}.
Successors: {35:2, 66:1, 47:2, 15:1, 17:1}.

58 windows (±4, row ids):
- @55 (a1_01): `37 11 79 85 58 35 53 12 41` — predecessor 85.
- @122 (a1_03): `21 60 90 19 58 66 98 82 48` — predecessor 19.
- @157 (a1_04): `66 84 26 35 58 35 93 52 94` — predecessor 35.
- @610 (a4_00): `64 39 64 02 58 47 77 87 83` — predecessor 02.
- @1202 (a7_00): `16 64 29 45 58 47 43 55 61` — predecessor 45 ('ce', A11
  hold). THE single determiner/demonstrative-preceded 58 window.
- @1695 (a8_06): `27 46 24 85 58 15 23 91 85` — predecessor 85; sole
  surviving parse per 24-en-verb-conflict: "qu'en [85] [58]"
  (gerund + complement, nominal position).
- @1756 (a8_08): `89 26 24 85 58 17 78 41 15` — predecessor 85;
  complement position under all three surviving @1754-56 parses; "[58]
  fois" noun-shaped tail (17=fois granted).

**Determiner/demonstrative-preceded census (re-derived, byte-exact):**
- 58: 1 window — @1202 (45='ce', A11 HOLD, not granted). Zero
  granted-determiner (11/47/87/79/77) predecessors.
- 21 (n=30): 2 windows — @109 (11='la'), @359 (11='la').
- 26 (n=17): 2 windows — @240 (11='la'), @1560 (11='la').
- 81 (n=14): 4 windows — @745, @1241, @1402, @1599 (all 77='le',
  provisional).

## Per-clause results

- **C1 (promote): FAIL.** The bar needs >=2 independent
  determiner/demonstrative slots with 58 as the noun. The re-derived
  census finds exactly 1 — @1202, and it is hold-level (45='ce', A11),
  not grant-level like the reference nouns' 11/77 slots. 1 < 2 at every
  reading of the bar. The distributional asymmetry noted by
  cede-614-subject (zero granted-determiner predecessors for 58 vs
  11/77-attested 21/26/81) is confirmed byte-exact, not refuted.
- **C2 (kill): FAIL.** No window forces non-nominal under the adjudicated
  standings. @1695's sole survivor is nominal ("qu'en [85] [58]");
  @1202 forces non-verbal (nominal survivor, ant-58-ending kill adopted);
  @1756 is nominal-position under all surviving parses; @610/@122/@157
  compatible with zero forced contradiction (58-complement-1695,
  adopted); @55 fenced on the banked "la tout" contradiction (adopted,
  not re-litigated). Firing kill would also contradict the standing
  battery PROMOTE (58-complement-1695); §5.2 bars downgrade.
- **Adjudication state of the 24-conflict (adverse answered):** the adverse
  gated this target on 24-en-verb-conflict resolving. That battery
  returned NULL (2026-10-09) with a red-team escalation — the GLOBAL
  conflict is NOT resolved (24-redteam-adjudication queued, P1, red-team
  venue, untouched). But the bar's functional need — the per-window
  consequences for 58 — IS adjudicated: @1695 modal parse dead, sole
  survivor "qu'en [85] [58]"; @1756 complement position under all
  surviving parses. The gate therefore fired in its usable form, and
  58-complement-1695 already built on it. The brief's "kill/fence
  fallback" is honored: fence taken.

## Verdict: NULL (fence, stated cause)

The stricter distributional bar is not met (1 hold-level demonstrative
slot < 2 required; zero granted-determiner predecessors), while no
window forces non-nominal. This verdict does NOT downgrade or contradict
58-complement-1695's PROMOTE (58 = nominal, noun-class) — that verdict
stands on its own pre-registered bar; this battery only records that the
determiner-slot distribution criterion remains unmet, which is consistent
with that battery's own stated caveat. No standing or red-team verdict
contradicted or downgraded; §7 intact; R5005, sealed gates, red-team
queue untouched.

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `58-45-demslot-rerun-gated` (P4) — gated re-run of the determiner-slot
   count once the red team adjudicates the A11 45='ce' hold: if 45='ce'
   is banked, @1202 becomes a granted demonstrative slot and the promote
   bar needs exactly one more independent det-preceded 58 window; the
   hunt is then resolving 19/02/35 classes at @122/@157/@610 for
   determiner-shaped predecessors. Do not dispatch before the A11 ruling.
2. `58-det-gap-corpus` (P3) — corpus test: in 1841 diplomatic French, do
   gerund-complement nouns of the "en [V]ant [bare-N]" shape (the @1695
   frame) license determiner-less position at the observed rate? If yes,
   the zero-determiner-predecessor asymmetry is expected for 58's nominal
   subtype, not evidence against noun-hood; if bare gerund complements
   are rare, the asymmetry stands as an answered residual.
3. `58-value-name` (P3) — name 58's VALUE from its nominal windows:
   @1756 "[58] fois" ("X fois" = "une fois"-shaped temporal NP) +
   @1695 "qu'en [85] [58]" (gerund complement of 85's verb) +
   @1202 "ce [58]" (demonstrative + noun). Bars: one French noun fitting
   all three frames with zero ungranted assumptions; fence if the lexical
   field underdetermines. Value only; class standing not re-opened.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-58-noun-adjudicate.md`
  (this file).
- Queue: `58-noun-adjudicate` → status `verdict`, result `null`,
  2026-10-09 (pre-write assert passed — was queued/verdictless;
  temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `locks/58-noun-adjudicate.lock`: created on start, deleted on
  completion (verified gone).
