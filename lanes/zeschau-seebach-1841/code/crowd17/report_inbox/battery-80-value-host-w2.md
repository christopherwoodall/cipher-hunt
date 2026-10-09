# Battery report: 80-value-host-w2 — name 80's value at the W2 host (@1322–1323)

Worker: battery worker 80-value-host-w2 (d60fb290-deaf-4b11-a36d-66af65fa6899), 2026-10-09.
Lock: `locks/80-value-host-w2.lock` created fresh on start (no pre-existing/stale lock), deleted on completion.
Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`), re-derived in-session per `code/side-keyhunt/repair_parse.py`; asserts held (1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed gate instances, and the red-team adjudication queue untouched. All numbers trace to the stream.

Provenance: follow-up #2 of `08-leftattach-944-1323` NULL (2026-10-09). That battery fenced the 08-as-word-final-letter left-attachment route: W2's minimal host (`80 08`) needed 2 ungranted assumptions (80's value, 08's letter value) against a bar of <=1. This target tests whether naming 80's value drops that bill to 1.

Locus note: the brief says "80's value at @1323"; byte-exact, 80 is at 0-based **@1322** and 08 at @1323 (row a7_04). This battery tests 80@1322 — the W2 window of the parent.

## Bar (verbatim, pre-registered)

"80's value named at battery grade; 80 = sole unnamed cell at W2 besides 08's letter."

## Bar restated as numbered clauses (fixed before testing)

- C1: 80's value is named at battery grade at the W2 window (@1322) — a specific value with byte evidence and standing-licensed grammar, no invented values (§3).
- C2: 80 is the sole unnamed cell at W2 besides 08's letter — i.e., in the W2 host (`80 08`, extended `29 80 08`), every cell other than 80 and 08's letter value carries a standing grant, so naming 80 would drop the parent's bill to 1.

Adverses: none listed.

Standing premises adopted (§7; not re-litigated): 80 = A8 verb-frame, value OPEN, absent from registry (zero promoted values queue-wide — re-verified: 1,303-target scan, no 80 value promoted). 08 = letter-tier, letter value OPEN (`val-08-31-letter`, `syllable-08-letter-value` both still queued). 29='er' pencil GT. 03=verb-stem class (R19), scoped to the three `03 29` windows. 24 = finite/modal verb per R24 (follower @1320=03, not 85). 06='ent' promoted. 67 et/veut sole polyvalence. Adopted battery findings: modal-80 KILL (`modal-80-license`), determiner arm fenced at @1322 (`x29-80-1322-det`), 80 infinitive-shaped at @768 (`frame66-vient-80` PROMOTE), finite-80 rival fenced at @1596 (`imp-80-finite-rival-1156-1596`).

## Method

1. Read BATTERY-PROTOCOL.md first. Created the lock on start; deleted on completion.
2. Re-derived the repaired stream byte-exact in-session (1,847 pairs / 96 types asserted).
3. Byte-exact census of 80: n=17, loci [441, 469, 517, 565, 663, 673, 720, 768, 1011, 1032, 1090, 1156, 1295, 1322, 1596, 1662, 1808]; '80 08' bigram exactly x1 stream-wide (@1322–1323) — zero repetition leverage.
4. Byte-confirmed W2 (row a7_04, [1315..1331]): `62 48 98 15 24 03 29 80 | 08 62 98 | 56 30 06 62 94 70`; the `03 29 80` trigram at @1320–1322 is one of three stream-wide (@1032/@1322/@1596).
5. Tested seven naming routes for 80@1322 against standing values; counted ungranted assumptions per route.

## Window-level evidence and route tests (C1)

Local frame: `24 03 29 80 08` = [24 finite/modal] [03 verb-stem]"er" (= infinitive) [80] [08-letter].

- **Route 1 — letter-tier host "[80][08]"** (the parent's hypothesis): 80's spelling is unconstrained by any standing value (zero promoted values; '80 08' x1). Any French word spelling fits the slot. Additionally the host's right edge (08|62 boundary) has no standing license (parent finding, adopted). No value nameable. FAIL.
- **Route 2 — 80 as finite verb** ("[24][03-er][80-fin][08]"): a finite verb directly after a bare infinitive is ungrammatical in 1841 French; no subject or agreement is licensable (80 unvalued). FAIL.
- **Route 3 — 80 as imperative** (parallel to @1032 "[03]er [80]-le"): the @1032 imperative arm is conditional on the provisional 77='le' enclitic; here the follower is 08, letter-tier and word-internal per adopted `stem-08-letter-probe` — it cannot serve as an enclitic pronoun. No transfer. FAIL.
- **Route 4 — 80 as infinitive** (transfer from @768 "vient [80-inf]", adopted PROMOTE): "[03-er][80-inf]" = two bare infinitives in sequence — ungrammatical. The transfer kills the @1322 parse rather than naming a consistent value. FAIL.
- **Route 5 — 80 as modal governor**: CLOSED. `modal-80-license` KILL holds globally — zero infinitive-shaped followers in all 17 windows; @1322's follower is 08 (unvalued letter cell). FAIL.
- **Route 6 — 80 as determiner** ("[03]er [80-det] [08-N]"): fenced by adopted `x29-80-1322-det` (08 resists standalone-nominal). Not available at battery grade. FAIL.
- **Route 7 — 80 as 3pl stem** (transfer from @469/@1090 "[80]ent", 06='ent' promoted): "[03-er][80-stem]" = bare stem after an infinitive — ungrammatical; and one lexeme covering both "vient [80-inf]" (@768) and "[80]ent" 3pl would need polyvalence, barred by §7 at battery grade. FAIL.

**C1: FAIL.** No route names 80's value at battery grade at @1322. Not kill grade: every failure rests on unvalued cells (80, 08, 03's value, 24's value) — a future naming of any of them reopens the count. No standing or red-team verdict is contradicted or downgraded.

## Structural check (C2)

W2 minimal host `80 08` (@1322–1323): 80 value-open (A8 frame only), 08 letter value open — no other cells. Extended host `29 80 08`: 29='er' pencil GT. The 29|80 word boundary is licensed (an infinitive "[03]er" is a complete word for any stem value, so no ungranted assumption). **C2: PASS** — the deficit characterization is correct: naming 80's value would drop the parent's W2 bill to 08's letter value alone (1 <= 1).

## Verdict

**null** — C1 fails on all seven routes; C2 passes. 80's value is unnameable at battery grade at @1322: the modal arm is killed, the determiner arm is fenced, the imperative/infinitive/finite transfers are ungrammatical or unlicensed at this window, and the letter-tier spelling is unconstrained ('80 08' x1, zero promoted values queue-wide). The W2 fence bill stands at 2 until 80 or 08 is named elsewhere.

## Follow-ups (nulls regenerate work; all verified ABSENT from battery-queue.json, 2026-10-09)

1. **val-80-469-stem** (P3) — name 80's value at the "[80]ent" 3pl windows (@469/@1090), where promoted 06='ent' gives the tightest morphological constraint on 80 (3pl stem). Bar: name the stem with <=1 ungranted assumption; a named stem constrains 80's value globally and feeds the @1322 transfer question. Evidence: this report; `33 79 80 06` x2 @469/@1090. Adverses: §7 sole-polyvalence — battery names the stem only, no split declared.
2. **80-inf-transfer-1322** (P3) — test whether the adopted @768 "vient [80]" infinitive value transfers uniformly to the three "03 29 80" windows (@1032/@1322/@1596). Bar: one uniform infinitive parse with <=1 ungranted assumption across all three, or documented per-window ungrammaticality; battery gathers only (§7), feeding the 80-class red-team adjudication. Evidence: this report (Route 4 kill at @1322); `frame66-vient-80` PROMOTE. Adverses: none.
3. **wordint-80-08-unit** (P4) — test "80 08" @1322–1323 as one word from 80's side, independent of 08's letter value: byte-exact census of 80's right-neighbor boundary evidence across all 17 windows. Bar: state 80|08 as boundary or no-boundary on standing-licensed grounds; else fence the one-word claim with stated cause. Evidence: '80 08' x1 stream-wide (this report). Adverses: none.

## Bookkeeping

- Lock `locks/80-value-host-w2.lock` created on start (fresh, no stale lock), deleted on completion (verified below).
- Queue: `80-value-host-w2` -> `status: verdict`, `result: null`, `2026-10-09` (pre-write assert: was `queued`/verdictless; temp-file + rename; JSON re-validated from disk; own entry only; no downgrade).
- R5005, sealed gates, red-team adjudication queue untouched. Canonical-stream caveat stands (row a7_04 unvalidated).
