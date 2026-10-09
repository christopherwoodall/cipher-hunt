# Battery report: sel-37-nominal-1179

- Target id: `sel-37-nominal-1179`
- Claim: test 37's class at @1179 ("est [37] le [78]"): does the remaining non-cleft, non-@625 "est 37" window also force nominal?
- Date: 2026-10-09
- Worker: battery worker (subagent a03f3d9c-dcb3-42d6-9195-85df805f5546)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`). Verified in-session: 1,847 pairs, 96 types. `canonical.py` never used. R5005, sealed gates, red-team queue untouched.
- Offsets below are 0-based stream indices (lane convention).

Terms (ASD-STE100): "name" = state a class/value with byte evidence at battery grade. "kill grade" = a window forcing the claim false under standing values. "unaccusative inversion" = the French shape "est [past participle] le [noun]" with postposed subject (e.g. "est arrivé le courrier").

## Bar (verbatim from queue `bars` field)

"Bar: test 37's class at @1179 ("est [37] le [78]"): does the remaining non-cleft, non-@625 "est 37" window also force nominal? Bar: name 37's class at @1179 at battery grade, or fence with stated cause."

Restated as numbered pass/fail clauses before testing:

1. **C1:** 37's class at @1179 is named at battery grade — one class parses "est [37] le [78]" with standing values and zero new assumptions, and every rival class is excluded at kill grade.
2. **C2:** fence with stated cause iff C1 fails.
3. Embedded question: does @1179 force nominal like the cleft windows (@529/@1444) and @625? Answered inside C1.

Standing premises used, not re-litigated: banked pencil 11=la/70=pre/82=m/34=i/29=er/40=e/46=que; granted 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce; provisional 59=est, 77="le" (§7-usable); 78='ver' LEAD (R16-005) with the R20-banked @819 "ce verre" noun leg; A1 predicative grant for 37 (class open); French grammar as test apparatus (no pro-drop; no zero-relativizer; "est" + finite verb ungrammatical).

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/sel-37-nominal-1179.lock` (agent id + UTC timestamp); deleted on completion. No stale lock was present.
2. Re-derived the repaired stream in-session. All asserts held (1,847 pairs, 96 types, n(37)=28).
3. Byte-confirmed the locus (row a6_10): `[1177]48 [1178]59 [1179]37 [1180]77 [1181]78 [1182]94 [1183]82`, i.e. "[48] est [37] le [78] ne m…".
4. Enumerated every class arm for 37 in the "est [37] le [78]" frame against standing values; ran a period-corpus shape check for "est [X] le [inf]" (77 files, ~34.5M chars).

## Window-level evidence

The six byte-exact "59 37" ("est 37") windows: @528, @624, @912, @1178, @1443, @1796 — matching the parent battery's @529/@625/@913/@1179/@1444/@1797 (1-indexed there).

**The "37 77" bigram is a hapax pair:** exactly 2 occurrences stream-wide — @676 ("64 37 77" = "qui [37] le ce", the window that kill-graded 37='re' in enterre-37re-s5) and @1179 ("59 37 77" = "est [37] le [78]"). No other "37 le" geometry exists to borrow a parse from.

**Corpus shape check:** a regex sweep for "est [X] le [infinitive]" over the full period corpus returned zero genuine hits — the "le"-as-object-pronoun + infinitive shape after "est [X]" is unattested. What IS attested is the unaccusative inversion "est [past participle] le [noun]": "lorsque y est arrivé le courrier de Brunnow" (nesselrode-v9, diplomatic correspondence). So the "le [78]" tail is licensable only as determiner + noun, i.e. "le verre" under the standing 78='ver' lead.

### Class-by-class elimination at @1179 ("est [37] le [78]")

- **Finite verb:** "est [37-V]" = auxiliary + finite verb. Ungrammatical at kill grade. DEAD.
- **Infinitive:** "est [37-INF]" needs à/de/modal governor; none present. DEAD at kill grade.
- **Determiner / pronoun / adverb:** cannot stand predicatively after "est". DEAD at kill grade.
- **Noun:** "est [37-N] le verre" — no French construction licenses "est [noun] le [noun]"; the "le"-as-object-pronoun reading gives "est [N] le [V-fin]", ungrammatical; a dropped-"qui" relative is barred. DEAD.
- **Adjective:** "est [37-ADJ] le verre" — ungrammatical in canonical order (inversion runs the other way: "grande est la déception"); the corpus sweep finds no "est [ADJ] le [INF]" shape. DEAD.
- **Past participle:** "est [37-PP] le verre" — licensed by the unaccusative-inversion construction ("est arrivé le courrier", corpus-attested above): 37 = past participle of an être-taking verb, "le verre" = postposed subject. Uses only standing premises: 59=est (provisional), 77="le" (provisional), 78="verre" (lead + R20-banked @819 leg). SURVIVES — the unique surviving arm.

The 48-as-subject rival ("[48-S] est [37] le verre") makes the window unparseable under every class above; since the cipher encodes grammatical French, 48 closes leftward ("…[32] [48]") and the clause is the subjectless inversion — a consequence of the elimination, not a new assumption.

### C1 — PASS: 37 = past participle at @1179, named at battery grade

Past participle is the unique surviving class with zero new assumptions. This answers the embedded question: **No — @1179 does not force nominal.** It is the first "est 37" window to force the participle arm. Tally of the six "est 37" windows: nominal forced at @529/@625/@1444 (clefts + x-33-37-licensing), past participle forced at @1179, predicative-shaped (unadjudicated here) at @913/@1797.

Note: the être-verb restriction (only unaccusative participles license the inversion) constrains 37's VALUE, which stays red-team venue. The class naming does not depend on it.

### C2 — does not fire

## Verdict: PROMOTE

37's class at @1179 is named at battery grade: past participle, forced by unique-survivor elimination in the "est [37] le [78]" frame.

## Scope and caveats

- Locus-level class naming only (@1179). No value named for 37; 37's global class stays red-team venue (§7; frame-37-reexam untouched).
- The parallel "est [37] par [09]" window @913 (agentive "par" — also participle-suggestive) is NOT adjudicated here; flagged as the natural next locus.
- Premises: 59=est and 77="le" provisional; 78="verre" lead-grade (R16-005, @819 leg banked R20). If the red team ever kills 78="verre", the "le [78]" determiner reading collapses and this naming must be re-run.
- No standing or red-team verdict contradicted, downgraded, or re-litigated; §7 intact. Canonical-stream caveat stands (row a6_10 offset unvalidated).
- Per §4 (promote), no follow-ups required. One natural next question is noted in scope (@913) but not queued, at the supervisor's discretion.

## Bookkeeping

- Queue: `sel-37-nominal-1179` → status `verdict`, result `promote`, 2026-10-09 (pre-write assert passed — was `queued`/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `locks/sel-37-nominal-1179.lock` created on start, deleted on completion.
