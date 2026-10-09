# Battery report: 80-inf-transfer-1322 — test the adopted @768 "vient [80]" infinitive transfer to the three "03 29 80" windows

- Worker: battery worker 80-inf-transfer-1322 (subagent 1f8f3856-8f13-4c22-95c9-eb28500f0452), 2026-10-09.
- Lock: `locks/80-inf-transfer-1322.lock` supervisor-created, fresh (14:20 UTC, inside 90 min); kept during the run; deleted on completion (verified below).
- Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`), re-derived in-session per `code/side-keyhunt/repair_parse.py`; asserts held (1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed gate instances, and the red-team adjudication queue untouched. Every number traces to the stream. All @-offsets 0-based.
- Provenance: follow-up #2 of `80-value-host-w2` NULL (2026-10-09). Route 4 kill at @1322 is the adopted starting point. Adopted `frame66-vient-80` PROMOTE: at @768, "…[88-inf] [66-subj] vient(98) [80-inf]…" — 80 is a GOVERNED infinitive under the finite semi-auxiliary 98='vient'. That promote is @768-scoped only ("not a global class claim").

Terms (ASD-STE100): "infinitive-shaped" = the cipher number fills a governed-infinitive slot. "Ungranted assumption" = a value, boundary, or construction with no standing grant (§7 or adopted battery finding). "Battery grade" = the evidence standard of this pipeline.

## Bar (verbatim, pre-registered before testing)

"one uniform infinitive parse with <=1 ungranted assumption across all three, or documented per-window ungrammaticality; battery gathers only (§7), feeding the 80-class red-team adjudication"

## Bar restated as numbered clauses (fixed before testing, not modified after)

- **C1:** one uniform infinitive parse of 80 (the role adopted at @768: 80 as infinitive) holds across all three "03 29 80" windows (@1032/@1322/@1596) with <=1 ungranted assumption in total.
- **C2:** if C1 fails, per-window ungrammaticality is documented — each of the three windows fences the infinitive reading on stated grammatical grounds at battery grade.

Adverses: none listed.

Standing premises adopted (§7; not re-litigated): 29='er' pencil GT; 03 = verb-stem class (R19), value OPEN; 80 = A8 verb-frame, value OPEN; 98='vient' finite semi-auxiliary; 77='le' provisional; 87='ce' promoted; 24 = finite/modal per R24; 08 = letter-tier, word-internal (adopted `stem-08-letter-probe`); 81="prin" killed (81's value open); 67 et/veut sole polyvalence. Adopted battery findings: Route 4 kill at @1322 (`80-value-host-w2`); `frame66-vient-80` PROMOTE (@768 only).

## Method

1. Read BATTERY-PROTOCOL.md in full first. Kept the supervisor-created lock; deleted it on completion.
2. Re-derived the repaired stream byte-exact in-session; asserts held (1,847 pairs, 96 types).
3. Byte-exact census: the "03 29 80" trigram occurs exactly 3x stream-wide, at @1030/@1320/@1594 — i.e. 80 at **@1032**, **@1322**, **@1596**. Zero other occurrences.
4. Dumped ±8 windows at each locus with row ids; tested the infinitive reading of 80 per window under standing grants, counting ungranted assumptions.

## Window-level evidence (byte-exact)

Structural fact common to all three: "03 29" = [03 verb-stem (R19)] + [29='er' banked GT] = a bare infinitive "[stem]-er". The adopted @768 parse has 80 as an infinitive GOVERNED BY a finite verb (98='vient', "il vient manger" construction). In all three "03 29 80" windows, 80 instead follows a bare infinitive with no finite governor in the window — the structural inverse of @768.

### W1 — @1032 (row a6_03; canonicality caveat: row offsets unvalidated)

`@1028–@1036: 87 01 03 29 80 77` = "[87='ce' promoted] [01 open] [03-stem]er [80] [77='le' provisional]".

- 80 as infinitive → "[03-er][80-inf]": two bare infinitives in sequence, ungrammatical. No standing governor: 87='ce' cannot govern a bare infinitive; 01's value is open (any 01-value hypothesis is ungranted).
- The follower blocks the rescue: 77='le' (provisional grant) is an enclitic pronoun and cannot attach to an infinitive. Rejecting the provisional 77='le' would be a second ungranted move.
- Best rescuing route: 03 = causative "faire"/"laisser"-class (1 ungranted assumption) → "[faire] [80-inf]" is grammatical. But the 77-enclitic problem persists ("faire [80-inf] le" ungrammatical) and needs a second ungranted move. The <=1 budget is exceeded.
- Result: infinitive reading ungrammatical at battery grade.

### W2 — @1322 (row a7_04; canonicality caveat: row offsets unvalidated)

`@1319–@1324: 24 03 29 80 08` = "[24 finite/modal per R24] [03-stem]er [80] [08 letter-tier]".

- Adopted Route 4 kill (`80-value-host-w2`): 24 governs [03]er; 80 as infinitive follows the bare infinitive bare — "[inf][inf]" adjacency, ungrammatical. Re-verified byte-exact; no change.
- The follower blocks the rescue: 08 is letter-tier, word-internal (adopted `stem-08-letter-probe`) — an infinitive is a complete word and cannot sit word-internal with 08; licensing the 80|08 boundary is a second ungranted move against an adopted finding.
- Causative-03 rescue (1 ungranted): still exceeds the budget on the 08-boundary problem.
- Result: infinitive reading ungrammatical at battery grade.

### W3 — @1596 (row a8_02; canonicality caveat: row offsets unvalidated)

`@1593–@1598: 81 03 29 80 67` = "[81 open] [03-stem]er [80] [67 et/veut polyvalence] 77…".

- 80 as infinitive → "[03-er][80-inf]": the same bare "[inf][inf]" adjacency. No standing governor: 81's value is open (81="prin" killed, no replacement named); 67='et' sits AFTER 80 and does not govern backward.
- Causative-03 rescue (1 ungranted): completing the "et"-coordination ("faire [80] et …77…") needs 81 named finite — a second ungranted move. The <=1 budget is exceeded.
- Result: infinitive reading ungrammatical at battery grade.

Uniformity check: the only uniform parse candidate is 03 = causative "faire"/"laisser"-class governing [80-inf] (the same 03 value stream-wide at all three loci). It exceeds the <=1-ungranted budget at EVERY window on independent follower grounds (77-enclitic @1032; 08 word-internal @1322; 81-naming @1596). No other uniform parse exists under standing grants.

## Per-clause pass/fail

- **C1 — FAIL (kill grade).** No uniform infinitive parse exists within the <=1-ungranted budget. Each window independently forces the transfer false: @1032 (no governor + enclitic follower), @1322 (adopted Route 4: 24-governed [03]er leaves 80 bare + letter-tier follower), @1596 (no governor + coordination needs 81 named). The best rescuing route needs >=2 ungranted moves at each window.
- **C2 — PASS.** Per-window ungrammaticality documented above for all three windows with byte-exact loci, row ids, and stated grammatical cause.

Scope fence (§5.2): this KILL is scoped to the TRANSFER at the three "03 29 80" windows only. It does not touch, contradict, or downgrade `frame66-vient-80` PROMOTE: that verdict is @768-scoped, and at @768 the finite governor 98='vient' is present — exactly the structural element these three windows lack. No standing or red-team verdict is contradicted or downgraded. 80's value is not named at battery grade (§7 battery-gathers-only); the per-window fences feed the 80-class red-team adjudication (the `poly-80-docket` venue, untouched).

## Verdict: kill

The uniform-transfer claim is forced false at battery grade at all three windows (§4 kill: a window forces the claim false — here each of the three does so independently). No follow-ups are licensed by a kill verdict per §4; the gathered per-window fences feed the red-team adjudication.

## Bookkeeping

- Lock `locks/80-inf-transfer-1322.lock` (supervisor-created, fresh) kept during the run, deleted on completion (verified below).
- Queue: `80-inf-transfer-1322` → status `verdict`, result `kill`, 2026-10-09 (pre-write assert: was `queued`/verdictless; temp-file + rename; JSON re-validated from disk; own entry only; no downgrade).
- R5005, sealed gate instances, red-team adjudication queue untouched.
