# Battery `val-61-wordbound-1257` — verdict: NULL

**Target:** `val-61-wordbound-1257` (P3)
**Claim:** When 61 receives any value/grant, re-test '61 31' wordhood at @1256-1257 (stream hapax). The surviving word-internal-31 arm hinges on this boundary.
**Date:** 2026-10-09

## Bar (verbatim, pre-registered)

"name the boundary (one word vs two) with zero new assumptions, else fence word-internal-31 at the locus"

Restated as numbered pass/fail clauses (pre-registered before testing — bar not modified after data):

- **C1:** Name the @1256–1257 boundary (one word vs two) with zero new assumptions under standing values.
- **C2:** Else, fence the word-internal-31 arm at the locus with stated cause.

## Method

Read BATTERY-PROTOCOL.md §1–§8 in full before testing. Created
`code/crowd17/next-token/locks/val-61-wordbound-1257.lock` on start (agent
6d8bcb81-3de7-4425-9d59-b17ba0293df2, 2026-10-09T21:20:00Z); no stale lock
present. Re-derived the repaired 1,847-pair / 96-type stream in-session from
`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`
(parsed like `repair_parse.py`: `[s[i:i+2] for i in range(o, len(s)-1, 2)]`).
Asserts held: 1,847 pairs, 96 types. `canonical.py` never used. R5005,
sealed gates, red-team adjudication queue untouched. Standing values held
fixed per §7.

Gate check (supervisor-verified, re-confirmed in-session):
`val-61-premier` → verdict/promote 2026-10-09 (locus-level): 61 = "premier"
(single-group spelling of 70-82-34-29) at @1556 ("61 40 17" = "première
fois"). 61's GLOBAL value stays fenced — `val-61-contact`'s KILL of any
global 61 value stands (verdict/kill, 2026-10-09). Registry carries no 61
cell at all.

## Window-level evidence (all byte-verified on the repaired stream)

### The locus — @1256–1257 (row a7_02)

`@1248–1267: 67 46 26 30 06 65 46 01 61 31 29 69 88 01 09 11 50 46 69 88`

Reads under standing values: `[67] que(46) [26] [30] ent(06) [65-N] que(46)
[01] [61] [31] er(29) [69-N] [88-V] [01] [09] la(11) [50] que(46) [69-N]
[88-V]`.

- "61 31" occurs exactly **once** stream-wide (@1256–1257): hapax confirmed.
- "31 29" occurs exactly once (@1257): hapax confirmed (parent's census).
- Adverses adopted: 01 and 61 unvalued; 31 unvalued globally (battery-grade
  finite-verb legs at @338/@1647, "qui [31]" ×2, per val-31-verb-test).

### Why the @1556 grant does not transfer — three independent blocks

1. **Scope block (zero-new-assumptions):** `val-61-premier` is explicitly
   locus-level: "61 = 'premier' ... **at this locus**". Applying it at @1256
   is itself a new assumption — the exact thing C1 forbids.
2. **Standing-verdict block:** `val-61-contact` KILL'd any global 61 value
   (four discriminating frames force disjoint classes). Extending
   61="premier" to @1256 contradicts that standing KILL; per §5 a battery
   worker does not overwrite it.
3. **Affirmative-resistance block:** `premier-61-admit-fence` PROMOTE
   classifies @1256 in the premier-RESISTING set ("FALSE at all 5
   unresolved: ... @1256 (01|31) ..."): the conditioned ordinal-slot rule
   admits exactly the four premier-admitting windows and none of the five
   unresolved — left neighbor 01 is not a determiner cell, so the premier
   slot cannot license 61 here.

### Boundary-naming routes — all fail C1

- **Two words ("61 | 31"):** needs 61 as a standalone word at @1256 → needs
  61's class. 61's class is open everywhere except the @1556 locus grant,
  which does not transfer (blocks 1–3 above). Naming it = new assumption.
- **One word ("61 31"):** needs a French word spelled [61][31]. Both cells
  unvalued; no candidate statable without inventing values = new
  assumptions.
- **One word ("01 61 31"):** same, plus 01 unvalued. No candidate statable.
- **Right-side route via 31's finite-verb legs:** "61 | [31-fin]" would need
  "01 61" to compose a subject NP under "que [01] [61] [31-fin]" — the
  parent already showed "que [01] [61] [N]" has no licensed parse under
  standing values. New assumption. (The "31 | 29" segmentation alternative
  is parent follow-up `locus-1257-reseg`, already queued — not duplicated.)

**C1: FAIL** — no boundary naming available with zero new assumptions.

### Else-arm (C2) — cannot be executed with stated cause

Fencing word-internal-31 at the locus needs a kill-grade contradiction
against "61 31" / "01 61 31" wordhood. None exists under standing values:
the parent battery (val-31-1257-word, NULL) already established "no
standing value licenses '61 31' / '01 61 31' as a word, and nothing at the
locus contradicts it." The new evidence does not supply one either: the
@1556 grant is locus-scoped and affirmatively inapplicable at @1256
(block 3), so it cannot be wielded as a premise against wordhood here.
Executing C2 without a stated cause would be a new assumption in disguise.

**C2: FAIL** — fence not executable with stated cause; the bar as written
is unexecutable at battery grade.

## Per-clause results

- **C1: FAIL** — boundary not nameable with zero new assumptions (61's
  class open at @1256; the @1556 locus grant does not transfer).
- **C2: FAIL** — word-internal-31 cannot be fenced with stated cause on
  current evidence.

**Verdict: NULL.** The surviving word-internal-31 arm from val-31-1257-word
remains unfenced. No standing or red-team verdict contradicted or
downgraded (§5 does not fire — this result is consistent with
val-61-contact's KILL, val-61-premier's locus PROMOTE, and
premier-61-admit-fence's PROMOTE); §7 intact. Canonical-stream caveat
stands (row a7_02 offset unvalidated).

## Follow-ups proposed (all verified ABSENT from battery-queue.json; supervisor to queue per §4)

1. `wordbound-61-31-rerun` (P4, gated) — re-arm this exact bar iff the red
   team adjudicates 61's scope (upgrades val-61-premier's locus grant or
   rules the 61-duality conditioned-global). Do not dispatch before a
   red-team 61-scope ruling lands.
2. `val-61-1256-class` (P4) — name 61's class at @1256 independently of the
   @1556 value, in the frame "que [01] [61] [31]er [69-N] [88-V]". A class
   naming discriminates the boundary without extending the locus grant.
3. `duality-61-redteam-input` (P4, gather-only) — package the 61 tension as
   red-team input: val-61-contact KILL (no global 61 value) vs
   val-61-premier locus PROMOTE (61="premier" @1556) vs
   premier-61-admit-fence (@1256 premier-resisting). Ask whether the
   one-group "premier" reading can ever license a "61 31" composition.

Not duplicated: `locus-1257-reseg` already queued; `poly-31-docket-input`
already verdict/null.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-61-wordbound-1257.md`
- Queue: `val-61-wordbound-1257` → `status: verdict`, `verdict: {result:
  null, report: code/crowd17/report_inbox/battery-val-61-wordbound-1257.md,
  date: 2026-10-09}` (pre-write assert passed — was queued/verdictless;
  target-id-unique temp file + atomic rename; disk re-read confirms; own
  entry only; no downgrade)
- Lock created on start (2026-10-09T21:20:00Z, agent
  6d8bcb81-3de7-4425-9d59-b17ba0293df2, no stale lock), deleted on
  completion.
- `canonical.py` never used. R5005, sealed gates, red-team adjudication
  queue untouched.
