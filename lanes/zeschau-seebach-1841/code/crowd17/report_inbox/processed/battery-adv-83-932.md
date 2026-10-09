# Battery report: adv-83-932

- Target id: `adv-83-932`
- Claim: test 83 as clause-adverb at @932 once 98's value is named (gated on val-98-subject). Bar: adverb parse of "98 [83] [56-fin]" with ≤1 ungranted assumption, or fence the adverb arm.
- Date: 2026-10-09
- Worker: battery worker (subagent a086a596-b361-4d20-9889-805cf5062d64)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; asserts held: 1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed gate instances, red-team adjudication queue untouched.

Terms (ASD-STE100): "GT" = banked ground truth (pencil). "kill grade" = evidence strong enough to close a reading. "ungranted assumption" = a premise not in pencil GT, promoted/granted standing, or a red-team verdict.

## Bar (verbatim from battery-queue.json, pre-registered before testing)

"Bar: test 83 as clause-adverb at @932 once 98's value is named (gated on val-98-subject). Bar: adverb parse of "98 [83] [56-fin]" with ≤1 ungranted assumption, or fence the adverb arm. [GATED — do not dispatch until gate fires]"

Gate check (supervisor-verified, re-confirmed in-session): `val-98-subject` → verdict/promote 2026-10-09 — 98's class named finite clause-head verb (two independent banked-GT legs: "qui 98" x2, "m' 98" x2). Gate fired; proceed.

Numbered pass/fail clauses (fixed before testing, not modified after):

1. **C1:** an adverb parse of "98 [83] [56-fin]" at @932 is stated with ≤1 ungranted assumption. Pass iff a complete grammatical structure exists with 83 in clause-adverb role and at most one premise outside standing values.
2. **C2 (else-arm):** fence the adverb arm with stated cause.

Resolve-arm: C1 passes → verdict promote. Else-arm: C2 fires → verdict null (fence executed).

Adverses listed in queue entry: none.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/adv-83-932.lock` (agent id + 2026-10-09T21:16:00Z) on start. No fresh lock was present. Deleted on completion.
2. Re-derived the repaired stream byte-exact in-session. All @-offsets below are 0-based. The claim's "@932" is 1-based for the 83 pair = 0-based @931.
3. Sibling reports read first and adopted, not re-litigated: val-98-subject PROMOTE (98 = finite clause-head verb, class-level); de83-932-gate NULL (83≠'de' at @932 at kill grade; 83's value fenced; this target is its follow-up 2); form-56-1627 PROMOTE (56 = 3sg finite, "crée"-shaped, at @932/@1626 — adopted as the bar's [56-fin] stipulation).
4. Standing premises used, not re-litigated: pencil GT (82='m', 96='par', 00='pour'); registry 98=['verb','cls'], 69=['noun','cls'], 48=['e','prom'], 26=['noun','lead']; 86=INF-class (R15-A9, R20-087); §7 (67 et/veut sole true polyvalence). Canonicality caveat stands (row a5_10 offset unvalidated).

## Window-level evidence

**Locus byte-confirmed** (0-based, row a5_10):
`@926=61 @927=96 @928=48 @929=82 @930=98 @931=83 @932=56 @933=69 @934=26 @935=00(pour) @936=33`
= "…[61] par [48='e'] m' [98-fin] [83] [56-fin] [69-noun] [26] pour [33]…"

**83 census** (n=15, byte-exact, matches de83-932-gate): @228, 614, 898, 907, 911, 931, 1061, 1161, 1171, 1217, 1334, 1612, 1784, 1829, 1840. The "98 83" predecessor block is x5: @228, @898, @931, @1061, @1784.

### C1: adverb parse at @931 — FAILS (minimum 2 ungranted assumptions)

The frame is Vfin X Vfin: 98 finite (val-98-subject), 56 3sg finite at @932 (form-56-1627, also the bar's stipulation). Two adjacent finite verbs need a clause boundary; every placement was tested:

- **P1: "[98] [83-adv] ‖ [56-fin]…"** (83 modifies 98). Then 56's clause = "[56-fin] [69-noun] [26] pour…" — subjectless. Rescue via postposed subject 69 needs 26 as the direct object (26's role at @934 is open; noun is LEAD only → ungranted #1) and 98's own clause needs a subject: 48 is promoted 'e' (letter tier, cannot serve as subject), "par e" is unparseable, so the subject must come from 61 (@926, unvalued) or earlier → ungranted #2. Total ≥2.
- **P2: "[98] ‖ [83-adv] [56-fin]…"** (83 fronted adverbial in 56's clause: "…‖ souvent crée [69-subj] [26-obj]…"). Grammatical shape (VSO with fronted adverbial is licensed literary French), but needs 26's nominal-object role (ungranted #1) and 98's subject (ungranted #2, same left-edge problem as P1). Total ≥2.
- **P3:** postposed subject 69 without the fronted-adverbial licenser — ungrammatical for a transitive "crée"-shaped verb. Dead.
- **P4:** coordination/subordination of the two finite verbs — no conjunction or subordinator present. Dead.
- **P5:** 56 non-finite — contradicts adopted form-56-1627 PROMOTE and the bar's stipulation. Out of scope (re-litigation, not tested).

No placement reaches a complete parse within the ≤1-assumption budget. The binding constraints are 98's missing subject (48='e' promoted; "par e" unparseable; 61 unvalued) and 26's open role — both outside standing values.

### Supporting distributional result: zero adverb-viable "98 83" windows stream-wide

The other four "98 83" windows break the adverb reading on independent, 83-value-independent grounds:
- @228, @1061, @1784: "98 83 82 96" = "…vient [83] me par…" — 82='m' (pencil GT) stranded before 96='par' (preposition); the clitic has no verb host. Broken regardless of 83.
- @898: "98 83 86" with 86=INF-class — an adverb cannot license the following infinitive. Broken.
- @931: the two-finite-verb geometry above.

The adverb arm has no positive leg at any of its 5 host windows.

### Why this is a fence, not a kill

The failure is assumption-budget, not grammatical impossibility: P2's shape ("‖ [adv] [56] [69-subj] [26-obj]") is grammatical French. If 61 (or another left neighbor) names as subject-capable AND 26's nominal role firms up, the adverb arm re-opens. No window forces every adverb reading false. Per the bar's else-arm, the adverb arm is fenced (evidentiary, re-openable), not killed.

## Per-clause verdict

- **C1: FAIL** — no adverb parse of "98 [83] [56-fin]" at @932 statable within ≤1 ungranted assumption (minimum 2: 98's subject, 26's role; left edge "par e" independently unparseable under standing values).
- **C2: FIRES** — adverb arm fenced with stated cause above.

## Verdict: NULL (fence executed)

Scope: fences only the clause-adverb arm for 83 at @932 (with the stream-wide zero-positive-legs note as supporting evidence). Untouched: 83's global value/class (still open), val-98-subject PROMOTE, form-56-1627 PROMOTE, de83-932-gate's 'de'-kill, 48='e', 26's noun-LEAD, 69's noun class, §7. No standing or red-team verdict contradicted, downgraded, or re-litigated. Canonical-stream caveat stands (row a5_10 offset unvalidated).

## Follow-ups proposed (all verified ABSENT from battery-queue.json)

1. `subj-98-930` (P4) — name 98's subject at @930. The "par e me" left edge must resolve (nearest candidate: 61 at @926) before any 83-class parse at @931 can firm up; a named subject removes C1's assumption #2.
2. `val-26-934-role` (P4) — name 26's class/role at @934. A nominal 26 as 56's direct object completes the P2 VSO parse ("‖ [adv] [56] [69-subj] [26-obj]"); removes C1's assumption #1.
3. `adv-83-932-rearm` (P4, gated) — re-run this bar once 98's subject is named AND 26's role resolves; fires only if both name compatibly (subject left of 98, nominal 26).

## Bookkeeping

- Pre-write assert passed on start: `adv-83-932` was queued/verdictless; no fresh lock present.
- Queue: `adv-83-932` → `status: verdict`, `verdict: {result: null, report: code/crowd17/report_inbox/battery-adv-83-932.md, date: 2026-10-09}` — written through target-id-unique temp file `battery-queue.json.adv-83-932.tmp` + atomic rename; no tmp leftover; disk re-validated after write; own entry only; no downgrade (was queued, no prior verdict).
- Lock `code/crowd17/next-token/locks/adv-83-932.lock` created on start (agent a086a596-b361-4d20-9889-805cf5062d64, 2026-10-09T21:16:00Z), deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
