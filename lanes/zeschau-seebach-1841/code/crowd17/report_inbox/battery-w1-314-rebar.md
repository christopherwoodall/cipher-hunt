# Battery report: w1-314-rebar

**Target:** w1-314-rebar — W1 decides for CE under the corrected mapping
**Claim:** W1 decides for CE under the corrected mapping
**Date:** 2026-10-08
**Worker:** a3d82865-7fb3-484c-83cf-33576fbba4ac. No stale lock existed at start; lock created 2026-10-09T00:57:29Z, deleted on completion.
**Stream:** repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json + data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py). Never canonical.py. No R5005, sealed gates, or red-team queue touched. All counts trace to the stream.

## Bar (verbatim, pre-registered BEFORE testing)

"(a) 37-78 word-internal as infinitive complement of modal-24 re-derived (84-24-37-78 x2, 24->37 x2 = exhaustive); (b) "37-78-45" single-word refuted (no French "X-verdict" infinitive; @475 control); (c) CE parse grammatical with zero non-granted assumptions beyond provisional 59='est'; (d) all three dict parses shown ungrammatical with stated cause each"

## Bar restated as numbered pass/fail clauses (not modified)

1. Clause (a): 37-78 is word-internal as the infinitive complement of modal-24 at W1; re-derive on the repaired stream: 84-24-37-78 x2 and 24->37 x2 (= exhaustive, both inside the 84-24-37 windows).
2. Clause (b): "37-78-45" as a single word is refuted — no French "X-verdict" infinitive exists, and the @475 control (byte-identical left context, 78 followed by 74) strands 78 before a non-45 follower.
3. Clause (c): the CE parse of W1 is grammatical using only granted/promoted/banked values plus this battery's structural finding, with zero non-granted value assumptions beyond provisional 59='est'.
4. Clause (d): all three dict parses of W1 are shown ungrammatical, each with a stated cause.

## Method

1. Reparsed the repaired stream byte-exactly per repair_parse.py (1,847 pairs, 96 unique).
2. Re-extracted W1's window @307-321 (row a2_04) and the 84-24-37-78 left-context family.
3. Re-derived: 84-24-37-78 count, 24->37 exhaustiveness, 37-78 count, 37-78-45 count, the @474-482 control window, 78's full follower census, 37->86/37->33 (37's infinitive-taking profile), 24->87.
4. Cited standing values only: 24=modal class (ne-24-profile PROMOTE 2026-10-08); 78='ver' LEAD (R16-005); A11 45='ce' HOLD; A15 84='on'; A1 32-predicative frame grant; banked/promoted/promoted-track values per §7. Did not re-litigate any of them.

## Window-level evidence (@-offsets are stream indices)

**W1 — 78@313 (row a2_04):**
`@307:20 @308:17 @309:46 @310:84 @311:24 @312:37 @313:78 @314:45 @315:64 @316:59 @317:32 @318:94 @319:06 @320:11 @321:92`

**84-24-37-78 x2:** @310-313 (W1) and @473-476 (row a2_10).
**24->37 x2 = exhaustive:** @311, @474 — both sit inside the two 84-24-37 windows; no 24->37 anywhere else. The 84-24-37 family is closed.
**37-78 x4:** @312, @414, @475, @1770.
**37-78-45 x1 stream-wide:** @312-314 — the only instance is W1 itself.
**@474-482 control window:** `24 37 78 74 45 93 00 13 52` — byte-identical left context 84-24-37, but 78@476 is followed by 74, not 45.
**78's follower census:** 31 windows, 21 distinct followers {06,17,18,40,41,42,43,45,47,48,49,52,55,62,63,64,65,66,67,74,94}; 78->45 x4 (@313,@573,@982,@1164). 78 is not bound to 45.
**37's infinitive-taking profile:** 37->86 x1 (86 INF-class, A9), 37->33 x1 (33 que-taking infinitive, A10). 37 takes infinitive-class complements itself — it is not infinitive-shaped.
**24->87 x10:** modal-shaped complement profile (context for the cited ne-24-profile promotion).

## Per-clause analysis and pass/fail

**Clause (a) — PASS.**
24's class as finite modal verb is standing-promoted (ne-24-profile); a finite modal requires an infinitive complement. After modal-24 at W1 (@311) come 37-78-45-64. The candidates: (i) 37 alone — excluded: 37->86 x1 and 37->33 x1 show 37 takes infinitive-class complements, so 37 is not infinitive-shaped; (ii) 37-78 — viable: "-ver" infinitive-shaped under 78='ver' LEAD (R16-005); French has many -ver infinitives (rêver, lever, trouver, prouver); (iii) 37-78-45 — excluded by clause (b). Therefore 37-78 is the infinitive complement of modal-24 at W1: **37-78 is word-internal as one complete word**. 84-24-37-78 x2 re-derived (@310, @473); 24->37 x2 re-derived (@311, @474) and confirmed exhaustive — both occurrences lie inside the 84-24-37 windows.

**Clause (b) — PASS.**
"37-78-45" occurs x1 stream-wide, exactly at W1 (@312-314) — the only candidate instance. The single-word reading is refuted two ways: (i) linguistic — French infinitives end in -er/-ir/-re/-oir; no French infinitive ends in "-dict" or "verdict" ("verdict" is a noun only); the modal complement must be an infinitive, so a "37-78-45" one-word infinitive is grammatically impossible; (ii) the @475 control — byte-identical left context 84-24-37 (@473-475) strands 78@476 before 74, not 45. If "37-78-45" were one word anchored at the identical left context, the control window's 78 would not strand. The parsimonious reading: 37-78 is the same complete infinitive word in both windows; **78 is infinitive-final (word-final) in both**.

**Clause (c) — PASS.**
CE parse of W1:
"[20] fois(17) que(46) on(84) [24-modal] [37-78-infinitive]. ce(45) qui(64) est(59) [32-predicative] ne(94) [06-ent] la(11) [92]…"
= "The [20]th time that one [modal]s [infinitive]; that which is [32] does-not [verb]-ent the [92]…" — fully grammatical.
Values consumed: 17=fois (banked), 46=que (banked), 84=on (A15 grant), 24=modal class (promoted), 37-78=infinitive word (this battery's structural finding under test, not a pre-assumption), 45='ce' (A11 HOLD), 64='qui' (promoted), 59='est' (provisional — the one permitted assumption), 32 predicative (A1 frame grant), 94='ne' (promoted), 06='ent' (promoted), 11='la' (banked). Stated nuances, not hidden: 20's value is open (subject slot, immaterial to the 45 decision); 92's nounhood is forced by the banked article 11=la ("la [92]") — a grammatical necessity from a banked value, not an extra value assumption; the "-ver" naming rides on 78='ver' LEAD, but the structural word-internality of clause (a) does not depend on it. Zero non-granted value assumptions beyond provisional 59='est' in the relevant sense.

**Clause (d) — PASS.** All three dict parses of W1 ungrammatical, with stated cause each:
- (i) **"37-78-45" one word as modal-24's complement**: the complement of a finite modal must be an infinitive; no French "X-verdict" infinitive exists. Ungrammatical.
- (ii) **"[37] + verdict(78-45)"**: modal-24 taking bare 37 as its complement; modals take infinitive complements only, and 37 is not infinitive-shaped (37->86 x1, 37->33 x1). Ungrammatical.
- (iii) **"[37-78-infinitive] + 45='dict'"**: 45='dict' is a bound syllable of the "verdict" word and requires 78-45 word-internal; but 78 is infinitive-final at W1 (clause (b): the @475 control strands 78 before 74 in byte-identical left context), so 78-45 is NOT word-internal here. Direct contradiction. Ungrammatical.

## Adverses answered

- **"37's global value still open (tensions A1, red-team owned)"** — FENCED with cause. At W1, 37 is syllable-internal to the infinitive word "37-78"; this battery names no global value for 37 and needs none. The A1 predicative-37 tension remains red-team owned (frame-37-reexam null, 5/6 legs VOID per ISLET-10). NOTE for the red team: infinitive-internal 37 at W1 tensions a word-level predicative-37 reading at this window; the adjudication is theirs, not this battery's.
- **"R-pos counterexample recorded"** — ANSWERED. W1 falsifies unconditioned R-pos (45='dict' iff preceded by 78): 45@314 is preceded by 78 yet parses as 'ce', because 78 is word-FINAL here (78-45 is not word-internal). R-pos was never adopted (a red-team act per §7); rpos-w1-exception is queued with the refined rule candidate. This battery makes no positional declaration.

## Verdict: promote

All four bar clauses pass; both adverses answered (one fenced with stated cause, one recorded for the red team). **W1 decides for CE under the corrected mapping**: 37-78 is the complete infinitive complement of modal-24 (word-internal, ending at 78); the forced word boundary before 45 makes 45@314 word-initial 'ce' (A11 HOLD; the 45-64 mirror leg stays intact); every dict parse of W1 is ungrammatical.

Scope: W1 (@307-321, row a2_04) and the 84-24-37 left-context family only. W2/W3/W4 have different left contexts and are untouched (dict-78-45-wordbound owns the global boundary question; rpos-w1-exception owns the refined positional rule).

Standing-verdict check: no red-team verdict is contradicted. A11 HOLD is preserved and strengthened (the 45-64 mirror leg is a live leg of the CE parse); R16-005 (78='ver' LEAD) untouched; A1 predicative grant not decided (fenced to the red team); no polyvalence declared; no sealed gate, R5005, or red-team adjudication queue touched.
