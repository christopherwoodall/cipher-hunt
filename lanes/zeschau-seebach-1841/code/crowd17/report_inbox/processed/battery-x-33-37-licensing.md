# Battery report: x-33-37-licensing

- Target id: `x-33-37-licensing`
- Claim: decide how 37 licenses the bare infinitive at the @625-626 hapax (37-33 adjacency; 37's only 33-follower in 28 occurrences)
- Date: 2026-10-09
- Worker: battery worker (subagent cb705043-eef8-45c0-8be5-f0bdcda7c541)
- Stream: repaired 1,847-pair parse (`data/upstream-ct_R5005.txt` + `code/side-keyhunt/repaired_offsets.json`, parsed per `code/side-keyhunt/repair_parse.py`; 1,847 pairs / 96 types re-derived in-session, asserts held). `canonical.py` never used. R5005, sealed gate instances, and the red-team adjudication queue untouched.

## Bar (verbatim, pre-registered before testing)

"name the licensing mechanism (predicative-with-bare-infinitive, 37 non-predicative here, or boundary re-segmentation) with the window parsing under standing values + <=1 stated assumption"

Numbered pass/fail clauses (restated before testing, not modified after):

- **C1:** The @625-626 window is byte-confirmed on the repaired stream; "37 33" is 37's sole 33-follower in n(37)=28.
- **C2:** Exactly one of the three named mechanisms — (a) predicative-with-bare-infinitive, (b) 37 non-predicative here, (c) boundary re-segmentation — yields a grammatical 1841-French parse of the window under standing values + <=1 stated assumption. The other two fail with stated cause.

Verdict rule: **promote** the mechanism iff C1 and C2 pass (one mechanism parses within budget, others dead with cause). **null** iff no mechanism parses or two tie (with 1-3 follow-ups). No kill grade applies (the claim is a decision question, not a falsifiable value).

## Method

1. Read BATTERY-PROTOCOL.md first. Created `code/crowd17/next-token/locks/x-33-37-licensing.lock` on start (agent id + 2026-10-09T10:45:00Z); no prior/stale lock; deleted on completion.
2. Re-derived the repaired stream in-session. Census: n(37)=28, n(33)=25; "37->33" adjacency exactly 1x (@625); "33 29" bigram 5x (@273/@626/@1232/@1424/@1477).
3. Standing values used: pencil 11=la, 70=pre, 82=m, 34=i, 29=er, 40=e, 46=que; granted 87=ce, 64=qui, 96=par, 17=fois, 79="tout" (A5), 00="pour" (A9), 84="on" (A15), 47="ce" (A4); provisional 59=est, 77="le"; A1 (37/32/42 predicative frames, value open), A10 (33+29 stem/whole HOLD), 67 et/veut positional rule (sole polyvalence, §7).
4. Adopted (not re-litigated): erstem-33-id (null, 2026-10-08): 33 is an -er verb stem, X='laisser' at LEAD strength (conditional on 16/85 as infinitives); at @626 it parsed "[37] laisser ce [78]" as transitive but left "Governor 37 open" — the exact question this battery answers.
5. Corpus checks for French licensing ran against `code/side-period/corpus/` (1841 texts) and the 27.66M-char prose set (`data/gutenberg-*.txt`).

## Window-level evidence (@-offsets, 0-based repaired stream)

**Locus:** 0b@625=37, 0b@626=33, row a4_01 mid-row. ±7 window (0b@618-632):

`29(er) 88 [37] 76 82(m) 14 59(est) [37] [33] 29(er) 87(ce) 78 67 08 52`

Relevant slice 0b@624-629: `59 37 33 29 87 78` = "est [37] [33]er ce [78]".

**C1: PASS.** "37 33" is byte-confirmed at 0b@625-626 and occurs exactly once stream-wide (37's only 33-follower in 28 occurrences; "33 37" occurs 0x).

**Distributional facts bearing on 37's role:**
- "59 37" ("est [37]") occurs 6x: @529/@625/@913/@1179/@1444/@1797.
- @529: `59 37 64 26` = "est [37] qui [26]"; @1444: `59 37 64 77` = "est [37] qui…". The cleft "c'est [NP] qui [VP]" requires a nominal — *"c'est [adj] qui"* is ungrammatical. So 37 has a live **nominal arm** (2/6 "est 37" windows force it).
- 78's left profile (n=31): {77='le' x7, 47='ce' x5, 37 x4, 67 x4, 11='la' x2, 87='ce' x2} — 78 follows determiners/demonstratives, i.e. 78 is nominal-class (consistent with the standing 78='ver' LEAD, R16-005 unsettled, not used here).
- "87 78" ("ce [78]") occurs 2x stream-wide: @572 and @628 (the locus).

**The five "33 29" ([33]er infinitive) windows:** @273/@1424/@1477 are governed by 67="veut" (positional rule, follower infinitive-shaped); @1232 "ce [33]er" (47-governor); @626 is the ONLY one with no modal/prepositional governor — the hapax this battery resolves.

## Mechanism tests

### (a) predicative-with-bare-infinitive — FAIL (no French license)

For (a) to work, 37 must be predicative AND some predicative must license a bare infinitive: "il est [37-pred] [33]er".

Corpus test (1841 French, side-period corpus + 27.66M-char prose): searched `est [predicative-adjective] [infinitive]` with no intervening preposition across a 30-adjective predicative set (bon/beau/facile/difficile/possible/nécessaire/temps/mieux/…) — **zero genuine hits**. Every predicative+infinitive in the corpus intervenes "de" or "à" ("c'est de faire", "il est à croire", "c'est à dire"); the only bare-looking hits are adverbial ("C'est assez dire", "assez" = adverb) or pronominal ("c'est vous dire", "c'est la faire"). French predicatives categorically require "de"/"à" before an infinitive complement. There is no predicative in 1841 French licensing a bare infinitive, so (a) cannot parse the window under any value of 37. **(a) is dead at the grammar level, zero assumptions needed to kill it.**

### (c) boundary re-segmentation — FAIL (no viable re-segmentation)

- "37 33" as one word + 29='er': yields "est [X-er]" = "est [infinitive]" — *"c'est partir"* is ungrammatical. Dead.
- 33 word-internal ("37[33]er" one word, e.g. "entendre"-shaped): same "est [inf]" death. Dead.
- "33"+"29" split as "33" + word-initial "er": "er" is not a French word (29 is word-initial elsewhere only inside the "[29 40 65]" unit per left-64-29-boundary). Dead.
- 37 attaching left ("59 37" one word): changes nothing about the infinitive's licensing. Moot.
**No re-segmentation produces a grammatical parse. (c) dead.**

### (b) 37 non-predicative here — PASS (1 stated assumption)

- **Stated assumption (the one):** 37 = nominal at @625, grounded in the "est 37 qui" clefts (@529/@1444) which force 37's nominal arm distributionally.
- Parse: "…82(m)' 14 59(est) [37-N]. [33]er ce [78-N]!" — i.e. "…m' [14] est [37-N]. [33]er (= -er infinitive, 'laisser'-lead per erstem-33-id) ce [78-N]!"
- The infinitive is **not licensed by 37 at all**: "est [37-N]" is a complete clause, and "[33]er ce [78]" is an independent **exclamatory/instruction infinitive** ("Laisser ce [78]!" = "Leave this [78] (alone)!"), the standard infinitif de consigne which takes direct objects freely.
- License evidence: corpus attests "laisser ce costume", "laisser ce drame" ("laisser ce + N" is natural 1841 French); the lane's own @1029 promote ("Ceci, [03]er!") establishes the exclamatory infinitive as a live construction. The 7-level demonstrative-head fence does NOT apply here — "ce" (87) is the infinitive's direct object ("laisser ce [78]"), not a dislocated topic.
- "ce [78]" = determiner + noun: 87='ce' granted, 78 nominal-class per its determiner-follower distribution (0 new assumptions).
- 67='et' (positional rule: follower 08 not infinitive-shaped), so "…ce [78] et [08] [52]…" continues the clause normally.
- Assumption audit: 37 nominal (1 stated); 59='est' provisional standing (0); 33 verb stem per A10 HOLD (0); 29='er' GT (0); 87='ce' granted (0); 78 nominal per distribution (0); exclamatory infinitive = licensed construction (0); clause boundary between @625/@626 is inherent to the mechanism (no punctuation survives in the cipher). **Total: 1 stated assumption — within budget.**
- Robustness note: the infinitive's licensing is independent of 37's exact class — even a predicative 37 ("est [37-pred]. [33]er!") would leave the infinitive self-licensed. The nominal reading is preferred because the clefts positively evidence it.

## Per-clause pass/fail

- **C1: PASS** — locus byte-confirmed; "37 33" hapax in n(37)=28.
- **C2: PASS** — (a) dead (no predicative licenses bare infinitive; corpus zero), (c) dead (no viable re-segmentation), (b) parses with exactly 1 stated assumption.

## Verdict: PROMOTE (mechanism (b), parse-level)

**Decision:** 37 does **not** license the bare infinitive. At @625-626, 37 is non-predicative (nominal, per the "est 37 qui" cleft distribution); "est [37-N]" closes its clause, and "[33]er ce [78-N]" is an independent exclamatory/instruction infinitive ("Laisser ce [78]!"). The erstem-33-id "Governor 37 open" is thus closed: there is no governor — the infinitive is self-licensed. Scope: parse-level promote only; no value or class is named (33's value stays at 'laisser'-lead; 37's global class stays split per §7 — this battery names 37's role at @625 only, it does not adjudicate the 37 predicative/nominal split).

No standing or red-team verdict contradicted or downgraded; §7 intact (no new polyvalence; 67="et" here follows the positional rule). Canonical-stream caveat stands (row a4_01 offset unvalidated).

## Bookkeeping

- Report: `code/crowd17/report_inbox/battery-x-33-37-licensing.md` (this file).
- Queue: `x-33-37-licensing` queued → `verdict`/`promote` via temp-file + rename (pre-write assert confirmed queued/verdictless; JSON re-validated post-write; own entry only).
- Lock `locks/x-33-37-licensing.lock`: created on start, deleted on completion.
