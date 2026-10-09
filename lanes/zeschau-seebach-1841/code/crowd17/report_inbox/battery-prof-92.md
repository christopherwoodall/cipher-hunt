# Battery report: prof-92 — 92's class profile (n=22)

- Target id: `prof-92`
- Claim: "92's class profile (n=22): '00 92' x6, 92->64 x2 — decides npframe-60-1674's budget blocker"
- Date: 2026-10-09
- Worker: battery worker (subagent 3c5e070c-e0db-4b85-9c2c-9a0e439a820a)
- Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed like `code/side-keyhunt/repair_parse.py`; n=1847 asserted, 96 groups asserted).
  All @-offsets are 0-based repaired-stream indices. n(92) = 22 re-derived in-session:
  @49, @66, @203, @321, @330, @354, @356, @593, @683, @901, @978, @1022, @1154, @1218, @1310, @1361, @1379, @1453, @1490, @1550, @1607, @1673.
- Lock: `code/crowd17/next-token/locks/prof-92.lock` (created at start, deleted at end; no prior lock existed).
- `canonical.py` never used. R5005, sealed gates, red-team adjudication queue untouched.

## Bar (verbatim, pre-registered before testing)

"name 92's class with >=3 windows parsing under it with zero forced contradiction; result unblocks npframe-60-1674's budget (budget failure was 92-class, not value contradiction)"

Numbered pass/fail clauses (restated before testing, not modified after):

1. (C1) ≥3 windows parse with 92 in the named class (frame-level parse under the class counts; a window is a leg iff the class assignment yields grammatical 1841 French at the contact, using only banked/granted/promoted/provisional values).
2. (C2) Zero forced contradiction: no window forces 92≠named-class globally (window-local failures under the class are fenced with stated cause; a forced local failure is not a global contradiction iff the subset-scoped registry account covers it).
3. (C3) The result states the consequence for npframe-60-1674's budget blocker (unblocked vs still blocked, with cause).
4. (C4) Adverses answered: coordinated with verb-92-subset (PROMOTE, 2026-10-08 — adopted as premise, not re-run); seg-61-94-word-adjudicate (about 61-94, not 92 — not duplicated); §7 sole-polyvalence — no polyvalence declared at battery level.

## Standing values spent

- 00="pour" (granted, A9 class-level), 64="qui" (banked GT), 46="que" (banked GT),
  94="ne" (STRONG LEAD R17-001), 29="er"/40="e" (banked letters), 82="m" (banked letter),
  77="le" (provisional), 98="vient" (promoted), 84="on" (promoted, conditions C1–C3),
  69="noun class" (battery-promote), 63="verb class" (battery-promote),
  79="tout" (granted A5), 47="ce" (A4), 11="la" (banked GT).
- Registry (red-team Round 18, ratified): **92 = verb class, subset-scoped**. Not re-litigated; this battery tests whether the stream sustains it.

## Method

1. Re-derived the repaired 1,847-pair parse in-session; enumerated all 22 windows of 92 with ±4 context.
2. Predecessor census: 00 x6 (@49,@330,@593,@683,@978,@1154), 11 x3 (@203,@321,@1607),
   94 x2 (@66,@1550), 84 x2 (@1022,@1379), and 40/98/16/83/30/13/31/46/81 x1 each.
3. Successor census: 79 x2 (@49,@593), 69 x2 (@66,@1379), 64 x2 (@683,@1022),
   60 x2 (@321,@1673), 62 x2 (@1361,@1453), and 63/98/47/50/67/07/29/61/44/39/45/65 x1 each.
4. Tested each window under 92=verb (infinitive, finite) and 92=nominal against standing values only.

## Window-level evidence

### Verb arm — infinitive ("pour [92]" x6, all clean)

- **@49** (a1_01): "00 92 79" = "pour [92] tout" — "pour [INF] tout [37]": "pour dire tout"-shaped. Clean. (a1_01 is phase-uncertain soil; leg holds on the canonical stream per protocol.)
- **@330** (a2_05): "00 92 50" = "pour [92] [50]" — infinitive frame clean; tail depends on 50's open value.
- **@593** (a4_00): "00 92 79" = "pour [92] tout" — same shape as @49. Clean.
- **@683** (a5_00): "00 92 64" = "pour [92] qui" — under infinitive: "pour [INF] qui" is ungrammatical; this window forces the nominal subset (see below). Not an infinitive leg — fenced to the subset.
- **@978** (a6_01): "00 92 07" = "pour [92] [07]" — infinitive frame clean.
- **@1154** (a6_09): "00 92 29" = "pour [92]er [80]" — 92+29 = "[92]er": the infinitive ending attaches to 92 directly. **Verb-STEM leg** — strongest morphological evidence in the profile: 92 supplies the stem, 29 the "-er". Parallels the granted 85 verb-stem frame (A3).

Infinitive legs: @49, @330, @593, @978, @1154 = **5 windows** (bar needs ≥3; passed before finite legs are even needed).

### Verb arm — finite (supporting legs)

- **@1379** (a7_06): "84 92 69" = "on [92] [69-noun]" — "on [V] [N]" clean SVO (84="on" provisional).
- **@66** (a1_01): "94 92 69" = "ne [92] [69-noun]" — subjectless "ne [V]" under the standing W1 "ne mentent" precedent (battery-grade, 2026-10-09).
- **@1550** (a8_00): "94 92 45" = "ne [92] ce [23]" — "ne [V] ce [N]"-shaped; conditional on 23's class, recorded as a leg with stated cost.
- **@1607** (a8_02): "11 92 65" = "la [92] [65-noun]" — object-clitic "la" + finite 92 + noun object ("la [V] [65]") parses; nominal rival would need bare N-N juxtaposition (ungrammatical). Verb-preferred.

### Nominal subset (the R18 subset-scoping — evidence, not a rival class)

- **@683** (a5_00): "00 92 64" = "pour [92] qui" — "qui" (banked GT) needs a nominal antecedent; "pour [INF] qui" is ungrammatical. **92 is nominal at this window.** This is the registry's subset-scoping in the flesh, not a contradiction of the verb class.
- **@203** (a2_00): "11 92 63" = "la [92] [63-verb]" — "la [92-N] [63-V]": determiner + subject noun + finite verb ("la femme parle"-shaped). Clean nominal leg.
- @1218 (a7_00): "83 92 61" = "[83] [92] [61]" — nominal-compatible ("de [N]", under the 83="de" lead) but tied with the infinitive reading; not counted as a leg.

Nominal-subset legs: **2 windows** (@683, @203).

### Fenced windows (stated cause, no contradiction)

- **@1022** (a6_03): "84 92 64" = "on [92] qui" — nominal needs a verb after "on"; verbal can't host "qui". Fenced both arms.
- **@1673** (a8_05): "81 92 60" = "[81] [92] [60]" — nominal needs N-N juxtaposition; verbal needs V-V adjacency. Fenced both arms (adopts npframe-60-1674's fence, not re-run).
- **@354/@356** (a2_06): "40 92 98 92 47" — first 92 parses nominal-subject ("[92-N] vient"), second 92 fenced ("vient [92] ce" ungrammatical under both). Window-local, not global.
- **@1310** (a7_04): "30 92 44" = "pas [92] [44]" — "pas [V]" order needs "ne"; ne-drop doesn't rescue the order. Fenced.
- **@901** (a5_09): "16 92 67" — 16 open; no licensed parse under either arm. Fenced.
- **@321** (a2_04): "11 92 60" = "la [92] [60]" — 60's split keeps both arms conditional; fenced to 60's class.
- **@1361** (a7_06): "13 92 62" = "[13] [92] il" — inversion shape conditional on 13's class. Fenced.
- **@1453** (a7_09): "46 92 62" = "que [92] il" — literary inversion possible; conditional, not counted.
- **@1490** (a7_10): "31 92 39" — conditional on 39/24's open classes. Fenced.

## Per-clause pass/fail

1. **C1 — PASS.** 92=verb class: 5 clean infinitive legs (@49,@330,@593,@978,@1154) + supporting finite legs (@1379,@66,@1550,@1607). The bar's ≥3 is exceeded on the infinitive subset alone.
2. **C2 — PASS.** Zero forced contradiction: no window forces 92≠verb globally. The two nominal windows (@683,@203) are window-local and covered by the ratified "subset-scoped" account — the registry already names the mechanism. @1022/@1673 fail under both arms (fences, not contradictions).
3. **C3 — answered.** npframe-60-1674's budget is **NOT unblocked**: the budget failure was specifically "92 nominal as 1 unstated assumption" at @1673, and the nominal subset has only **2 legs** (@683,@203) — below the battery's own ≥3 standard. The dominant account is verb class (subset-scoped); a nominal-92 assumption at @1673 remains unstated evidence, so the fence stands until a third nominal leg lands. Follow-up proposed below.
4. **C4 — PASS.** verb-92-subset's PROMOTE (2026-10-08, verbal-governor subset) adopted as premise — consistent, not duplicated. seg-61-94-word-adjudicate concerns 61-94, untouched. No polyvalence declared (§7 intact — the subset-scoping is the red-team-ratified account, not a new declaration).

## Verdict: PROMOTE (finding grade, battery-grade)

92 = verb class, subset-scoped — confirmed at battery grade, consistent with the red-team Round-18 ratification. No standing or red-team verdict contradicted or downgraded.

**Strongest new evidence:** @1154's "pour [92]er" — 92 supplies a verb stem to which banked 29="er" attaches, paralleling the granted A3 85 verb-stem frame.

**Docket consequence:** the nominal subset (2 legs) is real but under-evidenced; npframe-60-1674's budget assumption stays unstated.

## Follow-ups proposed (for supervisor queuing)

1. `nom-92-third-leg` (P3) — hunt a third nominal-92 leg (candidates: @1218 "de [92]" if 83="de" promotes; @356's second 92 if "vient [92] ce" can be licensed; re-test @901 if 16's value lands). Promote would unblock npframe-60-1674's budget; kill of the hunt fences the budget permanently.
2. `verb-92-impframe` (P4) — test whether any 92 window (esp. @1379 "on [92] [69]") admits an imperative frame; would extend the verb class beyond infinitive/finite-declarative.

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-prof-92.md`
- Queue: `battery-queue.json` → `prof-92` status `verdict`, result `promote`, date 2026-10-09 (temp-file + rename; pre-write assert passed — was queued/verdictless; JSON re-validated; own entry only; no downgrade)
- Lock created at start, deleted on completion. R5005, sealed gates, red-team adjudication queue untouched.
