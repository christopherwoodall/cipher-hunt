# Battery verdict: pre-00-frame-census

- Target: `pre-00-frame-census` (battery-queue.json, priority 3, status queued)
- Claim: "census all 55 'X 00' windows against the licensed French 'X pour' frames; fence the ungrammatical ones"
- Date: 2026-10-09
- Worker: ad35aa7d-8ac0-4ece-a076-bcabdb641858

## Bar (verbatim, pre-registered)

"For each of the 25 distinct X predecessors of 00: license the 'X pour' frame with a French grammatical frame (verb/noun/adjective/'c'est'/'voilà'/adverb + 'pour + inf', or clause boundary), or fence the window as ungrammatical-as-written (re-segmentation or non-'pour' 00 reading). Pay special attention to 'la pour' (11 00 x4), '-ent pour' (06 00 x4), 'par pour' (96 00 x3)."

Numbered clauses:
- C1: All 55 'X 00' windows (25 distinct X) rendered with byte-exact context on the repaired stream.
- C2: Each X adjudicated: LICENSED (a French grammatical 'X pour' frame exists) or FENCED (ungrammatical-as-written, with stated cause; or unresolvable pending an open cell, with the blocker named).
- C3: The three flagged anomalies ('la pour' x4, '-ent pour' x4, 'par pour' x3) receive explicit rulings.
- C4: Adverse answered: 00='pour' is leg-1 class-level (A9), not uniform — non-'pour' readings noted as live rescue paths at fenced windows.

## Method

Re-derived the repaired 1,847-pair / 96-type stream in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` (asserts: 1,847 pairs, 96 types — held). `canonical.py` never used. Enumerated all 55 'X 00' bigrams with ±3 context, grouped by the 25 distinct X. Standing values from the table registry (50/96). French frame judgments against 1841 diplomatic French (preposition 'pour' + infinitive / + noun / 'pour que' + subjunctive).

## Findings — per-X adjudication (all 25)

### LICENSED (10 distinct X, 22 windows)

- **X=06 'ent' x4 — LICENSED.** The '-ent pour' anomaly DISSOLVES: 06='ent' (promoted) is a 3pl verb ending, hence word-final. The frame is '[V]ent pour …', not 'ent pour'. @184 '[V]ent pour [33-INF]', @544 '[V]ent pour que [24-verb]' ('pour que' + subjunctive frame), @666 '[V]ent pour [20]', @738 '[V]ent pour [36-noun]' ('pour' + noun). All four grammatical.
- **X=63 verb x4 — LICENSED.** Verb + 'pour' at all four (@252, @713, @1107, @1531). Followers (66) are a separate question, not the X-00 contact.
- **X=43 noun x3 — LICENSED.** Noun + 'pour'. @1126 '[N] pour [86-INF]', @1544 '[N] pour que', @244 '[N] pour [66]'.
- **X=26 noun x3 — LICENSED.** Noun + 'pour [33-INF]' at all three (@406, @934, @1628).
- **X=98 verb x3 — LICENSED.** Verb + 'pour' at contact. @1373 '[V] pour [86-INF]'; @1137/@1601 followers open but contact licensed.
- **X=93 verb x1 — LICENSED.** @479 '[ce] [93-verb] pour [13]'.
- **X=46 'que' x1 — LICENSED.** @865 'ce que pour [86-INF]' — conjunction 'que' + purpose clause ('Il dit que pour réussir il faut…'). Grammatical.
- **X=68 noun x1 — LICENSED.** @1286 '[68-noun] pour la [17-fois]' — noun + 'pour' at contact.
- **X=24 verb x1 — LICENSED.** @1492 '[à] [24-verb] pour [66]'.
- **X=02 (split) — @1152 LICENSED.** 'on [02] pour [92]' with 02=finite verb per the val-02-1153 PROMOTE (this wave). @887 fenced unresolvable (02's tier open there).

### FENCED — ungrammatical-as-written (3 distinct X, 8 windows)

- **X=11 'la' x4 — FENCED.** 'la pour' is ungrammatical: 'la' (article or object clitic) cannot precede 'pour' in any French frame. @75 'ce la pour la er', @726 'qui la pour [86-INF]', @1243 'ce la pour [33-INF]', @1404 'ce la pour la…'. Rescue paths (both unlicensed, noted not adopted): (a) '87 11'='cela' composition for @75/@1243/@1404 ('cela pour' IS grammatical: 'Il a fait cela pour vous aider') — but the standing 'cela' finding is locus-level '69 11' (R19-108/R20-135), not '87 11'; (b) non-'pour' 00 reading (A9 leg-1). @726 ('qui la pour') has no 'cela' rescue — strongest anomaly.
- **X=96 'par' x3 — FENCED.** 'par pour' — two prepositions in sequence; no French frame licenses it. @47 'par pour [92-verb]', @465 'par pour [33-INF]', @960 'par pour [86-INF]'. Rescue: non-'pour' 00 reading or re-segmentation.
- **X=48 'e' x1 — FENCED.** @377 'm e pour la' — letter 'e' (val-48-initial NULL: 48 letter-tier everywhere) or 'me' (82+48) before 'pour'; neither composes. Ungrammatical-as-written.

### FENCED — unresolvable pending open cell (12 distinct X, 25 windows)

X is class/value-open, so the frame can be neither licensed nor killed at battery grade. Blocker named per X:
- X=16 x4 (@187, @659, @844, @1246) — 16 open.
- X=81 x3 (@26, @551, @1086) — 81 open.
- X=28 x3 (@105, @286, @747) — 28 open. Note @747 '[85] [28] pour qui' — 'pour qui' is a licensed frame shape once 28 resolves.
- X=44 x3 (@1311, @1583, @1679) — 44 open. Note @1679 'le [44] pour que' — licensed shape if 44 is nominal.
- X=09 x2 (@0, @591) — 09 split-shaped; pending the 09 nominal/adverbial split resolution (red-team venue).
- X=19 x2 (@328, @1821) — 19 open.
- X=33 x2 (@1000, @1504) — 33 is verb-STEM (A10); a bare stem cannot precede 'pour' — needs a completion neighbor. Incomplete, not ungrammatical.
- X=03 x1 (@1790) — 03 bare verb-stem ('ce [03] pour [86-INF]'); needs its '29' completion per the conditioned '03 29' scope.
- X=14 x1 (@586), X=07 x1 (@681), X=01 x1 (@976), X=97 x1 (@1823) — open.
- X=02 @887 x1 — 02's tier open at this window (the @1152 finite-verb promote is locus-level).

### Tally

22 licensed + 8 fenced-ungrammatical + 25 fenced-unresolvable = 55 windows, 25 distinct X. All clauses pass.

## Per-clause verdict

- C1 (full census, byte-exact): PASS — 55/55 windows, 25/25 X.
- C2 (each X licensed or fenced with cause): PASS — 10 X licensed, 3 X fenced-ungrammatical, 12 X fenced-unresolvable with blockers named.
- C3 (three flagged anomalies ruled): PASS — 'la pour' x4 FENCED (real anomaly, strongest at @726); '-ent pour' x4 LICENSED (anomaly dissolves — 06 word-final); 'par pour' x3 FENCED (real anomaly).
- C4 (adverse answered): PASS — non-'pour' 00 readings noted as live rescue at all 8 ungrammatical windows (A9 leg-1 class-level, not uniform).

## Verdict: PROMOTE

The census is complete and decisive. Headline results: (1) the 'la pour' x4 anomaly is REAL — 'la' cannot precede 'pour', and @726 ('qui la pour') has no compositional rescue; (2) the '-ent pour' x4 anomaly DISSOLVES — 06 is a word-final 3pl ending, the frame is '[V]ent pour'; (3) 'par pour' x3 is REAL — no French frame; (4) 'pour' is confirmed as overwhelmingly preposition-before-infinitive (86/33 INF followers dominate), which is what makes the predecessor census discriminating.

## Scope

Census only. No value named, no class changed, no split declared. The 8 ungrammatical windows are fenced as windows, not as claims about 00's global value. The 25 unresolvable windows re-open when their X cells resolve. No standing or red-team verdict contradicted, downgraded, or re-litigated; §7 intact. Canonical-stream caveat stands (68 of 70 row offsets unvalidated).

Natural next targets for the supervisor (not formal follow-ups — this is a promote): '87 11'='cela' composition test (rescues 3 of the 4 'la pour' windows); non-'pour' 00 readings at the 8 fenced windows; 28/44 resolution (both sit in licensed 'pour qui' / 'pour que' shapes).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-pre-00-frame-census.md` (this file)
- Queue: `pre-00-frame-census` queued → `verdict`/`promote` 2026-10-09 (pre-write assert passed — was queued/verdictless; target-id-unique tmp `battery-queue.json.pre-00-frame-census.tmp` + rename; JSON re-validated from disk; own entry only; no downgrade)
- Lock `locks/pre-00-frame-census.lock`: created on start (2026-10-09T19:29:08Z, no stale lock), deleted on completion (verified gone)
- R5005, sealed gates, red-team adjudication queue untouched
