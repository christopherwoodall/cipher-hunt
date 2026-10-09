# Battery report: nom-83-1217 — 83 as nominal at the fenced @1217 window

- Target id: `nom-83-1217`
- Claim: test 83 as nominal at the fenced @1217 window ("36 77 83" = "...le [83-noun] [92-verb]...")
- Date: 2026-10-09
- Worker: battery worker (subagent 1b908a5b-4b4d-4708-8d0e-9a72960cedc7)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`). Re-derived in-session: 1,847 pairs, 96 types. `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
- Parent: battery-de83-932-gate (null, 2026-10-09), follow-up 3.

Terms (ASD-STE100): "nominal" = noun-shaped. "fence" = the localized 83-blocker from battery-le83-window / battery-fence-83-1217. "kill grade" = evidence strong enough to close a reading. "granted" = a standing promoted / red-team-ratified / provisional value or class.

## Bar (verbatim, pre-registered before testing)

"Bar: test 83 as nominal at the fenced @1217 window ("36 77 83" = "...le [83-noun] [92-verb]..."). Bar: nominal-83 parses with zero ungranted assumptions, or the le83-window fence is confirmed as terminal."

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** nominal-83 parses at @1217 with zero ungranted assumptions (standing, promoted, provisional, and granted values/classes only, plus the claim itself).
2. **C2:** the le83-window fence is confirmed as terminal (83 remains the blocker at @1217 with no remaining battery-grade resolution path).

Adverses listed: none.

## Method

1. Read BATTERY-PROTOCOL.md first. Checked `code/crowd17/next-token/locks/nom-83-1217.lock` — absent. Created it on start with agent id + UTC timestamp; deleted on completion.
2. Re-derived the repaired stream in-session. All @-offsets below are 0-based.
3. Adopted as premises (not re-litigated): 36=NOUN class (R18-027 GRANT PROMOTE, class tier; battery-class-36-profile promote); 92=verb subset-scoped promote (verbal-governor subset {00, 94, 84, 46} only — battery-class-92); 92=noun killed globally (prenne-92-noun kill); 92='-ère' killed; 92='ver' dead; 77='le' provisional (§7); 96='par', 45='ce' (HOLD A11); 83='de' kill-grade excluded (fence-911-de owns unconditioned; battery-de83-932-gate excluded at @932); 83=infinitive killed (inf-83-fork); fence-83-1217 and fence-92-1218 nulls (83 designated blocker; both adjacencies hapax).
4. Surveyed every 92-class at @1218 under the nominal-83 hypothesis. Tested the claim's own frame "...le [83-noun] [92-verb]..." against the full window.

## Window-level evidence

**Window byte-confirmed**, row a7_00/a7_01:
`[1213]96 [1214]45 [1215]36 [1216]77 [1217]83 [1218]92 [1219]61 [1220]24 [1221]48`
= "par ce [36-NOUN] le [83] [92] [61] [24] [48]..."

Contact facts (re-derived): 77-83 bigram unique stream-wide (x1). 36-77 bigram unique (x1). 83-92 hapax (83's followers: 92 x1 of 15). 92-61 hapax (61's predecessors: 92 x1 of 18). 61 unnamed. @1220=24 is finite-modal verb class (per battery-fence-92-1218).

**Left edge parses clean.** "par ce [36-NOUN]" is grammatical with zero new assumptions (96='par' promoted, 45='ce' HOLD, 36=NOUN granted). The R18 grant is new since battery-fence-83-1217 — it fixes the left edge but does not touch the blocker.

**C1 test — "le [83-noun] [92-verb]": FAILS.** Under nominal-83, "le 83" is a subject NP. It needs 92 as its finite verb. Every 92-class at @1218 is closed:

- 92=verb: the promote is scoped to verbal governors {00, 94, 84, 46}. @1218's governor is 83 — outside the subset (battery-fence-92-1218, coordinated). Extending the subset is an ungranted assumption.
- 92=verb as infinitive governed by 83: needs 83='de'-shaped. That contradicts nominal-83, and 83='de' is kill-grade excluded anyway.
- 92=noun: killed globally (prenne-92-noun kill).
- 92=adjective (postnominal "le NOUN ADJ"): no lead exists anywhere in the lane; 83-92 and 92-61 are both hapax with no parallel. Ungranted.
- Clause boundary after 83 ("le NOUN. [92]..."): fenced (battery-fence-92-1218 Attempt 3 — 92 verb-shaped gives two finite verbs; 92 noun-shaped killed; else unanchored).
- Word-internal 83-92: fenced as speculation (Attempt 4).
- 77='le' as object pronoun ("...le [83-verb]"): contradicts the nominal claim.

**Secondary kill-grade point.** @1220=24 is finite-modal class. Even arguendo 92=verb, "Le [83-noun] [92-verb] [61] [24-fin]" puts two finite verbs in one clause. It needs 61 to subordinate (e.g. 61='que'). 61 is unnamed — ungranted. The claim's own frame is ungrammatical in context.

**C2 test — fence terminal: CONFIRMED.** The re-test with the new grants (36=NOUN R18, class-36-profile promote) still leaves 83 as the blocker. Status of every 83 value-class at @1217: 'de' kill-grade excluded, infinitive killed, nominal killed here (this battery). 77='le' is not downgraded — the failure is fully absorbed by 83's cell, per the fence's pre-commit. No battery-grade path remains that names 83's value at this window.

## Per-clause verdict

- **C1: FAIL at kill grade** — the @1217 window forces nominal-83 false: under the claim, 92 has no grantable class at @1218 (verb scoped-out, noun killed, all rescues fenced or ungranted), and the claim's own frame is ungrammatical in context (@1220=24 finite).
- **C2: PASS** — the le83-window fence is confirmed as terminal: 83 remains the blocker with stated cause; 'de', infinitive, and nominal arms are all closed; 77 not downgraded.

## Verdict: KILL

Nominal-83 at @1217 is dead at kill grade. The le83-window fence stands terminal at battery grade: 83 is the blocker at @1217, 77='le' not downgraded, and no remaining battery-grade path names 83's value at this window. No standing or red-team verdict is contradicted: this confirms (does not overwrite) the battery-le83-window, battery-fence-83-1217, and battery-fence-92-1218 nulls; adopts the class-36-profile promote, verb-92-subset promote (scope respected), prenne-92-noun kill, fence-911-de kill-grade, inf-83-fork kill, and de83-932-gate exclusion as premises. §7 intact — no polyvalence declared. Canonical-stream caveat stands (row a7_00 offset unvalidated).

## Follow-ups

None. A kill with the fence confirmed terminal regenerates no work: the nominal arm is closed, and the fence's terminal status means no further battery can unblock 83 at @1217. (The 'de' question stays with de-83-sweep's null; the 83='de' kill-grade stays with fence-911-de.)

## Bookkeeping

- Queue: `nom-83-1217` → `status: verdict`, `result: kill`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `locks/nom-83-1217.lock` created on start, deleted on completion (verified gone).
- R5005, sealed gates, red-team adjudication queue untouched.
