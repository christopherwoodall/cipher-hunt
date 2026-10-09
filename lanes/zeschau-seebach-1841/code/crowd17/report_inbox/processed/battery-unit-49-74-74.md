# Battery `unit-49-74-74` — verdict: KILL

- Target: `unit-49-74-74` (battery-queue.json, priority 3, status queued → verdict)
- Claim: 'test "49 74 74" as a single word/unit with 74 as a letter/syllable (e.g. doubled consonant "-tt-"/"-ss-")'
- Worker: 04d153f0-2c2b-4f28-8e25-6d5f2473a1fa. Date: 2026-10-09.
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; asserts held: 1,847 pairs, 96 types). `canonical.py` NOT used. R5005, sealed gates, red-team adjudication queue untouched.
- Lock: `code/crowd17/next-token/locks/unit-49-74-74.lock` created on start (no prior/fresh lock; no stale lock); deleted on completion.

## Bar (verbatim from battery-queue.json, pre-registered BEFORE testing)

"name the host word via 49's contact profile; the four chains parse with <=10% orphan; kill iff no French word-formation covers all four."

**Restated as numbered pass/fail clauses (frozen before testing):**
1. **C1 (name):** name the host word via 49's contact profile.
2. **C2 (parse):** the four chains parse with <=10% orphan.
3. **C3 (kill):** kill iff no French word-formation covers all four windows.

## Adopted premises (not re-litigated)

- Standing values (§7): 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que (pencil); 87=ce, 64=qui, 96=par, 17=fois, 79=tout, 00=pour, 84=on, 47=ce (granted); 59=est, 77=le (provisional). 48=e (promoted, per `noun-74-formula`).
- 49's class: verb, determiner, relative/interrogative pronoun dead at kill grade (`formula-49-value`); adjective dead at kill grade (`adj-49-420-366`); noun fenced globally (`noun-49-nonchain`, 2026-10-09). Surviving tier: syllable/letter.
- 74's class: open; whole-word 74 killed at kill grade by the '74 74' ×6 doubling (`noun-74-census` NULL/fence, `noun-74-formula` — "no noun, verb, adjective, pronoun, adverb, or determiner doubles adjacently in French"); verb-74 killed (`ne-alone-02-74`).
- `val-49-74-frame` (NULL/fence, 2026-10-09): the '74 74' doubling is a kill-grade blocker for any whole-word parse of the chains; its follow-up #1 (`val-74-letter`) anticipated that a letter-tier 74 dissolves the doubling — this battery is that test.

## Method

1. Read BATTERY-PROTOCOL.md in full before testing.
2. Re-derived the repaired stream in-session; byte-confirmed all four "49 74 74" windows and their rows.
3. Built 49's full contact profile (n(49)=12): predecessors {76×3, 78×2, 24×2, 48×1, 46×1, 29×1, 74×1, 54×1}; followers {74×5, 24×2, 64×2, 61×1, 36×1, 16×1}.
4. Enumerated every French word-formation compatible with "49 74 74" + the followers, constrained by the contact profile; tested each against all four windows.

## Window-level evidence (byte-exact, 0-based pair indices)

| # | @ | row | ±4 context (49 bracketed) |
|---|---|-----|---------------------------|
| W1 | 416 | a2_08 | `84=on 51 37 78 [49] 74 74 46=que 49 36 29=er` |
| W2 | 815 | a5_05 | `24 65 14 29=er [49] 74 74 47=ce 78 40=e 95` |
| W3 | 860 | a5_07 | `48=e 84=on 02 24 [49] 74 74 48=e 47=ce 46=que` |
| W4 | 918 | a5_09 | `96=par 09 02 24 [49] 74 74 40=e 08 65 71` |

Right contexts: W1 `46=que`, W2 `47=ce`, W3 `48=e`, W4 `40=e`. (Matches the doublet-41-589 census.)

49's diagnostic contacts:
- "49 64=qui" ×2 (@909: `54 49 64`; @1433: `76 49 64`) — 49 in antecedent position before relative "qui".
- "76 49 24" ×2 (@653/@990: `76 49 24 26 30 03`) — 76=masc noun, 49, 24=finite verb.
- "49 74" ×5 — the four chains + @1844 (`78 49 74 93`, no doubling).

## Analysis

**Step 1 — the unit cannot be exactly "49 74 74".** No French word ends in a doubled consonant. With 74 as a doubled letter, "49 74 74" = S+CC is word-internal at best; the host word must extend right.

**Step 2 — the only viable rightward extension is "e".** W3/W4 give "49 74 74 e" (48=e promoted, 40=e banked): host word H = "49"+"74"+"74"+"e" = S+LL+e. W1/W2 ("…que", "…ce") admit no letter extension — the word would have to be exactly "49 74 74" there, which Step 1 rules out. This already strains the single-formation requirement; the most charitable reading is H="S LLe" with W1/W2 parsed as H + word boundary.

**Step 3 — 49's contact profile names 49="ce", the only value yielding real words.** "49 64=qui" ×2 forces 49 to be a "qui"-antecedent. Candidates: "ce" ("ce qui" ✓), "rien"/"celui" ("rien/celui qui" ✓ but full words — cannot start a "49 74 74" word), or 49="s"/"x" attaching left as a plural letter ("[N]s qui" ✓ — but then "49 74 74" = letter+doubled consonant, not a French word: no "sll"/"stt"/"sss" word exists). Only 49="ce" yields French words: "cette" (74="t"), "celle" (74="l"), "cesse" (74="s"). Verb candidates ("mettre" 49="me", "battre" 49="ba", "frapper" 49="fra") die on "49 64=qui" ("me/… qui" ungrammatical). The reduplicated-syllable reading (74="pa"→"papa"-type) yields no "49papa" word.

**Step 4 — test each surviving word against all four windows:**
- **"cette"** (best; 49="ce", 74="t"): W4 parses iff 08 is adjectival (`02 24 cette [08-adj] [65-noun]`, 1 assumption). W1 "37 78 cette que" — "cette que" ungrammatical at kill grade (determiner cannot take "que"; no "ne…que", no noun for a relative). W2 "cette ce" — double determiner, ungrammatical. W3 "cette ce que" — ungrammatical. **Covers 1/4.**
- **"celle"** (74="l"): W1 "celle que" ✗, W2 "celle ce" ✗, W3 "celle ce que" ✗, W4 "celle 08" ✗ ("celle" cannot take a bare following cell). **Covers 0/4.**
- **"cesse"** (74="s"): "cesse que" ✗ ("cesser" governs "de"), "cesse ce" ✗, W4 "cesse 08" marginal but W1–W3 dead. **Covers 0/4.**

No other (49, 74) pairing both respects the contact profile and produces a French word. The syllable-tier reading produces no word at any window.

## Per-clause pass/fail

- **C1 (name): FAIL.** The best contact-profile naming is "cette" (49="ce" via "ce qui" ×2, 74="t"), but it does not survive C2; no host word covering the data can be named.
- **C2 (parse ≤10% orphan): FAIL.** Under the only viable formation ("cette"), W1/W2/W3 are ungrammatical — not merely unparsed. Orphan rate is moot: the formation itself is rejected at 3 of 4 windows.
- **C3 (kill iff no formation covers all four): FIRES.** Exhaustion above: the "ce"-family ("cette"/"celle"/"cesse") is the unique contact-compatible word family and none of its members covers all four; every alternative 49 value either kills the word claim outright (letter-attachment) or contradicts "49 64=qui".

## Verdict: KILL

No French word-formation covers all four "49 74 74" windows. The "49 74 74 as a single word/unit with 74 as a doubled letter/syllable" claim is dead. The letter-tier 74 hypothesis (val-49-74-frame follow-up #1) dissolves the doubling but the resulting words ("cette"/"celle"/"cesse") are syntactically impossible at W1–W3 — the failure is French grammar, not the cipher.

## Scope (explicit)

- Killed: the "49 74 74" single-word/unit claim with 74 as doubled letter/syllable, at all four windows.
- NOT decided: 49's global value (49="ce" was a hypothesis for the word-formation only; "76 49 24" does not cleanly support it and no global value is named here); 74's global value/class (74="t" was formation-local); the @1844 "49 74 93" window; standing kills/fences (§7) unchanged.
- No standing or red-team verdict contradicted or downgraded.

## Follow-ups

None — kill verdicts regenerate no mandatory follow-ups per §4. (Natural next question, not queued: 49's value remains open at non-chain windows; `noun-49-nonchain` already fenced the noun leg.)

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-unit-49-74-74.md` (this file).
- Queue: `battery-queue.json` — `unit-49-74-74` status `queued` → `verdict`, result `kill`, date 2026-10-09 (pre-write assert confirmed queued/verdictless; temp-file + rename; JSON re-validated post-write; only this entry's keys touched; no downgrade).
- Lock `locks/unit-49-74-74.lock`: created on start, deleted on completion.
- R5005, sealed gates, red-team adjudication queue untouched.
