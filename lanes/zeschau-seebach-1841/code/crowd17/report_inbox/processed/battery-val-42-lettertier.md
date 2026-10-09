# Battery report: val-42-lettertier — verdict: NULL (no composition parses with zero new assumptions)

- Target id: `val-42-lettertier`
- Claim: letter-tier composition test: "33 42" x2 (@267/@1504) as one word, and 42 against the 29/40/33 syllabary; a composed 42 names its syllable value directly.
- Date: 2026-10-09
- Worker: battery worker (subagent dfccdefc-38a6-4e16-9c63-9b6ac9c4be60)
- Stream: repaired 1,847-pair / 96-type parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; asserts 1847/96 held in-session). `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.
- Offset note: @-offsets below are 0-based pair indices of the FIRST pair of each quoted bigram. The queue brief's "@267/@1504" are the 1-based positions of the 42 in each "33 42" bigram (0-based: 33 at @265/@1502, 42 at @266/@1503). Same loci.

Terms (ASD-STE100): "letter-tier" = sub-lexical composition (a group as part of a spelled word, not a whole word). "Syllabary" = groups with standing spelled values usable as composition pieces (29="er", 40="e" pencil ground truth). "Zero new assumptions" = every piece of the composed word has a standing (banked/granted/promoted/battery) value; no open value is named and no word is chosen by invention.

## Bar (verbatim, pre-registered before testing)

"name 42 syllable iff one composition parses with zero new assumptions"

Numbered pass/fail clauses (restated before testing, not modified after):

1. **C1:** One letter-tier composition involving 42 — "33 42" x2 as one word, or 42 composed with a member of the 29/40/33 syllabary — parses as a single French word using only standing values (zero new assumptions) AND thereby determines 42's syllable value → name the syllable.
2. **C2 (else-arm):** If no composition meets C1, the conditional claim is unproven (not falsified) → NULL with follow-ups per §4.

Adverses listed: none.

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/val-42-lettertier.lock` on start (agent dfccdefc, 2026-10-09T18:51:28Z); no prior/stale lock; deleted on completion.
2. Re-derived the repaired stream byte-exact in-session (1,847 pairs / 96 types asserted).
3. Adopted (never re-litigated) standing values per §7: pencil 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que; granted 87=ce, 64=qui, 96=par, 17=fois, 79=tout (A5), 00=pour (A9), 84=on (A15), 47=ce (A4); provisional 59=est, 77=le; battery 94=ne, 12=n, 48=e, 06=ent; 42 NOUN class (val-42-nominal PROMOTE, 2026-10-08); 33 ∈ {dire, [X]er} with 'laisser' candidate-only (laisser-unique-sweep PROMOTE names no value); orphan-1502's "on [33]" fence to 84.
4. Enumerated every 42 contact with a standing-valued neighbor and tested each as a one-word composition. 1841 diplomatic French throughout.

## Census (byte-exact, re-derived)

- "33 42": exactly **2x** — 33 at @265, @1502 (42 at 266/1503).
- "29 42": exactly **3x** — 29 at @79, @219, @1144.
- "42 33": exactly **1x** — 42 at @1503.
- 40 within ±2 pairs of any 42 window: **0** — the 40 arm of the syllabary is vacuous (no contact exists to test).
- 42's full profile: n(42)=20; predecessors {29×3, 63, 33×2, 61, 76×3, 59×2, 78, 48, 24, 74, 52, 56, 50, 22}; successors {98×3, 06×5, 16×2, 48, 63, 96, 41, 94×3, 33, 44×2}.

## Window-level composition tests

### T1 — "33 42" as one word (the claim's primary test)

- W1 @265: `84 74 45 93 52 33 [42] 06 73 47 11 06 67` = "on [74] ce [93] [52] [33] [42] ent [73] ce la ent et/veut".
- W2 @1502: `24 89 41 74 84 33 [42] 33 00 86 56` = "[24] [89] [41] [74] on [33] [42] [33] pour [86] [56]".
- **33's value is open** (33 ∈ {dire, [X]er}; 'laisser' unratified). Identifying any one-word "33"+"42" spelling requires naming 33's value first — a new assumption by definition. The bar's zero-assumption condition fails at the first step.
- Even arguendo with 33='dire' (battery read, unratified, adopted only for the negative test): "dire"+"[42]" yields no French word ("direct" is di-rect, not "dire"+"ct"; no "dire"+syllable word exists). W2 additionally forces the composed word into a finite-verb slot ("on" + __, per orphan-1502's 84-fence): no "dire"+X finite verb exists in French.
- Even arguendo with 33=[X]er stem ("laiss-"): "laiss"+"[42]" as one word needs 42 to complete a word ("laisse" needs "se", "laisser" needs "ser") — naming both 33's stem and 42's piece, two unknowns, zero forced.
- **T1: FAIL.**

### T2 — "29 42" = "er"+"[42]" (29="er" pencil ground truth; zero-assumption eligible)

- @79: `11 29 [42] 98` = "la er [42] [98]". @219: `46 29 [42] 16` = "que er [42] [16]". @1144: `16 29 [42] 98` = "[16] er [42] [98]".
- French 2-syllable "er"+X words: erreur, ermite, errer, ergot. @79 ("la" + noun) admits "l'erreur"/"l'ermite" (with elision, and 98='vient' is LEAD-only — a further assumption). @219 ("que" + __) admits NONE: "que"+"erreur"/"ermite" ungrammatical (determiner missing), "que"+"errer" ungrammatical. No single word parses all three windows; selecting any word invents data. Reading different words per window is a split declaration — §7 red-team venue, not battery-actable.
- **T2: FAIL.**

### T3 — 40 arm of the syllabary

- 40 never occurs within ±2 of 42 on the stream. No composition exists to test.
- **T3: vacuous — FAIL (no test possible).**

### T4 — "42 33" @1503 as "[42]dire" (completeness; 33 open)

- Window: `84 33 [42] 33 00` = "on [33] [42] [33] pour". Candidate "redire" (42="re"): "on dire redire pour" — "on"+infinitive "dire" ungrammatical (orphan-1502 fenced "on [33]" to 84). The composition cannot rescue the window.
- **T4: FAIL.**

### T5/T6 — excluded by standing verdicts (not re-tested)

- "42 06" x5 (06="ent" battery): the verb-stem contact — noun/verb-stem polyvalence ESCALATED to the red team per §7 (stem-42-verb). Battery may not name a syllable here (venue).
- "42 94" x3 (94="ne" battery): "[42]ne" composition KILLED (adopted, 2026-10-09). Not re-litigated.
- "42 48" @282 (48="e" battery): "[42]e" word choice would be invented (any feminine "[X]e"); owned by queued `val-42-282-fem`. Deferred to that target, not tested here.

## Per-clause results

- **C1: FAIL.** No composition parses with zero new assumptions: T1 needs 33's open value; T2 has no uniform word and any word choice is invented; T3 is vacuous; T4 fails window grammar; T5/T6 are venue/killed/deferred.
- **C2: FIRES.** The conditional claim ("a composed 42 names its syllable value directly") is unproven, not falsified — no window forces it false. The bar carries no kill arm, and none is imported.

## Verdict: NULL

## Scope (stated, not hidden)

- 42's NOUN class (val-42-nominal PROMOTE) untouched; no class claim made.
- The 42-06 verb-stem contact and its §7 escalation untouched (red-team venue).
- The "[42]ne" kill untouched. No standing or red-team verdict contradicted, downgraded, or re-litigated. §7 intact.
- This battery does not name any value for 42, 33, or any neighbor.

## Follow-ups proposed (all verified ABSENT from battery-queue.json; left for supervisor)

1. `syll-42-wordedge` (P4) — word-edge census for 42: test whether 42 ever sits at a licensed word boundary vs always word-internal; distinguishes noun-word 42 from syllable-42 distributionally without naming values.
2. `val-42-219-queframe` (P3) — @219 "que [X]er [42]": the "que" frame forces a verb before 42; test "29 42" as verb+"42-standalone" vs one word, with the verb identified from 29's left context (no invented word).
3. `redteam-42-tier-input` (P2, gather-only) — package the letter-tier results (42-06 escalated, 42-94 killed, 29/33 compositions fail at battery grade, 40 vacuous, 42-48 deferred to val-42-282-fem) as red-team input for 42's tier adjudication.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-val-42-lettertier.md` (this file).
- Queue: `val-42-lettertier` queued → `verdict`/`null`, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `code/crowd17/next-token/locks/val-42-lettertier.lock` created on start, deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
