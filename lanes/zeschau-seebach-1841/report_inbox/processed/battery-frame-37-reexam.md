# Battery report: frame-37-reexam (ESCALATION — red-team re-adjudication required)

**Target:** frame-37-reexam — 37 predicative-frame re-examination
**Worker:** 8ad0f2f2-908b-44e3-b37f-4dec061523ca | **Date:** 2026-10-08 | **Run:** UTC 2026-10-08T08:50:42Z
**Stream:** repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py). Never canonical.py. No R5005 touched. No data invented.

## ESCALATION HEADLINE (red team decides; this battery does NOT)

**The est-finder's fencing arithmetic is confirmed exact on the repaired stream, and it tensions — but does not on its own overturn — the standing round-15 A1 grant.** Under standing ISLET-10 law (round-10 R7), five of the six 59→37 legs are unlicensed-pre LEFTOVER (VOID) and the sixth (@1796, pre=94) is licensed but S5-fenced on 37="le" MEDIUM. The A1 battery and its red team never checked the six legs against classification.json. Whether the ISLET-10 scope gap voids A1's clause (a) — and with it the 37 frame (6→0 valid legs: DEMOTE to HOLD) and the 42 frame (2→0: DEMOTE to HOLD) — is a red-team adjudication, not a battery decision. 32 stands on 2 valid legs either way. This report delivers the re-derived window-level evidence only.

## Bar (verbatim from battery-queue.json)

> escalate to red team with re-derived fencing analysis; battery may only gather the window-level evidence

## Bar as numbered clauses

1. Re-derive all six 59→37 windows on the repaired stream with @-offsets, 7-mer windows, and pre cells.
2. Apply the ISLET-10 fencing analysis per window (licensed pre in {64,94,93}; LEFTOVER = VOID; S5 status).
3. Verify A1's "+1 negated leg @1795" against the stream (@1795/@1796 = one physical window or two).
4. Re-derive the listed adverses: la-finder's "la 52-37-43" vote; the verb frames "qui 37", "en ce qui [23/26]-37", "que 84-24-37".
5. Escalate the A1-vs-est-finder conflict to the red team WITHOUT deciding it.

Per-clause result: **PASS / PASS / PASS / PASS / PASS** — all clauses satisfied as evidence-gathering. No decision taken.

## Method

1. Reparsed the repaired 1,847-pair stream byte-exactly per repair_parse.py (96 unique pairs; crib pair-aligned).
2. Enumerated all 27 59-cells; filtered 59→37 transitions (n=6, no other).
3. Cross-checked each 59-cell against code/crowd10/conditioner59/classification.json (ISLET-10 partition).
4. Applied the ISLET-10 rule mechanically: licensed iff pre(59) ∈ {64,94,93}; unconditioned 59="est" is kill-grade refuted (round-10 R7(a)).
5. Re-derived all adverse frames by byte-exact n-gram search on the repaired stream.

## Window-level evidence (59-cell @-offsets, 0-based stream index)

| # | 59-cell | pre | window (9-mer centered on 59) | ISLET-10 class | fencing result |
|---|---------|-----|-------------------------------|----------------|----------------|
| 1 | @528 | 44 | 81 97 47 44 **[59] 37 64** 26 32 (a3_00) | LEFTOVER | **VOID** — pre not in {64,94,93}; note: "'ce [44] [59] le qui' resists both" |
| 2 | @624 | 14 | 37 76 82 14 **[59] 37 33** 29 87 (a4_01) | LEFTOVER | **VOID** — pre not in {64,94,93} |
| 3 | @912 | 83 | 54 49 64 83 **[59] 37 96** 09 02 (a5_09) | LEFTOVER | **VOID** — pre not in {64,94,93}; 37@913 suc = 96="par" (promoted): "le par" ungrammatical under S5's own foundation |
| 4 | @1178 | 48 | 36 74 32 48 **[59] 37 77** 78 94 (a6_10) | LEFTOVER | **VOID** — pre not in {64,94,93}; 37@1179 suc = 77; classification.json notes "37!=le forced ('le le' x)"; A7 killed 48="est" so pre is not "est" either way |
| 5 | @1443 | 68 | 85 01 52 68 **[59] 37 64** 77 84 (a7_09) | LEFTOVER | **VOID** — pre not in {64,94,93} |
| 6 | @1796 | 94 | 86 56 42 [94] **[59] 37 91** 79 87 (a8_10) | LEFTOVER ("n'est le" era 10/3.96M, rare not absent) | **CONDITIONAL** — ISLET-10 LICENSES "n'est" (pre=94); the ONLY fence is S5 (37="le" MEDIUM, round-7, never re-litigated) |

**Fencing score: 5 VOID, 1 CONDITIONAL (@1796, turns on S5).**

### A1 double-count correction — CONFIRMED

stream[1794:1798] = [42,94,59,37]. @1795 is the 94-cell of the @1796 window, not a second window. A1's "+1 negated leg @1795" violates A1's own independence clause (non-overlapping positions). **6 unique windows, not 7.**

### Control re-derives (both sides' counts confirmed exact)

- 59→32 x3 @316/@448/@1210: @316 EST, @1210 EST (both pre=64, "qui est 32"), @448 ESTE (pre=61, F33-excluded from the islet rule). **Valid 32 legs under standing law: 2.** 32 frame survives on 2 legs.
- 59→42 x2 @463 (LEFTOVER, pre=11) / @1186 (ESTE, pre=06, F33-excluded). **Valid 42 legs: 0.**
- 59→19 x1 @1777 (pre=64, EST) — HOLD, both sides agree; round-15 "x2" was one physical window.
- 59→30 x2 @559 (EST) / @1715 (ESTE); 59→39 x2 @763 (EST) / @1511 (LEFTOVER); 59→45 x1 @103 (EST).
- classification.json EST keys = exactly {103, 316, 559, 763, 1210, 1777} (n=6). No other keys.
- n59 = 27; all six claimed positions are the only 59→37 transitions stream-wide.

### Adverse re-derives (live 37 evidence outside the est fight)

- **la-finder's "la 52-37-43" x2 — CONFIRMED:** 11-52-37-43 @1123 (ctx 14-06-[11-52-37-43]-00-86) and @1721 (ctx 68-06-[11-52-37-43]-98-39). 11="la" banked. Two distinct windows vote adjective-class 37 from a non-est frame.
- **"qui 37" x3 — CONFIRMED:** 64-37 @675 (ctx 24-80-03-[64-37]-77-45-23-09-07), @938, @1632 (both byte-identical 00-33-21-[64-37]-01-...; both feed the A12-granted 37-01 unit). 37 sits in verb position after "qui" three times.
- **"en ce qui [23/26]-37" — PARTIALLY CONFIRMED with a correction:** 64-23-37 @181 and 64-26-37 @1768 both exist and are the only two. BUT the byte-exact "en ce qui" prefix (40-45-64) does **not** occur — the observed left context at both windows is **24-87-64** ("[24] ce [23/26] 37", 87="ce" promoted). The claim as worded needs re-bar-ing with the real prefix.
- **"que 84-24-37" x2 — CONFIRMED:** 46-84-24-37 @309 (ctx 20-17-[46-84-24-37]-78-45-64) and @472 (ctx 06-67-[46-84-24-37]-78-74-45). 46="que" banked, 84="on" granted (A15). Both feed 37-78.
- **37-01 x3 — CONFIRMED:** @939/@1633/@1817 (A12 granted unit).
- **37-78 x4 — CONFIRMED:** @312/@414/@475/@1770 (est-finder's own correction holds).
- **52-37 x4 — CONFIRMED:** @1124/@1129/@1356/@1722 (est-finder's CORRECTION of its own x3 stands; @1124 and @1722 sit inside the two 11-52-37-43 windows).
- 37 total n = 28; 37-96 x1 stream-wide (@913 only); 37-77 x2.

## Per-window fencing vs the two sides

- **Side A (A1 grant)** claimed six predicative "est [37]" legs under clause (a) (>=2 independent "est X" windows). The round-15 A1 battery and its red team never checked the six legs against classification.json, which was already partitioned before A1 ran. ISLET-10 is standing law; under it, clause (a)'s leg count is 6→0 (five VOID + one S5-fenced). Whether that scope gap voids clause (a) is for the red team.
- **Side B (est-finder)** claimed all six legs VOID per ISLET-10 + S5. Confirmed arithmetically: the partition applies exactly as claimed. Its one soft claim — @1796's VOID depends on S5 standing — is correctly flagged as conditional, not asserted.
- **S5's foundation (37="le" MEDIUM, round-7):** the two windows that strain it are re-derived: @913 "le par" (37-96, the ONLY 37-96 adjacency stream-wide; 96="par" promoted) and @1179 "le le" (37-77, classification.json's own note). Real tension, single window each, neighbors (83, 09) unresolved. Not kill-grade on its own.

## Verdict

**NULL — escalation battery.** The bar is satisfied as evidence-gathering (all 5 clauses PASS), and the conflict is escalated to the red team with both counts re-derived. No verdict downgraded; A1's frame grant stands untouched pending red-team re-adjudication (protocol §5.2: a battery never overwrites a standing red-team verdict).

## Follow-ups for the supervisor queue (null regeneration)

1. **s5-foundation** — 37="le" MEDIUM under test. Bar: (a) >=2 of 37's 28 windows where a "le" reading forces ungrammatical French, with named parses; (b) the @913 "le par" window re-derived with neighbor analysis (83, 09 — both unresolved); (c) zero windows requiring 37="le". Priority 1: gates @1796 and the S5 fence. Evidence: @913 (37-96, sole stream-wide 37-96 adjacency, 96="par" promoted); @1179 "le le" (37-77 x2, classification.json's own note); "qui 37" x3; 37-78 x4; 37-01 x3. Adverses: S5 standing fence (round-7); A12 37-01 unit grant ("certain" cer-tain compatibility, not proof). (Matches est-finder's proposal 1.)
2. **qui-2326-prefix** — name 24/87 in "qui [23/26] 37". Bar: parse the real 24-87-64-23/26-37 windows (@181, @1768) with 24 and 87 named; test whether the frames stay verb-position after naming; coordinate with noun-26 (26 is class-unresolved). The claimed "en ce qui" (40-45) prefix does not occur — do not re-bar it as written.
3. **la-523743-adjective** — test la-finder's adjective vote. Bar: 52's contact profile under the 11="la" article frame (both windows @1123/@1721 parse with 52 adjective-shaped and 37 in a nominal slot); >=1 independent adjective-slot confirmation of 37 outside the est frames or record the vote as unanchored.

---
Lock: locks/frame-37-reexam.lock created 2026-10-08T08:50:42Z, deleted on completion of this report. No R5005 touched. No sealed gates touched. No promotions made.
