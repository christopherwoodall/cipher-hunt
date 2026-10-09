# Battery report: lon-77-le-gate

**Target:** `lon-77-le-gate` (P2)
**Date:** 2026-10-09
**Verdict:** NULL (trigger condition not met — the bar's precondition is absent, not falsified)

## Bar (verbatim from queue)

"re-test the @508 discriminator once 77's value resolves; a non-'le' 77 dissolves both readings of the discriminator — record, do not force"

## Bar restated as numbered clauses

1. (C1) 77's value has RESOLVED (77='le' promoted to a standing value, or overturned in favor of a named non-'le' value) at red-team or banked grade.
2. (C2) Given C1: re-test the @508 discriminator (62-94's two readings under the 77-slot) under the resolved 77 value; if 77 resolves non-'le', record that both readings dissolve (no forcing).
3. The bar fires only on C1. If 77's value is still provisional, the re-test is not actionable — record the trigger as absent.

## Method

Re-derived the full stream on the repaired 1,847-pair parse
(`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`;
upstream tokenization `[s[i:i+2] for i in range(o, len(s)-1, 2)]`).
`canonical.py` never used. R5005, sealed gate instances, red-team adjudication
queue untouched. Lock created on start, deleted on completion.

77's resolution status was checked against: the protocol's standing
constraints (§7), REPORT.md's registry row for 77, the latest red-team round
(next-token-redteam-r18, dated 2026-10-08 — the controlling round), and all
queued 77-value targets in battery-queue.json.

## Window-level evidence

**E1 — The discriminator window (byte-exact, re-derived).**
0-based @505–513, row a3_00: `21 67 77 62 94 64 98 65 88`
= "[21-noun] et le [62][94] qui vient [65-noun] [88]".
The discriminator is the 77-slot at @507. Under provisional 77='le',
the two readings of 62-94 (@508–509) are:
(a) two-word "il ne" (62='il' demonstrated; adverse's 62→94 x9 re-read);
(b) one-word "[noun]ne" (syll-94-508-verify PROMOTE, syllabic 94,
explicitly conditional on provisional 77='le'; w508-noun-ne PROMOTE names
"trône"). Both readings are live only inside the "et le ___ qui vient"
frame the 77-slot builds. A non-'le' 77 removes the determiner frame and
dissolves both readings — the bar's dissolution clause, correctly recorded.

**E2 — 77's value has NOT resolved.** Protocol §7 standing constraint:
"Provisional: 59=est, 77='le'". REPORT.md registry row (line 7424):
"| 77 | le | **provisional** — DEMOTED prom→prov round-16; R17-023 CONFIRMS
(no new evidence; R16-001 stands). Docket: 76-noun battery (F104) resolved
in favor — 77='le' now re-evaluable by the red team". Line 2787: "promotions
and the 77='le' provisional→promoted merge are pending". The 77="gouv" rival
was demoted→disfavored (line 1994/6368), which removes a competitor but does
not constitute a resolution. Queued 77-value targets: `le-77` (verdict null),
`lon-ne-77-62-94` (verdict null), `lever-77-78` (verdict null),
`le-77-residual-adjudicate` (queued), `frame-77-78-43-slot` (queued) — no
target has named or promoted any 77 value since. The controlling red-team
round (r18) does not adjudicate 77's value; it notes a potential adverse
against provisional 77='le' (parallel to s5-foundation's use against 37='le')
but leaves the provisional status intact.

## Per-clause pass/fail

1. **C1: NOT MET.** 77's value is still provisional. No red-team or banked
   resolution has occurred (R17-023 confirmed no new evidence; the
   provisional→promoted merge is pending red-team re-evaluation).
2. **C2: INAPPLICABLE.** The trigger (C1) has not fired; per the bar's own
   gating ("once 77's value resolves"), the re-test is not actionable now.
3. **Trigger recorded absent.** Not falsified — the gate is a live re-arm,
   not a dead target.

Adverses answered: (a) 77='le' provisional — confirmed still provisional,
not re-litigated; (b) 62→94 x9 stand re-read as 'il ne' — adopted as the
frame state; the discriminator's two readings and their 77-dependency are
stated per the bar ("record, do not force"). No standing or red-team verdict
contradicted or downgraded; §7 intact; no polyvalence implicated.

## Verdict: NULL

The @508 discriminator re-test cannot fire because its sole trigger —
resolution of 77's value — has not occurred. 77='le' remains provisional;
the red-team merge/overturn decision is still pending. Nothing to re-test
yet; the gate stays armed.

## Follow-ups proposed (for supervisor queuing)

1. `lon-77-le-gate-rerun` (P2): re-fire this exact bar the moment the red
   team adjudicates 77='le' (provisional→promoted merge or overturn to a
   named value). Sole trigger: the red-team 77 ruling. Record dissolution
   of both @508 readings iff 77 resolves non-'le'.
2. `f104-77-merge-input` (P3): package the pending 77='le' provisional→
   promoted merge evidence (F104 76-noun resolution + the strengthened
   77="gouv"-demoted field) as a ruling-ready input for the red-team 77
   docket — the decision that will arm follow-up 1.

## Bookkeeping

- Lock `code/crowd17/next-token/locks/lon-77-le-gate.lock` created on start,
  deleted on completion.
- `battery-queue.json`: `lon-77-le-gate` queued -> verdict/null
  (temp-file + rename; pre-write assert confirmed no prior verdict; JSON
  re-validated; only this entry touched).
- R5005, sealed gate instances, red-team adjudication queue untouched.
- `canonical.py` never used.
