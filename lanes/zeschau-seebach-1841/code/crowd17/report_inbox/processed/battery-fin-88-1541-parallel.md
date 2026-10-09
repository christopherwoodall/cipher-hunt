# Battery report: fin-88-1541-parallel

- Target id: `fin-88-1541-parallel`
- Claim: force 88's finiteness at the parallel @1541 '[62] [93] [88] le [78]' window (62='il' battery-promoted subject); a forced-finite @1541 makes the @646 finite reading frame-consistent.
- Date: 2026-10-09
- Worker: battery worker (subagent cb93f90a-7406-477d-b70f-1fb7d548d8e4)
- Stream: repaired 1,847-pair / 96-type parse re-derived in-session from `data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json` (asserts held: 1,847 pairs, 96 types). `canonical.py` never used. R5005, sealed gate instances, and the red-team adjudication queue untouched.
- Lock note: no lockfile existed at start (no stale lock). Created `code/crowd17/next-token/locks/fin-88-1541-parallel.lock` 2026-10-09T11:16:15Z; deleted on completion.

## Bar (verbatim, from battery-queue.json)

"finite-88 forced at @1541 with zero ungranted assumptions; kill iff the window forces 88 non-finite; else fence"

Numbered pass/fail clauses (pre-registered before testing, not modified after):

1. **C1:** finite-88 is FORCED at the locus — no licensed alternative reading under standing values.
2. **C2:** the forcing argument uses ZERO ungranted assumptions.
3. **Verdict rule:** promote iff C1 and C2 both pass; kill iff the window forces 88 non-finite; else NULL (fence).

Terms. A finite verb is a verb form that agrees with a subject (example: "il mange"). An infinitive is the non-finite verb form (example: "manger"). The locus is the test window. An ungranted assumption is a premise the lane has not approved.

## Method

1. Read BATTERY-PROTOCOL.md first. Created the lock on start; deleted it on completion.
2. Re-derived the repaired stream byte-exact per `code/side-keyhunt/repair_parse.py`. All @-offsets below are 0-based pair indices.
3. Adopted, never re-litigated: 62='il' (battery PROMOTE, il-62, 2026-10-08; the il-62 battery itself reads @1539's 62 as clause-initial 'il' subject, Group C), 93=verb-class (battery PROMOTE, verb-93, 2026-10-09, class-level), 88=verb-class (battery PROMOTE, governor-88-value, 2026-10-08, class-level), 77='le' (provisional), 46='que' / 00='pour' / 70='pre' (banked/granted), 06='ent' (battery promote). 78's value left OPEN (78='ver' is a red-team-fenced LEAD, R16-005 — not granted, not used). 43's class left open (feminine-noun battery NULL).

## Window-level evidence

### The locus — @1535–1547 (row a8_00)

`[1535]41 [1536]62 [1537]06 [1538]21 [1539]62 [1540]93 [1541]88 [1542]77 [1543]78 [1544]43 [1545]00 [1546]46 [1547]70`

The il-62 battery establishes a clause boundary between @1538 and @1539 (its Group C reads "…il [06] [21]. Il [93]…"). The locus clause is therefore:

**"Il [93] [88] le [78] [43]"** (@1539–@1544), followed by "pour que pre…" (@1545–@1547).

### Census facts (byte-exact, re-derived)

- n(88)=23, n(93)=14, n(62)=35, n(77)=44. Confirmed.
- "88 77 78" trigram: exactly 2x stream-wide — @646 and @1541. Confirmed.
- "62 93 88" trigram: exactly 1x stream-wide — @1539 only. The locus frame is a hapax (a one-time frame). No repetition leverage.
- 93's successor 88: x1 (@1540 only). 93's predecessor 62: x1 (@1539 only).
- "43 00 46" trigram: @1544. 43 sits at the clause tail before "pour que".

### The forcing test — form assignment for {93, 88}

Both 93 and 88 are verb-class under standing. 62='il' is the subject. A subject clause needs exactly one finite verb. The four form pairs:

1. **(93 finite, 88 finite):** ungrammatical. Two finite verbs with no clause boundary between them.
2. **(93 non-finite, 88 non-finite):** ungrammatical. The subject 'il' gets no finite verb.
3. **(93 non-finite, 88 finite):** ungrammatical. A non-finite verb between subject and finite verb has no licensed slot: no modal verb is present (French puts the modal first, "il veut manger", never "il manger veut"); a gerund needs an 'en' marker (none licensed); an appositive participle needs punctuation or agreement evidence (none); and 93=verb-class excludes adverb, clitic, or particle readings.
4. **(93 finite, 88 non-finite):** grammatical and licensed. "Il [93-fin] [88-inf] le [78]". 93 finite is distributionally supported: @1761 "15 93 06" = "[93]ent" (3pl finite-shaped); @1812 "15 93 50 42" (finite frame). 88 as governed infinitive is supported: governor-88-value L5 @1049 "[88] 29-40" (infinitive-shaped, 29='er' banked); T1 @304 "[verb] [88-inf]" reading. "[88] le [78]" is the standing transitive-governor frame (2x, @646/@1541).

Pair 4 is the only standing-licensed parse. It has 88 non-finite.

### Robustness checks

- The forcing does not use 78's value. The object slot "[77] [78]" is enough. 78 stays open.
- The forcing does not use 77's value. If 77 is not 'le', the object frame changes shape, but 88 stays non-finite in every surviving parse.
- The forcing does not use 43's role. Whether 43 closes the clause or opens the "pour que" phrase, the 93/88 form assignment is unchanged.
- No new polyvalence is declared. §7 intact: 67 et/veut stays the sole true polyvalence.
- No standing or red-team verdict is contradicted or downgraded. verb-93, governor-88-value, and il-62 are used, not overturned. The parent fin-88-645 battery keeps its NULL verdict; only one leg of its kill-check rationale is weakened (see below). No red-team A/R verdict is touched.

## Per-clause pass/fail

1. **C1 (finite-88 forced): FAIL.** Pair 4 above — "Il [93-fin] [88-inf] le [78]" — is a fully licensed alternative reading under standing values. Finite-88 is not forced.
2. **C2 (zero ungranted assumptions): FAIL.** Moot after C1. Any forcing attempt would need 93's form decided at @1540 (it is open) and 78's value (red-team fenced).
3. **Kill check: the window forces 88 non-finite — HOLDS.** Under standing values, the only grammatical parse of "Il [93] [88] le [78]" assigns 88 the non-finite (infinitive) form. Finite-88 would need 93 to be non-verbal, which contradicts the standing verb-93 class promote.

## Verdict: KILL

The @1541 window forces 88 non-finite. The claim "finite-88 forced at @1541" is false at battery grade: 62='il' is the subject of 93 (finite), and 88 is 93's infinitive complement governing "le [78]".

### Downstream consequence (not a re-verdict)

The parent battery fin-88-645 (NULL, 2026-10-09) kept the @646 finite reading "live" partly because "[88] le [78]" is "byte-real at @1541 with 62='il' as subject". This kill removes that leg: at @1541, 62='il' subjects 93, not 88. The @1541 parallel now supports 88-as-INFINITIVE, not finite-88. fin-88-645's NULL verdict stands (never downgraded); its @646 window must now stand on its own legs.

### Downstream notes (non-mandated, optional)

Kills do not mandate follow-ups. Two optional next steps, both verified ABSENT from battery-queue.json:

1. `inf88-1541-value` (P3) — name 88's infinitive value at @1541 via the "Il [93-fin] [88-inf] le [78]" frame; the "le [78]" object constrains the infinitive's transitivity.
2. `fin88-646-rerun` (P3) — re-run finiteness at @646 without the @1541 parallel leg; the @646 finite reading must stand on its own legs after this kill.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-fin-88-1541-parallel.md` (this file).
- Queue: `fin-88-1541-parallel` queued → verdict/kill, 2026-10-09 (pre-write assert passed — was queued/verdictless; temp-file + rename; JSON re-validated; own entry only; no downgrade).
- Lock `locks/fin-88-1541-parallel.lock`: created on start (no stale lock existed), deleted on completion (verified gone).
- R5005, sealed gate instances, red-team adjudication queue untouched.
