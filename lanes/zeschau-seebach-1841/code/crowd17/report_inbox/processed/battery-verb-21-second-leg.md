# Battery report: verb-21-second-leg — verdict: KILL

- Target id: `verb-21-second-leg`
- Claim: "find a second verb-frame 21 window (\"qui 21\" or finite-frame) to battery-grade the @134 verb arm, or re-parse \"64 21\" wordhood"
- Date: 2026-10-09
- Worker: battery worker (subagent b2617101-cbc0-4941-9f56-b4a66e23d2e8)
- Stream: repaired 1,847-pair parse (code/side-keyhunt/repaired_offsets.json +
  data/upstream-ct_R5005.txt, parsed per code/side-keyhunt/repair_parse.py;
  asserts held in-work: 1,847 pairs, 96 types, n(21)=30). `canonical.py`
  never used. R5005, sealed gates, red-team adjudication queue untouched.
  All @-offsets are 0-based repaired-stream pair indices.
- Lock: code/crowd17/next-token/locks/verb-21-second-leg.lock (created at
  start, 2026-10-09T17:57:15Z, agent id + timestamp; no prior lock existed).

## Bar (verbatim, pre-registered before testing)

"pass iff a second verb-frame 21 window is found, or \"64 21\" re-parses as
word-internal; else fence 21's verb tension as unfounded"

Numbered pass/fail clauses (restated before testing, not modified after):

1. (C1) A second verb-frame 21 window is found: a second "qui 21" bigram
   anywhere in the repaired stream, OR a finite-frame window where 21 is
   forced into a verb slot (a verb-forcing governor immediately left of 21).
2. (C2) "64 21" @133–134 re-parses as word-internal: 21 sits word-internal
   to a 64-led word, dissolving the "qui [21]" verb-forcing geometry.
3. (C3) If C1 and C2 both fail, fence 21's verb tension as unfounded.

## Method

1. Re-derived the repaired stream in-session; asserts held (1,847 pairs,
   96 types, n(21)=30).
2. Enumerated all 30 windows of 21 with ±4 context and tabulated the
   immediate governor (left neighbor) of each.
3. Bigram census over the full stream: n("64 21") and n("21 64").
4. Contact census of 64=qui: all 47 windows of 64, testing for any
   word-internal precedent for a 64-led word.
5. Checked the two apparent verb-contact windows (@719 "21 80", @1172
   "83 21 85") against the granted frame definitions (A8 80/89 verb-frames;
   A3 85 verb-stem `que [85]er`) to see whether either forces 21 into a
   verb slot.

## Window-level evidence

### C1 — "qui 21" bigram census

- n("64 21") = **1** in the whole 1,847-pair stream: @133–134 only
  (a1_04: `…32 96 56 [64] [21] 65 23 91 65…`).
- n("21 64") = 2: @937 and @1631, both `33 21 64` — 21 as nominal
  antecedent of the relative pronoun (noun legs, val-08 C4). Not "qui 21".

### C1 — governor census: all 30 windows of 21, left neighbor

| @ | left | window | governor class |
|---|---|---|---|
| 99 | 08 | `85 08 [21] 62` | neutral (val-08: not discriminating) |
| 109 | 11 | `00 46 11 [21] 67` | la — noun |
| 115 | 68 | `89 68 [21] 67` | neutral |
| 118 | 14 | `67 14 [21] 60` | neutral |
| **134** | **64** | `56 64 [21] 65` | **qui — verb-forcing (the single leg)** |
| 171 | 48 | `53 12 48 [21] 60` | "donne X" F1 — noun object |
| 176 | 86 | `09 87 86 [21] 69` | neutral (residual, suite-21-residuals owns) |
| 196 | 01 | `56 47 01 [21] 60` | neutral |
| 231 | 96 | `83 82 96 [21] 60` | par — noun |
| 359 | 11 | `47 11 [21] 62` | la — noun |
| 371 | 06 | `70 17 06 [21] 65` | neutral |
| 505 | 68 | `56 39 68 [21] 67` | neutral |
| 706 | 66 | `20 12 66 [21] 35` | neutral |
| 719 | 02 | `86 01 02 [21] 80` | **21 before A8 verb-frame 80 = subject slot → noun** |
| 850 | 62 | `96 40 62 [21] 67` | neutral |
| 937 | 33 | `26 00 33 [21] 64` | noun (nominal antecedent of qui) |
| 1064 | 96 | `83 82 96 [21] 62` | par — noun |
| 1162 | 83 | `82 44 83 [21] 67` | de — noun |
| 1172 | 83 | `94 87 83 [21] 85` | **de + 21 + A3 verb-stem 85: 21 in subject slot → noun** |
| 1207 | 61 | `43 55 61 [21] 65` | neutral (residual, suite-21-residuals owns) |
| 1304 | 43 | `37 08 43 [21] 43` | neutral |
| 1422 | 33 | `79 15 33 [21] 67` | neutral ("21 67" = noun + veut/et) |
| 1456 | 61 | `92 62 61 [21] 67` | neutral |
| 1463 | 01 | `79 17 01 [21] 62` | neutral |
| 1466 | 48 | `21 62 48 [21] 02` | neutral |
| 1529 | 46 | `96 87 46 [21] 65` | que — "que [21] [65] [63-verb]": subject NP → noun |
| 1538 | 06 | `41 62 06 [21] 62` | neutral |
| 1631 | 33 | `26 00 33 [21] 64` | noun (nominal antecedent of qui) |
| 1787 | 96 | `83 82 96 [21] 68` | par — noun |
| 1841 | 83 | `42 44 83 [21] 67` | de — noun |

- Exactly ONE verb-forcing governor in 30 windows: 64=qui at @134.
- The two verb-contact windows cut the wrong way: @719 "21 80" puts 21
  in the SUBJECT slot of the A8 verb-frame (noun leg, not a verb leg);
  @1172 "83 21 85" = "de [21] [85-verb]" puts 21 in subject slot (noun).
- The recurring "X 21 67" pattern (@115/@505/@850/@1162/@1422/@1456/
  @1841) is "21 + et/veut": with 67="veut" (follower infinitive-shaped
  per §7 rule) 21 is the subject; with 67="et" 21 is a coordinated noun.
  Neither reading puts 21 in a verb slot.

### C2 — "64 21" word-internal re-parse

- 64=qui contact census: 47 windows, preceded by 17, 03, 39, 56, 67, 87,
  09, 45, 03, 45, 67, 19, 94, 37, 54, 39, 03, 92, 65, 00, 77, 07, 51, 49,
  21, 92, 45, 78, 16, 57, 20, 71, 65, 37, 49, 37, 70, 21, 03, 84, 30, 87,
  87, 87, 69. Followed by 21 once (@133–134), by verbs/other nouns
  elsewhere (@338 `64 31`, @315 `64 59`, @1209 `64 59`...).
- In ALL 47 windows 64 behaves as a standalone word (granted 64=qui, §7).
  Zero windows show 64 word-internal or prefixal; the two "21 64" windows
  (@938/@1632) keep 64 as the standalone relative pronoun with 21 as its
  nominal antecedent (val-08 C4).
- A word-internal "64 21" re-parse would require qui to be a prefix at
  @133–134 while standing alone in the other 46 windows — no precedent,
  contradicts the grant. Not supportable at battery grade.

## Per-clause pass/fail

1. (C1) Second verb-frame 21 window found: **FAIL.** One "64 21" bigram in
   1,847 pairs (@133–134 only); the sole verb-forcing governor of 21 is
   @134 itself; both verb-contact windows (@719, @1172) place 21 in the
   subject slot.
2. (C2) "64 21" re-parses as word-internal: **FAIL.** 64=qui is standalone
   in all 47 windows; no word-internal precedent exists.
3. (C3) Fence the verb tension as unfounded: **FIRES.** Both positive arms
   test negative at grade.

## Adverses

- "5 noun legs for 21 stand": **ANSWERED** — re-verified byte-exact on the
  repaired stream: "par [21]" ×3 @231/@1064/@1787 (`96 21`), "[21] qui" ×2
  @937/@1631 (`33 21 64`); plus subject-slot windows @719/@1172/@1529.
- "@134 may be a '64 21' wordhood misread": **ANSWERED as unsupported** —
  the misread has no contact-profile support (C2 census above).

## Verdict: KILL

The proposition "21 has a battery-grade verb arm (split is real)" fails:
the single @134 leg finds no second leg in any of 21's 30 windows and no
wordhood rescue, so the bar's negative arm fires — **21's verb tension is
fenced as unfounded**. Consistent with §7 standing ("21 otherwise NOUN
battery grade") and val-21-reopen's closure of the battery-grade value
search. This is a tension closure, not a class/value verdict: 21=noun
(de-frame-21-class / val-08 C4) stands untouched; no red-team verdict
contradicted or downgraded; no new polyvalence declared (§5.2: a promote
was never available — it would contradict battery-promoted 21=noun).
No follow-ups from this kill: the @134 residual is already owned by queued
targets (suite-21-residuals, phase-a1_04-134, reopen-21-65-ratified) —
no duplication.

## Phase caveat (stated, not hidden)

@134's "64 21 65" trigram dissolves under a1_04's rival offset-0
(re-parses to "56 42 16 52 39 ..."; cited from val-21-reopen). a1_04's
repaired offset-1 is likelihood-favored per protocol, so all counts above
hold on the canonical stream — but the single leg is a canonical-offset
object, which is one more reason its tension does not survive to grade.

## Bookkeeping

- Report: code/crowd17/report_inbox/battery-verb-21-second-leg.md
- Queue: battery-queue.json → `verb-21-second-leg` status `verdict`,
  result `kill`, date 2026-10-09 (pre-write assert: was `queued`,
  verdictless; temp-file + rename; JSON re-validated; own entry only;
  no downgrade).
- Lock created on start, deleted on completion. `canonical.py` never used.
  R5005, sealed gates, red-team adjudication queue untouched.
