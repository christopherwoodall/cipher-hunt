# Battery verdict: val-02-1153

- Target id: `val-02-1153`
- Claim: "name 02's class/value at @1153"
- Date: 2026-10-09
- Worker: battery worker (subagent 860d1a1b-03c3-47fc-a6c6-0d11b76e4ac7)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; asserts 1847/96 held in-session). `canonical.py` never used. R5005, sealed gates, red-team queue untouched.

Terms (ASD-STE100): "locus-level" = the class naming holds at this window only, not as a global claim about 02. "Battery grade" = the evidence standard of this pipeline.

## Bar (verbatim, pre-registered before testing)

"name 02 at @1153; a finite-02 revives the @1156 finite-80 reading (the only live resurrection path of the fenced imperative arms); else fence"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** 02 is named (class and/or value) at the locus with battery-grade evidence.
2. **C2:** If 02 is finite at the locus, the @1156 finite-80 reading is revived (per the parent battery's pre-registered revival logic).
3. **C3 (else-arm):** If 02 cannot be named, fence with stated cause.
4. **C4 (adverse):** The fenced bare-verb imperative readings (imp-80-bare-1156-1596) are not disturbed.

## Offset note

The target's "@1153" is 1-based. The 02 locus is **0-based @1152** (last pair of row a6_08; row a6_09 starts at @1153). The parent battery's "@1156" (the 80 locus) is 0-based @1156 in both conventions. All offsets below are 0-based repaired-stream indices.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/val-02-1153.lock` on start (agent id + 2026-10-09T19:09:00Z); no prior/stale lock; deleted on completion.
2. Re-derived the repaired stream byte-exact in-session (1,847 pairs / 96 types asserted).
3. Read the parent battery (`battery-imp-80-finite-rival-1156-1596.md`, NULL 2026-10-09) and the standing 02 record before testing; adopted, never re-litigated:
   - 84="on" granted, **unconditioned** (A15-C2; on-01-vs-84-homophony battery).
   - 00="pour" granted (A9, leg-1 class-level).
   - 29="er" banked GT; 92=verb class-level; 17="fois" granted.
   - 02-class-609 (NULL): 02's global profile is split — verb-selecting "qui [02]" windows x2 (@609, @750) vs non-finite-forcing windows (@305 "[88] [02] [88]", @858 "on [02] faire"); no global class nameable at battery grade. This battery tests the locus only.
   - 02-preposition killed (standing).
4. 1841 diplomatic French throughout.

## Window-level evidence

Locus (0-based @1149–1162):
`33 66 84 02 00 92 29 80 17 77 82 44 83 21`
= "[33-INF] [66] on(84) [02] pour(00) [92-verb]er(29) [80] fois(17) le(77) m(82) [44] [83] [21-noun]"

n(02) = 17 stream-wide (re-confirmed in-session): @128, @305, @410, @459, @495, @609, @695, @718, @750, @858, @887, @916, @1084, @1152, @1299, @1467, @1819.

### The @1152 frame

The immediate frame is "on(84) [02] pour(00)". 84="on" is a granted, unconditioned subject pronoun; it selects a finite verb. 00="pour" is a granted preposition heading the purpose infinitive "pour [92]er".

Class-by-class exclusion at this locus:

| Class | Test | Result |
|---|---|---|
| Finite verb | "on [V-fin] pour [V-inf]" — canonical French clause | **LICENSED** |
| Infinitive | "*on parler pour manger" | DEAD — ungrammatical every period |
| Participle | "*on parlé pour manger" | DEAD |
| Noun | "*on table pour manger" | DEAD — "on" + bare noun ungrammatical |
| Adjective | no nominal head present | DEAD |
| Adverb | "on [adv] pour [inf]" — adverb cannot satisfy "on"'s verb requirement | DEAD |
| Preposition | killed lane-wide; "on [prep] pour" ungrammatical | DEAD |
| Conjunction | "on [conj] pour" ungrammatical | DEAD |
| Pronoun/clitic | clitic needs a verb to its right; "pour" is a preposition | DEAD |
| Determiner | "on [det] pour" ungrammatical | DEAD |
| Interjection | does not satisfy "on"'s verb requirement | DEAD |
| Imperative | "on" cannot be an imperative subject | DEAD |
| Sub-lexical with 84 | contradicts 84="on" word grant (A15) | DEAD |
| Sub-lexical with 00 | contradicts 00="pour" word grant (A9) | DEAD |

Finite verb is the **only licensed class** — by positive frame ("on" + finite verb is the canonical clause) and by exhaustion of every rival.

Consistency check: the "qui [02]" windows (@609, @750) independently show 02 in verb-selecting position (relative "qui" requires a finite verb). The @1152 finite-verb naming is consistent with those legs; it does not override the @305/@858 non-finite-forcing windows — hence locus-level scope only.

## Per-clause pass/fail

- **C1: PASS.** 02 is named **finite verb** at @1152 (0-based), locus-level. Positive leg: the canonical "on [V-fin]" frame with granted, unconditioned 84="on". Exclusion leg: all 13 rival classes die at this locus (table above). No value is named — 02's value stays open.
- **C2: PASS.** Per the parent battery's pre-registered revival logic ("naming 02 as finite revives the reading"), the @1156 finite-80 reading is now **live** (revived from fenced). The parent's C1 failed solely because 02 was unvalued; that blocker is removed. Note: "live" ≠ "proven" — the finite-80 reading still needs its own licensing (80's value, agreement, the continuing-clause mechanics), which belongs to the already-queued `val-80-1596-3sg` and the finite-80 work, not to this battery.
- **C3: moot** (C1 passed).
- **C4: PASS.** The fenced bare-verb imperative readings are untouched — this verdict revives only the finite-80 rival, exactly the resurrection path the bar names.

## Scope (stated, not hidden)

- **Locus-level class only.** 02 = finite verb at @1152. No value named. 02's global class stays split-shaped per 02-class-609 (@305 and @858 force non-finite elsewhere) — this verdict does not name a global class and does not contradict that NULL.
- **No §7 declaration.** A locus-level class naming is not a polyvalence claim; 67 et/veut remains the sole true polyvalence.
- **No standing/red-team verdict contradicted or downgraded.** 84="on", 00="pour", 29="er", 92 verb-class, 17="fois" all used as granted/banked; none re-litigated.
- **Canonical-stream caveat stands:** the locus straddles the a6_08/a6_09 row boundary (68/70 offsets unvalidated).
- The @1156 finite-80 reading is revived to live status; its proof is separate work.

## Verdict: PROMOTE (locus-level class)

02 is **finite verb** at @1152 (0-based; the target's "@1153" is 1-based). The @1156 finite-80 reading is revived per the bar. No follow-ups required (promote, not null); the natural continuation (`val-80-1596-3sg`, finite-80 licensing) is already queued.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-02-1153.md` (this file).
- Queue: `val-02-1153` queued → `verdict`/`promote`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `code/crowd17/next-token/locks/val-02-1153.lock` created on start, deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
