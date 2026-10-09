# Battery report: prenne-92-noun — 92 as feminine noun (value arm)

- Target: `prenne-92-noun` (claim: "92 is a feminine noun (value lead for the @1545 direct-object slot)")
- Worker: 27fc242b-5bf9-4283-9632-13f73fad35b3
- Date: 2026-10-08
- Stream: repaired 1,847-pair parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed exactly like `code/side-keyhunt/repair_parse.py`). `canonical.py` NOT used. R5005 NOT touched.
- Lock: `code/crowd17/next-token/locks/prenne-92-noun.lock` (created 2026-10-08T23:55:52Z; no prior lock)

## Bar (verbatim, pre-registered before testing)

"name 92's value iff one class covers >=80% of its 22 windows; if 92 = noun, @1545 reads 'pour que [S] prenne 92' (V + direct object, S still open — narrows the search)"

Numbered clauses:

- **C1**: one class (feminine noun) covers ≥80% of 92's 22 windows (≥18 windows) with a grammatical feminine-noun parse under standing values.
- **C2** (conditional): if C1 holds and 92 is named a noun, @1545 reads 'pour que [S] prenne 92' (V + direct object, S still open).

Standing values used: 11=la (pencil), 00=pour (A9 class-level), 84=on (A15, unconditioned per collision battery 2026-10-08), 94=ne (battery-promoted, pending ratification), 30=pas (battery-promoted, pending ratification), 64=qui (pencil), 46=que (pencil), 29=er (pencil), 79=tout (A5), 47=ce (A4 allophone tier), 67=et/veut (sole polyvalence, §7). Open: 16, 81, 13, 31, 83, 98, 62, 07, 69, 60, 65.

## Method

Re-derived all 22 windows of 92 on the repaired stream (independent re-read, not copied from class-92). For each window, tested whether a whole-word feminine-noun parse of 92 is grammatical under standing values. Windows depending on open values are fenced (not counted as passes — no evidence invented). The class-92, verb-92-subset, and split-92-adjudication bars were not duplicated; this battery tests the NOUN arm only. No polyvalence declared (§7).

22 windows re-derived: @49, @66, @203, @321, @330, @354, @356, @593, @683, @901, @978, @1022, @1154, @1218, @1310, @1361, @1379, @1453, @1490, @1550, @1607, @1673.

## Window-level evidence (@-offsets)

### PASS under feminine noun (6)

- @203: `87 11 92 63 42` = "ce la [N] [63]" — "la [N]" clean article+noun.
- @321: `06 11 92 60 15` = "[06] la [N] [60]" — "la [N]" clean.
- @1607: `39 11 92 65 23` = "a la [N] [65] [23]" — "la [N]" clean.
- @330: `19 00 92 50 45` = "[19] pour [N] [50] ce" — "pour [N]" grammatical (preposition + noun).
- @978: `01 00 92 07 76` = "[01] pour [N] [07] [76]" — "pour [N]" grammatical (followers 07/76 open).
- @1550: byte context `@1545:00 @1546:46 @1547:70 @1548:12 @1549:94 @1550:92 @1551:45` = "pour que prenne [92] ce" — the bar's direct-object reading "pour que [S] prenne 92" is grammatical (S open). PASS per the bar's framing. This is consistent with the standing prenne-subject-S1545 promote verdict (92 direct-object-shaped).

### MARGINAL (governor passes, follower marginal) (2)

- @49: `96 00 92 79 37` = "par pour [N] tout [37]" — "pour [N]" grammatical; post-nominal 79='tout' marginal.
- @593: `09 00 92 79 85` = "[09] pour [N] tout [85]" — same marginal follower.

### FAIL under feminine noun (5)

- @1154: `02 00 92 29 80` = "[02] pour [92]er [80]" — 92 takes the -er infinitive ending directly (29='er' banked, A10 composition). "pour [N]er" is impossible. Kill grade for noun.
- @1379: `89 84 92 69 13` = "[89] on [N] [69] [13]" — 84='on' holds unconditioned (A15 + collision battery); "on"+noun is ungrammatical. Kill grade for noun.
- @66: `12 94 92 69 13` = "n ne [N] [69]" — 94='ne' (promoted, pending ratification); "ne"+bare-noun is ungrammatical (ne-expletif governs verbs). Only true ne-governor of 92 (@1549's 94 is word-internal to "prenne" — verified @1547=70, @1548=12, @1549=94).
- @1310: `52 30 92 44 00` = "[52] pas [N] [44] pour" — 30='pas' (promoted, pending ratification); bare "pas [N]" without 'de' is ungrammatical (parses under ADJ, not noun).
- @1453: `33 46 92 62 61` = "[33] que [N] [62] [61]" — a que-clause needs a finite verb; bare "que [N]" is ungrammatical unless [62] is verb-shaped (62 open; 'il'-rival lead points to pronoun). Clean under V-subjunctive only.

### FENCED — excluded from coverage count (9)

- @354: `78 40 92 98 92` — 40='e' banked letter directly before 92; segmentation open (word-internal "e[92]" composition possible). Fenced for the queued seg-92-354-356 battery.
- @356: `92 98 92 47 11` — parse depends on open 98 ("98 92" self-adjacent sandwich); 98's class unknown. Cannot count as pass.
- @683: `07 00 92 64 29 40 65` — the A6 frame; fenced per A6 (value killed, not re-litigated).
- @901: `86 16 92 67 16` — depends on open 16.
- @1022: `53 84 92 64 45 64` = "[53] on [92] qui ce qui" — fenced residual R-class92-1022 (anomalous under ALL classes, per split-92-adjudication evidence package). Not counted against any class.
- @1218: `77 83 92 61 24` — depends on 83, fenced blocker (le83-window battery).
- @1361: `35 13 92 62 94` — depends on open 13.
- @1490: `08 31 92 39 24` — depends on open 31.
- @1673: `55 81 92 60 03` — depends on open 81 (noun-81 lead open).

## Coverage count (C1)

- Clean passes: 6/22 (27%).
- Passes + marginals: 8/22 (36%).
- Even counting every fenced window as a pass (dishonest upper bound): 17/22 (77%) — still below 80%.
- Excluding all 9 fenced windows: 6/13 (46%), 8/13 (62%) with marginals — still below 80%.

The bar's gate (≥80% of 22 windows = ≥18) is not met on any honest counting.

## Adverses answered

- "'on 92' x2 need reconciliation" — answered: @1379 is a kill-grade fail for noun ("on"+noun, 84='on' unconditioned); @1022 is fenced R-class92-1022 (anomalous under all classes, not a noun-specific adverse).
- "'pour 92' x6 need reconciliation" — answered: @49/@330/@593/@978 parse as "pour [N]" (pass/marginal); @683 fenced under A6; @1154 "pour [92]er" is a kill-grade fail for noun (92 takes -er as stem). None ignored.

## Inverted-subject re-framing (coordination note)

The class-92 null battery recommended re-barring @1550 as inverted subject ("que prenne [92-S]"). This battery tested the bar as written (direct-object reading). The DO reading is grammatical and consistent with the standing prenne-subject-S1545 PROMOTE verdict ("clause genuinely subjectless; 92 is direct-object-shaped; postposed subject after 'pour que' is ungrammatical"). Adopting the inverted-subject re-framing would contradict that promote verdict; this battery has no new bytes to overturn it (the @1550 bytes are identical to what prenne-subject-S1545 saw). Per the escalation rule, the class-92 recommendation vs prenne-subject-S1545 promote is recorded as a standing cross-battery disagreement for the red team — this battery does not re-litigate it and does not overwrite the promote.

## Per-clause results

| clause | result |
|---|---|
| C1 — feminine noun covers ≥80% of 22 windows | **FAIL (kill grade)** — distributional rejection: 6/22 clean (27%), 8/22 with marginals (36%); upper bound 17/22 (77%) < 80%. Two independent kill-grade forcing windows: @1154 "pour [92]er" (noun impossible) and @1379 "on [92]" (84='on' unconditioned). Under §7's sole-polyvalence rule, an unconditioned noun value cannot survive these windows. |
| C2 — conditional @1545 DO reading | **VACUOUS** — C1 fails, so the value is not named and the conditional does not fire. (The DO parse at @1550 remains grammatical; unaffected by this verdict.) |

## Verdict: KILL

The bar's distributional gate rejects the claim at the lane's standard, and two windows force an unconditioned feminine-noun value false at kill grade. This does not contradict any standing verdict: A14 granted 92 only set-level INF-signal ("genuinely ambiguous"); the A6 '-ère' value kill is untouched (@683 fenced, never re-valued); the 09~92 HOLD is untouched; prenne-subject-S1545's promote (92 direct-object-shaped as a slot claim) is not a value claim and stands. The split/polyvalence question stays with the red team (split-92-redteam-evidence queued) — this kill is of the noun VALUE arm only, per §7 (no polyvalence declared at battery level).

No follow-ups are queued by this kill (nulls regenerate; kills close). Standing next steps live elsewhere: verb-92-subset (queued, tests the verbal arm) and split-92-redteam-evidence (red-team adjudication of the tripartite profile).

## Standing constraints observed

Did not touch R5005, sealed gate instances, or the red-team adjudication queue. Did not use `canonical.py`. No numbers invented: every offset and count re-derived on the repaired 1,847-pair stream. No polyvalence declared. No standing verdict downgraded or overwritten.
