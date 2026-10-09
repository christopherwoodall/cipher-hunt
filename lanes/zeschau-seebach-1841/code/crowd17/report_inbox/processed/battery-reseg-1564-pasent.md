# Battery verdict: reseg-1564-pasent

**Target claim:** re-segment '30 06 60 71' at window B (@1557-1574, 1-based) under the 'pasent' findings; gates on 26/56 class.
**Date:** 2026-10-09. **Priority:** 3.

## Bar (verbatim, pre-registered)

"resolve iff window B re-segments grammatically under the 'pasent' boundary shift; else fence with stated cause"

Numbered clauses (fixed before testing, not modified after):

1. **C1** — window B re-segments grammatically under one of the pasent boundary-shift arms: (a) 06 as previous word's ending ("passent"); (b) 06 as next word's onset ("pas" | "ent[60…]"); (c) word-internal "[26]pas".
2. **C2 (else-arm)** — fence with stated cause.

Adverse: "window B's left edge independently anomalous — 'pas'+'ent' ungrammatical; no class of 60 rescues cleanly."

## Method

Read BATTERY-PROTOCOL.md first. Lock `reseg-1564-pasent.lock` created on start, deleted on completion. Re-derived the repaired 1,847-pair / 96-type stream in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` (parsed per `repair_parse.py`; 1,847 pairs / 96 types asserted). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched. 1841 diplomatic French throughout. 0-based indices below unless noted.

Adopted (not re-litigated): `battery-pre-71-60-class` (null — nominal-60 fails at window B; follow-up #3 is this target); `battery-spell-single-consonant` (null — "passent" grammatically excluded at W4); `battery-pasent-subject-26-56` (KILL — 26/56 cannot be 3pl subjects; the 'passent' word-reading dies at all four windows; 30-06 must re-segment; gate "26/56 class" satisfied); `battery-split-60-verbs` (PROMOTE, battery-grade — "06 60" bigram x2, "ent" is a PREFIX: bare-60 verb vs ent-60 verb are two items sharing syllable 60, "entre"/"entend"/"entonne"-shaped).

## Byte-verified window

Row a8_01, 0-based @1554–1573:

`@1554=13 @1555=93 @1556=61 @1557=40 @1558=17 @1559=11 @1560=26 @1561=30 @1562=06 @1563=60 @1564=71 @1565=50 @1566=29 @1567=24 @1568=74 @1569=62 @1570=48 @1571=56 @1572=32 @1573=28`

Knot "30 06 60 71" @1561–1564 (1-based @1562–1565; the target's "@1557-1574" is the 1-based window span). Standing values: 93=verb (class, R19), 40='e' (GT), 17='fois' (promoted), 11='la' (GT), 30='pas' (promoted, conditional), 06='ent' (granted), 29='er' (GT), 24=finite/modal (R24: follower @1568=74 ≠ 85), 62='il' KILLED (R19), 32=predicative (A1, value open). 26/56/60/71 unvalued or class-only.

## Per-arm results

**Arm (a) — 06 as previous word's ending ("passent"): DEAD at kill grade.** Adopted from `pasent-subject-26-56` (KILL): neither 26 nor 56 can be a 3pl subject under standing values and §7, and W4 (@1561, this window) is specifically excluded — "la [26] passent" strands the determiner and French does not pro-drop a 3pl subject.

**Arm (b) — 06 as next word's onset ("pas" | "ent[60]"): BOUNDARY LICENSED, parse still ungrammatical.** `split-60-verbs` (PROMOTE, battery-grade) licenses "06 60" as the ent-60 verb item at exactly this window (its V5: predecessor 06, successor 71). So the knot re-segments as `@1561 "pas" | @1562–1563 "ent[60]" (ent-verb) | @1564 [71]`. The boundary shift the pasent findings demanded is real. But the window does not parse grammatically: "pas" at @1561 has no "ne". Nearest 94='ne' positions: @1549 (consumed by its own clause "94 92 45 23" closing row a8_00 — a "ne" cannot skip its clause) and @1576 (downstream of "pas"; "ne…pas" requires "ne" BEFORE "pas"). "pas"-as-noun fails on gender ("la" feminine vs "pas" masculine). No elliptical or answer-particle license for bare "pas" exists in 1841 diplomatic register mid-clause. Resulting string: "…[93-verb] [61]e fois la [26] pas ent[60-verb] [71] [50]er [24-finite]…" — bare "pas" before a finite verb phrase, ungrammatical.

**Arm (c) — word-internal "[26]pas": over budget.** "repas"/"trépas"/"appas"-shaped readings require inventing 26's letter content (§3 bars invented values at battery grade). The trépas route is independently dead.

**Arm (d) — 06 as 26's ending ("[26]ent", 26 verbal 3pl): dead.** "la [26-stem]ent" would be a 3pl verb with no licensable subject (pasent-subject C1 kill).

**Adverse — answered in part, residual fenced.** The "pas"+"ent" adjacency anomaly is resolved by the boundary shift: 06 is the onset of the ent-60 verb (split-60-verbs PROMOTE), not "pas"'s ending. The adverse's "no class of 60 rescues cleanly" is superseded by the ent-60 item — the rescue is real for the boundary. But the rescue does not extend to "pas", which remains unlicensed. The left edge stays anomalous, now as bare "pas" rather than "pasent".

## Verdict: NULL (fence executed)

C1 FAILS: no boundary-shift arm yields a grammatical parse of window B. C2 FIRES. The fence cause: the "pasent" boundary shift is realized at battery grade ("pas" | "ent[60]", split-60-verbs), but "pas" @1561 lacks "ne" (no 94 in the clause's left context; @1549 consumed, @1576 downstream), "pas"-as-noun fails gender, and the remaining arms need invented values.

**Not kill-grade:** the failure is epistemic, resting on unvalued cells and one missing license — a corpus attestation of bare "pas" in 1841 diplomatic prose, 26's letter content ("repas"), or a "ne" re-analysis could revive the parse. §7 intact; no standing or red-team verdict contradicted or downgraded; no polyvalence declared.

## Follow-ups proposed (all verified ABSENT from the queue)

1. `pas-bare-corpus` (P3) — corpus test: bare "pas" (no "ne") as clause negator in 1841 diplomatic prose. Bar: ≥1 genuine attestation licenses @1561; confirmed zero hardens this fence. (Distinct from `ne-1330-bare-corpus`, which tests bare "ne".)
2. `reseg-1564-26pas` (P3) — test the "[26]pas" word-internal arm at window B: census "26 30" bigrams stream-wide (@995 "26 30 03 60" is a second instance) for a "repas"/"Xpas" word reading. Bar: name 26's letter content with byte evidence or fence the arm.
3. `ent60-71-complement` (P4) — gated: once 71's class is named, test "ent[60] [71]" complement selection to complete the local parse if "pas" is ever licensed.

## Bookkeeping

- Report: this file (`code/crowd17/report_inbox/battery-reseg-1564-pasent.md`).
- `battery-queue.json`: `reseg-1564-pasent` → status `verdict`, result `null`, date 2026-10-09 (temp-file + rename; pre-write assert confirmed queued/verdictless; JSON re-validated post-write; own entry only; no downgrade).
- Lock `locks/reseg-1564-pasent.lock`: created on start, deleted on completion.
- R5005, sealed gates, red-team adjudication queue untouched.
