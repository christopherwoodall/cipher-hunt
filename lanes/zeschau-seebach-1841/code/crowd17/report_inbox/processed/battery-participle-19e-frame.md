# Battery verdict: participle-19e-frame

## Bar (verbatim from queue)
"'par'-agent continuation discriminator; gender/number agreement"

## Bar restated as numbered clauses (frozen before testing)
1. **(C1) "par"-agent continuation discriminator:** test whether any "19" window carries a "par"-agent continuation (96 within 4 pairs downstream); a positive hit licenses the passive (past-participle) arm, a confirmed zero leaves the passive arm with zero positive support (agent omission is grammatical, so zero is not kill-grade).
2. **(C2) Gender/number agreement:** test whether the feminine -e on "19e" agrees with the subject of the "ce qui est 19e" frame under each arm (past-participle passive vs predicative adjective).
3. **(C3) Decision rule:** kill one arm iff it fails at kill grade; else fence the residual with stated cause.

## Method
Read BATTERY-PROTOCOL.md first. Created `locks/participle-19e-frame.lock` on start with UTC timestamp; deleted on completion. Re-derived the repaired 1,847-pair / 96-type stream in-session from `code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt` parsed like `repair_parse.py` (asserts held: 1847 pairs, 96 types). `canonical.py` never used. R5005, sealed gate instances, red-team adjudication queue untouched. Offsets 0-based in analysis; 1-based @ in prose.

Standing premises (not re-litigated): 87=ce allophone-tier grant (A4), 64=qui granted, 59=est provisional, 48="e" R17 letter-tier grant; F148 battery-PROMOTE (function-scoped): 48 as feminine/inflectional "-e" in the 32-48 x4 and 19-48 x1 frames; adj-19 battery verdict NULL, folded as a HOLD: 19's adjective class holds one leg only ("est 19[e]" @1778–1780); noun-32e passive frame at @1211 ("65 qui est 32e par") is the battery-supported comparandum for a passive PP in this letter.

## Locus
1-based @1775–1780 (0-based idx 1775–1779), row a8_09: `87 64 59 19 48` = "ce qui est [19]e". Full byte context (0-based 1772–1784): `62 94 24 | 87 64 59 19 48 | 74 65 23 98 83`. "87 64 59 X" occurs exactly once stream-wide (hapax frame).

## Window census: n(19) = 9
0-based idx (1-based @, followers): 90(@91: 41), 121(@122: 58), 211(@212: 74), 328(@329: 00), 485(@486: 64), 584(@585: 18), 965(@966: 24), 1778(@1779: 48), 1821(@1822: 00). Only one "19 48" bigram stream-wide (the locus). No "19 29" (no infinitive ending), no verb-shaped governor at any window.

## C1 — "par"-agent continuation: confirmed zero
Scanned all 9 "19" windows for 96 within 4 pairs downstream: **zero hits**. The passive (past-participle) arm therefore has zero positive support anywhere in the letter. Not kill-grade (a passive without an expressed agent is grammatical: "ce qui est donne"). Contrast noted, not litigated: the letter's one battery-supported passive-PP frame, "65 qui est 32e par" (@1211), carries an explicit "par"-agent continuation; this frame has none and a different subject ("ce qui" vs 65-noun).

## C2 — gender/number agreement: strain on both arms, neither killed
Under standing F148, "19e" is feminine-inflected. The subject "ce qui" is neuter/masculine: predicative participles and adjectives take masculine singular agreement after "ce qui" in 1841 French ("ce qui est donne/arrive", never *"ce qui est donnee"). So:
- **PP arm:** passive "est [19ee]" (feminine past participle) requires a feminine subject; "ce qui" mismatches. Ungrammatical under standard agreement.
- **Adjective arm:** copular "est [19e-fem]" (feminine predicative adjective) requires a feminine subject; "ce qui" mismatches identically.
Both arms carry the same agreement strain; neither is forced false at kill grade (the subject's gender is byte-fixed, but the locus is a hapax with no comparandum, and F148's feminine function is battery-promoted — a battery does not downgrade a standing promote on agreement inference alone). The neutral/masculine reading of "19e" (unaccented -e masculine participle/adjective) remains open for both arms.

## C3 — decision
Neither arm fails at kill grade. The adjective arm retains its battery HOLD (one leg, "est 19[e]" @1778–1780); the PP arm is unsupported (no agent, no verb-frame evidence at any of the 9 windows, agreement strain). Per the bar's else-branch: **fence the residual** — "ce qui est 19e" @1775–1780 stays fenced; class (past participle vs adjective) unresolved at battery grade.

No standing or red-team verdict contradicted (F148 untouched; adj-19's NULL untouched; no polyvalence declared — §7 intact).

## Caveats
- Row a8_09 is one of the 68 unvalidated upstream row offsets: canonical-stream verdict per protocol.
- The agreement strain rests on the 1841 grammatical rule for "ce qui" (masculine/neuter); the fence would re-open if red-team offset adjudication re-segments the locus.
- 59=est is provisional; if 59 resolves non-copular, both arms moot.

## Verdict
**NULL** (fence executed).

## Follow-ups proposed (for supervisor queuing; all verified absent from battery-queue.json)
1. `pp-19e-agent-recall` (P3) — re-scan the 9 "19" windows with a ±8-pair window (allowing row-boundary spillover) for any "96"-agent continuation; calibrates the passive arm with byte evidence.
2. `ce-qui-agreement-census` (P4) — census all predicative frames under "87 64" subject ("ce qui est X" and "ce qui [finite]" shapes) for agreement behavior; tests whether the feminine -e strain at @1778–1780 is a genuine agreement kill or a hapax artifact.
3. `val-19-stem` (P3) — name 19's stem value from its 9 windows (predecessors 98/90/88/01/10/41/59/09; followers 41/58/74/00/64/18/24/48/00); name iff one stem fits all windows with zero kill-grade contradictions — a named stem decides PP vs adjective directly.

## Bookkeeping
- Report: `code/crowd17/report_inbox/battery-participle-19e-frame.md`
- Queue entry `participle-19e-frame`: queued → verdict/null via temp-file + rename (pre-write assert passed — was queued/verdictless; post-write JSON re-validated; own entry only; claim/bars/evidence/adverses preserved)
- Lock created on start, deleted on completion (verified gone)
