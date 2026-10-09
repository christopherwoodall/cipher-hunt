# Battery report: val-61-646-secondleg-sweep

- Target id: `val-61-646-secondleg-sweep`
- Claim: sweep for a second 61-as-adjective leg stream-wide; if @645 stays sole, fence it as a one-window residual.
- Date: 2026-10-09
- Worker: battery worker (subagent 8316c5ae-7921-40a3-bfa3-e2e3c984f3e9)
- Stream: repaired 1,847-pair / 96-type parse re-derived in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` (asserts held: 1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed gate instances, and the red-team adjudication queue untouched.

Terms (ASD-STE100): "adjective leg" = a window where 61 can read as an adjective with a nominal head, i.e. a "[det] 61 [noun]" or "[noun] 61" frame at battery grade. "One-window residual" = a reading licensed at exactly one window with no repetition leverage, fenced from any broader claim.

## Bar (verbatim, pre-registered before testing)

"second 61-as-adjective leg found with byte evidence, or fence @645 as one-window residual"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** a second 61-as-adjective leg exists — some window other than @645 shows a "[det] 61 [noun]" or "[noun] 61" frame with byte evidence at battery grade → second leg found.
2. **C2:** else-arm — if no second leg is found, fence @645 as a one-window residual with stated cause → fence executed.
3. **Verdict rule:** promote iff C1 passes (second leg named); fence (NULL) iff C2 fires. No kill clause in the bar — a zero result is a fence, not a forced-false.

Adverses: none were listed.

## Method

1. Read BATTERY-PROTOCOL.md in full before testing. Created `code/crowd17/next-token/locks/val-61-646-secondleg-sweep.lock` on start (agent id + 2026-10-09T18:53:00Z); no stale lock present.
2. Re-derived the repaired stream byte-exact per `code/side-keyhunt/repair_parse.py` (1,847 pairs / 96 types asserted in-session).
3. Adopted, never re-litigated: 87='ce' granted; 87 at @644 = determiner (battery-det-87-644-function PROMOTE, function-level, today); 88=verb-class (battery PROMOTE, pending red-team ratification); val-61-premier locus-level PROMOTE at @1556; val-61-contact KILL of any global 61 value (stands); battery-spell-61-anchor-census PROMOTE (@1556 sole complete spelling anchor, today).
4. Swept all 18 windows of 61 for (a) determiner-left-neighbor frames ("[det] 61", dets = {11,47,77,79,87}), (b) noun-class neighbors in the adjective position, (c) postnominal "[noun] 61" frames with granted nouns.

## Window-level evidence (all byte-verified on the repaired stream)

Full 61 census (0-based, ±3 window, L1/R1 with standing values):

| @ | L1 | 61 | R1 | frame check |
|---|----|----|----|---|
| 223 | 89 | 61 | 96(par) | no |
| 279 | 37 | 61 | 20 | no |
| 281 | 20 | 61 | 42 | no |
| 367 | 49 | 61 | 70(pre) | no (fenced: "premier pre fois" ungrammatical) |
| 447 | 62 | 61 | 59(est) | no |
| 577 | 55 | 61 | 94 | no |
| **645** | **87(ce-det)** | 61 | **88(verb-class)** | **determiner left, but NO noun slot** |
| 926 | 17(fois) | 61 | 96(par) | no ("fois premier par" unlicensed) |
| 1168 | 55 | 61 | 94 | no |
| 1206 | 55 | 61 | 21 | no |
| 1219 | 92 | 61 | 24 | no |
| 1256 | 01 | 61 | 31 | no |
| 1281 | 53 | 61 | 56 | no |
| 1429 | 91 | 61 | 12(n-letter) | no |
| 1455 | 62 | 61 | 21 | no |
| 1510 | 12(n-letter) | 61 | 59(est) | no (fenced: clitic-class KILL) |
| 1556 | 93 | 61 | 40(e) | promoted spelling locus, not adjective frame |
| 1810 | 04 | 61 | 15 | no |

Key results:

1. **@645 is the sole determiner-adjacent 61 window.** Determiner census across all 18 windows: "87 61" is exactly 1× stream-wide (@644–645); 11/47/77/79 never neighbor 61 on either side. **C1: no second leg found.**
2. **Even @645 fails the adjective frame.** battery-det-87-644-function (PROMOTE today) names 87="ce" at @644 as a determiner, so the frame is "[ce-det] [61] [88-verb-class]" — the prenominal-adjective slot "[det] [61-adj] [NOUN]" requires a noun after 61, but 88 is verb-class (battery-promoted). The postnominal shape also fails: 87 is a determiner, not a noun.
3. **Postnominal "[noun] 61" sweep:** the only granted/promoted value in 61's left-neighbor set is 17=fois (@926: "17 61 96"). "fois premier par" is an unlicensed frame — a postnominal adjective followed by 96="par" with no governing head.
4. **Follower set of 61** (14 distinct): {12, 15, 20, 21, 24, 31, 40, 42, 56, 59, 70, 88, 94, 96} — no granted-noun follower in any adjective-plausible slot; 65 (noun-class) never follows 61.
5. **Consistency with battery-spell-61-anchor-census (PROMOTE today):** @1556 remains the sole complete spelling-composed 61 window; the adjective reading needs no spelling anchor, but the zero-repetition result (each adjective-shaped adjacency is unique) confirms there is no distributional crib for a second leg.

## Per-clause pass/fail

- **C1 (second leg found): FAIL.** The stream-wide census finds zero windows with a "[det] 61 [noun]" or "[noun] 61" frame beyond @645, and @645 itself fails the noun-slot requirement. No second leg exists at battery grade.
- **C2 (fence arm): FIRES.** @645 is fenced as a one-window residual: it is the sole 61 window with a determiner left neighbor, and even its frame cannot host an adjective reading under standing values. The fence cause: (a) "87 61" is 1× stream-wide — zero repetition leverage; (b) 88's verb-class reading leaves no nominal head for the adjective; (c) 61-as-adjective has no second window anywhere, so no distributional claim can attach to it.

## Verdict: NULL (fence executed)

Per the bar's else-arm and lane precedent (fence executions resolve to NULL, not KILL): no second 61-as-adjective leg exists; @645 is fenced as a one-window residual for the adjective reading. val-61-premier's @1556 locus-level PROMOTE stands unchanged; val-61-contact's global KILL stands; 87="ce" and the det-87-644-function PROMOTE are not contradicted. No standing or red-team verdict downgraded; §7 intact. Canonical-stream caveat stands (row a4_02 offset unvalidated).

Note: this fence covers only the ADJECTIVE reading of 61 at @645. The nominal reading ("[ce-det] [61-N]") and the word-composition reading are separate arms with separate bars — they are not fenced by this battery.

## Scope (stated, not hidden)

- Sweep is window-complete: all 18 windows of 61 inspected at the adjective-frame question, not a sample.
- The fence does not touch 88's class, 61's other arms (spelling at @1556, nominal, clitic), or any standing value.
- No follow-ups are required by the bar beyond the fence, but §4 requires nulls to regenerate work; proposed below.

## Follow-ups proposed (all verified ABSENT from battery-queue.json, 2026-10-09)

1. `nominal-61-645-test` (P4) — test the nominal arm at @645: "[87=ce-det] [61-N]" with 88 as the clause's verb; name-or-fence at battery grade. This is the surviving reading of the @645 residual after the adjective fence.
2. `adj-61-follower-noun-census` (P4) — formalize today's follower census as a standing result: census whether any granted-noun or noun-class group follows 61 in an adjective-hosting slot; if the zero stands, the adjective bar for any 61 window is permanently fence-grade unless a new noun value lands.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-61-646-secondleg-sweep.md` (this file).
- Queue: `val-61-646-secondleg-sweep` queued → verdict/null, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `code/crowd17/next-token/locks/val-61-646-secondleg-sweep.lock`: created on start, deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
