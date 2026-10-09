# Battery report: particle-20-760-839 — **NULL** (particle face confirmed at battery grade; value 'mais' named and routed to poly-20-docket)

**Target:** `particle-20-760-839` (P3)
**Date:** 2026-10-09 (UTC)
**Worker:** 0b48984a-4a0a-4612-ad1c-fc81e1e5bb36
**Lock:** `code/crowd17/next-token/locks/particle-20-760-839.lock` created on start (agent id + UTC 2026-10-09T08:35:00Z); no stale lock present.

## Bar (verbatim from queue)

"name the clause-initial particle value parsing BOTH windows ('la première' nominalized @760 with the ellipsis stated; the @839 clause boundary after 98 stated); @1703/@307/@280 explicitly out of scope (fenced, not explained)"

## Bar restated as numbered clauses (fixed before testing)

- (c1) Name ONE clause-initial particle value for 20 that grammatically parses BOTH windows: @760 with "la première" nominalized (head-noun ellipsis stated) and 20 clause-initial before the "62 94" ('il ne') frame; @839 with the clause boundary stated after 98 and 20 clause-initial before the "62 94" frame. PASS iff the named value yields a grammatical French reading at both windows.
- (c2) Scope fence: @1703 (verbal face), @307 (det/adj face), @280 (sandwich) explicitly stated as out of scope — not explained, not re-litigated. PASS iff the report states the fence.
- (c3) Decision rule (pre-registered): if (c1) PASS and (c2) PASS → particle face confirmed at battery grade; the value-NAMING routes to `poly-20-docket` per the det-20-window-local-paradigm bound (c) ("route value-naming to poly-20-docket rather than promoting") → verdict NULL with routing + follow-ups. If (c1) FAIL (no particle value parses both) → NULL with follow-ups (nulls regenerate). If a window forces the claim false → KILL.

## Method

Read BATTERY-PROTOCOL.md in full first. All stream facts re-derived in-session from the repaired 1,847-pair / 96-type parse (`code/side-keyhunt/repaired_offsets.json` + `data/upstream-ct_R5005.txt`, parsed per `code/side-keyhunt/repair_parse.py`: `load_rows` + `parse`; asserts held: 1,847 pairs, 96 types; 20 census n=15: @280 @307 @490 @642 @668 @703 @741 @760 @839 @873 @958 @1135 @1224 @1270 @1703). `canonical.py` never touched. R5005, sealed gate instances, red-team adjudication queue untouched. Sibling reports read first: `battery-det-20-window-local-paradigm.md` (null; per-window paradigm decided affirmative at battery grade; bound (a)/(b)/(c) honored) and `battery-nepas-20-adverb-gate.md` (PROMOTE; "ne pas [20-inf]" at @1703 unconditional — hence @1703's "20 62 94" is the verbal face, a different window-class, fenced here). Standing values used: pencil GT (11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que); banked (17=fois); promoted (30=pas, 87=ce, 64=qui, 96=par, 79=tout, 00=pour, 84=on, 47=ce); provisional (59=est, 77=le); demonstrated-not-promoted (62='il' on the 62-94 frames per collision-62-84; 94='ne' R17-001 strong lead). Kills honored: 20="fois", uniform-20-particle (ellipsis-760), uniform-verbal-20-value (inf-20-nepas), 20~17 split.

## Window-level evidence (re-derived, @-offsets 0-based)

The "20 62 94" trigram occurs x3 stream-wide: @760, @839, @1703 (byte-exact). At @1703 the trigram is the verbal face ("ne pas [20-inf]" + "il ne"; nepas-20-adverb-gate PROMOTE) — out of scope here. The remaining two are the particle face under test.

### @760 (row a5_03)

`@748–773: 00 64 02 97 40 67 | 11 70 82 34 29 40 | 20 62 94 59 39 88 66 98 80 10 22 94 07 06`
"…[00=pour] [64=qui] [02] [97] [40=e] [67=et/veut] **la première** [20] [62=il] [94=ne] [59=est] [39] [88] [66] [98] [80]…"

- "la première" = `11 70 82 34 29 40` @754–759 (repair_parse.py gloss-(i) crib, pencil GT). It is a nominalized determiner+adjective: the head noun it modifies is elided — **the stated ellipsis**. The NP is complete without 20.
- 20 @760 heads the "62 94" frame rightward: 62='il' + 94='ne' (collision-62-84 re-read all nine 62→94 windows, including @761, as 'il ne'; "62 94 88" licenses only the "il ne [verb]" parse — no standing word-frame re-segments `40 20` or `20 62`).
- Named value **'mais'**: "…[e], et/veut **la première** ; **mais il ne** [59=est] [39] [88-verb]…" — grammatical: clause-initial adversative particle + "il ne [verb]" frame. (Battery grade: "il n'est [39] [88]" admits an adverb+participle reading, e.g. "il n'est jamais venu"; no fuller naming of 39/66 is attempted — out of scope.)
- The surviving noun leg ("la première [20-noun]", det-20-window-local-paradigm c1) coexists; it does not force the particle leg false — the bar requires the particle parse to be grammatical, not unique.

### @839 (row a5_06)

`@827–852: 82 01 24 87 11 77 76 59 35 56 17 98 | 20 62 94 26 12 16 00 33 96 40 | 62 21 67 91`
"…[87=ce] [11=la] [77=le] [76] [59] [35] [56] [17=fois] [98] **.** [20] [62=il] [94=ne] [26] [12] [16] [00=pour] [33] [96=par] [40=e]…"

- **Clause boundary stated after 98 (@838):** 20 @839 cannot attach leftward — no standing frame re-segments `98 20` (or `17 98 20`) as one constituent, and a free 20 cannot be clause-medial after a closed "…fois [98]" clause without a governor. It heads the "62 94" ('il ne') frame rightward (collision-62-84 covers @840). The "20 62 94" unit is left-anchored at 20 in all three stream occurrences (@760, @839, @1703); at @839 the clause therefore opens at 20, and the boundary is stated after 98.
- 98 distributional note (stated, not decided): n=40; followers 83/82/80/98/00/56/20…; the boundary claim here is positional (20's unattachability leftward + left-anchored frame), not a claim about 98's word-class — hardening 98's function is follow-up #1.
- Named value **'mais'**: "…fois. **Mais il ne** [26] [12] [16] pour [33] par [e]…" — grammatical: clause-initial particle + "il ne [verb]" frame. At @839 the particle slot is effectively forced: noun/det-adj/verbal readings of a free 20 between a closed clause and "il ne" are all ungrammatical (no governor available either side), leaving the clause-initial particle/adverb slot as the only surviving class.

### Scope fence (c2)

@1703 (verbal face: "ne pas [20-inf]", unconditional per nepas-20-adverb-gate), @307 (det/adj face: "[20] fois que", det-20-307-fenced), @280 ("61 [20] 61" sandwich, det values failed per det-20-value) are **explicitly out of scope** — fenced, not explained, per the paradigm bound (a): one window-class per battery, no cross-window-class uniformity claim.

## Per-clause pass/fail

- **(c1) PASS.** 'mais' named as the clause-initial particle value; grammatical French readings at both windows ("…la première ; mais il ne…" with the nominalization ellipsis stated; "…fois. Mais il ne…" with the clause boundary stated after 98). Rivals 'or'/'donc'/'cependant' occupy the same slot and are undiscriminated at battery grade (stated, not hidden); 'et' would require a homophone ruling against 67='et' and is therefore not the named value.
- **(c2) PASS.** @1703/@307/@280 explicitly fenced out of scope above.
- **(c3) FIRES.** (c1) PASS + (c2) PASS → face confirmed at battery grade; value-naming routes to `poly-20-docket` rather than promoting, per the paradigm bound (c) and §7 (no per-window polyvalence declared at battery level; 'mais' is one value for one window-class, named as a routed candidate, not a declared value).

## Verdict: **NULL** — particle face confirmed at battery grade; value 'mais' routed to poly-20-docket

**Headline:** the "20 62 94" particle face survives at both in-scope windows. @839 forces the particle slot (no other word-class is grammatical there); @760 admits the particle parse alongside the surviving noun leg. The named clause-initial particle value is **'mais'**, routed as a candidate to the queued P1 `poly-20-docket` for red-team adjudication — this battery declares no value and no polyvalence. Standing verdicts: none contradicted or downgraded (uniform-particle kill at @1703 untouched — different window-class, fenced; 20="fois" kill and 20~17 split intact). §7 honored.

## Follow-ups proposed (null regenerates work; none duplicate queued or verdict'd targets)

1. `boundary-98-839` (P3) — Harden the @839 clause-boundary statement: determine 98's distributional function (n=40 census; followers 83/82/80/98/00/56/20; predecessors 62/42/66/98/64/43). Bar: state at battery grade whether 98 is clause-terminal; if 98 is shown clause-medial, this battery's @839 face re-opens.
2. `particle-20-value-rivals` (P3) — Discriminate 'mais' vs 'or'/'donc'/'cependant' at @760/@839 using left-context requirements (adversative vs consecutive vs narrative particle after "la première"-type nominals and "…fois [98]" closes). Bar: narrow the rival set or confirm 'mais' as best-supported; feeds `poly-20-docket`.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-particle-20-760-839.md` (this file)
- Queue: `particle-20-760-839` → status `verdict`, result `null`, report path above, date 2026-10-09 (temp-file + atomic rename; only this entry touched; JSON re-validated after write)
- Lock created on start, deleted on completion. `canonical.py` never used; R5005, sealed gate instances, red-team adjudication queue untouched.
