# Battery `noun-89-status` — verdict: PROMOTE (audit grade)

- Target id: `noun-89-status`
- Claim: "audit noun-89 standing legs independently of this tail; the bar kill arm needs a residual demonstrated against a NAMED 16, which this audit supplies once 16 resolves"
- Evidence: `battery-tail-89-16.md` NULL 2026-10-09, follow-up 3
- Date: 2026-10-09
- Worker: subagent 5acc9260-1cc9-4a44-ac04-d2dbab6778ff
- Stream: repaired 1,847-pair / 96-type parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parsed like code/side-keyhunt/repair_parse.py; n=1847 asserted, 96 types asserted). All @-offsets 0-based repaired-stream indices. `canonical.py` never used. R5005 not touched.
- Lock: code/crowd17/next-token/locks/noun-89-status.lock (created 2026-10-09T19:25:00Z, deleted on completion; no prior lock existed).

## Bar (verbatim, pre-registered before testing)

"state the leg inventory with counts and the kill-arm status"

Numbered pass/fail clauses (restated before testing, not modified after):

1. (C1) The leg inventory for noun-89 is stated with per-leg counts, all windows byte-verified in-session on the repaired stream.
2. (C2) The kill-arm status is stated: which kill arm exists, its trigger condition, and whether it has fired.

No adverses listed on this target.

## Method

1. Re-derived the repaired parse in-session; asserted 1,847 pairs / 96 types. Never used canonical.py. R5005 not touched.
2. Census: n(89) = 14, 0-based indices [113, 222, 275, 285, 303, 640, 781, 871, 986, 1082, 1377, 1393, 1498, 1752]. All 14 windows rendered ±2 with standing values in-session.
3. Read the standing record: R19-161 (red-team, ratified), battery-noun26-89-class PROMOTE (finding grade, 2026-10-09), battery-poly-89-redteam-package PROMOTE (packaging grade, 2026-10-09), battery-tail-89-16 NULL (2026-10-09), battery-frame-82-16 NULL (2026-10-09), R20 references (R20-047, R20-787). Registry: 89=["noun","lead"].
4. Checked 16's status: n(16)=28, class open; frame-82-16 verdict NULL — 16 NOT named.

## Findings

### Leg inventory (n(89)=14, all windows byte-verified)

**Standing: 89=noun LEAD (R19-161, ratified; infinitive rival KILLED as uniform class; positional split REJECTED under §7).**

Noun-arm legs:
1. @640 — "77 89" = "le [89]e", determiner + noun with -e ending. Noun FORCED (an infinitive after an article is ungrammatical in 1841 French). Load-bearing condition: provisional 77='le'.
2. @871 — "87 77 89 48 20" = "ce le [89] e [20]". Same shape, noun forced, same 77='le' condition.
3. @1752 — "28 [89] 26 24" = "[28] [89] [26] [24-modal]". 89 as subject of the finite modal. Conditional noun leg #3 (noun26-residual-adjud NULL context; the @1753 residual "89 26 24" parses under noun-89).
4. @113, @275, @781, @1377, @1393 — the "[X]er 89" family. Parse under noun OR governed-infinitive OR word-internal; fenced as sub-question (battery-er89-wordinternal-govern venue). Not noun-forcing, not noun-killing.
5. @285 ("52 [89] 28"), @303 ("18 [89] 88"), @1082 ("52 [89] 24") — arm-neutral open windows; 52/28/18/88 class-open, no forcing evidence.

Infinitive-arm legs (battery-grade, fenced split arm — NOT ratified; red-team venue):
6. @222 — "24 89" = "[24-modal] [89]". Modal + infinitive; a noun as direct object of a modal is ungrammatical. Load-bearing: 24=modal (24's value open; modal reading is standing grant, conditional).
7. @986 — "24 89" = "[24-modal] [89] e". Same, with word-internal 89-48 = "[89]e" (-re-shaped infinitive).
8. @1498 — "24 89" = "[24-modal] [89]". Same.

### Kill-arm status: PENDING (trigger unresolved)

The designated kill arm is the @1391 "[89] [16]" tail (battery-tail-89-16): IF 16's class is ever named such that the tail cannot parse under noun-89, the residual kills the noun-89 LEAD. Current status:
- battery-frame-82-16 verdict NULL (2026-10-09) — 16 unnamed, class open (n(16)=28; predecessors 82×11, 62×4, 12×3, 33×2, 42×2; heterogeneous successors, no forcing frame).
- Trigger UNRESOLVED → kill arm UNFIRED.

### Tensions recorded (red-team jurisdiction, NOT kill arms)

- R19-161's §7 split-rejection ("no kill-grade byte evidence for two classes") vs battery-noun26-89-class's fenced conditioned split (noun at '77 89' ×2, infinitive at '24 89' ×3). R19-161's kill targeted the *uniform* infinitive rival; the conditioned arm was named "conditional tension" then and re-evidenced since. Resolution is red-team venue (poly-89-redteam-package is ruling-ready).
- The noun arm's load-bearing condition (provisional 77='le') and the infinitive arm's load-bearing condition (24=modal, value open) are both stated, not hidden.

## Per-clause pass/fail

1. **C1 PASS** — full 14-window inventory stated with counts, all windows byte-verified in-session.
2. **C2 PASS** — kill arm stated: the @1391 "[89] [16]" tail, trigger = 16's class named; status = PENDING (frame-82-16 NULL).

## Verdict: PROMOTE (audit grade)

The inventory is complete and the kill-arm status is stated. This audit does not name a value, does not declare a split, and does not touch §7. No standing or red-team verdict contradicted, downgraded, or re-litigated. Canonical-stream caveat stands.

## Recommended next step (not queued by this worker)

Once any battery names 16's class, re-run the @1391 tail test (battery-tail-89-16's C2) — that is the live kill-arm trigger for noun-89.

## Bookkeeping

- Report: code/crowd17/report_inbox/battery-noun-89-status.md
- Queue: `noun-89-status` → `status: verdict`, `result: promote`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.noun-89-status.tmp` + rename per the 2026-10-09 tmp-name rule; JSON re-validated from disk; own entry only; no downgrade)
- Lock created on start (2026-10-09T19:25:00Z, no stale lock), deleted on completion (verified gone). R5005, sealed gates, red-team adjudication queue untouched.
