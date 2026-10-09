# Battery verdict: noun-88-epicene-rescope

- Target: `noun-88-epicene-rescope` (priority 3, status queued)
- Claim: Re-scope or kill noun-88-epicene if the red team ratifies 'cela', since its gate ('both determiner frames alive') fails at its premise. Gate FIRED: cela ratified at locus level (R19-108 GRANT, R20-135: 69 11="cela" @1115-1116).
- Worker: battery worker (subagent session 540a0f10-4a6f-4fbc-bf6d-450fc95c44bc)
- Date: 2026-10-09
- Stream: repaired 1,847-pair / 96-type parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, repair_parse.py tokenization). 1,847 pairs / 96 types re-verified in-session. canonical.py never used. R5005 untouched. Sealed gates untouched. Red-team adjudication queue untouched. No invented numbers.

## 1. Bar (verbatim from battery-queue.json)

"on cela ratification: noun-88-epicene's two-window epicene bar is doubly moot (its gate dies with @1117's frame); decide rescope-to-single-window vs kill, without inventing values"

Numbered clauses:
- C1: On cela ratification, assess whether noun-88-epicene's two-window epicene bar survives (its gate was 'both determiner frames alive').
- C2: Decide rescope-to-single-window vs kill, without inventing values.

## 2. Method

Byte-exact re-derivation of the two gated windows on the repaired stream; adoption (not re-litigation) of the standing dispositions: R19-108 GRANT / R20-135 (69 11="cela" @1115-1116), cela-1117-frame-resume PROMOTE (88's determiner window set shrinks to {@402}), ce88-leftedge-402 PROMOTE (45 is demonstrative pronoun at @401; the "ce [88-noun]" determiner frame falls at @402), subj-88-730 PROMOTE (finite-88 licensed at @402). Full 23-window predecessor census of 88 for any surviving determiner frame.

## 3. Findings

**C1 — the gate is dead, and doubly so.**

(a) @1117's "la [88]" frame is dead as the gate-firing premise states. Byte-exact @1115-1117: `69 11 88` = "cela"(R19-108/R20-135) + gov. The "la" at @1116 is word-internal to "cela"; no free "la" precedes 88. Confirmed in-session.

(b) The rescope candidate @402's determiner frame is ALSO dead — this goes beyond the bar's parenthetical. Byte-exact @400-402: `11 45 88` = "la"(GT) + "ce/dict"(45, LEAD) + gov. Adopted: ce88-leftedge-402 PROMOTE decided that 45 is a demonstrative pronoun at @401, so the "ce [88-noun]" determiner frame FALLS at @402. Independently, subj-88-730 PROMOTE licenses finite-88 at @402 ('ce [88]' with overt subject) — the window's live arm is verbal, not nominal.

(c) No third determiner frame exists. Full 88 predecessor census (n=23): 39(a/à)×2, 69(noun)×2, 24(verb), 06(ent), 50(?), 89(noun), 02(?), 54(?), 45(ce/dict), 79(tout), 65(noun), 70(pre), 29(er), 61(?), 48(e), 16(?), 41(?), 11(la), 81(?), 93(verb), 94(ne). The only determiner-class predecessors are 11 (@1117, dead per (a)), 45 (@402, dead per (b)), and 79='tout' (@497) — which the standing cela-1117-frame-resume computation already excluded from 88's determiner window set (it shrank the set to {@402}, now empty). No re-litigation; the set computation stands.

**C2 — KILL, not rescope.**

Rescope-to-single-window requires a surviving determiner frame at @402. There is none: the frame fell at battery grade (ce88-leftedge-402), and the window's live arm is finite-verb (subj-88-730). The noun-88-epicene bar ("name a period-attested (1841) consonant-initial epicene noun parsing both @402 and @1117 with distributional support beyond these two windows") cannot be met even in principle — both frames are dead, so no value, invented or otherwise, can parse them. This is a frame-level kill, not a value-naming failure. The target's gate ('both determiner frames alive') fails at both premises.

## 4. Verdict: KILL

Per-clause: C1 PASS (gate doubly dead, verified byte-exact) / C2 KILL (rescope impossible — no surviving determiner frame for 88 anywhere in the 23-window profile; the epicene-noun test has no frame to run in).

No follow-ups required (kill, not null). The 88-determiner question is closed stream-wide at battery grade: zero live determiner frames for 88.

## 5. Scope

Kills only the noun-88-epicene target's viability (recommendation: the supervisor may mark noun-88-epicene's queue entry accordingly — this battery does not edit it, per adverses). Untouched: R19-108/R20-135 cela, ce88-leftedge-402, cela-1117-frame-resume, subj-88-730 finite-88, tout-88-frame, 88's governor class (registry cls), 88's finite-subject legs (@402/@1260). No standing or red-team verdict contradicted, downgraded, or re-litigated. §7 intact — no polyvalence declared (the sole-polyvalence rule for 67 is unaffected). No values invented. Canonical-stream caveat stands (row a6_06/a6_07 and a2_07/a2_08 offsets unvalidated).

## 6. Bookkeeping

- Report: code/crowd17/report_inbox/battery-noun-88-epicene-rescope.md
- Queue: `noun-88-epicene-rescope` queued → `verdict`/`kill`, 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.noun-88-epicene-rescope.tmp` + atomic rename; JSON re-validated from disk; own entry only; no downgrade)
- Lock `code/crowd17/next-token/locks/noun-88-epicene-rescope.lock`: created on start (2026-10-09T19:42:43Z, no stale lock), deleted on completion (verified gone)
- R5005, sealed gates, red-team adjudication queue untouched
